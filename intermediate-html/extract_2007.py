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
_NAME_FIXES: tuple[tuple[str, str], ...] = (
    ("Aaron Brewton III", "Aaron Brewton II"),
    ("Brendan Ty Hall", "Brendan Tyler Hall"),
    ("Christophe Bartels", "Christopher Bartels"),
    ("Christophe Carton", "Christopher Carton"),
    ("Christophe Lopez", "Christopher Lopez"),
    ("Christophe Wright", "Christopher Wright"),
    ("Malik - Ja Taylor", "Malik - Jabri Taylor"),
)
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Tyrone Sally Jr.", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Tyrone",
        last_name="Sally",
        suffix="Jr",
        team="Harvey Park Dist Twisters",
    ),
    ("Wardell Rosemon Jr.", "Dundee Highlanders"): bracket_utils.Competitor(
        first_name="Wardell",
        last_name="Rosemon",
        suffix="Jr",
        team="Dundee Highlanders",
    ),
    ("Archie Williams Jr.", "Champaign Kids Wrestling"): bracket_utils.Competitor(
        first_name="Archie",
        last_name="Williams",
        suffix="Jr",
        team="Champaign Kids Wrestling",
    ),
    ("Anthony Ferraris Jr", "Maine Eagles WC"): bracket_utils.Competitor(
        first_name="Anthony", last_name="Ferraris", suffix="Jr", team="Maine Eagles WC"
    ),
    ("Lusiano Cantu Jr.", "Gomez Wrestling Academy"): bracket_utils.Competitor(
        first_name="Lusiano",
        last_name="Cantu",
        suffix="Jr",
        team="Gomez Wrestling Academy",
    ),
    ("Antwyone Brown Jr.", "Crosstown WC"): bracket_utils.Competitor(
        first_name="Antwyone", last_name="Brown", suffix="Jr", team="Crosstown WC"
    ),
    ("Brendan Tyler Hall", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Brendan Tyler",
        last_name="Hall",
        suffix=None,
        team="Harvey Park Dist Twisters",
    ),
    ("Lonne Cleveland III", "GC Jr Warriors"): bracket_utils.Competitor(
        first_name="Lonne",
        last_name="Cleveland",
        suffix="III",
        team="GC Jr Warriors",
    ),
    ("Aaron Brewton II", "Waukegan Youth WC"): bracket_utils.Competitor(
        first_name="Aaron", last_name="Brewton", suffix="II", team="Waukegan Youth WC"
    ),
    ("Malik - Jabri Taylor", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Malik - Jabri",
        last_name="Taylor",
        suffix=None,
        team="Harvey Park Dist Twisters",
    ),
    ("Michael Aldrich Jr", "Peoria Razorbacks Youth WC"): bracket_utils.Competitor(
        first_name="Michael",
        last_name="Aldrich",
        suffix="Jr",
        team="Peoria Razorbacks Youth WC",
    ),
    ("Ross Ferraro III", "Gomez Wrestling Academy"): bracket_utils.Competitor(
        first_name="Ross",
        last_name="Ferraro",
        suffix="III",
        team="Gomez Wrestling Academy",
    ),
    ("Alvin Foster III", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Alvin",
        last_name="Foster",
        suffix="III",
        team="Harvey Park Dist Twisters",
    ),
}


class Entrant(pydantic.BaseModel):
    name: str | None
    team: str | None
    bout_number: int | None

    @property
    def long_name(self) -> str | None:
        if self.name is None:
            if self.team is not None:
                raise RuntimeError("Invariant violation", self)

            return None

        if self.team is None:
            raise RuntimeError("Invariant violation", self)

        return f"{self.name} ({self.team})"


EntrantMap = dict[
    tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition], list[Entrant]
]


def _normalize_division(division_display: str) -> bracket_utils.Division:
    if division_display.strip() == "Novice":
        return "novice"

    if division_display.strip() == "Senior":
        return "senior"

    raise NotImplementedError(division_display)


class TeamScore(pydantic.BaseModel):
    name: str
    acronym: str
    score: float


def _team_scores_from_html(html: Any) -> list[TeamScore]:
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html))

    soup = bs4.BeautifulSoup(html, features="html.parser")

    scores: list[TeamScore] = []
    for tr in soup.find_all("tr"):
        all_td = tr.find_all("td")
        all_th = tr.find_all("th")
        if len(all_td) == 0 and len(all_th) == 4:
            continue

        if len(all_td) != 4 or len(all_th) != 0:
            raise RuntimeError("Invariant violation", tr)

        scores.append(
            TeamScore(
                name=all_td[1].text,
                acronym=all_td[2].text,
                score=float(all_td[3].text),
            )
        )

    return scores


def _parse_team_scores(
    selenium_team_scores: Any,
) -> dict[bracket_utils.Division, list[TeamScore]]:
    if not isinstance(selenium_team_scores, dict):
        raise TypeError("Unexpected value", type(selenium_team_scores))

    result: dict[bracket_utils.Division, list[TeamScore]] = {}
    for division_display, html in selenium_team_scores.items():
        division = _normalize_division(division_display)
        if division in result:
            raise KeyError("Duplicate value", division)

        scores = _team_scores_from_html(html)
        result[division] = scores

    return result


class Deduction(pydantic.BaseModel):
    team: str
    reason: str
    value: float


class Deductions(pydantic.RootModel[list[Deduction]]):
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


def _split_name_team(
    name_team: str, division_scores: list[TeamScore]
) -> tuple[str, str] | tuple[None, None]:
    if name_team == "Bye":
        return None, None

    if not name_team.endswith(")"):
        raise RuntimeError("Invariant violation", name_team)

    to_parse = name_team[:-1]

    parts = to_parse.split(" (", 1)
    if len(parts) != 2:
        raise RuntimeError("Invariant violation", name_team)

    name = parts[0]
    team_prefix = parts[1]

    for before, after in _NAME_FIXES:
        name = name.replace(before, after)

    matches: list[str] = []
    for score in division_scores:
        if score.name.startswith(team_prefix):
            matches.append(score.name)

    if len(matches) != 1:
        raise RuntimeError("Invariant violation", name_team, matches)

    return name, matches[0]


def _initial_entries(
    soup: bs4.BeautifulSoup, division_scores: list[TeamScore]
) -> EntrantMap:
    initial_bout_index = 0
    opening_bouts = _get_opening_bout_numbers(soup)

    all_wrestler_tds = soup.find_all(
        "td", width="100%", align="center", valign="bottom"
    )
    if len(all_wrestler_tds) != 63:
        raise RuntimeError("Invariant violation", len(all_wrestler_tds))

    entrant_map: EntrantMap = {}

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

        name, team = _split_name_team(wrestler_td.text, division_scores)
        key = match_slot, bracket_position
        if key in entrant_map:
            raise KeyError("Duplicate", key)

        entrant_map[key] = [
            Entrant(
                name=name,
                team=team,
                bout_number=bout_number,
            )
        ]

    return entrant_map


def _determine_result_type(result: str, result_how: str) -> bracket_utils.ResultType:
    if result.startswith("OT "):
        if result_how != "in overtime":
            raise ValueError("Invalid `how`", result, result_how)

        score_win_str, score_lose_str = result[len("OT ") :].split("-")
        score_win = int(score_win_str)
        score_lose = int(score_lose_str)
        delta = score_win - score_lose
        if not (0 < delta < 8):
            raise ValueError("Unexpected difference", result, result_how)

        return "decision"

    if result.startswith("2-OT "):
        if result_how != "in double overtime":
            raise ValueError("Invalid `how`", result, result_how)

        score_win_str, score_lose_str = result[len("2-OT ") :].split("-")
        score_win = int(score_win_str)
        score_lose = int(score_lose_str)
        delta = score_win - score_lose
        if not (0 < delta < 8):
            raise ValueError("Unexpected difference", result, result_how)

        return "decision"

    if result == "Dec" or result.startswith("Dec "):
        if result_how != "by decision":
            raise ValueError("Invalid `how`", result, result_how)

        return "decision"

    if result.startswith("Maj "):
        if result_how != "by major decision":
            raise ValueError("Invalid `how`", result, result_how)

        return "major"

    if result.startswith("TF "):
        if result_how != "by tech fall":
            raise ValueError("Invalid `how`", result, result_how)

        return "tech"

    if result == "Fall" or result.startswith("Fall "):
        if result_how != "by fall":
            raise ValueError("Invalid `how`", result, result_how)

        return "fall"

    if result.startswith("Inj. "):
        if result_how != "by injury default":
            raise ValueError("Invalid `how`", result, result_how)

        return "default"

    if result == "FF":
        if result_how != "by forfeit":
            raise ValueError("Invalid `how`", result, result_how)

        return "forfeit"

    if result == "Bye":
        if result_how != "":
            raise ValueError("Invalid `how`", result, result_how)

        return "bye"

    raise NotImplementedError(result, result_how)


def _to_competitor(entrant: Entrant) -> bracket_utils.Competitor | None:
    if entrant.name is None:
        if entrant.team is not None:
            raise RuntimeError("Invariant violation", entrant)

        return None

    if entrant.team is None:
        raise RuntimeError("Invariant violation", entrant)

    exception_key = entrant.name, entrant.team
    if exception_key in _NAME_EXCEPTIONS:
        return _NAME_EXCEPTIONS[exception_key]

    parts = entrant.name.split()
    if len(parts) != 2:
        raise NotImplementedError("Missing name exception", entrant)

    return bracket_utils.Competitor(
        first_name=parts[0], last_name=parts[1], suffix=None, team=entrant.team
    )


def _get_entrant(index: int | None, entrants: list[Entrant]) -> Entrant:
    if index is not None:
        return entrants[index]

    bout_numbers = set(entrant.bout_number for entrant in entrants)
    if len(bout_numbers) != 1:
        raise RuntimeError("Bout numbers must agree", bout_numbers)

    bout_number = bout_numbers.pop()
    if bout_number is None:
        raise RuntimeError("Must have a bout number", bout_number)

    return Entrant(name=None, team=None, bout_number=bout_number)


def _handle_bye(
    entry_text: str, top_entrants: list[Entrant], bottom_entrants: list[Entrant]
) -> tuple[int | None, int | None, bool, str, bracket_utils.ResultType]:
    top_entrant_names = [entrant.long_name for entrant in top_entrants]
    bottom_entrant_names = [entrant.long_name for entrant in bottom_entrants]

    winner, remaining = entry_text.split(" received a bye ")
    if remaining.strip() != "() Bye":
        raise RuntimeError("Invariant violation", entry_text)

    winner_top_index = _matching_index(winner, top_entrant_names)
    winner_bottom_index = _matching_index(winner, bottom_entrant_names)

    if winner_top_index is not None:
        if winner_bottom_index is not None:
            raise RuntimeError("Invariant violation", entry_text)

        top_index = winner_top_index
        bottom_index = None
        top_win = True
    elif winner_bottom_index is not None:
        if winner_top_index is not None:
            raise RuntimeError("Invariant violation", entry_text)

        top_index = None
        bottom_index = winner_bottom_index
        top_win = False
    else:
        raise RuntimeError("Invariant violation", entry_text)

    result = "Bye"
    result_type = _determine_result_type(result, "")
    return top_index, bottom_index, top_win, result, result_type


def _matching_index(value: str, choices: list[str | None]) -> int | None:
    matches = [i for i, choice in enumerate(choices) if choice == value]
    if len(matches) == 0:
        return None

    if len(matches) != 1:
        raise RuntimeError("Invariant violation", value, matches, choices)

    return matches[0]


def _handle_match(
    entry_text: str, top_entrants: list[Entrant], bottom_entrants: list[Entrant]
) -> tuple[int, int, bool, str, bracket_utils.ResultType]:
    top_entrant_names = [entrant.long_name for entrant in top_entrants]
    bottom_entrant_names = [entrant.long_name for entrant in bottom_entrants]

    winner, loser_extra = entry_text.split(" won ")
    result_how, loser_extra = loser_extra.split(" over ")
    loser, result = loser_extra.rsplit(") ", 1)
    loser = f"{loser})"

    winner_top_index = _matching_index(winner, top_entrant_names)
    winner_bottom_index = _matching_index(winner, bottom_entrant_names)
    loser_top_index = _matching_index(loser, top_entrant_names)
    loser_bottom_index = _matching_index(loser, bottom_entrant_names)

    if winner_top_index is not None:
        if (
            loser_bottom_index is None
            or winner_bottom_index is not None
            or loser_top_index is not None
        ):
            raise RuntimeError("Invariant violation", entry_text)

        top_win = True
        top_index = winner_top_index
        bottom_index = loser_bottom_index
    elif winner_bottom_index is not None:
        if (
            loser_top_index is None
            or winner_top_index is not None
            or loser_bottom_index is not None
        ):
            raise RuntimeError("Invariant violation", entry_text)

        top_index = loser_top_index
        bottom_index = winner_bottom_index
        top_win = False
    else:
        raise RuntimeError("Invariant violation", winner)

    result_type = _determine_result_type(result, result_how)
    return top_index, bottom_index, top_win, result, result_type


def _add_r32_bye(
    index: int,
    r16_bout_number: int,
    matches: list[bracket_utils.Match],
    entrant_map: EntrantMap,
) -> None:
    """Add a bye in the Round of 32 for a sectional winner."""
    slot_id = 2 * (index + 1) - 1
    match_slot: bracket_utils.MatchSlot = f"championship_r32_{slot_id:02}"

    entrants = entrant_map[(match_slot, "top")]
    if len(entrants) != 1:
        raise RuntimeError("Invariant violation", match_slot)
    entrant = entrants[0]

    competitor = _to_competitor(entrant)
    match = bracket_utils.Match(
        match_slot=match_slot,
        top_competitor=competitor,
        bottom_competitor=None,
        result="Bye",
        result_type="bye",
        bout_number=None,
        top_win=True,
    )
    matches.append(match)

    win_position = bracket_utils.next_match_position_win_2007(match_slot)
    entrant_map.setdefault(win_position, [])
    entrant_map[win_position].append(
        Entrant(
            name=entrant.name,
            team=entrant.team,
            bout_number=r16_bout_number,
        )
    )


def _r32_bout_number(top_entrant: Entrant, bottom_entrant: Entrant) -> int:
    if top_entrant.bout_number is not None:
        raise RuntimeError("No top bout number for R32", top_entrant)

    if bottom_entrant.bout_number is None:
        raise RuntimeError("Need bottom bout number for R32", bottom_entrant)

    return bottom_entrant.bout_number


def _parse_r32(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
    weight_counts: dict[bracket_utils.Division, int],
) -> list[bracket_utils.Match]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[bracket_utils.Match] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        entrant_map = entrants_by_bracket[key]
        r16_bout_number_delta = weight_counts[division] * 8
        cons_bout_number_delta = weight_counts[division] * 20

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

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            if not entry.text.startswith(match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(match_prefix) :]
            if " received a bye " in entry_text:
                _, _, top_win, result, result_type = _handle_bye(
                    entry_text, top_entrants, bottom_entrants
                )
            else:
                _, _, top_win, result, result_type = _handle_match(
                    entry_text, top_entrants, bottom_entrants
                )

            top_entrant = top_entrants[0]
            bottom_entrant = bottom_entrants[0]
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)
            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_r32_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            loser_entrant = bottom_entrant
            if not top_win:
                winner_entrant = bottom_entrant
                loser_entrant = top_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # 1. Make the `entrant_map` aware of the winner
            r16_bout_number = r16_bout_number_delta + match.bout_number
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=r16_bout_number,
                )
            )

            # 2. Make the `entrant_map` aware of the top-side wrestler that
            #    had a bye.
            _add_r32_bye(i, r16_bout_number, matches, entrant_map)

            # 3. Make the `entrant_map` aware of the loser
            # NOTE: The loser **MIGHT** have a match in `cons_bout_number`,
            #       **IF** the winner makes the semifinals. But this is true
            #       for another R32 loser so we need to keep an array.
            cons_bout_number = cons_bout_number_delta + (match.bout_number + 1) // 2
            lose_position = bracket_utils.next_match_position_lose_2007(match_slot)
            entrant_map.setdefault(lose_position, [])
            entrant_map[lose_position].append(
                Entrant(
                    name=loser_entrant.name,
                    team=loser_entrant.team,
                    bout_number=cons_bout_number,
                )
            )

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _require_bout_number(top_entrant: Entrant, bottom_entrant: Entrant) -> int:
    if top_entrant.bout_number is None or bottom_entrant.bout_number is None:
        raise RuntimeError("Must have a bout number", top_entrant, bottom_entrant)

    bout_number = bottom_entrant.bout_number

    if top_entrant.bout_number != bout_number:
        raise RuntimeError("Bout numbers must agree", top_entrant, bottom_entrant)

    return bout_number


def _parse_r16(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
    weight_counts: dict[bracket_utils.Division, int],
) -> list[bracket_utils.Match]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[bracket_utils.Match] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        entrant_map = entrants_by_bracket[key]
        qf_bout_number_delta = weight_counts[division] * 12
        cons_bout_number_delta = weight_counts[division] * 16

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

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            if not entry.text.startswith(match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(match_prefix) :]
            top_index, bottom_index, top_win, result, result_type = _handle_match(
                entry_text, top_entrants, bottom_entrants
            )

            top_entrant = top_entrants[top_index]
            bottom_entrant = bottom_entrants[bottom_index]
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)
            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_require_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            loser_entrant = bottom_entrant
            if not top_win:
                winner_entrant = bottom_entrant
                loser_entrant = top_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # 1. Make the `entrant_map` aware of the winner
            qf_bout_number = qf_bout_number_delta + (match.bout_number + 1) // 2
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=qf_bout_number,
                )
            )

            # 2. Make the `entrant_map` aware of the loser
            # NOTE: The loser **MIGHT** have a match in `cons_bout_number`,
            #       **IF** the winner makes the semifinals. But this is true
            #       for another R16 loser so we need to keep an array.
            cons_bout_number = cons_bout_number_delta + (match.bout_number + 1) // 2
            lose_position = bracket_utils.next_match_position_lose_2007(match_slot)
            entrant_map.setdefault(lose_position, [])
            entrant_map[lose_position].append(
                Entrant(
                    name=loser_entrant.name,
                    team=loser_entrant.team,
                    bout_number=cons_bout_number,
                )
            )

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_quarterfinal(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
    weight_counts: dict[bracket_utils.Division, int],
) -> list[bracket_utils.Match]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[bracket_utils.Match] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        entrant_map = entrants_by_bracket[key]
        sf_bout_number_delta = weight_counts[division] * 20
        cons_bout_number_delta = weight_counts[division] * 8

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

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 1:
                raise RuntimeError("Invariant violation", match_slot)

            if not entry.text.startswith(match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(match_prefix) :]
            top_index, bottom_index, top_win, result, result_type = _handle_match(
                entry_text, top_entrants, bottom_entrants
            )

            top_entrant = top_entrants[top_index]
            bottom_entrant = bottom_entrants[bottom_index]
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)
            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_require_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            loser_entrant = bottom_entrant
            if not top_win:
                winner_entrant = bottom_entrant
                loser_entrant = top_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # 1. Make the `entrant_map` aware of the winner
            sf_bout_number = sf_bout_number_delta + (match.bout_number + 1) // 2
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=sf_bout_number,
                )
            )

            # 2. Make the `entrant_map` aware of the loser
            cons_bout_number = cons_bout_number_delta + match.bout_number
            lose_position = bracket_utils.next_match_position_lose_2007(match_slot)
            entrant_map.setdefault(lose_position, [])
            entrant_map[lose_position].append(
                Entrant(
                    name=loser_entrant.name,
                    team=loser_entrant.team,
                    bout_number=cons_bout_number,
                )
            )

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_consolation_round3(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
    weight_counts: dict[bracket_utils.Division, int],
) -> list[bracket_utils.Match]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[bracket_utils.Match] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        entrant_map = entrants_by_bracket[key]
        round4_bout_number_delta = weight_counts[division] * 4

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

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 2:
                raise RuntimeError("Invariant violation", len(top_entrants), match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 2:
                raise RuntimeError(
                    "Invariant violation", len(bottom_entrants), match_slot
                )

            if not entry.text.startswith(match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(match_prefix) :]
            if " received a bye " in entry_text:
                top_index, bottom_index, top_win, result, result_type = _handle_bye(
                    entry_text, top_entrants, bottom_entrants
                )
            else:
                top_index, bottom_index, top_win, result, result_type = _handle_match(
                    entry_text, top_entrants, bottom_entrants
                )

            top_entrant = _get_entrant(top_index, top_entrants)
            bottom_entrant = _get_entrant(bottom_index, bottom_entrants)
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)
            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_require_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            if not top_win:
                winner_entrant = bottom_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # Make the `entrant_map` aware of the winner (loser is eliminated)
            round4_bout_number = round4_bout_number_delta + match.bout_number
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=round4_bout_number,
                )
            )

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_consolation_round4(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
    weight_counts: dict[bracket_utils.Division, int],
) -> list[bracket_utils.Match]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[bracket_utils.Match] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        entrant_map = entrants_by_bracket[key]
        round5_bout_number_delta = weight_counts[division] * 4

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

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 1:
                raise RuntimeError("Invariant violation", len(top_entrants), match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_entrants), match_slot
                )

            if not entry.text.startswith(match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(match_prefix) :]
            top_index, bottom_index, top_win, result, result_type = _handle_match(
                entry_text, top_entrants, bottom_entrants
            )

            top_entrant = top_entrants[top_index]
            bottom_entrant = bottom_entrants[bottom_index]
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)
            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_require_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            if not top_win:
                winner_entrant = bottom_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # Make the `entrant_map` aware of the winner (loser is eliminated)
            half_next_multiple = (match.bout_number + 1) // 2
            quarter_next_multiple = (match.bout_number + 3) // 4
            # NOTE: This is fairly complex because the semifinals and
            #       quarterfinal wrestlebacks share bout numbers.
            round5_bout_number = (
                round5_bout_number_delta
                + half_next_multiple
                + 2 * quarter_next_multiple
            )
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=round5_bout_number,
                )
            )

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_semi_mixed(
    round_name: str,
    semi_match_prefix: str,
    cons_match_prefix: str,
    selenium_rounds: dict,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
    weight_counts: dict[bracket_utils.Division, int],
) -> list[bracket_utils.Match]:
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[bracket_utils.Match] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        entrant_map = entrants_by_bracket[key]
        first_place_bout_number_delta = 1 + weight_counts[division] * 6
        semi_cons_bout_number_delta = 1 + weight_counts[division] * 18
        # TODO: delta(s)

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

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 1:
                raise RuntimeError("Invariant violation", len(top_entrants), match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_entrants), match_slot
                )

            if not entry.text.startswith(semi_match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(semi_match_prefix) :]
            top_index, bottom_index, top_win, result, result_type = _handle_match(
                entry_text, top_entrants, bottom_entrants
            )

            top_entrant = top_entrants[top_index]
            bottom_entrant = bottom_entrants[bottom_index]
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)

            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_require_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            loser_entrant = bottom_entrant
            if not top_win:
                winner_entrant = bottom_entrant
                loser_entrant = top_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # 1. Make the `entrant_map` aware of the winner
            half_next_multiple = (match.bout_number + 1) // 2
            first_place_bout_number = (
                first_place_bout_number_delta + 2 * half_next_multiple
            )
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=first_place_bout_number,
                )
            )

            # 2. Make the `entrant_map` aware of the loser
            half_next_multiple = (match.bout_number + 1) // 2
            semi_cons_bout_number = (
                semi_cons_bout_number_delta + match.bout_number - half_next_multiple
            )
            lose_position = bracket_utils.next_match_position_lose_2007(match_slot)
            entrant_map.setdefault(lose_position, [])
            entrant_map[lose_position].append(
                Entrant(
                    name=loser_entrant.name,
                    team=loser_entrant.team,
                    bout_number=semi_cons_bout_number,
                )
            )

        # Wrestlebacks
        for i in range(2):
            entry = all_entries[i + 2]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"consolation_round5_{slot_id:02}"

            top_entrants = entrant_map[(match_slot, "top")]
            if len(top_entrants) != 1:
                raise RuntimeError("Invariant violation", len(top_entrants), match_slot)

            bottom_entrants = entrant_map[(match_slot, "bottom")]
            if len(bottom_entrants) != 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_entrants), match_slot
                )

            if not entry.text.startswith(cons_match_prefix):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len(cons_match_prefix) :]
            top_index, bottom_index, top_win, result, result_type = _handle_match(
                entry_text, top_entrants, bottom_entrants
            )

            top_entrant = top_entrants[top_index]
            bottom_entrant = bottom_entrants[bottom_index]
            top_competitor = _to_competitor(top_entrant)
            bottom_competitor = _to_competitor(bottom_entrant)

            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=result,
                result_type=result_type,
                bout_number=_require_bout_number(top_entrant, bottom_entrant),
                top_win=top_win,
            )
            matches.append(match)

            winner_entrant = top_entrant
            loser_entrant = bottom_entrant
            if not top_win:
                winner_entrant = bottom_entrant
                loser_entrant = top_entrant

            if match.bout_number is None:
                raise RuntimeError("Invariant violation")

            # 1. Make the `entrant_map` aware of the winner
            win_position = bracket_utils.next_match_position_win_2007(match_slot)
            entrant_map.setdefault(win_position, [])
            entrant_map[win_position].append(
                Entrant(
                    name=winner_entrant.name,
                    team=winner_entrant.team,
                    bout_number=-1,  # TODO
                )
            )

            # 2. Make the `entrant_map` aware of the loser
            lose_position = bracket_utils.next_match_position_lose_2007(match_slot)
            entrant_map.setdefault(lose_position, [])
            entrant_map[lose_position].append(
                Entrant(
                    name=loser_entrant.name,
                    team=loser_entrant.team,
                    bout_number=-1,  # TODO
                )
            )

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")

    return matches


def _parse_rounds(
    selenium_rounds: Any,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap],
) -> None:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    weight_counts: dict[bracket_utils.Division, int] = {}
    for key in entrants_by_bracket.keys():
        division, _ = key
        weight_counts[division] = weight_counts.get(division, 0) + 1

    matches: list[bracket_utils.Match] = []

    matches.extend(
        _parse_r32(
            "Champ Round 1 (32 Man)",
            "Champ. Round 1 - ",
            selenium_rounds,
            entrants_by_bracket,
            weight_counts,
        )
    )

    matches.extend(
        _parse_r16(
            "Champ Round 2 (32 Man)",
            "Champ. Round 2 - ",
            selenium_rounds,
            entrants_by_bracket,
            weight_counts,
        )
    )

    matches.extend(
        _parse_quarterfinal(
            "Quarters (32 Man)",
            "Quarterfinal - ",
            selenium_rounds,
            entrants_by_bracket,
            weight_counts,
        )
    )

    matches.extend(
        _parse_consolation_round3(
            "1st Wrestleback (32 Man)",
            "Cons. Round 1 - ",
            selenium_rounds,
            entrants_by_bracket,
            weight_counts,
        )
    )

    matches.extend(
        _parse_consolation_round4(
            "2nd Wrestleback (32 Man)",
            "Cons. Round 2 - ",
            selenium_rounds,
            entrants_by_bracket,
            weight_counts,
        )
    )

    matches.extend(
        _parse_semi_mixed(
            "Semis & WB (32 Man)",
            "Semifinal - ",
            "Cons. Round 3 - ",
            selenium_rounds,
            entrants_by_bracket,
            weight_counts,
        )
    )

    # "Cons. Semis (32 Man)"
    # "Placement Matches (32 Man)"

    # TODO: `if selenium_rounds: raise ValueError('keys', ...)`

    for match in matches:
        print(match)


def main():
    root = HERE.parent / "raw-data" / "2007"
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

    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], EntrantMap] = {}

    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = _normalize_division(division_display)
        division_scores = team_scores[division]

        if not isinstance(html, str):
            raise TypeError("Unexpected value", type(html))

        soup = bs4.BeautifulSoup(html, features="html.parser")
        bracket_entrants = _initial_entries(soup, division_scores)
        key = (division, weight)
        if key in entrants_by_bracket:
            raise KeyError("Duplicate", key)

        entrants_by_bracket[key] = bracket_entrants

    _parse_rounds(selenium_rounds, entrants_by_bracket)


if __name__ == "__main__":
    main()
