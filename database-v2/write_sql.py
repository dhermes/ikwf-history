# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3
from typing import NamedTuple, TypeVar

import pydantic

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


def _validate_division_sort_key():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        cursor.execute("SELECT id, key FROM division")
        division_rows = [dict(row) for row in cursor.fetchall()]
        cursor.close()

    for division_row in division_rows:
        actual_id = division_row["id"]
        division = division_row["key"]
        sort_id = bracket_utils.division_sort_key(division)
        if actual_id != sort_id:
            raise ValueError("Mismatch", division, actual_id, sort_id)


class BracketInfoTuple(NamedTuple):
    weight: int
    division: bracket_utils.Division
    tournament_id: int


class BracketInfo(_ForbidExtra):
    weight: int
    division: bracket_utils.Division
    tournament_id: int

    def as_tuple(self) -> BracketInfoTuple:
        """Convert to a (hashable) tuple."""
        return BracketInfoTuple(
            weight=self.weight, division=self.division, tournament_id=self.tournament_id
        )


class TeamRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name_normalized: str


class TournamentTeamRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    tournament_id: int
    division: bracket_utils.Division
    team_id: int
    team_score: float | None
    name: str
    acronym: str | None
    non_scoring: bool


class TeamPointDeductionRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    team_id: int
    reason: str
    amount: int


class CompetitorRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    full_name_normalized: str


class TournamentCompetitorRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    competitor_id: int
    team_id: int
    full_name: str
    first_name: str
    last_name: str


class MatchRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    bracket_id: int
    bout_number: int | None
    match_slot: bracket_utils.MatchSlot
    top_competitor_id: int
    bottom_competitor_id: int
    top_win: bool | None
    result: str
    result_type: bracket_utils.ResultType
    top_score: int | None
    bottom_score: int | None
    match_time_minutes: int | None
    match_time_seconds: int | None


class InsertIDs(_ForbidExtra):
    next_team_id: int
    next_tournament_team_id: int
    next_team_point_deduction_id: int
    next_competitor_id: int
    next_tournament_competitor_id: int
    next_match_id: int


class Inserts(_ForbidExtra):
    team_rows: list[TeamRow]
    tournament_team_rows: list[TournamentTeamRow]
    team_point_deduction_rows: list[TeamPointDeductionRow]
    competitor_rows: list[CompetitorRow]
    tournament_competitor_rows: list[TournamentCompetitorRow]
    match_rows: list[MatchRow]


K = TypeVar("K")
V = TypeVar("V")


def _insert_only(data: dict[K, V], key: K, value: V) -> None:
    if key in data:
        raise KeyError("Duplicate", key, data[key], value)
    data[key] = value


def _insert_check(data: dict[K, V], key: K, value: V) -> None:
    if key in data:
        if data[key] != value:
            raise KeyError("Conflict", key, data[key], value)
    else:
        data[key] = value


def _build_team_maps(
    extracted: bracket_utils.ExtractedTournament,
) -> tuple[
    dict[bracket_utils.Division, dict[str, str]],
    dict[bracket_utils.Division, dict[str, str | None]],
]:
    by_acronym: dict[bracket_utils.Division, dict[str, str]] = {}
    by_name: dict[bracket_utils.Division, dict[str, str | None]] = {}

    # 1. Team name / acronyms from team scores
    for division, team_scores in extracted.team_scores.items():
        by_acronym.setdefault(division, {})
        by_name.setdefault(division, {})

        for team_score in team_scores:
            _insert_only(by_name[division], team_score.team, team_score.acronym)
            if team_score.acronym is not None:
                _insert_only(by_acronym[division], team_score.acronym, team_score.team)

    # 2. Team name / acronyms from match entries (athletes)
    for weight_class in extracted.weight_classes:
        division = weight_class.division
        division_by_acronym = by_acronym.setdefault(division, {})
        division_by_name = by_name.setdefault(division, {})

        for match in weight_class.matches:
            competitors: list[bracket_utils.Competitor] = []
            if match.top_competitor is not None:
                competitors.append(match.top_competitor)
            if match.bottom_competitor is not None:
                competitors.append(match.bottom_competitor)

            for competitor in competitors:
                team_full = competitor.team_full
                team_acronym = competitor.team_acronym
                _insert_check(division_by_name, team_full, team_acronym)
                if team_acronym is not None:
                    _insert_check(division_by_acronym, team_acronym, team_full)

    return by_acronym, by_name


def _team_score_for_name(
    division: bracket_utils.Division,
    name: str,
    extracted: bracket_utils.ExtractedTournament,
) -> float | None:
    # NOTE: This could be sped up if we find the computation is taking too long.
    team_scores = extracted.team_scores.get(division, [])
    matches: list[bracket_utils.TeamScore] = []
    for team_score in team_scores:
        if team_score.team == name:
            matches.append(team_score)

    if len(matches) == 1:
        return matches[0].score

    if len(matches) > 1:
        raise RuntimeError("Invariant violation", division, matches)

    return None


def _is_non_scoring(
    tournament_id: int, division: bracket_utils.Division, name: str
) -> bool:
    return False


def _match_deduction(
    team_name: str,
    divisions: list[bracket_utils.Division],
    tournament_teams: list[TournamentTeamRow],
) -> list[int]:
    # NOTE: We **could** pre-process `tournament_teams` to a dictionary to
    #       increase this lookup speed. However we expect it to be small enough
    #       so just iterate over the full list.
    matches: dict[bracket_utils.Division, list[int]] = {}
    for tournament_team in tournament_teams:
        if tournament_team.name == team_name:
            matches.setdefault(tournament_team.division, []).append(tournament_team.id_)

    if set(matches.keys()) != set(divisions):
        raise ValueError("Did not match all divisions", divisions, matches.keys())

    result: list[int] = []
    for division, team_ids in matches.items():
        if len(team_ids) != 1:
            raise ValueError("Non-unique match for division", division, team_ids)
        result.append(team_ids[0])

    return result


def _add_team_rows(
    tournament_id: int,
    insert_ids: InsertIDs,
    inserts: Inserts,
    team_by_name: dict[bracket_utils.Division, dict[str, str | None]],
    extracted: bracket_utils.ExtractedTournament,
):
    # 1. `TeamRow` (allow duplicates across year and division)
    # 2. `TournamentTeamRow`
    tournament_teams: list[TournamentTeamRow] = []

    divisions = sorted(team_by_name.keys(), key=bracket_utils.division_sort_key)
    for division in divisions:
        teams = team_by_name[division]
        team_names = sorted(teams.keys())
        for team_name in team_names:
            acronym = teams[team_name]

            team_id = insert_ids.next_team_id
            inserts.team_rows.append(TeamRow(id=team_id, name_normalized=team_name))
            insert_ids.next_team_id += 1

            tournament_team_row = TournamentTeamRow(
                id=insert_ids.next_tournament_team_id,
                tournament_id=tournament_id,
                division=division,
                team_id=team_id,
                team_score=_team_score_for_name(division, team_name, extracted),
                name=team_name,
                acronym=acronym,
                non_scoring=_is_non_scoring(tournament_id, division, team_name),
            )
            inserts.tournament_team_rows.append(tournament_team_row)
            tournament_teams.append(tournament_team_row)
            insert_ids.next_tournament_team_id += 1

    # 3. `TeamPointDeductionRow`
    for deduction in extracted.deductions:
        amount_float = deduction.value
        amount = -int(amount_float)
        if amount != -amount_float:
            raise ValueError("Deductions are expected to be integer", deduction.value)
        if amount <= 0:
            raise ValueError("Deductions are expected to be negative", deduction.value)

        # Ensure team is in all divisions (because deductions apply across all
        # divisions)
        team_ids = _match_deduction(deduction.team, divisions, tournament_teams)
        for team_id in team_ids:
            deduction_id = insert_ids.next_team_point_deduction_id
            inserts.team_point_deduction_rows.append(
                TeamPointDeductionRow(
                    id=deduction_id,
                    team_id=team_id,
                    reason=deduction.reason,
                    amount=amount,
                )
            )
            insert_ids.next_team_point_deduction_id += 1


def _handle_tournament(
    year: int,
    tournament_id: int,
    insert_ids: InsertIDs,
    inserts: Inserts,
    bracket_id_info: dict[BracketInfoTuple, int],
    extracted: bracket_utils.ExtractedTournament,
) -> InsertIDs:
    team_by_acronym, team_by_name = _build_team_maps(extracted)
    _add_team_rows(tournament_id, insert_ids, inserts, team_by_name, extracted)

    # 4. `CompetitorRow` (allow duplicates across year)
    # 5. `TournamentCompetitorRow`
    # 6. `MatchRow`

    return insert_ids


def _handle_year(
    extracted_dir: pathlib.Path,
    year: int,
    insert_ids: InsertIDs,
    inserts: Inserts,
    filenames: dict[int, str],
    bracket_id_info: dict[BracketInfoTuple, int],
) -> InsertIDs:
    for tournament_id, filename in filenames.items():
        with open(extracted_dir / filename) as file_obj:
            extracted = bracket_utils.ExtractedTournament.model_validate_json(
                file_obj.read()
            )

        insert_ids = _handle_tournament(
            year, tournament_id, insert_ids, inserts, bracket_id_info, extracted
        )

        # NOTE: We round-trip the file back to ensure it is formatted correctly
        with open(extracted_dir / filename, "w") as file_obj:
            file_obj.write(extracted.model_dump_json(indent=2))
            file_obj.write("\n")

    return insert_ids


def _write_brackets_sql() -> dict[BracketInfoTuple, int]:
    with open(HERE / "_weight-classes.json") as file_obj:
        weight_classes = bracket_utils.WeightClassesByYear.model_validate_json(
            file_obj.read()
        )

    lines = [
        "-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.",
        "",
        "-- Generated by `write_sql.py`",
        "",
        "PRAGMA foreign_keys = ON;",
        "PRAGMA encoding = 'UTF-8';",
        "PRAGMA integrity_check;",
        "",
        "--------------------------------------------------------------------------------",
        "",
        "INSERT INTO",
        "  bracket (id, weight, division, tournament_id)",
        "VALUES",
    ]

    result: dict[BracketInfo, int] = {}

    years = sorted(weight_classes.root.keys())
    current_id = 1
    for i, year in enumerate(years):
        last_i = i == len(years) - 1
        by_tournament = weight_classes.root[year]
        tournament_ids = sorted(by_tournament.keys())
        for j, tournament_id in enumerate(tournament_ids):
            last_j = j == len(tournament_ids) - 1
            by_division = by_tournament[tournament_id]
            divisions = sorted(by_division.keys(), key=bracket_utils.division_sort_key)
            for k, division in enumerate(divisions):
                last_k = k == len(divisions) - 1
                weights = by_division[division]
                for l, weight in enumerate(weights):
                    last_l = l == len(weights) - 1
                    last_line = last_i and last_j and last_k and last_l
                    line_ending = ";" if last_line else ","

                    lines.append(
                        f"  ({current_id}, {weight}, '{division}', "
                        f"{tournament_id}){line_ending}"
                    )

                    info = BracketInfo(
                        weight=weight, division=division, tournament_id=tournament_id
                    )
                    key = info.as_tuple()
                    if key in result:
                        raise KeyError("Duplicate", key)
                    result[key] = current_id

                    # Prepare for next iteration
                    current_id += 1

    lines.append("")

    with open(HERE / "migrations" / "0004-brackets.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))

    return result


def _get_filenames_by_year() -> dict[int, bracket_utils.TournamentFilename]:
    with open(HERE / "_filenames-by-year.json") as file_obj:
        loaded = bracket_utils.FilenamesByYear.model_validate_json(file_obj.read())

    return loaded.root


def _sql_nullable_str(value: str | None) -> str:
    if value is None:
        return "NULL"

    quoted = value.replace("'", "''")
    return f"'{quoted}'"


def _sql_nullable_float(value: float | None) -> str:
    if value is None:
        return "NULL"

    return str(value)


def _sql_bool_str(value: bool) -> str:
    if value:
        return "TRUE"
    return "FALSE"


def _write_teams_sql(inserts: Inserts) -> None:
    lines = [
        "-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.",
        "",
        "-- Generated by `write_sql.py`",
        "",
        "PRAGMA foreign_keys = ON;",
        "PRAGMA encoding = 'UTF-8';",
        "PRAGMA integrity_check;",
        "",
        "--------------------------------------------------------------------------------",
        "",
        "INSERT INTO",
        "  team (id, name_normalized)",
        "VALUES",
    ]

    insert_rows = inserts.team_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        name_str = _sql_nullable_str(row.name_normalized)
        lines.append(f"  ({row.id_}, {name_str}){line_ending}")

    lines.append("")

    with open(HERE / "migrations" / "0005-teams.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def _write_tournament_teams_sql(inserts: Inserts) -> None:
    lines = [
        "-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.",
        "",
        "-- Generated by `write_sql.py`",
        "",
        "PRAGMA foreign_keys = ON;",
        "PRAGMA encoding = 'UTF-8';",
        "PRAGMA integrity_check;",
        "",
        "--------------------------------------------------------------------------------",
        "",
        "INSERT INTO",
        "  tournament_team (id, tournament_id, division, team_id, team_score, name, acronym, non_scoring)",
        "VALUES",
    ]

    insert_rows = inserts.tournament_team_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        division_str = _sql_nullable_str(row.division)
        score_str = _sql_nullable_float(row.team_score)
        name_str = _sql_nullable_str(row.name)
        acronym_str = _sql_nullable_str(row.acronym)
        non_scoring_str = _sql_bool_str(row.non_scoring)
        lines.append(
            f"  ({row.id_}, {row.tournament_id}, {division_str}, {row.team_id}, "
            f"{score_str}, {name_str}, {acronym_str}, {non_scoring_str}){line_ending}"
        )

    lines.append("")

    with open(HERE / "migrations" / "0006-tournament-teams.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def _write_team_point_deductions_sql(inserts: Inserts) -> None:
    lines = [
        "-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.",
        "",
        "-- Generated by `write_sql.py`",
        "",
        "PRAGMA foreign_keys = ON;",
        "PRAGMA encoding = 'UTF-8';",
        "PRAGMA integrity_check;",
        "",
        "--------------------------------------------------------------------------------",
        "",
        "INSERT INTO",
        "  team_point_deduction (id, team_id, reason, amount)",
        "VALUES",
    ]

    insert_rows = inserts.team_point_deduction_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        reason_str = _sql_nullable_str(row.reason)
        lines.append(
            f"  ({row.id_}, {row.team_id}, {reason_str}, {row.amount}){line_ending}"
        )

    lines.append("")

    with open(HERE / "migrations" / "0007-team-point-deductions.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def main():
    _validate_division_sort_key()
    bracket_id_info = _write_brackets_sql()

    extracted_dir = HERE.parent / "intermediate-data"
    filenames_by_year = _get_filenames_by_year()

    insert_ids = InsertIDs(
        next_team_id=1,
        next_tournament_team_id=1,
        next_team_point_deduction_id=1,
        next_competitor_id=1,
        next_tournament_competitor_id=1,
        next_match_id=1,
    )
    inserts = Inserts(
        team_rows=[],
        tournament_team_rows=[],
        team_point_deduction_rows=[],
        competitor_rows=[],
        tournament_competitor_rows=[],
        match_rows=[],
    )
    for year, filenames in filenames_by_year.items():
        insert_ids = _handle_year(
            extracted_dir, year, insert_ids, inserts, filenames, bracket_id_info
        )

    _write_teams_sql(inserts)
    _write_tournament_teams_sql(inserts)
    _write_team_point_deductions_sql(inserts)


if __name__ == "__main__":
    main()
