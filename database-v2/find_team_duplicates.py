# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib
import sqlite3

import bracket_utils
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
_ALL_CAPS_PARTS = ("AJ", "AO", "WC")


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


def _normalize_name(value: str) -> str:
    parts = value.split()
    space_normal = " ".join(parts)
    return space_normal.lower()


def _fix_title_part(value: str) -> str:
    value_upper = value.upper()
    if value_upper in _ALL_CAPS_PARTS:
        return value_upper

    return value


def _title_case(value: str) -> str:
    as_title = value.title()
    parts = [_fix_title_part(part) for part in as_title.split()]
    return " ".join(parts)


def main():
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        all_teams = _get_all_teams(connection)

    by_name: dict[str, list[TeamInfo]] = {}
    for team_info in all_teams:
        name_lower = _normalize_name(team_info.name)
        by_name.setdefault(name_lower, []).append(team_info)

    verified_teams: list[bracket_utils.VerifiedTeam] = []
    for name_lower in sorted(by_name.keys()):
        duplicate_teams = by_name[name_lower]
        if len(duplicate_teams) == 0:
            raise RuntimeError("Invariant violation")
        # If there is no actual duplication, no need to deduplicate (yet)
        if len(duplicate_teams) == 1:
            continue

        duplicates = [
            bracket_utils.TeamDuplicate(
                tournament_id=team.tournament_id,
                division=team.division,
                name=team.name,
            )
            for team in duplicate_teams
        ]
        # Close enough (until human inspection)
        name_normalized = _title_case(name_lower)
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
