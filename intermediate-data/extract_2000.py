# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
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
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "AOK": "A-O KIDS WRESTLING",
    "BAD": "BADGER WRESTLING CLUB",
    "BAT": "BATAVIA PINNERS",
    "BB": "BELVIDERE BANDITS WC",
    "BBW": "BRADLEY-BOURBONNAIS WC",
    "BH": "BISMARCK-HENNING WC",
    "BJH": "BETHALTO / JR. HIGH",
    "BLD": "BELLEVILLE LITTLE DEVILS",
    "CCK": "CHAMPAIGN CHARGER KIDS WRESTLING",
    "CDW": "CHILLI DAWGS WRESTLING CLUB",
    "CHE": "CHENOA MAT CATS",
    "CJT": "CARY JR. TROJAN MATMEN",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "DAK": "DAKOTA WRESTLING CLUB",
    "DH": "DUNDEE HIGHLANDERS",
    "EBK": "EVANSTON BLACK KAT WC",
    "EMP": "EAST MOLINE PANTHER PINNERS",
    "EP": "EDISON PANTHERS",
    "EWC": "EDWARDSVILLE WRESTLING CLUB",
    "FBG": "FREEPORT BOYS AND GIRLS CLUB",
    "FPR": "FRANKLIN PARK RAIDERS",
    "FVW": "FOX VALLEY WRESTLING CLUB",
    "FYW": "FALCON YOUTH WRESTLING CLUB",
    "GJS": "GALESBURG JUNIOR STREAKS",
    "GWC": "GENESEO WC",
    "HAW": "HOOPESTON AREA WRESTLING CLUB",
    "HBJ": "HIGHLAND BULLDOG JR WC",
    "HC": "HARLEM COUGARS",
    "HIL": "HILL TRAILBLAZERS",
    "HON": "HONONEGAH KIDS WRESTLING CLUB",
    "HPL": "HIGHLAND PARK LITTLE GIANTS",
    "HUS": "HUSKIES WRESTLING CLUB",
    "JAC": "JACKSONVILLE WC",
    "JGE": "JR. GOLDEN EAGLES",
    "JRW": "JUNIOR ROCKET WRESTLING",
    "LB": "LEMONT BEARS WRESTLING CLUB",
    "LC": "LITTLE CELTIC WRESTLING CLUB",
    "LKW": "LITCHFIELD KIDS WRESTLING",
    "LLP": "LAKELAND PREDATORS WC",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WRESTLING",
    "LVL": "LAKE VILLA LANCERS",
    "LYW": "LIMESTONE YOUTH ROCKET WC",
    "MAR": "MARENGO WRESTLING CLUB",
    "MAT": "MATTOON YOUTH WRESTLING CLUB",
    "MCY": "MIDWEST CENTRAL YOUTH",
    "ME": "MAINE EAGLES WRESTLING YOUTH PROGRAM",
    "MET": "METAMORA KIDS WRESTLING CLUB",
    "MFV": "MARTINEZ FOX VALLEY ELITE",
    "MON": "MONTEGO WC",
    "MOR": "MORTON YOUTH WRESTLING",
    "MS": "METRO STALLIONS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "NE": "NAPERVILLE EAGLES",
    "OAK": "OAKWOOD WRESTLING CLUB",
    "OC": "OSWEGO COUGARS",
    "OLW": "OAK LAWN P.D. WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSP": "OSWEGO PANTHERS WC",
    "PCW": "PANTHER CUB WRESTLING CLUB",
    "POL": "POLO WRESTLING CLUB",
    "PPW": "PONTIAC PYTHON WRESTLING CLUB",
    "PWC": "PLAINFIELD WRESTLING CLUB",
    "RAM": "RAMS WRESTLING CLUB",
    "RIV": "RIVERBEND WC",
    "RJH": "RIVERDALE JR. HIGH WC",
    "ROC": "ROCHELLE WRESTLING CLUB",
    "ROX": "ROXANA KIDS WRESTLING CLUB",
    "RWC": "ROCKFORD WRESTLING CLUB",
    "SC": "SPRINGFIELD CAPITALS",
    "SHA": "SHARKS WRESTLING CLUB",
    "SHE": "SHERRARD JR. WRESTLING CLUB",
    "SIE": "SOUTHERN ILLINOIS EAGLES",
    "SJO": "SJO YOUTH WRESTLING",
    "SJW": "SHELBYVILLE JUNIOR WRESTLING RAMS",
    "SN": "STERLING NEWMAN JR. COMETS",
    "SSW": "SOUTHSIDE WC",
    "STB": "ST. BEDE'S",
    "STC": "STC WC",
    "SVW": "STILLMAN VALLEY WRESTLING CLUB",
    "SW": "STATELINE WILDCATS",
    "SYW": "SAUKEE YOUTH WRESTLING CLUB",
    "TAZ": "TAZEWELL COUNTY KIDZ WC",
    "TCB": "TRI-CITY BRAVES",
    "TPB": "TINLEY PARK BULLDOGS",
    "TTT": "TIGERTOWN TANGLERS",
    "TWC": "TIGER WRESTLING CLUB",
    "UNI": "UNITY WRESTLING CLUB",
    "VAN": "VANDALIA JR WRESTLING",
    "VC": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGARS",
    "VPY": "VILLA PARK YOUNG WARRIORS",
    "WB": "WHEATON BULLDOGS",
    "WES": "WESTVILLE YOUTH WRESTLING CLUB",
    "WF": "WEST FRANKFORT REDBIRDS",
    "WFL": "WRESTLING FACTORY OF LIBERTYVILLE",
    "WJP": "WASHINGTON JR. PANTHERS",
    "WME": "WHEATON MONROE EAGLES",
    "WWC": "WOLFPAK WRESTLING CLUB",
    "YWC": "YORKVILLE WRESTLING CLUB",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "BJW": "BENTON JR. WRESTLING CLUB",
    "BRO": "BRONCO WRESTLING",
    "DGC": "DOWNERS GROVE COUGARS",
    "DPC": "DURAND-PECATONICA CARNIVORES",
    "EMS": "ERIE MIDDLE SCHOOL WRESTLING CLUB",
    "FAW": "FAIRFIELD ANIMALS WRESTLING CLUB",
    "FWC": "FISHER WRESTLING CLUB",
    "GDW": "GRAPPLIN' DEVILS WRESTLING CLUB",
    "GED": "GLEN ELLYN DUNGEON WRESTLING",
    "GEN": "GENERALS",
    "HJT": "HILLSBORO JR. TOPPERS",
    "HRD": "HINSDALE RED DEVIL WC",
    "IB": "ILLINI BLUFFS WC",
    "JRB": "JR. BEARS WRESTLING CLUB",
    "JRM": "JR. MAROON'S WRESTLING CLUB",
    "LCW": "LAWRENCE COUNTY WC",
    "LSW": "LIL' STORM YOUTH WRESTLING",
    "MK": "MONTICELLO KIDS WC",
    "MKW": "MACOMB KIDS WRESTLING",
    "MMM": "MONTEGO MAT MEN",
    "PR": "PEORIA RAZORBACKS",
    "RCK": "REED-CUSTER KNIGHTS",
    "RFW": "ROCK FALLS WC",
    "SAN": "SANDWICH WC",
    "TAY": "TAYLORVILLE WC",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "BAR": "BARTLETT HAWK WC",
    "BGP": "BOYS & GIRLS CLUB OF PEKIN",
    "CEN": "CENTRALIA WRESTLING CLUB",
    "CW": "CROSSFACE WRESTLING",
    "CYW": "CUMBERLAND YOUTH WC",
    "DEC": "DECATUR WRESTLING CLUB",
    "GEJ": "GLENBARD EAST JR. RAMS",
    "JS2": "JUNIOR STREAKS #2",
    "MTV": "MT. VERNON LIONS / DOMINO'S PIZZA WRESTLING",
    "NAP": "NAPERVILLE WRESTLING CLUB",
    "PIN": "PINCKNEYVILLE JR. PANTHERS",
    "SII": "STC WC II",
    "T1": "TEAM 1",
    "TRI": "TRIAD WRESTLING CLUB",
}


def _get_team_full(acronym: str, division: bracket_utils.Division) -> str:
    if division == "senior":
        division_mapping = SENIOR_TEAM_ACRONYM_MAPPING
    elif division == "novice":
        division_mapping = NOVICE_TEAM_ACRONYM_MAPPING
    else:
        raise NotImplementedError(division)

    if acronym in division_mapping:
        return division_mapping[acronym]

    if acronym not in TEAM_ACRONYM_MAPPING:
        raise KeyError("Unmapped acronym", acronym, division)

    return TEAM_ACRONYM_MAPPING[acronym]


def parse_competitor_full(
    value: str, division: bracket_utils.Division
) -> bracket_utils.CompetitorRaw | None:
    cleaned = value.strip().rstrip("+").rstrip("-")
    name, team = cleaned.rsplit("-", 1)
    team = team.strip()

    if name == "" and team == "Bye":
        return None

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return bracket_utils.CompetitorRaw(
        name=name,
        team_full=_get_team_full(team, division),
        team_acronym=team,
    )


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


def extract_bracket(
    weight: int, division: bracket_utils.Division
) -> list[bracket_utils.Match]:
    filename = f"{weight}.html"
    with open(_HERE / "2000" / division / filename) as file_obj:
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

    parse_competitor = functools.partial(parse_competitor_full, division=division)

    matches = [
        bracket_utils.MatchRaw(
            match_slot="championship_r32_01",
            top_competitor=parse_competitor(championship_lines[0][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_02",
            top_competitor=parse_competitor(championship_lines[2][:26]),
            bottom_competitor=parse_competitor(championship_lines[4][:26]),
            result=parse_bout_result(championship_lines[3][:26]),
            bout_number=parse_bout_number(championship_lines[3][:26]),
            winner=None,
            winner_from=("championship_r16_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_03",
            top_competitor=parse_competitor(championship_lines[6][:26]),
            bottom_competitor=parse_competitor(championship_lines[8][:26]),
            result=parse_bout_result(championship_lines[7][:26]),
            bout_number=parse_bout_number(championship_lines[7][:26]),
            winner=None,
            winner_from=("championship_r16_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_04",
            top_competitor=parse_competitor(championship_lines[10][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_05",
            top_competitor=parse_competitor(championship_lines[12][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_06",
            top_competitor=parse_competitor(championship_lines[14][:26]),
            bottom_competitor=parse_competitor(championship_lines[16][:26]),
            result=parse_bout_result(championship_lines[15][:26]),
            bout_number=parse_bout_number(championship_lines[15][:26]),
            winner=None,
            winner_from=("championship_r16_03", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_07",
            top_competitor=parse_competitor(championship_lines[18][:26]),
            bottom_competitor=parse_competitor(championship_lines[20][:26]),
            result=parse_bout_result(championship_lines[19][:26]),
            bout_number=parse_bout_number(championship_lines[19][:26]),
            winner=None,
            winner_from=("championship_r16_04", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_08",
            top_competitor=parse_competitor(championship_lines[22][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_09",
            top_competitor=parse_competitor(championship_lines[24][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        ###
        bracket_utils.MatchRaw(
            match_slot="championship_r32_10",
            top_competitor=parse_competitor(championship_lines[26][:26]),
            bottom_competitor=parse_competitor(championship_lines[28][:26]),
            result=parse_bout_result(championship_lines[27][:26]),
            bout_number=parse_bout_number(championship_lines[27][:26]),
            winner=None,
            winner_from=("championship_r16_05", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_11",
            top_competitor=parse_competitor(championship_lines[30][:26]),
            bottom_competitor=parse_competitor(championship_lines[32][:26]),
            result=parse_bout_result(championship_lines[31][:26]),
            bout_number=parse_bout_number(championship_lines[31][:26]),
            winner=None,
            winner_from=("championship_r16_06", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_12",
            top_competitor=parse_competitor(championship_lines[34][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_13",
            top_competitor=parse_competitor(championship_lines[36][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_14",
            top_competitor=parse_competitor(championship_lines[38][:26]),
            bottom_competitor=parse_competitor(championship_lines[40][:26]),
            result=parse_bout_result(championship_lines[39][:26]),
            bout_number=parse_bout_number(championship_lines[39][:26]),
            winner=None,
            winner_from=("championship_r16_07", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_15",
            top_competitor=parse_competitor(championship_lines[42][:26]),
            bottom_competitor=parse_competitor(championship_lines[44][:26]),
            result=parse_bout_result(championship_lines[43][:26]),
            bout_number=parse_bout_number(championship_lines[43][:26]),
            winner=None,
            winner_from=("championship_r16_08", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_16",
            top_competitor=parse_competitor(championship_lines[46][26:52]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_r16_01",
            top_competitor=parse_competitor(championship_lines[0][26:52]),
            bottom_competitor=parse_competitor(championship_lines[3][26:52]),
            result=parse_bout_result(championship_lines[1][26:52]),
            bout_number=parse_bout_number(championship_lines[1][26:52]),
            winner=None,
            winner_from=("championship_quarter_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_02",
            top_competitor=parse_competitor(championship_lines[7][26:52]),
            bottom_competitor=parse_competitor(championship_lines[10][26:52]),
            result=parse_bout_result(championship_lines[9][26:52]),
            bout_number=parse_bout_number(championship_lines[9][26:52]),
            winner=None,
            winner_from=("championship_quarter_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_03",
            top_competitor=parse_competitor(championship_lines[12][26:52]),
            bottom_competitor=parse_competitor(championship_lines[15][26:52]),
            result=parse_bout_result(championship_lines[13][26:52]),
            bout_number=parse_bout_number(championship_lines[13][26:52]),
            winner=None,
            winner_from=("championship_quarter_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_04",
            top_competitor=parse_competitor(championship_lines[19][26:52]),
            bottom_competitor=parse_competitor(championship_lines[22][26:52]),
            result=parse_bout_result(championship_lines[21][26:52]),
            bout_number=parse_bout_number(championship_lines[21][26:52]),
            winner=None,
            winner_from=("championship_quarter_02", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_05",
            top_competitor=parse_competitor(championship_lines[24][26:52]),
            bottom_competitor=parse_competitor(championship_lines[27][26:52]),
            result=parse_bout_result(championship_lines[25][26:52]),
            bout_number=parse_bout_number(championship_lines[25][26:52]),
            winner=None,
            winner_from=("championship_quarter_03", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_06",
            top_competitor=parse_competitor(championship_lines[31][26:52]),
            bottom_competitor=parse_competitor(championship_lines[34][26:52]),
            result=parse_bout_result(championship_lines[33][26:52]),
            bout_number=parse_bout_number(championship_lines[33][26:52]),
            winner=None,
            winner_from=("championship_quarter_03", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_07",
            top_competitor=parse_competitor(championship_lines[36][26:52]),
            bottom_competitor=parse_competitor(championship_lines[39][26:52]),
            result=parse_bout_result(championship_lines[37][26:52]),
            bout_number=parse_bout_number(championship_lines[37][26:52]),
            winner=None,
            winner_from=("championship_quarter_04", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_08",
            top_competitor=parse_competitor(championship_lines[43][26:52]),
            bottom_competitor=parse_competitor(championship_lines[46][26:52]),
            result=parse_bout_result(championship_lines[45][26:52]),
            bout_number=parse_bout_number(championship_lines[45][26:52]),
            winner=None,
            winner_from=("championship_quarter_04", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_01",
            top_competitor=parse_competitor(championship_lines[1][52:70]),
            bottom_competitor=parse_competitor(championship_lines[9][52:70]),
            result=parse_bout_result(championship_lines[5][52:70]),
            bout_number=parse_bout_number(championship_lines[5][52:70]),
            winner=None,
            winner_from=("championship_semi_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_02",
            top_competitor=parse_competitor(championship_lines[13][52:70]),
            bottom_competitor=parse_competitor(championship_lines[21][52:70]),
            result=parse_bout_result(championship_lines[17][52:70]),
            bout_number=parse_bout_number(championship_lines[17][52:70]),
            winner=None,
            winner_from=("championship_semi_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_03",
            top_competitor=parse_competitor(championship_lines[25][52:70]),
            bottom_competitor=parse_competitor(championship_lines[33][52:70]),
            result=parse_bout_result(championship_lines[29][52:70]),
            bout_number=parse_bout_number(championship_lines[29][52:70]),
            winner=None,
            winner_from=("championship_semi_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_04",
            top_competitor=parse_competitor(championship_lines[37][52:70]),
            bottom_competitor=parse_competitor(championship_lines[45][52:70]),
            result=parse_bout_result(championship_lines[41][52:70]),
            bout_number=parse_bout_number(championship_lines[41][52:70]),
            winner=None,
            winner_from=("championship_semi_02", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_semi_01",
            top_competitor=parse_competitor(championship_lines[5][70:88]),
            bottom_competitor=parse_competitor(championship_lines[17][70:88]),
            result=parse_bout_result(championship_lines[11][70:88]),
            bout_number=parse_bout_number(championship_lines[11][70:88]),
            winner=None,
            winner_from=("championship_first_place", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_semi_02",
            top_competitor=parse_competitor(championship_lines[29][70:88]),
            bottom_competitor=parse_competitor(championship_lines[41][70:88]),
            result=parse_bout_result(championship_lines[35][70:88]),
            bout_number=parse_bout_number(championship_lines[35][70:88]),
            winner=None,
            winner_from=("championship_first_place", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_first_place",
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
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_01",
            top_competitor=parse_competitor(consolation_lines[4][:26]),
            bottom_competitor=parse_competitor(consolation_lines[6][:26]),
            result=parse_bout_result(consolation_lines[5][:26]),
            bout_number=parse_bout_number(consolation_lines[5][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_02",
            top_competitor=parse_competitor(consolation_lines[8][:26]),
            bottom_competitor=parse_competitor(consolation_lines[10][:26]),
            result=parse_bout_result(consolation_lines[9][:26]),
            bout_number=parse_bout_number(consolation_lines[9][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_03",
            top_competitor=parse_competitor(consolation_lines[18][:26]),
            bottom_competitor=parse_competitor(consolation_lines[20][:26]),
            result=parse_bout_result(consolation_lines[19][:26]),
            bout_number=parse_bout_number(consolation_lines[19][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_03", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_04",
            top_competitor=parse_competitor(consolation_lines[22][:26]),
            bottom_competitor=parse_competitor(consolation_lines[24][:26]),
            result=parse_bout_result(consolation_lines[23][:26]),
            bout_number=parse_bout_number(consolation_lines[23][:26]),
            winner=None,
            winner_from=("consolation_round4_blood_04", "top"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_01",
            top_competitor=parse_competitor(consolation_lines[1][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[5][26:52]),
            result=parse_bout_result(consolation_lines[3][26:52]),
            bout_number=parse_bout_number(consolation_lines[3][26:52]),
            winner=None,
            winner_from=("consolation_round5_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_02",
            top_competitor=parse_competitor(consolation_lines[9][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[13][26:52]),
            result=parse_bout_result(consolation_lines[11][26:52]),
            bout_number=parse_bout_number(consolation_lines[11][26:52]),
            winner=None,
            winner_from=("consolation_round5_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_03",
            top_competitor=parse_competitor(consolation_lines[15][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[19][26:52]),
            result=parse_bout_result(consolation_lines[17][26:52]),
            bout_number=parse_bout_number(consolation_lines[17][26:52]),
            winner=None,
            winner_from=("consolation_round5_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_04",
            top_competitor=parse_competitor(consolation_lines[23][26:52]),
            bottom_competitor=parse_competitor(consolation_lines[27][26:52]),
            result=parse_bout_result(consolation_lines[25][26:52]),
            bout_number=parse_bout_number(consolation_lines[25][26:52]),
            winner=None,
            winner_from=("consolation_round5_02", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round5_01",
            top_competitor=parse_competitor(consolation_lines[3][52:70]),
            bottom_competitor=parse_competitor(consolation_lines[11][52:70]),
            result=parse_bout_result(consolation_lines[7][52:70]),
            bout_number=parse_bout_number(consolation_lines[7][52:70]),
            winner=None,
            winner_from=("consolation_round6_semi_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round5_02",
            top_competitor=parse_competitor(consolation_lines[17][52:70]),
            bottom_competitor=parse_competitor(consolation_lines[25][52:70]),
            result=parse_bout_result(consolation_lines[21][52:70]),
            bout_number=parse_bout_number(consolation_lines[21][52:70]),
            winner=None,
            winner_from=("consolation_round6_semi_02", "top"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round6_semi_01",
            top_competitor=parse_competitor(consolation_lines[0][70:88]),
            bottom_competitor=parse_competitor(consolation_lines[7][70:88]),
            result=parse_bout_result(consolation_lines[2][70:88]),
            bout_number=parse_bout_number(consolation_lines[2][70:88]),
            winner=None,
            winner_from=("consolation_third_place", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round6_semi_02",
            top_competitor=parse_competitor(consolation_lines[21][70:88]),
            bottom_competitor=parse_competitor(consolation_lines[28][70:88]),
            result=parse_bout_result(consolation_lines[26][70:88]),
            bout_number=parse_bout_number(consolation_lines[26][70:88]),
            winner=None,
            winner_from=("consolation_third_place", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_third_place",
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
        bracket_utils.MatchRaw(
            match_slot="consolation_fifth_place",
            top_competitor=parse_competitor(fifth_place_lines[0][52:70]),
            bottom_competitor=parse_competitor(fifth_place_lines[2][52:70]),
            result=parse_bout_result(fifth_place_lines[1][52:70]),
            bout_number=parse_bout_number(fifth_place_lines[1][52:70]),
            winner=parse_competitor(fifth_place_lines[1][70:]),
            winner_from=None,
        ),
    ]

    by_match = {match.match_slot: match for match in matches}
    if len(by_match) != len(matches):
        raise ValueError("Invariant violation")

    for match in matches:
        bracket_utils.set_winner(match, by_match)
        bracket_utils.set_result(match)
        # NOTE: This **MUST** happen after `set_winner()` and `set_result()`
        bracket_utils.set_top_competitor(match)

    return bracket_utils.clean_raw_matches(matches, NAME_EXCEPTIONS)


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

    parsed: list[bracket_utils.WeightClass] = []
    division = "novice"
    for weight in novice_weights:
        matches = extract_bracket(weight, division)
        parsed.append(
            bracket_utils.WeightClass(
                division=division,
                weight=weight,
                matches=matches,
            )
        )

    division = "senior"
    for weight in senior_weights:
        matches = extract_bracket(weight, division)
        parsed.append(
            bracket_utils.WeightClass(
                division=division,
                weight=weight,
                matches=matches,
            )
        )

    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=parsed, team_scores={}, deductions=[]
    )
    extracted_tournament.sort()
    with open(_HERE / "extracted.2000.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
