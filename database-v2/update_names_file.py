# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3

import bracket_utils
import pydantic

_HERE = pathlib.Path(__file__).resolve().parent


_ALL_NAMES = """\
WITH tournament_competitor_extended AS (
  SELECT
    c.id,
    tc.id AS competitor_id,
    c.full_name_normalized,
    t.name_normalized AS team_name_normalized,
    tt.tournament_id,
    tournament.year,
    b.division,
    b.weight
  FROM
    match AS m
    INNER JOIN tournament_competitor AS tc ON m.top_competitor_id = tc.id
    INNER JOIN competitor AS c ON tc.competitor_id = c.id
    INNER JOIN tournament_team AS tt ON tc.team_id = tt.id
    INNER JOIN team AS t ON tt.team_id = t.id
    INNER JOIN bracket AS b ON m.bracket_id = b.id
    INNER JOIN tournament ON b.tournament_id = tournament.id
  ----------------------------------------
  UNION
  ----------------------------------------
  SELECT
    c.id,
    tc.id AS competitor_id,
    c.full_name_normalized,
    t.name_normalized AS team_name_normalized,
    tt.tournament_id,
    tournament.year,
    b.division,
    b.weight
  FROM
    match AS m
    INNER JOIN tournament_competitor AS tc ON m.bottom_competitor_id = tc.id
    INNER JOIN competitor AS c ON tc.competitor_id = c.id
    INNER JOIN tournament_team AS tt ON tc.team_id = tt.id
    INNER JOIN team AS t ON tt.team_id = t.id
    INNER JOIN bracket AS b ON m.bracket_id = b.id
    INNER JOIN tournament ON b.tournament_id = tournament.id
)

SELECT DISTINCT
  tce.id,
  tce.competitor_id,
  tce.full_name_normalized,
  tce.team_name_normalized,
  tce.tournament_id,
  tce.year,
  tce.division,
  tce.weight
FROM
  tournament_competitor_extended AS tce
ORDER BY tce.id
"""


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid", validate_by_name=True, validate_by_alias=True
    )


class _NameInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    competitor_id: int
    full_name_normalized: str
    team_name_normalized: str
    tournament_id: int
    year: int
    division: bracket_utils.Division
    weight: int


def _get_all_names(
    connection: sqlite3.Connection,
) -> list[_NameInfo]:
    cursor = connection.cursor()
    cursor.execute(_ALL_NAMES)
    rows = [_NameInfo(**row) for row in cursor.fetchall()]
    cursor.close()

    return rows


class _NameDuplicate(_ForbidExtra):
    tournament_id: int
    year: int
    team_name_normalized: str
    full_name_normalized: str
    division: bracket_utils.Division
    weight: int


def _verified_name_sort_func(
    name_duplicate: _NameDuplicate,
) -> tuple[int, bracket_utils.Division, int, int, str]:
    return (
        name_duplicate.year,
        name_duplicate.division,
        name_duplicate.weight,
        name_duplicate.tournament_id,
        name_duplicate.full_name_normalized,
    )


class _VerifiedName(_ForbidExtra):
    full_name_normalized: str
    url_path_slug: str | None
    duplicates: list[_NameDuplicate]

    def sort(self) -> None:
        self.duplicates.sort(key=_verified_name_sort_func)


def _duplicate_sort_func(verified_name: _VerifiedName) -> str:
    return verified_name.full_name_normalized


class _NameDuplicates(pydantic.RootModel[list[_VerifiedName]]):
    def sort(self) -> None:
        self.root.sort(key=_duplicate_sort_func)

        for verified_name in self.root:
            verified_name.sort()


def main() -> None:
    with sqlite3.connect(_HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        all_names = _get_all_names(connection)

    verified_names: dict[str, _VerifiedName] = {}
    for name_info in all_names:
        name_duplicate = _NameDuplicate(
            tournament_id=name_info.tournament_id,
            year=name_info.year,
            team_name_normalized=name_info.team_name_normalized,
            full_name_normalized=name_info.full_name_normalized,
            division=name_info.division,
            weight=name_info.weight,
        )

        full_name_normalized = name_info.full_name_normalized

        if full_name_normalized not in verified_names:
            verified_names[full_name_normalized] = _VerifiedName(
                full_name_normalized=full_name_normalized,
                url_path_slug=None,
                duplicates=[],
            )

        verified_names[full_name_normalized].duplicates.append(name_duplicate)

    name_duplicates = _NameDuplicates(root=verified_names.values())
    name_duplicates.sort()

    as_json = name_duplicates.model_dump_json(indent=2)
    with open(_HERE / "_competitor-name-duplicates.json", "w") as file_obj:
        file_obj.write(as_json)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
