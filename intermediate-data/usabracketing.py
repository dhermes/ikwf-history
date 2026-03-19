# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import json
import pathlib
import re
from collections.abc import Callable
from typing import Any

import bracket_utils
import bs4
import pydantic

_MISSING_BOUT_NUMBER_SENTINEL = -54572
_TITLE_MARGIN_LEFT = "margin-left:0px"
_MATCH_MARGIN_LEFT = "margin-left:20px"
_BOUT_MAT_RE = re.compile(r"^Bout (\d+) \(Mat (\d+)\)$")
_BOUT_RE = re.compile(r"^Bout (\d+)$")


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


def _get_bout_number(bout_mat: str) -> int:
    """Parse the bout number out of "Bout N (Mat M)"."""
    match_ = _BOUT_MAT_RE.match(bout_mat)
    if match_ is not None:
        bout_number_str, _ = match_.groups()
        return int(bout_number_str)

    match_ = _BOUT_RE.match(bout_mat)
    if match_ is None:
        raise ValueError("Unexpected bout mat string", bout_mat)

    (bout_number_str,) = match_.groups()
    return int(bout_number_str)


def _extract_division(
    prefix_division: str, match_prefix: str
) -> bracket_utils.Division:
    """Parse the bout number out of "Bout N (Mat M)"."""
    full_prefix = f"{match_prefix}: "
    if not prefix_division.startswith(full_prefix):
        raise ValueError("Unexpected prefix + division", prefix_division, match_prefix)

    division_display = prefix_division[len(full_prefix) :]
    return normalize_division(division_display)


def _get_all_opening_bout_numbers(
    selenium_rounds: Any, round_name: str, match_prefix: str
) -> dict[tuple[bracket_utils.Division, int], list[int]]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    html = selenium_rounds.get(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_div = soup.find_all("div")

    if len(all_div) < 3:
        raise ValueError("Unexpected div count", len(all_div))

    outer_div, title_div = all_div[:2]
    if _get_margin_left_style(outer_div) != "":
        raise ValueError("Unexpected outer div")

    if _get_margin_left_style(title_div) != _TITLE_MARGIN_LEFT:
        raise ValueError("Unexpected title div", _get_margin_left_style(title_div))

    if title_div.text.strip() != round_name:
        raise ValueError("Unexpected title div", title_div.text.strip())

    match_divs = all_div[2:]
    result: dict[tuple[bracket_utils.Division, int], list[int]] = {}
    for match_div in match_divs:
        if _get_margin_left_style(match_div) != _MATCH_MARGIN_LEFT:
            raise ValueError("Unexpected match div", _get_margin_left_style(match_div))

        match_line = match_div.text.strip()
        bout_mat, prefix_division, weight_str, match_info = match_line.split(" - ")
        division = _extract_division(prefix_division, match_prefix)
        bout_number = _get_bout_number(bout_mat)
        weight = int(weight_str)
        key = (division, weight)
        result.setdefault(key, [])

        result[key].append(bout_number)
        result[key].sort()

    return result


class _Abbreviations(pydantic.RootModel[dict[str, str]]):
    pass


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
        extracted_deductions = _Deductions.model_validate_json(file_obj.read())

    deductions = extracted_deductions.root

    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    with open(root / "rounds.selenium.json") as file_obj:
        selenium_rounds = json.load(file_obj)

    with open(root / "abbreviations.selenium.json") as file_obj:
        extracted_abbreviations = _Abbreviations.model_validate_json(file_obj.read())

    abbreviations = extracted_abbreviations.root

    match_slots_by_bracket: MatchSlotsByBracket = {}

    all_opening_bout_numbers = _get_all_opening_bout_numbers(
        selenium_rounds, prelim_round_name, prelim_match_prefix
    )

    print(len(team_scores), len(deductions), all_opening_bout_numbers)
