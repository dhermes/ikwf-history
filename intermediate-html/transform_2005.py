# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ABC": "ALEDO BEAR COUNTRY",
    "ACE": "ACES WC",
    "ARG": "ARGENTA-OREANA KIDS CLUB",
    "ARL": "ARLINGTON CARDNALS",
    "BAT": "BATAVIA PINNERS",
    "BDG": "BADGERS WC",
    "BJH": "BARTLETT JR. HAWKS",
    "BKH": "BLACKHAWK WC",
    "BKT": "BLACK KATS WC",
    "BLD": "BELLEVILLE LITTLE DEVILS",
    "BLM": "BLOOMINGTON RAIDERS WC",
    "BLV": "BELVIDERE BANDITS",
    "BMH": "BISMARK-HENNING WC",
    "BRL": "BRAWLERS",
    "BRR": "BARRINGTON BRONCOS",
    "BSN": "BISON WC",
    "BTB": "BETHALTO BULLS WC",
    "CHM": "CHAMPAIGN KIDS WC",
    "CJS": "CARBONDALE JUNIOR SPIRITS",
    "CJT": "CARY JR. TROJAN MATMEN",
    "CLA": "CENTRAILIA",
    "CLP": "CLIPPER WC",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "CMB": "CUMBERLAND YOUTH WC",
    "CNT": "CENTRAL",
    "CTC": "CROSSTOWN CRUSHERS",
    "CVR": "COLLINSVILLE RAIDERS",
    "DAK": "DAKOTA WC",
    "DDH": "DUNDEE HIGHLANDERS",
    "DGC": "DOWNERS GROVE COUGARS",
    "DIX": "DIXON WC",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM JUNIOR WC",
    "EJD": "ELMHUSRT JR. DUKES",
    "EPG": "EL PASO/GRIDLEY WC",
    "FCY": "FALCON YOUTH WC",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FLC": "FALCON WC",
    "FOX": "FOX VALLEY WC",
    "FRR": "FAIRMONT ROUGH RIDERS",
    "FTT": "FIGHTIN' TITANS",
    "GEN": "GENESEO WC",
    "GER": "GLENBARD EAST JR. RAMS",
    "GLA": "GLADIATORS",
    "GLD": "GOLDEN EAGLES",
    "GRM": "GERMANTOWN WC",
    "GRY": "GEORGETOWN RUDE DOGS YOUTH WC",
    "HBJ": "HIGHLAND BULLDOGS JR. WC",
    "HER": "HERRIN WC",
    "HJT": "HILLSBORO JR. TOPPERS",
    "HOF": "HOFFMAN ESTATES WC",
    "HON": "HONONEGAH KIDS WC",
    "HPG": "HIGHLAND PARK LITTLE GIANTS",
    "HPN": "HOOPSTON AREA WC",
    "HRD": "HINSDALE RED DEVILS",
    "HRL": "HARLEM COUGARS",
    "HTW": "HARVEY PARK DISTRICT TWISTERS",
    "HUR": "HURRICANES",
    "IMP": "IMPACT WC",
    "JBC": "JOLIET BOYS CLUB COBRAS",
    "JCG": "JR. COUGARS",
    "JMS": "JR. MUSTANGS",
    "JVK": "JR. VIKINGS",
    "KGT": "KNIGHTS WC",
    "LAK": "LAKELAND PREDATORS",
    "LEM": "LEMONT BEARS WC",
    "LHI": "LIONHEART INTENSE WC",
    "LJP": "LOCKPORT JR PORTERS",
    "LLB": "LITTLE BOILERS WC",
    "LLC": "LITTLE CELTICS",
    "LLF": "LITTLE FALCONS WC",
    "LLH": "LITTLE HUSKIES WC",
    "LLS": "LIL' STORM YOUTH WC",
    "LNW": "LINCOLN-WAY WC",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WC",
    "MAT": "MATTOON YOUTH WC",
    "MDW": "MAD DOG WRESTLING ACADEMY",
    "MED": "MEDALIST WC",
    "MEN": "MENDOTA WC",
    "MFV": "MARTINEZ FOX VALLEY ELITE",
    "MIY": "MARENGO INDIANS YOUTH WC",
    "MLB": "MACOMB LITTLE BOMBERS",
    "MLI": "MINOOKA LITTLE INDIANS",
    "MLM": "MORTON LITTLE MUSTANGS",
    "MNE": "MAINE EAGLES",
    "MOL": "MOLINE WC",
    "MRB": "MURPHYSBORO WC",
    "MRS": "MORRISON STALLIONS WC",
    "MRT": "MORTON YOUTH WC",
    "MST": "MUSTANG WC",
    "MTP": "MT. PULASKI",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MWC": "MIDWEST CENTRAL YOUTH WC",
    "NPV": "NAPERVILLE WC",
    "OFW": "OAK FOREST WARRIORS",
    "OLP": "O'FALLION LITTLE PANTHERS",
    "OLW": "OAK LAWN PARK DISTRICT WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTERS",
    "PAN": "PANTHER WC",
    "PCC": "PRAIRIE CENTRAL-CHENOA HAWKS",
    "PEK": "PEKIN BOYS AND GIRLS CLUB",
    "PLF": "PLAINFIELD WC",
    "PLP": "PALATINE PANTHERS WC",
    "PLT": "PLAINFIELD TORNADOES WC",
    "PLW": "PANTHER CUB WC",
    "PNP": "PANTHER POWERHOUSE WC",
    "PON": "PONTIAC PYTHONS",
    "PRP": "PROVISO POWERHOUSE",
    "PRZ": "PEORIA RAZORBACKS",
    "RJR": "RIVERDALE JR RAMS WC",
    "RKF": "ROCKFORD WC",
    "RKI": "ROCK ISLAND WC",
    "RKR": "ROCKRIDGE WC",
    "RMD": "RICHMOND WC",
    "ROX": "ROXANA KIDS WC",
    "RRT": "RICH RATTLERS WC",
    "RVB": "RIVERBEND WC",
    "SAV": "SAVANNA REDHAWKS",
    "SCE": "ST. CHARLES EAST WC",
    "SCN": "SCN YOUTH WC",
    "SHM": "SHAMROCK WC",
    "SIC": "SENECA IRISH CADETS",
    "SJO": "SJO SPRATAN YOUTH",
    "SJR": "SHELBYVILLE JR. RAMS WC",
    "SKE": "SAUKEE YOUTH WC",
    "SKV": "SAUK VALLEY WC",
    "SOT": "SONS OF THUNDER",
    "SPD": "SPIDER WC",
    "SPR": "SPRINGFIELD CAPITAL KIDS WRESTLING",
    "SRD": "SHERRARD WC",
    "STV": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE",
    "TAK": "TAKEDOWN WC",
    "TIG": "TIGER WC",
    "TLK": "TRIAD LITTLE KNIGHTS",
    "TOM": "TOMCAT WC",
    "TPB": "TINLEY PARK BULLDOGS",
    "TRV": "TRI-VALLEY WC",
    "TVN": "TREVIAN",
    "TWW": "TEAM WEST WOLVES",
    "UNT": "UNITED TOWNSHIP WC",
    "UNY": "UNITY WC",
    "VAN": "VANDALIA JR. WRESLTING",
    "VIT": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGARS",
    "WBN": "WAUBONSIE WC",
    "WHN": "WEST HANCOCK WC",
    "WHT": "WHEATON TIGERS",
    "WPK": "WOLFPAK WC",
    "WRB": "WARRENSBURG WC",
    "WRF": "WRESTLING FACTORY",
    "WSV": "WESTVILLE YOUTH WC",
    "XTR": "XTREME WC",
    "YRK": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING = {
    "CLD": "CHILLI DAWGS WC",
    "GCW": "GC JR. WARRIORS",
}
SENIOR_TEAM_ACRONYM_MAPPING = {
    "CLD": "CHILLI DAWGS",
    "GCW": "GRANITE CITY JR. WARRIORS",
}
TEAM_NAME_MAPPING = {
    "ACES WC": -30303,
    "ALEDO BEAR COUNTRY": -30303,
    "ARGENTA-OREANA KIDS CLUB": -30303,
    "ARLINGTON CARDNALS": -30303,
    "BADGERS WC": -30303,
    "BARRINGTON BRONCOS": -30303,
    "BARTLETT JR. HAWKS": -30303,
    "BATAVIA PINNERS": -30303,
    "BELLEVILLE LITTLE DEVILS": -30303,
    "BELVIDERE BANDITS": -30303,
    "BETHALTO BULLS WC": -30303,
    "BISMARK-HENNING WC": -30303,
    "BISON WC": -30303,
    "BLACK KATS WC": -30303,
    "BLACKHAWK WC": -30303,
    "BLOOMINGTON RAIDERS WC": -30303,
    "BRAWLERS": -30303,
    "CARBONDALE JUNIOR SPIRITS": -30303,
    "CARY JR. TROJAN MATMEN": -30303,
    "CENTRAILIA": -30303,
    "CENTRAL": -30303,
    "CHAMPAIGN KIDS WC": -30303,
    "CHILLI DAWGS WC": -30303,
    "CHILLI DAWGS": -30303,
    "CLIPPER WC": -30303,
    "COLLINSVILLE RAIDERS": -30303,
    "CROSSTOWN CRUSHERS": -30303,
    "CRYSTAL LAKE WIZARDS": -30303,
    "CUMBERLAND YOUTH WC": -30303,
    "DAKOTA WC": -30303,
    "DIXON WC": -30303,
    "DOWNERS GROVE COUGARS": -30303,
    "DUNDEE HIGHLANDERS": -30303,
    "EDWARDSVILLE WC": -30303,
    "EFFINGHAM JUNIOR WC": -30303,
    "EL PASO/GRIDLEY WC": -30303,
    "ELMHUSRT JR. DUKES": -30303,
    "FAIRMONT ROUGH RIDERS": -30303,
    "FALCON WC": -30303,
    "FALCON YOUTH WC": -30303,
    "FENWICK FALCONS WC": -30303,
    "FIGHTIN' TITANS": -30303,
    "FISHER WC": -30303,
    "FOX VALLEY WC": -30303,
    "GC JR. WARRIORS": -30303,
    "GENESEO WC": -30303,
    "GEORGETOWN RUDE DOGS YOUTH WC": -30303,
    "GERMANTOWN WC": -30303,
    "GLADIATORS": -30303,
    "GLENBARD EAST JR. RAMS": -30303,
    "GOLDEN EAGLES": -30303,
    "GRANITE CITY JR. WARRIORS": -30303,
    "HARLEM COUGARS": -30303,
    "HARVEY PARK DISTRICT TWISTERS": -30303,
    "HERRIN WC": -30303,
    "HIGHLAND BULLDOGS JR. WC": -30303,
    "HIGHLAND PARK LITTLE GIANTS": -30303,
    "HILLSBORO JR. TOPPERS": -30303,
    "HINSDALE RED DEVILS": -30303,
    "HOFFMAN ESTATES WC": -30303,
    "HONONEGAH KIDS WC": -30303,
    "HOOPSTON AREA WC": -30303,
    "HURRICANES": -30303,
    "IMPACT WC": -30303,
    "JOLIET BOYS CLUB COBRAS": -30303,
    "JR. COUGARS": -30303,
    "JR. MUSTANGS": -30303,
    "JR. VIKINGS": -30303,
    "KNIGHTS WC": -30303,
    "L-P CRUNCHING CAVS": -30303,
    "LAKELAND PREDATORS": -30303,
    "LEMONT BEARS WC": -30303,
    "LIL' STORM YOUTH WC": -30303,
    "LINCOLN-WAY WC": -30303,
    "LIONHEART INTENSE WC": -30303,
    "LITTLE BOILERS WC": -30303,
    "LITTLE CELTICS": -30303,
    "LITTLE FALCONS WC": -30303,
    "LITTLE HUSKIES WC": -30303,
    "LITTLE REDBIRD WC": -30303,
    "LOCKPORT JR PORTERS": -30303,
    "MACOMB LITTLE BOMBERS": -30303,
    "MAD DOG WRESTLING ACADEMY": -30303,
    "MAINE EAGLES": -30303,
    "MARENGO INDIANS YOUTH WC": -30303,
    "MARTINEZ FOX VALLEY ELITE": -30303,
    "MATTOON YOUTH WC": -30303,
    "MEDALIST WC": -30303,
    "MENDOTA WC": -30303,
    "MIDWEST CENTRAL YOUTH WC": -30303,
    "MINOOKA LITTLE INDIANS": -30303,
    "MOLINE WC": -30303,
    "MORRISON STALLIONS WC": -30303,
    "MORTON LITTLE MUSTANGS": -30303,
    "MORTON YOUTH WC": -30303,
    "MT. PULASKI": -30303,
    "MT. VERNON LIONS": -30303,
    "MT. ZION WC": -30303,
    "MURPHYSBORO WC": -30303,
    "MUSTANG WC": -30303,
    "NAPERVILLE WC": -30303,
    "O'FALLION LITTLE PANTHERS": -30303,
    "OAK FOREST WARRIORS": -30303,
    "OAK LAWN PARK DISTRICT WILDCATS": -30303,
    "ORLAND PARK PIONEERS": -30303,
    "OSWEGO PANTERS": -30303,
    "PALATINE PANTHERS WC": -30303,
    "PANTHER CUB WC": -30303,
    "PANTHER POWERHOUSE WC": -30303,
    "PANTHER WC": -30303,
    "PEKIN BOYS AND GIRLS CLUB": -30303,
    "PEORIA RAZORBACKS": -30303,
    "PLAINFIELD TORNADOES WC": -30303,
    "PLAINFIELD WC": -30303,
    "PONTIAC PYTHONS": -30303,
    "PRAIRIE CENTRAL-CHENOA HAWKS": -30303,
    "PROVISO POWERHOUSE": -30303,
    "RICH RATTLERS WC": -30303,
    "RICHMOND WC": -30303,
    "RIVERBEND WC": -30303,
    "RIVERDALE JR RAMS WC": -30303,
    "ROCK ISLAND WC": -30303,
    "ROCKFORD WC": -30303,
    "ROCKRIDGE WC": -30303,
    "ROXANA KIDS WC": -30303,
    "SAUK VALLEY WC": -30303,
    "SAUKEE YOUTH WC": -30303,
    "SAVANNA REDHAWKS": -30303,
    "SCN YOUTH WC": -30303,
    "SENECA IRISH CADETS": -30303,
    "SHAMROCK WC": -30303,
    "SHELBYVILLE JR. RAMS WC": -30303,
    "SHERRARD WC": -30303,
    "SJO SPRATAN YOUTH": -30303,
    "SONS OF THUNDER": -30303,
    "SPIDER WC": -30303,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": -30303,
    "ST. CHARLES EAST WC": -30303,
    "STILLMAN VALLEY WC": -30303,
    "SYCAMORE": -30303,
    "TAKEDOWN WC": -30303,
    "TEAM WEST WOLVES": -30303,
    "TIGER WC": -30303,
    "TINLEY PARK BULLDOGS": -30303,
    "TOMCAT WC": -30303,
    "TREVIAN": -30303,
    "TRI-VALLEY WC": -30303,
    "TRIAD LITTLE KNIGHTS": -30303,
    "UNITED TOWNSHIP WC": -30303,
    "UNITY WC": -30303,
    "VANDALIA JR. WRESLTING": -30303,
    "VILLA LOMBARD COUGARS": -30303,
    "VITTUM CATS": -30303,
    "WARRENSBURG WC": -30303,
    "WAUBONSIE WC": -30303,
    "WEST HANCOCK WC": -30303,
    "WESTVILLE YOUTH WC": -30303,
    "WHEATON TIGERS": -30303,
    "WOLFPAK WC": -30303,
    "WRESTLING FACTORY": -30303,
    "XTREME WC": -30303,
    "YORKVILLE WC": -30303,
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
    with open(HERE / "extracted.2005.json") as file_obj:
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
