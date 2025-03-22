# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ACE": "ACES WC",  # Absent from Senior team scores
    "AGO": "ARGENTA/OREANA KIDS CLUB",
    "AJP": "ALLEMAN JR PIONEERS",
    "ARL": "ARLINGTON CARDINALS",
    "BB": "BETHALTO BULLS WC",
    "BELV": "BELVIDERE BANDITS",
    "BEN": "BENTON JR WC",
    "BHK": "BLACKHAWK WC",
    "BIS": "BISON WC",
    "BLD": "BELLEVILLE LITTLE DEVILS",
    "BLM": "BLOOMINGTON RAIDER WC",
    "BMH": "BISMARCK HENNING WRESTLING CLUB",
    "CARY": "CARY JR TROJAN MATMEN",
    "CCR": "CHICAGO CRUSADERS",
    "CENT": "CENTRAL WRESTLING CLUB",
    "CHAR": "CHARLESTON WC",  # Absent from Senior team scores
    "CKW": "CHAMPAIGN KIDS WRESTLING",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "CMB": "CUMBERLAND YOUTH WC",
    "CMW": "CALUMET MEMORIAL PD WOLVERINES",
    "COL": "COLLINSVILLE RAIDERS",
    "CRB": "CARBONDALE WC",  # Absent from Senior team scores
    "CRST": "CROSSTOWN CRUSHERS",
    "DAK": "DAKOTA WC",
    "DGC": "DOWNERS GROVE COUGARS",
    "DIX": "DIXON WC",
    "DUN": "DUNDEE HIGHLANDERS",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM JUNIOR WRESTLING TEAM",  # Absent from Senior team scores
    "ELM": "ELMHURST JR. DUKES",
    "EPG": "EL PASO/GRIDLEY WC",
    "ERIE": "ERIE MIDDLE SCHOOL WC",
    "FEN": "FENWICK FALCONS WC",
    "FISH": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "FRR": "FAIRMONT ROUGH RIDERS",
    "FTT": "FIGHTIN TITAN WC",
    "FWC": "FALCON WRESTLING CLUB",
    "FYW": "FALCON YOUTH WC",  # Absent from Senior team scores
    "GCW": "GC JR WARRIORS",
    "GE": "GOLDEN EAGLES",
    "GEJR": "GLENBARD EAST JR RAMS",
    "GEN": "GENESEO SPIDER WC",
    "GLD": "GLADIATORS",
    "GOM": "GOMEZ WRESTLING ACADEMY",
    "GPD": "GRAPPLIN' DEVILS WRESTLING CLUB",
    "HBD": "HIGHLAND BULLDOG JR WC",
    "HBG": "HIGHLAND BULLDOG JR WC",
    "HCX": "HECOX TEAM BENAIAH",
    "HILL": "HILLTOPPERS WC",
    "HOF": "HOFFMAN ESTATES WC",
    "HON": "HONONEGAH KIDS WC",
    "HPDT": "HARVEY PARK DIST TWISTERS",
    "HPLG": "HIGHLAND PARK LITTLE GIANTS",
    "HPN": "HOOPESTON AREA WC",
    "HRD": "HINSDALE RED DEVIL WC",
    "HRL": "HARLEM COUGARS",
    "HRR": "HERRIN JUNIOR WC",
    "IRN": "IRON MAN",
    "JJS": "JOLIET JUNIOR STEELMEN",
    "JRG": "JUNIOR GATORS WC",
    "JRV": "JUNIOR VIKINGS",
    "KNGT": "KNIGHTS WRESTLING",
    "LEM": "LEMONT BEARS WC",
    "LIM": "LIMESTONE YOUTH WC",
    "LIW": "LIONHEART INTENSE WRESTLING",
    "LJP": "LOCKPORT JR PORTERS WC",
    "LKP": "LAKELAND PREDATORS",
    "LLC": "LITTLE CELTIC WC",
    "LLF": "LITTLE FALCONS WC",
    "LLH": "LITTLE HUSKIE WC",
    "LLRB": "LITTLE REDBIRD WC",
    "LPC": "L-P CRUNCHING CAVS",
    "LWW": "LINCOLN-WAY WC",
    "MCC": "MCLEAN COUNTY WC",  # Absent from Senior team scores
    "MDWA": "MAD DOG WRESTLING ACADEMY",
    "MEN": "MENDOTA WC",  # Absent from Senior team scores
    "MFV": "MARTINEZ FOX VALLEY ELITE",
    "MIN": "MINOOKA LITTLE INDIANS",
    "MIY": "MARENGO INDIANS YOUTH WRESTLING",
    "MLM": "MORTON LITTLE MUSTANGS",
    "MNE": "MAINE EAGLES WC",
    "MOL": "MOLINE WC",
    "MRS": "MORRISON STALLIONS WC",
    "MST": "MUSTANG WC",
    "MTP": "MT. PULASKI WC",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "MWC": "MIDWEST CENTRAL YOUTH",
    "MYW": "MORTON YOUTH WRESTLING",
    "NAP": "NAPERVILLE WC",
    "NDW": "NOTRE DAME WRESTLING",
    "OFW": "OAK FOREST WARRIORS",
    "OKW": "OAKWOOD WC",
    "OLP": "O'FALLON LITTLE PANTHERS",
    "OLW": "OAK LAWN P.D. WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTHERS",  # Absent from Senior team scores
    "PCCH": "PRAIRIE CENTRAL-CHENOA HAWKS",
    "PCUB": "PANTHER CUB WRESTLING CLUB",
    "PLNF": "PLAINFIELD WC",
    "PNP": "PANTHER POWERHOUSE WC",
    "PNRD": "PANTHER/REDHAWK WC",
    "POLO": "POLO WC",
    "PON": "PONTIAC PYTHONS",
    "PRY": "PEORIA RAZORBACKS YOUTH WC",
    "PVP": "PROVISO POWERHOUSE WC",
    "QUI": "QUINCY WC",
    "RCH": "RICHMOND WRESTLING CLUB",
    "RCK": "REED CUSTER KNIGHTS",  # Absent from Senior team scores
    "RJR": "RIVERDALE JR. RAMS WC",
    "RKFD": "ROCKFORD WC",  # Absent from Senior team scores
    "RKI": "ROCK ISLAND WC",
    "ROC": "ROCHESTER WC",
    "ROM": "ROMEOVILLE WC",
    "RRT": "RICH RATTLERS WC",
    "RVB": "RIVERBEND WC",
    "SAU": "SAUKEE YOUTH WC",
    "SCE": "ST. CHARLES EAST WC",
    "SCN": "SCN YOUTH WC",
    "SEN": "SENECA IRISH CADETS",
    "SHM": "SHAMROCK WC",
    "SJO": "SJO SPARTAN YOUTH WC",
    "SKV": "SAUK VALLEY WRESTLING CLUB",  # Absent from Senior team scores
    "SLB": "SHELBYVILLE JR RAMS WRESTLING",
    "SOT": "SONS OF THUNDER",
    "SPI": "SPIDER WC",
    "SPR": "SPRINGFIELD CAPITAL KIDS WRESTLING",
    "SV": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE WC",
    "TAY": "TAYLORVILLE WC",
    "TIG": "TIGER WC",
    "TLK": "TRIAD LITTLE KNIGHTS",
    "TOM": "TOMCAT WC",
    "TPB": "TINLEY PARK BULLDOGS",
    "TRI": "TRI-VALLEY WC",  # Absent from Senior team scores
    "TRV": "TREVIAN WC",
    "TTT": "TIGERTOWN TANGLERS",  # Absent from Senior team scores
    "TWW": "TEAM WEST WOLVES",
    "UNI": "UNITY WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VER": "VERMILION VALLEY ELITE",
    "VIT": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGARS",
    "VPYW": "VILLA PARK YOUNG WARRIORS",
    "WAR": "WARRENSBURG WC",
    "WAS": "WASHINGTON JR PANTHERS",
    "WES": "WESTVILLE YOUTH WC",  # Absent from Senior team scores
    "WHT": "WEST HANCOCK WC",  # Absent from Senior team scores
    "WLP": "WOLFPAK WC",
    "WRF": "WRESTLING FACTORY",
    "WTG": "WHEATON TIGER WC",
    "XTR": "XTREME WRESTLING",
    "YKV": "YORKVILLE WRESTLING CLUB",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING = {
    "BAT": "BATAVIA",
}
SENIOR_TEAM_ACRONYM_MAPPING = {
    "BAT": "BATAVIA PINNERS",
}
TEAM_NAME_MAPPING = {
    "ACES WC": -90501,
    "ALLEMAN JR PIONEERS": -90501,
    "ARGENTA/OREANA KIDS CLUB": -90501,
    "ARLINGTON CARDINALS": -90501,
    "BATAVIA PINNERS": -90501,
    "BATAVIA": -90501,
    "BELLEVILLE LITTLE DEVILS": -90501,
    "BELVIDERE BANDITS": -90501,
    "BENTON JR WC": -90501,
    "BETHALTO BULLS WC": -90501,
    "BISMARCK HENNING WRESTLING CLUB": -90501,
    "BISON WC": -90501,
    "BLACKHAWK WC": -90501,
    "BLOOMINGTON RAIDER WC": -90501,
    "CALUMET MEMORIAL PD WOLVERINES": -90501,
    "CARBONDALE WC": -90501,
    "CARY JR TROJAN MATMEN": -90501,
    "CENTRAL WRESTLING CLUB": -90501,
    "CHAMPAIGN KIDS WRESTLING": -90501,
    "CHARLESTON WC": -90501,
    "CHICAGO CRUSADERS": -90501,
    "COLLINSVILLE RAIDERS": -90501,
    "CROSSTOWN CRUSHERS": -90501,
    "CRYSTAL LAKE WIZARDS": -90501,
    "CUMBERLAND YOUTH WC": -90501,
    "DAKOTA WC": -90501,
    "DIXON WC": -90501,
    "DOWNERS GROVE COUGARS": -90501,
    "DUNDEE HIGHLANDERS": -90501,
    "EDWARDSVILLE WC": -90501,
    "EFFINGHAM JUNIOR WRESTLING TEAM": -90501,
    "EL PASO/GRIDLEY WC": -90501,
    "ELMHURST JR. DUKES": -90501,
    "ERIE MIDDLE SCHOOL WC": -90501,
    "FAIRMONT ROUGH RIDERS": -90501,
    "FALCON WRESTLING CLUB": -90501,
    "FALCON YOUTH WC": -90501,
    "FENWICK FALCONS WC": -90501,
    "FIGHTIN TITAN WC": -90501,
    "FISHER WC": -90501,
    "FOX VALLEY WC": -90501,
    "GC JR WARRIORS": -90501,
    "GENESEO SPIDER WC": -90501,
    "GLADIATORS": -90501,
    "GLENBARD EAST JR RAMS": -90501,
    "GOLDEN EAGLES": -90501,
    "GOMEZ WRESTLING ACADEMY": -90501,
    "GRAPPLIN' DEVILS WRESTLING CLUB": -90501,
    "HARLEM COUGARS": -90501,
    "HARVEY PARK DIST TWISTERS": -90501,
    "HECOX TEAM BENAIAH": -90501,
    "HERRIN JUNIOR WC": -90501,
    "HIGHLAND BULLDOG JR WC": -90501,
    "HIGHLAND PARK LITTLE GIANTS": -90501,
    "HILLTOPPERS WC": -90501,
    "HINSDALE RED DEVIL WC": -90501,
    "HOFFMAN ESTATES WC": -90501,
    "HONONEGAH KIDS WC": -90501,
    "HOOPESTON AREA WC": -90501,
    "IRON MAN": -90501,
    "JOLIET JUNIOR STEELMEN": -90501,
    "JUNIOR GATORS WC": -90501,
    "JUNIOR VIKINGS": -90501,
    "KNIGHTS WRESTLING": -90501,
    "L-P CRUNCHING CAVS": -90501,
    "LAKELAND PREDATORS": -90501,
    "LEMONT BEARS WC": -90501,
    "LIMESTONE YOUTH WC": -90501,
    "LINCOLN-WAY WC": -90501,
    "LIONHEART INTENSE WRESTLING": -90501,
    "LITTLE CELTIC WC": -90501,
    "LITTLE FALCONS WC": -90501,
    "LITTLE HUSKIE WC": -90501,
    "LITTLE REDBIRD WC": -90501,
    "LOCKPORT JR PORTERS WC": -90501,
    "MAD DOG WRESTLING ACADEMY": -90501,
    "MAINE EAGLES WC": -90501,
    "MARENGO INDIANS YOUTH WRESTLING": -90501,
    "MARTINEZ FOX VALLEY ELITE": -90501,
    "MCLEAN COUNTY WC": -90501,
    "MENDOTA WC": -90501,
    "MIDWEST CENTRAL YOUTH": -90501,
    "MINOOKA LITTLE INDIANS": -90501,
    "MOLINE WC": -90501,
    "MORRISON STALLIONS WC": -90501,
    "MORTON LITTLE MUSTANGS": -90501,
    "MORTON YOUTH WRESTLING": -90501,
    "MT. PULASKI WC": -90501,
    "MT. VERNON LIONS": -90501,
    "MT. ZION WC": -90501,
    "MURPHYSBORO WRESTLING": -90501,
    "MUSTANG WC": -90501,
    "NAPERVILLE WC": -90501,
    "NOTRE DAME WRESTLING": -90501,
    "O'FALLON LITTLE PANTHERS": -90501,
    "OAK FOREST WARRIORS": -90501,
    "OAK LAWN P.D. WILDCATS": -90501,
    "OAKWOOD WC": -90501,
    "ORLAND PARK PIONEERS": -90501,
    "OSWEGO PANTHERS": -90501,
    "PANTHER CUB WRESTLING CLUB": -90501,
    "PANTHER POWERHOUSE WC": -90501,
    "PANTHER/REDHAWK WC": -90501,
    "PEORIA RAZORBACKS YOUTH WC": -90501,
    "PLAINFIELD WC": -90501,
    "POLO WC": -90501,
    "PONTIAC PYTHONS": -90501,
    "PRAIRIE CENTRAL-CHENOA HAWKS": -90501,
    "PROVISO POWERHOUSE WC": -90501,
    "QUINCY WC": -90501,
    "REED CUSTER KNIGHTS": -90501,
    "RICH RATTLERS WC": -90501,
    "RICHMOND WRESTLING CLUB": -90501,
    "RIVERBEND WC": -90501,
    "RIVERDALE JR. RAMS WC": -90501,
    "ROCHESTER WC": -90501,
    "ROCK ISLAND WC": -90501,
    "ROCKFORD WC": -90501,
    "ROMEOVILLE WC": -90501,
    "SAUK VALLEY WRESTLING CLUB": -90501,
    "SAUKEE YOUTH WC": -90501,
    "SCN YOUTH WC": -90501,
    "SENECA IRISH CADETS": -90501,
    "SHAMROCK WC": -90501,
    "SHELBYVILLE JR RAMS WRESTLING": -90501,
    "SJO SPARTAN YOUTH WC": -90501,
    "SONS OF THUNDER": -90501,
    "SPIDER WC": -90501,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": -90501,
    "ST. CHARLES EAST WC": -90501,
    "STILLMAN VALLEY WC": -90501,
    "SYCAMORE WC": -90501,
    "TAYLORVILLE WC": -90501,
    "TEAM WEST WOLVES": -90501,
    "TIGER WC": -90501,
    "TIGERTOWN TANGLERS": -90501,
    "TINLEY PARK BULLDOGS": -90501,
    "TOMCAT WC": -90501,
    "TREVIAN WC": -90501,
    "TRI-VALLEY WC": -90501,
    "TRIAD LITTLE KNIGHTS": -90501,
    "UNITY WC": -90501,
    "VANDALIA JR WRESTLING": -90501,
    "VERMILION VALLEY ELITE": -90501,
    "VILLA LOMBARD COUGARS": -90501,
    "VILLA PARK YOUNG WARRIORS": -90501,
    "VITTUM CATS": -90501,
    "WARRENSBURG WC": -90501,
    "WASHINGTON JR PANTHERS": -90501,
    "WEST HANCOCK WC": -90501,
    "WESTVILLE YOUTH WC": -90501,
    "WHEATON TIGER WC": -90501,
    "WOLFPAK WC": -90501,
    "WRESTLING FACTORY": -90501,
    "XTREME WRESTLING": -90501,
    "YORKVILLE WRESTLING CLUB": -90501,
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
    "WALKOVER",
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

    if result_type == "WALKOVER":
        return 0.0  # This is just an approximation

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
    with open(HERE / "extracted.2006.json") as file_obj:
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
