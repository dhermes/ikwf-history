# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
Note, there were 4 Novice competitors listed that do not show up in brackets:

- JOHN PAUL MONREAL-BERNER :: TEAM WEST WOLVES (122)
  - Replaced by `ROBERT MALIK :: SCHAUMBURG JR. SAXONS`
- NATE JARMAN :: HILLSBORO JR TOPPERS (130)
  - Replaced by `CURTIS LEGG :: JR. MAROON WC`
- JUAN SANCHEZ :: JUNIOR PIRATE WC (130) -- Scratched
- PETER KOWALCZUK JR. :: OPRF LITTLE HUSKIE WC (215) -- Scratched

and 4 Senior competitors listed that do not show up in brackets:

- ANDREW ORTMAN :: ARLINGTON CARDINALS (89) -- Scratched
- JOSHUA HAWTHORNE :: FALCON YOUTH WC (166)
  - Replaced by `JOSHUA VAN BEHREN :: UNITY WC`
- ALEX GRIFFIN :: MT. ZION WC (166)
  - Typo, actually `ALEXANDER GRIFFIN :: HARVEY TWISTERS`
- RAYMOND DONOVAN :: BADGER WC (275) -- Scratched

and 1 Senior competitor that was added to a bracket that was not full:

- ANDREW MOTT :: BATAVIA PINNERS (74)
"""

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "WRESTLING FACTORY": 144.0,
    "FOX VALLEY WC": 118.0,
    "HARVEY TWISTERS": 118.0,
    "MARTINEZ FOX VALLEY ELITE WC": 105.0,
    "TINLEY PARK BULLDOGS": 89.5,
    "HINSDALE RED DEVIL WC": 89.0,
    "BISON WC": 88.0,
    "MOLINE WC": 87.5,
    "GLADIATORS": 87.0,
    "VITTUM CATS": 79.5,
    "SJO SPARTAN WC": 70.5,
    "ORLAND PARK PIONEERS": 69.0,
    "LITTLE CELTIC WC": 65.0,
    "CRYSTAL LAKE WIZARDS": 57.0,
    "TIGERTOWN TANGLERS": 52.5,
    "ARLINGTON CARDINALS": 51.0,
    "GLENBARD EAST JR RAMS": 47.5,
    "JACKSONVILLE WC": 47.0,
    "KNIGHTS WRESTLING": 47.0,
    "BELLEVILLE LITTLE DEVILS": 45.0,
    "DIXON WC": 45.0,
    "JOLIET BOYS CLUB COBRAS": 45.0,
    "OAK FOREST WARRIORS": 43.5,
    "DAKOTA WC": 43.0,
    "OAK LAWN P.D. WILDCATS": 43.0,
    "VANDALIA JR WRESTLING": 37.0,
    "BLACKHAWK WC": 33.0,
    "BRAWLERS WC": 33.0,
    "LINCOLN-WAY WC": 28.0,
    "PLAINFIELD WC": 28.0,
    "VILLA LOMBARD COUGARS": 26.5,
    "SAUKEE YOUTH WC": 26.0,
    "PANTHER CUB WC": 25.0,
    "SAVANNA REDHAWKS": 25.0,
    "RAMS WC": 24.5,
    "CUMBERLAND YOUTH WC": 24.0,
    "MUSTANG WC": 24.0,
    "OSWEGO PANTHERS": 24.0,
    "PONTIAC PYTHONS": 24.0,
    "BETHALTO BULLS WC": 23.0,
    "LAKELAND PREDATORS": 23.0,
    "ST. CHARLES WC": 23.0,
    "BATAVIA PINNERS": 22.0,
    "POLO WC": 21.0,
    "YORKVILLE WC": 21.0,
    "OPRF LITTLE HUSKIE WC": 20.0,
    "GENESEO WC": 19.0,
    "HONONEGAH KIDS WC": 19.0,
    "LEMONT BEARS WC": 19.0,
    "ROXANA KIDS WRESTLING CLUB": 19.0,
    "UNITY WC": 18.5,
    "JR. PANTHERS WRESTLING": 18.0,
    "WOLFPAK WC": 18.0,
    "BENTON JR. WC": 16.0,
    "SPRINGFIELD CAPITALS": 16.0,
    "TRIAD KNIGHTS": 15.0,
    "CHILLICOTHE WC": 13.0,
    "MIDWEST CENTRAL YOUTH": 10.0,
    "L-P CRUNCHING CAVS": 8.0,
    "MAINE EAGLES WC": 8.0,
    "CARY JR TROJAN MATMEN": 6.0,
    "EDWARDSVILLE WC": 6.0,
    "FALCON YOUTH WC": 6.0,
    "HARLEM COUGARS": 6.0,
    "NAPERVILLE WC": 6.0,
    "STERLING NEWMAN JR COMETS": 6.0,
    "SOUTHERN ILLINOIS EAGLES": 5.0,
    "EFFINGHAM YOUTH WC": 4.0,
    "EUREKA KIDS WC": 4.0,
    "FISHER WC": 4.0,
    "HOOPESTON AREA WC": 4.0,
    "LITTLE BOILER WC": 4.0,
    "LOCKPORT GATORS WC": 4.0,
    "MACOMB LITTLE BOMBERS": 4.0,
    "MATTOON YOUTH WC": 4.0,
    "MORTON LITTLE MUSTANGS": 4.0,
    "PALATINE PANTHERS WC": 4.0,
    "PANTHER WC": 4.0,
    "ROCKFORD WC": 4.0,
    "SYCAMORE WC": 4.0,
    "WHEATON MONROE EAGLES": 4.0,
    "SCHAUMBURG JR. SAXONS": 3.0,
    "STILLMAN VALLEY WC": 3.0,
    "T-BIRD / RAIDER WRESTLING": 3.0,
    "TEAM XPRESS": 3.0,
    "ARGENTA / OREANA KIDS CLUB": 2.0,
    "BELVIDERE BANDITS": 2.0,
    "BISMARCK-HENNING WC": 2.0,
    "CHAMPAIGN KIDS WRESTLING": 2.0,
    "DOWNERS GROVE COUGARS": 2.0,
    "DUNDEE HIGHLANDERS": 2.0,
    "FALCON WC": 2.0,
    "LAWRENCE COUNTY WC": 2.0,
    "MURPHYSBORO WRESTLING": 2.0,
    "PONY EXPRESS WC": 2.0,
    "RICH RATTLERS WC": 2.0,
    "ROUND LAKE BAD BOYZ": 2.0,
    "TIGER WC": 2.0,
    "TOMCAT WC": 2.0,
    "BARTLETT HAWK WC": 1.0,
    "A-J JR. WILDCATS": 0.0,
    "ACES WC": 0.0,
    "BADGER WC": 0.0,
    "BLOOMINGTON RAIDER WC": 0.0,
    "BOYS & GIRLS CLUB OF PEKIN": 0.0,
    "BRONCO WRESTLING": 0.0,
    "CAMP POINT CENTRAL": 0.0,
    "CARLINVILLE KIDS WC": 0.0,
    "CENTRAL WC": 0.0,
    "CHARLESTON WC": 0.0,
    "CHENOA MAT CATS": 0.0,
    "CROSSFACE WRESTLING": 0.0,
    "DEKALB WC": 0.0,
    "DURAND-PECATONICA CARNIVORES": 0.0,
    "EAST MOLINE PANTHER PINNERS": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "FORD HEIGHTS FALCONS": 0.0,
    "GALESBURG JR STREAKS": 0.0,
    "GENERALS": 0.0,
    "GENEVA WC": 0.0,
    "GRANITE CITY JR WARRIORS": 0.0,
    "HIGHLAND BULLDOG JR WC": 0.0,
    "HILLSBORO JR TOPPERS": 0.0,
    "HILLTOPPERS WC": 0.0,
    "HOMEWOOD-FLOSSMOOR CATS": 0.0,
    "HUSKIES WC": 0.0,
    "ILLINI BLUFFS WC": 0.0,
    "JR. COUGAR WC": 0.0,
    "JR. GOLDEN EAGLES": 0.0,
    "JR. MAROON WC": 0.0,
    "JR. ROCKET WRESTLING": 0.0,
    "JR. SENTINELS": 0.0,
    "JUNIOR PIRATE WC": 0.0,
    "KISHWAUKEE WC": 0.0,
    "LAKE VIEW JR WILDCATS": 0.0,
    "LANCER WC": 0.0,
    "LARKIN JR. ROYALS WC": 0.0,
    "LIL' ROUGHNECKS": 0.0,
    "LIL' STORM YOUTH WRESTLING": 0.0,
    "LITTLE REDBIRD WC": 0.0,
    "MANTENO JR PANTHERS": 0.0,
    "MARENGO WC": 0.0,
    "METAMORA KIDS WC": 0.0,
    "MT. VERNON LIONS": 0.0,
    "MT. ZION WC": 0.0,
    "NORTHSHORE GATORS": 0.0,
    "NOTRE DAME": 0.0,
    "OAKWOOD WC": 0.0,
    "PLT PROPHETS WC": 0.0,
    "RAIDER WC": 0.0,
    "RIVERBEND WC": 0.0,
    "ROCK ISLAND JR. ROCKS": 0.0,
    "SHARKS WC": 0.0,
    "SHEPARD WRESTLING": 0.0,
    "TAYLORVILLE WC": 0.0,
    "TAZEWELL COUNTY KIDZ WC": 0.0,
    "TEAM WEST WOLVES": 0.0,
    "WARRENSBURG WC": 0.0,
    "WAUBONSIE WC": 0.0,
    "WAUKEGAN TAKEDOWN": 0.0,
    "WEST FRANKFORT JR. WC": 0.0,
    "WESTVILLE YOUTH WC": 0.0,
    "WHEATON BULLDOGS": 0.0,
    "WHEATON FRANKLIN WC": 0.0,
    "CARBONDALE WC": -1.0,
    "GLEN ELLYN DUNGEON WC": -1.0,
    "LAN-OAK P.D. LITTLE REBELS": -1.0,
    "LIONS WC": -1.0,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY TWISTERS": 240.5,
    "MARTINEZ FOX VALLEY ELITE WC": 235.0,
    "TINLEY PARK BULLDOGS": 124.5,
    "DAKOTA WC": 123.0,
    "VITTUM CATS": 117.5,
    "BLACKHAWK WC": 109.0,
    "BETHALTO BULLS WC": 99.5,
    "WRESTLING FACTORY": 84.0,
    "ORLAND PARK PIONEERS": 82.0,
    "EDWARDSVILLE WC": 79.0,
    "VILLA LOMBARD COUGARS": 78.0,
    "ROXANA KIDS WRESTLING CLUB": 75.0,
    "GRANITE CITY JR WARRIORS": 74.0,
    "MOLINE WC": 74.0,
    "BELLEVILLE LITTLE DEVILS": 72.0,
    "WOLFPAK WC": 65.0,
    "VANDALIA JR WRESTLING": 59.0,
    "GENESEO WC": 58.0,
    "HONONEGAH KIDS WC": 53.0,
    "ARLINGTON CARDINALS": 50.0,
    "SJO SPARTAN WC": 49.0,
    "BISON WC": 44.0,
    "PLAINFIELD WC": 43.0,
    "FOX VALLEY WC": 42.0,
    "LIONS WC": 42.0,
    "SOUTHERN ILLINOIS EAGLES": 34.5,
    "CHARLESTON WC": 34.0,
    "PANTHER CUB WC": 34.0,
    "HUSKIES WC": 33.0,
    "SCHAUMBURG JR. SAXONS": 33.0,
    "JOLIET BOYS CLUB COBRAS": 31.0,
    "MURPHYSBORO WRESTLING": 30.0,
    "BRAWLERS WC": 29.5,
    "ARGENTA / OREANA KIDS CLUB": 29.0,
    "PANTHER WC": 28.5,
    "CHAMPAIGN KIDS WRESTLING": 27.0,
    "HARLEM COUGARS": 27.0,
    "CRYSTAL LAKE WIZARDS": 26.0,
    "EAST MOLINE PANTHER PINNERS": 26.0,
    "PONTIAC PYTHONS": 26.0,
    "DIXON WC": 25.5,
    "MIDWEST CENTRAL YOUTH": 24.0,
    "MARENGO WC": 23.0,
    "WHEATON MONROE EAGLES": 22.0,
    "RIVERBEND WC": 20.5,
    "JR. SENTINELS": 19.0,
    "BATAVIA PINNERS": 18.0,
    "GLEN ELLYN DUNGEON WC": 18.0,
    "OAK FOREST WARRIORS": 17.0,
    "ILLINI BLUFFS WC": 15.0,
    "LEMONT BEARS WC": 15.0,
    "CARY JR TROJAN MATMEN": 13.0,
    "HOOPESTON AREA WC": 13.0,
    "MT. ZION WC": 13.0,
    "JR. ROCKET WRESTLING": 12.0,
    "GENERALS": 11.5,
    "BLOOMINGTON RAIDER WC": 11.0,
    "LITTLE CELTIC WC": 11.0,
    "MORTON LITTLE MUSTANGS": 11.0,
    "MUSTANG WC": 11.0,
    "DUNDEE HIGHLANDERS": 10.0,
    "HINSDALE RED DEVIL WC": 10.0,
    "JACKSONVILLE WC": 10.0,
    "LAWRENCE COUNTY WC": 10.0,
    "BELVIDERE BANDITS": 9.0,
    "LINCOLN-WAY WC": 9.0,
    "WAUBONSIE WC": 9.0,
    "BISMARCK-HENNING WC": 8.0,
    "NOTRE DAME": 8.0,
    "OSWEGO PANTHERS": 8.0,
    "TAZEWELL COUNTY KIDZ WC": 8.0,
    "MT. VERNON LIONS": 7.0,
    "PALATINE PANTHERS WC": 7.0,
    "NAPERVILLE WC": 6.0,
    "STILLMAN VALLEY WC": 6.0,
    "JR. GOLDEN EAGLES": 5.0,
    "DURAND-PECATONICA CARNIVORES": 4.0,
    "HILLSBORO JR TOPPERS": 4.0,
    "JR. PANTHERS WRESTLING": 4.0,
    "JUNIOR PIRATE WC": 4.0,
    "LARKIN JR. ROYALS WC": 4.0,
    "LITTLE BOILER WC": 4.0,
    "OAKWOOD WC": 4.0,
    "OPRF LITTLE HUSKIE WC": 4.0,
    "ROCKFORD WC": 4.0,
    "SHARKS WC": 4.0,
    "TEAM XPRESS": 4.0,
    "WAUKEGAN TAKEDOWN": 4.0,
    "WEST FRANKFORT JR. WC": 4.0,
    "RICH RATTLERS WC": 3.5,
    "DEKALB WC": 3.0,
    "GALESBURG JR STREAKS": 3.0,
    "HIGHLAND BULLDOG JR WC": 3.0,
    "TAYLORVILLE WC": 3.0,
    "YORKVILLE WC": 3.0,
    "CHILLICOTHE WC": 2.0,
    "POLO WC": 2.0,
    "STERLING NEWMAN JR COMETS": 2.0,
    "LAN-OAK P.D. LITTLE REBELS": 1.0,
    "A-J JR. WILDCATS": 0.0,
    "ACES WC": 0.0,
    "BADGER WC": 0.0,
    "BENTON JR. WC": 0.0,
    "BOYS & GIRLS CLUB OF PEKIN": 0.0,
    "BRONCO WRESTLING": 0.0,
    "CAMP POINT CENTRAL": 0.0,
    "CARLINVILLE KIDS WC": 0.0,
    "CENTRAL WC": 0.0,
    "CHENOA MAT CATS": 0.0,
    "CROSSFACE WRESTLING": 0.0,
    "CUMBERLAND YOUTH WC": 0.0,
    "DOWNERS GROVE COUGARS": 0.0,
    "EFFINGHAM YOUTH WC": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "EUREKA KIDS WC": 0.0,
    "FALCON WC": 0.0,
    "FALCON YOUTH WC": 0.0,
    "FISHER WC": 0.0,
    "FORD HEIGHTS FALCONS": 0.0,
    "GENEVA WC": 0.0,
    "GLADIATORS": 0.0,
    "GLENBARD EAST JR RAMS": 0.0,
    "HILLTOPPERS WC": 0.0,
    "HOMEWOOD-FLOSSMOOR CATS": 0.0,
    "JR. COUGAR WC": 0.0,
    "JR. MAROON WC": 0.0,
    "KISHWAUKEE WC": 0.0,
    "L-P CRUNCHING CAVS": 0.0,
    "LAKE VIEW JR WILDCATS": 0.0,
    "LAKELAND PREDATORS": 0.0,
    "LANCER WC": 0.0,
    "LIL' ROUGHNECKS": 0.0,
    "LIL' STORM YOUTH WRESTLING": 0.0,
    "LITTLE REDBIRD WC": 0.0,
    "LOCKPORT GATORS WC": 0.0,
    "MACOMB LITTLE BOMBERS": 0.0,
    "MAINE EAGLES WC": 0.0,
    "MANTENO JR PANTHERS": 0.0,
    "MATTOON YOUTH WC": 0.0,
    "METAMORA KIDS WC": 0.0,
    "NORTHSHORE GATORS": 0.0,
    "OAK LAWN P.D. WILDCATS": 0.0,
    "PLT PROPHETS WC": 0.0,
    "PONY EXPRESS WC": 0.0,
    "RAIDER WC": 0.0,
    "RAMS WC": 0.0,
    "ROCK ISLAND JR. ROCKS": 0.0,
    "ROUND LAKE BAD BOYZ": 0.0,
    "SAUKEE YOUTH WC": 0.0,
    "SAVANNA REDHAWKS": 0.0,
    "SHEPARD WRESTLING": 0.0,
    "SPRINGFIELD CAPITALS": 0.0,
    "SYCAMORE WC": 0.0,
    "TEAM WEST WOLVES": 0.0,
    "TIGER WC": 0.0,
    "TIGERTOWN TANGLERS": 0.0,
    "TOMCAT WC": 0.0,
    "TRIAD KNIGHTS": 0.0,
    "UNITY WC": 0.0,
    "WARRENSBURG WC": 0.0,
    "WESTVILLE YOUTH WC": 0.0,
    "WHEATON BULLDOGS": 0.0,
    "WHEATON FRANKLIN WC": 0.0,
    "BARTLETT HAWK WC": -1.0,
    "CARBONDALE WC": -1.0,
    "KNIGHTS WRESTLING": -1.0,
    "ST. CHARLES WC": -1.0,
    "T-BIRD / RAIDER WRESTLING": -1.0,
}
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("ANTHONY DEGANI JR", "CRYSTAL LAKE WIZARDS"): bracket_utils.Competitor(
        full_name="ANTHONY DEGANI JR",
        first_name="ANTHONY",
        last_name="DEGANI",
        team_full="CRYSTAL LAKE WIZARDS",
    ),
    ("ANTHONY RICH JR.", "L-P CRUNCHING CAVS"): bracket_utils.Competitor(
        full_name="ANTHONY RICH JR.",
        first_name="ANTHONY",
        last_name="RICH",
        team_full="L-P CRUNCHING CAVS",
    ),
    # NOTE: This also fixes a typo in BJ's name (BENARD -> BERNARD)
    ("BENARD FUTRELL II", "HARVEY TWISTERS"): bracket_utils.Competitor(
        full_name="BENARD FUTRELL II",
        first_name="BERNARD",
        last_name="FUTRELL",
        team_full="HARVEY TWISTERS",
    ),
    ("CARL FORESIDE JR", "GLADIATORS"): bracket_utils.Competitor(
        full_name="CARL FORESIDE JR",
        first_name="CARL",
        last_name="FORESIDE",
        team_full="GLADIATORS",
    ),
    # NOTE: This assumes LL was lowercase ll, which resembles capitalized II
    ("DARREN MILLER  LL", "OPRF LITTLE HUSKIE WC"): bracket_utils.Competitor(
        full_name="DARREN MILLER  LL",
        first_name="DARREN",
        last_name="MILLER",
        team_full="OPRF LITTLE HUSKIE WC",
    ),
    ("FRANK III BOLTON", "HARVEY TWISTERS"): bracket_utils.Competitor(
        full_name="FRANK III BOLTON",
        first_name="FRANK",
        last_name="BOLTON",
        team_full="HARVEY TWISTERS",
    ),
    ("HARRY STARKS III", "HARVEY TWISTERS"): bracket_utils.Competitor(
        full_name="HARRY STARKS III",
        first_name="HARRY",
        last_name="STARKS",
        team_full="HARVEY TWISTERS",
    ),
    ("JAMES VAN SOMEREN", "WHEATON FRANKLIN WC"): bracket_utils.Competitor(
        full_name="JAMES VAN SOMEREN",
        first_name="JAMES",
        last_name="VAN SOMEREN",
        team_full="WHEATON FRANKLIN WC",
    ),
    ("JERRY BEMIS III", "OAK LAWN P.D. WILDCATS"): bracket_utils.Competitor(
        full_name="JERRY BEMIS III",
        first_name="JERRY",
        last_name="BEMIS",
        team_full="OAK LAWN P.D. WILDCATS",
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
        last_name="MCCALL",
        team_full="ROCK ISLAND JR. ROCKS",
    ),
    ("NATHAN ST. CLAIR", "HINSDALE RED DEVIL WC"): bracket_utils.Competitor(
        full_name="NATHAN ST. CLAIR",
        first_name="NATHAN",
        last_name="ST. CLAIR",
        team_full="HINSDALE RED DEVIL WC",
    ),
    ("TOM REEDY JR", "MOLINE WC"): bracket_utils.Competitor(
        full_name="TOM REEDY JR",
        first_name="TOM",
        last_name="REEDY",
        team_full="MOLINE WC",
    ),
}
TEAM_SCORE_EXCEPTIONS: dict[tuple[bracket_utils.Division, str], float] = {}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ARG": "ARGENTA / OREANA KIDS CLUB",
    "ARL": "ARLINGTON CARDINALS",
    "BAD": "BADGER WC",
    "BAT": "BATAVIA PINNERS",
    "BEL": "BELLEVILLE LITTLE DEVILS",
    "BET": "BETHALTO BULLS WC",
    "BEV": "BELVIDERE BANDITS",
    "BIO": "BISON WC",
    "BIS": "BISMARCK-HENNING WC",
    "BLA": "BLACKHAWK WC",
    "BOY": "BOYS & GIRLS CLUB OF PEKIN",
    "BRA": "BRAWLERS WC",
    "CAY": "CARY JR TROJAN MATMEN",
    "CHA": "CHAMPAIGN KIDS WRESTLING",
    "CHE": "CHENOA MAT CATS",
    "CHR": "CHARLESTON WC",
    "CRY": "CRYSTAL LAKE WIZARDS",
    "CUM": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DEK": "DEKALB WC",
    "DIX": "DIXON WC",
    "DUN": "DUNDEE HIGHLANDERS",
    "EAS": "EAST MOLINE PANTHER PINNERS",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "EUR": "EUREKA KIDS WC",
    "FAL": "FALCON WC",
    "FIS": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "GEE": "GENESEO WC",
    "GLA": "GLADIATORS",
    "GLE": "GLEN ELLYN DUNGEON WC",
    "GRA": "GRANITE CITY JR WARRIORS",
    "HAE": "HARVEY TWISTERS",
    "HAR": "HARLEM COUGARS",
    "HIG": "HIGHLAND BULLDOG JR WC",
    "HIN": "HINSDALE RED DEVIL WC",
    "HON": "HONONEGAH KIDS WC",
    "HOO": "HOOPESTON AREA WC",
    "HUS": "HUSKIES WC",
    "JAC": "JACKSONVILLE WC",
    "JOL": "JOLIET BOYS CLUB COBRAS",
    "JRG": "JR. GOLDEN EAGLES",
    "JRP": "JR. PANTHERS WRESTLING",
    "JRS": "JR. SENTINELS",
    "LAO": "LAN-OAK P.D. LITTLE REBELS",
    "LAW": "LAWRENCE COUNTY WC",
    "LEM": "LEMONT BEARS WC",
    "LIB": "LITTLE BOILER WC",
    "LIC": "LITTLE CELTIC WC",
    "LIN": "LINCOLN-WAY WC",
    "LIS": "LIL' STORM YOUTH WRESTLING",
    "LOC": "LOCKPORT GATORS WC",
    "LPC": "L-P CRUNCHING CAVS",
    "MAF": "MARTINEZ FOX VALLEY ELITE WC",
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
    "RIC": "RICH RATTLERS WC",
    "ROF": "ROCKFORD WC",
    "ROX": "ROXANA KIDS WRESTLING CLUB",
    "SCH": "SCHAUMBURG JR. SAXONS",
    "SJO": "SJO SPARTAN WC",
    "SOU": "SOUTHERN ILLINOIS EAGLES",
    "SPR": "SPRINGFIELD CAPITALS",
    "STE": "STERLING NEWMAN JR COMETS",
    "STI": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE WC",
    "TBI": "T-BIRD / RAIDER WRESTLING",
    "TEX": "TEAM XPRESS",
    "TIG": "TIGER WC",
    "TIN": "TINLEY PARK BULLDOGS",
    "TOM": "TOMCAT WC",
    "UNI": "UNITY WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAK": "WAUKEGAN TAKEDOWN",
    "WES": "WEST FRANKFORT JR. WC",
    "WHM": "WHEATON MONROE EAGLES",
    "WOL": "WOLFPAK WC",
    "WRE": "WRESTLING FACTORY",
    "YOR": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "BAR": "BARTLETT HAWK WC",
    "BEN": "BENTON JR. WC",
    "CAR": "CARBONDALE WC",
    "CHL": "CHILLICOTHE WC",
    "CRO": "CROSSFACE WRESTLING",
    "DOW": "DOWNERS GROVE COUGARS",
    "FAC": "FALCON YOUTH WC",
    "FOR": "FORD HEIGHTS FALCONS",
    "GLN": "GLENBARD EAST JR RAMS",
    "HOM": "HOMEWOOD-FLOSSMOOR CATS",
    "JRM": "JR. MAROON WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAE": "LAKELAND PREDATORS",
    "LIL": "LIL' ROUGHNECKS",
    "MAC": "MACOMB LITTLE BOMBERS",
    "MAI": "MAINE EAGLES WC",
    "PLT": "PLT PROPHETS WC",
    "RAI": "RAIDER WC",
    "RAM": "RAMS WC",
    "ROK": "ROCK ISLAND JR. ROCKS",
    "ROU": "ROUND LAKE BAD BOYZ",
    "SAU": "SAUKEE YOUTH WC",
    "SAV": "SAVANNA REDHAWKS",
    "STC": "ST. CHARLES WC",
    "TIE": "TIGERTOWN TANGLERS",
    "TRI": "TRIAD KNIGHTS",
    "WHF": "WHEATON FRANKLIN WC",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ACE": "ACES WC",
    "AJJ": "A-J JR. WILDCATS",
    "BLO": "BLOOMINGTON RAIDER WC",
    "BRO": "BRONCO WRESTLING",
    "CAL": "CARLINVILLE KIDS WC",
    "CAM": "CAMP POINT CENTRAL",
    "CEN": "CENTRAL WC",
    "CHI": "CHILLICOTHE WC",
    "DUR": "DURAND-PECATONICA CARNIVORES",
    "ELM": "ELMHURST JR. DUKES",
    "GAL": "GALESBURG JR STREAKS",
    "GEN": "GENERALS",
    "GEV": "GENEVA WC",
    "HIL": "HILLSBORO JR TOPPERS",
    "HIT": "HILLTOPPERS WC",
    "ILL": "ILLINI BLUFFS WC",
    "JRC": "JR. COUGAR WC",
    "JRR": "JR. ROCKET WRESTLING",
    "JUP": "JUNIOR PIRATE WC",
    "LAR": "LARKIN JR. ROYALS WC",
    "LIO": "LIONS WC",
    "LIR": "LITTLE REDBIRD WC",
    "MET": "METAMORA KIDS WC",
    "NOR": "NORTHSHORE GATORS",
    "NOT": "NOTRE DAME",
    "RIV": "RIVERBEND WC",
    "SHP": "SHEPARD WRESTLING",
    "SHR": "SHARKS WC",
    "TAY": "TAYLORVILLE WC",
    "TAZ": "TAZEWELL COUNTY KIDZ WC",
    "WAR": "WARRENSBURG WC",
    "WAU": "WAUBONSIE WC",
    "WET": "WESTVILLE YOUTH WC",
    "WHE": "WHEATON BULLDOGS",
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
    # VERY SPECIAL CASES
    if value == "-Fall 20-1 3:01   Bout:    306|":
        return "Fall 20-1 3:01"
    if value == " T-Fall TF 2:37   Bout:    972|":
        return "T-Fall TF 2:37"

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
    with open(_HERE / "2002" / division / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre: list[bs4.Tag] = soup.find_all("pre")
    if len(all_pre) != 4:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre, seventh_place_pre = all_pre
    championship_text = championship_pre.text
    # Address known typo(s)
    championship_text = championship_text.replace("Fall 3;59", "Fall 3:59")

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
    with open(_HERE / "extracted.2002.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
