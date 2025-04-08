# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib
import sqlite3
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


def _to_bool(value: int) -> bool:
    """Convert a SQLite BOOLEAN to a Python bool."""
    if value == 0:
        return False

    if value == 1:
        return True

    raise ValueError(value)


def _get_all_tournaments(connection: sqlite3.Connection) -> dict[int, list[int]]:
    all_tournaments_sql = _get_sql("_all-tournaments.sql")
    cursor = connection.cursor()
    cursor.execute(all_tournaments_sql)
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()

    result: dict[int, list[int]] = {}
    for row in rows:
        year = row["year"]
        tournament_id = row["id"]
        result.setdefault(year, []).append(tournament_id)

    return result


def _get_all_brackets(
    connection: sqlite3.Connection, tournament_id: int
) -> list[tuple[str, int]]:
    all_brackets_sql = _get_sql("_all-brackets.sql")
    cursor = connection.cursor()
    bind_parameters = {"tournament_id": tournament_id}
    cursor.execute(all_brackets_sql, bind_parameters)
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()

    result: list[tuple[str, int]] = []
    for row in rows:
        result.append((row["division"], row["weight"]))

    return result


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


MatchSlot = Literal[
    "championship_r32_01",
    "championship_r32_02",
    "championship_r32_03",
    "championship_r32_04",
    "championship_r32_05",
    "championship_r32_06",
    "championship_r32_07",
    "championship_r32_08",
    "championship_r32_09",
    "championship_r32_10",
    "championship_r32_11",
    "championship_r32_12",
    "championship_r32_13",
    "championship_r32_14",
    "championship_r32_15",
    "championship_r32_16",
    "championship_r16_01",
    "championship_r16_02",
    "championship_r16_03",
    "championship_r16_04",
    "championship_r16_05",
    "championship_r16_06",
    "championship_r16_07",
    "championship_r16_08",
    "consolation_round2_01",
    "consolation_round2_02",
    "consolation_round2_03",
    "consolation_round2_04",
    "consolation_round2_05",
    "consolation_round2_06",
    "consolation_round2_07",
    "consolation_round2_08",
    "championship_quarter_01",
    "championship_quarter_02",
    "championship_quarter_03",
    "championship_quarter_04",
    "consolation_round3_01",
    "consolation_round3_02",
    "consolation_round3_03",
    "consolation_round3_04",
    "consolation_round4_blood_01",
    "consolation_round4_blood_02",
    "consolation_round4_blood_03",
    "consolation_round4_blood_04",
    "championship_semi_01",
    "championship_semi_02",
    "consolation_round5_01",
    "consolation_round5_02",
    "consolation_round6_semi_01",
    "consolation_round6_semi_02",
    "consolation_seventh_place",
    "consolation_fifth_place",
    "consolation_third_place",
    "championship_first_place",
]


class BracketJSON(_ForbidExtra):
    match_slot_id: int
    bout_number: int | None
    match_slot: MatchSlot
    top_full_name: str | None
    top_team: str | None
    top_team_acronym: str | None
    top_score: int | None
    bottom_full_name: str | None
    bottom_team: str | None
    bottom_team_acronym: str | None
    bottom_score: int | None
    top_win: bool
    result: str


Division = Literal[
    "bantam",
    "intermediate",
    "novice",
    "senior",
    "bantam_girls",
    "intermediate_girls",
    "novice_girls",
    "senior_girls",
]


def _get_bracket_json(
    connection: sqlite3.Connection, division: Division, weight: int, tournament_id: int
) -> list[BracketJSON]:
    bracket_json_sql = _get_sql("_bracket-json.sql")
    cursor = connection.cursor()
    bind_parameters = {
        "weight": weight,
        "division": division,
        "tournament_id": tournament_id,
    }
    cursor.execute(bracket_json_sql, bind_parameters)

    rows: list[BracketJSON] = []
    for row in cursor.fetchall():
        keep_row = dict(row)
        keep_row["top_win"] = _to_bool(keep_row["top_win"])
        rows.append(BracketJSON(**keep_row))

    cursor.close()

    return rows


class JSONBrackets(pydantic.RootModel[list[BracketJSON]]):
    pass


def _render_bracket_json(
    api_root: pathlib.Path,
    year: int,
    division: Division,
    weight: int,
    bracket_json_rows: list[BracketJSON],
):
    division_path = division.replace("_", "-")
    destination = api_root / "brackets" / str(year) / division_path
    destination.mkdir(parents=True, exist_ok=True)
    json_path = destination / f"{weight}.json"

    to_serialize = JSONBrackets(root=bracket_json_rows)
    with open(json_path, "w") as file_obj:
        file_obj.write(to_serialize.model_dump_json(indent=2))
        file_obj.write("\n")


def main():
    static_root = HERE.parent / "static" / "static"
    api_root = static_root / "api" / "v20250408"

    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        all_tournaments = _get_all_tournaments(connection)
        tournament_years = sorted(all_tournaments.keys())
        for year in tournament_years:
            for tournament_id in all_tournaments[year]:
                tournament_brackets = _get_all_brackets(connection, tournament_id)
                for division, weight in tournament_brackets:
                    bracket_json_rows = _get_bracket_json(
                        connection, division, weight, tournament_id
                    )

                    if len(bracket_json_rows) == 0:
                        continue

                    _render_bracket_json(
                        api_root, year, division, weight, bracket_json_rows
                    )


if __name__ == "__main__":
    main()
