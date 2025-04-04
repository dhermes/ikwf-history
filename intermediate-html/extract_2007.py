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


class Entrant(pydantic.BaseModel):
    division: bracket_utils.Division
    weight: int
    match_slot: bracket_utils.MatchSlot
    bracket_position: bracket_utils.BracketPosition
    name: str | None
    team: str | None
    bout_number: int | None


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

    matches: list[str] = []
    for score in division_scores:
        if score.name.startswith(team_prefix):
            matches.append(score.name)

    if len(matches) != 1:
        raise RuntimeError("Invariant violation", name_team, matches)

    return name, matches[0]


def _initial_entries(
    soup: bs4.BeautifulSoup,
    division: bracket_utils.Division,
    weight: int,
    division_scores: list[TeamScore],
) -> list[Entrant]:
    initial_bout_index = 0
    opening_bouts = _get_opening_bout_numbers(soup)

    all_wrestler_tds = soup.find_all(
        "td", width="100%", align="center", valign="bottom"
    )
    if len(all_wrestler_tds) != 63:
        raise RuntimeError("Invariant violation", len(all_wrestler_tds))

    entrants: list[Entrant] = []

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
        entrants.append(
            Entrant(
                division=division,
                weight=weight,
                match_slot=match_slot,
                bracket_position=bracket_position,
                name=name,
                team=team,
                bout_number=bout_number,
            )
        )

    return entrants


def _parse_rounds(
    selenium_rounds: Any,
    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], list[Entrant]],
) -> dict[bracket_utils.Division, list[TeamScore]]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    html = selenium_rounds["Champ Round 1 (32 Man)"]
    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != ["Champ Round 1 (32 Man)"]:
        raise RuntimeError("Invariant violation", all_h1_text)

    entrant_keys = set(entrants_by_bracket.keys())

    all_h2 = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    for h2 in all_h2:
        division_display, weight_str = h2.text.split()
        weight = int(weight_str)
        division = _normalize_division(division_display)
        round_keys.add((division, weight))

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 8:
            raise RuntimeError("Invariant violation", all_entries)

        for entry in all_entries:
            if not entry.text.startswith("Champ. Round 1 - "):
                raise RuntimeError("Invariant violation", entry)

            entry_text = entry.text[len("Champ. Round 1 - ") :]
            if " received a bye " in entry_text:
                winner, remaining = entry_text.split(" received a bye ")
                if remaining.strip() != "() Bye":
                    raise RuntimeError("Invariant violation", entry_text)

                print((winner, None, "Bye", None))
            else:
                winner, loser_extra = entry_text.split(" won ")
                result_how, loser_extra = loser_extra.split(" over ")
                loser, result = loser_extra.rsplit(") ", 1)
                loser = f"{loser})"
                print((winner, loser, result, result_how))

    if round_keys != entrant_keys:
        raise RuntimeError("Invariant violation")


# [
#   "Champ Round 1 (32 Man)",
#   "Champ Round 2 (32 Man)",
#   "1st Wrestleback (32 Man)",
#   "2nd Wrestleback (32 Man)",
#   "Quarters (32 Man)",
#   "Semis & WB (32 Man)"
#   "Cons. Semis (32 Man)",
#   "Placement Matches (32 Man)",
# ]


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

    entrants_by_bracket: dict[tuple[bracket_utils.Division, int], list[Entrant]] = {}

    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = _normalize_division(division_display)
        division_scores = team_scores[division]

        soup = bs4.BeautifulSoup(html, features="html.parser")
        bracket_entrants = _initial_entries(soup, division, weight, division_scores)
        key = (division, weight)
        if key in entrants_by_bracket:
            raise KeyError("Duplicate", key)

        entrants_by_bracket[key] = bracket_entrants

    _parse_rounds(selenium_rounds, entrants_by_bracket)


if __name__ == "__main__":
    main()
