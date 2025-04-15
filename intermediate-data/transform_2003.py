# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import extract_2003 as extract_this_year

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 34
TEAM_SCORE_ID_START = 605
TEAM_ACRONYM_MAPPING = extract_this_year.TEAM_ACRONYM_MAPPING
NOVICE_TEAM_ACRONYM_MAPPING = extract_this_year.NOVICE_TEAM_ACRONYM_MAPPING
SENIOR_TEAM_ACRONYM_MAPPING = extract_this_year.SENIOR_TEAM_ACRONYM_MAPPING
TEAM_NAME_MAPPING: dict[str, int] = {
    "ALEDO BEAR COUNTRY WC": 10002,
    "ALLEMAN JR. PIONEER WC": 10003,
    "ARGENTA/OREANA KIDS CLUB": 8,
    "ARLINGTON CARDINALS": 9,
    "BADGER WC": 14,
    "BARRINGTON BRONCOS": 15,
    "BARTLETT HAWK WC": 16,
    "BATAVIA PINNERS": 10005,
    "BELLEVILLE LITTLE DEVILS": 23,
    "BELVIDERE BANDITS": 24,
    "BENTON JR. WC": 26,
    "BETHALTO BULLS WC": 10006,
    "BISMARCK-HENNING WC": 28,
    "BISON WC": 126,
    "BLACKHAWK WC": 30,
    "BLAZER KIDS": 10008,
    "BLOOMINGTON RAIDER WC": 32,
    "BRAWLERS WC": 39,
    "CARBONDALE WC": 53,
    "CARLINVILLE KIDS WC": 54,
    "CARY JR. TROJAN MATMEN": 59,
    "CHAMPAIGN KIDS WRESTLING": 65,
    "CHARLESTON WC": 69,
    "CHENOA MAT CATS": 10011,
    "CHICAGO BULLDOG WC": 10012,
    "CHILLI DAWGS WC": 10014,
    "CRIMSON HEAT WC": 10017,
    "CRYSTAL LAKE WIZARDS": 89,
    "CUMBERLAND YOUTH WC": 90,
    "DAKOTA WC": 92,
    "DEKALB WC": 96,
    "DIXON WC": 98,
    "DOWNERS GROVE COUGARS": 100,
    "DU-PEC CARNIVORES": 10020,
    "DUNDEE HIGHLANDERS": 102,
    "EDWARDSVILLE WC": 110,
    "EFFINGHAM YOUTH WC": 111,
    "EL PASO WC": 10022,
    "ELMHURST JR. DUKES": 10024,
    "FAIRMONT ROUGH RIDERS": 10027,
    "FALCON WC": 124,
    "FALCON YOUTH WC": 123,
    "FENWICK FALCONS WC": 10028,
    "FIGHTIN TITAN WC": 128,
    "FISHER WC": 130,
    "FORD HEIGHTS FALCONS": 10029,
    "FOX VALLEY WC": 134,
    "GALESBURG JR STREAKS": 10030,
    "GENESEO WC": 10033,
    "GENEVA WC": 10034,
    "GEORGETOWN YOUTH WC": 10036,
    "GLADIATORS": 10038,
    "GLENBARD EAST JR RAMS": 147,
    "GRANITE CITY JR WARRIORS": 10040,
    "GRAPPLIN' DEVILS WC": 153,
    "HARLEM COUGARS": 10041,
    "HARVEY TWISTERS": 162,
    "HERRIN WC": 10042,
    "HIGHLAND BULLDOG JR WC": 168,
    "HILLSBORO JR TOPPERS": 170,
    "HINSDALE RED DEVIL WC": 171,
    "HOFFMAN ESTATES WC": 172,
    "HONONEGAH KIDS WC": 173,
    "HOOPESTON AREA WC": 174,
    "JACKSONVILLE WC": 189,
    "JOLIET BOYS CLUB COBRAS": 10047,
    "JR. GOLDEN EAGLES": 10050,
    "JR. PANTHERS WRESTLING": 198,
    "JR. ROCKET WC": 10052,
    "JR. SAXONS WC": 10053,
    "JR. SENTINELS WC": 10054,
    "JUNIOR PIRATE WC": 201,
    "KNIGHTS WRESTLING": 206,
    "L-P CRUNCHING CAVS": 241,
    "LAKELAND PREDATORS": 10057,
    "LANCER WC": 216,
    "LAWRENCE COUNTY WC": 217,
    "LEMONT BEARS WC": 219,
    "LIL' ROUGHNECKS": 10059,
    "LIL' STORM YOUTH WRESTLING": 10060,
    "LIMESTONE YOUTH WC": 10061,
    "LINCOLN-WAY WC": 227,
    "LIONS WC": 229,
    "LITTLE BOILER WC": 232,
    "LITTLE CELTIC WC": 233,
    "LITTLE INDIANS WC": 10063,
    "LITTLE PANTHERS WC": 10064,
    "LITTLE REDBIRD WC": 10065,
    "LITTLE VIKINGS OF H-F": 10067,
    "LOCKPORT GATORS": 10068,
    "MACOMB LITTLE BOMBERS": 243,
    "MAINE EAGLES WC": 245,
    "MANTENO JR PANTHERS": 247,
    "MARENGO WC": 248,
    "MARTINEZ FOX VALLEY ELITE WC": 250,
    "MATTOON YOUTH WC": 252,
    "MENDOTA MAT MASTERS": 10072,
    "METAMORA KIDS WC": 262,
    "MIDWEST CENTRAL YOUTH": 263,
    "MOLINE WC": 268,
    "MORTON LITTLE MUSTANGS": 271,
    "MORTON YOUTH WC": 272,
    "MT. ZION WC": 276,
    "MURPHYSBORO WRESTLING": 278,
    "MUSTANG WC": 279,
    "NAPERVILLE WC": 281,
    "NOTRE DAME WC": 295,
    "OAK FOREST WARRIORS": 297,
    "OAK LAWN P.D. WILDCATS": 10075,
    "OAKWOOD WC": 299,
    "ORLAND PARK PIONEERS": 306,
    "OSWEGO PANTHERS": 10076,
    "PALATINE PANTHERS": 10078,
    "PANTHER CUB WC": 10079,
    "PANTHER WC": 346,
    "PLAINFIELD WC": 326,
    "POLO WC": 327,
    "PONTIAC PYTHONS": 10082,
    "QUINCY WC": 336,
    "RAIDER WC": 10084,
    "RAMS WC": 236,
    "RICH RATTLERS": 349,
    "RIVERBEND WC": 354,
    "RIVERDALE JR. HIGH": 10153,
    "ROCHELLE WC": 358,
    "ROCK ISLAND JR. ROCKS": 361,
    "ROCK ISLAND WC": 361,
    "ROCKFORD WC": 364,
    "ROXANA KIDS WRESTING CLUB": 371,
    "SAUKEE YOUTH WC": 376,
    "SAVANNA REDHAWKS": 10089,
    "SCN YOUTH WC": 377,
    "SENECA IRISH CADETS": 379,
    "SHAMROCK WC": 380,
    "SHELBYVILLE JR. RAMS WC": 382,
    "SILVER & BLACK ATTACK": 10090,
    "SJO YOUTH WC": 402,
    "SOUTHERN ILLINOIS EAGLES": 10092,
    "SPRINGFIELD CAPITALS": 397,
    "ST. CHARLES WC": 400,
    "ST. TARCISSUS": 403,
    "STILLMAN VALLEY WC": 407,
    "SYCAMORE WC": 418,
    "T-BIRD/RAIDER WRESTLING": 10099,
    "TAKEDOWN WC": 10100,
    "TAYLORVILLE WC": 420,
    "TIGER WC": 10103,
    "TIGERTOWN TANGLERS": 441,
    "TINLEY PARK BULLDOGS": 443,
    "TOMCAT WC": 448,
    "TREVIAN WC": 288,
    "TRIAD KNIGHTS": 452,
    "UNITED TOWNSHIP WC": 10107,
    "UNITY WC": 457,
    "VANDALIA JR WRESTLING": 461,
    "VILLA LOMBARD COUGARS": 10109,
    "VITTUM CATS": 466,
    "WARRENSBURG WC": 468,
    "WAUBONSIE WC": 473,
    "WEST CHICAGO SPIDER WC": 10112,
    "WEST FRANKFORT JR. WC": 478,
    "WESTVILLE YOUTH WC": 482,
    "WHEATON FRANKLIN WC": 10113,
    "WHEATON MONROE EAGLES": 10114,
    "WHEATON TIGER WC": 483,
    "WILMINGTON WC": 488,
    "WOLFPAK WC": 490,
    "WRESTLING FACTORY": 10115,
    "YORKVILLE WC": 497,
    "ZEE-BEE STINGERS": 501,
}
NOVICE_EXTRA_TEAM_SCORES: dict[str, float] = {
    "MORTON YOUTH WC": 0.0,
}
SENIOR_EXTRA_TEAM_SCORES: dict[str, float] = {
    "BARRINGTON BRONCOS": 0.0,
    "LIL' STORM YOUTH WRESTLING": 0.0,
    "LINCOLN-WAY WC": 0.0,
}
BRACKET_ID_MAPPING: dict[tuple[bracket_utils.Division, int], int] = {
    ("novice", 62): 104,
    ("novice", 66): 105,
    ("novice", 70): 106,
    ("novice", 74): 107,
    ("novice", 79): 108,
    ("novice", 84): 109,
    ("novice", 89): 110,
    ("novice", 95): 111,
    ("novice", 101): 112,
    ("novice", 108): 113,
    ("novice", 115): 114,
    ("novice", 122): 115,
    ("novice", 130): 116,
    ("novice", 147): 117,
    ("novice", 166): 118,
    ("novice", 215): 119,
    ("senior", 70): 120,
    ("senior", 74): 121,
    ("senior", 79): 122,
    ("senior", 84): 123,
    ("senior", 89): 124,
    ("senior", 95): 125,
    ("senior", 101): 126,
    ("senior", 108): 127,
    ("senior", 115): 128,
    ("senior", 122): 129,
    ("senior", 130): 130,
    ("senior", 138): 131,
    ("senior", 147): 132,
    ("senior", 156): 133,
    ("senior", 166): 134,
    ("senior", 177): 135,
    ("senior", 189): 136,
    ("senior", 215): 137,
    ("senior", 275): 138,
}


def main():
    with open(HERE / "extracted.2003.json", "rb") as file_obj:
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

    # NOTE: We just do team score **matching** for validation (but do not use
    #       the outputs).
    bracket_utils.team_scores_for_sql(
        "novice",
        TOURNAMENT_ID,
        extracted,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
        NOVICE_EXTRA_TEAM_SCORES,
    )
    bracket_utils.team_scores_for_sql(
        "senior",
        TOURNAMENT_ID,
        extracted,
        TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
        SENIOR_EXTRA_TEAM_SCORES,
    )

    start_id = 2625
    mapped_competitors = bracket_utils.get_competitors_for_sql(
        start_id,
        weight_classes,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
    )

    start_id = 4847
    bracket_utils.get_matches_for_sql(
        start_id,
        weight_classes,
        mapped_competitors.team_competitor_by_info,
        BRACKET_ID_MAPPING,
    )

    start_id = 759
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
