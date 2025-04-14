# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3
from typing import NamedTuple

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
    team_score: int | None
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


def _handle_tournament(
    year: int,
    tournament_id: int,
    insert_ids: InsertIDs,
    bracket_id_info: dict[BracketInfoTuple, int],
    extracted: bracket_utils.ExtractedTournament,
) -> tuple[InsertIDs, Inserts]:
    # 1. `TeamRow` (allow duplicates across year and division)
    team_rows: list[TeamRow] = []
    # 2. `TournamentTeamRow`
    tournament_team_rows: list[TournamentTeamRow] = []
    # 3. `TeamPointDeductionRow`
    team_point_deduction_rows: list[TeamPointDeductionRow] = []
    # 4. `CompetitorRow` (allow duplicates across year)
    competitor_rows: list[CompetitorRow] = []
    # 5. `TournamentCompetitorRow`
    tournament_competitor_rows: list[TournamentCompetitorRow] = []
    # 6. `MatchRow`
    match_rows: list[MatchRow] = []

    inserts = Inserts(
        team_rows=team_rows,
        tournament_team_rows=tournament_team_rows,
        team_point_deduction_rows=team_point_deduction_rows,
        competitor_rows=competitor_rows,
        tournament_competitor_rows=tournament_competitor_rows,
        match_rows=match_rows,
    )
    return insert_ids, inserts  # TODO


def _handle_year(
    extracted_dir: pathlib.Path,
    year: int,
    insert_ids: InsertIDs,
    filenames: dict[int, str],
    bracket_id_info: dict[BracketInfoTuple, int],
) -> InsertIDs:
    for tournament_id, filename in filenames.items():
        with open(extracted_dir / filename) as file_obj:
            extracted = bracket_utils.ExtractedTournament.model_validate_json(
                file_obj.read()
            )

        insert_ids, _ = _handle_tournament(
            year, tournament_id, insert_ids, bracket_id_info, extracted
        )

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
    for year, filenames in filenames_by_year.items():
        insert_ids = _handle_year(
            extracted_dir, year, insert_ids, filenames, bracket_id_info
        )


if __name__ == "__main__":
    main()
