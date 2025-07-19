# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "VC": 187.0,
    "MFV": 144.5,
    "OPP": 134.0,
    "BJH": 115.0,
    "TPB": 107.0,
    "FVW": 97.5,
    "DAK": 96.0,
    "HRD": 90.0,
    "ROX": 65.0,
    "MTZ": 63.0,
    "CLW": 61.5,
    "MCY": 57.0,
    "SSW": 57.0,
    "HC": 55.0,
    "WFL": 47.0,
    "MAR": 45.0,
    "MS": 45.0,
    "VAN": 42.5,
    "SN": 42.0,
    "JGE": 41.0,
    "PLW": 37.0,
    "PPW": 36.0,
    "SW": 36.0,
    "CYW": 35.5,
    "AOK": 34.0,
    "POL": 29.5,
    "SJO": 29.0,
    "HJT": 28.0,
    "JAC": 28.0,
    "RWC": 28.0,
    "HUS": 27.0,
    "LC": 27.0,
    "PWC": 27.0,
    "RIV": 27.0,
    "EWC": 26.0,
    "SYW": 25.0,
    "SIE": 25.0,
    "ABC": 23.5,
    "DIX": 23.0,
    "NW": 23.0,
    "JRS": 22.0,
    "OLW": 21.0,
    "BWC": 20.0,
    "EMP": 20.0,
    "RFR": 20.0,
    "ACE": 19.0,
    "BAT": 19.0,
    "GEN": 19.0,
    "GED": 19.0,
    "HON": 18.0,
    "LLP": 17.0,
    "ME": 16.0,
    "MKW": 13.0,
    "WME": 13.0,
    "WWC": 12.0,
    "DH": 11.0,
    "WF": 10.0,
    "PLH": 9.0,
    "GEJ": 8.5,
    "BLD": 8.0,
    "BRO": 8.0,
    "DPC": 8.0,
    "IB": 8.0,
    "MAT": 8.0,
    "MTV": 8.0,
    "OAK": 8.0,
    "RAM": 8.0,
    "UNI": 8.0,
    "EUR": 7.0,
    "TTT": 7.0,
    "BJW": 6.0,
    "HBJ": 6.0,
    "MET": 6.0,
    "MUR": 5.5,
    "OC": 5.0,
    "CHL": 4.0,
    "FYW": 4.0,
    "JFW": 4.0,
    "JRW": 4.0,
    "LIT": 4.0,
    "WAU": 4.0,
    "YWC": 4.0,
    "YOU": 4.0,
    "OSP": 3.5,
    "FPR": 3.0,
    "LPC": 3.0,
    "LB": 3.0,
    "FIS": 2.0,
    "GDW": 2.0,
    "HER": 2.0,
    "HAW": 2.0,
    "JRM": 2.0,
    "AC": 0.0,
    "BAD": 0.0,
    "BB": 0.0,
    "BH": 0.0,
    "CPC": 0.0,
    "CWC": 0.0,
    "CKW": 0.0,
    "CJT": 0.0,
    "CCK": 0.0,
    "CHE": 0.0,
    "CRW": 0.0,
    "GWC": 0.0,
    "JUN": 0.0,
    "LCW": 0.0,
    "LG": 0.0,
    "LIN": 0.0,
    "MEN": 0.0,
    "MOR": 0.0,
    "PCW": 0.0,
    "PON": 0.0,
    "SAV": 0.0,
    "SJW": 0.0,
    "SHE": 0.0,
    "SC": 0.0,
    "SVW": 0.0,
    "TAY": 0.0,
    "TWC": 0.0,
    "VLC": 0.0,
    "WCI": 0.0,
    "WES": 0.0,
    "WAR": -1.0,
    "WJP": -1.0,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "LC": 233.0,
    "MFV": 200.5,
    "VLC": 157.5,
    "VC": 138.5,
    "TPB": 124.0,
    "MTZ": 74.0,
    "DAK": 64.0,
    "WWC": 62.0,
    "SN": 57.0,
    "BAT": 56.5,
    "WFL": 55.5,
    "GWC": 54.5,
    "JGE": 51.0,
    "BB": 49.0,
    "RWC": 47.0,
    "CLW": 44.0,
    "NL": 41.0,
    "LB": 39.0,
    "AOK": 38.0,
    "DH": 37.0,
    "WME": 37.0,
    "MET": 36.0,
    "NE": 36.0,
    "SW": 36.0,
    "EMP": 33.0,
    "HC": 32.0,
    "MOR": 31.0,
    "BJH": 30.0,
    "WB": 29.5,
    "ME": 28.0,
    "BLD": 27.0,
    "BGP": 27.0,
    "RFR": 27.0,
    "GEJ": 26.0,
    "FVW": 25.0,
    "JRW": 25.0,
    "SJO": 25.0,
    "OLW": 24.0,
    "OSP": 23.0,
    "WF": 23.0,
    "WHT": 23.0,
    "CCK": 22.0,
    "MUR": 22.0,
    "EWC": 21.0,
    "HUS": 21.0,
    "ROC": 21.0,
    "HON": 20.0,
    "RJH": 20.0,
    "FVC": 19.5,
    "PCW": 19.0,
    "BRL": 17.0,
    "GJS": 17.0,
    "LIT": 17.0,
    "SYW": 17.0,
    "WES": 17.0,
    "CHL": 16.0,
    "OC": 16.0,
    "CHA": 15.0,
    "BH": 14.0,
    "HAW": 14.0,
    "MAR": 13.0,
    "VPY": 13.0,
    # "WHE": 13.0,
    "BJW": 12.0,
    "FYW": 12.0,
    "HBJ": 12.0,
    "JRK": 12.0,
    "WJP": 12.0,
    "SIE": 11.0,
    "LRB": 10.0,
    "TWC": 9.0,
    "MAT": 8.0,
    "SHE": 8.0,
    "TTT": 8.0,
    "OPP": 7.0,
    "ROX": 7.0,
    "SSW": 5.0,
    "SVW": 5.0,
    "ADA": 4.0,
    "ABC": 4.0,
    "CJT": 4.0,
    "DIX": 4.0,
    "EMS": 4.0,
    "GED": 4.0,
    "LPC": 4.0,
    "LSW": 4.0,
    "MAN": 4.0,
    "OAK": 4.0,
    "RAM": 4.0,
    "RMD": 4.0,
    "RIV": 4.0,
    "SJW": 4.0,
    "WAG": 4.0,
    "CHE": 3.0,
    "EP": 3.0,
    "GDW": 2.0,
    "JAC": 2.0,
    "LCW": 2.0,
    "PLW": 2.0,
    # "WHEATON WC (2)": 2.0,
    "MTV": 1.0,
    "ACE": 0.0,
    # "ADDISON ANIMALS (2)": 0.0,
    "BAD": 0.0,
    # "BWC": 0.0,
    "CEN": 0.0,
    # "CHR": 0.0,
    "CYW": 0.0,
    "DEC": 0.0,
    "DC": 0.0,
    "DW": 0.0,
    "DPC": 0.0,
    # "ERIE MIDDLE SCHOOL W (2)": 0.0,
    "FWC": 0.0,
    "FPR": 0.0,
    "GJ1": 0.0,
    "HJT": 0.0,
    "JFW": 0.0,
    "JRS": 0.0,
    "JUN": 0.0,
    "LJW": 0.0,
    "LVL": 0.0,
    "LLP": 0.0,
    "LYW": 0.0,
    # "MANTENO JR PANTHERS (2)": 0.0,
    # "NAPERVILLE LANCERS (2)": 0.0,
    "NAP": 0.0,
    "PIN": 0.0,
    "PWC": 0.0,
    "PLT": 0.0,
    "PPW": 0.0,
    # "RICHMOND WC (2)": 0.0,
    "SHA": 0.0,
    "SC": 0.0,
    "STB": 0.0,
    "TAY": 0.0,
    "TCB": 0.0,
    "VAN": 0.0,
    "WAB": 0.0,
    "YWC": 0.0,
    "WAR": -1.0,
    "HRD": -2.0,
}
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
        team_full="OAK LAWN P.D. WILDCATS",
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
    ("novice", "WASHINGTON JR PANTHERS"): -1.0,
    ("senior", "HINSDALE RED DEVILS"): -2.0,
}
_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ABC": "ALEDO BEAR COUNTRY WC",
    "ACE": "ACES WRESTLING",
    "AOK": "A-O KIDS WC",
    "BAD": "BADGER WC",
    "BAT": "BATAVIA PINNERS",
    "BB": "BELVIDERE BANDITS",
    "BH": "BISMARCK-HENNING WC",
    "BJH": "BETHALTO JR HIGH",
    "BJW": "BENTON JR. WC",
    "BLD": "BELLEVILLE LITTLE DEVILS",
    "BWC": "BRAWLERS WC",
    "CCK": "CHAMPAIGN CHARGER KIDS",
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLICOTHE WC",
    "CJT": "CARY JR TROJAN MATMEN",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "CYW": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DH": "DUNDEE HIGHLANDERS",
    "DIX": "DIXON WC",
    "DPC": "DURAND-PECATONICA CARNIVORES",
    "EMP": "EAST MOLINE PANTHER PINNERS",
    "EWC": "EDWARDSVILLE WC",
    "FPR": "FRANKLIN PARK RAIDERS",
    "FVW": "FOX VALLEY WC",
    "FYW": "FALCON YOUTH WC",
    "GDW": "GRAPPLIN' DEVILS WC",
    "GED": "GLEN ELLYN DUNGEON WC",
    "GEJ": "GLENBARD EAST JR RAMS",
    "GWC": "GENESEO WC",
    "HAW": "HOOPESTON AREA WC",
    "HBJ": "HIGHLAND BULLDOG JR WC",
    "HC": "HARLEM COUGARS",
    "HJT": "HILLSBORO JR TOPPERS",
    "HON": "HONONEGAH KIDS WC",
    "HRD": "HINSDALE RED DEVIL WC",
    "HUS": "HUSKIES WC",
    "JAC": "JACKSONVILLE WC",
    "JFW": "JACOBS FALCONS",
    "JGE": "JR GOLDEN EAGLES",
    "JRS": "JR SENTINELS",
    "JRW": "JR ROCKET WRESTLING",
    "JUN": "JUNIOR PIRATE WC",
    "LB": "LEMONT BEARS WC",
    "LC": "LITTLE CELTIC WC",
    "LCW": "LAWRENCE COUNTY WC",
    "LG": "LITTLE GIANTS",
    "LIT": "LITTLE BOILER WC",
    "LLP": "LAKELAND PREDATORS",
    "LPC": "L-P CRUNCHING CAVS",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "ME": "MAINE EAGLES WC",
    "MET": "METAMORA KIDS WC",
    "MFV": "MARTINEZ FOX VALLEY ELITE WC",
    "MOR": "MORTON YOUTH WRESTLING",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "OAK": "OAKWOOD WC",
    "OC": "OSWEGO COUGARS",
    "OLW": "OAK LAWN P.D. WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSP": "OSWEGO PANTHERS",
    "PCW": "PANTHER CUB WC",
    "PLW": "PLAINFIELD WOLVES WC",
    "PPW": "PONTIAC PYTHONS",
    "PWC": "PLAINFIELD WC",
    "RAM": "RAMS WC",
    "RFR": "ROCK FALLS RIPPIN ROCKETS",
    "RIV": "RIVERBEND WC",
    "ROX": "ROXANA KIDS WC",
    "RWC": "ROCKFORD WC",
    "SC": "SPRINGFIELD CAPITALS",
    "SHE": "SHERRARD JR WC",
    "SIE": "SOUTHERN ILLINOIS EAGLES",
    "SJO": "SJO YOUTH WRESTLING",
    "SJW": "SHELBYVILLE JUNIOR RAMS WC",
    "SN": "STERLING NEWMAN JR COMETS",
    "SSW": "SOUTHSIDE WC",
    "SVW": "STILLMAN VALLEY WC",
    "SW": "STATELINE WILDCATS",
    "SYW": "SAUKEE YOUTH WC",
    "TAY": "TAYLORVILLE WC",
    "TPB": "TINLEY PARK BULLDOGS",
    "TTT": "TIGERTOWN TANGLERS",
    "TWC": "TIGER WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VC": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGARS",
    "WAR": "WARRENSBURG WC",
    "WES": "WESTVILLE YOUTH WC",
    "WF": "WEST FRANKFORT JR WC",
    "WFL": "WRESTLING FACTORY",
    "WJP": "WASHINGTON JR PANTHERS",
    "WME": "WHEATON MONROE EAGLES",
    "WWC": "WOLFPAK WC",
    "YWC": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
_NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "AC": "ARLINGTON CARDINALS",
    "BRO": "BRONCO WRESTLING",
    "CKW": "CARLINVILLE KIDS WC",
    "CPC": "CAMP POINT CENTRAL",
    "CRW": "CROSSFACE WRESTLING",
    "CWC": "CARBONDALE WC",
    "EUR": "EUREKA KIDS WC",
    "FIS": "FISHER WC",
    "GEN": "GENERALS",
    "HER": "HERRIN WC",
    "IB": "ILLINI BLUFFS WC",
    "JRM": "JR MAROON WC",
    "LIN": "LITTLE INDIANS",
    "MCY": "MIDWEST CENTRAL YOUTH",
    "MEN": "MENDOTA MAT MASTERS",
    "MKW": "MACOMB KIDS WRESTLING",
    "MS": "METRO STALLIONS",
    "NW": "NAPERVILLE WARHAWKS",
    "PLH": "PLAINFIELD HUSKIES WC",
    "POL": "POLO WC",
    "PON": "PONY EXPRESS WC",
    "SAV": "SAVANNA REDHAWKS",
    "UNI": "UNITY WC",
    "WAU": "WAUBONSIE TRAILBLAZERS",
    "WCI": "WEST CHICAGO P.D. WILDCATS",
    "YOU": "YOUNG CHAMPIONS",
}
_SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    # ADA: Duplicate (team name shows up twice in Senior Team Scores)
    "ADA": "ADDISON ANIMALS",
    "BGP": "BOYS & GIRLS CLUB OF PEKIN",
    "BRL": "BRAWLERS WC",
    "CEN": "CENTRALIA WC",
    "CHA": "CHARLESTON WC",
    "CHR": "CHARLESTON WC",  # TODO
    "DC": "DUNDEE HIGHLANDERS-CARPENTERSVILLE",
    "DW": "DUNDEE HIGHLANDERS-WESTFIELD",
    "DEC": "DECATUR WC",
    # EMS: Duplicate (team name shows up twice in Senior Team Scores)
    "EMS": "ERIE MIDDLE SCHOOL WRESTLING CLUB",
    "EP": "EDISON PANTHERS",
    "FVC": "FOX VALLEY CRONE WC",
    "FWC": "FISHER WC",
    "GJ1": "GALESBURG JR STREAKS",
    "GJS": "GALESBURG JR STREAKS #2",
    "JRK": "JUNIOR ROCKS WRESTLING",
    "LJW": "LAKE VIEW JR WILDCATS",
    "LRB": "LITTLE REDBIRD WC",
    "LSW": "LIL' STORM YOUTH WRESTLING",
    "LVL": "LAKE VILLA LANCERS",
    "LYW": "LIMESTONE YOUTH ROCKET WC",
    "MAN": "MANTENO JR PANTHERS",
    "NAP": "NAPERVILLE WC",
    "NE": "NAPERVILLE EAGLES",
    "NL": "NAPERVILLE LANCERS",
    "PIN": "PINCKNEYVILLE JR PANTHERS",
    "PLT": "PLT PROPHETS WC",
    "RJH": "RIVERDALE JR HIGH WC",
    "RMD": "RICHMOND WC",
    "ROC": "ROCHELLE WC",
    "SHA": "SHARKS WC",
    "STB": "ST. BEDE'S",
    "TCB": "TRI-CITY BRAVES",
    "VPY": "VILLA PARK YOUNG WARRIORS",
    "WAB": "WAUBONSIE BULLDOGS",
    "WAG": "WAUBONSIE GRIZZLIES",
    "WB": "WHEATON BULLDOGS",
    "WHC": "WHEATON WC",  # TODO
    "WHE": "WHEATON BULLDOGS",  # TODO
    "WHT": "WHEATON WC",
}


def _get_team_full(acronym: str, division: bracket_utils.Division) -> str:
    if division == "senior":
        division_mapping = _SENIOR_TEAM_ACRONYM_MAPPING
    elif division == "novice":
        division_mapping = _NOVICE_TEAM_ACRONYM_MAPPING
    else:
        raise NotImplementedError(division)

    if acronym in division_mapping:
        return division_mapping[acronym]

    if acronym not in _TEAM_ACRONYM_MAPPING:
        raise KeyError("Unmapped acronym", acronym, division)

    return _TEAM_ACRONYM_MAPPING[acronym]


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
    with open(_HERE / "2001" / division / filename) as file_obj:
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

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["novice"] = []
    for acronym, score in _NOVICE_TEAM_SCORES.items():
        team_name = _get_team_full(acronym, "novice")
        team_scores["novice"].append(
            bracket_utils.TeamScore(team=team_name, acronym=acronym, score=score)
        )

    team_scores["senior"] = []
    for acronym, score in _SENIOR_TEAM_SCORES.items():
        team_name = _get_team_full(acronym, "senior")
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=acronym, score=score)
        )

    deductions = bracket_utils.infer_deductions(team_scores)
    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=parsed, team_scores=team_scores, deductions=deductions
    )
    extracted_tournament.sort()
    with open(_HERE / "extracted.2001.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
