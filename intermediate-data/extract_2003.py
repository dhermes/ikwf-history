# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "FOX VALLEY WC": 151.5,
    "ORLAND PARK PIONEERS": 117.0,
    "VITTUM CATS": 106.0,
    "WRESTLING FACTORY": 105.5,
    "LITTLE CELTIC WC": 97.0,
    "MARTINEZ FOX VALLEY ELITE WC": 95.0,
    "ARLINGTON CARDINALS": 69.0,
    "CRYSTAL LAKE WIZARDS": 59.0,
    "TINLEY PARK BULLDOGS": 58.0,
    "HARVEY TWISTERS": 53.0,
    "BELVIDERE BANDITS": 49.0,
    "LINCOLN-WAY WC": 48.0,
    "LEMONT BEARS WC": 47.5,
    "BADGER WC": 46.0,
    "JR. GOLDEN EAGLES": 46.0,
    "BISON WC": 45.0,
    "DIXON WC": 44.0,
    "GLADIATORS": 39.5,
    "EDWARDSVILLE WC": 37.0,
    "PANTHER WC": 36.0,
    "CHILLI DAWGS WC": 35.5,
    "EFFINGHAM YOUTH WC": 35.0,
    "MOLINE WC": 35.0,
    "KNIGHTS WRESTLING": 33.0,
    "HINSDALE RED DEVIL WC": 32.0,
    "LAKELAND PREDATORS": 31.5,
    "DUNDEE HIGHLANDERS": 31.0,
    "ROCKFORD WC": 31.0,
    "STILLMAN VALLEY WC": 31.0,
    "SYCAMORE WC": 31.0,
    "BLACKHAWK WC": 29.0,
    "GLENBARD EAST JR RAMS": 29.0,
    "WHEATON MONROE EAGLES": 29.0,
    "CRIMSON HEAT WC": 28.0,
    "HARLEM COUGARS": 28.0,
    "BATAVIA PINNERS": 26.0,
    "MUSTANG WC": 26.0,
    "POLO WC": 25.0,
    "SPRINGFIELD CAPITALS": 25.0,
    "VILLA LOMBARD COUGARS": 25.0,
    "TIGER WC": 24.0,
    "BELLEVILLE LITTLE DEVILS": 23.0,
    "BRAWLERS WC": 23.0,
    "VANDALIA JR WRESTLING": 22.5,
    "JOLIET BOYS CLUB COBRAS": 22.0,
    "ARGENTA/OREANA KIDS CLUB": 20.0,
    "MATTOON YOUTH WC": 20.0,
    "OAK LAWN P.D. WILDCATS": 20.0,
    "CHENOA MAT CATS": 19.0,
    "DAKOTA WC": 19.0,
    "GRANITE CITY JR WARRIORS": 19.0,
    "SJO YOUTH WC": 18.5,
    "MAINE EAGLES WC": 18.0,
    "CUMBERLAND YOUTH WC": 17.0,
    "MT. ZION WC": 17.0,
    "L-P CRUNCHING CAVS": 16.0,
    "PLAINFIELD WC": 16.0,
    "RIVERBEND WC": 15.5,
    "DOWNERS GROVE COUGARS": 15.0,
    "MIDWEST CENTRAL YOUTH": 15.0,
    "WHEATON TIGER WC": 15.0,
    "FISHER WC": 14.0,
    "RIVERDALE JR. HIGH": 14.0,
    "TOMCAT WC": 14.0,
    "PANTHER CUB WC": 12.5,
    "WESTVILLE YOUTH WC": 12.0,
    "FALCON YOUTH WC": 11.0,
    "HOOPESTON AREA WC": 11.0,
    "SAUKEE YOUTH WC": 11.0,
    "WHEATON FRANKLIN WC": 11.0,
    "ROXANA KIDS WRESTING CLUB": 10.0,
    "BENTON JR. WC": 9.0,
    "JUNIOR PIRATE WC": 9.0,
    "UNITED TOWNSHIP WC": 9.0,
    "HONONEGAH KIDS WC": 8.5,
    "SHELBYVILLE JR. RAMS WC": 8.0,
    "DEKALB WC": 7.0,
    "FALCON WC": 7.0,
    "MORTON LITTLE MUSTANGS": 7.0,
    "T-BIRD/RAIDER WRESTLING": 7.0,
    "YORKVILLE WC": 7.0,
    "CHAMPAIGN KIDS WRESTLING": 6.0,
    "LITTLE VIKINGS OF H-F": 6.0,
    "OSWEGO PANTHERS": 6.0,
    "FENWICK FALCONS WC": 4.5,
    "GEORGETOWN YOUTH WC": 4.0,
    "HOFFMAN ESTATES WC": 4.0,
    "SHAMROCK WC": 4.0,
    "SOUTHERN ILLINOIS EAGLES": 4.0,
    "ST. CHARLES WC": 4.0,
    "WAUBONSIE WC": 4.0,
    "MURPHYSBORO WRESTLING": 3.5,
    "WEST CHICAGO SPIDER WC": 3.0,
    "BETHALTO BULLS WC": 2.0,
    "GENESEO WC": 2.0,
    "TRIAD KNIGHTS": 2.0,
    "WOLFPAK WC": 2.0,
    "WARRENSBURG WC": 1.0,
    "ROCK ISLAND JR. ROCKS": 0.5,
    "ALEDO BEAR COUNTRY WC": 0.0,
    "BLOOMINGTON RAIDER WC": 0.0,
    "CARBONDALE WC": 0.0,
    "CARLINVILLE KIDS WC": 0.0,
    "EL PASO WC": 0.0,
    "GALESBURG JR STREAKS": 0.0,
    "GRAPPLIN' DEVILS WC": 0.0,
    "HIGHLAND BULLDOG JR WC": 0.0,
    "HILLSBORO JR TOPPERS": 0.0,
    "JR. PANTHERS WRESTLING": 0.0,
    "JR. SAXONS WC": 0.0,
    "LAWRENCE COUNTY WC": 0.0,
    "LIL' ROUGHNECKS": 0.0,
    "LITTLE INDIANS WC": 0.0,
    "LITTLE PANTHERS WC": 0.0,
    "MACOMB LITTLE BOMBERS": 0.0,
    "MANTENO JR PANTHERS": 0.0,
    "MARENGO WC": 0.0,
    "MENDOTA MAT MASTERS": 0.0,
    "METAMORA KIDS WC": 0.0,
    "MORTON YOUTH WC": 0.0,
    "NAPERVILLE WC": 0.0,
    "OAKWOOD WC": 0.0,
    "SAVANNA REDHAWKS": 0.0,
    "SILVER & BLACK ATTACK": 0.0,
    "ST. TARCISSUS": 0.0,
    "TAYLORVILLE WC": 0.0,
    "WILMINGTON WC": 0.0,
    "LIMESTONE YOUTH WC": -1.0,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "MARTINEZ FOX VALLEY ELITE WC": 300.5,
    "VITTUM CATS": 183.5,
    "HARVEY TWISTERS": 160.0,
    "LITTLE CELTIC WC": 113.0,
    "WRESTLING FACTORY": 113.0,
    "ORLAND PARK PIONEERS": 88.0,
    "EDWARDSVILLE WC": 83.0,
    "BETHALTO BULLS WC": 81.5,
    "TINLEY PARK BULLDOGS": 73.5,
    "GRANITE CITY JR WARRIORS": 64.0,
    "LEMONT BEARS WC": 61.0,
    "BLACKHAWK WC": 59.0,
    "DAKOTA WC": 59.0,
    "GENESEO WC": 57.0,
    "KNIGHTS WRESTLING": 51.0,
    "HINSDALE RED DEVIL WC": 50.0,
    "BRAWLERS WC": 49.0,
    "WHEATON TIGER WC": 47.0,
    "PONTIAC PYTHONS": 41.0,
    "PLAINFIELD WC": 40.0,
    "JR. PANTHERS WRESTLING": 39.0,
    "HARLEM COUGARS": 38.0,
    "PANTHER WC": 37.0,
    "CRYSTAL LAKE WIZARDS": 36.0,
    "JOLIET BOYS CLUB COBRAS": 36.0,
    "SJO YOUTH WC": 36.0,
    "BELLEVILLE LITTLE DEVILS": 33.0,
    "UNITED TOWNSHIP WC": 33.0,
    "ARGENTA/OREANA KIDS CLUB": 31.5,
    "CHAMPAIGN KIDS WRESTLING": 31.5,
    "MURPHYSBORO WRESTLING": 31.5,
    "BISMARCK-HENNING WC": 30.0,
    "CUMBERLAND YOUTH WC": 30.0,
    "ROXANA KIDS WRESTING CLUB": 30.0,
    "CHICAGO BULLDOG WC": 29.5,
    "GLENBARD EAST JR RAMS": 28.0,
    "VANDALIA JR WRESTLING": 28.0,
    "BATAVIA PINNERS": 26.0,
    "L-P CRUNCHING CAVS": 26.0,
    "NAPERVILLE WC": 26.0,
    "SCN YOUTH WC": 25.0,
    "ALEDO BEAR COUNTRY WC": 23.5,
    "GLADIATORS": 22.0,
    "LIONS WC": 22.0,
    "EFFINGHAM YOUTH WC": 21.0,
    "POLO WC": 21.0,
    "SAUKEE YOUTH WC": 21.0,
    "TIGERTOWN TANGLERS": 21.0,
    "METAMORA KIDS WC": 19.0,
    "ST. CHARLES WC": 19.0,
    "DIXON WC": 18.0,
    "DUNDEE HIGHLANDERS": 18.0,
    "LITTLE VIKINGS OF H-F": 18.0,
    "WHEATON MONROE EAGLES": 18.0,
    "ARLINGTON CARDINALS": 17.5,
    "NOTRE DAME WC": 17.0,
    "T-BIRD/RAIDER WRESTLING": 17.0,
    "MATTOON YOUTH WC": 16.0,
    "MIDWEST CENTRAL YOUTH": 15.0,
    "PANTHER CUB WC": 15.0,
    "VILLA LOMBARD COUGARS": 14.0,
    "FALCON YOUTH WC": 13.0,
    "FALCON WC": 12.0,
    "SOUTHERN ILLINOIS EAGLES": 12.0,
    "ALLEMAN JR. PIONEER WC": 11.0,
    "HERRIN WC": 11.0,
    "JR. ROCKET WC": 11.0,
    "YORKVILLE WC": 11.0,
    "CARY JR. TROJAN MATMEN": 10.0,
    "TAKEDOWN WC": 10.0,
    "BISON WC": 9.0,
    "HIGHLAND BULLDOG JR WC": 9.0,
    "DU-PEC CARNIVORES": 8.0,
    "ELMHURST JR. DUKES": 8.0,
    "LITTLE REDBIRD WC": 8.0,
    "UNITY WC": 8.0,
    "WOLFPAK WC": 8.0,
    "LOCKPORT GATORS": 7.0,
    "MOLINE WC": 7.0,
    "OSWEGO PANTHERS": 6.0,
    "MAINE EAGLES WC": 5.0,
    "WESTVILLE YOUTH WC": 5.0,
    "FISHER WC": 4.0,
    "JACKSONVILLE WC": 4.0,
    "LANCER WC": 4.0,
    "MANTENO JR PANTHERS": 4.0,
    "RIVERDALE JR. HIGH": 4.0,
    "WHEATON FRANKLIN WC": 4.0,
    "CARBONDALE WC": 3.5,
    "RAMS WC": 3.5,
    "JR. GOLDEN EAGLES": 3.0,
    "MORTON LITTLE MUSTANGS": 3.0,
    "OAKWOOD WC": 3.0,
    "SAVANNA REDHAWKS": 3.0,
    "CHILLI DAWGS WC": 2.0,
    "GRAPPLIN' DEVILS WC": 2.0,
    "HOOPESTON AREA WC": 2.0,
    "LAWRENCE COUNTY WC": 2.0,
    "MUSTANG WC": 2.0,
    "RAIDER WC": 2.0,
    "SENECA IRISH CADETS": 2.0,
    "SPRINGFIELD CAPITALS": 2.0,
    "STILLMAN VALLEY WC": 2.0,
    "SYCAMORE WC": 2.0,
    "HONONEGAH KIDS WC": 1.5,
    "PALATINE PANTHERS": 1.0,
    "BADGER WC": 0.0,
    "BARRINGTON BRONCOS": 0.0,
    "BARTLETT HAWK WC": 0.0,
    "BENTON JR. WC": 0.0,
    "BLAZER KIDS": 0.0,
    "CHARLESTON WC": 0.0,
    "CHENOA MAT CATS": 0.0,
    "DEKALB WC": 0.0,
    "FAIRMONT ROUGH RIDERS": 0.0,
    "FIGHTIN TITAN WC": 0.0,
    "FORD HEIGHTS FALCONS": 0.0,
    "GENEVA WC": 0.0,
    "HOFFMAN ESTATES WC": 0.0,
    "JR. SAXONS WC": 0.0,
    "JR. SENTINELS WC": 0.0,
    "LIL' STORM YOUTH WRESTLING": 0.0,
    "LINCOLN-WAY WC": 0.0,
    "LITTLE BOILER WC": 0.0,
    "MARENGO WC": 0.0,
    "MENDOTA MAT MASTERS": 0.0,
    "OAK FOREST WARRIORS": 0.0,
    "OAK LAWN P.D. WILDCATS": 0.0,
    "QUINCY WC": 0.0,
    "RICH RATTLERS": 0.0,
    "ROCHELLE WC": 0.0,
    "TIGER WC": 0.0,
    "TREVIAN WC": 0.0,
    "TRIAD KNIGHTS": 0.0,
    "WAUBONSIE WC": 0.0,
    "WEST FRANKFORT JR. WC": 0.0,
    "ZEE-BEE STINGERS": 0.0,
    "FOX VALLEY WC": -1.0,
    "LIMESTONE YOUTH WC": -1.0,
    "RIVERBEND WC": -1.0,
    "WARRENSBURG WC": -1.0,
    "FENWICK FALCONS WC": -3.0,
    "ROCK ISLAND WC": -3.0,
}
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("ANTHONY RICH JR", "L-P CRUNCHING CAVS"): bracket_utils.Competitor(
        full_name="ANTHONY RICH JR",
        first_name="ANTHONY",
        last_name="RICH",
        team_full="L-P CRUNCHING CAVS",
    ),
    ("BJ FUTRELL II", "HARVEY TWISTERS"): bracket_utils.Competitor(
        full_name="BJ FUTRELL II",
        first_name="BJ",
        last_name="FUTRELL",
        team_full="HARVEY TWISTERS",
    ),
    ("CARL FORESIDE, JR.", "GLADIATORS"): bracket_utils.Competitor(
        full_name="CARL FORESIDE, JR.",
        first_name="CARL",
        last_name="FORESIDE",
        team_full="GLADIATORS",
    ),
    ("CASEY MC MURRAY", "LIONS WC"): bracket_utils.Competitor(
        full_name="CASEY MC MURRAY",
        first_name="CASEY",
        last_name="MC MURRAY",
        team_full="LIONS WC",
    ),
    ("DWIGHT MC CALL", "ROCK ISLAND WC"): bracket_utils.Competitor(
        full_name="DWIGHT MC CALL",
        first_name="DWIGHT",
        last_name="MC CALL",
        team_full="ROCK ISLAND WC",
    ),
    ("GINO DE FRANCISCO", "HOFFMAN ESTATES WC"): bracket_utils.Competitor(
        full_name="GINO DE FRANCISCO",
        first_name="GINO",
        last_name="DE FRANCISCO",
        team_full="HOFFMAN ESTATES WC",
    ),
    ("JAMES VAN SOMEREN", "WHEATON FRANKLIN WC"): bracket_utils.Competitor(
        full_name="JAMES VAN SOMEREN",
        first_name="JAMES",
        last_name="VAN SOMEREN",
        team_full="WHEATON FRANKLIN WC",
    ),
    ("JOSHUA VAN BEHREN", "UNITY WC"): bracket_utils.Competitor(
        full_name="JOSHUA VAN BEHREN",
        first_name="JOSHUA",
        last_name="VAN BEHREN",
        team_full="UNITY WC",
    ),
    ("MARCUS MC CALL", "ROCK ISLAND JR. ROCKS"): bracket_utils.Competitor(
        full_name="MARCUS MC CALL",
        first_name="MARCUS",
        last_name="MC CALL",
        team_full="ROCK ISLAND JR. ROCKS",
    ),
    ("MICHAEL MATOZZI, JR.", "OSWEGO PANTHERS"): bracket_utils.Competitor(
        full_name="MICHAEL MATOZZI, JR.",
        first_name="MICHAEL",
        last_name="MATOZZI",
        team_full="OSWEGO PANTHERS",
    ),
    ("REGINALD WILSON JR", "FORD HEIGHTS FALCONS"): bracket_utils.Competitor(
        full_name="REGINALD WILSON JR",
        first_name="REGINALD",
        last_name="WILSON",
        team_full="FORD HEIGHTS FALCONS",
    ),
    ("ROBERT PROVAX III", "NOTRE DAME WC"): bracket_utils.Competitor(
        full_name="ROBERT PROVAX III",
        first_name="ROBERT",
        last_name="PROVAX",
        team_full="NOTRE DAME WC",
    ),
    ("RONALD REEVES JR", "TRIAD KNIGHTS"): bracket_utils.Competitor(
        full_name="RONALD REEVES JR",
        first_name="RONALD",
        last_name="REEVES",
        team_full="TRIAD KNIGHTS",
    ),
    ("T. J. WARNER", "HOOPESTON AREA WC"): bracket_utils.Competitor(
        full_name="T. J. WARNER",
        first_name="T. J.",
        last_name="WARNER",
        team_full="HOOPESTON AREA WC",
    ),
}
TEAM_SCORE_EXCEPTIONS: dict[tuple[bracket_utils.Division, str], float] = {}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ALE": "ALEDO BEAR COUNTRY WC",
    "ARG": "ARGENTA/OREANA KIDS CLUB",
    "ARL": "ARLINGTON CARDINALS",
    "BAD": "BADGER WC",
    "BAT": "BATAVIA PINNERS",
    "BEL": "BELLEVILLE LITTLE DEVILS",
    "BEN": "BENTON JR. WC",
    "BET": "BETHALTO BULLS WC",
    "BIO": "BISON WC",
    "BLA": "BLACKHAWK WC",
    "BRA": "BRAWLERS WC",
    "CAR": "CARBONDALE WC",
    "CHA": "CHAMPAIGN KIDS WRESTLING",
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLI DAWGS WC",
    "CRY": "CRYSTAL LAKE WIZARDS",
    "CUM": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DEK": "DEKALB WC",
    "DIX": "DIXON WC",
    "DUN": "DUNDEE HIGHLANDERS",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "FAC": "FALCON YOUTH WC",
    "FAL": "FALCON WC",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "GEE": "GENESEO WC",
    "GLA": "GLADIATORS",
    "GLN": "GLENBARD EAST JR RAMS",
    "GRA": "GRANITE CITY JR WARRIORS",
    "GRP": "GRAPPLIN' DEVILS WC",
    "HAE": "HARVEY TWISTERS",
    "HAR": "HARLEM COUGARS",
    "HIG": "HIGHLAND BULLDOG JR WC",
    "HIN": "HINSDALE RED DEVIL WC",
    "HOF": "HOFFMAN ESTATES WC",
    "HON": "HONONEGAH KIDS WC",
    "HOO": "HOOPESTON AREA WC",
    "JOL": "JOLIET BOYS CLUB COBRAS",
    "JRG": "JR. GOLDEN EAGLES",
    "JRP": "JR. PANTHERS WRESTLING",
    "JRX": "JR. SAXONS WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAW": "LAWRENCE COUNTY WC",
    "LEM": "LEMONT BEARS WC",
    "LIC": "LITTLE CELTIC WC",
    "LIV": "LITTLE VIKINGS OF H-F",
    "LPC": "L-P CRUNCHING CAVS",
    "MAF": "MARTINEZ FOX VALLEY ELITE WC",
    "MAI": "MAINE EAGLES WC",
    "MAN": "MANTENO JR PANTHERS",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "MEN": "MENDOTA MAT MASTERS",
    "MET": "METAMORA KIDS WC",
    "MID": "MIDWEST CENTRAL YOUTH",
    "MOL": "MOLINE WC",
    "MOT": "MORTON LITTLE MUSTANGS",
    "MUR": "MURPHYSBORO WRESTLING",
    "MUS": "MUSTANG WC",
    "NAP": "NAPERVILLE WC",
    "OAL": "OAK LAWN P.D. WILDCATS",
    "OAW": "OAKWOOD WC",
    "ORL": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTHERS",
    "PAN": "PANTHER CUB WC",
    "PAT": "PANTHER WC",
    "PLA": "PLAINFIELD WC",
    "POL": "POLO WC",
    "RIV": "RIVERBEND WC",
    "RJH": "RIVERDALE JR. HIGH",
    "ROX": "ROXANA KIDS WRESTLING CLUB",
    "SAU": "SAUKEE YOUTH WC",
    "SAV": "SAVANNA REDHAWKS",
    "SJO": "SJO YOUTH WC",
    "SOU": "SOUTHERN ILLINOIS EAGLES",
    "SPR": "SPRINGFIELD CAPITALS",
    "STC": "ST. CHARLES WC",
    "STI": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE WC",
    "TBI": "T-BIRD/RAIDER WRESTLING",
    "TIG": "TIGER WC",
    "TIN": "TINLEY PARK BULLDOGS",
    "TRI": "TRIAD KNIGHTS",
    "UNT": "UNITED TOWNSHIP WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAR": "WARRENSBURG WC",
    "WAU": "WAUBONSIE WC",
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
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "BEV": "BELVIDERE BANDITS",
    "BLO": "BLOOMINGTON RAIDER WC",
    "CAL": "CARLINVILLE KIDS WC",
    "CRI": "CRIMSON HEAT WC",
    "DOW": "DOWNERS GROVE COUGARS",
    "ELP": "EL PASO WC",
    "GAL": "GALESBURG JR STREAKS",
    "GEO": "GEORGETOWN YOUTH WC",
    "HIL": "HILLSBORO JR TOPPERS",
    "JUP": "JUNIOR PIRATE WC",
    "LAE": "LAKELAND PREDATORS",
    "LII": "LITTLE INDIANS WC",
    "LIL": "LIL' ROUGHNECKS",
    "LIN": "LINCOLN-WAY WC",
    "LIP": "LITTLE PANTHERS WC",
    "MAC": "MACOMB LITTLE BOMBERS",
    "MTZ": "MT. ZION WC",
    "ROF": "ROCKFORD WC",
    "ROK": "ROCK ISLAND JR. ROCKS",
    "SHA": "SHAMROCK WC",
    "SHE": "SHELBYVILLE JR. RAMS WC",
    "SIL": "SILVER & BLACK ATTACK",
    "STT": "ST. TARCISSUS",
    "TAY": "TAYLORVILLE WC",
    "TOM": "TOMCAT WC",
    "WEC": "WEST CHICAGO SPIDER WC",
    "WIL": "WILMINGTON WC",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ALL": "ALLEMAN JR. PIONEER WC",
    "BAH": "BARTLETT HAWK WC",
    "BIS": "BISMARCK-HENNING WC",
    "BLK": "BLAZER KIDS",
    "CAY": "CARY JR. TROJAN MATMEN",
    "CHB": "CHICAGO BULLDOG WC",
    "CHR": "CHARLESTON WC",
    "DUP": "DU-PEC CARNIVORES",
    "ELM": "ELMHURST JR. DUKES",
    "FAI": "FAIRMONT ROUGH RIDERS",
    "FIG": "FIGHTIN TITAN WC",
    "FOR": "FORD HEIGHTS FALCONS",
    "GEN": "GENEVA WC",
    "HER": "HERRIN WC",
    "JAC": "JACKSONVILLE WC",
    "JRR": "JR. ROCKET WC",
    "JRS": "JR. SENTINELS WC",
    "LAN": "LANCER WC",
    "LIB": "LITTLE BOILER WC",
    "LIM": "LIMESTONE YOUTH WC",
    "LIO": "LIONS WC",
    "LIR": "LITTLE REDBIRD WC",
    "LOC": "LOCKPORT GATORS",
    "NOT": "NOTRE DAME WC",
    "OAK": "OAK FOREST WARRIORS",
    "PAL": "PALATINE PANTHERS",
    "PON": "PONTIAC PYTHONS",
    "QUI": "QUINCY WC",
    "RAI": "RAIDER WC",
    "RAM": "RAMS WC",
    "RIC": "RICH RATTLERS",
    "ROC": "ROCHELLE WC",
    "ROK": "ROCK ISLAND WC",
    "SCN": "SCN YOUTH WC",
    "SEN": "SENECA IRISH CADETS",
    "TAK": "TAKEDOWN WC",
    "TRE": "TREVIAN WC",
    "TTT": "TIGERTOWN TANGLERS",
    "UNI": "UNITY WC",
    "WES": "WEST FRANKFORT JR. WC",
    "ZEE": "ZEE-BEE STINGERS",
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
    cleaned = value.strip().rstrip("+").strip("-")
    if cleaned == "Bye":
        return None

    name, team = cleaned.rsplit(" ", 1)
    team = team.strip()

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return bracket_utils.CompetitorRaw(
        name=name, team_full=_get_team_full(team, division)
    )


def parse_bout_result(value: str) -> str:
    if value.endswith("|"):
        value = value[:-1]

    if not value.endswith(" ") or not value.startswith(" "):
        raise ValueError("Invariant violation", value)

    parts = value.split("Bout:")
    if len(parts) > 2:
        raise ValueError("Invariant violation", value)

    return parts[0].strip()


def parse_bout_number(value: str) -> int:
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].split("Bout:")
    if len(parts) != 2:
        raise ValueError("Invariant violation", value)

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
    top_competitor_str = championship_lines[start_index][:31]
    if top_competitor_str != EMPTY_SLOT:
        top_competitor = parse_competitor_full(top_competitor_str, division)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:31]
    if bottom_competitor_str != EMPTY_SLOT:
        bottom_competitor = parse_competitor_full(bottom_competitor_str, division)

    bout_number_str = championship_lines[start_index + 1][:31]
    bout_number = None
    if bout_number_str != EMPTY_SLOT:
        bout_number = parse_bout_number(bout_number_str)

    result_str = championship_lines[start_index + 2][31:62]
    result = ""
    if result_str != EMPTY_SLOT:
        result = parse_bout_result(result_str)

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
    with open(_HERE / "2003" / division / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre: list[bs4.Tag] = soup.find_all("pre")
    if len(all_pre) != 4:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre, seventh_place_pre = all_pre
    championship_text = championship_pre.text

    championship_lines = championship_text.lstrip("\n").split("\n")
    consolation_lines = consolation_pre.text.lstrip("\n").split("\n")
    fifth_place_lines = fifth_place_pre.text.lstrip("\n").split("\n")
    seventh_place_lines = seventh_place_pre.text.lstrip("\n").split("\n")

    parse_competitor = functools.partial(parse_competitor_full, division=division)

    matches = [
        bracket_utils.MatchRaw(
            match_slot="championship_r32_01",
            top_competitor=parse_competitor(championship_lines[0][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            1,
            "championship_r32_02",
            "championship_r16_01",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            5,
            "championship_r32_03",
            "championship_r16_02",
            "top",
            division,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_04",
            top_competitor=parse_competitor(championship_lines[8][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_05",
            top_competitor=parse_competitor(championship_lines[10][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            11,
            "championship_r32_06",
            "championship_r16_03",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            15,
            "championship_r32_07",
            "championship_r16_04",
            "top",
            division,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_08",
            top_competitor=parse_competitor(championship_lines[18][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_09",
            top_competitor=parse_competitor(championship_lines[20][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            21,
            "championship_r32_10",
            "championship_r16_05",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            25,
            "championship_r32_11",
            "championship_r16_06",
            "top",
            division,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_12",
            top_competitor=parse_competitor(championship_lines[28][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_13",
            top_competitor=parse_competitor(championship_lines[30][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            31,
            "championship_r32_14",
            "championship_r16_07",
            "bottom",
            division,
        ),
        maybe_r32_empty_bye(
            championship_lines,
            35,
            "championship_r32_15",
            "championship_r16_08",
            "top",
            division,
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r32_16",
            top_competitor=parse_competitor(championship_lines[38][31:62]),
            bottom_competitor=None,
            result="Bye",
            bout_number=None,
            winner=None,
            winner_from=None,
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_r16_01",
            top_competitor=parse_competitor(championship_lines[0][31:62]),
            bottom_competitor=parse_competitor(championship_lines[2][31:62]),
            result=parse_bout_result(championship_lines[2][62:93]),
            bout_number=parse_bout_number(championship_lines[1][31:62]),
            winner=None,
            winner_from=("championship_quarter_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_02",
            top_competitor=parse_competitor(championship_lines[6][31:62]),
            bottom_competitor=parse_competitor(championship_lines[8][31:62]),
            result=parse_bout_result(championship_lines[8][62:93]),
            bout_number=parse_bout_number(championship_lines[7][31:62]),
            winner=None,
            winner_from=("championship_quarter_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_03",
            top_competitor=parse_competitor(championship_lines[10][31:62]),
            bottom_competitor=parse_competitor(championship_lines[12][31:62]),
            result=parse_bout_result(championship_lines[12][62:93]),
            bout_number=parse_bout_number(championship_lines[11][31:62]),
            winner=None,
            winner_from=("championship_quarter_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_04",
            top_competitor=parse_competitor(championship_lines[16][31:62]),
            bottom_competitor=parse_competitor(championship_lines[18][31:62]),
            result=parse_bout_result(championship_lines[18][62:93]),
            bout_number=parse_bout_number(championship_lines[17][31:62]),
            winner=None,
            winner_from=("championship_quarter_02", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_05",
            top_competitor=parse_competitor(championship_lines[20][31:62]),
            bottom_competitor=parse_competitor(championship_lines[22][31:62]),
            result=parse_bout_result(championship_lines[22][62:93]),
            bout_number=parse_bout_number(championship_lines[21][31:62]),
            winner=None,
            winner_from=("championship_quarter_03", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_06",
            top_competitor=parse_competitor(championship_lines[26][31:62]),
            bottom_competitor=parse_competitor(championship_lines[28][31:62]),
            result=parse_bout_result(championship_lines[28][62:93]),
            bout_number=parse_bout_number(championship_lines[27][31:62]),
            winner=None,
            winner_from=("championship_quarter_03", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_07",
            top_competitor=parse_competitor(championship_lines[30][31:62]),
            bottom_competitor=parse_competitor(championship_lines[32][31:62]),
            result=parse_bout_result(championship_lines[32][62:93]),
            bout_number=parse_bout_number(championship_lines[31][31:62]),
            winner=None,
            winner_from=("championship_quarter_04", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_r16_08",
            top_competitor=parse_competitor(championship_lines[36][31:62]),
            bottom_competitor=parse_competitor(championship_lines[38][31:62]),
            result=parse_bout_result(championship_lines[38][62:93] + " "),
            bout_number=parse_bout_number(championship_lines[37][31:62]),
            winner=None,
            winner_from=("championship_quarter_04", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_01",
            top_competitor=parse_competitor(championship_lines[1][62:93]),
            bottom_competitor=parse_competitor(championship_lines[7][62:93]),
            result=parse_bout_result(championship_lines[5][93:124]),
            bout_number=parse_bout_number(championship_lines[4][62:93]),
            winner=None,
            winner_from=("championship_semi_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_02",
            top_competitor=parse_competitor(championship_lines[11][62:93]),
            bottom_competitor=parse_competitor(championship_lines[17][62:93]),
            result=parse_bout_result(championship_lines[15][93:124]),
            bout_number=parse_bout_number(championship_lines[14][62:93]),
            winner=None,
            winner_from=("championship_semi_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_03",
            top_competitor=parse_competitor(championship_lines[21][62:93]),
            bottom_competitor=parse_competitor(championship_lines[27][62:93]),
            result=parse_bout_result(championship_lines[25][93:124]),
            bout_number=parse_bout_number(championship_lines[24][62:93]),
            winner=None,
            winner_from=("championship_semi_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_quarter_04",
            top_competitor=parse_competitor(championship_lines[31][62:93]),
            bottom_competitor=parse_competitor(championship_lines[37][62:93]),
            result=parse_bout_result(championship_lines[35][93:124] + " "),
            bout_number=parse_bout_number(championship_lines[34][62:93]),
            winner=None,
            winner_from=("championship_semi_02", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_semi_01",
            top_competitor=parse_competitor(championship_lines[4][93:124]),
            bottom_competitor=parse_competitor(championship_lines[14][93:124]),
            result=parse_bout_result(championship_lines[10][124:155]),
            bout_number=parse_bout_number(championship_lines[9][93:124]),
            winner=None,
            winner_from=("championship_first_place", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="championship_semi_02",
            top_competitor=parse_competitor(championship_lines[24][93:124]),
            bottom_competitor=parse_competitor(championship_lines[34][93:124]),
            result=parse_bout_result(championship_lines[30][124:155] + " "),
            bout_number=parse_bout_number(championship_lines[29][93:124]),
            winner=None,
            winner_from=("championship_first_place", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="championship_first_place",
            top_competitor=parse_competitor(championship_lines[9][124:155]),
            bottom_competitor=parse_competitor(championship_lines[29][124:155]),
            result=parse_bout_result(championship_lines[21][155:] + " "),
            bout_number=parse_bout_number(championship_lines[19][124:155]),
            winner=parse_competitor(championship_lines[19][155:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_01",
            top_competitor=parse_competitor(consolation_lines[0][:31]),
            bottom_competitor=parse_competitor(consolation_lines[2][:31]),
            result=parse_bout_result(consolation_lines[2][31:62]),
            bout_number=parse_bout_number(consolation_lines[1][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_02",
            top_competitor=parse_competitor(consolation_lines[4][:31]),
            bottom_competitor=parse_competitor(consolation_lines[6][:31]),
            result=parse_bout_result(consolation_lines[6][31:62]),
            bout_number=parse_bout_number(consolation_lines[5][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_03",
            top_competitor=parse_competitor(consolation_lines[8][:31]),
            bottom_competitor=parse_competitor(consolation_lines[10][:31]),
            result=parse_bout_result(consolation_lines[10][31:62]),
            bout_number=parse_bout_number(consolation_lines[9][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_03", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round3_04",
            top_competitor=parse_competitor(consolation_lines[12][:31]),
            bottom_competitor=parse_competitor(consolation_lines[14][:31]),
            result=parse_bout_result(consolation_lines[14][31:62]),
            bout_number=parse_bout_number(consolation_lines[13][:31]),
            winner=None,
            winner_from=("consolation_round4_blood_04", "top"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_01",
            top_competitor=parse_competitor(consolation_lines[1][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[3][31:62]),
            result=parse_bout_result(consolation_lines[3][62:93]),
            bout_number=parse_bout_number(consolation_lines[2][31:62]),
            winner=None,
            winner_from=("consolation_round5_01", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_02",
            top_competitor=parse_competitor(consolation_lines[5][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[7][31:62]),
            result=parse_bout_result(consolation_lines[7][62:93]),
            bout_number=parse_bout_number(consolation_lines[6][31:62]),
            winner=None,
            winner_from=("consolation_round5_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_03",
            top_competitor=parse_competitor(consolation_lines[9][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[11][31:62]),
            result=parse_bout_result(consolation_lines[11][62:93]),
            bout_number=parse_bout_number(consolation_lines[10][31:62]),
            winner=None,
            winner_from=("consolation_round5_02", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round4_blood_04",
            top_competitor=parse_competitor(consolation_lines[13][31:62]),
            bottom_competitor=parse_competitor(consolation_lines[15][31:62]),
            result=parse_bout_result(consolation_lines[15][62:93] + " "),
            bout_number=parse_bout_number(consolation_lines[14][31:62]),
            winner=None,
            winner_from=("consolation_round5_02", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round5_01",
            top_competitor=parse_competitor(consolation_lines[2][62:93]),
            bottom_competitor=parse_competitor(consolation_lines[6][62:93]),
            result=parse_bout_result(consolation_lines[5][93:124]),
            bout_number=parse_bout_number(consolation_lines[4][62:93]),
            winner=None,
            winner_from=("consolation_round6_semi_01", "bottom"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round5_02",
            top_competitor=parse_competitor(consolation_lines[10][62:93]),
            bottom_competitor=parse_competitor(consolation_lines[14][62:93]),
            result=parse_bout_result(consolation_lines[13][93:124] + " "),
            bout_number=parse_bout_number(consolation_lines[12][62:93]),
            winner=None,
            winner_from=("consolation_round6_semi_02", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_round6_semi_01",
            top_competitor=parse_competitor(consolation_lines[0][93:124]),
            bottom_competitor=parse_competitor(consolation_lines[4][93:124]),
            result=parse_bout_result(consolation_lines[3][124:155]),
            bout_number=parse_bout_number(consolation_lines[2][93:124]),
            winner=None,
            winner_from=("consolation_third_place", "top"),
        ),
        bracket_utils.MatchRaw(
            match_slot="consolation_round6_semi_02",
            top_competitor=parse_competitor(consolation_lines[8][93:124]),
            bottom_competitor=parse_competitor(consolation_lines[12][93:124]),
            result=parse_bout_result(consolation_lines[11][124:155] + " "),
            bout_number=parse_bout_number(consolation_lines[10][93:124]),
            winner=None,
            winner_from=("consolation_third_place", "bottom"),
        ),
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_third_place",
            top_competitor=parse_competitor(consolation_lines[2][124:155]),
            bottom_competitor=parse_competitor(consolation_lines[10][124:155]),
            result=parse_bout_result(consolation_lines[8][155:] + " "),
            bout_number=parse_bout_number(consolation_lines[6][124:155]),
            winner=parse_competitor(consolation_lines[6][155:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_fifth_place",
            top_competitor=parse_competitor(fifth_place_lines[0][:31]),
            bottom_competitor=parse_competitor(fifth_place_lines[2][:31]),
            result=parse_bout_result(fifth_place_lines[3][31:] + " "),
            bout_number=parse_bout_number(fifth_place_lines[1][:31]),
            winner=parse_competitor(fifth_place_lines[1][31:]),
            winner_from=None,
        ),
        ########################################################################
        # **********************************************************************
        ########################################################################
        bracket_utils.MatchRaw(
            match_slot="consolation_seventh_place",
            top_competitor=parse_competitor(seventh_place_lines[0][31:62]),
            bottom_competitor=parse_competitor(seventh_place_lines[2][31:62]),
            result=parse_bout_result(seventh_place_lines[3][62:] + " "),
            bout_number=parse_bout_number(seventh_place_lines[1][31:62]),
            winner=parse_competitor(seventh_place_lines[1][62:]),
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
        215,
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
    for team_name, score in _NOVICE_TEAM_SCORES.items():
        team_scores["novice"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    deductions = bracket_utils.infer_deductions(team_scores)
    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=parsed, team_scores=team_scores, deductions=deductions
    )
    extracted_tournament.sort()
    with open(_HERE / "extracted.2003.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
