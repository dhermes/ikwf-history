# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import html
import pathlib
import sqlite3

import bracket_utils
import bs4
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
_TEAMS_IDS: tuple[int, ...] = (167, 438, 479, 2255)


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class TeamInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name_normalized: str


def _get_team_info(
    connection: sqlite3.Connection, team_ids: tuple[int, ...]
) -> list[TeamInfo]:
    team_info_sql = _get_sql("_team-info.sql")
    if team_info_sql.count(":team_ids") != 1:
        raise ValueError("Unexpected SQL", team_info_sql)

    placeholders = ", ".join(["?"] * len(team_ids))
    sql = team_info_sql.replace(":team_ids", placeholders)

    cursor = connection.cursor()
    cursor.execute(sql, team_ids)
    rows = [TeamInfo(**row) for row in cursor.fetchall()]
    cursor.close()
    return rows


def _teams_landing_html(teams: list[TeamInfo]) -> str:
    if len(teams) == 0:
        raise NotImplementedError("No teams")

    parts: list[str] = [
        "<html>",
        "  <head>",
        "    <title>Teams</title>",
        '    <link href="/css/tournament-view.fb678ab0.min.css" rel="stylesheet" />',
        "  </head>",
        "  <body>",
        '    <div class="tournament-view">',
        "      <h1>Teams</h1>",
        "      <ul>",
    ]

    for team in teams:
        parts.extend(
            [
                "      <li>",
                f'        <a href="/teams/{team.id_}/index.html">',
                f"          {html.escape(team.name_normalized)}",
                f"        </a> ({team.id_})",
                "      </li>",
            ]
        )

    parts.extend(
        [
            "      </ul>",
            "    </div>",
            "  </body>",
            "</html>",
        ]
    )

    soup = bs4.BeautifulSoup("\n".join(parts), features="html.parser")
    return soup.prettify(formatter="html")


class Qualifier(_ForbidExtra):
    competitor_id: int
    year: int
    division: bracket_utils.Division
    weight: int
    full_name: str
    place: int | None


def _get_all_qualifiers(
    connection: sqlite3.Connection, team_id: int
) -> list[Qualifier]:
    all_qualifiers_sql = _get_sql("_all-qualifiers.sql")

    cursor = connection.cursor()
    bind_parameters = {"team_id": team_id}
    cursor.execute(all_qualifiers_sql, bind_parameters)
    rows = [Qualifier(**row) for row in cursor.fetchall()]
    cursor.close()
    return rows


def _get_weight_ref_html(
    static_root: pathlib.Path, year: int, qualifier: Qualifier
) -> str:
    division_path = bracket_utils.get_division_path(qualifier.division)
    brackets_root = static_root / "brackets"
    html_path = brackets_root / str(year) / division_path / f"{qualifier.weight}.html"
    include_url = html_path.is_file()

    division_display = bracket_utils.get_division_display(qualifier.division)
    weight_text = f"{division_display} {qualifier.weight}"
    if not include_url:
        return html.escape(weight_text)

    url = f"/brackets/{year}/{division_path}/{qualifier.weight}.html"
    return f'<a href="{url}">{html.escape(weight_text)}</a>'


def _get_placement_suffix(place: int | None) -> str:
    if place is None:
        return ""

    if place == 1:
        return " (Champion)"
    if place == 2:
        return " (2nd place)"
    if place == 3:
        return " (3rd place)"
    if place == 4:
        return " (4th place)"
    if place == 5:
        return " (5th place)"
    if place == 6:
        return " (6th place)"
    if place == 7:
        return " (7th place)"
    if place == 8:
        return " (8th place)"

    raise NotImplementedError(place)


def _get_team_html(
    static_root: pathlib.Path, team: TeamInfo, qualifiers: list[Qualifier]
) -> str:
    name = team.name_normalized
    parts: list[str] = [
        "<html>",
        "  <head>",
        f"    <title>Team: {html.escape(name)}</title>",
        '    <link href="/css/tournament-view.fb678ab0.min.css" rel="stylesheet" />',
        "  </head>",
        "  <body>",
        '    <div class="tournament-view">',
        f"      <h1>{html.escape(name)}</h1>",
        f"      <h2>State Qualifiers ({len(qualifiers)})</h2>",
    ]

    by_year: dict[int, list[Qualifier]] = {}
    for qualifier in qualifiers:
        by_year.setdefault(qualifier.year, []).append(qualifier)

    years = sorted(by_year.keys())
    for year in years:
        year_qualifiers = by_year[year]
        parts.extend(
            [
                f"      <h3>{year} ({len(year_qualifiers)})</h3>",
                "      <ol>",
            ]
        )
        for qualifier in year_qualifiers:
            weight_link = _get_weight_ref_html(static_root, year, qualifier)
            place_suffix = _get_placement_suffix(qualifier.place)
            parts.extend(
                [
                    "        <li>",
                    f"{html.escape(qualifier.full_name)}, {weight_link}{place_suffix}",
                    "        </li>",
                ]
            )

        parts.append("      </ol>")

    parts.extend(
        [
            "    </div>",
            "  </body>",
            "</html>",
        ]
    )

    soup = bs4.BeautifulSoup("\n".join(parts), features="html.parser")
    return soup.prettify(formatter="html")


def main() -> None:
    static_root = HERE.parent / "static" / "static"
    teams_root = static_root / "teams"
    teams_root.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        teams = _get_team_info(connection, _TEAMS_IDS)
        landing_html = _teams_landing_html(teams)
        with open(teams_root / "index.html", "w") as file_obj:
            file_obj.write(landing_html)

        for team in teams:
            qualifiers = _get_all_qualifiers(connection, team.id_)
            team_html = _get_team_html(static_root, team, qualifiers)
            with_id = teams_root / str(team.id_)
            with_id.mkdir(parents=True, exist_ok=True)
            with open(with_id / "index.html", "w") as file_obj:
                file_obj.write(team_html)


if __name__ == "__main__":
    main()
