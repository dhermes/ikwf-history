# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import csv
import functools
import pathlib
import sqlite3

import pydantic

HERE = pathlib.Path(__file__).resolve().parent


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class TeamInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name: str
    slug: str | None


def _get_all_teams(
    connection: sqlite3.Connection,
) -> list[TeamInfo]:
    all_teams_sql = _get_sql("_all-teams.sql")
    cursor = connection.cursor()
    cursor.execute(all_teams_sql)
    rows = [TeamInfo(**row) for row in cursor.fetchall()]
    cursor.close()

    return rows


def main():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        all_teams = _get_all_teams(connection)

    with open(HERE / "team-crowd-source.csv", "w") as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=("name", "slug"))
        writer.writeheader()
        for team in all_teams:
            writer.writerow({"name": team.name, "slug": team.slug})


if __name__ == "__main__":
    main()
