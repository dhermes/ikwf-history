# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import html
import pathlib
import sqlite3
from typing import Literal, NamedTuple

import bracket_utils
import bs4
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
_MAX_MATCH_ID = 54


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class TournamentConfig(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    year: int
    wrestleback_type: bracket_utils.WrestlebackType
    medalist_count: int


def _get_all_tournaments(
    connection: sqlite3.Connection,
) -> dict[int, list[TournamentConfig]]:
    all_tournaments_sql = _get_sql("_all-tournaments.sql")
    cursor = connection.cursor()
    cursor.execute(all_tournaments_sql)
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()

    result: dict[int, list[TournamentConfig]] = {}
    for row in rows:
        config = TournamentConfig(**row)
        result.setdefault(config.year, []).append(config)

    return result


def _get_all_brackets(
    connection: sqlite3.Connection, tournament_id: int
) -> list[tuple[str, int]]:
    all_brackets_sql = _get_sql("_all-brackets.sql")
    cursor = connection.cursor()
    bind_parameters = {"tournament_id": tournament_id}
    cursor.execute(all_brackets_sql, bind_parameters)
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()

    result: list[tuple[str, int]] = []
    for row in rows:
        result.append((row["division"], row["weight"]))

    return result


class MatchData(_ForbidExtra):
    match_slot_id: int
    bout_number: int | None
    match_slot: bracket_utils.MatchSlot
    top_name: str | None
    top_team: str | None
    top_score: int | None
    bottom_name: str | None
    bottom_team: str | None
    bottom_score: int | None
    top_win: bool | None
    result: str


def _get_match_data(
    connection: sqlite3.Connection,
    division: bracket_utils.Division,
    weight: int,
    tournament_id: int,
) -> list[MatchData]:
    match_data_sql = _get_sql("_match-data.sql")
    cursor = connection.cursor()
    bind_parameters = {
        "weight": weight,
        "division": division,
        "tournament_id": tournament_id,
    }
    cursor.execute(match_data_sql, bind_parameters)

    rows: list[MatchData] = []
    for row in cursor.fetchall():
        keep_row = dict(row)
        rows.append(MatchData(**keep_row))

    cursor.close()

    return rows


class JSONBrackets(pydantic.RootModel[list[MatchData]]):
    pass


def _render_bracket_json(
    api_root: pathlib.Path,
    year: int,
    division: bracket_utils.Division,
    weight: int,
    match_data_rows: list[MatchData],
):
    division_path = bracket_utils.get_division_path(division)
    destination = api_root / "brackets" / str(year) / division_path
    destination.mkdir(parents=True, exist_ok=True)
    json_path = destination / f"{weight}.json"

    to_serialize = JSONBrackets(root=match_data_rows)
    with open(json_path, "w") as file_obj:
        file_obj.write(to_serialize.model_dump_json(indent=2))
        file_obj.write("\n")


def _get_match_map(match_data_rows: list[MatchData]) -> dict[int, MatchData]:
    result: dict[int, MatchData] = {}
    for row in match_data_rows:
        if row.match_slot_id in result:
            raise KeyError("Duplicate", row.match_slot_id)

        result[row.match_slot_id] = row

    return result


class Participant(NamedTuple):
    full_name: str
    team: str


BracketPosition = Literal["top", "bottom"]


def _get_participant(
    match: MatchData, bracket_position: BracketPosition
) -> Participant | None:
    if bracket_position == "top":
        full_name = match.top_name
        team = match.top_team
    elif bracket_position == "bottom":
        full_name = match.bottom_name
        team = match.bottom_team
    else:
        raise NotImplementedError(bracket_position)

    if full_name is None:
        if team is not None:
            raise ValueError(
                "Team and full name must both be set or null", team, full_name
            )

        return None

    if team is None:
        raise ValueError("Team and full name must both be set or null", team, full_name)

    return Participant(full_name=full_name, team=team)


def _maybe_add_participant(
    match: MatchData,
    bracket_position: BracketPosition,
    participant_map: dict[Participant, int],
) -> None:
    participant = _get_participant(match, bracket_position)
    if participant is None:
        return

    if participant in participant_map:
        return

    participant_id = len(participant_map)
    participant_map[participant] = participant_id
    if len(set(participant_map.values())) != len(participant_map):
        raise ValueError("Duplicate participant IDs", participant_map)


def _get_participant_map(
    match_map: dict[int, MatchData],
) -> dict[Participant, int]:
    result: dict[Participant, int] = {}

    # Only consider participants from the championship side **FIRST**
    # (where the match ordering is somewhat reliable)
    for match_slot_id in range(1, _MAX_MATCH_ID + 1):
        match = match_map.get(match_slot_id)
        if match is None:
            continue

        if not match.match_slot.startswith("championship_"):
            continue

        _maybe_add_participant(match, "top", result)
        _maybe_add_participant(match, "bottom", result)

    # Now consider participants from the consolation and place matches
    # (e.g. for 1999 where we have partial brackets)
    for match_slot_id in range(1, _MAX_MATCH_ID + 1):
        match = match_map.get(match_slot_id)
        if match is None:
            continue

        if match.match_slot.startswith("championship_"):
            continue

        _maybe_add_participant(match, "top", result)
        _maybe_add_participant(match, "bottom", result)

    if len(result) > 24:
        raise RuntimeError("Unexpected participant map")

    return result


def _get_included_images(
    static_root: pathlib.Path, year: int, division: bracket_utils.Division, weight: int
) -> list[str]:
    filenames: list[str] = []

    filename = f"{year}-{division}-{weight}.jpg"
    image_path = static_root / "images" / filename
    if image_path.is_file():
        filenames.append(filename)

    filename = f"{year}-{division}-{weight}.png"
    image_path = static_root / "images" / filename
    if image_path.is_file():
        filenames.append(filename)

    return filenames


def _get_html_title(year: int, division: bracket_utils.Division, weight: int) -> str:
    division_display = bracket_utils.get_division_display(division)
    return f"{division_display} {weight} ({year})"


def _render_html_head(title: str) -> str:
    return "\n".join(
        [
            "<head>",
            f"  <title>{html.escape(title)}</title>",
            '  <link href="/css/brackets-viewer.98d9c077.min.css" rel="stylesheet" />',
            "</head>",
        ]
    )


def _format_null(value: int | None) -> str:
    if value is None:
        return "&nbsp;"
    return str(value)


def _result_score_str(score: int | None, win: bool | None) -> str:
    if score is not None:
        return str(score)

    if win is None:
        return ""

    if win:
        return "W"

    return "L"


def _render_participant_html(
    match: MatchData | None,
    bracket_position: BracketPosition,
    participant_map: dict[Participant, int],
    include_team_span: bool = False,
) -> list[str]:
    if match is None:
        return [
            '<div class="participant">',
            '  <div class="name bye">&nbsp;</div>',
            '  <div class="result"></div>',
            "</div>",
        ]

    participant = _get_participant(match, bracket_position)
    if participant is None:
        return [
            '<div class="participant">',
            '  <div class="name bye">&nbsp;</div>',
            '  <div class="result"></div>',
            "</div>",
        ]

    participant_id = participant_map.get(participant)
    if participant_id is None:
        raise RuntimeError("Cannot find participant", participant)

    if bracket_position == "top":
        extra_class = "win" if match.top_win else "loss"
        result_score = _result_score_str(match.top_score, match.top_win)
    elif bracket_position == "bottom":
        extra_class = "loss" if match.top_win else "win"
        result_score = _result_score_str(match.bottom_score, not match.top_win)
    else:
        raise NotImplementedError(bracket_position)

    with_team = f"{participant.full_name} ({participant.team})"
    participant_class = f"participant {extra_class}"
    if match.top_win is None:
        participant_class = "participant"
        result_score = ""

    parts: list[str] = [
        "<div",
        f'  class="{participant_class}"',
        f'  data-participant-id="{participant_id}"',
        f'  title="{html.escape(with_team)}"',
        ">",
        '  <div class="name">',
        f"    {html.escape(participant.full_name)}",
    ]

    if include_team_span:
        parts.append(f"    <span> ({html.escape(participant.team)}) </span>")

    parts.extend(
        [
            "  </div>",
            f'  <div class="result">{html.escape(result_score)}</div>',
            "</div>",
        ]
    )

    return parts


def _match_html(
    match_slot_id: int,
    match_map: dict[int, MatchData],
    participant_map: dict[Participant, int],
    match_class: str,
    opponents_class: str,
    include_team_span: bool = False,
) -> list[str]:
    match_slot = bracket_utils.get_match_slot_from_id(match_slot_id)
    match = match_map.get(match_slot_id)
    bout_number = None
    result = ""
    if match is not None:
        bout_number = match.bout_number
        result = match.result

    bout_number_str = _format_null(bout_number)
    parts: list[str] = [
        "<div",
        f'  class="{match_class}"',
        f'  data-match-id="{match_slot_id}"',
        f'  data-match-slot="{match_slot}"',
        ">",
        f'  <div class="{opponents_class}">',
    ]

    parts.extend(
        _render_participant_html(
            match, "top", participant_map, include_team_span=include_team_span
        )
    )
    parts.extend(
        _render_participant_html(
            match, "bottom", participant_map, include_team_span=include_team_span
        )
    )

    parts.extend(
        [
            '    <div class="match-info">',
            f'      <div class="bout-number">{bout_number_str}</div>',
            f'      <div class="match-result">{html.escape(result)}</div>',
            "    </div>",
            "  </div>",
            "</div>",
        ]
    )
    return parts


def _render_r32_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round first-match" data-round-id="0">',
        "  <h3>Preliminaries</h3>",
    ]

    for match_slot_id in range(1, 17):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents",
                include_team_span=True,
            )
        )

    parts.append("</article>")
    return parts


def _render_r16_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="1">',
        "  <h3>R16</h3>",
    ]

    for match_slot_id in range(17, 25):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents connect-previous",
            )
        )

    parts.append("</article>")
    return parts


def _render_quarterfinal_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="2">',
        "  <h3>Quarterfinals</h3>",
    ]

    for match_slot_id in range(33, 37):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents connect-previous",
            )
        )

    parts.append("</article>")
    return parts


def _render_semifinal_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="3">',
        "  <h3>Semifinals</h3>",
    ]

    for match_slot_id in range(45, 47):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents connect-previous",
            )
        )

    parts.append("</article>")
    return parts


def _render_first_place_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="4">',
        "  <h3>First Place</h3>",
    ]

    parts.extend(
        _match_html(
            54,
            match_map,
            participant_map,
            "match",
            "opponents connect-previous",
        )
    )

    parts.append("</article>")
    return parts


def _render_championship_html(
    match_map: dict[int, MatchData],
    participant_map: dict[Participant, int],
) -> list[str]:
    parts: list[str] = [
        '<section class="bracket" data-group-id="0">',
        "  <h2>Championship</h2>",
        '  <div class="rounds">',
    ]

    parts.extend(_render_r32_html(match_map, participant_map))
    parts.extend(_render_r16_html(match_map, participant_map))
    parts.extend(_render_quarterfinal_html(match_map, participant_map))
    parts.extend(_render_semifinal_html(match_map, participant_map))
    parts.extend(_render_first_place_html(match_map, participant_map))

    parts.extend(
        [
            "  </div>",
            "</section>",
        ]
    )
    return parts


def _render_consolation_round2_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="6">',
        "  <h3>Round 1</h3>",
    ]

    for match_slot_id in range(25, 33):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents straight",
            )
        )

    parts.append("</article>")
    return parts


def _render_consolation_round3_html(
    match_map: dict[int, MatchData],
    participant_map: dict[Participant, int],
    config: TournamentConfig,
) -> list[str]:
    if config.wrestleback_type == "full":
        round_name = "Round 2"
        opponents_class = "opponents connect-previous"
    elif config.wrestleback_type == "follow_leader_semifinal":
        round_name = "Round 1"
        opponents_class = "opponents"
    else:
        raise NotImplementedError(config.wrestleback_type)

    parts: list[str] = [
        '<article class="round" data-round-id="7">',
        f"  <h3>{round_name}</h3>",
    ]

    for match_slot_id in range(37, 41):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next straight",
                opponents_class,
            )
        )

    parts.append("</article>")
    return parts


def _render_consolation_round4_blood_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="8">',
        "  <h3>Blood Round</h3>",
    ]

    for match_slot_id in range(41, 45):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents connect-previous straight",
            )
        )

    parts.append("</article>")
    return parts


def _render_consolation_round5_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="9">',
        "  <h3>Quarterfinals</h3>",
    ]

    for match_slot_id in range(47, 49):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next straight",
                "opponents connect-previous",
            )
        )

    parts.append("</article>")
    return parts


def _render_consolation_round6_semi_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="10">',
        "  <h3>Semifinals</h3>",
    ]

    for match_slot_id in range(49, 51):
        parts.extend(
            _match_html(
                match_slot_id,
                match_map,
                participant_map,
                "match connect-next",
                "opponents connect-previous straight",
            )
        )

    parts.append("</article>")
    return parts


def _render_consolation_third_place_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<article class="round" data-round-id="11">',
        "  <h3>Third Place</h3>",
    ]

    parts.extend(
        _match_html(
            53,
            match_map,
            participant_map,
            "match",
            "opponents connect-previous",
        )
    )

    parts.append("</article>")
    return parts


def _render_consolation_html(
    match_map: dict[int, MatchData],
    participant_map: dict[Participant, int],
    config: TournamentConfig,
) -> list[str]:
    parts: list[str] = [
        '<section class="bracket" data-group-id="1">',
        "  <h2>Consolation</h2>",
        '  <div class="rounds">',
    ]

    if config.wrestleback_type == "full":
        parts.extend(_render_consolation_round2_html(match_map, participant_map))

    parts.extend(_render_consolation_round3_html(match_map, participant_map, config))
    parts.extend(_render_consolation_round4_blood_html(match_map, participant_map))
    parts.extend(_render_consolation_round5_html(match_map, participant_map))
    parts.extend(_render_consolation_round6_semi_html(match_map, participant_map))
    parts.extend(_render_consolation_third_place_html(match_map, participant_map))

    parts.extend(
        [
            "  </div>",
            "</section>",
        ]
    )
    return parts


def _render_fifth_place_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<section class="bracket" data-group-id="2">',
        "  <h2>Fifth Place</h2>",
        '  <div class="rounds">',
        '    <article class="round" data-round-id="12">',
        "      <h3>Fifth Place</h3>",
    ]

    parts.extend(_match_html(52, match_map, participant_map, "match", "opponents"))

    parts.extend(
        [
            "    </article>",
            "  </div>",
            "</section>",
        ]
    )
    return parts


def _render_seventh_place_html(
    match_map: dict[int, MatchData], participant_map: dict[Participant, int]
) -> list[str]:
    parts: list[str] = [
        '<section class="bracket" data-group-id="3">',
        "  <h2>Seventh Place</h2>",
        '  <div class="rounds">',
        '    <article class="round" data-round-id="13">',
        "      <h3>Seventh Place</h3>",
    ]

    parts.extend(_match_html(51, match_map, participant_map, "match", "opponents"))

    parts.extend(
        [
            "      </div>",
            "    </article>",
            "  </div>",
            "</section>",
        ]
    )
    return parts


def _render_bracket_html(
    static_root: pathlib.Path,
    config: TournamentConfig,
    division: bracket_utils.Division,
    weight: int,
    match_data_rows: list[MatchData],
) -> None:
    match_map = _get_match_map(match_data_rows)
    participant_map = _get_participant_map(match_map)
    included_images = _get_included_images(static_root, config.year, division, weight)

    html_title = _get_html_title(config.year, division, weight)
    parts: list[str] = ["<html>"]
    parts.extend(
        [
            _render_html_head(html_title),
            "<body>",
            '  <div class="brackets-viewer" id="bracket">',
            f"    <h1>{html.escape(html_title)}</h1>",
        ]
    )
    parts.extend(_render_championship_html(match_map, participant_map))
    parts.extend(_render_consolation_html(match_map, participant_map, config))
    parts.extend(_render_fifth_place_html(match_map, participant_map))
    if config.medalist_count == 8:
        parts.extend(_render_seventh_place_html(match_map, participant_map))

    for included_image in included_images:
        parts.append(f'<img src="/images/{included_image}" width="100%" />')

    parts.extend(
        [
            "    </div>",
            '    <script defer="" src="/js/add-hover.e70024f1.js"></script>',
            "  </body>",
            "</html>",
        ]
    )

    soup = bs4.BeautifulSoup("\n".join(parts), features="html.parser")
    formatted_html = soup.prettify(formatter="html")

    division_path = bracket_utils.get_division_path(division)
    destination = static_root / "brackets" / str(config.year) / division_path
    destination.mkdir(parents=True, exist_ok=True)
    html_path = destination / f"{weight}.html"

    with open(html_path, "w") as file_obj:
        file_obj.write(formatted_html)


def _render_base_brackets_html(
    static_root: pathlib.Path, tournament_years: list[int]
) -> None:
    parts: list[str] = [
        "<html>",
        "  <head>",
        "    <title>Brackets</title>",
        '    <link href="/css/tournament-view.fb678ab0.min.css" rel="stylesheet" />',
        "  </head>",
        "  <body>",
        '    <div class="tournament-view">',
        "      <h1>Brackets</h1>",
        "      <ul>",
    ]

    for year in tournament_years:
        parts.append(f'<li><a href="/brackets/{year}/index.html">{year}</a></li>')

    parts.extend(
        [
            "      </ul>",
            "    </div>",
            "  </body>",
            "</html>",
        ]
    )

    soup = bs4.BeautifulSoup("\n".join(parts), features="html.parser")
    formatted_html = soup.prettify(formatter="html")

    destination = static_root / "brackets"
    destination.mkdir(parents=True, exist_ok=True)
    html_path = destination / "index.html"

    with open(html_path, "w") as file_obj:
        file_obj.write(formatted_html)


def main() -> None:
    static_root = HERE.parent / "static" / "static"
    api_root = static_root / "api" / "v20250408"

    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        all_tournaments = _get_all_tournaments(connection)
        tournament_years = sorted(all_tournaments.keys())
        for year in tournament_years:
            for config in all_tournaments[year]:
                tournament_brackets = _get_all_brackets(connection, config.id_)
                for division, weight in tournament_brackets:
                    match_data_rows = _get_match_data(
                        connection, division, weight, config.id_
                    )

                    if len(match_data_rows) == 0:
                        continue

                    _render_bracket_json(
                        api_root, year, division, weight, match_data_rows
                    )
                    _render_bracket_html(
                        static_root, config, division, weight, match_data_rows
                    )

    _render_base_brackets_html(static_root, tournament_years)


if __name__ == "__main__":
    main()
