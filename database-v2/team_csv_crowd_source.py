# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import csv
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


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class TeamYearInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name: str
    slug: str | None
    year: int
    division: bracket_utils.Division


class TeamInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name: str
    slug: str | None
    divisions_text: str


def _info_sort_key(info: TeamYearInfo) -> tuple[int, int]:
    return info.year, bracket_utils.division_sort_key(info.division)


def _unique(values: list[str]) -> list[str]:
    seen = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)

    return result


def _get_all_teams(
    connection: sqlite3.Connection,
) -> list[TeamInfo]:
    all_teams_sql = _get_sql("_all-teams.sql")
    cursor = connection.cursor()
    cursor.execute(all_teams_sql)
    rows = [TeamYearInfo(**row) for row in cursor.fetchall()]
    cursor.close()

    by_id: dict[int, list[TeamYearInfo]] = {}
    for row in rows:
        by_id.setdefault(row.id_, []).append(row)

    result: list[TeamInfo] = []
    for id_, matches in by_id.items():
        sorted_matches = sorted(matches, key=_info_sort_key)
        divisions_text_parts = [
            f"{bracket_utils.get_division_display(match.division)} {match.year}"
            for match in sorted_matches
        ]
        divisions_text_parts = _unique(divisions_text_parts)
        divisions_text = ", ".join(divisions_text_parts)

        # NOTE: We assume `name` and `slug` are the same for all rows.
        result.append(
            TeamInfo(
                id=id_,
                name=matches[0].name,
                slug=matches[0].slug,
                divisions_text=divisions_text,
            )
        )

    return result


def main():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        all_teams = _get_all_teams(connection)

    with open(HERE / "team-crowd-source.csv", "w") as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=("name", "slug", "divisions_text"))
        writer.writeheader()
        for team in all_teams:
            writer.writerow(
                {
                    "name": team.name,
                    "slug": team.slug,
                    "divisions_text": team.divisions_text,
                }
            )


if __name__ == "__main__":
    main()
