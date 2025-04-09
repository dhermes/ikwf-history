# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import html
import pathlib
import sqlite3
from typing import Literal, NamedTuple

import bs4
import pydantic

HERE = pathlib.Path(__file__).resolve().parent


@functools.cache
def _get_sql(filename: str) -> str:
    with open(HERE / filename) as file_obj:
        return file_obj.read()


def _to_bool(value: int) -> bool:
    """Convert a SQLite BOOLEAN to a Python bool."""
    if value == 0:
        return False

    if value == 1:
        return True

    raise ValueError(value)


def _get_all_tournaments(connection: sqlite3.Connection) -> dict[int, list[int]]:
    all_tournaments_sql = _get_sql("_all-tournaments.sql")
    cursor = connection.cursor()
    cursor.execute(all_tournaments_sql)
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()

    result: dict[int, list[int]] = {}
    for row in rows:
        year = row["year"]
        tournament_id = row["id"]
        result.setdefault(year, []).append(tournament_id)

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


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


MatchSlot = Literal[
    "championship_r32_01",
    "championship_r32_02",
    "championship_r32_03",
    "championship_r32_04",
    "championship_r32_05",
    "championship_r32_06",
    "championship_r32_07",
    "championship_r32_08",
    "championship_r32_09",
    "championship_r32_10",
    "championship_r32_11",
    "championship_r32_12",
    "championship_r32_13",
    "championship_r32_14",
    "championship_r32_15",
    "championship_r32_16",
    "championship_r16_01",
    "championship_r16_02",
    "championship_r16_03",
    "championship_r16_04",
    "championship_r16_05",
    "championship_r16_06",
    "championship_r16_07",
    "championship_r16_08",
    "consolation_round2_01",
    "consolation_round2_02",
    "consolation_round2_03",
    "consolation_round2_04",
    "consolation_round2_05",
    "consolation_round2_06",
    "consolation_round2_07",
    "consolation_round2_08",
    "championship_quarter_01",
    "championship_quarter_02",
    "championship_quarter_03",
    "championship_quarter_04",
    "consolation_round3_01",
    "consolation_round3_02",
    "consolation_round3_03",
    "consolation_round3_04",
    "consolation_round4_blood_01",
    "consolation_round4_blood_02",
    "consolation_round4_blood_03",
    "consolation_round4_blood_04",
    "championship_semi_01",
    "championship_semi_02",
    "consolation_round5_01",
    "consolation_round5_02",
    "consolation_round6_semi_01",
    "consolation_round6_semi_02",
    "consolation_seventh_place",
    "consolation_fifth_place",
    "consolation_third_place",
    "championship_first_place",
]


def _match_slot_for_id(match_slot_id: int) -> MatchSlot:
    if match_slot_id == 1:
        return "championship_r32_01"
    if match_slot_id == 2:
        return "championship_r32_02"
    if match_slot_id == 3:
        return "championship_r32_03"
    if match_slot_id == 4:
        return "championship_r32_04"
    if match_slot_id == 5:
        return "championship_r32_05"
    if match_slot_id == 6:
        return "championship_r32_06"
    if match_slot_id == 7:
        return "championship_r32_07"
    if match_slot_id == 8:
        return "championship_r32_08"
    if match_slot_id == 9:
        return "championship_r32_09"
    if match_slot_id == 10:
        return "championship_r32_10"
    if match_slot_id == 11:
        return "championship_r32_11"
    if match_slot_id == 12:
        return "championship_r32_12"
    if match_slot_id == 13:
        return "championship_r32_13"
    if match_slot_id == 14:
        return "championship_r32_14"
    if match_slot_id == 15:
        return "championship_r32_15"
    if match_slot_id == 16:
        return "championship_r32_16"
    if match_slot_id == 17:
        return "championship_r16_01"
    if match_slot_id == 18:
        return "championship_r16_02"
    if match_slot_id == 19:
        return "championship_r16_03"
    if match_slot_id == 20:
        return "championship_r16_04"
    if match_slot_id == 21:
        return "championship_r16_05"
    if match_slot_id == 22:
        return "championship_r16_06"
    if match_slot_id == 23:
        return "championship_r16_07"
    if match_slot_id == 24:
        return "championship_r16_08"
    if match_slot_id == 25:
        return "consolation_round2_01"
    if match_slot_id == 26:
        return "consolation_round2_02"
    if match_slot_id == 27:
        return "consolation_round2_03"
    if match_slot_id == 28:
        return "consolation_round2_04"
    if match_slot_id == 29:
        return "consolation_round2_05"
    if match_slot_id == 30:
        return "consolation_round2_06"
    if match_slot_id == 31:
        return "consolation_round2_07"
    if match_slot_id == 32:
        return "consolation_round2_08"
    if match_slot_id == 33:
        return "championship_quarter_01"
    if match_slot_id == 34:
        return "championship_quarter_02"
    if match_slot_id == 35:
        return "championship_quarter_03"
    if match_slot_id == 36:
        return "championship_quarter_04"
    if match_slot_id == 37:
        return "consolation_round3_01"
    if match_slot_id == 38:
        return "consolation_round3_02"
    if match_slot_id == 39:
        return "consolation_round3_03"
    if match_slot_id == 40:
        return "consolation_round3_04"
    if match_slot_id == 41:
        return "consolation_round4_blood_01"
    if match_slot_id == 42:
        return "consolation_round4_blood_02"
    if match_slot_id == 43:
        return "consolation_round4_blood_03"
    if match_slot_id == 44:
        return "consolation_round4_blood_04"
    if match_slot_id == 45:
        return "championship_semi_01"
    if match_slot_id == 46:
        return "championship_semi_02"
    if match_slot_id == 47:
        return "consolation_round5_01"
    if match_slot_id == 48:
        return "consolation_round5_02"
    if match_slot_id == 49:
        return "consolation_round6_semi_01"
    if match_slot_id == 50:
        return "consolation_round6_semi_02"
    if match_slot_id == 51:
        return "consolation_seventh_place"
    if match_slot_id == 52:
        return "consolation_fifth_place"
    if match_slot_id == 53:
        return "consolation_third_place"
    if match_slot_id == 54:
        return "championship_first_place"
    raise NotImplementedError(match_slot_id)


class BracketJSON(_ForbidExtra):
    match_slot_id: int
    bout_number: int | None
    match_slot: MatchSlot
    top_full_name: str | None
    top_team: str | None
    top_team_acronym: str | None
    top_score: int | None
    bottom_full_name: str | None
    bottom_team: str | None
    bottom_team_acronym: str | None
    bottom_score: int | None
    top_win: bool
    result: str


Division = Literal[
    "bantam",
    "intermediate",
    "novice",
    "senior",
    "bantam_girls",
    "intermediate_girls",
    "novice_girls",
    "senior_girls",
]


def _get_bracket_json(
    connection: sqlite3.Connection, division: Division, weight: int, tournament_id: int
) -> list[BracketJSON]:
    bracket_json_sql = _get_sql("_bracket-json.sql")
    cursor = connection.cursor()
    bind_parameters = {
        "weight": weight,
        "division": division,
        "tournament_id": tournament_id,
    }
    cursor.execute(bracket_json_sql, bind_parameters)

    rows: list[BracketJSON] = []
    for row in cursor.fetchall():
        keep_row = dict(row)
        keep_row["top_win"] = _to_bool(keep_row["top_win"])
        rows.append(BracketJSON(**keep_row))

    cursor.close()

    return rows


class JSONBrackets(pydantic.RootModel[list[BracketJSON]]):
    pass


def _render_bracket_json(
    api_root: pathlib.Path,
    year: int,
    division: Division,
    weight: int,
    bracket_json_rows: list[BracketJSON],
):
    division_path = division.replace("_", "-")
    destination = api_root / "brackets" / str(year) / division_path
    destination.mkdir(parents=True, exist_ok=True)
    json_path = destination / f"{weight}.json"

    to_serialize = JSONBrackets(root=bracket_json_rows)
    with open(json_path, "w") as file_obj:
        file_obj.write(to_serialize.model_dump_json(indent=2))
        file_obj.write("\n")


def _get_division_display(division: Division) -> str:
    if division == "bantam":
        return "Bantam"

    if division == "intermediate":
        return "Intermediate"

    if division == "novice":
        return "Novice"

    if division == "senior":
        return "Senior"

    if division == "bantam_girls":
        return "Girls Bantam"

    if division == "intermediate_girls":
        return "Girls Intermediate"

    if division == "novice_girls":
        return "Girls Novice"

    if division == "senior_girls":
        return "Girls Senior"

    raise NotImplementedError(division)


def _get_html_title(year: int, division: Division, weight: int) -> str:
    division_display = _get_division_display(division)
    return f"{division_display} {weight} ({year})"


class Participant(NamedTuple):
    full_name: str
    team: str


def _render_html_head(title: str) -> str:
    return "\n".join(
        [
            "<head>",
            f"  <title>{html.escape(title)}</title>",
            '  <link href="/css/brackets-viewer.98d9c077.min.css" rel="stylesheet" />',
            "</head>",
        ]
    )


BracketPosition = Literal["top", "bottom"]


def _result_score_str(score: int | None, win: bool) -> str:
    if score is not None:
        return str(score)

    if win:
        return "W"

    return "L"


def _render_participant_html(
    match: BracketJSON | None,
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
    parts: list[str] = [
        "<div",
        f'  class="participant {extra_class}"',
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
    match_map: dict[int, BracketJSON],
    participant_map: dict[Participant, int],
    match_class: str,
    opponents_class: str,
    include_team_span: bool = False,
) -> list[str]:
    match_slot = _match_slot_for_id(match_slot_id)
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON],
    participant_map: dict[Participant, int],
    full_wrestlebacks: bool,
) -> list[str]:
    round_name = "Round 2"
    opponents_class = "opponents connect-previous"
    if not full_wrestlebacks:
        round_name = "Round 1"
        opponents_class = "opponents"

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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON],
    participant_map: dict[Participant, int],
    full_wrestlebacks: bool,
) -> list[str]:
    parts: list[str] = [
        '<section class="bracket" data-group-id="1">',
        "  <h2>Consolation</h2>",
        '  <div class="rounds">',
    ]

    if full_wrestlebacks:
        parts.extend(_render_consolation_round2_html(match_map, participant_map))

    parts.extend(
        _render_consolation_round3_html(match_map, participant_map, full_wrestlebacks)
    )
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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
    match_map: dict[int, BracketJSON], participant_map: dict[Participant, int]
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


def _get_match_map(bracket_json_rows: list[BracketJSON]) -> dict[int, BracketJSON]:
    result: dict[int, BracketJSON] = {}
    for row in bracket_json_rows:
        if row.match_slot_id in result:
            raise KeyError("Duplicate", row.match_slot_id)

        result[row.match_slot_id] = row

    return result


def _get_participant(
    match: BracketJSON, bracket_position: BracketPosition
) -> Participant | None:
    if bracket_position == "top":
        full_name = match.top_full_name
        team = match.top_team
    elif bracket_position == "bottom":
        full_name = match.bottom_full_name
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


def _format_null(value: int | None) -> str:
    if value is None:
        return "&nbsp;"
    return str(value)


def _maybe_add_participant(
    match: BracketJSON,
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
    match_map: dict[int, BracketJSON],
) -> dict[Participant, int]:
    result: dict[Participant, int] = {}

    # Only consider participants from the championship side **FIRST**
    # (where the match ordering is somewhat reliable)
    for match_slot_id in range(1, 55):
        match = match_map.get(match_slot_id)
        if match is None:
            continue

        if not match.match_slot.startswith("championship_"):
            continue

        _maybe_add_participant(match, "top", result)
        _maybe_add_participant(match, "bottom", result)

    # Now consider participants from the consolation and place matches
    # (e.g. for 1999 where we have partial brackets)
    for match_slot_id in range(1, 55):
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


def _render_bracket_html(
    static_root: pathlib.Path,
    year: int,
    division: Division,
    weight: int,
    bracket_json_rows: list[BracketJSON],
):
    match_map = _get_match_map(bracket_json_rows)
    participant_map = _get_participant_map(match_map)
    include_seventh = year >= 2001
    full_wrestlebacks = year >= 2022

    html_title = _get_html_title(year, division, weight)
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
    parts.extend(
        _render_consolation_html(match_map, participant_map, full_wrestlebacks)
    )
    parts.extend(_render_fifth_place_html(match_map, participant_map))
    if include_seventh:
        parts.extend(_render_seventh_place_html(match_map, participant_map))

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

    division_path = division.replace("_", "-")
    destination = static_root / "brackets" / str(year) / division_path
    destination.mkdir(parents=True, exist_ok=True)
    html_path = destination / f"{weight}.html"

    with open(html_path, "w") as file_obj:
        file_obj.write(formatted_html)


def main():
    static_root = HERE.parent / "static" / "static"
    api_root = static_root / "api" / "v20250408"

    with sqlite3.connect(HERE / "ikwf.sqlite") as connection:
        connection.row_factory = sqlite3.Row

        all_tournaments = _get_all_tournaments(connection)
        tournament_years = sorted(all_tournaments.keys())
        for year in tournament_years:
            for tournament_id in all_tournaments[year]:
                tournament_brackets = _get_all_brackets(connection, tournament_id)
                for division, weight in tournament_brackets:
                    bracket_json_rows = _get_bracket_json(
                        connection, division, weight, tournament_id
                    )

                    if len(bracket_json_rows) == 0:
                        continue

                    _render_bracket_json(
                        api_root, year, division, weight, bracket_json_rows
                    )
                    _render_bracket_html(
                        static_root, year, division, weight, bracket_json_rows
                    )


if __name__ == "__main__":
    main()
