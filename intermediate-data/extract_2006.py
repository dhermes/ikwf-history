# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "HARVEY PARK DIST TWISTERS": 193.5,
    "LITTLE CELTIC WC": 142.5,
    "CRYSTAL LAKE WIZARDS": 97.0,
    "VITTUM CATS": 94.5,
    "GOMEZ WRESTLING ACADEMY": 90.5,
    "SONS OF THUNDER": 80.0,
    "MARTINEZ FOX VALLEY ELITE": 79.0,
    "VILLA LOMBARD COUGARS": 75.5,
    "FOX VALLEY WC": 75.0,
    "WRESTLING FACTORY": 69.5,
    "ARLINGTON CARDINALS": 67.0,
    "FAIRMONT ROUGH RIDERS": 62.0,
    "ORLAND PARK PIONEERS": 55.5,
    "BETHALTO BULLS WC": 51.0,
    "DOWNERS GROVE COUGARS": 48.0,
    "LEMONT BEARS WC": 47.0,
    "BELLEVILLE LITTLE DEVILS": 44.0,
    "HINSDALE RED DEVIL WC": 41.0,
    "OAK FOREST WARRIORS": 40.0,
    "RIVERBEND WC": 37.0,
    "HARLEM COUGARS": 34.0,
    "BELVIDERE BANDITS": 31.0,
    "MORTON LITTLE MUSTANGS": 31.0,
    "MT. ZION WC": 31.0,
    "BISON WC": 30.0,
    "EDWARDSVILLE WC": 30.0,
    "RIVERDALE JR. RAMS WC": 30.0,
    "COLLINSVILLE RAIDERS": 29.0,
    "OAK LAWN P.D. WILDCATS": 29.0,
    "FALCON WRESTLING CLUB": 28.0,
    "GOLDEN EAGLES": 25.0,
    "MOLINE WC": 25.0,
    "FIGHTIN TITAN WC": 24.0,
    "PEORIA RAZORBACKS YOUTH WC": 23.0,
    "PRAIRIE CENTRAL-CHENOA HAWKS": 23.0,
    "SYCAMORE WC": 23.0,
    "TINLEY PARK BULLDOGS": 23.0,
    "YORKVILLE WRESTLING CLUB": 22.0,
    "EL PASO/GRIDLEY WC": 21.0,
    "SJO SPARTAN YOUTH WC": 21.0,
    "LITTLE FALCONS WC": 20.5,
    "IRON MAN": 20.0,
    "LOCKPORT JR PORTERS WC": 20.0,
    "NOTRE DAME WRESTLING": 19.5,
    "MINOOKA LITTLE INDIANS": 19.0,
    "ROMEOVILLE WC": 18.0,
    "ACES WC": 17.0,
    "BLOOMINGTON RAIDER WC": 15.0,
    "CARBONDALE WC": 15.0,
    "HIGHLAND BULLDOG JR WC": 15.0,
    "TAYLORVILLE WC": 15.0,
    "CHAMPAIGN KIDS WRESTLING": 14.5,
    "CROSSTOWN CRUSHERS": 13.0,
    "DUNDEE HIGHLANDERS": 13.0,
    "PLAINFIELD WC": 13.0,
    "SCN YOUTH WC": 12.0,
    "WASHINGTON JR PANTHERS": 12.0,
    "BLACKHAWK WC": 11.0,
    "ELMHURST JR. DUKES": 10.0,
    "HONONEGAH KIDS WC": 10.0,
    "TRIAD LITTLE KNIGHTS": 10.0,
    "CHICAGO CRUSADERS": 9.0,
    "ERIE MIDDLE SCHOOL WC": 9.0,
    "SPIDER WC": 9.0,
    "VANDALIA JR WRESTLING": 9.0,
    "HERRIN JUNIOR WC": 8.0,
    "MORRISON STALLIONS WC": 8.0,
    "MT. VERNON LIONS": 8.0,
    "PONTIAC PYTHONS": 8.0,
    "PROVISO POWERHOUSE WC": 8.0,
    "SAUK VALLEY WRESTLING CLUB": 8.0,
    "UNITY WC": 7.0,
    "DAKOTA WC": 6.0,
    "WARRENSBURG WC": 6.0,
    "XTREME WRESTLING": 5.5,
    "CENTRAL WRESTLING CLUB": 5.0,
    "BATAVIA": 4.0,
    "CALUMET MEMORIAL PD WOLVERINES": 4.0,
    "DIXON WC": 4.0,
    "EFFINGHAM JUNIOR WRESTLING TEAM": 4.0,
    "FENWICK FALCONS WC": 4.0,
    "HIGHLAND PARK LITTLE GIANTS": 4.0,
    "LAKELAND PREDATORS": 4.0,
    "LIMESTONE YOUTH WC": 4.0,
    "MAINE EAGLES WC": 4.0,
    "MORTON YOUTH WRESTLING": 4.0,
    "QUINCY WC": 4.0,
    "ROCK ISLAND WC": 4.0,
    "WHEATON TIGER WC": 4.0,
    "HILLTOPPERS WC": 3.0,
    "MARENGO INDIANS YOUTH WRESTLING": 3.0,
    "RICH RATTLERS WC": 3.0,
    "CARY JR TROJAN MATMEN": 2.0,
    "GENESEO SPIDER WC": 2.0,
    "L-P CRUNCHING CAVS": 2.0,
    "LITTLE HUSKIE WC": 2.0,
    "SHAMROCK WC": 2.0,
    "JUNIOR GATORS WC": 1.0,
    "ALEDO BEAR COUNTRY WC": 0.0,
    "BADGER WC": 0.0,
    "BENTON JR WC": 0.0,
    "BRAWLERS WC": 0.0,
    "CHICAGO WOLVES DEN": 0.0,
    "CLIPPER WC": 0.0,
    "CUMBERLAND YOUTH WC": 0.0,
    "DEKALB WC": 0.0,
    "FALCON YOUTH WC": 0.0,
    "GLEN ELLYN DUNGEON WC": 0.0,
    "HOOPESTON AREA WC": 0.0,
    "IMPACT WC": 0.0,
    "LANCER WC": 0.0,
    "LINCOLN-WAY WC": 0.0,
    "LIONHEART INTENSE WRESTLING": 0.0,
    "LITCHFIELD KIDS WRESTLING": 0.0,
    "LITTLE REDBIRD WC": 0.0,
    "LITTLE REDSKINS WC": 0.0,
    "M-S KIDS CLUB": 0.0,
    "MACOMB LITTLE BOMBERS": 0.0,
    "MATTOON YOUTH WC": 0.0,
    "MCLEAN COUNTY WC": 0.0,
    "METAMORA KIDS WC": 0.0,
    "MIDWEST CENTRAL YOUTH": 0.0,
    "NAPERVILLE WC": 0.0,
    "OAKWOOD WC": 0.0,
    "OSWEGO PANTHERS": 0.0,
    "PANTHER POWERHOUSE WC": 0.0,
    "RICHMOND WRESTLING CLUB": 0.0,
    "ROAD WARRIORS": 0.0,
    "ROCHESTER WC": 0.0,
    "SHARKS WC": 0.0,
    "SHELBYVILLE JR RAMS WRESTLING": 0.0,
    "STOCKTON RENEGADES": 0.0,
    "TIGER WC": 0.0,
    "TIGERTOWN TANGLERS": 0.0,
    "TREVIAN WC": 0.0,
    "VERMILION VALLEY ELITE": 0.0,
    "VILLA PARK YOUNG WARRIORS": 0.0,
    "WAUKEGAN YOUTH WC": 0.0,
    "WESTVILLE YOUTH WC": 0.0,
    "WOLFPAK WC": 0.0,
    "JOLIET JUNIOR STEELMEN": -1.0,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "SONS OF THUNDER": 199.0,
    "FOX VALLEY WC": 124.5,
    "VITTUM CATS": 124.5,
    "MARTINEZ FOX VALLEY ELITE": 114.0,
    "LITTLE CELTIC WC": 103.0,
    "CRYSTAL LAKE WIZARDS": 100.0,
    "EDWARDSVILLE WC": 90.0,
    "BLACKHAWK WC": 88.0,
    "HARLEM COUGARS": 77.0,
    "PLAINFIELD WC": 70.0,
    "SCN YOUTH WC": 66.0,
    "SAUKEE YOUTH WC": 64.0,
    "BATAVIA PINNERS": 63.0,
    "GOMEZ WRESTLING ACADEMY": 62.0,
    "ORLAND PARK PIONEERS": 56.0,
    "MOLINE WC": 55.0,
    "GLADIATORS": 53.0,
    "GENESEO SPIDER WC": 50.0,
    "FIGHTIN TITAN WC": 45.0,
    "FENWICK FALCONS WC": 44.5,
    "PANTHER/REDHAWK WC": 44.0,
    "MT. ZION WC": 43.0,
    "POLO WC": 43.0,
    "HERRIN JUNIOR WC": 38.5,
    "MINOOKA LITTLE INDIANS": 35.0,
    "HECOX TEAM BENAIAH": 33.0,
    "TINLEY PARK BULLDOGS": 32.5,
    "BISON WC": 32.0,
    "LITTLE FALCONS WC": 32.0,
    "PANTHER POWERHOUSE WC": 32.0,
    "HONONEGAH KIDS WC": 31.0,
    "MURPHYSBORO WRESTLING": 29.0,
    "OAK LAWN P.D. WILDCATS": 28.5,
    "VILLA LOMBARD COUGARS": 28.0,
    "JOLIET JUNIOR STEELMEN": 26.5,
    "NAPERVILLE WC": 26.5,
    "RICH RATTLERS WC": 26.0,
    "COLLINSVILLE RAIDERS": 25.5,
    "OAK FOREST WARRIORS": 25.0,
    "YORKVILLE WRESTLING CLUB": 25.0,
    "BISMARCK HENNING WRESTLING CLUB": 24.0,
    "CHAMPAIGN KIDS WRESTLING": 24.0,
    "GOLDEN EAGLES": 24.0,
    "WRESTLING FACTORY": 24.0,
    "HARVEY PARK DIST TWISTERS": 23.0,
    "ARLINGTON CARDINALS": 22.0,
    "MAD DOG WRESTLING ACADEMY": 20.0,
    "BENTON JR WC": 19.0,
    "SHAMROCK WC": 19.0,
    "FALCON WRESTLING CLUB": 18.0,
    "GLENBARD EAST JR RAMS": 18.0,
    "HINSDALE RED DEVIL WC": 17.0,
    "STILLMAN VALLEY WC": 17.0,
    "CARY JR TROJAN MATMEN": 16.0,
    "CROSSTOWN CRUSHERS": 16.0,
    "MT. PULASKI WC": 16.0,
    "PROVISO POWERHOUSE WC": 15.0,
    "LAKELAND PREDATORS": 14.0,
    "TOMCAT WC": 14.0,
    "LOCKPORT JR PORTERS WC": 13.0,
    "MAINE EAGLES WC": 13.0,
    "DIXON WC": 12.0,
    "JUNIOR VIKINGS": 12.0,
    "RIVERBEND WC": 11.5,
    "KNIGHTS WRESTLING": 11.0,
    "LEMONT BEARS WC": 11.0,
    "MORTON YOUTH WRESTLING": 11.0,
    "O'FALLON LITTLE PANTHERS": 11.0,
    "SHELBYVILLE JR RAMS WRESTLING": 11.0,
    "SJO SPARTAN YOUTH WC": 11.0,
    "LINCOLN-WAY WC": 10.0,
    "LITTLE HUSKIE WC": 10.0,
    "MIDWEST CENTRAL YOUTH": 10.0,
    "NOTRE DAME WRESTLING": 10.0,
    "TRIAD LITTLE KNIGHTS": 10.0,
    "DAKOTA WC": 9.0,
    "HIGHLAND BULLDOG JR WC": 9.0,
    "HIGHLAND PARK LITTLE GIANTS": 9.0,
    "FISHER WC": 8.0,
    "MUSTANG WC": 8.0,
    "WHEATON TIGER WC": 8.0,
    "OAKWOOD WC": 7.0,
    "SYCAMORE WC": 7.0,
    "TREVIAN WC": 7.0,
    "HOFFMAN ESTATES WC": 6.0,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": 6.0,
    "ALLEMAN JR PIONEERS": 4.0,
    "ARGENTA/OREANA KIDS CLUB": 4.0,
    "ERIE MIDDLE SCHOOL WC": 4.0,
    "GC JR WARRIORS": 4.0,
    "GRAPPLIN' DEVILS WRESTLING CLUB": 4.0,
    "LIONHEART INTENSE WRESTLING": 4.0,
    "PANTHER CUB WRESTLING CLUB": 4.0,
    "PEORIA RAZORBACKS YOUTH WC": 4.0,
    "ROCHESTER WC": 4.0,
    "SENECA IRISH CADETS": 4.0,
    "TEAM WEST WOLVES": 4.0,
    "TIGER WC": 4.0,
    "UNITY WC": 4.0,
    "WOLFPAK WC": 4.0,
    "CUMBERLAND YOUTH WC": 3.0,
    "ELMHURST JR. DUKES": 3.0,
    "MT. VERNON LIONS": 2.5,
    "BELLEVILLE LITTLE DEVILS": 2.0,
    "BETHALTO BULLS WC": 2.0,
    "EL PASO/GRIDLEY WC": 2.0,
    "LIMESTONE YOUTH WC": 2.0,
    "ST. CHARLES EAST WC": 2.0,
    "TAYLORVILLE WC": 2.0,
    "IRON MAN": -1.0,
}
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("AARON BREWTON II", "WAUK"): bracket_utils.Competitor(
        full_name="AARON BREWTON II",
        first_name="AARON",
        last_name="BREWTON",
        team_full="WAUKEGAN YOUTH WC",
    ),
    ("ALVIN FOSTER III", "HPDT"): bracket_utils.Competitor(
        full_name="ALVIN FOSTER III",
        first_name="ALVIN",
        last_name="FOSTER",
        team_full="HARVEY PARK DIST TWISTERS",
    ),
    ("ANTHONY FERRARIS JR", "MNE"): bracket_utils.Competitor(
        full_name="ANTHONY FERRARIS JR",
        first_name="ANTHONY",
        last_name="FERRARIS",
        team_full="MAINE EAGLES WC",
    ),
    ("ANTWYONE BROWN JR.", "CRST"): bracket_utils.Competitor(
        full_name="ANTWYONE BROWN JR.",
        first_name="ANTWYONE",
        last_name="BROWN",
        team_full="CROSSTOWN CRUSHERS",
    ),
    ("BRENDAN TYLER HALL", "HPDT"): bracket_utils.Competitor(
        full_name="BRENDAN TYLER HALL",
        first_name="BRENDAN TYLER",
        last_name="HALL",
        team_full="HARVEY PARK DIST TWISTERS",
    ),
    ("CURTIS CRIMS JR.", "CRST"): bracket_utils.Competitor(
        full_name="CURTIS CRIMS JR.",
        first_name="CURTIS",
        last_name="CRIMS",
        team_full="CROSSTOWN CRUSHERS",
    ),
    ("GEORGE CANALES IV", "DIX"): bracket_utils.Competitor(
        full_name="GEORGE CANALES IV",
        first_name="GEORGE",
        last_name="CANALES",
        team_full="DIXON WC",
    ),
    ("JIM JERNIGAN JR.", "MOL"): bracket_utils.Competitor(
        full_name="JIM JERNIGAN JR.",
        first_name="JIM",
        last_name="JERNIGAN",
        team_full="MOLINE WC",
    ),
    ("JOSE MANUEL DEAVILA", "COL"): bracket_utils.Competitor(
        full_name="JOSE MANUEL DEAVILA",
        first_name="JOSE MANUEL",
        last_name="DEAVILA",
        team_full="COLLINSVILLE RAIDERS",
    ),
    ("LUSIANO JR. CANTU", "GOM"): bracket_utils.Competitor(
        full_name="LUSIANO JR. CANTU",
        first_name="LUSIANO",
        last_name="CANTU",
        team_full="GOMEZ WRESTLING ACADEMY",
    ),
    ("MATTHEW SCHEFKE JR.", "NAP"): bracket_utils.Competitor(
        full_name="MATTHEW SCHEFKE JR.",
        first_name="MATTHEW",
        last_name="SCHEFKE",
        team_full="NAPERVILLE WC",
    ),
    ("ROSS FERRARO III", "GOM"): bracket_utils.Competitor(
        full_name="ROSS FERRARO III",
        first_name="ROSS",
        last_name="FERRARO",
        team_full="GOMEZ WRESTLING ACADEMY",
    ),
    ("TRAVIS BUCHANAN / WILL", "HPDT"): bracket_utils.Competitor(
        full_name="TRAVIS BUCHANAN / WILL",
        first_name="TRAVIS / WILL",
        last_name="BUCHANAN",
        team_full="HARVEY PARK DIST TWISTERS",
    ),
    ("TYRONE  SALLY JR.", "HPDT"): bracket_utils.Competitor(
        full_name="TYRONE  SALLY JR.",
        first_name="TYRONE",
        last_name="SALLY",
        team_full="HARVEY PARK DIST TWISTERS",
    ),
    ("WARDELL ROSEMAN JR.", "DUN"): bracket_utils.Competitor(
        full_name="WARDELL ROSEMAN JR.",
        first_name="WARDELL",
        last_name="ROSEMAN",
        team_full="DUNDEE HIGHLANDERS",
    ),
}
TEAM_SCORE_EXCEPTIONS: dict[tuple[bracket_utils.Division, str], float] = {}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ACE": "ACES WC",  # Absent from Senior team scores
    "ARL": "ARLINGTON CARDINALS",
    "BB": "BETHALTO BULLS WC",
    "BEN": "BENTON JR WC",
    "BHK": "BLACKHAWK WC",
    "BIS": "BISON WC",
    "BLD": "BELLEVILLE LITTLE DEVILS",
    "CARY": "CARY JR TROJAN MATMEN",
    "CKW": "CHAMPAIGN KIDS WRESTLING",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "CMB": "CUMBERLAND YOUTH WC",
    "COL": "COLLINSVILLE RAIDERS",
    "CRB": "CARBONDALE WC",  # Absent from Senior team scores
    "CRST": "CROSSTOWN CRUSHERS",
    "DAK": "DAKOTA WC",
    "DIX": "DIXON WC",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM JUNIOR WRESTLING TEAM",  # Absent from Senior team scores
    "ELM": "ELMHURST JR. DUKES",
    "EPG": "EL PASO/GRIDLEY WC",
    "ERIE": "ERIE MIDDLE SCHOOL WC",
    "FEN": "FENWICK FALCONS WC",
    "FOX": "FOX VALLEY WC",
    "FTT": "FIGHTIN TITAN WC",
    "FWC": "FALCON WRESTLING CLUB",
    "FYW": "FALCON YOUTH WC",  # Absent from Senior team scores
    "GE": "GOLDEN EAGLES",
    "GEN": "GENESEO SPIDER WC",
    "GOM": "GOMEZ WRESTLING ACADEMY",
    "HON": "HONONEGAH KIDS WC",
    "HPDT": "HARVEY PARK DIST TWISTERS",
    "HPLG": "HIGHLAND PARK LITTLE GIANTS",
    "HPN": "HOOPESTON AREA WC",
    "HRD": "HINSDALE RED DEVIL WC",
    "HRL": "HARLEM COUGARS",
    "HRR": "HERRIN JUNIOR WC",
    "IMP": "IMPACT WC",
    "IRN": "IRON MAN",
    "JJS": "JOLIET JUNIOR STEELMEN",
    "LAN": "LANCER WC",
    "LEM": "LEMONT BEARS WC",
    "LIM": "LIMESTONE YOUTH WC",
    "LIW": "LIONHEART INTENSE WRESTLING",
    "LJP": "LOCKPORT JR PORTERS WC",
    "LKP": "LAKELAND PREDATORS",
    "LLC": "LITTLE CELTIC WC",
    "LLF": "LITTLE FALCONS WC",
    "LLH": "LITTLE HUSKIE WC",
    "LLRS": "LITTLE REDSKINS WC",
    "LPC": "L-P CRUNCHING CAVS",
    "LWW": "LINCOLN-WAY WC",
    "MCC": "MCLEAN COUNTY WC",  # Absent from Senior team scores
    "MFV": "MARTINEZ FOX VALLEY ELITE",
    "MIN": "MINOOKA LITTLE INDIANS",
    "MLM": "MORTON LITTLE MUSTANGS",
    "MNE": "MAINE EAGLES WC",
    "MOL": "MOLINE WC",
    "MRS": "MORRISON STALLIONS WC",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MWC": "MIDWEST CENTRAL YOUTH",
    "MYW": "MORTON YOUTH WRESTLING",
    "NAP": "NAPERVILLE WC",
    "NDW": "NOTRE DAME WRESTLING",
    "OFW": "OAK FOREST WARRIORS",
    "OKW": "OAKWOOD WC",
    "OLW": "OAK LAWN P.D. WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTHERS",  # Absent from Senior team scores
    "PLNF": "PLAINFIELD WC",
    "PNP": "PANTHER POWERHOUSE WC",
    "PON": "PONTIAC PYTHONS",
    "PRY": "PEORIA RAZORBACKS YOUTH WC",
    "PVP": "PROVISO POWERHOUSE WC",
    "RCH": "RICHMOND WRESTLING CLUB",
    "RKI": "ROCK ISLAND WC",
    "ROC": "ROCHESTER WC",
    "ROM": "ROMEOVILLE WC",
    "RRT": "RICH RATTLERS WC",
    "RVB": "RIVERBEND WC",
    "SCN": "SCN YOUTH WC",
    "SHM": "SHAMROCK WC",
    "SJO": "SJO SPARTAN YOUTH WC",
    "SKV": "SAUK VALLEY WRESTLING CLUB",  # Absent from Senior team scores
    "SLB": "SHELBYVILLE JR RAMS WRESTLING",
    "SOT": "SONS OF THUNDER",
    "SYC": "SYCAMORE WC",
    "TAY": "TAYLORVILLE WC",
    "TIG": "TIGER WC",
    "TLK": "TRIAD LITTLE KNIGHTS",
    "TPB": "TINLEY PARK BULLDOGS",
    "TRV": "TREVIAN WC",
    "TTT": "TIGERTOWN TANGLERS",  # Absent from Senior team scores
    "UNI": "UNITY WC",
    "VIT": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGARS",
    "WES": "WESTVILLE YOUTH WC",  # Absent from Senior team scores
    "WLP": "WOLFPAK WC",
    "WRF": "WRESTLING FACTORY",
    "WTG": "WHEATON TIGER WC",
    "YKV": "YORKVILLE WRESTLING CLUB",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ABC": "ALEDO BEAR COUNTRY WC",
    "BAT": "BATAVIA",
    "BDGR": "BADGER WC",
    "BELV": "BELVIDERE BANDITS",
    "BLM": "BLOOMINGTON RAIDER WC",
    "BRL": "BRAWLERS WC",
    "CCR": "CHICAGO CRUSADERS",
    "CENT": "CENTRAL WRESTLING CLUB",
    "CMW": "CALUMET MEMORIAL PD WOLVERINES",
    "CWD": "CHICAGO WOLVES DEN",
    "DEK": "DEKALB WC",
    "DGC": "DOWNERS GROVE COUGARS",
    "DUN": "DUNDEE HIGHLANDERS",
    "FRR": "FAIRMONT ROUGH RIDERS",
    "GED": "GLEN ELLYN DUNGEON WC",
    "HBD": "HIGHLAND BULLDOG JR WC",
    "HILL": "HILLTOPPERS WC",
    "JRG": "JUNIOR GATORS WC",
    "LIT": "LITCHFIELD KIDS WRESTLING",
    "LLRB": "LITTLE REDBIRD WC",
    "MAT": "MATTOON YOUTH WC",
    "MET": "METAMORA KIDS WC",
    "MIY": "MARENGO INDIANS YOUTH WRESTLING",
    "MLB": "MACOMB LITTLE BOMBERS",
    "MSK": "M-S KIDS CLUB",
    "PCCH": "PRAIRIE CENTRAL-CHENOA HAWKS",
    "QUI": "QUINCY WC",
    "RDW": "ROAD WARRIORS",
    "RJR": "RIVERDALE JR. RAMS WC",
    "SHR": "SHARKS WC",
    "SPI": "SPIDER WC",
    "SRN": "STOCKTON RENEGADES",
    "VAN": "VANDALIA JR WRESTLING",
    "VER": "VERMILION VALLEY ELITE",
    "VPYW": "VILLA PARK YOUNG WARRIORS",
    "WAR": "WARRENSBURG WC",
    "WAS": "WASHINGTON JR PANTHERS",
    "WAUK": "WAUKEGAN YOUTH WC",
    "XTR": "XTREME WRESTLING",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "AGO": "ARGENTA/OREANA KIDS CLUB",
    "AJP": "ALLEMAN JR PIONEERS",
    "ANI": "ANIMALS WC",
    "BAT": "BATAVIA PINNERS",
    "BMH": "BISMARCK HENNING WRESTLING CLUB",
    "CHAR": "CHARLESTON WC",  # Absent from Senior team scores
    "CLD": "CHILLI DAWGS WC",
    "FISH": "FISHER WC",
    "GCW": "GC JR WARRIORS",
    "GEJR": "GLENBARD EAST JR RAMS",
    "GLD": "GLADIATORS",
    "GPD": "GRAPPLIN' DEVILS WRESTLING CLUB",
    "HBG": "HIGHLAND BULLDOG JR WC",
    "HCX": "HECOX TEAM BENAIAH",
    "HOF": "HOFFMAN ESTATES WC",
    "HUR": "HURRICANES",
    "JRC": "JR. COUGARS WC",
    "JRV": "JUNIOR VIKINGS",
    "KNGT": "KNIGHTS WRESTLING",
    "LION": "LIONS WC",
    "MDWA": "MAD DOG WRESTLING ACADEMY",
    "MEN": "MENDOTA WC",  # Absent from Senior team scores
    "MST": "MUSTANG WC",
    "MTP": "MT. PULASKI WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "OLP": "O'FALLON LITTLE PANTHERS",
    "PAL": "PALATINE PANTHERS",  # Absent from Senior team scores
    "PCUB": "PANTHER CUB WRESTLING CLUB",
    "PNRD": "PANTHER/REDHAWK WC",
    "POLO": "POLO WC",
    "RCK": "REED CUSTER KNIGHTS",  # Absent from Senior team scores
    "REN": "RENEGADES",
    "RKFD": "ROCKFORD WC",  # Absent from Senior team scores
    "RRDG": "ROCKRIDGE WC",  # Absent from Senior team scores
    "SAU": "SAUKEE YOUTH WC",
    "SCE": "ST. CHARLES EAST WC",
    "SEN": "SENECA IRISH CADETS",
    "SIUT": "SOUTHERN ILLINOIS UNITED THUNDER CATS",  # Absent from Senior team scores
    "SPR": "SPRINGFIELD CAPITAL KIDS WRESTLING",
    "SV": "STILLMAN VALLEY WC",
    "TOM": "TOMCAT WC",
    "TRI": "TRI-VALLEY WC",  # Absent from Senior team scores
    "TWW": "TEAM WEST WOLVES",
    "WAUB": "WAUBONSIE WC",  # Absent from Senior team scores
    "WHT": "WEST HANCOCK WC",  # Absent from Senior team scores
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

    if len(team) not in (1, 2, 3, 4):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return bracket_utils.CompetitorRaw(
        name=name,
        team_full=_get_team_full(team, division),
        team_acronym=team,
    )


def parse_bout_result(value: str) -> str:
    if value.endswith("|"):
        value = value[:-1]

    # SPECIAL CASES
    if value.startswith("T-Fall "):
        value = f" {value} "
    if value.startswith("-Fall "):
        value = f" {value[1:]} "

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
    with open(_HERE / "2006" / division / filename) as file_obj:
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
    with open(_HERE / "extracted.2006.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
