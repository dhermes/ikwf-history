# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import Literal

import bs4
import pydantic

HERE = pathlib.Path(__file__).resolve().parent
EMPTY_SLOT = "                          "
CHAMPIONSHIP_FIXES: tuple[tuple[str, str], ...] = (
    ("JON ISACSON-VL\n", "JON ISACSON-VLC\n"),
    ("MATT WENGER-DA\n", "MATT WENGER-DAK\n"),
    ("JASON WHITE-SY\n", "JASON WHITE-SYW\n"),
    ("N FANTHORPE-MF\n", "N FANTHORPE-MFV\n"),
    ("JOSH HARPER-BL\n", "JOSH HARPER-BLD\n"),
    ("RYAN OVERBY-LV\n", "RYAN OVERBY-LVL\n"),
    ("MARK FRIEND-MF\n", "MARK FRIEND-MFV\n"),
    ("MATT COLLUM-MF\n", "MATT COLLUM-MFV\n"),
)
CONSOLATION_FIXES: tuple[tuple[str, str], ...] = (
    ("KYLE HUTTER-TP\n", "KYLE HUTTER-TPB\n"),
    ("J ASCHENBREN-M\n", "J ASCHENBREN-MTZ\n"),
    ("D LATTIMORE-MO\n", "D LATTIMORE-MOR\n"),
    ("L WINTERHALT-D\n", "L WINTERHALT-DAK\n"),
    ("JOSH PULLEN-MT\n", "JOSH PULLEN-MTZ\n"),
    ("TONY DIEPPA-VL\n", "TONY DIEPPA-VLC\n"),
    ("CONOR BEEBE-MF\n", "CONOR BEEBE-MFV\n"),
    ("MICHAEL ORI-HP\n", "MICHAEL ORI-HPL\n"),
    ("M LUKASZEWSK-M\n", "M LUKASZEWSK-MFV\n"),
    ("S DINTELMAN-BL\n", "S DINTELMAN-BLD\n"),
    ("JESUS ORDAZ-CL\n", "JESUS ORDAZ-CLW\n"),
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


class Competitor(pydantic.BaseModel):
    first_name: str
    last_name: str
    suffix: str | None
    team: str


NAME_EXCEPTIONS: dict[tuple[str, str], Competitor] = {}


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


def determine_result_type(result: str) -> ResultType:
    if result == "Dec" or result.startswith("Dec "):
        return "DECISION"

    if result.startswith("MajDec "):
        return "MAJOR"

    if result == "T-Fall" or result.startswith("T-Fall "):
        return "TECH"

    if result == "Fall" or result.startswith("Fall "):
        return "FALL"

    if result == "Bye":
        return "BYE"

    if result == "Dflt" or result.startswith("Dflt "):
        return "DEFAULT"

    raise NotImplementedError(result)


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
                result_type=determine_result_type(match.result),
                bout_number=match.bout_number,
                top_win=top_win,
            )
        )

    ensure_no_name_duplicates(result)

    return result


def extract_bracket(weight: int, divison: Literal["senior", "novice"]) -> list[Match]:
    filename = f"{weight}.html"
    with open(HERE / "2000" / divison / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre: list[bs4.Tag] = soup.find_all("pre")
    if len(all_pre) != 3:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre = all_pre
    championship_text = championship_pre.text
    consolation_text = consolation_pre.text
    # Address known typo(s)
    championship_text = championship_text.replace("Fall 1;40", "Fall 1:40")
    championship_text = championship_text.replace("Fall 3;55", "Fall 3:55")
    championship_text = championship_text.replace("Fall 1;37", "Fall 1:37")
    for old_value, new_value in CHAMPIONSHIP_FIXES:
        championship_text = championship_text.replace(old_value, new_value)
    for old_value, new_value in CONSOLATION_FIXES:
        consolation_text = consolation_text.replace(old_value, new_value)

    championship_lines = championship_text.lstrip("\n").split("\n")
    consolation_lines = consolation_text.lstrip("\n").split("\n")
    fifth_place_lines = fifth_place_pre.text.lstrip("\n").split("\n")

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
        MatchRaw(
            match="championship_r32_02",
            top_competitor=parse_competitor(championship_lines[2][:26]),
            bottom_competitor=parse_competitor(championship_lines[4][:26]),
            result=parse_bout_result(championship_lines[3][:26]),
            bout_number=parse_bout_number(championship_lines[3][:26]),
            winner=None,
            winner_from=("championship_r16_01", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r32_03",
            top_competitor=parse_competitor(championship_lines[6][:26]),
            bottom_competitor=parse_competitor(championship_lines[8][:26]),
            result=parse_bout_result(championship_lines[7][:26]),
            bout_number=parse_bout_number(championship_lines[7][:26]),
            winner=None,
            winner_from=("championship_r16_02", "top_competitor"),
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
        MatchRaw(
            match="championship_r32_06",
            top_competitor=parse_competitor(championship_lines[14][:26]),
            bottom_competitor=parse_competitor(championship_lines[16][:26]),
            result=parse_bout_result(championship_lines[15][:26]),
            bout_number=parse_bout_number(championship_lines[15][:26]),
            winner=None,
            winner_from=("championship_r16_03", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r32_07",
            top_competitor=parse_competitor(championship_lines[18][:26]),
            bottom_competitor=parse_competitor(championship_lines[20][:26]),
            result=parse_bout_result(championship_lines[19][:26]),
            bout_number=parse_bout_number(championship_lines[19][:26]),
            winner=None,
            winner_from=("championship_r16_04", "top_competitor"),
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
        ###
        MatchRaw(
            match="championship_r32_10",
            top_competitor=parse_competitor(championship_lines[26][:26]),
            bottom_competitor=parse_competitor(championship_lines[28][:26]),
            result=parse_bout_result(championship_lines[27][:26]),
            bout_number=parse_bout_number(championship_lines[27][:26]),
            winner=None,
            winner_from=("championship_r16_05", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r32_11",
            top_competitor=parse_competitor(championship_lines[30][:26]),
            bottom_competitor=parse_competitor(championship_lines[32][:26]),
            result=parse_bout_result(championship_lines[31][:26]),
            bout_number=parse_bout_number(championship_lines[31][:26]),
            winner=None,
            winner_from=("championship_r16_06", "top_competitor"),
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
        MatchRaw(
            match="championship_r32_14",
            top_competitor=parse_competitor(championship_lines[38][:26]),
            bottom_competitor=parse_competitor(championship_lines[40][:26]),
            result=parse_bout_result(championship_lines[39][:26]),
            bout_number=parse_bout_number(championship_lines[39][:26]),
            winner=None,
            winner_from=("championship_r16_07", "bottom_competitor"),
        ),
        MatchRaw(
            match="championship_r32_15",
            top_competitor=parse_competitor(championship_lines[42][:26]),
            bottom_competitor=parse_competitor(championship_lines[44][:26]),
            result=parse_bout_result(championship_lines[43][:26]),
            bout_number=parse_bout_number(championship_lines[43][:26]),
            winner=None,
            winner_from=("championship_r16_08", "top_competitor"),
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
            top_competitor=parse_competitor(consolation_lines[4][:26]),
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
    ]

    by_match = {match.match: match for match in matches}
    if len(by_match) != len(matches):
        raise ValueError("Invariant violation")

    for match in matches:
        set_winner(match, by_match)
        set_result(match)

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

    with open(HERE / "extracted.2000.json", "w") as file_obj:
        json.dump(
            [weight_class.model_dump() for weight_class in parsed], file_obj, indent=2
        )
        file_obj.write("\n")


if __name__ == "__main__":
    main()
