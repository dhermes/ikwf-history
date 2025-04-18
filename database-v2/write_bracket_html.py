# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib
import sqlite3

import bracket_utils
import pydantic

HERE = pathlib.Path(__file__).resolve().parent


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


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


class MatchData(_ForbidExtra):
    match_slot_id: int
    bout_number: int | None
    match_slot: bracket_utils.MatchSlot
    top_name: str | None
    top_team: str | None
    top_score: int | None
    bottom_name: str | None
    bottom_team: str | None
    bottom_score: int | None
    top_win: bool | None
    result: str


def _get_match_data(
    connection: sqlite3.Connection,
    division: bracket_utils.Division,
    weight: int,
    tournament_id: int,
) -> list[MatchData]:
    match_data_sql = _get_sql("_match-data.sql")
    cursor = connection.cursor()
    bind_parameters = {
        "weight": weight,
        "division": division,
        "tournament_id": tournament_id,
    }
    cursor.execute(match_data_sql, bind_parameters)

    rows: list[MatchData] = []
    for row in cursor.fetchall():
        keep_row = dict(row)
        rows.append(MatchData(**keep_row))

    cursor.close()

    return rows


class JSONBrackets(pydantic.RootModel[list[MatchData]]):
    pass


def _render_bracket_json(
    api_root: pathlib.Path,
    year: int,
    division: bracket_utils.Division,
    weight: int,
    match_data_rows: list[MatchData],
):
    division_path = bracket_utils.get_division_path(division)
    destination = api_root / "brackets" / str(year) / division_path
    destination.mkdir(parents=True, exist_ok=True)
    json_path = destination / f"{weight}.json"

    to_serialize = JSONBrackets(root=match_data_rows)
    with open(json_path, "w") as file_obj:
        file_obj.write(to_serialize.model_dump_json(indent=2))
        file_obj.write("\n")


def main() -> None:
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
                    match_data_rows = _get_match_data(
                        connection, division, weight, tournament_id
                    )

                    if len(match_data_rows) == 0:
                        continue

                    _render_bracket_json(
                        api_root, year, division, weight, match_data_rows
                    )


if __name__ == "__main__":
    main()
