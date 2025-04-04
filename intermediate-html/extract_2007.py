# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib

import bs4
import pydantic

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_INITIAL_ENTRY_INFO: tuple[
    tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition, int], ...
] = (
    ("championship_r32_02", "top", 4),
    ("championship_r32_02", "bottom", 7),
    ("championship_r32_04", "top", 12),
    ("championship_r32_04", "bottom", 15),
    ("championship_r32_06", "top", 20),
    ("championship_r32_06", "bottom", 23),
    ("championship_r32_08", "top", 28),
    ("championship_r32_08", "bottom", 31),
    ("championship_r32_10", "top", 36),
    ("championship_r32_10", "bottom", 39),
    ("championship_r32_12", "top", 44),
    ("championship_r32_12", "bottom", 47),
    ("championship_r32_14", "top", 52),
    ("championship_r32_14", "bottom", 55),
    ("championship_r32_16", "top", 60),
    ("championship_r32_16", "bottom", 62),
)


class Entrant(pydantic.BaseModel):
    division: bracket_utils.Division
    weight: int
    match_slot: bracket_utils.MatchSlot
    bracket_position: bracket_utils.BracketPosition
    name_team: str
    bout_number: int | None


def _normalize_division(division_display: str) -> bracket_utils.Division:
    if division_display.strip() == "Novice":
        return "novice"

    if division_display.strip() == "Senior":
        return "senior"

    raise NotImplementedError(division_display)


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


def _initial_entries(
    soup: bs4.BeautifulSoup, division: bracket_utils.Division, weight: int
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

        entrants.append(
            Entrant(
                division=division,
                weight=weight,
                match_slot=match_slot,
                bracket_position=bracket_position,
                name_team=wrestler_td.text,
                bout_number=bout_number,
            )
        )

    return entrants


def main():
    root = HERE.parent / "raw-data" / "2007"
    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    entrants: list[Entrant] = []
    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = _normalize_division(division_display)

        soup = bs4.BeautifulSoup(html, features="html.parser")
        entrants.extend(_initial_entries(soup, division, weight))


if __name__ == "__main__":
    main()
