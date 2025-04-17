# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bracket_utils
import bs4

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
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("JEFFERY BYBEE,JR", "CHL"): bracket_utils.Competitor(
        full_name="JEFFERY BYBEE,JR",
        first_name="JEFFERY",
        last_name="BYBEE",
        team_full="CHILLICOTHE WC",
        team_acronym="CHL",
    ),
    ("JERRY BEMIS III", "OLW"): bracket_utils.Competitor(
        full_name="JERRY BEMIS III",
        first_name="JERRY",
        last_name="BEMIS",
        team_full="OAK LAWN PD WILDCATS",
        team_acronym="OLW",
    ),
    ("MICHAEL J. RYAN", "LIT"): bracket_utils.Competitor(
        full_name="MICHAEL J. RYAN",
        first_name="MICHAEL J.",
        last_name="RYAN",
        team_full="LITTLE BOILER WC",
        team_acronym="LIT",
    ),
    ("SHANE FICH TENMUELLER", "DIX"): bracket_utils.Competitor(
        full_name="SHANE FICH TENMUELLER",
        first_name="SHANE",
        last_name="FICHTENMUELLER",
        team_full="DIXON WC",
        team_acronym="DIX",
    ),
}
TEAM_SCORE_EXCEPTIONS: dict[tuple[bracket_utils.Division, str], float] = {
    ("novice", "WARRENSBURG WC"): -1.0,
    ("novice", "WASHINGTON JR PANT"): -1.0,
    ("senior", "HINSDALE RED DEVILS"): -2.0,
}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ABC": "ALEDO BEAR COUNTRY W",
    "ACE": "ACES WRESTLING",
    "AOK": "A-O KIDS WC",
    "BAD": "BADGER WC",
    "BAT": "BATAVIA PINNERS",
    "BB": "BELVIDERE BANDITS",
    "BH": "BISMARK-HENNING WC",
    "BJH": "BETHALTO JR HIGH",
    "BJW": "BENTON JR. WC",
    "BLD": "BELLEVILLE LITTLE DE",
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLICOTHE WC",
    "CJT": "CARY JR TROJAN MATME",
    "CYW": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DH": "DUNDEE HIGHLANDERS",
    "DIX": "DIXON WC",
    "DPC": "DURAND-PECATONICA",
    "EMP": "EAST MOLINE PANTHER",
    "EWC": "EDWARDSVILLE WC",
    "FPR": "FRANKLIN PARK RAIDER",
    "FVW": "FOX VALLEY WC",
    "FYW": "FALCON YOUTH WC",
    "GED": "GLEN ELLYN DUNGEON W",
    "HAW": "HOOPESTON AREA WC",
    "HBJ": "HIGHLAND BULLDOG JR",
    "HC": "HARLEM COUGARS",
    "HJT": "HILLSBORO JR TOPPERS",
    "HON": "HONONEGAH KIDS WC",
    "HUS": "HUSKIES WC",
    "JAC": "JACKSONVILLE WC",
    "JFW": "JACOBS FALCONS",
    "JGE": "JR GOLDEN EAGLES",
    "JRW": "JR ROCKET WRESTLING",
    "LB": "LEMONT BEARS WC",
    "LC": "LITTLE CELTIC WC",
    "LCW": "LAWRENCE COUNTY WC",
    "LIT": "LITTLE BOILER WC",
    "LLP": "LAKELAND PREDATORS",
    "LPC": "L-P CRUNCHING CAVS",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "ME": "MAINE EAGLES WC",
    "MET": "METAMORA KIDS WC",
    "MFV": "MARTINEZ FOX VALLEY",
    "MOR": "MORTON YOUTH WRESTLI",
    "MTV": "MT VERNON LIONS",
    "MTZ": "MT ZION WC",
    "MUR": "MURPHYSBORO WRESTLIN",
    "OAK": "OAKWOOD WC",
    "OC": "OSWEGO COUGARS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSP": "OSWEGO PANTHERS",
    "PCW": "PANTHER CUB WC",
    "PLW": "PLAINFIELD WOLVES WC",
    "PPW": "PONTIAC PYTHONS",
    "PWC": "PLAINFIELD WC",
    "RAM": "RAMS WC",
    "RFR": "ROCK FALLS RIPPIN",
    "RIV": "RIVERBEND WC",
    "ROX": "ROXANA KIDS WC",
    "RWC": "ROCKFORD WC",
    "SC": "SPRINGFIELD CAPTIALS",
    "SHE": "SHERRAND JR WC",
    "SN": "STERLING NEWMAN JR",
    "SSW": "SOUTHSIDE WC",
    "SVW": "STILLMAN VALLEY WC",
    "SW": "STATELINE WILDCATS",
    "SYW": "SAUKEE YOUTH WC",
    "TAY": "TAYLORVILLE WC",
    "TPB": "TINLEY PARK BULLDOGS",
    "TTT": "TIGERTOWN TANGLERS",
    "TWC": "TIGER WC",
    "VAN": "VANDALIA JR WRESTLIN",
    "VC": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGAR",
    "WES": "WESTVILLE YOUTH WC",
    "WF": "WEST FRANKFORT JR WC",
    "WFL": "WRESTLING FACTORY",
    "WME": "WHEATON MONROE EAGLE",
    "WWC": "WOLFPAK WC",
    "YWC": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "AC": "ARLINGTON CARDINALS",
    "BRO": "BRONCO WRESTLING",
    "BWC": "BRAWLERS WC",
    "CCK": "CHAMPAIGN CHARGER KD",
    "CKW": "CARLINVILLE KIDS WC",
    "CLW": "CRYSTAL LAKE WIRZARD",
    "CPC": "CAMP POINT CENTRAL",
    "CWC": "CARBONDALE WC",
    "EUR": "EUREKA KIDS WC",
    "FIS": "FISHER WC",
    "GDW": "GRAPPLIN'DEVILS WC",
    "GEJ": "GLENBARD EST JR RAMS",
    "GEN": "GENERALS",
    "HRD": "HINSDALE RED DEVIL W",
    "IB": "ILLINI BLUFFS WC",
    "JRM": "JR MAROON WC",
    "JRS": "JR SENTINELS",
    "LIN": "LITTLE INDIANS",
    "MCY": "MIDWEST CENTRAL YOUT",
    "MEN": "MENDOTA MAT MASTERS",
    "MKW": "MACOMB KIDS WRESTLIN",
    "MS": "METRO STALLIONS",
    "NW": "NAPERVILLE WARHAWKS",
    "OLW": "OAK LAWN PD WILDCATS",
    "PLH": "PLANIFIELD HUSKIES W",
    "POL": "POLO WC",
    "PON": "PONY EXPRESS WC",
    "SAV": "SAVANNA REDHAWKS",
    "SIE": "SOUTHERN IL EAGLES",
    "SJO": "SHO YOUTH WRESTLING",
    "UNI": "UNITY WRESTLING CLUB",
    "WAR": "WARRENSBURG WC",
    "WAU": "WAUBONSIE TRAILBLAZE",
    "WCI": "WEST CHICAGO PD",
    "YOU": "YOUNG CHAMPIONS",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    # ADA: Duplicate (team name shows up twice in Senior Team Scores)
    "ADA": "ADDISON ANIMALS",
    "BGP": "BOYS & GIRLS CLUB",  # ... of Pekin
    "BRL": "BRAWLERS WC",
    "BWC": "BRAWLERS WC (2)",
    "CCK": "CHAMPAIGN CHARGER KI",
    "CEN": "CENTRALIA WC",
    "CHA": "CHARLESTON WC",
    "CHR": "CHARLESTON WC (2)",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "DC": "DUNDEE CARPETERVILL",
    "DEC": "DECATUR WC",
    # EMS: Duplicate (team name shows up twice in Senior Team Scores)
    "EMS": "ERIE MIDDLE SCHOOL W",
    "EP": "EDISON PANTHERS",
    "FVC": "FOX VALLEY CRONE WC",
    "FWC": "FISHER WC",
    "GDW": "GRAPPLIN DEVILS WC",
    "GEJ": "GLENBARD EAST JR RAM",
    "GJS": "GALESBURG JR STRK 2",
    "GWC": "GENESEO WC",
    "HRD": "HINSDALE RED DEVILS",
    "JRK": "JUNIOR ROCKS WRESTLI",
    "JUN": "JUNIOR PIRATE WC",
    "LJW": "LAKE VIEW JR WILDCAT",
    "LRB": "LITTLE REDBIRD WC",
    "LSW": "LIL STORM YOUTH",
    "LVL": "LAKE VILLA LANCERS",
    "LYW": "LIMESTONE YOUTH ROCK",
    "MAN": "MANTENO JR PANTHERS",
    "NAP": "NAPERVILLE WC",
    "NE": "NAPERVILLE EAGLES",
    "NL": "NAPERVILLE LANCERS",
    "OLW": "OAK LAWN P.D. WILDCA",
    "PIN": "PINCKNEYVILLE JR",
    "PLT": "PLT PROPHETS WC",
    "RJH": "RIVERDALE JR HIGH",
    "RMD": "RICHMOND WC",
    "ROC": "ROCHELLE WC",
    "SHA": "SHARKS WC",
    "SIE": "SOUTHERN ILLINOIS EA",
    "SJO": "SJO YOUTH WRESTLING",
    "SJW": "SHELBYVILLE JUNIOR R",
    "STB": "ST BEDE WC",
    "TCB": "TRI-CITY BRAVES",
    "VPY": "VILLA PARK YOUNG",
    "WAB": "WAUBONSIE BULLDOGS",
    "WAG": "WAUONSIE GRIZZLIES",
    "WB": "WHEATON BULLDOGS",
    "WHC": "WHEATON WC",
    "WHE": "WHEATON BULLDOGS (2)",
    "WHT": "WHEATON WC (2)",
    "WJP": "WASHINGTON JR PANTHE",
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


def maybe_r32_empty_bye(
    championship_lines: list[str],
    start_index: int,
    match_slot: bracket_utils.MatchSlot,
    winner_round: str,
    winner_key: str,
    division: bracket_utils.Division,
) -> bracket_utils.MatchRaw:
    top_competitor = None
    top_competitor_str = championship_lines[start_index][:26]
    if top_competitor_str != EMPTY_SLOT:
        top_competitor = parse_competitor_full(top_competitor_str, division)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:26]
    if bottom_competitor_str != EMPTY_SLOT:
        bottom_competitor = parse_competitor_full(bottom_competitor_str, division)

    result_bout_number_str = championship_lines[start_index + 1][:26]
    result = ""
    bout_number = None
    if result_bout_number_str != EMPTY_SLOT:
        result = parse_bout_result(result_bout_number_str)
        bout_number = parse_bout_number(result_bout_number_str)

    return bracket_utils.MatchRaw(
        match_slot=match_slot,
        top_competitor=top_competitor,
        bottom_competitor=bottom_competitor,
        result=result,
        bout_number=bout_number,
        winner=None,
        winner_from=(winner_round, winner_key),
    )


def extract_bracket(
    weight: int, division: bracket_utils.Division
) -> list[bracket_utils.Match]:
    filename = f"{weight}.html"
    with open(HERE / "2001" / division / filename) as file_obj:
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

    parse_competitor = functools.partial(parse_competitor_full, division=division)

    if division == "senior" and weight == 84:
        consolation_round3_01_top_competitor = bracket_utils.CompetitorRaw(
            name="KEITH WILLIAMS", team_full="JUNIOR PIRATE WC", team_acronym="JUN"
        )
    else:
        consolation_round3_01_top_competitor = parse_competitor(
            consolation_lines[4][:26]
        )

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
        maybe_r32_empty_bye(
            championship_lines,
            2,
            "championship_r32_02",
            "championship_r16_01",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            6,
            "championship_r32_03",
            "championship_r16_02",
            "top",
            division,
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
        maybe_r32_empty_bye(
            championship_lines,
            14,
            "championship_r32_06",
            "championship_r16_03",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            18,
            "championship_r32_07",
            "championship_r16_04",
            "top",
            division,
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
        maybe_r32_empty_bye(
            championship_lines,
            26,
            "championship_r32_10",
            "championship_r16_05",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            30,
            "championship_r32_11",
            "championship_r16_06",
            "top",
            division,
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
        maybe_r32_empty_bye(
            championship_lines,
            38,
            "championship_r32_14",
            "championship_r16_07",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            42,
            "championship_r32_15",
            "championship_r16_08",
            "top",
            division,
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
            top_competitor=consolation_round3_01_top_competitor,
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
        ########################################################################
        # **********************************************************************
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_seventh_place",
            top_competitor=parse_competitor(seventh_place_lines[0][:26]),
            bottom_competitor=parse_competitor(seventh_place_lines[2][:26]),
            result=parse_bout_result(seventh_place_lines[1][:26]),
            bout_number=parse_bout_number(seventh_place_lines[1][:26]),
            winner=parse_competitor(seventh_place_lines[1][26:]),
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

    novice_reverse_acronym = bracket_utils.reverse_acronym_map(
        TEAM_ACRONYM_MAPPING, NOVICE_TEAM_ACRONYM_MAPPING
    )
    senior_reverse_acronym = bracket_utils.reverse_acronym_map(
        TEAM_ACRONYM_MAPPING, SENIOR_TEAM_ACRONYM_MAPPING
    )
    year_str = "2001"
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {
        "novice": bracket_utils.parse_team_scores(
            HERE / year_str, "novice", novice_reverse_acronym, TEAM_SCORE_EXCEPTIONS
        ),
        "senior": bracket_utils.parse_team_scores(
            HERE / year_str, "senior", senior_reverse_acronym, TEAM_SCORE_EXCEPTIONS
        ),
    }

    # Add a **CUSTOM** "missing" negative team score based on the rule that
    # "all team point deductions applied across all divisions"
    team_scores["senior"].append(
        bracket_utils.TeamScore(team="WARRENSBURG WC", acronym="WAR", score=-1.0)
    )

    deductions = bracket_utils.infer_deductions(team_scores)
    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=parsed, team_scores=team_scores, deductions=deductions
    )
    extracted_tournament.sort()
    with open(HERE / "extracted.2001.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
