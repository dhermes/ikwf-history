# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib
import sqlite3

HERE = pathlib.Path(__file__).resolve().parent


@functools.cache
def _get_bracket_json_sql() -> str:
    with open(HERE / "_bracket-json.sql") as file_obj:
        return file_obj.read()


def main():
    bracket_json_sql = _get_bracket_json_sql()

    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        bind_parameters = {"weight": 84, "division": "bantam", "tournament_id": 55}
        cursor.execute(bracket_json_sql, bind_parameters)

        rows = [dict(row) for row in cursor.fetchall()]
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
