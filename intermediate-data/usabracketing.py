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


class _Abbreviations(pydantic.RootModel[dict[str, str]]):
    pass


def _extract_bracket_name(soup: bs4.BeautifulSoup) -> str:
    bracket_spans = soup.find_all(
        "span", class_="font-gotham antialiased text-xl text-usa-red font-extrabold"
    )
    if len(bracket_spans) != 2:
        raise RuntimeError("Failed to load bracket", len(bracket_spans), key)

    bracket_names = set(bracket_span.text for bracket_span in bracket_spans)
    if len(bracket_names) != 1:
        raise RuntimeError("Failed to load bracket", len(bracket_names), key)

    (bracket_name,) = list(bracket_names)
    return bracket_name


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

    for bracket_url, html in selenium_brackets.items():
        soup = bs4.BeautifulSoup(html, features="html.parser")

        bracket_name = _extract_bracket_name(soup)
        division_display, weight_str = bracket_name.rsplit(" ", 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
        division_scores = team_scores[division]

        key = (division, weight)
