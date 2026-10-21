# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3

import pydantic

_HERE = pathlib.Path(__file__).resolve().parent


_ALL_NAMES = """\
SELECT DISTINCT
    c.id,
    c.full_name_normalized,
    t.name_normalized AS team_name_normalized,
    tt.tournament_id
FROM
    tournament_competitor AS tc
INNER JOIN competitor AS c ON tc.competitor_id = c.id
INNER JOIN tournament_team AS tt ON tc.team_id = tt.id
INNER JOIN team AS t ON tt.team_id = t.id
ORDER BY c.id
"""


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        extra="forbid", validate_by_name=True, validate_by_alias=True
    )


class _NameInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    full_name_normalized: str
    team_name_normalized: str
    tournament_id: int


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
    team_name_normalized: str
    full_name_normalized: str


def _get_tournament_year(tournament_id: int) -> int:
    if tournament_id in (10028, 10029, 10030, 10031, 10050):
        return tournament_id - 8030
    if tournament_id == 10052:
        return tournament_id - 8028
    if tournament_id > 10000:
        raise ValueError("Unknown tournament ID", tournament_id)

    if tournament_id < 50:
        return tournament_id + 1970

    return tournament_id + 1972


def _verified_name_sort_func(
    name_duplicate: _NameDuplicate,
) -> tuple[int, int, str]:
    tournament_year = _get_tournament_year(name_duplicate.tournament_id)
    return (
        tournament_year,
        name_duplicate.tournament_id,
        name_duplicate.full_name_normalized,
    )


class _VerifiedName(_ForbidExtra):
    full_name_normalized: str
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
            team_name_normalized=name_info.team_name_normalized,
            full_name_normalized=name_info.full_name_normalized,
        )

        full_name_normalized = name_info.full_name_normalized

        if full_name_normalized not in verified_names:
            verified_names[full_name_normalized] = _VerifiedName(
                full_name_normalized=full_name_normalized, duplicates=[]
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
