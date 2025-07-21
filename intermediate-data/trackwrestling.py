# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from collections.abc import Callable
from typing import Any, Literal

import bracket_utils
import bs4
import pydantic

_MISSING_BOUT_NUMBER_SENTINEL = -30788
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
_ACRONYM_EXCEPTIONS: tuple[str, ...] = ("E1", "G2", "P3WW")


MatchSlotMap = dict[
    tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition],
    list[bracket_utils.CompetitorRaw],
]
MatchSlotsByBracket = dict[tuple[bracket_utils.Division, int], MatchSlotMap]


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


def _determine_acronym(value: str) -> str | None:
    if value in _ACRONYM_EXCEPTIONS:
        return value

    # If the "acronym" is an integer team ID, ignore it
    try:
        int(value)
        return None
    except ValueError:
        pass

    if value.upper() != value:
        raise NotImplementedError(value)

    if not value.isalpha():
        raise NotImplementedError(value)

    return value


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

        acronym = _determine_acronym(all_td[2].text)
        scores.append(
            bracket_utils.TeamScore(
                team=all_td[1].text, acronym=acronym, score=float(all_td[3].text)
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


class Deductions(pydantic.RootModel[list[bracket_utils.Deduction]]):
    pass


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

    return wrestler_td.text == "Bye"


def _get_team_matches(
    team_prefix: str, division_scores: list[bracket_utils.TeamScore]
) -> list[str]:
    # NOTE: 15 characters is the length where team names get abbreviated, so
    #       for this length only allow exact matches.
    if len(team_prefix) < 15:
        for score in division_scores:
            if score.team == team_prefix:
                return [team_prefix]

        return []

    matches: list[str] = []
    for score in division_scores:
        if score.team.startswith(team_prefix):
            matches.append(score.team)

    return matches


def _split_name_team_initial(
    name_team: str,
    division_scores: list[bracket_utils.TeamScore],
    name_fixes: dict[str, str],
    team_fixes: dict[str, tuple[str, str]],
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

    name = name_fixes.get(name, name)
    team_fix = team_fixes.get(name)
    if team_fix is not None:
        expected_team, full_team = team_fix
        if team_prefix != expected_team:
            raise RuntimeError("Invariant violation", name_team, team_fix)

        team_prefix = full_team

    matches = _get_team_matches(team_prefix, division_scores)
    if len(matches) != 1:
        raise RuntimeError("Invariant violation", name_team, matches)

    team_full = matches[0]
    return bracket_utils.CompetitorRaw(name=name, team_full=team_full)


def initial_entries(
    soup: bs4.BeautifulSoup,
    division_scores: list[bracket_utils.TeamScore],
    name_fixes: dict[str, str],
    team_fixes: dict[str, tuple[str, str]],
    opening_bouts: list[int],
) -> MatchSlotMap:
    initial_bout_index = 0

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
            if bout_number is not None:
                expected_bout_number = opening_bouts[initial_bout_index]
                if bout_number != expected_bout_number:
                    raise RuntimeError("Invariant violation", index)
                initial_bout_index += 1

        if not _is_valid_initial_entry(wrestler_td, bout_number, opening_bouts):
            raise RuntimeError("Invariant violation", index, wrestler_td)

        competitor_raw = _split_name_team_initial(
            wrestler_td.text, division_scores, name_fixes, team_fixes
        )
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
            raise RuntimeError(
                "Invariant violation",
                winner,
                top_competitor_names,
                bottom_competitor_names,
            )

        top_competitor = top_competitors[winner_top_index]
        bottom_competitor = None
        top_win = True
    elif winner_bottom_index is not None:
        if winner_top_index is not None:
            raise RuntimeError(
                "Invariant violation",
                winner,
                top_competitor_names,
                bottom_competitor_names,
            )

        top_competitor = None
        bottom_competitor = bottom_competitors[winner_bottom_index]
        top_win = False
    else:
        if winner.strip() != "()":
            raise RuntimeError(
                "Invariant violation",
                winner,
                top_competitor_names,
                bottom_competitor_names,
            )

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
        top_competitor = top_competitors[winner_top_index]
        top_win = True

        if loser.strip() == "()" and result == "FF":
            if len(bottom_competitors) != 1:
                raise NotImplementedError

            bottom_competitor = bottom_competitors[0]
        elif (
            loser_bottom_index is not None
            and winner_bottom_index is None
            and loser_top_index is None
        ):
            bottom_competitor = bottom_competitors[loser_bottom_index]
        else:
            raise RuntimeError(
                "Invariant violation",
                winner,
                loser,
                result,
                top_competitor_names,
                bottom_competitor_names,
            )
    elif winner_bottom_index is not None:
        bottom_competitor = bottom_competitors[winner_bottom_index]
        top_win = False

        if loser.strip() == "()" and result == "FF":
            if len(top_competitors) != 1:
                raise NotImplementedError

            top_competitor = top_competitors[0]
        elif (
            loser_top_index is not None
            and winner_top_index is None
            and loser_bottom_index is None
        ):
            top_competitor = top_competitors[loser_top_index]
        else:
            raise RuntimeError(
                "Invariant violation",
                winner,
                loser,
                result,
                top_competitor_names,
                bottom_competitor_names,
            )
    else:
        raise RuntimeError(
            "Invariant violation",
            winner,
            loser,
            result,
            top_competitor_names,
            bottom_competitor_names,
        )

    return top_competitor, bottom_competitor, top_win, result


class MatchWithBracket(pydantic.BaseModel):
    division: bracket_utils.Division
    weight: int
    match: bracket_utils.Match


def _add_r32_bye(
    index: int,
    division: bracket_utils.Division,
    weight: int,
    matches: list[MatchWithBracket],
    match_slot_map: MatchSlotMap,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
) -> None:
    """Add a bye in the Round of 32 for a sectional winner."""
    slot_id = 2 * (index + 1) - 1
    match_slot: bracket_utils.MatchSlot = f"championship_r32_{slot_id:02}"

    competitors = match_slot_map[(match_slot, "top")]
    if len(competitors) == 0:
        # NOTE: In very rare cases, there was **NO** sectional winner.
        win_position = bracket_utils.next_match_position_win(match_slot)
        match_slot_map.setdefault(win_position, [])
        return

    if len(competitors) != 1:
        raise RuntimeError(
            "Invariant violation", match_slot, division, weight, len(competitors)
        )

    competitor = competitors[0]
    match = MatchWithBracket(
        division=division,
        weight=weight,
        match=bracket_utils.Match(
            match_slot=match_slot,
            top_competitor=bracket_utils.competitor_from_raw(
                competitor, name_exceptions
            ),
            bottom_competitor=None,
            result="Bye",
            result_type="bye",
            bout_number=None,
            top_win=True,
        ),
    )
    matches.append(match)

    win_position = bracket_utils.next_match_position_win(match_slot)
    match_slot_map.setdefault(win_position, [])
    match_slot_map[win_position].append(competitor)


def _round_line_split(line: str, prefix: str) -> tuple[int, str, str, str]:
    parts = line.split(" :: ")
    if len(parts) != 5:
        raise RuntimeError("Invariant violation", len(parts), line)

    actual_prefix, bout_number_str, winner, loser, result = parts
    if actual_prefix != prefix:
        raise RuntimeError("Unexpected prefix", actual_prefix, prefix, line)

    if bout_number_str == "":
        bout_number = _MISSING_BOUT_NUMBER_SENTINEL
    else:
        bout_number = int(bout_number_str)

    # Swap loser and winner if a Bye is involved
    if winner.strip() == "()":
        winner, loser = loser, winner

    return bout_number, winner, loser, result


def _overtime_result_type(result: str, prefix: str) -> bracket_utils.ResultType:
    without_prefix = result[len(prefix) :]
    if without_prefix.startswith("(Fall) "):
        return "fall"

    score_win_str, score_lose_str = without_prefix.split("-")
    score_win = int(score_win_str)
    score_lose = int(score_lose_str)
    delta = abs(score_win - score_lose)  # Scores may be flipped
    if 0 < delta < 8:
        return "decision"

    if 8 <= delta < 15:
        return "major"

    raise NotImplementedError("Unexpected result", result, prefix)


def _determine_result_type(result: str) -> bracket_utils.ResultType:
    if result in ("UTB 0-0", "2-OT 3-3"):
        return "decision"

    if result.startswith("OT "):
        return _overtime_result_type(result, "OT ")

    if result.startswith("2-OT "):
        return _overtime_result_type(result, "2-OT ")

    if result.startswith("SV-1 "):
        return _overtime_result_type(result, "SV-1 ")

    if result.startswith("SV-2 "):
        return _overtime_result_type(result, "SV-2 ")

    if result.startswith("TB-1 "):
        return _overtime_result_type(result, "TB-1 ")

    if result.startswith("UTB "):
        return _overtime_result_type(result, "UTB ")

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

    if result == "FF" or result == "MFF" or result == "MFFL":
        return "forfeit"

    if result == "NC" or result == "OTHR1":
        return "walkover"

    if result == "DQ":
        return "disqualification"

    if result == "Bye":
        return "bye"

    raise NotImplementedError(result)


HelperVersion = Literal["v1", "v2", "v3"]


def _next_match_position_lose_v1(
    match_slot: bracket_utils.MatchSlot,
) -> tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition] | None:
    """In use from 2007-2019"""
    # NOTE: Earlier brackets used follow-the-leader so these are not guaranteed
    #       to happen unless the winner reached the semifinals.
    if match_slot == "championship_r32_02":
        return "consolation_round3_01", "bottom"

    if match_slot == "championship_r32_04":
        return "consolation_round3_01", "bottom"

    if match_slot == "championship_r32_06":
        return "consolation_round3_02", "bottom"

    if match_slot == "championship_r32_08":
        return "consolation_round3_02", "bottom"

    if match_slot == "championship_r32_10":
        return "consolation_round3_03", "bottom"

    if match_slot == "championship_r32_12":
        return "consolation_round3_03", "bottom"

    if match_slot == "championship_r32_14":
        return "consolation_round3_04", "bottom"

    if match_slot == "championship_r32_16":
        return "consolation_round3_04", "bottom"

    if match_slot == "championship_r16_01":
        return "consolation_round3_01", "top"

    if match_slot == "championship_r16_02":
        return "consolation_round3_01", "top"

    if match_slot == "championship_r16_03":
        return "consolation_round3_02", "top"

    if match_slot == "championship_r16_04":
        return "consolation_round3_02", "top"

    if match_slot == "championship_r16_05":
        return "consolation_round3_03", "top"

    if match_slot == "championship_r16_06":
        return "consolation_round3_03", "top"

    if match_slot == "championship_r16_07":
        return "consolation_round3_04", "top"

    if match_slot == "championship_r16_08":
        return "consolation_round3_04", "top"

    if match_slot == "championship_quarter_01":
        return "consolation_round4_blood_01", "top"

    if match_slot == "championship_quarter_02":
        return "consolation_round4_blood_02", "top"

    if match_slot == "championship_quarter_03":
        return "consolation_round4_blood_03", "bottom"

    if match_slot == "championship_quarter_04":
        return "consolation_round4_blood_04", "bottom"

    if match_slot == "championship_semi_01":
        return "consolation_round6_semi_01", "top"

    if match_slot == "championship_semi_02":
        return "consolation_round6_semi_02", "bottom"

    if match_slot == "consolation_round5_01":
        return "consolation_seventh_place", "top"

    if match_slot == "consolation_round5_02":
        return "consolation_seventh_place", "bottom"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_fifth_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_fifth_place", "bottom"

    raise NotImplementedError(match_slot)


def _next_match_position_lose_v2(
    match_slot: bracket_utils.MatchSlot,
) -> tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition] | None:
    """In use from 2022-2022"""
    if match_slot == "championship_r32_02":
        return "consolation_round2_01", "bottom"

    if match_slot == "championship_r32_04":
        return "consolation_round2_02", "bottom"

    if match_slot == "championship_r32_06":
        return "consolation_round2_03", "bottom"

    if match_slot == "championship_r32_08":
        return "consolation_round2_04", "bottom"

    if match_slot == "championship_r32_10":
        return "consolation_round2_05", "top"

    if match_slot == "championship_r32_12":
        return "consolation_round2_06", "top"

    if match_slot == "championship_r32_14":
        return "consolation_round2_07", "top"

    if match_slot == "championship_r32_16":
        return "consolation_round2_08", "top"

    if match_slot == "championship_r16_01":
        return "consolation_round2_08", "bottom"

    if match_slot == "championship_r16_02":
        return "consolation_round2_07", "bottom"

    if match_slot == "championship_r16_03":
        return "consolation_round2_06", "bottom"

    if match_slot == "championship_r16_04":
        return "consolation_round2_05", "bottom"

    if match_slot == "championship_r16_05":
        return "consolation_round2_04", "top"

    if match_slot == "championship_r16_06":
        return "consolation_round2_03", "top"

    if match_slot == "championship_r16_07":
        return "consolation_round2_02", "top"

    if match_slot == "championship_r16_08":
        return "consolation_round2_01", "top"

    if match_slot == "championship_quarter_01":
        return "consolation_round4_blood_03", "bottom"

    if match_slot == "championship_quarter_02":
        return "consolation_round4_blood_04", "bottom"

    if match_slot == "championship_quarter_03":
        return "consolation_round4_blood_01", "top"

    if match_slot == "championship_quarter_04":
        return "consolation_round4_blood_02", "top"

    if match_slot == "championship_semi_01":
        return "consolation_round6_semi_01", "top"

    if match_slot == "championship_semi_02":
        return "consolation_round6_semi_02", "bottom"

    if match_slot == "consolation_round5_01":
        return "consolation_seventh_place", "top"

    if match_slot == "consolation_round5_02":
        return "consolation_seventh_place", "bottom"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_fifth_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_fifth_place", "bottom"

    raise NotImplementedError(match_slot)


def _next_match_position_lose_v3(
    match_slot: bracket_utils.MatchSlot,
) -> tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition] | None:
    """In use from 2023-2025"""
    if match_slot == "championship_r32_02":
        return "consolation_round2_01", "bottom"

    if match_slot == "championship_r32_04":
        return "consolation_round2_02", "bottom"

    if match_slot == "championship_r32_06":
        return "consolation_round2_03", "bottom"

    if match_slot == "championship_r32_08":
        return "consolation_round2_04", "bottom"

    if match_slot == "championship_r32_10":
        return "consolation_round2_05", "top"

    if match_slot == "championship_r32_12":
        return "consolation_round2_06", "top"

    if match_slot == "championship_r32_14":
        return "consolation_round2_07", "top"

    if match_slot == "championship_r32_16":
        return "consolation_round2_08", "top"

    if match_slot == "championship_r16_01":
        return "consolation_round2_08", "bottom"

    if match_slot == "championship_r16_02":
        return "consolation_round2_07", "bottom"

    if match_slot == "championship_r16_03":
        return "consolation_round2_06", "bottom"

    if match_slot == "championship_r16_04":
        return "consolation_round2_05", "bottom"

    if match_slot == "championship_r16_05":
        return "consolation_round2_04", "top"

    if match_slot == "championship_r16_06":
        return "consolation_round2_03", "top"

    if match_slot == "championship_r16_07":
        return "consolation_round2_02", "top"

    if match_slot == "championship_r16_08":
        return "consolation_round2_01", "top"

    if match_slot == "championship_quarter_01":
        return "consolation_round4_blood_02", "top"

    if match_slot == "championship_quarter_02":
        return "consolation_round4_blood_01", "top"

    if match_slot == "championship_quarter_03":
        return "consolation_round4_blood_04", "bottom"

    if match_slot == "championship_quarter_04":
        return "consolation_round4_blood_03", "bottom"

    if match_slot == "championship_semi_01":
        return "consolation_round6_semi_02", "bottom"

    if match_slot == "championship_semi_02":
        return "consolation_round6_semi_01", "top"

    if match_slot == "consolation_round5_01":
        return "consolation_seventh_place", "top"

    if match_slot == "consolation_round5_02":
        return "consolation_seventh_place", "bottom"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_fifth_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_fifth_place", "bottom"

    raise NotImplementedError(match_slot)


def _next_match_position_lose(
    helper_version: HelperVersion, match_slot: bracket_utils.MatchSlot
) -> tuple[bracket_utils.MatchSlot, bracket_utils.BracketPosition] | None:
    if helper_version == "v1":
        return _next_match_position_lose_v1(match_slot)

    if helper_version == "v2":
        return _next_match_position_lose_v2(match_slot)

    if helper_version == "v3":
        return _next_match_position_lose_v3(match_slot)

    raise NotImplementedError(helper_version)


def parse_r32(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    helper_version: HelperVersion,
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the top-side wrestler that
            #    had a bye.
            _add_r32_bye(i, division, weight, matches, match_slot_map, name_exceptions)

            # 3. Make the `match_slot_map` aware of the loser
            # NOTE: The loser **MIGHT** have a match, **IF** the winner makes
            #       the semifinals. But this is true for another R32 loser so we
            #       need to keep an array.
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_r16(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    helper_version: HelperVersion,
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            # NOTE: The loser **MIGHT** have a match, **IF** the winner makes
            #       the semifinals. But this is true for another R16 loser so we
            #       need to keep an array.
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_quarterfinal(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    helper_version: HelperVersion,
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_consolation_round2(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
            match_slot: bracket_utils.MatchSlot = f"consolation_round2_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) > 1:
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # Make the `match_slot_map` aware of the winner (loser is eliminated)
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_quarterfinal_mixed(
    round_name: str,
    quarterfinal_match_prefix: str,
    cons_match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    helper_version: HelperVersion,
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
        key = (division, weight)
        round_keys.add(key)

        match_slot_map = match_slots_by_bracket[key]

        ul_sibling = h2.find_next_sibling()
        if ul_sibling.name != "ul":
            raise RuntimeError("Invariant violation", ul_sibling)

        all_entries: list[bs4.Tag] = [li for li in ul_sibling.find_all("li")]
        if len(all_entries) != 8:
            raise RuntimeError("Invariant violation", all_entries)

        # Quarterfinals
        for i in range(4):
            entry = all_entries[i]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"championship_quarter_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, quarterfinal_match_prefix
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

        # Wrestlebacks
        for i in range(4):
            entry = all_entries[i + 4]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"consolation_round3_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, cons_match_prefix
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # Make the `match_slot_map` aware of the winner (loser is eliminated)
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_consolation_round3(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # Make the `match_slot_map` aware of the winner (loser is eliminated)
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_consolation_round4(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
            if len(top_competitors) > 1:
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # Make the `match_slot_map` aware of the winner (loser is eliminated)
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_semi_mixed(
    round_name: str,
    semi_match_prefix: str,
    cons_match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    helper_version: HelperVersion,
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
            if len(top_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, semi_match_prefix
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

        # Wrestlebacks
        for i in range(2):
            entry = all_entries[i + 2]
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"consolation_round5_{slot_id:02}"

            top_competitors = match_slot_map[(match_slot, "top")]
            if len(top_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(top_competitors), match_slot
                )

            bottom_competitors = match_slot_map[(match_slot, "bottom")]
            if len(bottom_competitors) > 1:
                raise RuntimeError(
                    "Invariant violation", len(bottom_competitors), match_slot
                )

            bout_number, winner, loser, result = _round_line_split(
                entry.text, cons_match_prefix
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_consolation_semi(
    round_name: str,
    match_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    helper_version: HelperVersion,
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
            if len(top_competitors) > 1:
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
            loser_competitor = bottom_competitor
            if not top_win:
                winner_competitor = bottom_competitor
                loser_competitor = top_competitor

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
                    result=result,
                    result_type=_determine_result_type(result),
                    bout_number=bout_number,
                    top_win=top_win,
                ),
            )
            matches.append(match)

            # 1. Make the `match_slot_map` aware of the winner
            win_position = bracket_utils.next_match_position_win(match_slot)
            match_slot_map.setdefault(win_position, [])
            if winner_competitor is not None:
                match_slot_map[win_position].append(winner_competitor)

            # 2. Make the `match_slot_map` aware of the loser
            lose_position = _next_match_position_lose(helper_version, match_slot)
            match_slot_map.setdefault(lose_position, [])
            if loser_competitor is not None:
                match_slot_map[lose_position].append(loser_competitor)

    match_slot_keys = set(match_slots_by_bracket.keys())
    if round_keys != match_slot_keys:
        raise RuntimeError("Invariant violation")

    return matches


def parse_place_matches_v1(
    round_name: str,
    first_place_prefix: str,
    third_place_prefix: str,
    fifth_place_prefix: str,
    seventh_place_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
) -> list[MatchWithBracket]:
    """Used in 2007"""
    html = selenium_rounds.pop(round_name, None)
    if not isinstance(html, str):
        raise TypeError("Unexpected value", type(html), round_name)

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_h1_text = [h1.text for h1 in soup.find_all("h1")]
    if all_h1_text != [round_name]:
        raise RuntimeError("Invariant violation", all_h1_text)

    prefixes_and_slots: tuple[tuple[str, bracket_utils.MatchSlot]] = (
        (first_place_prefix, "championship_first_place"),
        (third_place_prefix, "consolation_third_place"),
        (fifth_place_prefix, "consolation_fifth_place"),
        (seventh_place_prefix, "consolation_seventh_place"),
    )

    all_h2: list[bs4.Tag] = soup.find_all("h2")
    round_keys: set[tuple[bracket_utils.Division, int]] = set()
    matches: list[MatchWithBracket] = []
    for h2 in all_h2:
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
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


def parse_place_matches_v2(
    round_name: str,
    third_place_prefix: str,
    fifth_place_prefix: str,
    seventh_place_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
) -> list[MatchWithBracket]:
    """Used from 2008-????"""
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
            if len(top_competitors) > 1:
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
            if loser.strip() == "()" and result == "Bye":
                top_competitor, bottom_competitor, top_win, result = _handle_bye(
                    winner, result, top_competitors, bottom_competitors
                )
            else:
                top_competitor, bottom_competitor, top_win, result = _handle_match(
                    winner, loser, result, top_competitors, bottom_competitors
                )

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
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


def parse_championship_matches(
    round_name: str,
    first_place_prefix: str,
    selenium_rounds: dict,
    match_slots_by_bracket: MatchSlotsByBracket,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
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
        division_display, weight_str = h2.text.rsplit(None, 1)
        weight = int(weight_str)
        division = normalize_division(division_display)
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
            if len(top_competitors) > 1:
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
            if loser.strip() == "()":
                top_competitor, bottom_competitor, top_win, result = _handle_bye(
                    winner, result, top_competitors, bottom_competitors
                )
            else:
                top_competitor, bottom_competitor, top_win, result = _handle_match(
                    winner, loser, result, top_competitors, bottom_competitors
                )

            match = MatchWithBracket(
                division=division,
                weight=weight,
                match=bracket_utils.Match(
                    match_slot=match_slot,
                    top_competitor=bracket_utils.competitor_from_raw(
                        top_competitor, name_exceptions
                    ),
                    bottom_competitor=bracket_utils.competitor_from_raw(
                        bottom_competitor, name_exceptions
                    ),
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


ParseRoundsFunc = Callable[[Any, MatchSlotsByBracket], list[MatchWithBracket]]


def _strip_suffix_deductions(
    deductions: list[bracket_utils.Deduction],
) -> list[bracket_utils.Deduction]:
    normalized: list[bracket_utils.Deduction] = []
    for deduction in deductions:
        team = deduction.team
        if team.endswith(", IL"):
            team = team[: -len(", IL")]

        normalized.append(
            bracket_utils.Deduction(
                team=team, reason=deduction.reason, value=deduction.value
            )
        )

    return normalized


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
        extracted = Deductions.model_validate_json(file_obj.read())

    deductions = _strip_suffix_deductions(extracted.root)

    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    with open(root / "rounds.selenium.json") as file_obj:
        selenium_rounds = json.load(file_obj)

    match_slots_by_bracket: MatchSlotsByBracket = {}

    all_opening_bout_numbers = _get_all_opening_bout_numbers(
        selenium_rounds, prelim_round_name, prelim_match_prefix
    )

    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = normalize_division(division_display)
        division_scores = team_scores[division]
        key = (division, weight)
        opening_bouts = all_opening_bout_numbers[key]

        if not isinstance(html, str):
            raise TypeError("Unexpected value", type(html))

        soup = bs4.BeautifulSoup(html, features="html.parser")
        initial_match_slots = initial_entries(
            soup, division_scores, name_fixes, team_fixes, opening_bouts
        )
        if key in match_slots_by_bracket:
            raise KeyError("Duplicate", key)

        match_slots_by_bracket[key] = initial_match_slots

    matches = parse_rounds(selenium_rounds, match_slots_by_bracket)

    weight_classes: list[bracket_utils.WeightClass] = []
    for key in match_slots_by_bracket:
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

    return bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=deductions
    )
