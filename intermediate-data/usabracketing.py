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
_BOUT_PHANTOM_RE = re.compile(r"^Bout m(\d+)$")
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


def _get_margin_left_style(tag: bs4.Tag) -> str:
    style = tag.get("style", "")
    matches = [part for part in style.split(";") if part.startswith("margin-left:")]
    if len(matches) == 0:
        return ""

    if len(matches) != 1:
        raise RuntimeError("Unexpected tag style", style)

    return matches[0]


def _extract_division_match_slot(
    weight: int,
    prefix_division: str,
    match_prefixes: dict[str, str],
    all_prefix_counters: dict[tuple[bracket_utils.Division, int], dict[str, int]],
) -> tuple[bracket_utils.Division, bracket_utils.MatchSlot]:
    matched: list[str] = []
    for match_prefix in match_prefixes:
        full_prefix = f"{match_prefix}: "
        if prefix_division.startswith(full_prefix):
            matched.append(match_prefix)

    if len(matched) != 1:
        raise ValueError(
            "Unexpected prefix + division", prefix_division, match_prefixes
        )

    match_prefix = matched[0]
    full_prefix = f"{match_prefix}: "
    division_display = prefix_division[len(full_prefix) :]
    division = normalize_division(division_display)

    match_slot_prefix = match_prefixes[match_prefix]
    all_prefix_counters.setdefault((division, weight), {})
    prefix_counters = all_prefix_counters[(division, weight)]
    prefix_counters[match_slot_prefix] = prefix_counters.get(match_slot_prefix, 0) + 1

    match_slot_index = prefix_counters[match_slot_prefix]
    if match_slot_prefix.endswith("_place"):
        match_slot = match_slot_prefix
    else:
        match_slot = f"{match_slot_prefix}_{match_slot_index:02d}"

    return division, match_slot


def _get_bout_number(bout_mat: str) -> int | None:
    """Parse the bout number.

    The `bout_mat` string may be of the form

    * "Bout m{N}": reserved fora Bye where there is no actual bout number
    * "Bout N (Mat M)": bout with a mat number too
    * "Bout N": bout without a mat number
    """
    match_ = _BOUT_PHANTOM_RE.match(bout_mat)
    if match_ is not None:
        return None

    match_ = _BOUT_MAT_RE.match(bout_mat)
    if match_ is not None:
        bout_number_str, _ = match_.groups()
        return int(bout_number_str)

    match_ = _BOUT_RE.match(bout_mat)
    if match_ is None:
        raise ValueError("Unexpected bout mat string", bout_mat)

    (bout_number_str,) = match_.groups()
    return int(bout_number_str)


def _determine_ot_type(score: str) -> bracket_utils.ResultType:
    win_score, lose_score = score.split("-")
    delta = int(win_score) - int(lose_score)
    if 1 <= delta <= 7:
        return "decision"

    raise NotImplementedError("Unknown result format", score)


def _determine_result_type(result: str) -> bracket_utils.ResultType:
    if result == "Bye":
        return "bye"

    if result.startswith("Dec "):
        return "decision"

    if result.startswith("ID "):
        return "default"
    if result == "MFF":
        return "default"

    if result.startswith("DQ "):
        return "disqualification"

    if result == "DFF":
        return "double_forfeit"

    if result.startswith("F "):
        return "fall"
    if result.startswith("F-SV "):
        return "fall"

    if result == "FF":
        return "forfeit"

    if result.startswith("MD "):
        return "major"

    if result.startswith("TF "):
        return "tech"

    if result.startswith("SV "):
        return _determine_ot_type(result[3:])

    if result.startswith("TB "):
        return _determine_ot_type(result[3:])

    raise NotImplementedError("Unknown result format", result)


def _split_result(extra: str) -> tuple[str, str]:
    if " (TF " in extra:
        loser, result = extra.rsplit(" (TF ")
        return loser, f"TF {result}"

    loser, result = extra.rsplit(" (", 1)
    return loser, result


def _parse_competitor(
    competitor: str, abbreviations: dict[str, str]
) -> bracket_utils.CompetitorRaw | None:
    if competitor == "Bye":
        return None

    if competitor == "Forfeit":
        return None

    name, team_abbreviation = competitor.rsplit(", ", 1)
    team_full = abbreviations.get(team_abbreviation)
    if team_full is None:
        raise KeyError("Unknown team abbreviation", team_abbreviation)
    return bracket_utils.CompetitorRaw(name=name, team_full=team_full)


def _extract_match_info(
    match_info: str, abbreviations: dict[str, str]
) -> tuple[bracket_utils.CompetitorRaw | None, bracket_utils.CompetitorRaw | None, str]:
    if match_info.count(" over ") == 0:
        # NOTE: This is a VERY rare case of a double forfeit
        wrestler1, extra = match_info.split(" vs. ")
        wrestler2, result = extra.rsplit(" (", 1)
        if result != "DFF)":
            raise NotImplementedError("Unexpected result", match_info)

        competitor1 = _parse_competitor(wrestler1, abbreviations)
        competitor2 = _parse_competitor(wrestler2, abbreviations)
        return competitor1, competitor2, "DFF"

    winner, extra = match_info.split(" over ")
    loser, result = _split_result(extra)
    if not result.endswith(")"):
        raise NotImplementedError("Unexpected result", match_info)
    result = result[:-1]

    competitor1 = _parse_competitor(winner, abbreviations)
    competitor2 = _parse_competitor(loser, abbreviations)
    return competitor1, competitor2, result


def _extract_bouts(
    soup: bs4.BeautifulSoup,
    round_name: str,
    match_prefixes: dict[str, str],
    abbreviations: dict[str, str],
) -> list[bracket_utils.MatchRaw]:
    all_div = soup.find_all("div")
    if len(all_div) < 3:
        raise ValueError("Unexpected div count", len(all_div))

    outer_div, title_div = all_div[:2]
    if _get_margin_left_style(outer_div) != "":
        raise ValueError("Unexpected outer div")

    if _get_margin_left_style(title_div) != _TITLE_MARGIN_LEFT:
        raise ValueError("Unexpected title div", _get_margin_left_style(title_div))

    if title_div.text.strip() != round_name:
        raise ValueError("Unexpected title div", title_div.text.strip(), round_name)

    match_divs = all_div[2:]
    all_prefix_counters: dict[tuple[bracket_utils.Division, int], dict[str, int]] = {}
    parsed_matches: list[bracket_utils.MatchRaw] = []
    for match_div in match_divs:
        if _get_margin_left_style(match_div) != _MATCH_MARGIN_LEFT:
            raise ValueError("Unexpected match div", _get_margin_left_style(match_div))

        match_line = match_div.text.strip()
        bout_mat, prefix_division, weight_str, match_info = match_line.split(" - ", 3)
        weight = int(weight_str)

        division, match_slot = _extract_division_match_slot(
            weight, prefix_division, match_prefixes, all_prefix_counters
        )
        bout_number = _get_bout_number(bout_mat)
        winner, loser, result = _extract_match_info(match_info, abbreviations)
        result_type = _determine_result_type(result)

        if bout_number is None and result_type != "bye":
            raise ValueError("Unexpected missing bout number", match_line)

        match_ = bracket_utils.MatchRaw(
            match_slot=match_slot,
            top_competitor=winner,  # TODO
            bottom_competitor=loser,  # TODO
            result=result,
            bout_number=bout_number,
            winner=winner,  # TODO
            winner_from=None,  # TODO
        )
        parsed_matches.append(match_)

    return parsed_matches


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


def main_tmp() -> None:
    here = pathlib.Path(__file__).resolve().parent
    root = here.parent
    path = root / "raw-data" / "2026" / "rounds.selenium.json"
    with open(path) as file_obj:
        by_round = json.load(file_obj)

    path = root / "raw-data" / "2026" / "abbreviations.selenium.json"
    with open(path) as file_obj:
        extracted_abbreviations = _Abbreviations.model_validate_json(file_obj.read())

    abbreviations = extracted_abbreviations.root

    prefixes = {
        "Championship Round 1": {"Champ. Rd of 32": "championship_r32"},
        "Championship Round 2": {"Champ. Rd of 16": "championship_r16"},
        "Consolation Round 2": {"Cons. Rd of 16": "consolation_round2"},
        "Championship Quarterfinals & Consolation Round 3": {
            "Quarters": "championship_quarter",
            "Cons. Sub-Quarters": "consolation_round3",
        },
        "Consolation Round 4": {"Cons. Quarters": "consolation_round4_blood"},
        "Championships Semifinals & Consolation Round 5": {
            "Semis": "championship_semi",
            "Cons. Sub-Semis": "consolation_round5",
        },
        "Consolation Semifinals": {"Cons. Semis": "consolation_round6_semi"},
        "3rd, 5th, 7th Place Bouts": {
            "3rd Place Match": "consolation_third_place",
            "5th Place Match": "consolation_fifth_place",
            "7th Place Match": "consolation_seventh_place",
        },
        "Championship Bouts": {"1st Place Match": "championship_first_place"},
    }
    for round_name, html in by_round.items():
        soup = bs4.BeautifulSoup(html, features="html.parser")
        match_prefixes = prefixes[round_name]
        _extract_bouts(soup, round_name, match_prefixes, abbreviations)


if __name__ == "__main__":
    main_tmp()
