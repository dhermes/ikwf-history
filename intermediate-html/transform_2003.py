# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ALE": "ALEDO BEAR COUNTRY WC",
    "ALL": "ALLEMAN JR. PIONEER WC",
    "ARG": "ARGENTA/OREANA KIDS CLUB",
    "ARL": "ARLINGTON CARDINALS",
    "BAD": "BADGER WC",
    "BAH": "BARTLETT HAWK WC",
    "BAT": "BATAVIA PINNERS",
    "BEL": "BELLEVILLE LITTLE DEVILS",
    "BEN": "BENTON JR. WC",
    "BET": "BETHALTO BULLS WC",
    "BEV": "BELVIDERE BANDITS",
    "BIO": "BISON WC",
    "BIS": "BISMARCK-HENNING WC",
    "BLA": "BLACKHAWK WC",
    "BRA": "BRAWLERS WC",
    "CAL": "CARLINVILLE KIDS WC",
    "CAR": "CARBONDALE WC",
    "CAY": "CARY JR. TROJAN MATMEN",
    "CHA": "CHAMPAIGN KIDS WRESTLING",
    "CHB": "CHICAGO BULLDOG WC",
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLI DAWGS WC",
    "CRI": "CRIMSON HEAT WC",
    "CRY": "CRYSTAL LAKE WIZARDS",
    "CUM": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DEK": "DEKALB WC",
    "DIX": "DIXON WC",
    "DOW": "DOWNERS GROVE COUGARS",
    "DUN": "DUNDEE HIGHLANDERS",
    "DUP": "DU-PEC CARNIVORES",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "ELM": "ELMHURST JR. DUKES",
    "FAC": "FALCON YOUTH WC",
    "FAL": "FALCON WC",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FOR": "FORD HEIGHTS FALCONS",
    "FOX": "FOX VALLEY WC",
    "GEE": "GENESEO WC",
    "GEO": "GEORGETOWN YOUTH WC",
    "GLA": "GLADIATORS",
    "GLN": "GLENBARD EAST JR RAMS",
    "GRA": "GRANITE CITY JR WARRIORS",
    "GRP": "GRAPPLIN' DEVILS WC",
    "HAE": "HARVEY TWISTERS",
    "HAR": "HARLEM COUGARS",
    "HER": "HERRIN WC",
    "HIG": "HIGHLAND BULLDOG JR WC",
    "HIL": "HILLSBORO JR TOPPERS",
    "HIN": "HINSDALE RED DEVIL WC",
    "HOF": "HOFFMAN ESTATES WC",
    "HON": "HONONEGAH KIDS WC",
    "HOO": "HOOPESTON AREA WC",
    "JAC": "JACKSONVILLE WC",
    "JOL": "JOLIET BOYS CLUB COBRAS",
    "JRG": "JR. GOLDEN EAGLES",
    "JRP": "JR. PANTHERS WRESTLING",
    "JRR": "JR. ROCKET WC",
    "JUP": "JUNIOR PIRATE WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAE": "LAKELAND PREDATORS",
    "LAN": "LANCER WC",
    "LAW": "LAWRENCE COUNTY WC",
    "LEM": "LEMONT BEARS WC",
    "LIB": "LITTLE BOILER WC",
    "LIC": "LITTLE CELTIC WC",
    "LIN": "LINCOLN-WAY WC",
    "LIO": "LIONS WC",
    "LIR": "LITTLE REDBIRD WC",
    "LIV": "LITTLE VIKINGS OF H-F",
    "LOC": "LOCKPORT GATORS",
    "LPC": "L-P CRUNCHING CAVS",
    "MAF": "MARTINEZ FOX VALLEY ELITE WC",
    "MAI": "MAINE EAGLES WC",
    "MAN": "MANTENO JR PANTHERS",
    "MAT": "MATTOON YOUTH WC",
    "MEN": "MENDOTA MAT MASTERS",
    "MET": "METAMORA KIDS WC",
    "MID": "MIDWEST CENTRAL YOUTH",
    "MOL": "MOLINE WC",
    "MOT": "MORTON LITTLE MUSTANGS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "MUS": "MUSTANG WC",
    "NAP": "NAPERVILLE WC",
    "NOT": "NOTRE DAME WC",
    "OAL": "OAK LAWN P.D. WILDCATS",
    "OAW": "OAKWOOD WC",
    "ORL": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTHERS",
    "PAL": "PALATINE PANTHERS",
    "PAN": "PANTHER CUB WC",
    "PAT": "PANTHER WC",
    "PLA": "PLAINFIELD WC",
    "POL": "POLO WC",
    "PON": "PONTIAC PYTHONS",
    "RAI": "RAIDER WC",
    "RAM": "RAMS WC",
    "RIC": "RICH RATTLERS",
    "RIV": "RIVERBEND WC",
    "RJH": "RIVERDALE JR. HIGH",
    "ROF": "ROCKFORD WC",
    "ROX": "ROXANA KIDS WRESTING CLUB",
    "SAU": "SAUKEE YOUTH WC",
    "SAV": "SAVANNA REDHAWKS",
    "SCN": "SCN YOUTH WC",
    "SEN": "SENECA IRISH CADETS",
    "SHA": "SHAMROCK WC",
    "SHE": "SHELBYVILLE JR. RAMS WC",
    "SJO": "SJO YOUTH WC",
    "SOU": "SOUTHERN ILLINOIS EAGLES",
    "SPR": "SPRINGFIELD CAPITALS",
    "STC": "ST. CHARLES WC",
    "STI": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE WC",
    "TAK": "TAKEDOWN WC",
    "TBI": "T-BIRD/RAIDER WRESTLING",
    "TIG": "TIGER WC",
    "TIN": "TINLEY PARK BULLDOGS",
    "TOM": "TOMCAT WC",
    "TRE": "TREVIAN WC",
    "TRI": "TRIAD KNIGHTS",
    "TTT": "TIGERTOWN TANGLERS",
    "UNI": "UNITY WC",
    "UNT": "UNITED TOWNSHIP WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAR": "WARRENSBURG WC",
    "WAU": "WAUBONSIE WC",
    "WEC": "WEST CHICAGO SPIDER WC",
    "WET": "WESTVILLE YOUTH WC",
    "WHF": "WHEATON FRANKLIN WC",
    "WHM": "WHEATON MONROE EAGLES",
    "WHT": "WHEATON TIGER WC",
    "WOL": "WOLFPAK WC",
    "WRE": "WRESTLING FACTORY",
    "YOR": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING = {
    "ROK": "ROCK ISLAND JR. ROCKS",
}
SENIOR_TEAM_ACRONYM_MAPPING = {
    "ROK": "ROCK ISLAND WC",
}
TEAM_NAME_MAPPING = {
    "ALEDO BEAR COUNTRY WC": -20802,
    "ALLEMAN JR. PIONEER WC": -20802,
    "ARGENTA/OREANA KIDS CLUB": -20802,
    "ARLINGTON CARDINALS": -20802,
    "BADGER WC": -20802,
    "BARTLETT HAWK WC": -20802,
    "BATAVIA PINNERS": -20802,
    "BELLEVILLE LITTLE DEVILS": -20802,
    "BELVIDERE BANDITS": -20802,
    "BENTON JR. WC": -20802,
    "BETHALTO BULLS WC": -20802,
    "BISMARCK-HENNING WC": -20802,
    "BISON WC": -20802,
    "BLACKHAWK WC": -20802,
    "BRAWLERS WC": -20802,
    "CARBONDALE WC": -20802,
    "CARLINVILLE KIDS WC": -20802,
    "CARY JR. TROJAN MATMEN": -20802,
    "CHAMPAIGN KIDS WRESTLING": -20802,
    "CHENOA MAT CATS": -20802,
    "CHICAGO BULLDOG WC": -20802,
    "CHILLI DAWGS WC": -20802,
    "CRIMSON HEAT WC": -20802,
    "CRYSTAL LAKE WIZARDS": -20802,
    "CUMBERLAND YOUTH WC": -20802,
    "DAKOTA WC": -20802,
    "DEKALB WC": -20802,
    "DIXON WC": -20802,
    "DOWNERS GROVE COUGARS": -20802,
    "DU-PEC CARNIVORES": -20802,
    "DUNDEE HIGHLANDERS": -20802,
    "EDWARDSVILLE WC": -20802,
    "EFFINGHAM YOUTH WC": -20802,
    "ELMHURST JR. DUKES": -20802,
    "FALCON WC": -20802,
    "FALCON YOUTH WC": -20802,
    "FENWICK FALCONS WC": -20802,
    "FISHER WC": -20802,
    "FORD HEIGHTS FALCONS": -20802,
    "FOX VALLEY WC": -20802,
    "GENESEO WC": -20802,
    "GEORGETOWN YOUTH WC": -20802,
    "GLADIATORS": -20802,
    "GLENBARD EAST JR RAMS": -20802,
    "GRANITE CITY JR WARRIORS": -20802,
    "GRAPPLIN' DEVILS WC": -20802,
    "HARLEM COUGARS": -20802,
    "HARVEY TWISTERS": -20802,
    "HERRIN WC": -20802,
    "HIGHLAND BULLDOG JR WC": -20802,
    "HILLSBORO JR TOPPERS": -20802,
    "HINSDALE RED DEVIL WC": -20802,
    "HOFFMAN ESTATES WC": -20802,
    "HONONEGAH KIDS WC": -20802,
    "HOOPESTON AREA WC": -20802,
    "JACKSONVILLE WC": -20802,
    "JOLIET BOYS CLUB COBRAS": -20802,
    "JR. GOLDEN EAGLES": -20802,
    "JR. PANTHERS WRESTLING": -20802,
    "JR. ROCKET WC": -20802,
    "JUNIOR PIRATE WC": -20802,
    "KNIGHTS WRESTLING": -20802,
    "L-P CRUNCHING CAVS": -20802,
    "LAKELAND PREDATORS": -20802,
    "LANCER WC": -20802,
    "LAWRENCE COUNTY WC": -20802,
    "LEMONT BEARS WC": -20802,
    "LINCOLN-WAY WC": -20802,
    "LIONS WC": -20802,
    "LITTLE BOILER WC": -20802,
    "LITTLE CELTIC WC": -20802,
    "LITTLE REDBIRD WC": -20802,
    "LITTLE VIKINGS OF H-F": -20802,
    "LOCKPORT GATORS": -20802,
    "MAINE EAGLES WC": -20802,
    "MANTENO JR PANTHERS": -20802,
    "MARTINEZ FOX VALLEY ELITE WC": -20802,
    "MATTOON YOUTH WC": -20802,
    "MENDOTA MAT MASTERS": -20802,
    "METAMORA KIDS WC": -20802,
    "MIDWEST CENTRAL YOUTH": -20802,
    "MOLINE WC": -20802,
    "MORTON LITTLE MUSTANGS": -20802,
    "MT. ZION WC": -20802,
    "MURPHYSBORO WRESTLING": -20802,
    "MUSTANG WC": -20802,
    "NAPERVILLE WC": -20802,
    "NOTRE DAME WC": -20802,
    "OAK LAWN P.D. WILDCATS": -20802,
    "OAKWOOD WC": -20802,
    "ORLAND PARK PIONEERS": -20802,
    "OSWEGO PANTHERS": -20802,
    "PALATINE PANTHERS": -20802,
    "PANTHER CUB WC": -20802,
    "PANTHER WC": -20802,
    "PLAINFIELD WC": -20802,
    "POLO WC": -20802,
    "PONTIAC PYTHONS": -20802,
    "RAIDER WC": -20802,
    "RAMS WC": -20802,
    "RICH RATTLERS": -20802,
    "RIVERBEND WC": -20802,
    "RIVERDALE JR. HIGH": -20802,
    "ROCK ISLAND JR. ROCKS": -20802,
    "ROCK ISLAND WC": -20802,
    "ROCKFORD WC": -20802,
    "ROXANA KIDS WRESTING CLUB": -20802,
    "SAUKEE YOUTH WC": -20802,
    "SAVANNA REDHAWKS": -20802,
    "SCN YOUTH WC": -20802,
    "SENECA IRISH CADETS": -20802,
    "SHAMROCK WC": -20802,
    "SHELBYVILLE JR. RAMS WC": -20802,
    "SJO YOUTH WC": -20802,
    "SOUTHERN ILLINOIS EAGLES": -20802,
    "SPRINGFIELD CAPITALS": -20802,
    "ST. CHARLES WC": -20802,
    "STILLMAN VALLEY WC": -20802,
    "SYCAMORE WC": -20802,
    "T-BIRD/RAIDER WRESTLING": -20802,
    "TAKEDOWN WC": -20802,
    "TIGER WC": -20802,
    "TIGERTOWN TANGLERS": -20802,
    "TINLEY PARK BULLDOGS": -20802,
    "TOMCAT WC": -20802,
    "TREVIAN WC": -20802,
    "TRIAD KNIGHTS": -20802,
    "UNITED TOWNSHIP WC": -20802,
    "UNITY WC": -20802,
    "VANDALIA JR WRESTLING": -20802,
    "VILLA LOMBARD COUGARS": -20802,
    "VITTUM CATS": -20802,
    "WARRENSBURG WC": -20802,
    "WAUBONSIE WC": -20802,
    "WEST CHICAGO SPIDER WC": -20802,
    "WESTVILLE YOUTH WC": -20802,
    "WHEATON FRANKLIN WC": -20802,
    "WHEATON MONROE EAGLES": -20802,
    "WHEATON TIGER WC": -20802,
    "WOLFPAK WC": -20802,
    "WRESTLING FACTORY": -20802,
    "YORKVILLE WC": -20802,
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
    with open(HERE / "extracted.2003.json", "rb") as file_obj:
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
