# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ARG": "ARGENTA/OREANA KIDS CLUB",
    "ARL": "ARLINGTON CARDINALS",
    "BAR": "BARTLETT HAWK WC",
    "BAT": "BATAVIA PINNERS",
    "BEL": "BELLEVILLE LITTLE DEVILS",
    "BEN": "BENTON JR. WC",
    "BET": "BETHALTO BULLS WC",
    "BEV": "BELVIDERE BANDITS",
    "BIO": "BISON WC",
    "BIS": "BISMARCK-HENNING WC",
    "BLA": "BLACKHAWK WC",
    "BLO": "BLOOMINGTON RAIDER WC",
    "BOY": "BOYS & GIRLS CLUB OF PEKIN",
    "BRA": "BRAWLERS WC",
    "CAM": "CAMP POINT CENTRAL",
    "CAR": "CARLINVILLE KIDS WC",
    "CAY": "CARY JR TROJAN MATMEN",
    "CEN": "CENTRAL WC",
    "CHA": "CHAMPAIGN KIDS WRESTLING",
    "CHE": "CHENOA MAT CATS",
    "CHI": "CHILLICOTHE WC",
    "CHL": "CHILLICOTHE WC",
    "CHR": "CHARLESTON WC",
    "CRY": "CRYSTAL LAKE WIZARDS",
    "CUM": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DEK": "DEKALB WC",
    "DIX": "DIXON WC",
    "DOW": "DOWNERS GROVE COUGARS",
    "DUN": "DUNDEE HIGHLANDERS",
    "DUR": "DURAND-PECATONICA CARNIVORES",
    "EAS": "EAST MOLINE PANTHER PINNERS",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "EUR": "EUREKA KIDS WC",
    "FAC": "FALCON YOUTH WC",
    "FAL": "FALCON WC",
    "FIS": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "GAL": "GALESBURG JR STREAKS",
    "GEE": "GENESEO WC",
    "GEN": "GENERALS",
    "GLA": "GLADIATORS",
    "GLE": "GLEN ELLYN DUNGEON WC",
    "GLN": "GLENBARD EAST JR RAMS",
    "GRA": "GRANITE CITY JR WARRIORS",
    "HAE": "HARVEY TWISTERS",
    "HAR": "HARLEM COUGARS",
    "HIG": "HIGHLAND BULLDOG JR WC",
    "HIL": "HILLSBORO JR TOPPERS",
    "HIN": "HINSDALE RED DEVIL WC",
    "HIT": "HILLTOPPERS WC",
    "HON": "HONONEGAH KIDS WC",
    "HOO": "HOOPESTON AREA WC",
    "HUS": "HUSKIES WC",
    "ILL": "ILLINI BLUFFS WC",
    "JAC": "JACKSONVILLE WC",
    "JOL": "JOLIET BOYS CLUB COBRAS",
    "JRG": "JR. GOLDEN EAGLES",
    "JRP": "JR. PANTHERS WRESTLING",
    "JRR": "JR. ROCKET WRESTLING",
    "JRS": "JR. SENTINELS",
    "JUP": "JUNIOR PIRATE WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAE": "LAKELAND PREDATORS",
    "LAO": "LAN-OAK P.D. LITTLE REBELS",
    "LAR": "LARKIN JR. ROYALS WC",
    "LAW": "LAWRENCE COUNTY WC",
    "LEM": "LEMONT BEARS WC",
    "LIB": "LITTLE BOILER WC",
    "LIC": "LITTLE CELTIC WC",
    "LIN": "LINCOLN-WAY WC",
    "LIO": "LIONS WC",
    "LIR": "LIL' ROUGHNECKS",
    "LOC": "LOCKPORT GATORS WC",
    "LPC": "L-P CRUNCHING CAVS",
    "MAC": "MACOMB LITTLE BOMBERS",
    "MAF": "MARTINEZ FOX VALLEY ELITE WC",
    "MAI": "MAINE EAGLES WC",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "MID": "MIDWEST CENTRAL YOUTH",
    "MOL": "MOLINE WC",
    "MOT": "MORTON LITTLE MUSTANGS",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "MUS": "MUSTANG WC",
    "NAP": "NAPERVILLE WC",
    "NOT": "NOTRE DAME",
    "OAK": "OAK FOREST WARRIORS",
    "OAL": "OAK LAWN P.D. WILDCATS",
    "OAW": "OAKWOOD WC",
    "OPR": "OPRF LITTLE HUSKIE WC",
    "ORL": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTHERS",
    "PAL": "PALATINE PANTHERS WC",
    "PAN": "PANTHER CUB WC",
    "PAT": "PANTHER WC",
    "PLA": "PLAINFIELD WC",
    "POL": "POLO WC",
    "PON": "PONTIAC PYTHONS",
    "POY": "PONY EXPRESS WC",
    "RAI": "RAIDER WC",
    "RAM": "RAMS WC",
    "RIC": "RICH RATTLERS WC",
    "RIV": "RIVERBEND WC",
    "ROF": "ROCKFORD WC",
    "ROU": "ROUND LAKE BAD BOYZ",
    "ROX": "ROXANA KIDS WRESTING CLUB",
    "SAU": "SAUKEE YOUTH WC",
    "SAV": "SAVANNA REDHAWKS",
    "SCH": "SCHAUMBURG JR. SAXONS",
    "SHR": "SHARKS WC",
    "SJO": "SJO SPARTAN WC",
    "SOU": "SOUTHERN ILLINOIS EAGLES",
    "SPR": "SPRINGFIELD CAPITALS",
    "STC": "ST. CHARLES WC",
    "STE": "STERLING NEWMAN JR COMETS",
    "STI": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE WC",
    "TAY": "TAYLORVILLE WC",
    "TAZ": "TAZEWELL COUNTY KIDZ WC",
    "TBI": "T-BIRD/RAIDER WRESTLING",
    "TEX": "TEAM XPRESS",
    "TIE": "TIGERTOWN TANGLERS",
    "TIG": "TIGER WC",
    "TIN": "TINLEY PARK BULLDOGS",
    "TOM": "TOMCAT WC",
    "TRI": "TRIAD KNIGHTS",
    "UNI": "UNITY WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAK": "WAUKEGAN TAKEDOWN",
    "WAU": "WAUBONSIE WC",
    "WES": "WEST FRANKFORT JR. WC",
    "WHF": "WHEATON FRANKLIN WC",
    "WHM": "WHEATON MONROE EAGLES",
    "WOL": "WOLFPAK WC",
    "WRE": "WRESTLING FACTORY",
    "YOR": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING = {}
SENIOR_TEAM_ACRONYM_MAPPING = {}
TEAM_NAME_MAPPING = {
    "ARGENTA/OREANA KIDS CLUB": -90105,
    "ARLINGTON CARDINALS": -90105,
    "BARTLETT HAWK WC": -90105,
    "BATAVIA PINNERS": -90105,
    "BELLEVILLE LITTLE DEVILS": -90105,
    "BELVIDERE BANDITS": -90105,
    "BENTON JR. WC": -90105,
    "BETHALTO BULLS WC": -90105,
    "BISMARCK-HENNING WC": -90105,
    "BISON WC": -90105,
    "BLACKHAWK WC": -90105,
    "BLOOMINGTON RAIDER WC": -90105,
    "BOYS & GIRLS CLUB OF PEKIN": -90105,
    "BRAWLERS WC": -90105,
    "CAMP POINT CENTRAL": -90105,
    "CARLINVILLE KIDS WC": -90105,
    "CARY JR TROJAN MATMEN": -90105,
    "CENTRAL WC": -90105,
    "CHAMPAIGN KIDS WRESTLING": -90105,
    "CHARLESTON WC": -90105,
    "CHENOA MAT CATS": -90105,
    "CHILLICOTHE WC": -90105,
    "CRYSTAL LAKE WIZARDS": -90105,
    "CUMBERLAND YOUTH WC": -90105,
    "DAKOTA WC": -90105,
    "DEKALB WC": -90105,
    "DIXON WC": -90105,
    "DOWNERS GROVE COUGARS": -90105,
    "DUNDEE HIGHLANDERS": -90105,
    "DURAND-PECATONICA CARNIVORES": -90105,
    "EAST MOLINE PANTHER PINNERS": -90105,
    "EDWARDSVILLE WC": -90105,
    "EFFINGHAM YOUTH WC": -90105,
    "EUREKA KIDS WC": -90105,
    "FALCON WC": -90105,
    "FALCON YOUTH WC": -90105,
    "FISHER WC": -90105,
    "FOX VALLEY WC": -90105,
    "GALESBURG JR STREAKS": -90105,
    "GENERALS": -90105,
    "GENESEO WC": -90105,
    "GLADIATORS": -90105,
    "GLEN ELLYN DUNGEON WC": -90105,
    "GLENBARD EAST JR RAMS": -90105,
    "GRANITE CITY JR WARRIORS": -90105,
    "HARLEM COUGARS": -90105,
    "HARVEY TWISTERS": -90105,
    "HIGHLAND BULLDOG JR WC": -90105,
    "HILLSBORO JR TOPPERS": 170,
    "HILLTOPPERS WC": -90105,
    "HINSDALE RED DEVIL WC": -90105,
    "HONONEGAH KIDS WC": -90105,
    "HOOPESTON AREA WC": -90105,
    "HUSKIES WC": -90105,
    "ILLINI BLUFFS WC": -90105,
    "JACKSONVILLE WC": -90105,
    "JOLIET BOYS CLUB COBRAS": -90105,
    "JR. GOLDEN EAGLES": -90105,
    "JR. PANTHERS WRESTLING": -90105,
    "JR. ROCKET WRESTLING": -90105,
    "JR. SENTINELS": -90105,
    "JUNIOR PIRATE WC": -90105,
    "KNIGHTS WRESTLING": -90105,
    "L-P CRUNCHING CAVS": -90105,
    "LAKELAND PREDATORS": -90105,
    "LAN-OAK P.D. LITTLE REBELS": -90105,
    "LARKIN JR. ROYALS WC": -90105,
    "LAWRENCE COUNTY WC": -90105,
    "LEMONT BEARS WC": -90105,
    "LIL' ROUGHNECKS": -90105,
    "LINCOLN-WAY WC": -90105,
    "LIONS WC": -90105,
    "LITTLE BOILER WC": -90105,
    "LITTLE CELTIC WC": -90105,
    "LOCKPORT GATORS WC": -90105,
    "MACOMB LITTLE BOMBERS": -90105,
    "MAINE EAGLES WC": -90105,
    "MARENGO WC": -90105,
    "MARTINEZ FOX VALLEY ELITE WC": -90105,
    "MATTOON YOUTH WC": -90105,
    "MIDWEST CENTRAL YOUTH": -90105,
    "MOLINE WC": -90105,
    "MORTON LITTLE MUSTANGS": -90105,
    "MT. VERNON LIONS": -90105,
    "MT. ZION WC": -90105,
    "MURPHYSBORO WRESTLING": -90105,
    "MUSTANG WC": -90105,
    "NAPERVILLE WC": -90105,
    "NOTRE DAME": -90105,
    "OAK FOREST WARRIORS": -90105,
    "OAK LAWN P.D. WILDCATS": -90105,
    "OAKWOOD WC": -90105,
    "OPRF LITTLE HUSKIE WC": -90105,
    "ORLAND PARK PIONEERS": -90105,
    "OSWEGO PANTHERS": -90105,
    "PALATINE PANTHERS WC": -90105,
    "PANTHER CUB WC": -90105,
    "PANTHER WC": -90105,
    "PLAINFIELD WC": -90105,
    "POLO WC": -90105,
    "PONTIAC PYTHONS": -90105,
    "PONY EXPRESS WC": -90105,
    "RAIDER WC": -90105,
    "RAMS WC": -90105,
    "RICH RATTLERS WC": -90105,
    "RIVERBEND WC": -90105,
    "ROCKFORD WC": -90105,
    "ROUND LAKE BAD BOYZ": -90105,
    "ROXANA KIDS WRESTING CLUB": -90105,
    "SAUKEE YOUTH WC": -90105,
    "SAVANNA REDHAWKS": -90105,
    "SCHAUMBURG JR. SAXONS": -90105,
    "SHARKS WC": -90105,
    "SJO SPARTAN WC": -90105,
    "SOUTHERN ILLINOIS EAGLES": -90105,
    "SPRINGFIELD CAPITALS": -90105,
    "ST. CHARLES WC": -90105,
    "STERLING NEWMAN JR COMETS": -90105,
    "STILLMAN VALLEY WC": -90105,
    "SYCAMORE WC": -90105,
    "T-BIRD/RAIDER WRESTLING": -90105,
    "TAYLORVILLE WC": -90105,
    "TAZEWELL COUNTY KIDZ WC": -90105,
    "TEAM XPRESS": -90105,
    "TIGER WC": -90105,
    "TIGERTOWN TANGLERS": -90105,
    "TINLEY PARK BULLDOGS": -90105,
    "TOMCAT WC": -90105,
    "TRIAD KNIGHTS": -90105,
    "UNITY WC": -90105,
    "VANDALIA JR WRESTLING": -90105,
    "VILLA LOMBARD COUGARS": -90105,
    "VITTUM CATS": -90105,
    "WAUBONSIE WC": -90105,
    "WAUKEGAN TAKEDOWN": -90105,
    "WEST FRANKFORT JR. WC": -90105,
    "WHEATON FRANKLIN WC": -90105,
    "WHEATON MONROE EAGLES": -90105,
    "WOLFPAK WC": -90105,
    "WRESTLING FACTORY": -90105,
    "YORKVILLE WC": -90105,
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
    with open(HERE / "extracted.2002.json") as file_obj:
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
