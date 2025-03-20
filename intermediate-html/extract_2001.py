# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import Literal

import bs4
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
EMPTY_SLOT = "                          "
CHAMPIONSHIP_FIXES: tuple[tuple[str, str], ...] = (
    ("M MCAULIFFE-TP\n", "M MCAULIFFE-TPB\n"),
    ("F BATTAGLIA-HR\n", "F BATTAGLIA-HRD\n"),
    ("MATT WENGER-DA\n", "MATT WENGER-DAK\n"),
    ("M MCNAUGHTON-O\n", "M MCNAUGHTON-OLW\n"),
    ("N FANTHORPE-MF\n", "N FANTHORPE-MFV\n"),
    ("B ZERFOWSKI-MT\n", "B ZERFOWSKI-MTZ\n"),
    ("JON ISACSON-VL\n", "JON ISACSON-VLC\n"),
    ("SCOTT SANDS-TP\n", "SCOTT SANDS-TPB\n"),
    ("A GREENAWALT-N\n", "A GREENAWALT-NE\n"),
)
CONSOLATION_FIXES: tuple[tuple[str, str], ...] = (
    ("VINNY ALBER-DA\n", "VINNY ALBER-DAK\n"),
    ("LUCAS FORCE-AO\n", "LUCAS FORCE-AOK\n"),
    ("STUART JELM-MF\n", "STUART JELM-MFV\n"),
    ("JESUS ORDAZ-CL\n", "JESUS ORDAZ-CLW\n"),
    ("C HIGHTOWER-FV\n", "C HIGHTOWER-FVW\n"),
    ("JASON WHITE-SY\n", "JASON WHITE-SYW\n"),
)


class CompetitorRaw(pydantic.BaseModel):
    name: str
    team: str


def parse_competitor(value: str) -> CompetitorRaw | None:
    cleaned = value.strip().rstrip("+").rstrip("-")
    name, team = cleaned.rsplit("-", 1)

    team = team.strip()

    if name == "" and team == "Bye":
        return None

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return CompetitorRaw(name=name, team=team)


def parse_bout_result(value: str) -> str:
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].strip().rsplit(None, 1)
    if len(parts) == 1:
        int(parts[0])  # Ensure the only part is a valid bout number
        return ""

    return parts[0].strip()


def parse_bout_number(value: str) -> int:
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].strip().rsplit(None, 1)
    if len(parts) == 1:
        return int(parts[0])

    return int(parts[1])


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
        if match.bottom_competitor is not None:
            raise ValueError("Invariant violation", match)
        match.winner = match.top_competitor
        return

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
    top_competitor_str = championship_lines[start_index][:26]
    if top_competitor_str != EMPTY_SLOT:
        top_competitor = parse_competitor(top_competitor_str)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:26]
    if bottom_competitor_str != EMPTY_SLOT:
        bottom_competitor = parse_competitor(bottom_competitor_str)

    result_bout_number_str = championship_lines[start_index + 1][:26]
    result = ""
    bout_number = None
    if result_bout_number_str != EMPTY_SLOT:
        result = parse_bout_result(result_bout_number_str)
        bout_number = parse_bout_number(result_bout_number_str)

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
    ("JEFFERY BYBEE,JR", "CHL"): Competitor(
        first_name="JEFFERY", last_name="BYBEE", suffix="JR", team="CHL"
    ),
    ("JERRY BEMIS III", "OLW"): Competitor(
        first_name="JERRY", last_name="BEMIS", suffix="III", team="OLW"
    ),
    ("MICHAEL J. RYAN", "LIT"): Competitor(
        first_name="MICHAEL J.", last_name="RYAN", suffix=None, team="LIT"
    ),
    ("SHANE FICH TENMUELLER", "DIX"): Competitor(
        first_name="SHANE", last_name="FICH TENMUELLER", suffix=None, team="DIX"
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


class Match(pydantic.BaseModel):
    match: str
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    bout_number: int | None
    top_win: bool | None


def competitor_equal_enough(competitor1: Competitor, competitor2: Competitor) -> bool:
    if competitor1.team != competitor2.team:
        return False

    if competitor1.suffix != competitor2.suffix:
        return False

    if competitor1.last_name != competitor2.last_name:
        return False

    name1 = competitor1.first_name
    name2 = competitor2.first_name
    if name1 == name2:
        return True

    # Names get shortened to first letter in later rounds
    if len(name1) == 1:
        return name2[0] == name1
    if len(name2) == 1:
        return name1[0] == name2

    return False


def ensure_no_name_duplicates(matches: list[Match]) -> None:
    competitors_with_canonical_names: list[Competitor] = []
    for match in matches:
        if not match.match.startswith("championship_r32_"):
            continue

        if match.top_competitor is not None:
            competitors_with_canonical_names.append(match.top_competitor)

        if match.bottom_competitor is not None:
            competitors_with_canonical_names.append(match.bottom_competitor)

    # Update names based on canonical
    for match in matches:
        if match.top_competitor is not None:
            canonical_competitors = [
                canonical
                for canonical in competitors_with_canonical_names
                if competitor_equal_enough(match.top_competitor, canonical)
            ]
            if len(canonical_competitors) != 1:
                raise ValueError(
                    "Invariant violation",
                    match.top_competitor,
                    len(canonical_competitors),
                    canonical_competitors,
                )
            match.top_competitor = canonical_competitors[0]

        if match.bottom_competitor is not None:
            canonical_competitors = [
                canonical
                for canonical in competitors_with_canonical_names
                if competitor_equal_enough(match.bottom_competitor, canonical)
            ]
            if len(canonical_competitors) != 1:
                raise ValueError(
                    "Invariant violation",
                    match.bottom_competitor,
                    len(canonical_competitors),
                    canonical_competitors,
                )
            match.bottom_competitor = canonical_competitors[0]


def competitor_name_equal_enough(name1: str, name2: str) -> bool:
    if name1 == name2:
        return True

    parts1 = name1.split()
    parts2 = name2.split()
    if len(parts1) != len(parts2):
        return False

    if parts1[1:] != parts2[1:]:
        return False

    start1 = parts1[0]
    start2 = parts2[0]
    # Names get shortened to first letter in later rounds
    if len(start1) == 1:
        return start2[0] == start1
    if len(start2) == 1:
        return start1[0] == start2

    return False


def competitor_raw_equal_enough(
    competitor1: CompetitorRaw | None, competitor2: CompetitorRaw | None
) -> bool:
    if competitor1 is None or competitor2 is None:
        return competitor1 == competitor2

    if competitor1.team != competitor2.team:
        return False

    return competitor_name_equal_enough(competitor1.name, competitor2.name)


def clean_raw_matches(matches: list[MatchRaw]) -> list[Match]:
    result: list[Match] = []
    for match in matches:
        top_win = None

        top_competitor = _to_competitor(match.top_competitor)
        bottom_competitor = _to_competitor(match.bottom_competitor)

        if top_competitor is not None and competitor_raw_equal_enough(
            match.winner, match.top_competitor
        ):
            top_win = True

        if bottom_competitor is not None and competitor_raw_equal_enough(
            match.winner, match.bottom_competitor
        ):
            top_win = False

        if top_win is None:
            if bottom_competitor is not None or top_competitor is not None:
                print(match)
                breakpoint()
                raise RuntimeError("Invariant violation")

        result.append(
            Match(
                match=match.match,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=match.result,
                bout_number=match.bout_number,
                top_win=top_win,
            )
        )

    ensure_no_name_duplicates(result)

    return result


def extract_bracket(weight: int, divison: Literal["senior", "novice"]) -> list[Match]:
    filename = f"{weight}.html"
    with open(HERE / "2001" / divison / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre: list[bs4.Tag] = soup.find_all("pre")
    if len(all_pre) != 4:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre, seventh_place_pre = all_pre
    championship_text = championship_pre.text
    consolation_text = consolation_pre.text
    # Address known typo(s)
    for old_value, new_value in CHAMPIONSHIP_FIXES:
        championship_text = championship_text.replace(old_value, new_value)
    for old_value, new_value in CONSOLATION_FIXES:
        consolation_text = consolation_text.replace(old_value, new_value)

    championship_lines = championship_text.lstrip("\n").split("\n")
    consolation_lines = consolation_text.lstrip("\n").split("\n")
    fifth_place_lines = fifth_place_pre.text.lstrip("\n").split("\n")
    seventh_place_lines = seventh_place_pre.text.lstrip("\n").split("\n")

    if divison == "senior" and weight == 84:
        consolation_round3_01_top_competitor = CompetitorRaw(
            name="KEITH WILLIAMS", team="JUN"
        )
    else:
        consolation_round3_01_top_competitor = parse_competitor(
            consolation_lines[4][:26]
        )

    matches = [
        MatchRaw(
            match="championship_r32_01",
            top_competitor=parse_competitor(championship_lines[0][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            2,
            "championship_r32_02",
            "championship_r16_01",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            6,
            "championship_r32_03",
            "championship_r16_02",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_04",
            top_competitor=parse_competitor(championship_lines[10][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        MatchRaw(
            match="championship_r32_05",
            top_competitor=parse_competitor(championship_lines[12][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            14,
            "championship_r32_06",
            "championship_r16_03",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            18,
            "championship_r32_07",
            "championship_r16_04",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_08",
            top_competitor=parse_competitor(championship_lines[22][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        MatchRaw(
            match="championship_r32_09",
            top_competitor=parse_competitor(championship_lines[24][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            26,
            "championship_r32_10",
            "championship_r16_05",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            30,
            "championship_r32_11",
            "championship_r16_06",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_12",
            top_competitor=parse_competitor(championship_lines[34][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        MatchRaw(
            match="championship_r32_13",
            top_competitor=parse_competitor(championship_lines[36][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            38,
            "championship_r32_14",
            "championship_r16_07",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            42,
            "championship_r32_15",
            "championship_r16_08",
            "top_competitor",
        ),
        MatchRaw(
            match="championship_r32_16",
            top_competitor=parse_competitor(championship_lines[46][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        ########################################################################
        MatchRaw(
            match="championship_r16_01",
            top_competitor=parse_competitor(championship_lines[0][26:52]),
            bottom_competitor=parse_competitor(championship_lines[3][26:52]),
            result=parse_bout_result(championship_lines[1][26:52]),
            bout_number=parse_bout_number(championship_lines[1][26:52]),
            winner=None,
            winner_from=("championship_quarter_01", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_02",
            top_competitor=parse_competitor(championship_lines[7][26:52]),
            bottom_competitor=parse_competitor(championship_lines[10][26:52]),
            result=parse_bout_result(championship_lines[9][26:52]),
            bout_number=parse_bout_number(championship_lines[9][26:52]),
            winner=None,
            winner_from=("championship_quarter_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r16_03",
            top_competitor=parse_competitor(championship_lines[12][26:52]),
            bottom_competitor=parse_competitor(championship_lines[15][26:52]),
            result=parse_bout_result(championship_lines[13][26:52]),
            bout_number=parse_bout_number(championship_lines[13][26:52]),
            winner=None,
            winner_from=("championship_quarter_02", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_04",
            top_competitor=parse_competitor(championship_lines[19][26:52]),
            bottom_competitor=parse_competitor(championship_lines[22][26:52]),
            result=parse_bout_result(championship_lines[21][26:52]),
            bout_number=parse_bout_number(championship_lines[21][26:52]),
            winner=None,
            winner_from=("championship_quarter_02", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r16_05",
            top_competitor=parse_competitor(championship_lines[24][26:52]),
            bottom_competitor=parse_competitor(championship_lines[27][26:52]),
            result=parse_bout_result(championship_lines[25][26:52]),
            bout_number=parse_bout_number(championship_lines[25][26:52]),
            winner=None,
            winner_from=("championship_quarter_03", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_06",
            top_competitor=parse_competitor(championship_lines[31][26:52]),
            bottom_competitor=parse_competitor(championship_lines[34][26:52]),
            result=parse_bout_result(championship_lines[33][26:52]),
            bout_number=parse_bout_number(championship_lines[33][26:52]),
            winner=None,
            winner_from=("championship_quarter_03", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r16_07",
            top_competitor=parse_competitor(championship_lines[36][26:52]),
            bottom_competitor=parse_competitor(championship_lines[39][26:52]),
            result=parse_bout_result(championship_lines[37][26:52]),
            bout_number=parse_bout_number(championship_lines[37][26:52]),
            winner=None,
            winner_from=("championship_quarter_04", "top_competitor"),
        ),
        MatchRaw(
            match="championship_r16_08",
            top_competitor=parse_competitor(championship_lines[43][26:52]),
            bottom_competitor=parse_competitor(championship_lines[46][26:52]),
            result=parse_bout_result(championship_lines[45][26:52]),
            bout_number=parse_bout_number(championship_lines[45][26:52]),
            winner=None,
            winner_from=("championship_quarter_04", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="championship_quarter_01",
            top_competitor=parse_competitor(championship_lines[1][52:70]),
            bottom_competitor=parse_competitor(championship_lines[9][52:70]),
            result=parse_bout_result(championship_lines[5][52:70]),
            bout_number=parse_bout_number(championship_lines[5][52:70]),
            winner=None,
            winner_from=("championship_semi_01", "top_competitor"),
        ),
        MatchRaw(
            match="championship_quarter_02",
            top_competitor=parse_competitor(championship_lines[13][52:70]),
            bottom_competitor=parse_competitor(championship_lines[21][52:70]),
            result=parse_bout_result(championship_lines[17][52:70]),
            bout_number=parse_bout_number(championship_lines[17][52:70]),
            winner=None,
            winner_from=("championship_semi_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_quarter_03",
            top_competitor=parse_competitor(championship_lines[25][52:70]),
            bottom_competitor=parse_competitor(championship_lines[33][52:70]),
            result=parse_bout_result(championship_lines[29][52:70]),
            bout_number=parse_bout_number(championship_lines[29][52:70]),
            winner=None,
            winner_from=("championship_semi_02", "top_competitor"),
        ),
        MatchRaw(
            match="championship_quarter_04",
            top_competitor=parse_competitor(championship_lines[37][52:70]),
            bottom_competitor=parse_competitor(championship_lines[45][52:70]),
            result=parse_bout_result(championship_lines[41][52:70]),
            bout_number=parse_bout_number(championship_lines[41][52:70]),
            winner=None,
            winner_from=("championship_semi_02", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="championship_semi_01",
            top_competitor=parse_competitor(championship_lines[5][70:88]),
            bottom_competitor=parse_competitor(championship_lines[17][70:88]),
            result=parse_bout_result(championship_lines[11][70:88]),
            bout_number=parse_bout_number(championship_lines[11][70:88]),
            winner=None,
            winner_from=("championship_first_place", "top_competitor"),
        ),
        MatchRaw(
            match="championship_semi_02",
            top_competitor=parse_competitor(championship_lines[29][70:88]),
            bottom_competitor=parse_competitor(championship_lines[41][70:88]),
            result=parse_bout_result(championship_lines[35][70:88]),
            bout_number=parse_bout_number(championship_lines[35][70:88]),
            winner=None,
            winner_from=("championship_first_place", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="championship_first_place",
            top_competitor=parse_competitor(championship_lines[11][88:106]),
            bottom_competitor=parse_competitor(championship_lines[35][88:106]),
            result=parse_bout_result(championship_lines[23][88:106]),
            bout_number=parse_bout_number(championship_lines[23][88:106]),
            winner=parse_competitor(championship_lines[23][106:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        MatchRaw(
            match="consolation_round3_01",
            top_competitor=consolation_round3_01_top_competitor,
            bottom_competitor=parse_competitor(consolation_lines[6][:26]),
            result=parse_bout_result(consolation_lines[5][:26]),
            bout_number=parse_bout_number(consolation_lines[5][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="consolation_round3_02",
            top_competitor=parse_competitor(consolation_lines[8][:26]),
            bottom_competitor=parse_competitor(consolation_lines[10][:26]),
            result=parse_bout_result(consolation_lines[9][:26]),
            bout_number=parse_bout_number(consolation_lines[9][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_02", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round3_03",
            top_competitor=parse_competitor(consolation_lines[18][:26]),
            bottom_competitor=parse_competitor(consolation_lines[20][:26]),
            result=parse_bout_result(consolation_lines[19][:26]),
            bout_number=parse_bout_number(consolation_lines[19][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_03", "bottom_competitor"),
        ),
        MatchRaw(
            match="consolation_round3_04",
            top_competitor=parse_competitor(consolation_lines[22][:26]),
            bottom_competitor=parse_competitor(consolation_lines[24][:26]),
            result=parse_bout_result(consolation_lines[23][:26]),
            bout_number=parse_bout_number(consolation_lines[23][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_04", "top_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_round4_blood_01",
            top_competitor=parse_competitor(consolation_lines[1][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[5][26:52]),
            result=parse_bout_result(consolation_lines[3][26:52]),
            bout_number=parse_bout_number(consolation_lines[3][26:52]),
            winner=None,
            winner_from=("consolation_round5_01", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round4_blood_02",
            top_competitor=parse_competitor(consolation_lines[9][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[13][26:52]),
            result=parse_bout_result(consolation_lines[11][26:52]),
            bout_number=parse_bout_number(consolation_lines[11][26:52]),
            winner=None,
            winner_from=("consolation_round5_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="consolation_round4_blood_03",
            top_competitor=parse_competitor(consolation_lines[15][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[19][26:52]),
            result=parse_bout_result(consolation_lines[17][26:52]),
            bout_number=parse_bout_number(consolation_lines[17][26:52]),
            winner=None,
            winner_from=("consolation_round5_02", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round4_blood_04",
            top_competitor=parse_competitor(consolation_lines[23][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[27][26:52]),
            result=parse_bout_result(consolation_lines[25][26:52]),
            bout_number=parse_bout_number(consolation_lines[25][26:52]),
            winner=None,
            winner_from=("consolation_round5_02", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_round5_01",
            top_competitor=parse_competitor(consolation_lines[3][52:70]),
            bottom_competitor=parse_competitor(consolation_lines[11][52:70]),
            result=parse_bout_result(consolation_lines[7][52:70]),
            bout_number=parse_bout_number(consolation_lines[7][52:70]),
            winner=None,
            winner_from=("consolation_round6_semi_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="consolation_round5_02",
            top_competitor=parse_competitor(consolation_lines[17][52:70]),
            bottom_competitor=parse_competitor(consolation_lines[25][52:70]),
            result=parse_bout_result(consolation_lines[21][52:70]),
            bout_number=parse_bout_number(consolation_lines[21][52:70]),
            winner=None,
            winner_from=("consolation_round6_semi_02", "top_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_round6_semi_01",
            top_competitor=parse_competitor(consolation_lines[0][70:88]),
            bottom_competitor=parse_competitor(consolation_lines[7][70:88]),
            result=parse_bout_result(consolation_lines[2][70:88]),
            bout_number=parse_bout_number(consolation_lines[2][70:88]),
            winner=None,
            winner_from=("consolation_third_place", "top_competitor"),
        ),
        MatchRaw(
            match="consolation_round6_semi_02",
            top_competitor=parse_competitor(consolation_lines[21][70:88]),
            bottom_competitor=parse_competitor(consolation_lines[28][70:88]),
            result=parse_bout_result(consolation_lines[26][70:88]),
            bout_number=parse_bout_number(consolation_lines[26][70:88]),
            winner=None,
            winner_from=("consolation_third_place", "bottom_competitor"),
        ),
        ########################################################################
        MatchRaw(
            match="consolation_third_place",
            top_competitor=parse_competitor(consolation_lines[2][88:106]),
            bottom_competitor=parse_competitor(consolation_lines[26][88:106]),
            result=parse_bout_result(consolation_lines[14][88:106]),
            bout_number=parse_bout_number(consolation_lines[14][88:106]),
            winner=parse_competitor(consolation_lines[14][106:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        MatchRaw(
            match="consolation_fifth_place",
            top_competitor=parse_competitor(fifth_place_lines[0][52:70]),
            bottom_competitor=parse_competitor(fifth_place_lines[2][52:70]),
            result=parse_bout_result(fifth_place_lines[1][52:70]),
            bout_number=parse_bout_number(fifth_place_lines[1][52:70]),
            winner=parse_competitor(fifth_place_lines[1][70:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        MatchRaw(
            match="consolation_seventh_place",
            top_competitor=parse_competitor(seventh_place_lines[0][:26]),
            bottom_competitor=parse_competitor(seventh_place_lines[2][:26]),
            result=parse_bout_result(seventh_place_lines[1][:26]),
            bout_number=parse_bout_number(seventh_place_lines[1][:26]),
            winner=parse_competitor(seventh_place_lines[1][26:]),
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

    with open(HERE / "extracted.2001.json", "w") as file_obj:
        json.dump(
            [weight_class.model_dump() for weight_class in parsed], file_obj, indent=2
        )
        file_obj.write("\n")


if __name__ == "__main__":
    main()
