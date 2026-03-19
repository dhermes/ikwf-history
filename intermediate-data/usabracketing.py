# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import json
import pathlib
from collections.abc import Callable
from typing import Any

import bracket_utils
import bs4
import pydantic

_MISSING_BOUT_NUMBER_SENTINEL = -54572


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class MatchWithBracket(_ForbidExtra):
    division: bracket_utils.Division
    weight: int
    match: bracket_utils.Match


MatchSlotMap = dict[
    tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition],
    list[bracket_utils.CompetitorRaw],
]
MatchSlotsByBracket = dict[tuple[bracket_utils.Division, int], MatchSlotMap]
ParseRoundsFunc = Callable[[Any, MatchSlotsByBracket], list[MatchWithBracket]]


def normalize_division(division_display: str) -> bracket_utils.Division:
    normalized = division_display.strip()
    if normalized == "Boys Bantam":
        return "bantam"

    if normalized == "Boys Intermediate":
        return "intermediate"

    if normalized in ("Novice", "Boys Novice"):
        return "novice"

    if normalized in ("Senior", "Boys Senior"):
        return "senior"

    if normalized == "Girls Bantam":
        return "bantam_girls"

    if normalized == "Girls Intermediate":
        return "intermediate_girls"

    if normalized == "Girls Novice":
        return "novice_girls"

    if normalized == "Girls Senior":
        return "senior_girls"

    raise NotImplementedError(division_display)


def _team_scores_from_html(html: Any) -> list[bracket_utils.TeamScore]:
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html))

    soup = bs4.BeautifulSoup(html, features="html.parser")

    team_tables = soup.find_all("tbody", {"wire:sortable": "updateSortOrder"})
    if len(team_tables) != 1:
        raise ValueError("Unexpected HTML structure", len(team_tables))

    (team_table,) = team_tables

    scores: list[bracket_utils.TeamScore] = []
    for tr in team_table.find_all("tr"):
        all_td = tr.find_all("td")
        all_th = tr.find_all("th")
        if len(all_td) != 5 or len(all_th) != 0:
            raise RuntimeError("Invariant violation", tr)

        scores.append(
            bracket_utils.TeamScore(
                team=all_td[1].text.strip(), score=float(all_td[4].text.strip())
            )
        )

    return scores


def parse_team_scores(
    selenium_team_scores: Any,
) -> dict[bracket_utils.Division, list[bracket_utils.TeamScore]]:
    if not isinstance(selenium_team_scores, dict):
        raise TypeError("Unexpected value", type(selenium_team_scores))

    result: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    for division_display, html in selenium_team_scores.items():
        division = normalize_division(division_display)
        if division in result:
            raise KeyError("Duplicate value", division)

        scores = _team_scores_from_html(html)
        result[division] = scores

    return result


class _Deductions(pydantic.RootModel[list[bracket_utils.Deduction]]):
    pass

def _get_margin_left_style(tag: bs4.Tag) -> str:
    style = tag.get("style", "")
    matches = [part for part in style.split(";") if part.startswith("margin-left:")]
    if len(matches) == 0:
        return ""

    if len(matches) != 1:
        raise RuntimeError("Unexpected tag style", style)

    return matches[0]


def _get_all_opening_bout_numbers(
    selenium_rounds: Any, round_name: str, match_prefix: str
) -> dict[tuple[bracket_utils.Division, int], list[int]]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    html = selenium_rounds.get(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    result: dict[tuple[bracket_utils.Division, int], list[int]] = {}
    for h2 in all_h2:
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
        key = (division, weight)
        if key in result:
            raise RuntimeError("Invariant violation", key)
        result[key] = []

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 8:
            raise RuntimeError("Invariant violation", all_entries)

        for i in range(8):
            entry = all_entries[i]
            bout_number, _, _, _ = _round_line_split(entry.text, match_prefix)
            if bout_number != _MISSING_BOUT_NUMBER_SENTINEL:
                result[key].append(bout_number)

    return result


def extract_year(
    root: pathlib.Path,
    parse_rounds: ParseRoundsFunc,
    prelim_round_name: str,
    prelim_match_prefix: str,
    name_fixes: dict[str, str],
    team_fixes: dict[str, tuple[str, str]],
) -> bracket_utils.ExtractedTournament:
    with open(root / "team_scores.selenium.json") as file_obj:
        selenium_team_scores = json.load(file_obj)

    team_scores = parse_team_scores(selenium_team_scores)

    with open(root / "deductions.selenium.json") as file_obj:
        extracted = _Deductions.model_validate_json(file_obj.read())

    deductions = extracted.root

    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    with open(root / "rounds.selenium.json") as file_obj:
        selenium_rounds = json.load(file_obj)

    match_slots_by_bracket: MatchSlotsByBracket = {}

    all_opening_bout_numbers = _get_all_opening_bout_numbers(
        selenium_rounds, prelim_round_name, prelim_match_prefix
    )

    print(len(team_scores), len(deductions))
