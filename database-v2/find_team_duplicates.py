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


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class TeamInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    tournament_id: int
    division: bracket_utils.Division
    name: str
    team_id: int
    name_normalized: str


def _get_all_teams(
    connection: sqlite3.Connection,
) -> list[TeamInfo]:
    unverified_team_info_sql = _get_sql("_unverified-team-info.sql")
    cursor = connection.cursor()
    cursor.execute(unverified_team_info_sql)
    rows = [TeamInfo(**row) for row in cursor.fetchall()]
    cursor.close()

    return rows


def main():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        all_teams = _get_all_teams(connection)

    by_name: dict[str, list[TeamInfo]] = {}
    for team_info in all_teams:
        name_lower = team_info.name.lower()
        by_name.setdefault(name_lower, []).append(team_info)

    verified_teams: list[bracket_utils.VerifiedTeam] = []
    for name_lower in sorted(by_name.keys()):
        duplicate_teams = by_name[name_lower]
        duplicates = [
            bracket_utils.TeamDuplicate(
                tournament_id=team.tournament_id,
                division=team.division,
                name=team.name,
            )
            for team in duplicate_teams
        ]
        # Close enough (until human inspection)
        name_normalized = name_lower.title()
        verified_team = bracket_utils.VerifiedTeam(
            name_normalized=name_normalized,
            url_path_slug=None,
            duplicates=duplicates,
        )
        verified_teams.append(verified_team)

    root_duplicates = bracket_utils.TeamDuplicates(root=verified_teams)
    print(root_duplicates.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
