# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3

import bracket_utils
import pydantic

_HERE = pathlib.Path(__file__).resolve().parent


_ALL_TEAMS = """\
SELECT DISTINCT
    tt.id,
    tt.name,
    tt.division,
    tt.tournament_id,
    tt.team_id,
    t.url_path_slug,
    t.name_normalized
FROM
    tournament_team AS tt
INNER JOIN team AS t ON tt.team_id = t.id
ORDER BY tt.id
"""


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid", validate_by_name=True, validate_by_alias=True
    )


class _TeamInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name: str
    division: bracket_utils.Division
    tournament_id: int
    team_id: int
    url_path_slug: str | None
    name_normalized: str


def _get_all_teams(
    connection: sqlite3.Connection,
) -> list[_TeamInfo]:
    cursor = connection.cursor()
    cursor.execute(_ALL_TEAMS)
    rows = [_TeamInfo(**row) for row in cursor.fetchall()]
    cursor.close()

    return rows


def main() -> None:
    with sqlite3.connect(_HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        all_teams = _get_all_teams(connection)

    verified_teams: dict[str, bracket_utils.VerifiedTeam] = {}
    for team_info in all_teams:
        team_duplicate = bracket_utils.TeamDuplicate(
            tournament_id=team_info.tournament_id,
            division=team_info.division,
            name=team_info.name,
        )

        url_path_slug = team_info.url_path_slug
        name_normalized = team_info.name_normalized

        if name_normalized not in verified_teams:
            verified_teams[name_normalized] = bracket_utils.VerifiedTeam(
                name_normalized=name_normalized,
                url_path_slug=url_path_slug,
                duplicates=[],
            )

        if verified_teams[name_normalized].url_path_slug is None:
            verified_teams[name_normalized].url_path_slug = url_path_slug

        if url_path_slug is None:
            url_path_slug = verified_teams[name_normalized].url_path_slug

        if verified_teams[name_normalized].url_path_slug != url_path_slug:
            raise RuntimeError("Invariant violation")

        verified_teams[name_normalized].duplicates.append(team_duplicate)

    team_duplicates = bracket_utils.TeamDuplicates(root=verified_teams.values())
    team_duplicates.sort()

    print(len(team_duplicates.root))


if __name__ == "__main__":
    main()
