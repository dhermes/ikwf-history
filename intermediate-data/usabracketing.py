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
_BRACKET_MARGIN_LEFT = "margin-left:20px"
_MATCH_MARGIN_LEFT = "margin-left:40px"
_BOUT_PHANTOM_RE = re.compile(r"^Bout m(\d+)$")
_BOUT_MAT_RE = re.compile(r"^Bout (\d+) \(Mat (\d+)\)$")
_BOUT_RE = re.compile(r"^Bout (\d+)$")
_ROUND_PREFIXES: dict[str, dict[str, str]] = {
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
_EXPECTED_BRACKET_ROWS_LENGTH = 65
_ENTRY_INDICES = (
    0,
    4,
    6,
    8,
    12,
    14,
    16,
    20,
    22,
    24,
    28,
    30,
    32,
    36,
    38,
    40,
    44,
    46,
    48,
    52,
    54,
    56,
    60,
    62,
)


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


class _DictStrStr(pydantic.RootModel[dict[str, str]]):
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


def _bout_number_sort(values: list[str], m_positions: dict[str, int]) -> list[str]:
    if len(values) != len(m_positions):
        raise ValueError("Invalid bout count", len(values), len(m_positions))

    reserved_indices: dict[int, str] = {}
    numerical_values: list[int] = []
    for value in values:
        reserved_index = m_positions.get(value)
        if reserved_index is None:
            value_int = int(value)
            numerical_values.append(value_int)
        else:
            reserved_indices[reserved_index] = value

    numerical_values.sort()
    num_values = len(values)

    sorted_result: list[str] = []
    numerical_value_index = 0
    for index in range(num_values):
        reserved_value = reserved_indices.get(index)
        if reserved_value is None:
            numerical_value = numerical_values[numerical_value_index]
            sorted_result.append(str(numerical_value))
            numerical_value_index += 1
        else:
            sorted_result.append(reserved_value)

    return sorted_result


def _to_match_slot_map(match_slot_prefix: str, bout_number_strs: list[str]) -> dict:
    result: dict[str, bracket_utils.MatchSlot] = {}
    for index, bout_number_str in enumerate(bout_number_strs):
        slot_index = index + 1
        match_slot = f"{match_slot_prefix}_{slot_index:02}"
        result[bout_number_str] = match_slot

    return result


def _extract_match_slots(
    match_slot_prefix: str, bout_number_strs: list[str]
) -> dict[str, bracket_utils.MatchSlot]:
    # NOTE: For the "no bout here" bouts, they have special sentinel numbers
    #       * championship_r32:          m2, m4, m6, m8, m10, m12, m14, m16
    #       * championship_r16:          m17, m19, m21, m23, m25, m27, m29, m31
    #       * consolation_round2:        m33, m34, m35, m36, m37, m38, m39, m40
    #       * championship_quarter:      m41, m42, m43, m44
    #       * consolation_round3:        m45, m46, m47, m48
    #       * consolation_round4_blood:  m49, m50, m51, m52
    #       * championship_semi:         m53, m54
    #       * consolation_round5:        m55, m56
    #       * consolation_round6_semi:   m57, m58
    #       * consolation_seventh_place: m59
    #       * consolation_fifth_place:   m60
    #       * consolation_third_place:   m61
    if match_slot_prefix == "championship_r32":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs,
            {
                "m2": 0,
                "m4": 1,
                "m6": 2,
                "m8": 3,
                "m10": 4,
                "m12": 5,
                "m14": 6,
                "m16": 7,
            },
        )

        result: dict[str, bracket_utils.MatchSlot] = {}
        for index, bout_number_str in enumerate(sorted_bout_number_strs):
            slot_index = 2 * (index + 1)
            # NOTE: We skip the byes for the sectional champions, they do
            #       not show up as bouts.
            match_slot = f"championship_r32_{slot_index:02}"
            result[bout_number_str] = match_slot

        return result

    if match_slot_prefix == "championship_r16":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs,
            {
                "m17": 0,
                "m19": 1,
                "m21": 2,
                "m23": 3,
                "m25": 4,
                "m27": 5,
                "m29": 6,
                "m31": 7,
            },
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "consolation_round2":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs,
            {
                "m33": 0,
                "m34": 1,
                "m35": 2,
                "m36": 3,
                "m37": 4,
                "m38": 5,
                "m39": 6,
                "m40": 7,
            },
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "championship_quarter":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs,
            {"m41": 0, "m42": 1, "m43": 2, "m44": 3},
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "consolation_round3":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs,
            {"m45": 0, "m46": 1, "m47": 2, "m48": 3},
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "consolation_round4_blood":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs,
            {"m49": 0, "m50": 1, "m51": 2, "m52": 3},
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "championship_semi":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs, {"m53": 0, "m54": 1}
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "consolation_round5":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs, {"m55": 0, "m56": 1}
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix == "consolation_round6_semi":
        sorted_bout_number_strs = _bout_number_sort(
            bout_number_strs, {"m57": 0, "m58": 1}
        )
        return _to_match_slot_map(match_slot_prefix, sorted_bout_number_strs)

    if match_slot_prefix in (
        "consolation_seventh_place",
        "consolation_fifth_place",
        "consolation_third_place",
        "championship_first_place",
    ):
        (bout_number_str,) = bout_number_strs
        result: dict[str, bracket_utils.MatchSlot] = {
            bout_number_str: match_slot_prefix
        }
        return result

    raise ValueError("Unexpected match slot prefix", match_slot_prefix)


def _get_bout_number_str(bout_mat: str) -> str:
    """Parse the bout number.

    The `bout_mat` string may be of the form

    * "Bout m{N}": reserved for a Bye where there is no actual bout number
    * "Bout N (Mat M)": bout with a mat number too
    * "Bout N": bout without a mat number
    """
    match_ = _BOUT_PHANTOM_RE.match(bout_mat)
    if match_ is not None:
        (bout_number_str,) = match_.groups()
        return f"m{bout_number_str}"

    match_ = _BOUT_MAT_RE.match(bout_mat)
    if match_ is not None:
        bout_number_str, _ = match_.groups()
        return bout_number_str

    match_ = _BOUT_RE.match(bout_mat)
    if match_ is None:
        raise ValueError("Unexpected bout mat string", bout_mat)

    (bout_number_str,) = match_.groups()
    return bout_number_str


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


_EntriesMap = dict[
    tuple[bracket_utils.Division, int], list[bracket_utils.CompetitorRaw | None]
]


def _match_r32_bye(
    winner: bracket_utils.CompetitorRaw | None,
    loser: bracket_utils.CompetitorRaw | None,
    entry: bracket_utils.CompetitorRaw | None,
) -> None:
    if loser is not None:
        raise ValueError("Unexpected bye", loser)


def _match_r32_match(
    winner: bracket_utils.CompetitorRaw | None,
    loser: bracket_utils.CompetitorRaw | None,
    top_entry: bracket_utils.CompetitorRaw | None,
    bottom_entry: bracket_utils.CompetitorRaw | None,
) -> None:
    pass


def _determine_top_bottom(
    winner: bracket_utils.CompetitorRaw | None,
    loser: bracket_utils.CompetitorRaw | None,
    entries: list[bracket_utils.CompetitorRaw | None],
    match_slot: bracket_utils.MatchSlot,
) -> None:
    if match_slot == "championship_r32_01":
        _match_r32_bye(winner, loser, entries[0])

    if match_slot == "championship_r32_02":
        _match_r32_match(winner, loser, entries[1], entries[2])

    if match_slot == "championship_r32_03":
        _match_r32_bye(winner, loser, entries[3])

    if match_slot == "championship_r32_04":
        _match_r32_match(winner, loser, entries[4], entries[5])

    if match_slot == "championship_r32_05":
        _match_r32_bye(winner, loser, entries[6])

    if match_slot == "championship_r32_06":
        _match_r32_match(winner, loser, entries[7], entries[8])

    if match_slot == "championship_r32_07":
        _match_r32_bye(winner, loser, entries[9])

    if match_slot == "championship_r32_08":
        _match_r32_match(winner, loser, entries[10], entries[11])

    if match_slot == "championship_r32_09":
        _match_r32_bye(winner, loser, entries[12])

    if match_slot == "championship_r32_10":
        _match_r32_match(winner, loser, entries[13], entries[14])

    if match_slot == "championship_r32_11":
        _match_r32_bye(winner, loser, entries[15])

    if match_slot == "championship_r32_12":
        _match_r32_match(winner, loser, entries[16], entries[17])

    if match_slot == "championship_r32_13":
        _match_r32_bye(winner, loser, entries[18])

    if match_slot == "championship_r32_14":
        _match_r32_match(winner, loser, entries[19], entries[20])

    if match_slot == "championship_r32_15":
        _match_r32_bye(winner, loser, entries[21])

    if match_slot == "championship_r32_16":
        _match_r32_match(winner, loser, entries[22], entries[23])


def _extract_bouts(
    soup: bs4.BeautifulSoup,
    round_name: str,
    match_slot_prefixes: dict[str, str],
    abbreviations: dict[str, str],
    entries_map: _EntriesMap,
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

    # 1. Do a first pass to bucket all matches by bracket. Only after that can
    #    we resolve the `match_slot` because the matches do not appear in order.
    #    (We can order them with the bout numbers.)
    match_divs = all_div[2:]
    bracket_key: tuple[bracket_utils.Division, int] | None = None
    brackets_first_pass: dict[
        tuple[bracket_utils.Division, int], dict[str, dict[str, str]]
    ] = {}
    for match_div in match_divs:
        margin_left_style = _get_margin_left_style(match_div)

        if margin_left_style == _BRACKET_MARGIN_LEFT:
            bracket_line = match_div.text.strip()
            division_display, weight_str = bracket_line.split(" - ")
            weight = int(weight_str)
            division = normalize_division(division_display)
            bracket_key = division, weight
            continue

        if margin_left_style != _MATCH_MARGIN_LEFT:
            raise ValueError("Unexpected match div", margin_left_style)

        if bracket_key is None:
            raise ValueError("Expected bracket key to be set", match_div)

        match_line = match_div.text.strip()
        if not isinstance(match_line, str):
            raise TypeError("Invalid type", match_line)
        bout_mat, round_description, match_info = match_line.split(" - ", 2)
        match_slot_prefix = match_slot_prefixes[round_description]
        bout_number_str = _get_bout_number_str(bout_mat)

        by_prefix = brackets_first_pass.setdefault(bracket_key, {})
        by_bout_number = by_prefix.setdefault(match_slot_prefix, {})
        if bout_number_str in by_bout_number:
            raise KeyError(
                "Bout already seen", bracket_key, match_slot_prefix, bout_number_str
            )

        by_bout_number[bout_number_str] = match_info

    # 2. Go through each bracket, sort the bouts to determine `match_slot`, then
    #    continue parsing the match info (wrestlers, teams, result).
    parsed_matches: list[bracket_utils.MatchRaw] = []
    for bracket_key, by_prefix in brackets_first_pass.items():
        entries = entries_map[bracket_key]
        for match_slot_prefix, by_bout_number in by_prefix.items():
            bout_number_strs = list(by_bout_number.keys())
            match_slot_map = _extract_match_slots(match_slot_prefix, bout_number_strs)
            for bout_number_str, match_slot in match_slot_map.items():
                match_info = by_bout_number[bout_number_str]
                bout_number = (
                    None if bout_number_str.startswith("m") else int(bout_number_str)
                )
                winner, loser, result = _extract_match_info(match_info, abbreviations)
                result_type = _determine_result_type(result)

                if bout_number is None and result_type != "bye":
                    raise ValueError(
                        "Unexpected missing bout number", bout_number_str, match_info
                    )

                _determine_top_bottom(winner, loser, entries, match_slot)
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

            if match_slot_prefix == "championship_r32":
                for bye_index in range(8):
                    slot_index = 2 * bye_index + 1
                    match_slot = f"championship_r32_{slot_index:02}"
                    entry_index = 3 * bye_index
                    winner = entries[entry_index]
                    match_ = bracket_utils.MatchRaw(
                        match_slot=match_slot,
                        top_competitor=winner,
                        bottom_competitor=None,
                        result=result,
                        bout_number=bout_number,
                        winner=winner,
                        winner_from=None,
                    )
                    parsed_matches.append(match_)

    return parsed_matches


def _extract_entry_athlete(td: bs4.Tag) -> tuple[str, str] | None:
    parts = list(td.stripped_strings)
    parts = [part for part in parts if part != "_"]
    if parts == ["Bye"]:
        return None

    if len(parts) == 4:
        first_name, last_name, team, bout_number = parts
        int(bout_number)  # Assert it is an integer
    elif len(parts) == 3:
        first_name, last_name, team = parts
    else:
        raise ValueError("Unexpected athlete <td>", len(parts), parts, td)

    name = f"{first_name} {last_name}"
    team = team.strip().lstrip("(").rstrip(")").strip()
    return name.strip(), team


def _add_initial_entries(soup: bs4.BeautifulSoup, entries_map: _EntriesMap) -> None:
    bracket_name = _extract_bracket_name(soup)
    division_display, weight_str = bracket_name.rsplit(" ", 1)
    weight = int(weight_str)
    division = normalize_division(division_display)

    (bracket_pages,) = soup.find_all("div", id="bracketPages")
    inner_divs = bracket_pages.find_all("div", recursive=False)
    if len(inner_divs) != 2:
        raise RuntimeError("Failed to bracket pages", len(inner_divs), key)

    championship_bouts, _ = inner_divs
    (bracket_table,) = championship_bouts.find_all("table", recursive=False)
    (bracket_tbody,) = bracket_table.find_all("tbody", recursive=False)
    table_rows = bracket_tbody.find_all("tr", attrs={"height": "13px"}, recursive=False)
    if len(table_rows) != _EXPECTED_BRACKET_ROWS_LENGTH:
        raise ValueError("Unexpected rows", len(table_rows))

    entries: list[bracket_utils.CompetitorRaw | None] = []
    for index in _ENTRY_INDICES:
        tr = table_rows[index]
        all_td = tr.find_all("td", recursive=False)
        if len(all_td) < 2:
            raise ValueError("Unexpected row", index, len(all_td))
        athlete_td = all_td[1]
        extracted = _extract_entry_athlete(athlete_td)
        if extracted is not None:
            name, team = extracted
            entries.append(bracket_utils.CompetitorRaw(name=name, team_full=team))
        else:
            entries.append(None)

    if len(entries) != 24:
        raise RuntimeError("Unexpected number of entries")

    key = (division, weight)
    if key in entries_map:
        raise KeyError("Unexpected duplicate bracket", key)

    entries_map[key] = entries


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
        extracted_abbreviations = _DictStrStr.model_validate_json(file_obj.read())

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
    with open(path, "rb") as file_obj:
        extracted_by_round = _DictStrStr.model_validate_json(file_obj.read())

    by_round = extracted_by_round.root

    path = root / "raw-data" / "2026" / "abbreviations.selenium.json"
    with open(path, "rb") as file_obj:
        extracted_abbreviations = _DictStrStr.model_validate_json(file_obj.read())

    abbreviations = extracted_abbreviations.root

    path = root / "raw-data" / "2026" / "brackets.selenium.json"
    with open(path, "rb") as file_obj:
        extracted_brackets = _DictStrStr.model_validate_json(file_obj.read())

    brackets = extracted_brackets.root

    entries_map: _EntriesMap = {}
    for html in brackets.values():
        soup = bs4.BeautifulSoup(html, features="html.parser")
        _add_initial_entries(soup, entries_map)

    for round_name, html in by_round.items():
        soup = bs4.BeautifulSoup(html, features="html.parser")
        match_slot_prefixes = _ROUND_PREFIXES[round_name]
        _extract_bouts(
            soup, round_name, match_slot_prefixes, abbreviations, entries_map
        )


if __name__ == "__main__":
    main_tmp()
