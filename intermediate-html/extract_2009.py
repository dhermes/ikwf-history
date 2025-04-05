# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import Any

import bs4
import pydantic

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_INITIAL_ENTRY_INFO: tuple[
    tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition, int], ...
] = (
    ("championship_r32_01", "top", 0),
    ("championship_r32_02", "top", 4),
    ("championship_r32_02", "bottom", 7),
    ("championship_r32_03", "top", 8),
    ("championship_r32_04", "top", 12),
    ("championship_r32_04", "bottom", 15),
    ("championship_r32_05", "top", 16),
    ("championship_r32_06", "top", 20),
    ("championship_r32_06", "bottom", 23),
    ("championship_r32_07", "top", 24),
    ("championship_r32_08", "top", 28),
    ("championship_r32_08", "bottom", 31),
    ("championship_r32_09", "top", 32),
    ("championship_r32_10", "top", 36),
    ("championship_r32_10", "bottom", 39),
    ("championship_r32_11", "top", 40),
    ("championship_r32_12", "top", 44),
    ("championship_r32_12", "bottom", 47),
    ("championship_r32_13", "top", 48),
    ("championship_r32_14", "top", 52),
    ("championship_r32_14", "bottom", 55),
    ("championship_r32_15", "top", 56),
    ("championship_r32_16", "top", 60),
    ("championship_r32_16", "bottom", 62),
)
_NAME_FIXES: dict[str, str] = {
    "Christophe Bartels": "Christopher Bartels",
    "Christophe Dranka": "Christopher Dranka",
    "Christophe Golden": "Christopher Golden",
    "Christophe Hiscock": "Christopher Hiscock",
    "Christophe Malone": "Christopher Malone",
    "Michael Mcnulty-ferguso": "Michael Mcnulty-ferguson",
    "Robert Vodicka-hirschm": "Robert Vodicka-hirschmann",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Carl Witt, Iii", "TOMCAT WC"): bracket_utils.Competitor(
        first_name="Carl", last_name="Witt", suffix="III", team="TOMCAT WC"
    ),
    (
        "Floyd Lomelino Iv",
        "JACKSONVILLE AREA YOUTH WRESTLING",
    ): bracket_utils.Competitor(
        first_name="Floyd",
        last_name="Lomelino",
        suffix="IV",
        team="JACKSONVILLE AREA YOUTH WRESTLING",
    ),
    ("James Zeigler Jr.", "EDWARDSVILLE WC"): bracket_utils.Competitor(
        first_name="James",
        last_name="Zeigler",
        suffix="Jr",
        team="EDWARDSVILLE WC",
    ),
    ("Larry Thomas Jr", "IRON MAN"): bracket_utils.Competitor(
        first_name="Larry", last_name="Thomas", suffix="Jr", team="IRON MAN"
    ),
    ("Lonnie Cleveland Iii", "UNITED SOUTHERN ALLSTARS"): bracket_utils.Competitor(
        first_name="Lonnie",
        last_name="Cleveland",
        suffix="III",
        team="UNITED SOUTHERN ALLSTARS",
    ),
    ("Michael Johnson Jr", "DOWNERS GROVE COUGARS"): bracket_utils.Competitor(
        first_name="Michael",
        last_name="Johnson",
        suffix="Jr",
        team="DOWNERS GROVE COUGARS",
    ),
    ("Miguel Silva Jr", "MARTINEZ FOX VALLEY ELITE"): bracket_utils.Competitor(
        first_name="Miguel",
        last_name="Silva",
        suffix="Jr",
        team="MARTINEZ FOX VALLEY ELITE",
    ),
    ("Ronald Shafer Iii", "GRANITE CITY WC"): bracket_utils.Competitor(
        first_name="Ronald",
        last_name="Shafer",
        suffix="III",
        team="GRANITE CITY WC",
    ),
    ("Shavez Hawkins Jr", "CROSSTOWN WC"): bracket_utils.Competitor(
        first_name="Shavez", last_name="Hawkins", suffix="Jr", team="CROSSTOWN WC"
    ),
}


MatchSlotMap = dict[
    tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition],
    list[bracket_utils.CompetitorRaw],
]


def _normalize_division(division_display: str) -> bracket_utils.Division:
    if division_display.strip() == "Novice":
        return "novice"

    if division_display.strip() == "Senior":
        return "senior"

    raise NotImplementedError(division_display)


def _team_scores_from_html(html: Any) -> list[bracket_utils.TeamScore]:
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html))

    soup = bs4.BeautifulSoup(html, features="html.parser")

    scores: list[bracket_utils.TeamScore] = []
    for tr in soup.find_all("tr"):
        all_td = tr.find_all("td")
        all_th = tr.find_all("th")
        if len(all_td) == 0 and len(all_th) == 4:
            continue

        if len(all_td) != 4 or len(all_th) != 0:
            raise RuntimeError("Invariant violation", tr)

        # NOTE: We also know `acronym=all_td[2].text` but have no use for it
        #       right now.
        scores.append(
            bracket_utils.TeamScore(team=all_td[1].text, score=float(all_td[3].text))
        )

    return scores


def _parse_team_scores(
    selenium_team_scores: Any,
) -> dict[bracket_utils.Division, list[bracket_utils.TeamScore]]:
    if not isinstance(selenium_team_scores, dict):
        raise TypeError("Unexpected value", type(selenium_team_scores))

    result: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    for division_display, html in selenium_team_scores.items():
        division = _normalize_division(division_display)
        if division in result:
            raise KeyError("Duplicate value", division)

        scores = _team_scores_from_html(html)
        result[division] = scores

    return result


class Deductions(pydantic.RootModel[list[bracket_utils.Deduction]]):
    pass


def _get_opening_bout_numbers(soup: bs4.BeautifulSoup) -> list[int]:
    bout_number_links: list[bs4.Tag] = soup.find_all("a", class_="segment-track")
    bouts: dict[int, bs4.Tag] = {}

    for anchor in bout_number_links:
        href = anchor.get("href", "")
        if isinstance(href, list):
            raise RuntimeError("Invariant violation", anchor)

        if not href.startswith("javascript:openBoutSheet"):
            continue

        if anchor.text == "_":
            continue

        bout_number = int(anchor.text)
        if bout_number in bouts:
            raise KeyError("Repeat bout number", bout_number, anchor)

        bouts[bout_number] = anchor

    bout_numbers = sorted(bouts.keys())
    if len(bout_numbers) < 8:
        raise NotImplementedError

    start_number = bout_numbers[0]
    first_bouts = bout_numbers[:8]
    expected = list(range(start_number, start_number + 8))
    if first_bouts != expected:
        raise RuntimeError("Invariant violation", bout_numbers)

    return expected


def _is_full_line(wrestler_td: bs4.Tag) -> bool:
    full_line_divs = wrestler_td.find_all("div", class_="full-line")
    if len(full_line_divs) > 1:
        raise RuntimeError("Invariant violation", wrestler_td)

    return len(full_line_divs) > 0


def _get_bout_number(wrestler_td: bs4.Tag) -> int | None:
    td_sibling = wrestler_td.find_next_sibling()
    if td_sibling.name != "td":
        raise RuntimeError("Invariant violation", td_sibling)

    bout_number_links = td_sibling.find_all("a", class_="segment-track")
    if len(bout_number_links) > 1:
        raise RuntimeError("Invariant violation", td_sibling)
    elif len(bout_number_links) == 0:
        return None

    anchor_text = bout_number_links[0].text
    if anchor_text == "_":
        return None

    return int(anchor_text)


def _is_valid_initial_entry(
    wrestler_td: bs4.Tag, bout_number: int | None, opening_bouts: list[int]
) -> bool:
    if _is_full_line(wrestler_td):
        return True

    if bout_number in opening_bouts:
        return True

    if wrestler_td.text == "Bye":
        return True

    return False


def _split_name_team_initial(
    name_team: str, division_scores: list[bracket_utils.TeamScore]
) -> bracket_utils.CompetitorRaw | None:
    if name_team == "Bye":
        return None

    if not name_team.endswith(")"):
        raise RuntimeError("Invariant violation", name_team)

    to_parse = name_team[:-1]

    parts = to_parse.split(" (", 1)
    if len(parts) != 2:
        raise RuntimeError("Invariant violation", name_team)

    name = parts[0]
    team_prefix = parts[1]

    name = _NAME_FIXES.get(name, name)

    matches: list[str] = []
    for score in division_scores:
        if score.team.startswith(team_prefix):
            matches.append(score.team)

    if len(matches) != 1:
        raise RuntimeError("Invariant violation", name_team, matches)

    return bracket_utils.CompetitorRaw(name=name, team=matches[0])


def _initial_entries(
    soup: bs4.BeautifulSoup, division_scores: list[bracket_utils.TeamScore]
) -> MatchSlotMap:
    initial_bout_index = 0
    opening_bouts = _get_opening_bout_numbers(soup)

    all_wrestler_tds = soup.find_all(
        "td", width="100%", align="center", valign="bottom"
    )
    if len(all_wrestler_tds) != 63:
        raise RuntimeError("Invariant violation", len(all_wrestler_tds))

    match_slot_map: MatchSlotMap = {}

    for match_slot, bracket_position, index in _INITIAL_ENTRY_INFO:
        wrestler_td = all_wrestler_tds[index]
        bout_number = _get_bout_number(wrestler_td)
        if bracket_position == "top":
            if bout_number is not None:
                raise RuntimeError("Invariant violation", index)
        else:
            expected_bout_number = opening_bouts[initial_bout_index]
            if bout_number != expected_bout_number:
                raise RuntimeError("Invariant violation", index)
            initial_bout_index += 1

        if not _is_valid_initial_entry(wrestler_td, bout_number, opening_bouts):
            raise RuntimeError("Invariant violation", index, wrestler_td)

        competitor_raw = _split_name_team_initial(wrestler_td.text, division_scores)
        key = match_slot, bracket_position
        if key in match_slot_map:
            raise KeyError("Duplicate", key)

        if competitor_raw is None:
            match_slot_map[key] = []
        else:
            match_slot_map[key] = [competitor_raw]

    return match_slot_map


def _handle_bye(
    winner: str,
    result: str,
    top_competitors: list[bracket_utils.CompetitorRaw],
    bottom_competitors: list[bracket_utils.CompetitorRaw],
) -> tuple[
    bracket_utils.CompetitorRaw | None,
    bracket_utils.CompetitorRaw | None,
    bool | None,
    str,
]:
    top_competitor_names = [competitor.long_name for competitor in top_competitors]
    bottom_competitor_names = [
        competitor.long_name for competitor in bottom_competitors
    ]

    winner_top_index = _matching_index(winner, top_competitor_names)
    winner_bottom_index = _matching_index(winner, bottom_competitor_names)

    if winner_top_index is not None:
        if winner_bottom_index is not None:
            raise RuntimeError("Invariant violation")

        top_competitor = top_competitors[winner_top_index]
        bottom_competitor = None
        top_win = True
    elif winner_bottom_index is not None:
        if winner_top_index is not None:
            raise RuntimeError("Invariant violation")

        top_competitor = None
        bottom_competitor = bottom_competitors[winner_bottom_index]
        top_win = False
    else:
        if winner.strip() != "()":
            raise RuntimeError("Invariant violation")

        return None, None, None, result

    if result != "Bye":
        raise RuntimeError("Invariant violation", result)

    return top_competitor, bottom_competitor, top_win, result


def _matching_index(value: str, choices: list[str | None]) -> int | None:
    matches = [i for i, choice in enumerate(choices) if choice == value]
    if len(matches) == 0:
        return None

    if len(matches) != 1:
        raise RuntimeError("Invariant violation", value, matches, choices)

    return matches[0]


def _handle_match(
    winner: str,
    loser: str,
    result: str,
    top_competitors: list[bracket_utils.CompetitorRaw],
    bottom_competitors: list[bracket_utils.CompetitorRaw],
) -> tuple[bracket_utils.CompetitorRaw, bracket_utils.CompetitorRaw, bool, str]:
    top_competitor_names = [competitor.long_name for competitor in top_competitors]
    bottom_competitor_names = [
        competitor.long_name for competitor in bottom_competitors
    ]

    winner_top_index = _matching_index(winner, top_competitor_names)
    winner_bottom_index = _matching_index(winner, bottom_competitor_names)
    loser_top_index = _matching_index(loser, top_competitor_names)
    loser_bottom_index = _matching_index(loser, bottom_competitor_names)

    if winner_top_index is not None:
        if (
            loser_bottom_index is None
            or winner_bottom_index is not None
            or loser_top_index is not None
        ):
            raise RuntimeError("Invariant violation")

        top_competitor = top_competitors[winner_top_index]
        bottom_competitor = bottom_competitors[loser_bottom_index]
        top_win = True
    elif winner_bottom_index is not None:
        if (
            loser_top_index is None
            or winner_top_index is not None
            or loser_bottom_index is not None
        ):
            raise RuntimeError("Invariant violation")

        top_competitor = top_competitors[loser_top_index]
        bottom_competitor = bottom_competitors[winner_bottom_index]
        top_win = False
    else:
        raise RuntimeError("Invariant violation", winner)

    return top_competitor, bottom_competitor, top_win, result


class MatchWithBracket(pydantic.BaseModel):
    division: bracket_utils.Division
    weight: int
    match: bracket_utils.Match


def _competitor_from_raw(
    value: bracket_utils.CompetitorRaw | None,
) -> bracket_utils.Competitor | None:
    return bracket_utils.competitor_from_raw(value, _NAME_EXCEPTIONS)


def _add_r32_bye(
    index: int,
    division: bracket_utils.Division,
    weight: int,
    matches: list[MatchWithBracket],
    match_slot_map: MatchSlotMap,
) -> None:
    """Add a bye in the Round of 32 for a sectional winner."""
    slot_id = 2 * (index + 1) - 1
    match_slot: bracket_utils.MatchSlot = f"championship_r32_{slot_id:02}"

    competitors = match_slot_map[(match_slot, "top")]
    if len(competitors) != 1:
        raise RuntimeError("Invariant violation", match_slot)
    competitor = competitors[0]

    match = MatchWithBracket(
        division=division,
        weight=weight,
        match=bracket_utils.Match(
            match_slot=match_slot,
            top_competitor=_competitor_from_raw(competitor),
            bottom_competitor=None,
            result="Bye",
            result_type="bye",
            bout_number=None,
            top_win=True,
        ),
    )
    matches.append(match)

    win_position = bracket_utils.next_match_position_win_v1(match_slot)
    match_slot_map.setdefault(win_position, [])
    match_slot_map[win_position].append(competitor)


def _round_line_split(line: str, prefix: str) -> tuple[int, str, str, str]:
    parts = line.split(" :: ")
    if len(parts) != 5:
        raise RuntimeError("Invariant violation", len(parts), line)

    actual_prefix, bout_number_str, winner, loser, result = parts
    if actual_prefix != prefix:
        raise RuntimeError("Unexpected prefix", actual_prefix, prefix, line)

    bout_number = int(bout_number_str)

    return bout_number, winner, loser, result


def _determine_result_type(result: str) -> bracket_utils.ResultType:
    if result.startswith("OT "):
        score_win_str, score_lose_str = result[len("OT ") :].split("-")
        score_win = int(score_win_str)
        score_lose = int(score_lose_str)
        delta = score_win - score_lose
        if not (0 < delta < 8):
            raise ValueError("Unexpected difference", result)

        return "decision"

    if result.startswith("2-OT "):
        score_win_str, score_lose_str = result[len("2-OT ") :].split("-")
        score_win = int(score_win_str)
        score_lose = int(score_lose_str)
        delta = score_win - score_lose
        if not (0 < delta < 8):
            raise ValueError("Unexpected difference", result)

        return "decision"

    if result == "Dec" or result.startswith("Dec "):
        return "decision"

    if result.startswith("Maj "):
        return "major"

    if result.startswith("TF "):
        return "tech"

    if result == "Fall" or result.startswith("Fall "):
        return "fall"

    if result.startswith("Inj. "):
        return "default"

    if result == "FF":
        return "forfeit"

    if result == "NC":
        return "walkover"

    if result == "DQ":
        return "disqualification"

    if result == "Bye":
        return "bye"

    raise NotImplementedError(result)


def _parse_r32(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 8:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(8):
            entry = all_entries[i]
            slot_id = 2 * (i + 1)
            match_slot: bracket_utils.MatchSlot = f"championship_r32_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) > 1:
                raise RuntimeError("Invariant violation", match_slot)

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError("Invariant violation", match_slot)

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            if loser.strip() == "()":
                top_competitor, bottom_competitor, top_win, result = _handle_bye(
                    winner, result, top_competitors, bottom_competitors
                )
            else:
                top_competitor, bottom_competitor, top_win, result = _handle_match(
                    winner, loser, result, top_competitors, bottom_competitors
                )

            winner_competitor = top_competitor
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the top-side wrestler that
            #    had a bye.
            _add_r32_bye(i, division, weight, matches, match_slot_map)

            # 3. Make the `match_slot_map` aware of the loser
            # NOTE: The loser **MIGHT** have a match, **IF** the winner makes
            #       the semifinals. But this is true for another R32 loser so we
            #       need to keep an array.
            lose_position = bracket_utils.next_match_position_lose_v1(match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_r16(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 8:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(8):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"championship_r16_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError("Invariant violation", match_slot)

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            if loser.strip() == "()":
                top_competitor, bottom_competitor, top_win, result = _handle_bye(
                    winner, result, top_competitors, bottom_competitors
                )
            else:
                top_competitor, bottom_competitor, top_win, result = _handle_match(
                    winner, loser, result, top_competitors, bottom_competitors
                )

            winner_competitor = top_competitor
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            # NOTE: The loser **MIGHT** have a match, **IF** the winner makes
            #       the semifinals. But this is true for another R16 loser so we
            #       need to keep an array.
            lose_position = bracket_utils.next_match_position_lose_v1(match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_quarterfinal(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 4:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(4):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"championship_quarter_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            top_competitor, bottom_competitor, top_win, result = _handle_match(
                winner, loser, result, top_competitors, bottom_competitors
            )

            winner_competitor = top_competitor
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = bracket_utils.next_match_position_lose_v1(match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_consolation_round3(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 4:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(4):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"consolation_round3_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) > 2:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 2:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            if loser.strip() == "()":
                top_competitor, bottom_competitor, top_win, result = _handle_bye(
                    winner, result, top_competitors, bottom_competitors
                )
            else:
                top_competitor, bottom_competitor, top_win, result = _handle_match(
                    winner, loser, result, top_competitors, bottom_competitors
                )

            winner_competitor = top_competitor
            if not top_win:
                winner_competitor = bottom_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # Make the `match_slot_map` aware of the winner (loser is eliminated)
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_consolation_round4(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 4:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(4):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = (
                f"consolation_round4_blood_{slot_id:02}"
            )

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            if loser.strip() == "()":
                top_competitor, bottom_competitor, top_win, result = _handle_bye(
                    winner, result, top_competitors, bottom_competitors
                )
            else:
                top_competitor, bottom_competitor, top_win, result = _handle_match(
                    winner, loser, result, top_competitors, bottom_competitors
                )

            winner_competitor = top_competitor
            if not top_win:
                winner_competitor = bottom_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # Make the `match_slot_map` aware of the winner (loser is eliminated)
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_semi_mixed(
    round_name: str,
    semi_match_prefix: str,
    cons_match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 4:
            raise RuntimeError("Invariant violation", all_entries)

        # Semifinals
        for i in range(2):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"championship_semi_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, semi_match_prefix
            )
            top_competitor, bottom_competitor, top_win, result = _handle_match(
                winner, loser, result, top_competitors, bottom_competitors
            )

            winner_competitor = top_competitor
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = bracket_utils.next_match_position_lose_v1(match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

        # Wrestlebacks
        for i in range(2):
            entry = all_entries[i + 2]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"consolation_round5_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, cons_match_prefix
            )
            top_competitor, bottom_competitor, top_win, result = _handle_match(
                winner, loser, result, top_competitors, bottom_competitors
            )

            winner_competitor = top_competitor
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = bracket_utils.next_match_position_lose_v1(match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_consolation_semi(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 2:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(2):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = (
                f"consolation_round6_semi_{slot_id:02}"
            )

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            top_competitor, bottom_competitor, top_win, result = _handle_match(
                winner, loser, result, top_competitors, bottom_competitors
            )

            winner_competitor = top_competitor
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_v1(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = bracket_utils.next_match_position_lose_v1(match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_place_matches(
    round_name: str,
    third_place_prefix: str,
    fifth_place_prefix: str,
    seventh_place_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    prefixes_and_slots: tuple[tuple[str, bracket_utils.MatchSlot]] = (
        (third_place_prefix, "consolation_third_place"),
        (fifth_place_prefix, "consolation_fifth_place"),
        (seventh_place_prefix, "consolation_seventh_place"),
    )

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 3:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(3):
            entry = all_entries[i]
            match_prefix, match_slot = prefixes_and_slots[i]

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            top_competitor, bottom_competitor, top_win, result = _handle_match(
                winner, loser, result, top_competitors, bottom_competitors
            )

            winner_competitor = top_competitor
            if not top_win:
                winner_competitor = bottom_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # NOTE: All of these rounds are **TERMINAL**, so no need to make
            #       `match_slot_map` aware of any of them.

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_championship_matches(
    round_name: str,
    first_place_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    prefixes_and_slots: tuple[tuple[str, bracket_utils.MatchSlot]] = (
        (first_place_prefix, "championship_first_place"),
    )

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 1:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(1):
            entry = all_entries[i]
            match_prefix, match_slot = prefixes_and_slots[i]

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, match_prefix
            )
            top_competitor, bottom_competitor, top_win, result = _handle_match(
                winner, loser, result, top_competitors, bottom_competitors
            )

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=_competitor_from_raw(top_competitor),
                    bottom_competitor=_competitor_from_raw(bottom_competitor),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # NOTE: All of these rounds are **TERMINAL**, so no need to make
            #       `match_slot_map` aware of any of them.

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_rounds(
    selenium_rounds: Any,
    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap],
) -> list[MatchWithBracket]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    matches: list[MatchWithBracket] = []

    matches.extend(
        _parse_r32(
            "Championship Preliminary",
            "Champ. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_r16(
            "Championship 1st Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_quarterfinal(
            "Championship Quarterfinals",
            "Quarterfinal",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_consolation_round3(
            "Consolation Preliminary",
            "Cons. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_consolation_round4(
            "Consolation 1st Round",
            "Cons. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_semi_mixed(
            "Champ Semis & Con Quarterfinal",
            "Semifinal",
            "Cons. Round 3",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_consolation_semi(
            "Consolation Semifinal",
            "Cons. Semi",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_place_matches(
            "Place Bouts",
            "3rd Place Match",
            "5th Place Match",
            "7th Place Match",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    matches.extend(
        _parse_championship_matches(
            "Championship Bouts",
            "1st Place Match",
            selenium_rounds,
            match_slots_by_bracket,
        )
    )

    if selenium_rounds:
        raise ValueError("Round not processed", selenium_rounds.keys())

    return matches


def main():
    root = HERE.parent / "raw-data" / "2009"
    with open(root / "team_scores.selenium.json") as file_obj:
        selenium_team_scores = json.load(file_obj)

    team_scores = _parse_team_scores(selenium_team_scores)

    with open(root / "deductions.selenium.json") as file_obj:
        extracted = Deductions.model_validate_json(file_obj.read())
        deductions = extracted.root

    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    with open(root / "rounds.selenium.json") as file_obj:
        selenium_rounds = json.load(file_obj)

    match_slots_by_bracket: dict[tuple[bracket_utils.Division, int], MatchSlotMap] = {}

    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = _normalize_division(division_display)
        division_scores = team_scores[division]

        if not isinstance(html, str):
            raise TypeError("Unexpected value", type(html))

        soup = bs4.BeautifulSoup(html, features="html.parser")
        initial_match_slots = _initial_entries(soup, division_scores)
        key = (division, weight)
        if key in match_slots_by_bracket:
            raise KeyError("Duplicate", key)

        match_slots_by_bracket[key] = initial_match_slots

    matches = _parse_rounds(selenium_rounds, match_slots_by_bracket)

    weight_classes: list[bracket_utils.WeightClass] = []
    for key in match_slots_by_bracket.keys():
        division, weight = key
        weight_class_matches = [
            match_with.match
            for match_with in matches
            if match_with.division == division and match_with.weight == weight
        ]
        weight_class = bracket_utils.WeightClass(
            division=division, weight=weight, matches=weight_class_matches
        )
        weight_classes.append(weight_class)

    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=deductions
    )
    with open(HERE / "extracted.2009.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
