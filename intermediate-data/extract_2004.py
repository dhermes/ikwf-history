# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
Note, there were 5 Novice competitors listed that do not show up in brackets:

- REED MOSKAL :: ELMHURST JR. DUKES (70) -- Scratched
- DAVID LUTZ :: HINSDALE RED DEVIL WC (89)
  - Replace by `NICHOLAS SAIZ :: FOX VALLEY WC`
- DANNY SOTHMANN :: RIVERDALE JR. RAMS WC (115)
  - Replaced by `D'AUNTAI THOMPSON :: ROCK ISLAND WC`
- ANTHONY RODRIGUEZ :: CHENOA MAT CATS (215) -- Scratched
- CHRIS GREEN :: CHILLI DAWGS WC (215) -- Scratched

and 8 Senior competitors listed that do not show up in brackets:

- JEFF BARNES :: CHARLESTON WC (74) -- Scratched
- JOSH JOHNSON :: WEST FRANKFORT JR. WC (84)
  - Replaced by `BRADLEY ALLSUP :: CHILLI DAWGS WC`
- COREY DOLBY :: HOOPESTON AREA WC (89)
  - Replaced by `JORDAN CRABTREE :: HOOPESTON AREA WC `
- MATTHEW CARROLL :: MAINE EAGLES WC (156)
  - Replaced by `RYAN PETTA :: DAKOTA WC`
- BEN JANSEN :: ZEE-BEE STINGERS (189)
  - Replaced by `NICK BRAMHALL :: EDWARDSVILLE WC`
- KRISTOPHER SMITH :: BLACKHAWK WC (215) -- Scratched
- BRYAN OPPENHEIMER :: NAPERVILLE WC (275) -- Scratched
- MARK ZIELINSKI :: TREVIAN WC (275) -- Scratched

and 1 Senior competitor that was added to a bracket that was not full:

- DANNY CAREY :: BLACKHAWK WC (177)
"""

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "FOX VALLEY WC": 179.0,
    "HARVEY PARK DISTRICT TWISTERS": 127.0,
    "CRYSTAL LAKE WIZARDS": 112.5,
    "MARTINEZ FOX VALLEY ELITE WC": 95.5,
    "MAINE EAGLES WC": 78.5,
    "HARLEM COUGARS": 71.0,
    "PLAINFIELD TORNADOES WC": 66.0,
    "HONONEGAH KIDS WC": 64.5,
    "LITTLE CELTIC WC": 64.5,
    "ROXANA KIDS WC": 61.5,
    "ST. CHARLES EAST WC": 60.0,
    "VITTUM CATS": 58.5,
    "HINSDALE RED DEVIL WC": 58.0,
    "FENWICK FALCONS WC": 56.5,
    "DIXON WC": 56.0,
    "ORLAND PARK PIONEERS": 55.0,
    "BLACKHAWK WC": 53.0,
    "DOWNERS GROVE COUGARS": 53.0,
    "BISON WC": 49.0,
    "GRANITE CITY JR WARRIORS": 45.0,
    "HOOPESTON AREA WC": 41.0,
    "JR. GOLDEN EAGLES": 39.0,
    "LAKELAND PREDATORS": 39.0,
    "SAUKEE YOUTH WC": 37.0,
    "WRESTLING FACTORY": 36.0,
    "BATAVIA PINNERS": 35.0,
    "YORKVILLE WC": 34.0,
    "BRAWLERS WC": 33.0,
    "EDWARDSVILLE WC": 33.0,
    "PROVISO POWERHOUSE WC": 33.0,
    "PANTHER WC": 32.5,
    "CHAMPAIGN KIDS WRESTLING": 31.0,
    "RIVERDALE JR. RAMS WC": 29.0,
    "BADGER WC": 28.0,
    "HOFFMAN ESTATES WC": 28.0,
    "OSWEGO PANTHERS": 25.0,
    "TINLEY PARK BULLDOGS": 25.0,
    "VILLA LOMBARD COUGARS": 25.0,
    "O'FALLON LITTLE PANTHERS": 24.0,
    "BETHALTO BULLS WC": 23.5,
    "MT. ZION WC": 23.0,
    "TAKEDOWN WC": 23.0,
    "DAKOTA WC": 22.0,
    "MURPHYSBORO WRESTLING": 22.0,
    "SYCAMORE WC": 22.0,
    "JOLIET BOYS CLUB COBRAS": 21.0,
    "METAMORA KIDS WC": 21.0,
    "DU-PEC CARNIVORES": 20.0,
    "BELLEVILLE LITTLE DEVILS": 19.0,
    "FALCON WC": 19.0,
    "SCN YOUTH WC": 19.0,
    "GENESEO WC": 18.5,
    "LIMESTONE YOUTH ROCKET WC": 18.5,
    "JR. SAXONS WC": 18.0,
    "JR. SENTINELS": 18.0,
    "GLENBARD EAST JR RAMS": 17.0,
    "ST. TARCISSUS": 15.0,
    "LOCKPORT GATORS WC": 14.0,
    "MOLINE WC": 14.0,
    "TOMCAT WC": 14.0,
    "HIGHLAND BULLDOG JR WC": 13.5,
    "ROCK ISLAND WC": 13.0,
    "JACKSONVILLE WC": 12.0,
    "SILVER & BLACK ATTACK": 12.0,
    "OAK LAWN P.D. WILDCATS": 11.5,
    "UNITY WC": 11.0,
    "POLO WC": 10.5,
    "LEMONT BEARS WC": 10.0,
    "MACOMB LITTLE BOMBERS": 9.0,
    "ANIMALS WC": 8.0,
    "BLAZER KIDS": 8.0,
    "PANTHER POWERHOUSE WC": 8.0,
    "SJO SPARTAN YOUTH WC": 7.0,
    "ARLINGTON CARDINALS": 6.0,
    "L-P CRUNCHING CAVS": 6.0,
    "CARBONDALE WC": 4.0,
    "ERIE MIDDLE SCHOOL WC": 4.0,
    "FIGHTIN TITAN WC": 4.0,
    "MENDOTA MAT MASTERS": 4.0,
    "TRI-CITY BRAVES": 4.0,
    "DEKALB WC": 3.5,
    "CENTRAL WC": 3.0,
    "MATTOON YOUTH WC": 3.0,
    "OAK FOREST WARRIORS": 3.0,
    "STERLING NEWMAN JR COMETS": 3.0,
    "BLOOMINGTON RAIDER WC": 2.0,
    "CARY JR TROJAN MATMEN": 2.0,
    "CHENOA MAT CATS": 2.0,
    "CHILLI DAWGS WC": 2.0,
    "LITTLE INDIANS": 2.0,
    "NAPERVILLE WC": 2.0,
    "PALATINE PANTHERS WC": 2.0,
    "SHAMROCK WC": 2.0,
    "DUNDEE HIGHLANDERS": 1.0,
    "ALEDO BEAR COUNTRY WC": 0.0,
    "BARRINGTON BRONCOS": 0.0,
    "BARTLETT JR HAWKS": 0.0,
    "BENTON JR WC": 0.0,
    "BISMARCK HENNING WC": 0.0,
    "CARLINVILLE KIDS WC": 0.0,
    "CHARLESTON WC": 0.0,
    "CUMBERLAND YOUTH WC": 0.0,
    "EFFINGHAM YOUTH WC": 0.0,
    "EL PASO WC": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "ERVIN WC": 0.0,
    "FALCON YOUTH WC": 0.0,
    "FISHER WC": 0.0,
    "GALESBURG JR STREAKS": 0.0,
    "GENEVA WC": 0.0,
    "HILLSBORO JR TOPPERS": 0.0,
    "JR. COUGARS WC": 0.0,
    "JR. MAROON WC": 0.0,
    "LAWRENCE COUNTY WC": 0.0,
    "LIL' STORM YOUTH WRESTLING": 0.0,
    "LINCOLN-WAY WC": 0.0,
    "LIONHEART INTENSE WRESTLING": 0.0,
    "LITTLE GIANTS WC": 0.0,
    "LITTLE HUSKIE WC": 0.0,
    "LITTLE REDBIRD WC": 0.0,
    "LITTLE REDSKINS WC": 0.0,
    "LITTLE VIKING WC OF H-F": 0.0,
    "M-S KIDS CLUB": 0.0,
    "MORRISON STALLIONS WC": 0.0,
    "MORTON YOUTH WRESTLING": 0.0,
    "MT. VERNON LIONS": 0.0,
    "MUSTANG WC": 0.0,
    "OAKWOOD WC": 0.0,
    "PALATINE JUNIOR PIRATES": 0.0,
    "PANTHER CUB WC": 0.0,
    "PONTIAC PYTHONS": 0.0,
    "RAMS WC": 0.0,
    "REED CUSTER KNIGHTS": 0.0,
    "RICHMOND WC": 0.0,
    "RIVERBEND WC": 0.0,
    "ROAD WARRIORS": 0.0,
    "ROCHELLE WC": 0.0,
    "ROCK RIDGE WC": 0.0,
    "ROCKFORD WC": 0.0,
    "SAVANNA REDHAWKS": 0.0,
    "SENECA IRISH CADETS": 0.0,
    "SHELBYVILLE JR RAMS WRESTLING": 0.0,
    "SHERRARD JR WC": 0.0,
    "STILLMAN VALLEY WC": 0.0,
    "T-BIRD RAIDER WRESTLING": 0.0,
    "TAYLORVILLE WC": 0.0,
    "TIGERTOWN TANGLERS": 0.0,
    "TREVIAN WC": 0.0,
    "TRIAD KNIGHTS": 0.0,
    "TWIN CITY WC": 0.0,
    "UNITED TOWNSHIP WC": 0.0,
    "WARRENSBURG WC": 0.0,
    "WAUBONSIE WC": 0.0,
    "WEST FRANKFORT JR. WC": 0.0,
    "WESTVILLE YOUTH WC": 0.0,
    "WHEATON MONROE EAGLES": 0.0,
    "WHEATON TIGER WC": 0.0,
    "WOLFPAK WC": 0.0,
    "YOUNG CHAMPIONS": 0.0,
    "ZEE-BEE STINGERS": 0.0,
    "ARGENTA / OREANA KIDS CLUB": -1.0,
    "BELVIDERE BANDITS": -1.0,
    "HERRIN WC": -1.0,
    "KNIGHTS WRESTLING": -1.0,
    "MIDWEST CENTRAL YOUTH": -1.0,
    "NOTRE DAME WRESTLING": -1.0,
    "PLAINFIELD WC": -1.0,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": -1.0,
    "TIGER WC": -1.0,
    "MARENGO WC": -2.0,
    "MORTON LITTLE MUSTANGS": -2.0,
    "RICH RATTLERS WC": -2.0,
    "VANDALIA JR WRESTLING": -2.0,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "MARTINEZ FOX VALLEY ELITE WC": 185.0,
    "TINLEY PARK BULLDOGS": 170.5,
    "ARLINGTON CARDINALS": 136.5,
    "FOX VALLEY WC": 135.0,
    "LITTLE CELTIC WC": 125.5,
    "VITTUM CATS": 111.0,
    "CRYSTAL LAKE WIZARDS": 97.0,
    "PANTHER WC": 77.5,
    "HARVEY PARK DISTRICT TWISTERS": 76.0,
    "GRANITE CITY JR WARRIORS": 65.0,
    "ORLAND PARK PIONEERS": 63.5,
    "LAKELAND PREDATORS": 61.0,
    "BELVIDERE BANDITS": 58.0,
    "EDWARDSVILLE WC": 55.0,
    "BLACKHAWK WC": 54.0,
    "VILLA LOMBARD COUGARS": 54.0,
    "LEMONT BEARS WC": 53.0,
    "WRESTLING FACTORY": 51.0,
    "ROCKFORD WC": 49.0,
    "SJO SPARTAN YOUTH WC": 49.0,
    "HARLEM COUGARS": 48.0,
    "WHEATON MONROE EAGLES": 48.0,
    "PLAINFIELD TORNADOES WC": 47.0,
    "ARGENTA / OREANA KIDS CLUB": 44.0,
    "GENESEO WC": 42.0,
    "MUSTANG WC": 40.0,
    "CHENOA MAT CATS": 39.0,
    "SYCAMORE WC": 39.0,
    "SCN YOUTH WC": 36.0,
    "PALATINE PANTHERS WC": 34.0,
    "SHERRARD JR WC": 32.5,
    "BRAWLERS WC": 32.0,
    "GLENBARD EAST JR RAMS": 32.0,
    "RICHMOND WC": 32.0,
    "MATTOON YOUTH WC": 31.5,
    "PANTHER CUB WC": 31.0,
    "STILLMAN VALLEY WC": 31.0,
    "NAPERVILLE WC": 29.5,
    "MOLINE WC": 28.0,
    "BLAZER KIDS": 26.0,
    "HONONEGAH KIDS WC": 26.0,
    "TIGER WC": 26.0,
    "HINSDALE RED DEVIL WC": 24.5,
    "BATAVIA PINNERS": 24.0,
    "RIVERBEND WC": 24.0,
    "BISON WC": 23.0,
    "JR. COUGARS WC": 23.0,
    "WESTVILLE YOUTH WC": 23.0,
    "MT. VERNON LIONS": 21.0,
    "UNITED TOWNSHIP WC": 21.0,
    "BENTON JR WC": 20.0,
    "CARBONDALE WC": 19.5,
    "JR. GOLDEN EAGLES": 19.0,
    "WAUBONSIE WC": 19.0,
    "FALCON WC": 17.0,
    "FIGHTIN TITAN WC": 16.0,
    "MURPHYSBORO WRESTLING": 16.0,
    "EFFINGHAM YOUTH WC": 15.0,
    "JR. SENTINELS": 15.0,
    "METAMORA KIDS WC": 15.0,
    "DUNDEE HIGHLANDERS": 14.0,
    "KNIGHTS WRESTLING": 14.0,
    "MORTON LITTLE MUSTANGS": 14.0,
    "VANDALIA JR WRESTLING": 13.5,
    "GENEVA WC": 13.0,
    "OAK LAWN P.D. WILDCATS": 13.0,
    "TRIAD KNIGHTS": 13.0,
    "TIGERTOWN TANGLERS": 12.0,
    "BADGER WC": 10.0,
    "BELLEVILLE LITTLE DEVILS": 10.0,
    "DIXON WC": 10.0,
    "DAKOTA WC": 9.0,
    "MORRISON STALLIONS WC": 8.0,
    "PALATINE JUNIOR PIRATES": 8.0,
    "LITTLE REDBIRD WC": 7.0,
    "SHELBYVILLE JR RAMS WRESTLING": 7.0,
    "CARLINVILLE KIDS WC": 5.0,
    "CHAMPAIGN KIDS WRESTLING": 5.0,
    "POLO WC": 5.0,
    "DOWNERS GROVE COUGARS": 4.0,
    "FISHER WC": 4.0,
    "JOLIET BOYS CLUB COBRAS": 4.0,
    "JR. MAROON WC": 4.0,
    "L-P CRUNCHING CAVS": 4.0,
    "OAKWOOD WC": 4.0,
    "PROVISO POWERHOUSE WC": 4.0,
    "ROCK ISLAND WC": 4.0,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": 4.0,
    "WOLFPAK WC": 4.0,
    "YORKVILLE WC": 4.0,
    "CARY JR TROJAN MATMEN": 3.5,
    "JR. SAXONS WC": 3.0,
    "WHEATON TIGER WC": 3.0,
    "LAWRENCE COUNTY WC": 2.0,
    "LITTLE VIKING WC OF H-F": 2.0,
    "RICH RATTLERS WC": 2.0,
    "MIDWEST CENTRAL YOUTH": 1.0,
    "ALEDO BEAR COUNTRY WC": 0.0,
    "ANIMALS WC": 0.0,
    "BARRINGTON BRONCOS": 0.0,
    "BARTLETT JR HAWKS": 0.0,
    "BETHALTO BULLS WC": 0.0,
    "BISMARCK HENNING WC": 0.0,
    "BLOOMINGTON RAIDER WC": 0.0,
    "CENTRAL WC": 0.0,
    "CHARLESTON WC": 0.0,
    "CHILLI DAWGS WC": 0.0,
    "CUMBERLAND YOUTH WC": 0.0,
    "DEKALB WC": 0.0,
    "EL PASO WC": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "ERIE MIDDLE SCHOOL WC": 0.0,
    "ERVIN WC": 0.0,
    "FALCON YOUTH WC": 0.0,
    "FENWICK FALCONS WC": 0.0,
    "GALESBURG JR STREAKS": 0.0,
    "GRAPPLIN' DEVILS WC": 0.0,
    "HIGHLAND BULLDOG JR WC": 0.0,
    "HILLSBORO JR TOPPERS": 0.0,
    "HOOPESTON AREA WC": 0.0,
    "JACKSONVILLE WC": 0.0,
    "LIL' STORM YOUTH WRESTLING": 0.0,
    "LIMESTONE YOUTH ROCKET WC": 0.0,
    "LINCOLN-WAY WC": 0.0,
    "LIONHEART INTENSE WRESTLING": 0.0,
    "LITTLE GIANTS WC": 0.0,
    "LITTLE HUSKIE WC": 0.0,
    "LITTLE INDIANS": 0.0,
    "LITTLE REDSKINS WC": 0.0,
    "LOCKPORT GATORS WC": 0.0,
    "M-S KIDS CLUB": 0.0,
    "MACOMB LITTLE BOMBERS": 0.0,
    "MAINE EAGLES WC": 0.0,
    "MENDOTA MAT MASTERS": 0.0,
    "MT. ZION WC": 0.0,
    "O'FALLON LITTLE PANTHERS": 0.0,
    "OAK FOREST WARRIORS": 0.0,
    "OSWEGO PANTHERS": 0.0,
    "PANTHER POWERHOUSE WC": 0.0,
    "PONTIAC PYTHONS": 0.0,
    "REED CUSTER KNIGHTS": 0.0,
    "RIVERDALE JR. RAMS WC": 0.0,
    "ROAD WARRIORS": 0.0,
    "ROCHELLE WC": 0.0,
    "ROCK RIDGE WC": 0.0,
    "ROXANA KIDS WC": 0.0,
    "SAUKEE YOUTH WC": 0.0,
    "SAVANNA REDHAWKS": 0.0,
    "SENECA IRISH CADETS": 0.0,
    "SHAMROCK WC": 0.0,
    "SILVER & BLACK ATTACK": 0.0,
    "ST. TARCISSUS": 0.0,
    "STERLING NEWMAN JR COMETS": 0.0,
    "T-BIRD RAIDER WRESTLING": 0.0,
    "TAKEDOWN WC": 0.0,
    "TAYLORVILLE WC": 0.0,
    "TOMCAT WC": 0.0,
    "TREVIAN WC": 0.0,
    "TRI-CITY BRAVES": 0.0,
    "TWIN CITY WC": 0.0,
    "UNITY WC": 0.0,
    "WARRENSBURG WC": 0.0,
    "WEST FRANKFORT JR. WC": 0.0,
    "YOUNG CHAMPIONS": 0.0,
    "ZEE-BEE STINGERS": 0.0,
    "DU-PEC CARNIVORES": -1.0,
    "HERRIN WC": -1.0,
    "HOFFMAN ESTATES WC": -1.0,
    "MORTON YOUTH WRESTLING": -1.0,
    "NOTRE DAME WRESTLING": -1.0,
    "PLAINFIELD WC": -1.0,
    "RAMS WC": -1.0,
    "MARENGO WC": -2.0,
    "ST. CHARLES EAST WC": -2.0,
}
_NAME_FIXES: dict[str, str] = {
    "CHRIS SPANGLER": "CHRISTOPHER SPANGLER",
    "MIKE STEIN": "MICHAEL STEIN",
}
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("BEN STUCKEY III", "MT. VERNON LIONS"): bracket_utils.Competitor(
        full_name="BEN STUCKEY III",
        first_name="BEN",
        last_name="STUCKEY",
        team_full="MT. VERNON LIONS",
    ),
    ("BILLY BYRD IV", "SYCAMORE WC"): bracket_utils.Competitor(
        full_name="BILLY BYRD IV",
        first_name="BILLY",
        last_name="BYRD",
        team_full="SYCAMORE WC",
    ),
    ("BJ FUTRELL II", "HARVEY PARK DISTRICT TWISTERS"): bracket_utils.Competitor(
        full_name="BJ FUTRELL II",
        first_name="BJ",
        last_name="FUTRELL",
        team_full="HARVEY PARK DISTRICT TWISTERS",
    ),
    ("CURTIS CRIMS JR.", "BLAZER KIDS"): bracket_utils.Competitor(
        full_name="CURTIS CRIMS JR.",
        first_name="CURTIS",
        last_name="CRIMS",
        team_full="BLAZER KIDS",
    ),
    ("EDDIE LANCE III", "GRANITE CITY JR WARRIORS"): bracket_utils.Competitor(
        full_name="EDDIE LANCE III",
        first_name="EDDIE",
        last_name="LANCE",
        team_full="GRANITE CITY JR WARRIORS",
    ),
    ("GEORGE CANALES IV", "STERLING NEWMAN JR COMETS"): bracket_utils.Competitor(
        full_name="GEORGE CANALES IV",
        first_name="GEORGE",
        last_name="CANALES",
        team_full="STERLING NEWMAN JR COMETS",
    ),
    ("NICKBRAMHALL", "EDWARDSVILLE WC"): bracket_utils.Competitor(
        full_name="NICK BRAMHALL",
        first_name="NICK",
        last_name="BRAMHALL",
        team_full="EDWARDSVILLE WC",
    ),
}
TEAM_SCORE_EXCEPTIONS: dict[tuple[bracket_utils.Division, str], float] = {}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ARL": "ARLINGTON CARDINALS",
    "BAD": "BADGER WC",
    "BAH": "BARTLETT JR HAWKS",
    "BAT": "BATAVIA PINNERS",
    "BEL": "BELLEVILLE LITTLE DEVILS",
    "BIS": "BISON WC",
    "BLA": "BLACKHAWK WC",
    "BLZ": "BLAZER KIDS",
    "BRA": "BRAWLERS WC",
    "CAR": "CARBONDALE WC",
    "CAY": "CARY JR TROJAN MATMEN",
    "CHA": "CHAMPAIGN KIDS WRESTLING",
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLI DAWGS WC",
    "CRY": "CRYSTAL LAKE WIZARDS",
    "CUM": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DIX": "DIXON WC",
    "DOW": "DOWNERS GROVE COUGARS",
    "DUN": "DUNDEE HIGHLANDERS",
    "EDW": "EDWARDSVILLE WC",
    "FAL": "FALCON WC",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "FTN": "FIGHTIN TITAN WC",
    "GAL": "GALESBURG JR STREAKS",
    "GEE": "GENESEO WC",
    "GLN": "GLENBARD EAST JR RAMS",
    "GRA": "GRANITE CITY JR WARRIORS",
    "HAE": "HARVEY PARK DISTRICT TWISTERS",
    "HAR": "HARLEM COUGARS",
    "HER": "HERRIN WC",
    "HIG": "HIGHLAND BULLDOG JR WC",
    "HIN": "HINSDALE RED DEVIL WC",
    "HON": "HONONEGAH KIDS WC",
    "HOO": "HOOPESTON AREA WC",
    "JOL": "JOLIET BOYS CLUB COBRAS",
    "JRG": "JR. GOLDEN EAGLES",
    "JRS": "JR. SENTINELS",
    "JRX": "JR. SAXONS WC",
    "LAE": "LAKELAND PREDATORS",
    "LEM": "LEMONT BEARS WC",
    "LIM": "LIMESTONE YOUTH ROCKET WC",
    "LIN": "LINCOLN-WAY WC",
    "LIS": "LIL' STORM YOUTH WRESTLING",
    "LLC": "LITTLE CELTIC WC",
    "LLG": "LITTLE GIANTS WC",
    "LLV": "LITTLE VIKING WC OF H-F",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WC",
    "LWN": "PANTHER CUB WC",
    "MAF": "MARTINEZ FOX VALLEY ELITE WC",
    "MAT": "MATTOON YOUTH WC",
    "MEN": "MENDOTA MAT MASTERS",
    "MET": "METAMORA KIDS WC",
    "MID": "MIDWEST CENTRAL YOUTH",
    "MLM": "MORTON LITTLE MUSTANGS",
    "MOL": "MOLINE WC",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "NAP": "NAPERVILLE WC",
    "OAL": "OAK LAWN P.D. WILDCATS",
    "OAW": "OAKWOOD WC",
    "ORL": "ORLAND PARK PIONEERS",
    "PAN": "PANTHER WC",
    "PLA": "PLAINFIELD WC",
    "PLP": "PALATINE PANTHERS WC",
    "PLT": "PLAINFIELD TORNADOES WC",
    "POL": "POLO WC",
    "PRO": "PROVISO POWERHOUSE WC",
    "RIC": "RICH RATTLERS WC",
    "RIV": "RIVERBEND WC",
    "ROK": "ROCK ISLAND WC",
    "ROX": "ROXANA KIDS WC",
    "SCN": "SCN YOUTH WC",
    "SHA": "SHAMROCK WC",
    "SHB": "SHELBYVILLE JR RAMS WRESTLING",
    "SJO": "SJO SPARTAN YOUTH WC",
    "SYC": "SYCAMORE WC",
    "TAY": "TAYLORVILLE WC",
    "TIG": "TIGER WC",
    "TIN": "TINLEY PARK BULLDOGS",
    "TTT": "TIGERTOWN TANGLERS",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAU": "WAUBONSIE WC",
    "WET": "WESTVILLE YOUTH WC",
    "WHT": "WHEATON TIGER WC",
    "WOL": "WOLFPAK WC",
    "WRE": "WRESTLING FACTORY",
    "YOR": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ABC": "ALEDO BEAR COUNTRY WC",
    "ANI": "ANIMALS WC",
    "BAB": "BARRINGTON BRONCOS",
    "BET": "BETHALTO BULLS WC",
    "BLO": "BLOOMINGTON RAIDER WC",
    "BSH": "BISMARCK HENNING WC",
    "CEN": "CENTRAL WC",
    "DEK": "DEKALB WC",
    "DUR": "DU-PEC CARNIVORES",
    "ELP": "EL PASO WC",
    "ERI": "ERIE MIDDLE SCHOOL WC",
    "ERV": "ERVIN WC",
    "HOF": "HOFFMAN ESTATES WC",
    "JAC": "JACKSONVILLE WC",
    "LHI": "LIONHEART INTENSE WRESTLING",
    "LLH": "LITTLE HUSKIE WC",
    "LLI": "LITTLE INDIANS",
    "LOC": "LOCKPORT GATORS WC",
    "LRS": "LITTLE REDSKINS WC",
    "M-S": "M-S KIDS CLUB",
    "MAC": "MACOMB LITTLE BOMBERS",
    "MAI": "MAINE EAGLES WC",
    "MAR": "MARENGO WC",
    "MRT": "MORTON YOUTH WRESTLING",
    "NOT": "NOTRE DAME WRESTLING",
    "OAK": "OAK FOREST WARRIORS",
    "OFL": "O'FALLON LITTLE PANTHERS",
    "OSW": "OSWEGO PANTHERS",
    "PON": "PONTIAC PYTHONS",
    "PWR": "PANTHER POWERHOUSE WC",
    "RCK": "REED CUSTER KNIGHTS",
    "ROC": "ROCHELLE WC",
    "RVD": "RIVERDALE JR. RAMS WC",
    "SAU": "SAUKEE YOUTH WC",
    "SBA": "SILVER & BLACK ATTACK",
    "SCE": "ST. CHARLES EAST WC",
    "STR": "STERLING NEWMAN JR COMETS",
    "STT": "ST. TARCISSUS",
    "TKD": "TAKEDOWN WC",
    "TOM": "TOMCAT WC",
    "TRC": "TRI-CITY BRAVES",
    "UNI": "UNITY WC",
    "YNC": "YOUNG CHAMPIONS",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ARG": "ARGENTA / OREANA KIDS CLUB",
    "BEN": "BENTON JR WC",
    "BEV": "BELVIDERE BANDITS",
    "BSH": "BISMARCK HENNING WC",
    "CAL": "CARLINVILLE KIDS WC",
    "CHR": "CHARLESTON WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "FAC": "FALCON YOUTH WC",
    "GEV": "GENEVA WC",
    "GRD": "GRAPPLIN' DEVILS WC",
    "HIL": "HILLSBORO JR TOPPERS",
    "JRC": "JR. COUGARS WC",
    "JRM": "JR. MAROON WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAW": "LAWRENCE COUNTY WC",
    "MRS": "MORRISON STALLIONS WC",
    "MUS": "MUSTANG WC",
    "PJP": "PALATINE JUNIOR PIRATES",
    "RCM": "RICHMOND WC",
    "RCR": "ROCK RIDGE WC",
    "RDW": "ROAD WARRIORS",
    "ROF": "ROCKFORD WC",
    "SAV": "SAVANNA REDHAWKS",
    "SEN": "SENECA IRISH CADETS",
    "SHR": "SHERRARD JR WC",
    "SPR": "SPRINGFIELD CAPITAL KIDS WRESTLING",
    "STI": "STILLMAN VALLEY WC",
    "TBI": "T-BIRD RAIDER WRESTLING",
    "TRI": "TRIAD KNIGHTS",
    "TRV": "TREVIAN WC",
    "TWC": "TWIN CITY WC",
    "UNT": "UNITED TOWNSHIP WC",
    "VAN": "VANDALIA JR WRESTLING",
    "WAR": "WARRENSBURG WC",
    "WHM": "WHEATON MONROE EAGLES",
    "ZBS": "ZEE-BEE STINGERS",
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

    name = _NAME_FIXES.get(name, name)
    return bracket_utils.CompetitorRaw(
        name=name, team_full=_get_team_full(team, division)
    )


def parse_bout_result(value: str) -> str:
    # VERY SPECIAL CASES
    if value == "T-Fall 4:00; 15-0  Bout:   772|":
        return "T-Fall 4:00; 15-0"
    if value == "T-Fall 1:21; 17-2  Bout:   268|":
        return "T-Fall 1:21; 17-2"
    if value == "T-Fall 3:42; 18-2  Bout:   286|":
        return "T-Fall 3:42; 18-2"
    if value == " T-Fall 3:30:15-0  Bout:   432|":
        return "T-Fall 3:30:15-0"

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

    return bracket_utils.to_int_with_commas(parts[1])


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
    with open(_HERE / "2004" / division / filename) as file_obj:
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

    if division == "novice" and weight == 108:
        consolation_fifth_place_bottom_competitor = bracket_utils.CompetitorRaw(
            name="SEPEHR KALHOR", team_full="ROCK ISLAND WC"
        )
    else:
        consolation_fifth_place_bottom_competitor = parse_competitor(
            fifth_place_lines[2][:31]
        )

    if division == "novice" and weight == 166:
        consolation_round6_semi_01_top_competitor = bracket_utils.CompetitorRaw(
            name="RYAN GAINES", team_full="MARENGO WC"
        )
        consolation_fifth_place_top_competitor = bracket_utils.CompetitorRaw(
            name="RYAN GAINES", team_full="MARENGO WC"
        )
    else:
        consolation_round6_semi_01_top_competitor = parse_competitor(
            consolation_lines[0][93:124]
        )
        consolation_fifth_place_top_competitor = parse_competitor(
            fifth_place_lines[0][:31]
        )

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
            top_competitor=consolation_round6_semi_01_top_competitor,
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
            top_competitor=consolation_fifth_place_top_competitor,
            bottom_competitor=consolation_fifth_place_bottom_competitor,
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
    with open(_HERE / "extracted.2004.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
