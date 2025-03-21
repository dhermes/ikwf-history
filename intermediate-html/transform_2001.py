# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ABC": "ALEDO BEAR COUNTRY W",
    "AC": "ARLINGTON CARDINALS",
    "ACE": "ACES WRESTLING",
    "ADA": "ADDISON ANIMALS",  # Duplicate
    "AOK": "A-O KIDS WC",
    "BAT": "BATAVIA PINNERS",
    "BB": "BELVIDERE BANDITS",
    "BGP": "BOYS & GIRLS CLUB",  # ... of Pekin
    "BH": "BISMARK-HENNING WC",
    "BJH": "BETHALTO JR HIGH",
    "BJW": "BENTON JR. WC",
    "BLD": "BELLEVILLE LITTLE DE",
    "BRO": "BRONCO WRESTLING",
    "BWC": "BRAWLERS WC",  # Duplicate
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLICOTHE WC",
    "CHR": "CHARLESTON WC",  # Duplicate
    "CJT": "CARY JR TROJAN MATME",
    "CKW": "CARLINVILLE KIDS WC",
    "CYW": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DH": "DUNDEE HIGHLANDERS",
    "DIX": "DIXON WC",
    "DPC": "DURAND-PECATONICA",
    "EMP": "EAST MOLINE PANTHER",
    "EMS": "ERIE MIDDLE SCHOOL W",  # Duplicate
    "EP": "EDISON PANTHERS",
    "EUR": "EUREKA KIDS WC",
    "EWC": "EDWARDSVILLE WC",
    "FIS": "FISHER WC",
    "FPR": "FRANKLIN PARK RAIDER",
    "FVC": "FOX VALLEY CRONE WC",
    "FVW": "FOX VALLEY WC",
    "FYW": "FALCON YOUTH WC",
    "GED": "GLEN ELLYN DUNGEON W",
    "GEN": "GENERALS",
    "GJS": "GALESBURG JR STRK 2",
    "GWC": "GENESEO WC",
    "HAW": "HOOPESTON AREA WC",
    "HBJ": "HIGHLAND BULLDOG JR",
    "HC": "HARLEM COUGARS",
    "HJT": "HILLSBORO JR TOPPERS",
    "HON": "HONONEGAH KIDS WC",
    "HUS": "HUSKIES WC",
    "IB": "ILLINI BLUFFS WC",
    "JAC": "JACKSONVILLE WC",
    "JFW": "JACOBS FALCONS",
    "JGE": "JR GOLDEN EAGLES",
    "JRK": "JUNIOR ROCKS WRESTLI",
    "JRM": "JR MAROON WC",
    "JRS": "JR SENTINELS",
    "JRW": "JR ROCKET WRESTLING",
    "LB": "LEMONT BEARS WC",
    "LC": "LITTLE CELTIC WC",
    "LCW": "LAWRENCE COUNTY WC",
    "LIT": "LITTLE BOILER WC",
    "LLP": "LAKELAND PREDATORS",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WC",
    "LSW": "LIL STORM YOUTH",
    "LVL": "LAKE VILLA LANCERS",
    "LYW": "LIMESTONE YOUTH ROCK",
    "MAN": "MANTENO JR PANTHERS",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "MCY": "MIDWEST CENTRAL YOUT",
    "ME": "MAINE EAGLES WC",
    "MET": "METAMORA KIDS WC",
    "MFV": "MARTINEZ FOX VALLEY",
    "MKW": "MACOMB KIDS WRESTLIN",
    "MOR": "MORTON YOUTH WRESTLI",
    "MS": "METRO STALLIONS",
    "MTV": "MT VERNON LIONS",
    "MTZ": "MT ZION WC",
    "MUR": "MURPHYSBORO WRESTLIN",
    "NE": "NAPERVILLE EAGLES",
    "NL": "NAPERVILLE LANCERS",
    "NW": "NAPERVILLE WARHAWKS",
    "OAK": "OAKWOOD WC",
    "OC": "OSWEGO COUGARS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSP": "OSWEGO PANTHERS",
    "PCW": "PANTHER CUB WC",
    "PLH": "PLANIFIELD HUSKIES W",
    "PLW": "PLAINFIELD WOLVES WC",
    "POL": "POLO WC",
    "PON": "PONY EXPRESS WC",
    "PPW": "PONTIAC PYTHONS",
    "PWC": "PLAINFIELD WC",
    "RAM": "RAMS WC",
    "RFR": "ROCK FALLS RIPPIN",
    "RIV": "RIVERBEND WC",
    "RJH": "RIVERDALE JR HIGH",
    "RMD": "RICHMOND WC",
    "ROC": "ROCHELLE WC",
    "ROX": "ROXANA KIDS WC",
    "RWC": "ROCKFORD WC",
    "SC": "SPRINGFIELD CAPTIALS",
    "SHE": "SHERRAND JR WC",
    "SJW": "SHELBYVILLE JUNIOR R",
    "SN": "STERLING NEWMAN JR",
    "SSW": "SOUTHSIDE WC",
    "SVW": "STILLMAN VALLEY WC",
    "SW": "STATELINE WILDCATS",
    "SYW": "SAUKEE YOUTH WC",
    "TAY": "TAYLORVILLE WC",
    "TPB": "TINLEY PARK BULLDOGS",
    "TTT": "TIGERTOWN TANGLERS",
    "TWC": "TIGER WC",
    "UNI": "UNITY WRESTLING CLUB",
    "VAN": "VANDALIA JR WRESTLIN",
    "VC": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGAR",
    "VPY": "VILLA PARK YOUNG",
    "WAG": "WAUONSIE GRIZZLIES",
    "WAR": "WARRENSBURG WC",
    "WAU": "WAUBONSIE TRAILBLAZE",
    "WB": "WHEATON BULLDOGS",
    "WCI": "WEST CHICAGO PD",
    "WES": "WESTVILLE YOUTH WC",
    "WF": "WEST FRANKFORT JR WC",
    "WFL": "WRESTLING FACTORY",  # ... of Libertyville
    "WHC": "WHEATON WC",
    "WHE": "WHEATON BULLDOGS",
    "WHT": "WHEATON WC",
    "WJP": "WASHINGTON JR PANTHE",
    "WME": "WHEATON MONROE EAGLE",
    "WWC": "WOLFPAK WC",
    "YOU": "YOUNG CHAMPIONS",
    "YWC": "YORKVILLE WC",
    # NOTE: These are acronyms that show up in `team*.pdf` keys but do not
    #       have athletes in any brackets.
    "ADD": "ADDISON ANIMALS",  # Duplicate (team name shows up twice in Senior Team Scores)
    "BAD": "BADGER WC",  # 0.0 points in both Novice and Senior
    "BRL": "BRAWLERS WC",  # Duplicate (team name shows up twice in Senior Team Scores)
    "CEN": "CENTRALIA WC",  # 0.0 points in Senior
    "CHA": "CHARLESTON WC",  # Duplicate (team name shows up twice in Senior Team Scores)
    "CPC": "CAMP POINT CENTRAL",  # 0.0 points in Novice
    "CW": "CROSSFACE WRESTLING",  # 0.0 points in Novice
    "CWC": "CARBONDALE WC",  # 0.0 points in Novice
    "DC": "DUNDEE CARPETERVILL",  # 0.0 points in Senior
    "DEC": "DECATUR WC",  # 0.0 points in Senior
    "DW": "DUNDEE WESTFIELD",  # 0.0 points in Senior
    "ERI": "ERIE MIDDLE SCHOOL W",  # Duplicate (team name shows up twice in Senior Team Scores)
    "FWC": "FISHER WC",  # 0.0 points in Senior
    "GAL": "GALESBURG JR STREAKS",  # 0.0 points in Senior
    "HER": "HERRIN WC",  # 0.0 points in Novice
    "JUN": "JUNIOR PIRATE WC",  # 0.0 points in both Novice and Senior
    "LG": "LITTLE GIANTS",  # 0.0 points in Novice
    "LIN": "LITTLE INDIANS",  # 0.0 points in Novice
    "LJW": "LAKE VIEW JR WILDCAT",  # 0.0 points in Senior
    "MEN": "MENDOTA MAT MASTERS",  # 0.0 points in Novice
    "NAP": "NAPERVILLE WC",  # 0.0 points in Senior
    "PIN": "PINCKNEYVILLE JR",  # 0.0 points in Senior
    "PLT": "PLT PROPHETS WC",  # 0.0 points in Senior
    "RIC": "RICHMOND WC",  # Duplicate (team name shows up twice in Senior Team Scores)
    "SAV": "SAVANNA REDHAWKS",  # 0.0 points in Novice
    "SHA": "SHARKS WC",  # 0.0 points in Senior
    "STB": "ST BEDE WC",  # 0.0 points in Senior
    "TCB": "TRI-CITY BRAVES",  # 0.0 points in Senior
    "WAB": "WAUBONSIE BULLDOGS",  # 0.0 points in Senior
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING = {
    "CCK": "CHAMPAIGN CHARGER KD",  # Team Name Spelling Differs
    "CLW": "CRYSTAL LAKE WIRZARD",  # Team Name Spelling Differs
    "GDW": "GRAPPLIN'DEVILS WC",  # Team Name Spelling Differs
    "GEJ": "GLENBARD EST JR RAMS",  # Team Name Spelling Differs
    "HRD": "HINSDALE RED DEVIL W",  # Team Name Spelling Differs
    "OLW": "OAK LAWN PD WILDCATS",  # Team Name Spelling Differs
    "SIE": "SOUTHERN IL EAGLES",  # Team Name Spelling Differs
    "SJO": "SHO YOUTH WRESTLING",  # Team Name Spelling Differs
}
SENIOR_TEAM_ACRONYM_MAPPING = {
    "CCK": "CHAMPAIGN CHARGER KI",  # Team Name Spelling Differs
    "CLW": "CRYSTAL LAKE WIZARDS",  # Team Name Spelling Differs
    "GDW": "GRAPPLIN DEVILS WC",  # Team Name Spelling Differs
    "GEJ": "GLENBARD EAST JR RAM",  # Team Name Spelling Differs
    "HRD": "HINSDALE RED DEVILS",  # Team Name Spelling Differs
    "OLW": "OAK LAWN P.D. WILDCA",  # Team Name Spelling Differs
    "SIE": "SOUTHERN ILLINOIS EA",  # Team Name Spelling Differs
    "SJO": "SJO YOUTH WRESTLING",  # Team Name Spelling Differs
}
TEAM_NAME_MAPPING = {
    "A-O KIDS WC": 8,
    "ACES WRESTLING": 3,
    "ADDISON ANIMALS": -10907,  # 10004?
    "ALEDO BEAR COUNTRY W": 10002,
    "ARLINGTON CARDINALS": 9,
    "BADGER WC": 14,
    "BATAVIA PINNERS": 10005,
    "BELLEVILLE LITTLE DE": 23,
    "BELVIDERE BANDITS": 24,
    "BENTON JR. WC": 26,
    "BETHALTO JR HIGH": 10118,
    "BISMARCK-HENNING WC": 28,
    "BISMARK-HENNING WC": 28,
    "BOYS & GIRLS CLUB": 319,
    "BRAWLERS WC": 39,
    "BRONCO WRESTLING": 41,  # Old Montini Feeder (Bukovsky)
    "CAMP POINT CENTRAL": 50,
    "CARBONDALE WC": 53,
    "CARLINVILLE KIDS WC": 54,
    "CARY JR TROJAN MATME": 59,
    "CENTRALIA WC": 64,
    "CHAMPAIGN CHARGER KD": 10124,
    "CHAMPAIGN CHARGER KI": 10124,
    "CHARLESTON WC": 69,
    "CHENOA MAT CATS": 10011,
    "CHILLICOTHE WC": 10014,  # Chilli Dawgs WC
    "CROSSFACE WRESTLING": 10018,
    "CRYSTAL LAKE WIRZARD": 89,
    "CRYSTAL LAKE WIZARDS": 89,
    "CUMBERLAND YOUTH WC": 90,
    "DAKOTA WC": 92,
    "DIXON WC": 98,
    "DUNDEE HIGHLANDERS": 102,
    "DURAND-PECATONICA": -10907,
    "EAST MOLINE PANTHER": 10121,
    "EDISON PANTHERS": 10131,
    "EDWARDSVILLE WC": 110,
    "ERIE MIDDLE SCHOOL W": 10025,
    "EUREKA KIDS WC": 117,
    "FALCON YOUTH WC": 123,
    "FISHER WC": 130,
    "FOX VALLEY CRONE WC": -10907,
    "FOX VALLEY WC": 134,
    "FRANKLIN PARK RAIDER": -10907,  # Leyden
    "GALESBURG JR STREAKS": 10030,
    "GALESBURG JR STRK 2": 10030,
    "GENERALS": -10907,
    "GENESEO WC": 10033,
    "GLEN ELLYN DUNGEON W": 10039,
    "GLENBARD EAST JR RAM": 147,
    "GLENBARD EST JR RAMS": 147,
    "GRAPPLIN DEVILS WC": 153,
    "GRAPPLIN'DEVILS WC": 153,
    "HARLEM COUGARS": 10041,
    "HERRIN WC": 10042,  # 166?
    "HIGHLAND BULLDOG JR": 168,
    "HILLSBORO JR TOPPERS": 170,
    "HINSDALE RED DEVIL W": 171,
    "HINSDALE RED DEVILS": 171,
    "HONONEGAH KIDS WC": 173,
    "HOOPESTON AREA WC": 174,
    "HUSKIES WC": -10907,
    "ILLINI BLUFFS WC": 181,
    "JACKSONVILLE WC": 189,
    "JACOBS FALCONS": -10907,
    "JR GOLDEN EAGLES": 10050,
    "JR MAROON WC": 538,
    "JR ROCKET WRESTLING": 10052,
    "JR SENTINELS": 10054,
    "JUNIOR PIRATE WC": 201,
    "JUNIOR ROCKS WRESTLI": 361,  # Maybe?
    "L-P CRUNCHING CAVS": 241,
    "LAKE VILLA LANCERS": -10907,
    "LAKELAND PREDATORS": 10057,
    "LAWRENCE COUNTY WC": 217,
    "LEMONT BEARS WC": 219,
    "LIL STORM YOUTH": 10060,
    "LIMESTONE YOUTH ROCK": 10061,
    "LITTLE BOILER WC": 232,
    "LITTLE CELTIC WC": 233,
    "LITTLE GIANTS": 641,
    "LITTLE INDIANS": 10063,
    "LITTLE REDBIRD WC": 10065,
    "MACOMB KIDS WRESTLIN": 243,
    "MAINE EAGLES WC": 245,
    "MANTENO JR PANTHERS": 247,
    "MARENGO WC": 248,
    "MARTINEZ FOX VALLEY": 250,
    "MATTOON YOUTH WC": 252,
    "MENDOTA MAT MASTERS": 10072,
    "METAMORA KIDS WC": 262,
    "METRO STALLIONS": -10907,
    "MIDWEST CENTRAL YOUT": 263,
    "MORTON YOUTH WRESTLI": 272,
    "MT VERNON LIONS": 275,
    "MT ZION WC": 276,
    "MURPHYSBORO WRESTLIN": 278,
    "NAPERVILLE EAGLES": -10907,
    "NAPERVILLE LANCERS": -10907,
    "NAPERVILLE WARHAWKS": -10907,
    "NAPERVILLE WC": 281,
    "OAK LAWN P.D. WILDCA": 10075,
    "OAK LAWN PD WILDCATS": 10075,
    "OAKWOOD WC": 299,
    "ORLAND PARK PIONEERS": 306,
    "OSWEGO COUGARS": -10907,
    "OSWEGO PANTHERS": 10076,
    "PANTHER CUB WC": 10079,
    "PINCKNEYVILLE JR": 10122,
    "PLAINFIELD WC": 326,
    "PLAINFIELD WOLVES WC": -10907,
    "PLANIFIELD HUSKIES W": -10907,
    "PLT PROPHETS WC": 10127,
    "POLO WC": 327,
    "PONTIAC PYTHONS": 10082,
    "PONY EXPRESS WC": -10907,
    "RAMS WC": -10907,
    "RICHMOND WC": 350,
    "RIVERBEND WC": 354,
    "RIVERDALE JR HIGH": 536,  # Maybe?
    "ROCHELLE WC": 358,
    "ROCK FALLS RIPPIN": -10907,
    "ROCKFORD WC": 364,
    "ROXANA KIDS WC": 371,
    "SAUKEE YOUTH WC": 376,
    "SAVANNA REDHAWKS": 10089,
    "SHARKS WC": 381,
    "SHELBYVILLE JR RAMS": 382,
    "SHELBYVILLE JUNIOR R": 382,
    "SHERRAND JR WC": 383,
    "SHERRARD JR WC": 383,
    "SHO YOUTH WRESTLING": 402,
    "SJO YOUTH WRESTLING": 402,
    "SOUTHERN IL EAGLES": 10092,
    "SOUTHERN ILLINOIS EA": 10092,
    "SOUTHSIDE WC": -10907,
    "SPRINGFIELD CAPITALS": 397,
    "SPRINGFIELD CAPTIALS": 397,
    "ST BEDE WC": 10095,
    "STATELINE WILDCATS": 10097,
    "STERLING NEWMAN JR": 10098,
    "STILLMAN VALLEY WC": 407,
    "TAYLORVILLE WC": 420,
    "TIGER WC": 10103,
    "TIGERTOWN TANGLERS": 441,
    "TINLEY PARK BULLDOGS": 443,
    "TRI-CITY BRAVES": 10104,
    "UNITY WRESTLING CLUB": 457,
    "VANDALIA JR WRESTLIN": 461,
    "VILLA LOMBARD COUGAR": 10109,
    "VILLA PARK YOUNG": 464,
    "VITTUM CATS": 466,
    "WARRENSBURG WC": 468,
    "WASHINGTON JR PANTHE": 10110,
    "WAUBONSIE TRAILBLAZE": -10907,
    "WAUONSIE GRIZZLIES": -10907,
    "WEST CHICAGO PD": -10907,
    "WEST FRANKFORT JR WC": 478,
    "WESTVILLE YOUTH WC": 482,
    "WHEATON BULLDOGS": 10120,
    "WHEATON MONROE EAGLE": 10114,
    "WHEATON WC": 234,
    "WOLFPAK WC": 490,
    "WRESTLING FACTORY": 10115,
    "YORKVILLE WC": 497,
    "YOUNG CHAMPIONS": 10116,
}


class Competitor(pydantic.BaseModel):
    first_name: str
    last_name: str
    suffix: str | None
    team: str


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


class WeightClass(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    matches: list[Match]


class WeightClasses(pydantic.RootModel[list[WeightClass]]):
    pass


class CompetitorWithWeight(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    competitor: Competitor


def get_advancement_points(match: str, winner: bool) -> float:
    if match == "championship_first_place":
        return 16.0 if winner else 12.0

    if match == "consolation_third_place":
        return 9.0 if winner else 7.0

    if match == "consolation_fifth_place":
        return 5.0 if winner else 3.0

    if match == "consolation_seventh_place":
        return 2.0 if winner else 1.0

    if match.startswith("consolation_"):
        return 1.0 if winner else 0.0

    if match.startswith("championship_"):
        return 2.0 if winner else 0.0

    raise NotImplementedError(match, winner)


def get_result_points(result_type: ResultType) -> float:
    if result_type == "BYE":
        return 0.0

    if result_type == "DECISION":
        return 0.0

    if result_type == "DEFAULT":
        return 2.0

    if result_type == "DISQUALIFICATION":
        return 2.0

    if result_type == "FALL":
        return 2.0

    if result_type == "FORFEIT":
        return 2.0

    if result_type == "MAJOR":
        return 1.0

    if result_type == "TECH":
        return 1.5

    raise NotImplementedError(result_type)


def next_match_for_bye(match: str) -> str | None:
    if match == "championship_r32_01":
        return "championship_r16_01"

    if match == "championship_r32_02":
        return "championship_r16_01"

    if match == "championship_r32_03":
        return "championship_r16_02"

    if match == "championship_r32_04":
        return "championship_r16_02"

    if match == "championship_r32_05":
        return "championship_r16_03"

    if match == "championship_r32_06":
        return "championship_r16_03"

    if match == "championship_r32_07":
        return "championship_r16_04"

    if match == "championship_r32_08":
        return "championship_r16_04"

    if match == "championship_r32_09":
        return "championship_r16_05"

    if match == "championship_r32_10":
        return "championship_r16_05"

    if match == "championship_r32_11":
        return "championship_r16_06"

    if match == "championship_r32_12":
        return "championship_r16_06"

    if match == "championship_r32_13":
        return "championship_r16_07"

    if match == "championship_r32_14":
        return "championship_r16_07"

    if match == "championship_r32_15":
        return "championship_r16_08"

    if match == "championship_r32_16":
        return "championship_r16_08"

    if match == "championship_r16_01":
        return "championship_quarter_01"

    if match == "championship_r16_02":
        return "championship_quarter_01"

    if match == "championship_r16_03":
        return "championship_quarter_02"

    if match == "championship_r16_04":
        return "championship_quarter_02"

    if match == "championship_r16_05":
        return "championship_quarter_03"

    if match == "championship_r16_06":
        return "championship_quarter_03"

    if match == "championship_r16_07":
        return "championship_quarter_04"

    if match == "championship_r16_08":
        return "championship_quarter_04"

    if match == "consolation_round2_01":
        return "consolation_round3_01"

    if match == "consolation_round2_02":
        return "consolation_round3_01"

    if match == "consolation_round2_03":
        return "consolation_round3_02"

    if match == "consolation_round2_04":
        return "consolation_round3_02"

    if match == "consolation_round2_05":
        return "consolation_round3_03"

    if match == "consolation_round2_06":
        return "consolation_round3_03"

    if match == "consolation_round2_07":
        return "consolation_round3_04"

    if match == "consolation_round2_08":
        return "consolation_round3_04"

    if match == "championship_quarter_01":
        return "championship_semi_01"

    if match == "championship_quarter_02":
        return "championship_semi_01"

    if match == "championship_quarter_03":
        return "championship_semi_02"

    if match == "championship_quarter_04":
        return "championship_semi_02"

    if match == "consolation_round3_01":
        return "consolation_round4_blood_01"

    if match == "consolation_round3_02":
        return "consolation_round4_blood_02"

    if match == "consolation_round3_03":
        return "consolation_round4_blood_03"

    if match == "consolation_round3_04":
        return "consolation_round4_blood_04"

    if match == "consolation_round4_blood_01":
        return "consolation_round5_01"

    if match == "consolation_round4_blood_02":
        return "consolation_round5_01"

    if match == "consolation_round4_blood_03":
        return "consolation_round5_02"

    if match == "consolation_round4_blood_04":
        return "consolation_round5_02"

    if match == "championship_semi_01":
        return "championship_first_place"

    if match == "championship_semi_02":
        return "championship_first_place"

    if match == "consolation_round5_01":
        return "consolation_round6_semi_01"

    if match == "consolation_round5_02":
        return "consolation_round6_semi_02"

    if match == "consolation_round6_semi_01":
        return "consolation_third_place"

    if match == "consolation_round6_semi_02":
        return "consolation_third_place"

    if match == "consolation_seventh_place":
        return None

    if match == "consolation_fifth_place":
        return None

    if match == "consolation_third_place":
        return None

    if match == "championship_first_place":
        return None

    raise NotImplementedError(match)


def bye_next_match_points(
    match: str, winner: Competitor | None, by_match: dict[str, Match]
) -> float:
    next_match_str = next_match_for_bye(match)
    if next_match_str is None:
        return 0.0

    next_match = by_match[next_match_str]
    next_winner = next_match.bottom_competitor
    if next_match.top_win:
        next_winner = next_match.top_competitor

    if winner is None or next_winner is None or winner != next_winner:
        return 0.0

    if next_match.result_type == "BYE":
        # No support (yet) for multiple consecutive byes
        return 0.0

    advancement_points = get_advancement_points(next_match.match, True)
    result_points = get_result_points(next_match.result_type)
    return advancement_points + result_points


def match_team_score_updates(
    match: Match, by_match: dict[str, Match]
) -> dict[str, float]:
    result: dict[str, float] = {}

    loser_team = None
    if match.top_win:
        winner = match.top_competitor
        winner_team = match.top_competitor.team
        if match.bottom_competitor is not None:
            loser_team = match.bottom_competitor.team
    else:
        winner = match.bottom_competitor
        winner_team = match.bottom_competitor.team
        if match.top_competitor is not None:
            loser_team = match.top_competitor.team

    winner_advancement_points = get_advancement_points(match.match, True)
    loser_advancement_points = get_advancement_points(match.match, False)
    winner_result_points = get_result_points(match.result_type)

    winner_points = winner_advancement_points + winner_result_points
    loser_points = loser_advancement_points

    if match.result_type == "BYE":
        winner_points = bye_next_match_points(match.match, winner, by_match)

    result[winner_team] = winner_points

    if loser_points > 0:
        if loser_team is None:
            raise RuntimeError("Invariant violation")
        result[loser_team] = loser_points

    return result


def weight_team_score_updates(weight_class: WeightClass) -> dict[str, float]:
    result: dict[str, float] = {}
    by_match: dict[str, Match] = {match.match: match for match in weight_class.matches}
    for match in weight_class.matches:
        if match.top_win is None:
            continue

        match_updates = match_team_score_updates(match, by_match)
        for acronym, score in match_updates.items():
            result.setdefault(acronym, 0.0)
            result[acronym] += score

    return result


def compute_team_scores(weight_classes: list[WeightClass]) -> dict[str, float]:
    result: dict[str, float] = {}
    for weight_class in weight_classes:
        weight_updates = weight_team_score_updates(weight_class)
        for acronym, score in weight_updates.items():
            result.setdefault(acronym, 0.0)
            result[acronym] += score

    return result


def _team_score_sort_reverse(value: tuple[str, float]) -> tuple[float, str]:
    acronym, score = value
    return -score, acronym


def print_team_scores(team_scores: dict[str, float]) -> None:
    sorted_scores = sorted(team_scores.items(), key=_team_score_sort_reverse)
    for acronym, score in sorted_scores:
        print(f"  {acronym}: {score}")


def main():
    with open(HERE / "extracted.2001.json") as file_obj:
        extracted = WeightClasses.model_validate_json(file_obj.read())

    weight_classes = extracted.root
    novice_weight_classes = [
        weight_class
        for weight_class in weight_classes
        if weight_class.division == "novice"
    ]
    novice_team_scores = compute_team_scores(novice_weight_classes)
    print("Novice:")
    print_team_scores(novice_team_scores)

    print("**************************************************")

    senior_weight_classes = [
        weight_class
        for weight_class in weight_classes
        if weight_class.division == "senior"
    ]
    senior_team_scores = compute_team_scores(senior_weight_classes)
    print("Senior:")
    print_team_scores(senior_team_scores)


if __name__ == "__main__":
    main()
