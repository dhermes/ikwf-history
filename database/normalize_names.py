# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib
import sqlite3

import pydantic

HERE = pathlib.Path(__file__).resolve().parent


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


def _get_all_competitors(connection: sqlite3.Connection):
    matches_for_scores_sql = _get_sql("_all-competitors.sql")
    cursor = connection.cursor()
    cursor.execute(matches_for_scores_sql)

    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()

    return rows


def _get_updated_names(
    first_name: str,
    last_name: str,
    first_name_replacements: dict[str, str],
    last_name_replacements: dict[str, str],
) -> tuple[str, str] | None:
    title_first = first_name.title()
    title_last = last_name.title()
    # Nothing to update if already title case
    if first_name == title_first and last_name == title_last:
        return None

    new_first_name = first_name_replacements.get(first_name, first_name)
    new_last_name = last_name_replacements.get(last_name, last_name)

    both = (new_first_name, new_last_name)
    if both == ("Mitch", "Alberstett"):
        return "Mitchell", "Alberstett"

    if both == ("Colin", "Allgire"):
        return "Collin", "Allgire"

    if both == ("Tom", "Ambrose"):
        return "Thomas", "Ambrose"

    if both == ("Auguste", "Anderson"):
        return "Augie", "Anderson"

    if both == ("Steven", "Andrukaiti"):
        return "Steven", "Andrukaitis"

    if both == ("Joe", "Aquino"):
        return "Joseph", "Aquino"

    if both == ("Christopher", "Arthurs"):
        return "Chris", "Arthurs"

    if both == ("Mike", "Bachner"):
        return "Michael", "Bachner"

    if both == ("Ernest", "Badger,Jr"):
        return None

    if both == ("Mike", "Bachner"):
        return "Michael", "Bachner"

    if both == ("Joseph", "Barczak"):
        return "Joe", "Barczak"

    if both == ("Timothy", "Barringer"):
        return "Tim", "Barringer"

    if both == ("Pete", "Bauer"):
        return "Peter", "Bauer"

    if both == ("Michael", "Benefiel"):
        return "Mike", "Benefiel"

    if both == ("Mikey", "Benefiel"):
        return "Mike", "Benefiel"

    if both == ("Matthew", "Bochenek"):
        return "Matt", "Bochenek"

    if both == ("Matthew", "Boggess"):
        return "Matt", "Boggess"

    if both == ("Chris", "Brassell"):
        return "Christopher", "Brassell"

    if both == ("Joseph", "Brooks"):
        return "Joe", "Brooks"

    if both == ("Daniel", "Bruce"):
        return "DJ", "Bruce"

    if both == ("Nick", "Bryson"):
        return "Nicholas", "Bryson"

    if both == ("Jeffrey", "Bybee"):
        return "Jeffery", "Bybee"

    if both == ("Joey", "Carfagnini"):
        return "Joseph", "Carfagnini"

    if both == ("Edward", "Castillo"):
        return "Eddie", "Castillo"

    if both == ("Edwardo", "Castillo"):
        return "Eddie", "Castillo"

    if both == ("Jordon", "Chang"):
        return "Jordan", "Chang"

    if both == ("Dominick", "Chase"):
        return "Dominic", "Chase"

    if both == ("James", "Chase"):
        return "Jimmy", "Chase"

    if both == ("Ryan", "Christophe"):
        return "Ryan", "Christopher"

    if both == ("Matt", "Cole"):
        return "Matthew", "Cole"

    if both == ("John", "Cook"):
        return "Jonathon", "Cook"

    if both == ("Christopher", "Cox"):
        return "Chris", "Cox"

    return new_first_name, new_last_name


def _sql_str(value: str) -> str:
    quoted = value.replace("'", "''")
    return f"'{quoted}'"


class MapStrStr(pydantic.RootModel[dict[str, str]]):
    pass


def main():
    with open(HERE / "_first-name-replacements.json") as file_obj:
        root_map = MapStrStr.model_validate_json(file_obj.read())
        first_name_replacements = root_map.root

    with open(HERE / "_last-name-replacements.json") as file_obj:
        root_map = MapStrStr.model_validate_json(file_obj.read())
        last_name_replacements = root_map.root

    lines = [
        "-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.",
        "",
        "PRAGMA foreign_keys = ON;",
        "PRAGMA encoding = 'UTF-8';",
        "PRAGMA integrity_check;",
        "",
        "--------------------------------------------------------------------------------",
        "",
        "UPDATE",
        "  competitor",
        "SET",
        "  suffix = 'Jr'",
        "WHERE",
        "  suffix = 'JR';",
        "",
        "UPDATE",
        "  competitor",
        "SET",
        "  first_name = 'Ernest',",
        "  last_name = 'Badger',",
        "  suffix = 'Jr'",
        "WHERE",
        "  id = 1300;",
        "",
        "--------------------------------------------------------------------------------",
        "",
        "CREATE TEMP TABLE competitor_update_temp (",
        "  id INTEGER,",
        "  first_name TEXT NOT NULL,",
        "  last_name TEXT NOT NULL",
        ");",
        "",
        "INSERT INTO",
        "  competitor_update_temp(id, first_name, last_name)",
        "VALUES",
    ]

    update_lines: list[tuple[str, str]] = []
    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        competitors = _get_all_competitors(connection)
        for competitor in competitors:
            first_name = competitor["first_name"]
            last_name = competitor["last_name"]
            update = _get_updated_names(
                first_name, last_name, first_name_replacements, last_name_replacements
            )
            if update is None:
                continue

            competitor_id = competitor["id"]
            new_first_name, new_last_name = update
            competitor_id_str = f"{competitor_id},"
            first_name_size = 17
            first_name_str = f"{_sql_str(new_first_name)},".ljust(first_name_size)
            if len(first_name_str) != first_name_size:
                raise RuntimeError("Too long", len(first_name_str), first_name_str)

            values = (
                f"({competitor_id_str:<6} {first_name_str} {_sql_str(new_last_name)})"
            )
            comment = f"WAS: {first_name} || {last_name}"
            update_lines.append((values, comment))

    num_updates = len(update_lines)
    for i, update_line in enumerate(update_lines):
        line_ending = ";" if i == num_updates - 1 else ","
        values, comment = update_line
        lines.append(f"  {values}{line_ending} -- {comment}")

    lines.extend(
        [
            "",
            "UPDATE",
            "  competitor AS c",
            "SET",
            "  first_name = u.first_name,",
            "  last_name = u.last_name",
            "FROM",
            "  competitor_update_temp AS u",
            "WHERE",
            "  c.id = u.id;",
            "",
        ]
    )

    with open(HERE / "migrations" / "0020-name-normalize.sql", "w") as file_obj:
        file_obj.write("\n".join(lines))


if __name__ == "__main__":
    main()
