# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import extract_2000 as extract_this_year

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 31
TEAM_ACRONYM_MAPPING = extract_this_year.TEAM_ACRONYM_MAPPING
NOVICE_TEAM_ACRONYM_MAPPING = extract_this_year.NOVICE_TEAM_ACRONYM_MAPPING
SENIOR_TEAM_ACRONYM_MAPPING = extract_this_year.SENIOR_TEAM_ACRONYM_MAPPING
TEAM_NAME_MAPPING: dict[str, int] = {
    "A-O KIDS WC": 8,
    "BADGER WC": 14,
    "BARTLETT HAWK WC": 16,
    "BATAVIA PINNERS": 10005,
    "BELLEVILLE LITTLE DE": 23,
    "BELVIDERE BANDITS": 24,
    "BENTON JR. WC": 26,
    "BETHALTO JR HIGH": 10118,
    "BISMARCK-HENNING WC": 28,
    "BOYS & GIRLS CLUB": 319,
    "BRADLEY BOURBONNAIS WRESTLING CLUB": 37,
    "BRONCO WRESTLING": 41,
    "CARY JR TROJAN MATME": 59,
    "CENTRALIA WC": 64,
    "CHAMPAIGN CHARGER KI": 10124,
    "CHENOA MAT CATS": 10011,
    "CHILLI DAWGS WC": 10014,
    "CROSSFACE WRESTLING": 10018,
    "CRYSTAL LAKE WIZARDS": 89,
    "CUMBERLAND YOUTH WC": 90,
    "DAKOTA WC": 92,
    "DECATUR WC": 10137,
    "DOWNERS GROVE COUGARS WC": 100,
    "DUNDEE HIGHLANDERS": 102,
    "DURAND-PECATONICA": 105,
    "EAST MOLINE PANTHER": 10121,
    "EDISON PANTHERS": 10131,
    "EDWARDSVILLE WC": 110,
    "ERIE MIDDLE SCHOOL W": 10025,
    "EVANSTON BLACK KAT WC": 10007,
    "FALCON YOUTH WC": 123,
    "FAW": 45270,
    "FBG": 45271,
    "FISHER WC": 130,
    "FOX VALLEY WC": 134,
    "FRANKLIN PARK RAIDER": 10138,
    "GALESBURG JR STREAKS": 10030,
    "GENERALS": 10144,
    "GENESEO WC": 10033,
    "GLEN ELLYN DUNGEON W": 10039,
    "GLENBARD EAST JR RAM": 147,
    "GRAPPLIN DEVILS WC": 153,
    "HARLEM COUGARS": 10041,
    "HIGHLAND BULLDOG JR": 168,
    "HIGHLAND PARK LITTLE GIANTS": 169,
    "HILL TRAILBLAZERS": 10143,
    "HILLSBORO JR TOPPERS": 170,
    "HINSDALE RED DEVILS": 171,
    "HONONEGAH KIDS WC": 173,
    "HOOPESTON AREA WC": 174,
    "HUSKIES WC": 10145,
    "ILLINI BLUFFS WC": 181,
    "JACKSONVILLE WC": 189,
    "JR BEARS WC": 10146,
    "JR GOLDEN EAGLES": 10050,
    "JR MAROON WC": 538,
    "JR ROCKET WRESTLING": 10052,
    "L-P CRUNCHING CAVS": 241,
    "LAKE VILLA LANCERS": 10141,
    "LAKELAND PREDATORS": 10057,
    "LAWRENCE COUNTY WC": 217,
    "LEMONT BEARS WC": 219,
    "LIL STORM YOUTH": 10060,
    "LIMESTONE YOUTH ROCK": 10061,
    "LITCHFIELD WRESTLING CLUB": 231,
    "LITTLE CELTIC WC": 233,
    "LITTLE REDBIRD WC": 10065,
    "MACOMB KIDS WRESTLIN": 243,
    "MAINE EAGLES WC": 245,
    "MARENGO WC": 248,
    "MARTINEZ FOX VALLEY": 250,
    "MATTOON YOUTH WC": 252,
    "METAMORA KIDS WC": 262,
    "METRO STALLIONS": 10142,
    "MIDWEST CENTRAL YOUT": 263,
    "MONTEGO MATMEN": 10117,
    "MONTICELLO YOUTH WRESTLING CLUB": 269,
    "MORTON YOUTH WRESTLI": 272,
    "MT VERNON LIONS": 275,
    "MT ZION WC": 276,
    "MURPHYSBORO WRESTLIN": 278,
    "NAPERVILLE EAGLES": 10133,
    "NAPERVILLE WC": 281,
    "OAK LAWN PD WILDCATS": 10075,
    "OAKWOOD WC": 299,
    "ORLAND PARK PIONEERS": 306,
    "OSWEGO COUGARS": 10136,
    "OSWEGO PANTHERS": 10076,
    "PANTHER CUB WC": 10079,
    "PINCKNEYVILLE JR": 10122,
    "PLAINFIELD WC": 326,
    "POLO WC": 327,
    "PONTIAC PYTHONS": 10082,
    "PR": 45272,
    "RAMS WC": 236,
    "REED CUSTER KNIGHTS": 10085,
    "RIVERBEND WC": 354,
    "RIVERDALE JR HIGH": 10153,
    "ROCHELLE WC": 358,
    "ROCK FALLS JUNIOR ROCKET WRESTLING": 360,
    "ROCKFORD WC": 364,
    "ROXANA KIDS WC": 371,
    "SANDWICH WC": 374,
    "SAUKEE YOUTH WC": 376,
    "SHARKS WC": 381,
    "SHELBYVILLE JR RAMS": 382,
    "SHERRARD JR WC": 383,
    "SJO YOUTH WRESTLING": 402,
    "SOUTHERN IL EAGLES": 10092,
    "SOUTHSIDE WC": 10140,
    "SPRINGFIELD CAPITALS": 397,
    "ST BEDE WC": 10095,
    "ST. CHARLES WC": 400,
    "STATELINE WILDCATS": 10097,
    "STC WC II": 10139,
    "STERLING NEWMAN JR": 10098,
    "STILLMAN VALLEY WC": 407,
    "TAYLORVILLE WC": 420,
    "TAZEWELL COUNTY KIDZ WC": 10135,
    "TEAM 1": 10134,
    "TIGER WC": 10103,
    "TIGERTOWN TANGLERS": 441,
    "TINLEY PARK BULLDOGS": 443,
    "TRI-CITY BRAVES": 10104,
    "TRIAD KNIGHTS WRESTLING CLUB": 452,
    "UNITY WRESTLING CLUB": 457,
    "VANDALIA JR WRESTLIN": 461,
    "VILLA LOMBARD COUGAR": 10109,
    "VILLA PARK YOUNG": 464,
    "VITTUM CATS": 466,
    "WASHINGTON JR PANTHE": 10110,
    "WEST FRANKFORT JR WC": 478,
    "WESTVILLE YOUTH WC": 482,
    "WHEATON BULLDOGS": 10120,
    "WHEATON MONROE EAGLE": 10114,
    "WOLFPAK WC": 490,
    "WRESTLING FACTORY": 10115,
    "YORKVILLE WC": 497,
}
NOVICE_EXTRA_TEAM_SCORES: dict[str, float] = {}
SENIOR_EXTRA_TEAM_SCORES: dict[str, float] = {}
BRACKET_ID_MAPPING: dict[tuple[bracket_utils.Division, int], int] = {
    ("novice", 62): 1,
    ("novice", 66): 2,
    ("novice", 70): 3,
    ("novice", 74): 4,
    ("novice", 79): 5,
    ("novice", 84): 6,
    ("novice", 89): 7,
    ("novice", 95): 8,
    ("novice", 101): 9,
    ("novice", 108): 10,
    ("novice", 115): 11,
    ("novice", 122): 12,
    ("novice", 130): 13,
    ("novice", 147): 14,
    ("novice", 166): 15,
    ("novice", 215): 16,
    ("senior", 70): 17,
    ("senior", 74): 18,
    ("senior", 79): 19,
    ("senior", 84): 20,
    ("senior", 89): 21,
    ("senior", 95): 22,
    ("senior", 101): 23,
    ("senior", 108): 24,
    ("senior", 115): 25,
    ("senior", 122): 26,
    ("senior", 130): 27,
    ("senior", 138): 28,
    ("senior", 147): 29,
    ("senior", 156): 30,
    ("senior", 166): 31,
    ("senior", 177): 32,
    ("senior", 189): 33,
    ("senior", 275): 34,
}


def main():
    with open(HERE / "extracted.2000.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    weight_classes = extracted.weight_classes
    bracket_utils.validate_acronym_mapping_names(
        weight_classes,
        (
            TEAM_ACRONYM_MAPPING,
            NOVICE_TEAM_ACRONYM_MAPPING,
            SENIOR_TEAM_ACRONYM_MAPPING,
        ),
        (NOVICE_EXTRA_TEAM_SCORES, SENIOR_EXTRA_TEAM_SCORES),
        TEAM_NAME_MAPPING,
    )
    unclassified = sorted(
        name for name, team_id in TEAM_NAME_MAPPING.items() if team_id < 0
    )
    if unclassified:
        raise ValueError("Some teams are unclassified", unclassified)

    bracket_utils.validate_acronym_mappings_divisions(
        weight_classes,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
    )

    start_id = 229
    mapped_competitors = bracket_utils.get_competitors_for_sql(
        start_id,
        weight_classes,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
    )

    start_id = 157
    bracket_utils.get_matches_for_sql(
        start_id,
        weight_classes,
        mapped_competitors.team_competitor_by_info,
        BRACKET_ID_MAPPING,
    )

    start_id = 1
    bracket_utils.tournament_team_sql(
        start_id,
        TOURNAMENT_ID,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
    )


if __name__ == "__main__":
    main()
