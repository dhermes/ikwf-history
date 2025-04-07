# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import json
import pathlib
import sqlite3

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


def _get_bracket_json(
    connection: sqlite3.Connection, division: str, weight: int, tournament_id: int
):
    bracket_json_sql = _get_sql("_bracket-json.sql")
    cursor = connection.cursor()
    bind_parameters = {
        "weight": weight,
        "division": division,
        "tournament_id": tournament_id,
    }
    cursor.execute(bracket_json_sql, bind_parameters)

    rows = []
    for row in cursor.fetchall():
        keep_row = dict(row)
        keep_row["top_win"] = _to_bool(keep_row["top_win"])
        rows.append(keep_row)

    cursor.close()

    return rows


def main():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        all_tournaments = _get_all_tournaments(connection)
        (tournament_id,) = all_tournaments[2025]
        tournament_brackets = _get_all_brackets(connection, tournament_id)
        division, weight = tournament_brackets[10]
        bracket_json_rows = _get_bracket_json(
            connection, division, weight, tournament_id
        )
        print(json.dumps(bracket_json_rows, indent=2))


if __name__ == "__main__":
    main()
