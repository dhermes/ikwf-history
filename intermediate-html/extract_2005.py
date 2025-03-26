# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import Literal

import bs4
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
EMPTY_SLOT = "                               "


class CompetitorRaw(pydantic.BaseModel):
    name: str
    team: str


def parse_competitor(value: str) -> CompetitorRaw | None:
    cleaned = value.strip().rstrip("+").strip("-")
    if cleaned == "Bye":
        return None

    name, team = cleaned.rsplit(" ", 1)
    team = team.strip()

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return CompetitorRaw(name=name, team=team)


def parse_bout_result(value: str) -> str:
    if value.endswith("|"):
        value = value[:-1]

    # SPECIAL CASES
    if value.startswith("T-Fall "):
        value = f" {value} "

    if not value.endswith(" ") or not value.startswith(" "):
        raise ValueError("Invariant violation", value)

    parts = value.split("Bout:")
    if len(parts) > 2:
        raise ValueError("Invariant violation", value)

    return parts[0].strip()


def to_int_with_commas(value: str) -> int:
    cleaned = value.strip()
    result = int(value.replace(",", ""))

    expected = f"{result:,}"
    if cleaned != expected:
        raise ValueError("Invariant violation", value)

    return result


def parse_bout_number(value: str) -> int:
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].split("Bout:")
    if len(parts) != 2:
        raise ValueError("Invariant violation", value)

    return to_int_with_commas(parts[1])


class MatchRaw(pydantic.BaseModel):
    match: str
    top_competitor: CompetitorRaw | None
    bottom_competitor: CompetitorRaw | None
    result: str
    bout_number: int | None
    winner: CompetitorRaw | None
    winner_from: tuple[str, str] | None


def set_winner(match: MatchRaw, by_match: dict[str, MatchRaw]) -> None:
    if match.winner is not None:
        return

    if match.result == "Bye":
        if match.bottom_competitor is None:
            if match.top_competitor is None:
                match.winner = None
                return

            match.winner = match.top_competitor
            return

        if match.top_competitor is None:
            if match.bottom_competitor is None:
                raise ValueError("Invariant violation", match)
            match.winner = match.bottom_competitor
            return

        raise ValueError("Invariant violation", match)

    if match.winner_from is not None:
        match_key, competitor_key = match.winner_from
        competitor = getattr(by_match[match_key], competitor_key)
        match.winner = competitor
        return

    raise NotImplementedError(match)


def set_result(match: MatchRaw) -> None:
    result = match.result
    if result != "":
        return

    top_competitor = match.top_competitor
    bottom_competitor = match.bottom_competitor
    if top_competitor is None or bottom_competitor is None:
        match.result = "Bye"
        return

    raise NotImplementedError(match)


def set_top_competitor(match: MatchRaw) -> None:
    top_competitor = match.top_competitor
    bottom_competitor = match.bottom_competitor
    if top_competitor is not None or bottom_competitor is not None:
        return

    result = match.result
    if result != "Bye":
        raise ValueError("Invariant violation", match)

    winner = match.winner
    if winner is None:
        return

    if not isinstance(winner, CompetitorRaw):
        raise ValueError("Invariant violation", match)

    match.top_competitor = winner


def maybe_r32_empty_bye(
    championship_lines: list[str],
    start_index: int,
    match: str,
    winner_round: str,
    winner_key: str,
) -> MatchRaw:
    top_competitor = None
    top_competitor_str = championship_lines[start_index][:31]
    if top_competitor_str != EMPTY_SLOT:
        top_competitor = parse_competitor(top_competitor_str)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:31]
    if bottom_competitor_str != EMPTY_SLOT:
        bottom_competitor = parse_competitor(bottom_competitor_str)

    bout_number_str = championship_lines[start_index + 1][:31]
    bout_number = None
    if bout_number_str != EMPTY_SLOT:
        bout_number = parse_bout_number(bout_number_str)

    result_str = championship_lines[start_index + 2][31:62]
    result = ""
    if result_str != EMPTY_SLOT:
        result = parse_bout_result(result_str)

    return MatchRaw(
        match=match,
        top_competitor=top_competitor,
        bottom_competitor=bottom_competitor,
        result=result,
        bout_number=bout_number,
        winner=None,
        winner_from=(winner_round, winner_key),
    )


class Competitor(pydantic.BaseModel):
    first_name: str
    last_name: str
    suffix: str | None
    team: str


NAME_EXCEPTIONS: dict[tuple[str, str], Competitor] = {
    ("ALVIN FOSTER III", "HTW"): Competitor(
        first_name="ALVIN", last_name="FOSTER", suffix="III", team="HTW"
    ),
    ("ANTWYONE BROWN JR.", "RRT"): Competitor(
        first_name="ANTWYONE", last_name="BROWN", suffix="JR", team="RRT"
    ),
    ("CARL FORESIDE JR.", "GLA"): Competitor(
        first_name="CARL", last_name="FORESIDE", suffix="JR", team="GLA"
    ),
    ("CURTIS CRIMS JR.", "CTC"): Competitor(
        first_name="CURTIS", last_name="CRIMS", suffix="JR", team="CTC"
    ),
    ("J. ALEXANDER GONZALEZ", "AJW"): Competitor(
        first_name="J. ALEXANDER", last_name="GONZALEZ", suffix=None, team="AJW"
    ),
    ("MALIK - JABRI TAYLOR", "HTW"): Competitor(
        first_name="MALIK - JABRI", last_name="TAYLOR", suffix=None, team="HTW"
    ),
    ("TYRONE  SALLY JR.", "PRP"): Competitor(
        first_name="TYRONE", last_name="SALLY", suffix="JR", team="PRP"
    ),
}


def _to_competitor(value: CompetitorRaw | None) -> Competitor | None:
    if value is None:
        return None

    exception_key = value.name, value.team
    if exception_key in NAME_EXCEPTIONS:
        return NAME_EXCEPTIONS[exception_key]

    parts = value.name.split()
    if len(parts) != 2:
        raise RuntimeError(value.name, value.team)

    return Competitor(
        first_name=parts[0],
        last_name=parts[1],
        suffix=None,
        team=value.team,
    )


ResultType = Literal[
    "BYE",
    "DECISION",
    "DEFAULT",
    "DISQUALIFICATION",
    "FALL",
    "FORFEIT",
    "MAJOR",
    "TECH",
]


class Match(pydantic.BaseModel):
    match: str
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    result_type: ResultType
    bout_number: int | None
    top_win: bool | None


def ensure_no_name_duplicates(matches: list[Match]) -> None:
    any_competitors: list[Competitor] = []
    first_round_competitors: list[Competitor] = []

    for match in matches:
        is_r32 = match.match.startswith("championship_r32_")
        if match.top_competitor is not None:
            any_competitors.append(match.top_competitor)
            if is_r32:
                first_round_competitors.append(match.top_competitor)

        if match.bottom_competitor is not None:
            any_competitors.append(match.bottom_competitor)
            if is_r32:
                first_round_competitors.append(match.bottom_competitor)

    by_team_any: dict[str, list[Competitor]] = {}
    for competitor in any_competitors:
        existing = by_team_any.setdefault(competitor.team, [])
        if not any(competitor == seen for seen in existing):
            existing.append(competitor)

    by_team_first_round: dict[str, list[Competitor]] = {}
    for competitor in first_round_competitors:
        existing = by_team_first_round.setdefault(competitor.team, [])
        if not any(competitor == seen for seen in existing):
            existing.append(competitor)

    if by_team_any != by_team_first_round:
        raise RuntimeError("Invariant violation")


def determine_result_type(result: str) -> ResultType:
    if result.startswith("Dec "):
        return "DECISION"

    if result.startswith("M-Dec "):
        return "MAJOR"

    if result.startswith("T-Fall "):
        return "TECH"

    if result == "Fall" or result.startswith("Fall "):
        return "FALL"

    if result == "Bye":
        return "BYE"

    if result == "Dflt":
        return "DEFAULT"

    if result == "Dq":
        return "DISQUALIFICATION"

    if result == "Forf":
        return "FORFEIT"

    raise NotImplementedError(result)


def clean_raw_matches(matches: list[MatchRaw]) -> list[Match]:
    result: list[Match] = []
    for match in matches:
        top_win = None

        top_competitor = _to_competitor(match.top_competitor)
        bottom_competitor = _to_competitor(match.bottom_competitor)
        winner = _to_competitor(match.winner)

        if top_competitor is not None and winner == top_competitor:
            top_win = True

        if bottom_competitor is not None and winner == bottom_competitor:
            top_win = False

        if top_win is None:
            if bottom_competitor is not None or top_competitor is not None:
                raise RuntimeError("Invariant violation")

        result.append(
            Match(
                match=match.match,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=match.result,
                result_type=determine_result_type(match.result),
                bout_number=match.bout_number,
                top_win=top_win,
            )
        )

    ensure_no_name_duplicates(result)

    return result


def extract_bracket(weight: int, division: Literal["senior", "novice"]) -> list[Match]:
    filename = f"{weight}.html"
    with open(HERE / "2005" / division / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre: list[bs4.Tag] = soup.find_all("pre")
    if len(all_pre) != 4:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre, seventh_place_pre = all_pre
    championship_text = championship_pre.text

    championship_lines = championship_text.lstrip("\n").split("\n")
    consolation_lines = consolation_pre.text.lstrip("\n").split("\n")
    fifth_place_lines = fifth_place_pre.text.lstrip("\n").split("\n")
    seventh_place_lines = seventh_place_pre.text.lstrip("\n").split("\n")

    matches = [
        MatchRaw(
            match="championship_r32_01",
            top_competitor=parse_competitor(championship_lines[0][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            1,
            "championship_r32_02",
            "championship_r16_01",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            5,
            "championship_r32_03",
            "championship_r16_02",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_04",
            top_competitor=parse_competitor(championship_lines[8][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        MatchRaw(
            match="championship_r32_05",
            top_competitor=parse_competitor(championship_lines[10][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            11,
            "championship_r32_06",
            "championship_r16_03",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            15,
            "championship_r32_07",
            "championship_r16_04",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_08",
            top_competitor=parse_competitor(championship_lines[18][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        MatchRaw(
            match="championship_r32_09",
            top_competitor=parse_competitor(championship_lines[20][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            21,
            "championship_r32_10",
            "championship_r16_05",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            25,
            "championship_r32_11",
            "championship_r16_06",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_12",
            top_competitor=parse_competitor(championship_lines[28][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        MatchRaw(
            match="championship_r32_13",
            top_competitor=parse_competitor(championship_lines[30][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            31,
            "championship_r32_14",
            "championship_r16_07",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            35,
            "championship_r32_15",
            "championship_r16_08",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_16",
            top_competitor=parse_competitor(championship_lines[38][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        ########################################################################
        MatchRaw(
            match="championship_r16_01",
            top_competitor=parse_competitor(championship_lines[0][31:62]),
            bottom_competitor=parse_competitor(championship_lines[2][31:62]),
            result=parse_bout_result(championship_lines[2][62:93]),
            bout_number=parse_bout_number(championship_lines[1][31:62]),
            winner=None,
            winner_from=("championship_quarter_01", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_02",
            top_competitor=parse_competitor(championship_lines[6][31:62]),
            bottom_competitor=parse_competitor(championship_lines[8][31:62]),
            result=parse_bout_result(championship_lines[8][62:93]),
            bout_number=parse_bout_number(championship_lines[7][31:62]),
            winner=None,
            winner_from=("championship_quarter_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r16_03",
            top_competitor=parse_competitor(championship_lines[10][31:62]),
            bottom_competitor=parse_competitor(championship_lines[12][31:62]),
            result=parse_bout_result(championship_lines[12][62:93]),
            bout_number=parse_bout_number(championship_lines[11][31:62]),
            winner=None,
            winner_from=("championship_quarter_02", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_04",
            top_competitor=parse_competitor(championship_lines[16][31:62]),
            bottom_competitor=parse_competitor(championship_lines[18][31:62]),
            result=parse_bout_result(championship_lines[18][62:93]),
            bout_number=parse_bout_number(championship_lines[17][31:62]),
            winner=None,
            winner_from=("championship_quarter_02", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r16_05",
            top_competitor=parse_competitor(championship_lines[20][31:62]),
            bottom_competitor=parse_competitor(championship_lines[22][31:62]),
            result=parse_bout_result(championship_lines[22][62:93]),
            bout_number=parse_bout_number(championship_lines[21][31:62]),
            winner=None,
            winner_from=("championship_quarter_03", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_06",
            top_competitor=parse_competitor(championship_lines[26][31:62]),
            bottom_competitor=parse_competitor(championship_lines[28][31:62]),
            result=parse_bout_result(championship_lines[28][62:93]),
            bout_number=parse_bout_number(championship_lines[27][31:62]),
            winner=None,
            winner_from=("championship_quarter_03", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r16_07",
            top_competitor=parse_competitor(championship_lines[30][31:62]),
            bottom_competitor=parse_competitor(championship_lines[32][31:62]),
            result=parse_bout_result(championship_lines[32][62:93]),
            bout_number=parse_bout_number(championship_lines[31][31:62]),
            winner=None,
            winner_from=("championship_quarter_04", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_08",
            top_competitor=parse_competitor(championship_lines[36][31:62]),
            bottom_competitor=parse_competitor(championship_lines[38][31:62]),
            result=parse_bout_result(championship_lines[38][62:93] + " "),
            bout_number=parse_bout_number(championship_lines[37][31:62]),
            winner=None,
            winner_from=("championship_quarter_04", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="championship_quarter_01",
            top_competitor=parse_competitor(championship_lines[1][62:93]),
            bottom_competitor=parse_competitor(championship_lines[7][62:93]),
            result=parse_bout_result(championship_lines[5][93:124]),
            bout_number=parse_bout_number(championship_lines[4][62:93]),
            winner=None,
            winner_from=("championship_semi_01", "top_competitor"),
        ),
        MatchRaw(
            match="championship_quarter_02",
            top_competitor=parse_competitor(championship_lines[11][62:93]),
            bottom_competitor=parse_competitor(championship_lines[17][62:93]),
            result=parse_bout_result(championship_lines[15][93:124]),
            bout_number=parse_bout_number(championship_lines[14][62:93]),
            winner=None,
            winner_from=("championship_semi_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_quarter_03",
            top_competitor=parse_competitor(championship_lines[21][62:93]),
            bottom_competitor=parse_competitor(championship_lines[27][62:93]),
            result=parse_bout_result(championship_lines[25][93:124]),
            bout_number=parse_bout_number(championship_lines[24][62:93]),
            winner=None,
            winner_from=("championship_semi_02", "top_competitor"),
        ),
        MatchRaw(
            match="championship_quarter_04",
            top_competitor=parse_competitor(championship_lines[31][62:93]),
            bottom_competitor=parse_competitor(championship_lines[37][62:93]),
            result=parse_bout_result(championship_lines[35][93:124] + " "),
            bout_number=parse_bout_number(championship_lines[34][62:93]),
            winner=None,
            winner_from=("championship_semi_02", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="championship_semi_01",
            top_competitor=parse_competitor(championship_lines[4][93:124]),
            bottom_competitor=parse_competitor(championship_lines[14][93:124]),
            result=parse_bout_result(championship_lines[10][124:155]),
            bout_number=parse_bout_number(championship_lines[9][93:124]),
            winner=None,
            winner_from=("championship_first_place", "top_competitor"),
        ),
        MatchRaw(
            match="championship_semi_02",
            top_competitor=parse_competitor(championship_lines[24][93:124]),
            bottom_competitor=parse_competitor(championship_lines[34][93:124]),
            result=parse_bout_result(championship_lines[30][124:155] + " "),
            bout_number=parse_bout_number(championship_lines[29][93:124]),
            winner=None,
            winner_from=("championship_first_place", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="championship_first_place",
            top_competitor=parse_competitor(championship_lines[9][124:155]),
            bottom_competitor=parse_competitor(championship_lines[29][124:155]),
            result=parse_bout_result(championship_lines[21][155:] + " "),
            bout_number=parse_bout_number(championship_lines[19][124:155]),
            winner=parse_competitor(championship_lines[19][155:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        MatchRaw(
            match="consolation_round3_01",
            top_competitor=parse_competitor(consolation_lines[0][:31]),
            bottom_competitor=parse_competitor(consolation_lines[2][:31]),
            result=parse_bout_result(consolation_lines[2][31:62]),
            bout_number=parse_bout_number(consolation_lines[1][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_01", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round3_02",
            top_competitor=parse_competitor(consolation_lines[4][:31]),
            bottom_competitor=parse_competitor(consolation_lines[6][:31]),
            result=parse_bout_result(consolation_lines[6][31:62]),
            bout_number=parse_bout_number(consolation_lines[5][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_02", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round3_03",
            top_competitor=parse_competitor(consolation_lines[8][:31]),
            bottom_competitor=parse_competitor(consolation_lines[10][:31]),
            result=parse_bout_result(consolation_lines[10][31:62]),
            bout_number=parse_bout_number(consolation_lines[9][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_03", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round3_04",
            top_competitor=parse_competitor(consolation_lines[12][:31]),
            bottom_competitor=parse_competitor(consolation_lines[14][:31]),
            result=parse_bout_result(consolation_lines[14][31:62]),
            bout_number=parse_bout_number(consolation_lines[13][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_04", "top_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_round4_blood_01",
            top_competitor=parse_competitor(consolation_lines[1][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[3][31:62]),
            result=parse_bout_result(consolation_lines[3][62:93]),
            bout_number=parse_bout_number(consolation_lines[2][31:62]),
            winner=None,
            winner_from=("consolation_round5_01", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round4_blood_02",
            top_competitor=parse_competitor(consolation_lines[5][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[7][31:62]),
            result=parse_bout_result(consolation_lines[7][62:93]),
            bout_number=parse_bout_number(consolation_lines[6][31:62]),
            winner=None,
            winner_from=("consolation_round5_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="consolation_round4_blood_03",
            top_competitor=parse_competitor(consolation_lines[9][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[11][31:62]),
            result=parse_bout_result(consolation_lines[11][62:93]),
            bout_number=parse_bout_number(consolation_lines[10][31:62]),
            winner=None,
            winner_from=("consolation_round5_02", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round4_blood_04",
            top_competitor=parse_competitor(consolation_lines[13][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[15][31:62]),
            result=parse_bout_result(consolation_lines[15][62:93] + " "),
            bout_number=parse_bout_number(consolation_lines[14][31:62]),
            winner=None,
            winner_from=("consolation_round5_02", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_round5_01",
            top_competitor=parse_competitor(consolation_lines[2][62:93]),
            bottom_competitor=parse_competitor(consolation_lines[6][62:93]),
            result=parse_bout_result(consolation_lines[5][93:124]),
            bout_number=parse_bout_number(consolation_lines[4][62:93]),
            winner=None,
            winner_from=("consolation_round6_semi_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="consolation_round5_02",
            top_competitor=parse_competitor(consolation_lines[10][62:93]),
            bottom_competitor=parse_competitor(consolation_lines[14][62:93]),
            result=parse_bout_result(consolation_lines[13][93:124] + " "),
            bout_number=parse_bout_number(consolation_lines[12][62:93]),
            winner=None,
            winner_from=("consolation_round6_semi_02", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_round6_semi_01",
            top_competitor=parse_competitor(consolation_lines[0][93:124]),
            bottom_competitor=parse_competitor(consolation_lines[4][93:124]),
            result=parse_bout_result(consolation_lines[3][124:155]),
            bout_number=parse_bout_number(consolation_lines[2][93:124]),
            winner=None,
            winner_from=("consolation_third_place", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round6_semi_02",
            top_competitor=parse_competitor(consolation_lines[8][93:124]),
            bottom_competitor=parse_competitor(consolation_lines[12][93:124]),
            result=parse_bout_result(consolation_lines[11][124:155] + " "),
            bout_number=parse_bout_number(consolation_lines[10][93:124]),
            winner=None,
            winner_from=("consolation_third_place", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_third_place",
            top_competitor=parse_competitor(consolation_lines[2][124:155]),
            bottom_competitor=parse_competitor(consolation_lines[10][124:155]),
            result=parse_bout_result(consolation_lines[8][155:] + " "),
            bout_number=parse_bout_number(consolation_lines[6][124:155]),
            winner=parse_competitor(consolation_lines[6][155:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        MatchRaw(
            match="consolation_fifth_place",
            top_competitor=parse_competitor(fifth_place_lines[0][:31]),
            bottom_competitor=parse_competitor(fifth_place_lines[2][:31]),
            result=parse_bout_result(fifth_place_lines[3][31:] + " "),
            bout_number=parse_bout_number(fifth_place_lines[1][:31]),
            winner=parse_competitor(fifth_place_lines[1][31:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        MatchRaw(
            match="consolation_seventh_place",
            top_competitor=parse_competitor(seventh_place_lines[0][31:62]),
            bottom_competitor=parse_competitor(seventh_place_lines[2][31:62]),
            result=parse_bout_result(seventh_place_lines[3][62:] + " "),
            bout_number=parse_bout_number(seventh_place_lines[1][31:62]),
            winner=parse_competitor(seventh_place_lines[1][62:]),
            winner_from=None,
        ),
    ]

    by_match = {match.match: match for match in matches}
    if len(by_match) != len(matches):
        raise ValueError("Invariant violation")

    for match in matches:
        set_winner(match, by_match)
        set_result(match)
        # NOTE: This **MUST** happen after `set_winner()` and `set_result()`
        set_top_competitor(match)

    return clean_raw_matches(matches)


class WeightClass(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    matches: list[Match]


def main():
    novice_weights = (
        62,
        66,
        70,
        74,
        79,
        84,
        89,
        95,
        101,
        108,
        115,
        122,
        130,
        147,
        166,
        215,
    )
    senior_weights = (
        70,
        74,
        79,
        84,
        89,
        95,
        101,
        108,
        115,
        122,
        130,
        138,
        147,
        156,
        166,
        177,
        189,
        215,
        275,
    )

    parsed: list[WeightClass] = []
    division = "novice"
    for weight in novice_weights:
        matches = extract_bracket(weight, division)
        parsed.append(
            WeightClass(
                division=division,
                weight=weight,
                matches=matches,
            )
        )

    division = "senior"
    for weight in senior_weights:
        matches = extract_bracket(weight, division)
        parsed.append(
            WeightClass(
                division=division,
                weight=weight,
                matches=matches,
            )
        )

    with open(HERE / "extracted.2005.json", "w") as file_obj:
        json.dump(
            {
                "weight_classes": [
                    weight_class.model_dump() for weight_class in parsed
                ],
                "team_scores": {},
            },
            file_obj,
            indent=2,
        )
        file_obj.write("\n")


if __name__ == "__main__":
    main()
