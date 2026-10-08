# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import html
import pathlib
import sqlite3

import bracket_utils
import bs4
import pydantic

_HERE = pathlib.Path(__file__).resolve().parent
_NAME_OVERLAPS: dict[int, dict[str, str]] = {
    2000: {
        # Multiple "teams" due to cap on scoring
        "JUNIOR STREAKS #2": "GALESBURG JUNIOR STREAKS",
    },
    2001: {
        # Multiple "teams" due to cap on scoring
        "GALESBURG JR STREAKS #2": "GALESBURG JR STREAKS"
    },
    2024: {
        # Different names used in Rockford/Decatur
        "Rochelle WC": "Rochelle Wrestling Club",
    },
}
_COACH_BIOS: dict[str, dict[str, str]] = {
    "dakota": {
        "pete-alber": "Pete Alber",
    },
}
_TEAM_LOGOS: dict[str, str] = {
    "dakota": "dakota.png",
    "fox-valley": "fox-valley.png",
    "rochelle": "rochelle.jpg",
}


@functools.cache
def _get_sql(filename: str) -> str:
    with open(_HERE / filename) as file_obj:
        return file_obj.read()


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class TeamInfo(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    name_normalized: str
    url_path_slug: str


def _get_team_info(connection: sqlite3.Connection) -> list[TeamInfo]:
    team_info_sql = _get_sql("_verified-team-info.sql")
    cursor = connection.cursor()
    cursor.execute(team_info_sql)
    rows = [TeamInfo(**row) for row in cursor.fetchall()]
    cursor.close()
    return rows


def _teams_landing_html(teams: list[TeamInfo]) -> str:
    if len(teams) == 0:
        raise NotImplementedError("No teams")

    parts: list[str] = [
        "<!doctype html>",
        '<html lang="en">',
        "  <head>",
        '    <meta charset="UTF-8" />',
        '    <meta name="viewport" content="width=device-width, initial-scale=1" />',
        "",
        "    <title>Teams &mdash; IKWF History</title>",
        "",
        '    <link rel="stylesheet" href="/css/teams.f908a804.min.css" />',
        '    <link rel="stylesheet" href="/css/footer.cb84bd19.min.css" />',
        "  </head>",
        "",
        "  <body>",
        '    <main class="teams-page">',
        '      <header class="teams-header">',
        '        <a class="back-link" href="/"> &larr; IKWF History </a>',
        "",
        '        <div class="header-content">',
        '          <div class="header-main">',
        "            <div>",
        '              <span class="eyebrow">THE ARCHIVE</span>',
        "              <h1>Teams</h1>",
        "              <p>",
        "                Explore the wrestling clubs and teams that have been part of",
        "                Illinois youth wrestling history",
        "              </p>",
        "            </div>",
        "",
        "            <img",
        '              class="header-logo"',
        '              src="/images/ikwf-logo-300x300.png"',
        '              alt="Illinois Kids Wrestling Federation"',
        "            />",
        "          </div>",
        "        </div>",
        "      </header>",
        "",
        '      <section class="teams-browser">',
        '        <div class="browser-toolbar">',
        '          <label class="search-box">',
        '            <span class="search-icon">&#8981;</span>',
        "            <input",
        '              id="team-search"',
        '              type="search"',
        '              placeholder="Search teams..."',
        '              autocomplete="off"',
        '              spellcheck="false"',
        "            />",
        "            <kbd>/</kbd>",
        "          </label>",
        "",
        '          <div class="team-count" id="team-count"></div>',
        "        </div>",
        "",
        '        <ul class="team-list" id="team-list">',
    ]

    for team in teams:
        html_name = html.escape(team.name_normalized)
        parts.extend(
            [
                "      <li>",
                f'        <a href="/teams/{team.url_path_slug}/">',
                f'          <span class="team-name">{html_name}</span>',
                "        </a>",
                "      </li>",
            ]
        )

    team_nav = (
        '        <nav class="pagination" id="pagination" aria-label="Team pages"></nav>'
    )
    parts.extend(
        [
            "        </ul>",
            "",
            '        <div class="no-results" id="no-results" hidden>',
            '          <div class="no-results-mark">?</div>',
            "          <h2>No teams found</h2>",
            "          <p>Try a different search.</p>",
            "        </div>",
            "",
            team_nav,
            "      </section>",
            "",
            '      <footer class="footer">',
            "        <p>",
            "          An independent project preserving and exploring the history of",
            "          Illinois youth wrestling.",
            "        </p>",
            "",
            "        <p>",
            "          Created by Coach",
            '          <a href="/bios/danny-hermes/">Danny Hermes</a>',
            "        </p>",
            "      </footer>",
            "    </main>",
            "",
            '    <script src="/js/teams-search.2ba506ec.min.js"></script>',
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
    team_name: str
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


def _get_placement_display(place: int) -> str:
    if place == 1:
        return "Champion"

    if place == 2:
        return "2nd place"

    if place == 3:
        return "3rd place"

    if place == 4:
        return "4th place"

    if place == 5:
        return "5th place"

    if place == 6:
        return "6th place"

    if place == 7:
        return "7th place"

    if place == 8:
        return "8th place"

    raise NotImplementedError(place)


def _get_champs_html_parts(
    static_root: pathlib.Path, qualifiers: list[Qualifier]
) -> list[str]:
    champions: list[Qualifier] = []
    for qualifier in qualifiers:
        if qualifier.place == 1:
            champions.append(qualifier)

    if len(champions) == 0:
        return []

    parts: list[str] = [
        '<section class="achievement-section champions">',
        '  <div class="section-heading">',
        "    <div>",
        '      <span class="section-eyebrow">TOP STEP</span>',
        "      <h2>State Champions</h2>",
        "    </div>",
        "",
        f'   <span class="section-count">{len(champions)}</span>',
        "  </div>",
        "",
        '  <ol class="achievement-list">',
    ]

    for qualifier in champions:
        weight_anchor = _get_weight_ref_html(static_root, qualifier.year, qualifier)
        parts.extend(
            [
                "    <li>",
                f'     <span class="athlete">{html.escape(qualifier.full_name)}</span>',
                f"     {weight_anchor}",
                f'      <span class="year">{qualifier.year}</span>',
                "    </li>",
            ]
        )

    parts.extend(
        [
            "  </ol>",
            "</section>",
            "",
        ]
    )
    return parts


def _get_result_class(result: str) -> str:
    if result == "Champion":
        return "result champion"

    return "result"


def _get_placers_html_parts(
    static_root: pathlib.Path, qualifiers: list[Qualifier]
) -> list[str]:
    placers: list[Qualifier] = []
    for qualifier in qualifiers:
        if qualifier.place is not None:
            placers.append(qualifier)

    if len(placers) == 0:
        return []

    parts: list[str] = [
        '<section class="achievement-section placers">',
        '  <div class="section-heading">',
        "    <div>",
        '      <span class="section-eyebrow">THE PODIUM</span>',
        "      <h2>State Placers</h2>",
        "    </div>",
        "",
        f'    <span class="section-count">{len(placers)}</span>',
        "  </div>",
        "",
        '  <ol class="achievement-list">',
    ]

    for qualifier in placers:
        weight_anchor = _get_weight_ref_html(static_root, qualifier.year, qualifier)
        full_name = html.escape(qualifier.full_name)
        result = _get_placement_display(qualifier.place)
        result_class = _get_result_class(result)
        parts.extend(
            [
                "    <li>",
                f'      <span class="athlete">{full_name}</span>',
                f"      {weight_anchor}",
                f'       <span class="{result_class}">{result}</span>',
                f'       <span class="year">{qualifier.year}</span>',
                "    </li>",
            ]
        )

    parts.extend(
        [
            "  </ol>",
            "</section>",
            "",
        ]
    )
    return parts


def _get_qualifiers_html_parts(
    static_root: pathlib.Path, qualifiers: list[Qualifier], team_name_normalized: str
) -> list[str]:
    parts: list[str] = [
        '<section class="achievement-section qualifiers">',
        '  <div class="section-heading">',
        "    <div>",
        '      <span class="section-eyebrow">THE ROAD TO STATE</span>',
        "      <h2>State Qualifiers</h2>",
        "    </div>",
        "",
        f'    <span class="section-count">{len(qualifiers)}</span>',
        "  </div>",
        "",
        '  <div class="qualifier-years">',
    ]

    by_year: dict[int, list[Qualifier]] = {}
    name_by_year: dict[int, str] = {}
    for qualifier in qualifiers:
        by_year.setdefault(qualifier.year, []).append(qualifier)
        team_name = qualifier.team_name
        team_name = _NAME_OVERLAPS.get(qualifier.year, {}).get(team_name, team_name)
        if qualifier.year not in name_by_year:
            name_by_year[qualifier.year] = team_name

        if name_by_year[qualifier.year] != team_name:
            raise RuntimeError(
                "Multiple team names in one year",
                qualifier.year,
                team_name,
                name_by_year[qualifier.year],
                qualifier.team_name,
            )

    years = sorted(by_year.keys(), reverse=True)
    for i, year in enumerate(years):
        year_qualifiers = by_year[year]
        team_name = name_by_year[year]

        open_prop = ' open="open"' if i == 0 else ""
        qualifier_str = "qualifier" if len(year_qualifiers) == 1 else "qualifiers"
        summary_count = (
            f'    <span class="summary-count">'
            f"{len(year_qualifiers)} {qualifier_str}</span>"
        )
        parts.extend(
            [
                f"<details{open_prop}>",
                "  <summary>",
                f'    <span class="summary-year">{year}</span>',
                f'    <span class="summary-team">{html.escape(team_name)}</span>',
                summary_count,
                "  </summary>",
                "",
                '  <ol class="achievement-list">',
            ]
        )
        for qualifier in year_qualifiers:
            weight_anchor = _get_weight_ref_html(static_root, year, qualifier)
            if qualifier.place is None:
                result_span = ""
            else:
                result = _get_placement_display(qualifier.place)
                result_class = _get_result_class(result)
                result_span = f'<span class="{result_class}">{result}</span>'

            full_name = html.escape(qualifier.full_name)
            parts.extend(
                [
                    "    <li>",
                    f'      <span class="athlete">{full_name}</span>',
                    f"      {weight_anchor}",
                    f"      {result_span}",
                    "    </li>",
                ]
            )

        parts.extend(
            [
                "  </ol>",
                "</details>",
            ]
        )

    parts.extend(
        [
            "  </div>",
            "</section>",
        ]
    )
    return parts


def _get_team_html(
    static_root: pathlib.Path, team: TeamInfo, qualifiers: list[Qualifier]
) -> str:
    name = team.name_normalized
    state_champion_count = sum(1 for qualifier in qualifiers if qualifier.place == 1)
    state_placer_count = sum(
        1 for qualifier in qualifiers if qualifier.place is not None
    )
    state_qualifier_count = len(qualifiers)

    parts: list[str] = [
        "<!doctype html>",
        '<html lang="en">',
        "  <head>",
        '    <meta charset="UTF-8" />',
        '    <meta name="viewport" content="width=device-width, initial-scale=1" />',
        "",
        f"    <title>{html.escape(name)} &mdash; IKWF History</title>",
        "",
        '    <link rel="stylesheet" href="/css/team-page.6e2a271c.min.css" />',
        '    <link rel="stylesheet" href="/css/footer.cb84bd19.min.css" />',
        "  </head>",
        "",
        "  <body>",
        '    <main class="team-page">',
        '      <header class="team-header">',
        '        <a class="back-link" href="/teams/"> &larr; Teams </a>',
        "",
        '        <div class="team-header-main">',
        "          <div>",
        '            <span class="eyebrow">TEAM HISTORY</span>',
        "",
        f"            <h1>{html.escape(name)}</h1>",
        "          </div>",
        "",
    ]

    team_logo = _TEAM_LOGOS.get(team.url_path_slug)
    if team_logo is None:
        parts.extend(
            [
                "          <img",
                '            class="header-logo"',
                '            src="/images/ikwf-logo-300x300.png"',
                '            alt="Illinois Kids Wrestling Federation"',
                "          />",
                "        </div>",
            ]
        )
    else:
        parts.extend(
            [
                "          <img",
                '            class="header-logo"',
                f'            src="/images/logos/{team_logo}"',
                f'            alt="{html.escape(name)}"',
                "          />",
                "        </div>",
            ]
        )

    if (
        state_champion_count > 1
        and state_placer_count > 1
        and state_qualifier_count > 1
    ):
        parts.extend(
            [
                '        <div class="team-summary" aria-label="Team career summary">',
                '          <div class="summary-stat">',
                f"            <strong>{state_champion_count}</strong>",
                "            <span>State Champions</span>",
                "          </div>",
                "",
                '          <div class="summary-divider"></div>',
                "",
                '          <div class="summary-stat">',
                f"            <strong>{state_placer_count}</strong>",
                "            <span>State Placers</span>",
                "          </div>",
                "",
                '          <div class="summary-divider"></div>',
                "",
                '          <div class="summary-stat">',
                f"            <strong>{state_qualifier_count}</strong>",
                "            <span>State Qualifiers</span>",
                "          </div>",
                "        </div>",
            ]
        )

    coach_bios = _COACH_BIOS.get(team.url_path_slug, {})
    if coach_bios:
        coach_text = "coach" if len(coach_bios) == 1 else "coaches"
        parts.extend(
            [
                '<aside class="team-coach-bios" aria-label="Historical coaches">',
                '  <span class="coach-bios-label">FROM THE ARCHIVE</span>',
                "  <p>",
                f"    Learn about the {coach_text} who shaped this club:",
            ]
        )

        for i, (slug, coach_name) in enumerate(coach_bios.items()):
            if i != 0:
                parts.append('    <span class="coach-bios-separator">&middot;</span>')

            parts.append(f'    <a href="/bios/{slug}/">{coach_name}</a>')

        parts.extend(["  </p>", "</aside>"])

    parts.extend(
        [
            "      </header>",
            "",
            '      <div class="team-content">',
        ]
    )

    parts.extend(_get_champs_html_parts(static_root, qualifiers))
    parts.extend(_get_placers_html_parts(static_root, qualifiers))
    parts.extend(_get_qualifiers_html_parts(static_root, qualifiers, name))

    parts.extend(
        [
            "      </div>",
            "",
            '      <footer class="footer">',
            "        <p>",
            "          An independent project preserving and exploring the history of",
            "          Illinois youth wrestling.",
            "        </p>",
            "",
            "        <p>",
            "          Created by Coach",
            '          <a href="/bios/danny-hermes/">Danny Hermes</a>',
            "        </p>",
            "      </footer>",
            "    </main>",
            "  </body>",
            "</html>",
        ]
    )

    soup = bs4.BeautifulSoup("\n".join(parts), features="html.parser")
    return soup.prettify(formatter="html")


def main() -> None:
    static_root = _HERE.parent / "static" / "static"
    teams_root = static_root / "teams"
    teams_root.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(_HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        teams = _get_team_info(connection)
        landing_html = _teams_landing_html(teams)
        with open(teams_root / "index.html", "w") as file_obj:
            file_obj.write(landing_html)

        for team in teams:
            qualifiers = _get_all_qualifiers(connection, team.id_)
            team_html = _get_team_html(static_root, team, qualifiers)
            with_id = teams_root / team.url_path_slug
            with_id.mkdir(parents=True, exist_ok=True)
            with open(with_id / "index.html", "w") as file_obj:
                file_obj.write(team_html)


if __name__ == "__main__":
    main()
