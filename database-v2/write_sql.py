# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3
from typing import Literal, NamedTuple, TypeVar

import bracket_utils
import match_scores
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
_MAX_MATCH_ID = 54
_MAX_PLACEMENT = 8


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


def _validate_get_match_slot_id():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        cursor.execute("SELECT id, key FROM match_slot")
        match_slot_rows = [dict(row) for row in cursor.fetchall()]
        cursor.close()

    for match_slot_row in match_slot_rows:
        actual_id = match_slot_row["id"]
        match_slot = match_slot_row["key"]
        match_slot_id = bracket_utils.get_match_slot_id(match_slot)
        if actual_id != match_slot_id:
            raise ValueError("Mismatch", match_slot, actual_id, match_slot_id)


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
    url_path_slug: str | None


class TournamentTeamRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    tournament_id: int
    division: bracket_utils.Division
    team_id: int
    team_score: float | None
    name: str


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
    top_competitor_id: int | None
    bottom_competitor_id: int | None
    top_win: bool | None
    result: str
    result_type: bracket_utils.ResultType
    top_score: int | None
    bottom_score: int | None
    match_time_minutes: int | None
    match_time_seconds: int | None


class PlacerDenormalizedRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    tournament_id: int
    division: bracket_utils.Division
    weight: int
    competitor_id: int
    place: Literal[1, 2, 3, 4, 5, 6, 7, 8]


class InsertIDs(_ForbidExtra):
    next_team_id: int
    next_tournament_team_id: int
    next_team_point_deduction_id: int
    next_competitor_id: int
    next_tournament_competitor_id: int
    next_match_id: int
    next_placer_denormalized_id: int


class Inserts(_ForbidExtra):
    team_rows: list[TeamRow]
    tournament_team_rows: list[TournamentTeamRow]
    team_point_deduction_rows: list[TeamPointDeductionRow]
    competitor_rows: list[CompetitorRow]
    tournament_competitor_rows: list[TournamentCompetitorRow]
    match_rows: list[MatchRow]
    placer_denormalized_rows: list[PlacerDenormalizedRow]


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


def _map_team_names(
    extracted: bracket_utils.ExtractedTournament,
) -> dict[bracket_utils.Division, dict[str, bool]]:
    all_names: dict[bracket_utils.Division, dict[str, bool]] = {}

    # 1. Team names from team scores
    for division, team_scores in extracted.team_scores.items():
        division_by_name = all_names.setdefault(division, {})
        for team_score in team_scores:
            division_by_name[team_score.team] = True

    # 2. Team names from match entries (athletes)
    for weight_class in extracted.weight_classes:
        division = weight_class.division
        division_by_name = all_names.setdefault(division, {})

        for match in weight_class.matches:
            competitors: list[bracket_utils.Competitor] = []
            if match.top_competitor is not None:
                competitors.append(match.top_competitor)
            if match.bottom_competitor is not None:
                competitors.append(match.bottom_competitor)

            for competitor in competitors:
                division_by_name[competitor.team_full] = True

    return all_names


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


def _match_deduction(
    team_name: str,
    divisions: list[bracket_utils.Division],
    team_id_map: dict[bracket_utils.Division, dict[str, int]],
    tournament_synonyms: list[bracket_utils.TeamNameSynonym],
) -> list[int]:
    all_synonyms: set[str] = set([team_name])
    for tournament_synonym in tournament_synonyms:
        if tournament_synonym.name == team_name:
            all_synonyms.add(tournament_synonym.synonym)

    matches: dict[bracket_utils.Division, list[int]] = {}
    for division, division_teams in team_id_map.items():
        for team_name in all_synonyms:
            if team_name not in division_teams:
                continue

            matches.setdefault(division, []).append(division_teams[team_name])

    if set(matches.keys()) != set(divisions):
        raise ValueError(
            "Did not match all divisions", team_name, divisions, matches.keys()
        )

    result: list[int] = []
    for division, team_ids in matches.items():
        if len(team_ids) != 1:
            raise ValueError(
                "Non-unique match for division", team_name, division, team_ids
            )
        result.append(team_ids[0])

    return result


def _deductions_sort_key(deduction: bracket_utils.Deduction):
    return deduction.team, deduction.reason, deduction.value


def _add_team_rows(
    tournament_id: int,
    insert_ids: InsertIDs,
    inserts: Inserts,
    team_names_map: dict[bracket_utils.Division, dict[str, bool]],
    extracted: bracket_utils.ExtractedTournament,
    team_name_synonyms: dict[int, list[bracket_utils.TeamNameSynonym]],
) -> dict[bracket_utils.Division, dict[str, int]]:
    team_id_map: dict[bracket_utils.Division, dict[str, int]] = {}

    # 1. `TeamRow` (allow duplicates across year and division)
    # 2. `TournamentTeamRow`
    divisions = sorted(team_names_map.keys(), key=bracket_utils.division_sort_key)
    for division in divisions:
        team_id_map.setdefault(division, {})

        teams = team_names_map[division]
        team_names = sorted(teams.keys())
        for team_name in team_names:
            team_id = insert_ids.next_team_id
            inserts.team_rows.append(
                TeamRow(id=team_id, name_normalized=team_name, url_path_slug=None)
            )
            insert_ids.next_team_id += 1

            tournament_team_row = TournamentTeamRow(
                id=insert_ids.next_tournament_team_id,
                tournament_id=tournament_id,
                division=division,
                team_id=team_id,
                team_score=_team_score_for_name(division, team_name, extracted),
                name=team_name,
            )
            inserts.tournament_team_rows.append(tournament_team_row)
            insert_ids.next_tournament_team_id += 1

            _insert_only(team_id_map[division], team_name, tournament_team_row.id_)

    # 3. `TeamPointDeductionRow`
    tournament_synonyms = team_name_synonyms.get(tournament_id, [])
    sorted_deductions = sorted(extracted.deductions, key=_deductions_sort_key)
    for deduction in sorted_deductions:
        amount_float = deduction.value
        amount = -int(amount_float)
        if amount != -amount_float:
            raise ValueError("Deductions are expected to be integer", deduction.value)
        if amount <= 0:
            raise ValueError("Deductions are expected to be negative", deduction.value)

        # Ensure team is in all divisions (because deductions apply across all
        # divisions)
        team_ids = _match_deduction(
            deduction.team, divisions, team_id_map, tournament_synonyms
        )
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

    return team_id_map


def _get_match_map(
    weight_class: bracket_utils.WeightClass,
) -> dict[int, bracket_utils.Match]:
    result: dict[int, bracket_utils.Match] = {}
    for match in weight_class.matches:
        match_slot_id = bracket_utils.get_match_slot_id(match.match_slot)
        _insert_only(result, match_slot_id, match)

    return result


class CompetitorTuple(NamedTuple):
    """Simple hashable type used to find unique competitors in a bracket."""

    full_name: str
    first_name: str
    last_name: str
    team: str


BracketPosition = Literal["top", "bottom"]


def _to_competitor_tuple(competitor: bracket_utils.Competitor) -> CompetitorTuple:
    return CompetitorTuple(
        full_name=competitor.full_name,
        first_name=competitor.first_name,
        last_name=competitor.last_name,
        team=competitor.team_full,
    )


def _get_competitor_tuple(
    match: bracket_utils.Match, bracket_position: BracketPosition
) -> CompetitorTuple | None:
    if bracket_position == "top":
        if match.top_competitor is not None:
            return _to_competitor_tuple(match.top_competitor)
    elif bracket_position == "bottom":
        if match.bottom_competitor is not None:
            return _to_competitor_tuple(match.bottom_competitor)
    else:
        raise NotImplementedError(bracket_position)

    return None


def _maybe_add_competitor_tuple(
    match: bracket_utils.Match,
    bracket_position: BracketPosition,
    competitor_map: dict[CompetitorTuple, int],
) -> None:
    competitor_tuple = _get_competitor_tuple(match, bracket_position)
    if competitor_tuple is None:
        return

    if competitor_tuple in competitor_map:
        return

    competitor_id = len(competitor_map)
    competitor_map[competitor_tuple] = competitor_id
    if len(set(competitor_map.values())) != len(competitor_map):
        raise ValueError("Duplicate competitor (tuple) IDs", competitor_map)


def _get_competitor_map(
    match_map: dict[int, bracket_utils.Match],
) -> dict[CompetitorTuple, int]:
    result: dict[CompetitorTuple, int] = {}

    # Only consider competitors from the championship side **FIRST**
    # (where the match ordering is somewhat reliable)
    for match_slot_id in range(1, _MAX_MATCH_ID + 1):
        match = match_map.get(match_slot_id)
        if match is None:
            continue

        if not match.match_slot.startswith("championship_"):
            continue

        _maybe_add_competitor_tuple(match, "top", result)
        _maybe_add_competitor_tuple(match, "bottom", result)

    # Now consider competitors from the consolation and place matches
    # (e.g. for 1999 where we have partial brackets)
    for match_slot_id in range(1, _MAX_MATCH_ID + 1):
        match = match_map.get(match_slot_id)
        if match is None:
            continue

        if match.match_slot.startswith("championship_"):
            continue

        _maybe_add_competitor_tuple(match, "top", result)
        _maybe_add_competitor_tuple(match, "bottom", result)

    if len(result) > 24:
        raise RuntimeError("Unexpected competitor (tuple) map")

    return result


def _handle_weight_class(
    tournament_id: int,
    bracket_id: int,
    weight_class: bracket_utils.WeightClass,
    team_id_map: dict[str, int],
    insert_ids: InsertIDs,
    inserts: Inserts,
):
    match_map = _get_match_map(weight_class)
    competitor_map = _get_competitor_map(match_map)

    competitors_by_id = {
        local_id: competitor_tuple
        for competitor_tuple, local_id in competitor_map.items()
    }
    if len(competitors_by_id) != len(competitor_map):
        raise ValueError("Duplicate local IDs")

    local_to_global: dict[int, int] = {}
    local_ids = sorted(competitors_by_id.keys())
    # 4. `CompetitorRow` (allow duplicates across years)
    # 5. `TournamentCompetitorRow`
    for local_id in local_ids:
        competitor_tuple = competitors_by_id[local_id]
        competitor_row = CompetitorRow(
            id=insert_ids.next_competitor_id,
            full_name_normalized=competitor_tuple.full_name,
        )
        inserts.competitor_rows.append(competitor_row)
        insert_ids.next_competitor_id += 1

        team_id = team_id_map[competitor_tuple.team]
        tournament_competitor_row = TournamentCompetitorRow(
            id=insert_ids.next_tournament_competitor_id,
            competitor_id=competitor_row.id_,
            team_id=team_id,
            full_name=competitor_row.full_name_normalized,
            first_name=competitor_tuple.first_name,
            last_name=competitor_tuple.last_name,
        )
        inserts.tournament_competitor_rows.append(tournament_competitor_row)
        _insert_only(local_to_global, local_id, tournament_competitor_row.id_)
        insert_ids.next_tournament_competitor_id += 1

    # 6. `MatchRow`
    # place => competitor_id
    placers: dict[int, int | None] = {}
    for match_slot_id in range(1, _MAX_MATCH_ID + 1):
        match = match_map.get(match_slot_id)
        if match is None:
            continue

        top_competitor_id = None
        bottom_competitor_id = None

        if match.top_competitor is not None:
            competitor_tuple = _to_competitor_tuple(match.top_competitor)
            local_id = competitor_map[competitor_tuple]
            top_competitor_id = local_to_global[local_id]

        if match.bottom_competitor is not None:
            competitor_tuple = _to_competitor_tuple(match.bottom_competitor)
            local_id = competitor_map[competitor_tuple]
            bottom_competitor_id = local_to_global[local_id]

        if top_competitor_id is None and bottom_competitor_id is None:
            # NOTE: In some brackets (e.g. in 2000), there are less than 24
            #       athletes and in earlier rounds we have parsed matches with
            #       a valid bout number but no competitors.
            if match.top_win is not None:
                raise NotImplementedError("Invalid match", match)
            if match.result_type != "bye":
                raise NotImplementedError("Invalid match", match)
            continue

        top_score = None
        bottom_score = None
        scores = match_scores.parse_scores(match.result, match.top_win)
        if scores is not None:
            top_score, bottom_score = scores

        if match.top_win is None:
            winner_competitor_id = None
            loser_competitor_id = None
        elif match.top_win:
            winner_competitor_id = top_competitor_id
            loser_competitor_id = bottom_competitor_id
        else:
            winner_competitor_id = bottom_competitor_id
            loser_competitor_id = top_competitor_id

        if match.match_slot == "championship_first_place":
            _insert_only(placers, 1, winner_competitor_id)
            _insert_only(placers, 2, loser_competitor_id)
        elif match.match_slot == "consolation_third_place":
            _insert_only(placers, 3, winner_competitor_id)
            _insert_only(placers, 4, loser_competitor_id)
        elif match.match_slot == "consolation_fifth_place":
            _insert_only(placers, 5, winner_competitor_id)
            _insert_only(placers, 6, loser_competitor_id)
        elif match.match_slot == "consolation_seventh_place":
            _insert_only(placers, 7, winner_competitor_id)
            _insert_only(placers, 8, loser_competitor_id)

        match_row = MatchRow(
            id=insert_ids.next_match_id,
            bracket_id=bracket_id,
            bout_number=match.bout_number,
            match_slot=match.match_slot,
            top_competitor_id=top_competitor_id,
            bottom_competitor_id=bottom_competitor_id,
            top_win=match.top_win,
            result=match.result,
            result_type=match.result_type,
            top_score=top_score,
            bottom_score=bottom_score,
            match_time_minutes=None,
            match_time_seconds=None,
        )
        inserts.match_rows.append(match_row)
        insert_ids.next_match_id += 1

    # 7. `PlacerDenormalizedRow`
    for place in range(1, _MAX_PLACEMENT + 1):
        competitor_id = placers.get(place)
        if competitor_id is None:
            continue

        placer_denormalized_row = PlacerDenormalizedRow(
            id=insert_ids.next_placer_denormalized_id,
            tournament_id=tournament_id,
            division=weight_class.division,
            weight=weight_class.weight,
            competitor_id=competitor_id,
            place=place,
        )
        inserts.placer_denormalized_rows.append(placer_denormalized_row)
        insert_ids.next_placer_denormalized_id += 1


def _handle_tournament(
    year: int,
    tournament_id: int,
    insert_ids: InsertIDs,
    inserts: Inserts,
    bracket_id_info: dict[BracketInfoTuple, int],
    extracted: bracket_utils.ExtractedTournament,
    team_name_synonyms: dict[int, list[bracket_utils.TeamNameSynonym]],
) -> InsertIDs:
    team_names_map = _map_team_names(extracted)
    team_id_map = _add_team_rows(
        tournament_id,
        insert_ids,
        inserts,
        team_names_map,
        extracted,
        team_name_synonyms,
    )

    for weight_class in extracted.weight_classes:
        key = weight_class.weight, weight_class.division, tournament_id
        bracket_id = bracket_id_info[key]
        division_team_id_map = team_id_map[weight_class.division]
        _handle_weight_class(
            tournament_id,
            bracket_id,
            weight_class,
            division_team_id_map,
            insert_ids,
            inserts,
        )

    return insert_ids


def _handle_year(
    extracted_dir: pathlib.Path,
    year: int,
    insert_ids: InsertIDs,
    inserts: Inserts,
    filenames: dict[int, str],
    bracket_id_info: dict[BracketInfoTuple, int],
    team_name_synonyms: dict[int, list[bracket_utils.TeamNameSynonym]],
) -> InsertIDs:
    for tournament_id, filename in filenames.items():
        with open(extracted_dir / filename) as file_obj:
            extracted = bracket_utils.ExtractedTournament.model_validate_json(
                file_obj.read()
            )

        insert_ids = _handle_tournament(
            year,
            tournament_id,
            insert_ids,
            inserts,
            bracket_id_info,
            extracted,
            team_name_synonyms,
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
    for index1, year in enumerate(years):
        last1 = index1 == len(years) - 1
        by_tournament = weight_classes.root[year]
        tournament_ids = sorted(by_tournament.keys())
        for index2, tournament_id in enumerate(tournament_ids):
            last2 = index2 == len(tournament_ids) - 1
            by_division = by_tournament[tournament_id]
            divisions = sorted(by_division.keys(), key=bracket_utils.division_sort_key)
            for index3, division in enumerate(divisions):
                last3 = index3 == len(divisions) - 1
                weights = by_division[division]
                for index4, weight in enumerate(weights):
                    last4 = index4 == len(weights) - 1
                    last_line = last1 and last2 and last3 and last4
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


def _get_team_name_synonyms() -> dict[int, list[bracket_utils.TeamNameSynonym]]:
    with open(HERE / "_team-name-synonyms.json") as file_obj:
        loaded = bracket_utils.TeamNameSynonyms.model_validate_json(file_obj.read())

    return loaded.root


def _get_team_name_duplicates() -> list[bracket_utils.VerifiedTeam]:
    with open(HERE / "_team-name-duplicates.json") as file_obj:
        loaded = bracket_utils.TeamDuplicates.model_validate_json(file_obj.read())

    return loaded.root


def _sql_nullable_str(value: str | None) -> str:
    if value is None:
        return "NULL"

    quoted = value.replace("'", "''")
    return f"'{quoted}'"


def _sql_nullable_numeric(value: float | int | None) -> str:
    if value is None:
        return "NULL"

    return str(value)


def _sql_nullable_bool(value: bool | None) -> str:
    if value is None:
        return "NULL"

    if value:
        return "TRUE"

    return "FALSE"


def _validate_brackets(match_rows: list[MatchRow]) -> None:
    by_bracket: dict[int, list[MatchRow]] = {}
    for match_row in match_rows:
        by_bracket.setdefault(match_row.bracket_id, []).append(match_row)

    # TODO


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
        "  team (id, name_normalized, url_path_slug)",
        "VALUES",
    ]

    insert_rows = inserts.team_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        name_str = _sql_nullable_str(row.name_normalized)
        slug_str = _sql_nullable_bool(row.url_path_slug)
        lines.append(f"  ({row.id_}, {name_str}, {slug_str}){line_ending}")

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
        "  tournament_team (id, tournament_id, division, team_id, team_score, name)",  # noqa: E501
        "VALUES",
    ]

    insert_rows = inserts.tournament_team_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        division_str = _sql_nullable_str(row.division)
        score_str = _sql_nullable_numeric(row.team_score)
        name_str = _sql_nullable_str(row.name)
        lines.append(
            f"  ({row.id_}, {row.tournament_id}, {division_str}, {row.team_id}, "
            f"{score_str}, {name_str}){line_ending}"
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


def _write_competitors_sql(inserts: Inserts) -> None:
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
        "  competitor (id, full_name_normalized)",
        "VALUES",
    ]

    insert_rows = inserts.competitor_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        full_name_str = _sql_nullable_str(row.full_name_normalized)
        lines.append(f"  ({row.id_}, {full_name_str}){line_ending}")

    lines.append("")

    with open(HERE / "migrations" / "0008-competitors.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def _write_tournament_competitors_sql(inserts: Inserts) -> None:
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
        "  tournament_competitor (id, competitor_id, team_id, full_name, first_name, last_name)",  # noqa: E501
        "VALUES",
    ]

    insert_rows = inserts.tournament_competitor_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        full_name_str = _sql_nullable_str(row.full_name)
        first_name_str = _sql_nullable_str(row.first_name)
        last_name_str = _sql_nullable_str(row.last_name)
        lines.append(
            f"  ({row.id_}, {row.competitor_id}, {row.team_id}, "
            f"{full_name_str}, {first_name_str}, {last_name_str}){line_ending}"
        )

    lines.append("")

    with open(HERE / "migrations" / "0009-tournament-competitors.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def _write_matches_sql(inserts: Inserts) -> None:
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
        "  match (id, bracket_id, bout_number, match_slot, top_competitor_id, bottom_competitor_id, top_win, result, result_type, top_score, bottom_score, match_time_minutes, match_time_seconds)",  # noqa: E501
        "VALUES",
    ]

    insert_rows = inserts.match_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        bout_number_str = _sql_nullable_numeric(row.bout_number)
        match_slot_str = _sql_nullable_str(row.match_slot)
        top_competitor_str = _sql_nullable_numeric(row.top_competitor_id)
        bottom_competitor_str = _sql_nullable_numeric(row.bottom_competitor_id)
        top_win_str = _sql_nullable_bool(row.top_win)
        result_str = _sql_nullable_str(row.result)
        result_type_str = _sql_nullable_str(row.result_type)
        top_score_str = _sql_nullable_numeric(row.top_score)
        bottom_score_str = _sql_nullable_numeric(row.bottom_score)
        minutes_str = _sql_nullable_numeric(row.match_time_minutes)
        seconds_str = _sql_nullable_numeric(row.match_time_seconds)
        lines.append(
            f"  ({row.id_}, {row.bracket_id}, {bout_number_str}, {match_slot_str}, "
            f"{top_competitor_str}, {bottom_competitor_str}, {top_win_str}, "
            f"{result_str}, {result_type_str}, {top_score_str}, {bottom_score_str}, "
            f"{minutes_str}, {seconds_str}){line_ending}"
        )

    lines.append("")

    with open(HERE / "migrations" / "0010-matches.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def _write_placers_denormalized_sql(inserts: Inserts) -> None:
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
        "  placer_denormalized (id, tournament_id, division, weight, competitor_id, place)",  # noqa: E501
        "VALUES",
    ]

    insert_rows = inserts.placer_denormalized_rows
    for i, row in enumerate(insert_rows):
        last_i = i == len(insert_rows) - 1
        line_ending = ";" if last_i else ","
        division_str = _sql_nullable_str(row.division)
        lines.append(
            f"  ({row.id_}, {row.tournament_id}, {division_str}, {row.weight}, "
            f"{row.competitor_id}, {row.place}){line_ending}"
        )

    lines.append("")

    with open(HERE / "migrations" / "0011-placers-denormalized.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def _verified_team_sort_key(team: bracket_utils.VerifiedTeam) -> str:
    return team.name_normalized


def _write_team_deduplicate_sql(
    inserts: Inserts, team_name_duplicates: list[bracket_utils.VerifiedTeam]
) -> None:
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
    ]

    team_name_duplicates = sorted(team_name_duplicates, key=_verified_team_sort_key)
    for verified_team in team_name_duplicates:
        team_name = verified_team.name_normalized
        duplicates = verified_team.duplicates
        if len(duplicates) < 2:
            raise ValueError("Need at least 2 duplicates", team_name)

        keep_tuples = set(duplicate.to_tuple() for duplicate in duplicates)
        if len(keep_tuples) != len(duplicates):
            raise ValueError("Invalid duplicates", team_name)

        duplicated_rows = [
            row
            for row in inserts.tournament_team_rows
            if (row.tournament_id, row.division, row.name) in keep_tuples
        ]
        if len(duplicated_rows) != len(keep_tuples):
            duplicated_row_tuples = [
                (row.tournament_id, row.division, row.name) for row in duplicated_rows
            ]
            missing = set(keep_tuples) - set(duplicated_row_tuples)
            raise ValueError("Some duplicates not matched", team_name, missing)

        keep_team_id = min(
            tournament_team.team_id for tournament_team in duplicated_rows
        )
        delete_team_ids = sorted(
            tournament_team.team_id
            for tournament_team in duplicated_rows
            if tournament_team.team_id != keep_team_id
        )
        delete_predicate = ", ".join(map(str, delete_team_ids))
        merge_tournament_team_ids = sorted(
            tournament_team.id_ for tournament_team in duplicated_rows
        )
        merge_predicate = ", ".join(map(str, merge_tournament_team_ids))
        team_name_str = _sql_nullable_str(team_name)
        slug_str = _sql_nullable_str(verified_team.url_path_slug)
        lines.extend(
            [
                "-" * 40,
                f"-- {team_name}",
                "",
                "UPDATE",
                "  team",
                "SET",
                f"  name_normalized = {team_name_str},",
                f"  url_path_slug = {slug_str}",
                "WHERE",
                f"  id = {keep_team_id};",
                "",
                "UPDATE",
                "  tournament_team",
                "SET",
                f"  team_id = {keep_team_id}",
                "WHERE",
                f"  id IN ({merge_predicate});",
                "",
                "DELETE FROM",
                "  team",
                "WHERE",
                f"  id IN ({delete_predicate});",
                "",
            ]
        )

    with open(HERE / "migrations" / "0012-teams-deduplicate.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


def main() -> None:
    _validate_division_sort_key()
    _validate_get_match_slot_id()
    bracket_id_info = _write_brackets_sql()

    extracted_dir = HERE.parent / "intermediate-data"
    filenames_by_year = _get_filenames_by_year()
    team_name_synonyms = _get_team_name_synonyms()
    team_name_duplicates = _get_team_name_duplicates()

    insert_ids = InsertIDs(
        next_team_id=1,
        next_tournament_team_id=1,
        next_team_point_deduction_id=1,
        next_competitor_id=1,
        next_tournament_competitor_id=1,
        next_match_id=1,
        next_placer_denormalized_id=1,
    )
    inserts = Inserts(
        team_rows=[],
        tournament_team_rows=[],
        team_point_deduction_rows=[],
        competitor_rows=[],
        tournament_competitor_rows=[],
        match_rows=[],
        placer_denormalized_rows=[],
    )
    for year, filenames in filenames_by_year.items():
        insert_ids = _handle_year(
            extracted_dir,
            year,
            insert_ids,
            inserts,
            filenames,
            bracket_id_info,
            team_name_synonyms,
        )

    _validate_brackets(inserts.match_rows)

    _write_teams_sql(inserts)
    _write_tournament_teams_sql(inserts)
    _write_team_point_deductions_sql(inserts)
    _write_competitors_sql(inserts)
    _write_tournament_competitors_sql(inserts)
    _write_matches_sql(inserts)
    _write_placers_denormalized_sql(inserts)

    _write_team_deduplicate_sql(inserts, team_name_duplicates)


if __name__ == "__main__":
    main()
