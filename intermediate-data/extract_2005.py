# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
Note, there were 2 Novice competitors listed that do not show up in brackets:

- JACOB ANDERSON :: DUNDEE HIGHLANDERS (74)
  - Replaced by `JASON FUGIEL :: CRYSTAL LAKE WIZARDS`
- THOMAS PAVLOVICH :: YOUNG CHAMPIONS (166)
  - Replaced by `ZACH HOUGHTON :: DAKOTA WC`

and 7 Senior competitors listed that do not show up in brackets:

- IAN GAFFNEY :: HOOPESTON AREA WC (79) -- Scratched
- NATHAN FUNK :: METAMORA KIDS WC (79)
  - Replaced by `BROCK HILL :: BOYS & GIRLS CLUB OF PEKIN`
- CHRIS DARDANES :: FENWICK FALCONS WC (89)
  - Replaced by `JEFF SMITH :: VILLA LOMBARD COUGARS`
- MICHAEL RODRIQUEZ :: MURPHYSBORO WC (108) -- Scratched
- NICHOLAS POTTS :: LAWRENCE COUNTY WC (189) -- Scratched
- NATE WELCH :: FENWICK FALCONS WC (215)
  - Replaced by `CODY JONES :: MINOOKA LITTLE INDIANS`
- MIKE STONE :: SPRINGFIELD CAPITAL KIDS WRESTLING (275) -- Scratched

and 1 Senior competitor that was erroneously included in a bracket:

- SCOTT HELTON :: ELMHURST JR. DUKES (215)
  - He was actually in 275 (he was in both brackets)
"""

import functools
import pathlib

import bracket_utils
import bs4

_HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "LITTLE CELTIC WC": 210.5,
    "CRYSTAL LAKE WIZARDS": 138.0,
    "BLACKHAWK WC": 81.0,
    "HARVEY PARK DISTRICT TWISTERS": 81.0,
    "TINLEY PARK BULLDOGS": 74.5,
    "BISON WC": 69.0,
    "LEMONT BEARS WC": 69.0,
    "SAUKEE YOUTH WC": 61.0,
    "LAKELAND PREDATORS": 58.0,
    "VITTUM CATS": 56.0,
    "PLAINFIELD TORNADOES WC": 53.0,
    "DIXON WC": 52.0,
    "FOX VALLEY WC": 50.0,
    "GOLDEN EAGLES": 49.0,
    "MARTINEZ FOX VALLEY ELITE": 46.0,
    "GLADIATORS": 42.0,
    "BETHALTO BULLS WC": 41.0,
    "ROXANA KIDS WC": 40.5,
    "FIGHTIN TITAN WC": 40.0,
    "PLAINFIELD WC": 40.0,
    "MORTON LITTLE MUSTANGS": 35.0,
    "SONS OF THUNDER": 35.0,
    "TAKEDOWN WC": 34.0,
    "VILLA LOMBARD COUGARS": 34.0,
    "ARLINGTON CARDINALS": 33.0,
    "MT. PULASKI WC": 33.0,
    "WRESTLING FACTORY": 31.0,
    "DOWNERS GROVE COUGARS": 30.0,
    "HARLEM COUGARS": 30.0,
    "GENESEO WC": 29.0,
    "PROVISO POWERHOUSE WC": 29.0,
    "XTREME WRESTLING": 29.0,
    "YORKVILLE WC": 29.0,
    "EDWARDSVILLE WC": 28.0,
    "FENWICK FALCONS WC": 28.0,
    "MT. ZION WC": 28.0,
    "SCN YOUTH WC": 28.0,
    "JOLIET BOYS CLUB COBRAS": 27.0,
    "MAD DOG WRESTLING ACADEMY": 26.0,
    "MINOOKA LITTLE INDIANS": 24.0,
    "PANTHER CUB WC": 24.0,
    "GLENBARD EAST JR. RAMS": 23.0,
    "ORLAND PARK PIONEERS": 22.5,
    "RICH RATTLERS WC": 21.5,
    "BATAVIA PINNERS": 19.5,
    "BLOOMINGTON RAIDER WC": 18.0,
    "MURPHYSBORO WRESTLING": 18.0,
    "OSWEGO PANTERS": 18.0,
    "FALCON WC": 17.0,
    "OAK FOREST WARRIORS": 16.5,
    "CHILLI DAWGS WC": 16.0,
    "MAINE EAGLES WC": 16.0,
    "TOMCAT WC": 16.0,
    "HINSDALE RED DEVIL WC": 15.0,
    "VANDALIA JR. WRESTLING": 15.0,
    "MT. VERNON LIONS": 14.5,
    "PEORIA RAZORBACKS YOUTH WC": 13.0,
    "WEST HANCOCK WC": 13.0,
    "CHAMPAIGN KIDS WRESTLING": 12.0,
    "HERRIN WC": 12.0,
    "TEAM WEST WOLVES": 12.0,
    "CENTRAL WC": 11.0,
    "HIGHLAND BULLDOG JR WC": 11.0,
    "DAKOTA WC": 10.0,
    "WHEATON TIGER WC": 10.0,
    "DUNDEE HIGHLANDERS": 9.0,
    "CUMBERLAND YOUTH WC": 8.0,
    "FAIRMONT ROUGH RIDERS": 8.0,
    "O'FALLON LITTLE PANTHERS": 8.0,
    "OAK LAWN P.D. WILDCATS": 8.0,
    "TRIAD LITTLE KNIGHTS": 8.0,
    "CARY JR. TROJAN MATMEN": 7.0,
    "LINCOLN-WAY WC": 7.0,
    "CROSSTOWN CRUSHERS": 6.0,
    "GC JR WARRIORS": 6.0,
    "LIL' STORM YOUTH WRESTLING": 6.0,
    "LITTLE FALCONS WC": 6.0,
    "SPIDER WC": 6.0,
    "ACES WC": 4.0,
    "BELLEVILLE LITTLE DEVILS": 4.0,
    "CARBONDALE JUNIOR SPIRITS": 4.0,
    "FALCON YOUTH WC": 4.0,
    "HOOPESTON AREA WC": 4.0,
    "LOCKPORT JR PORTERS WC": 4.0,
    "MUSTANG WC": 4.0,
    "PANTHER POWERHOUSE WC": 4.0,
    "RIVERBEND WC": 4.0,
    "SHERRARD JR WC": 4.0,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": 4.0,
    "TRI-VALLEY WC": 4.0,
    "MIDWEST CENTRAL YOUTH": 3.5,
    "BARRINGTON BRONCOS": 3.0,
    "CLIPPER WC": 3.0,
    "MACOMB LITTLE BOMBERS": 3.0,
    "PONTIAC PYTHONS": 3.0,
    "COLLINSVILLE RAIDERS": 2.0,
    "MARENGO INDIANS YOUTH WRESTLING": 2.0,
    "MORTON YOUTH WRESTLING": 2.0,
    "SHAMROCK WC": 2.0,
    "TIGER WC": 2.0,
    "WOLFPAK WC": 2.0,
    "BISMARK HENNING WC": 1.0,
    "ELMHURST JR. DUKES": 1.0,
    "A-J JUNIOR WILDCATS": 0.0,
    "ALEDO BEAR COUNTRY WC": 0.0,
    "ALLEMAN JR PIONEER WC": 0.0,
    "ANIMALS WC": 0.0,
    "BADGER WC": 0.0,
    "BARTLETT JR. HAWKS": 0.0,
    "CALUMET MEMORIAL P.D. WOLVERINES": 0.0,
    "CARLINVILLE KIDS WC": 0.0,
    "CHARLESTON WC": 0.0,
    "EL PASO / GRIDLEY WC": 0.0,
    "ERIE MIDDLE SCHOOL WC": 0.0,
    "FISHER WC": 0.0,
    # "HARVARD WC": 0.0, # TODO: DELETE
    "HIGHLAND PARK LITTLE GIANTS": 0.0,
    "HILLSBORO JR. TOPPERS": 0.0,
    "HONONEGAH KIDS WC": 0.0,
    "HURRICANES": 0.0,
    "KNIGHTS WRESTLING": 0.0,
    "LIONHEART INTENSE WRESTLING": 0.0,
    "LIONS WC": 0.0,
    "MEDALIST WC": 0.0,
    "MOLINE WC": 0.0,
    "MORRISON STALLIONS WC": 0.0,
    "NAPERVILLE WC": 0.0,
    "NOTRE DAME WRESTLING": 0.0,
    "OAKWOOD WC": 0.0,
    "PANTHER WC": 0.0,
    "BOYS & GIRLS CLUB OF PEKIN": 0.0,
    "RICHMOND WC": 0.0,
    "RIVERDALE JR RAMS WC": 0.0,
    "ROCHELLE WC": 0.0,
    "ROCHESTER WC": 0.0,
    "SAUK VALLEY WC": 0.0,
    "SHELBYVILLE JR RAMS WRESTLING": 0.0,
    "SJO SPARTAN YOUTH WC": 0.0,
    "ST. TARCISSUS": 0.0,
    "TAYLORVILLE WC": 0.0,
    "TIGERTOWN TANGLERS": 0.0,
    "UNITY WC": 0.0,
    "WARREN COUNTY WC": 0.0,
    "WASHINGTON JR. PANTHERS": 0.0,
    "WESTVILLE YOUTH WC": 0.0,
    "YOUNG CHAMPIONS": 0.0,
    "BRAWLERS WC": -1.0,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "FOX VALLEY WC": 186.0,
    "VITTUM CATS": 142.0,
    "MARTINEZ FOX VALLEY ELITE": 141.5,
    "HARVEY PARK DISTRICT TWISTERS": 137.5,
    "BLACKHAWK WC": 120.0,
    "ARLINGTON CARDINALS": 82.5,
    "LITTLE CELTIC WC": 81.0,
    "DIXON WC": 73.0,
    "VILLA LOMBARD COUGARS": 72.0,
    "FENWICK FALCONS WC": 70.0,
    "ORLAND PARK PIONEERS": 69.0,
    "PLAINFIELD TORNADOES WC": 64.5,
    "PANTHER WC": 64.0,
    "HONONEGAH KIDS WC": 59.0,
    "BADGER WC": 54.0,
    "EDWARDSVILLE WC": 49.0,
    "MURPHYSBORO WRESTLING": 48.0,
    "GENESEO WC": 45.0,
    "TINLEY PARK BULLDOGS": 44.0,
    "RIVERDALE JR RAMS WC": 41.0,
    "ROXANA KIDS WC": 41.0,
    "CROSSTOWN CRUSHERS": 40.0,
    "HARLEM COUGARS": 40.0,
    "YORKVILLE WC": 40.0,
    "ROCK ISLAND WC": 39.0,
    "LITTLE FALCONS WC": 35.0,
    "CRYSTAL LAKE WIZARDS": 33.0,
    "MAINE EAGLES WC": 33.0,
    "BRAWLERS WC": 32.0,
    "WESTVILLE YOUTH WC": 30.0,
    "ARGENTA / OREANA KIDS CLUB": 28.0,
    "BELLEVILLE LITTLE DEVILS": 28.0,
    "GOLDEN EAGLES": 28.0,
    "GC JR WARRIORS": 28.0,
    "STILLMAN VALLEY WC": 28.0,
    "FISHER WC": 27.5,
    "DOWNERS GROVE COUGARS": 27.0,
    "DAKOTA WC": 25.0,
    "TIGER WC": 25.0,
    "BELVIDERE BANDITS": 24.0,
    "SCN YOUTH WC": 24.0,
    "ST. CHARLES EAST WC": 24.0,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": 23.0,
    "BATAVIA PINNERS": 22.0,
    "COLLINSVILLE RAIDERS": 21.0,
    "SHAMROCK WC": 21.0,
    "OSWEGO PANTERS": 20.0,
    "WHEATON TIGER WC": 20.0,
    "HOFFMAN ESTATES WC": 18.0,
    "L-P CRUNCHING CAVS": 18.0,
    "LAKELAND PREDATORS": 18.0,
    "MEDALIST WC": 17.0,
    "WRESTLING FACTORY": 17.0,
    "IMPACT WC": 16.0,
    "LITTLE HUSKIE WC": 16.0,
    "ROCKFORD WC": 16.0,
    "SAVANNA REDHAWKS": 15.0,
    "SONS OF THUNDER": 15.0,
    "UNITED TOWNSHIP WC": 14.0,
    "MARENGO INDIANS YOUTH WRESTLING": 13.0,
    "EFFINGHAM JUNIOR WRESTLING TEAM": 12.0,
    "OAK FOREST WARRIORS": 12.0,
    "FALCON YOUTH WC": 11.0,
    "GLADIATORS": 11.0,
    "HIGHLAND BULLDOG JR WC": 10.5,
    "BETHALTO BULLS WC": 10.0,
    "O'FALLON LITTLE PANTHERS": 10.0,
    "PANTHER POWERHOUSE WC": 10.0,
    "PROVISO POWERHOUSE WC": 10.0,
    "SYCAMORE WC": 10.0,
    "WARRENSBURG WC": 9.0,
    "GEORGETOWN RUDEDOGS YOUTH WC": 8.0,
    "GERMANTOWN WC": 8.0,
    "LIL' STORM YOUTH WRESTLING": 8.0,
    "LITTLE REDBIRD WC": 8.0,
    "CHILLI DAWGS WC": 7.0,
    "CUMBERLAND YOUTH WC": 7.0,
    "EL PASO / GRIDLEY WC": 7.0,
    "PONTIAC PYTHONS": 7.0,
    "HERRIN WC": 6.0,
    "MENDOTA MAT MASTERS": 6.0,
    "MOLINE WC": 6.0,
    "XTREME WRESTLING": 6.0,
    "LEMONT BEARS WC": 5.0,
    "PALATINE PANTHERS WC": 5.0,
    "SJO SPARTAN YOUTH WC": 5.0,
    "BLACK KATS WC": 4.0,
    "CARBONDALE JUNIOR SPIRITS": 4.0,
    "CENTRALIA": 4.0,
    "FALCON WC": 4.0,
    "HIGHLAND PARK LITTLE GIANTS": 4.0,
    "HINSDALE RED DEVIL WC": 4.0,
    "JR. VIKINGS": 4.0,
    "MAD DOG WRESTLING ACADEMY": 4.0,
    "MATTOON YOUTH WC": 4.0,
    "OAK LAWN P.D. WILDCATS": 4.0,
    "PRAIRIE CENTRAL-CHENOA HAWKS": 4.0,
    "SENECA IRISH CADETS": 4.0,
    "SHELBYVILLE JR RAMS WRESTLING": 4.0,
    "BISON WC": 3.0,
    "CHAMPAIGN KIDS WRESTLING": 3.0,
    "HILLSBORO JR. TOPPERS": 3.0,
    "ROCK RIDGE WC": 3.0,
    "TREVIAN WC": 3.0,
    "BARRINGTON BRONCOS": 2.0,
    "DUNDEE HIGHLANDERS": 2.0,
    "PANTHER CUB WC": 2.0,
    "TRI-VALLEY WC": 2.0,
    "UNITY WC": 2.0,
    "A-J JUNIOR WILDCATS": 0.0,
    "ANIMALS WC": 0.0,
    "BENTON JR. WC": 0.0,
    "BLOOMINGTON RAIDER WC": 0.0,
    "CALUMET MEMORIAL P.D. WOLVERINES": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "ERVIN WC": 0.0,
    "GLENBARD EAST JR. RAMS": 0.0,
    # "HARVARD WC": 0.0, # TODO: DELETE
    "HOOPESTON AREA WC": 0.0,
    "HURRICANES": 0.0,
    "JR. COUGARS WC": 0.0,
    "JUNIOR MUSTANGS": 0.0,
    "LANCER WC": 0.0,
    "LAWRENCE COUNTY WC": 0.0,
    "LINCOLN-WAY WC": 0.0,
    "LIONHEART INTENSE WRESTLING": 0.0,
    "LITTLE BOILER WC": 0.0,
    "LITTLE REDSKINS WC": 0.0,
    "LOCKPORT JR PORTERS WC": 0.0,
    "METAMORA KIDS WC": 0.0,
    "MORRISON STALLIONS WC": 0.0,
    "NAPERVILLE WC": 0.0,
    "NOTRE DAME WRESTLING": 0.0,
    "OAKWOOD WC": 0.0,
    "BOYS & GIRLS CLUB OF PEKIN": 0.0,
    "PLAINFIELD WC": 0.0,
    "RAMS WC": 0.0,
    "RICHMOND WC": 0.0,
    "RIVERBEND WC": 0.0,
    "ROAD WARRIORS": 0.0,
    "SAUK VALLEY WC": 0.0,
    "SAUKEE YOUTH WC": 0.0,
    "ST. TARCISSUS": 0.0,
    "TEAM WEST WOLVES": 0.0,
    "TIGERTOWN TANGLERS": 0.0,
    "TRIAD LITTLE KNIGHTS": 0.0,
    "VANDALIA JR. WRESTLING": 0.0,
    "WAUBONSIE WC": 0.0,
    "WOLFPAK WC": 0.0,
    # "ZEE-BEE STINGERS": 0.0, # TODO: DELETE
    "MINOOKA LITTLE INDIANS": -1.0,
    "MORTON LITTLE MUSTANGS": -1.0,
}
_NAME_FIXES: dict[str, str] = {
    "JOEL RANGEL": "JOEL RANGLE",
}
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("ALVIN FOSTER III", "HARVEY PARK DISTRICT TWISTERS"): bracket_utils.Competitor(
        full_name="ALVIN FOSTER III",
        first_name="ALVIN",
        last_name="FOSTER",
        team_full="HARVEY PARK DISTRICT TWISTERS",
    ),
    ("ANTWYONE BROWN JR.", "RICH RATTLERS WC"): bracket_utils.Competitor(
        full_name="ANTWYONE BROWN JR.",
        first_name="ANTWYONE",
        last_name="BROWN",
        team_full="RICH RATTLERS WC",
    ),
    ("CARL FORESIDE JR.", "GLADIATORS"): bracket_utils.Competitor(
        full_name="CARL FORESIDE JR.",
        first_name="CARL",
        last_name="FORESIDE",
        team_full="GLADIATORS",
    ),
    ("CURTIS CRIMS JR.", "CROSSTOWN CRUSHERS"): bracket_utils.Competitor(
        full_name="CURTIS CRIMS JR.",
        first_name="CURTIS",
        last_name="CRIMS",
        team_full="CROSSTOWN CRUSHERS",
    ),
    ("J. ALEXANDER GONZALEZ", "A-J JUNIOR WILDCATS"): bracket_utils.Competitor(
        full_name="J. ALEXANDER GONZALEZ",
        first_name="J. ALEXANDER",
        last_name="GONZALEZ",
        team_full="A-J JUNIOR WILDCATS",
    ),
    ("MALIK - JABRI TAYLOR", "HARVEY PARK DISTRICT TWISTERS"): bracket_utils.Competitor(
        full_name="MALIK - JABRI TAYLOR",
        first_name="MALIK - JABRI",
        last_name="TAYLOR",
        team_full="HARVEY PARK DISTRICT TWISTERS",
    ),
    ("TYRONE  SALLY JR.", "PROVISO POWERHOUSE WC"): bracket_utils.Competitor(
        full_name="TYRONE  SALLY JR.",
        first_name="TYRONE",
        last_name="SALLY",
        team_full="PROVISO POWERHOUSE WC",
    ),
}
TEAM_SCORE_EXCEPTIONS: dict[tuple[bracket_utils.Division, str], float] = {}
TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "AJW": "A-J JUNIOR WILDCATS",
    "ANI": "ANIMALS WC",
    "ARL": "ARLINGTON CARDINALS",
    "BAT": "BATAVIA PINNERS",
    "BDG": "BADGER WC",
    "BKH": "BLACKHAWK WC",
    "BLD": "BELLEVILLE LITTLE DEVILS",
    "BLM": "BLOOMINGTON RAIDER WC",
    "BRL": "BRAWLERS WC",
    "BRR": "BARRINGTON BRONCOS",
    "BSN": "BISON WC",
    "BTB": "BETHALTO BULLS WC",
    "CHM": "CHAMPAIGN KIDS WRESTLING",
    "CJS": "CARBONDALE JUNIOR SPIRITS",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "CMB": "CUMBERLAND YOUTH WC",
    "CTC": "CROSSTOWN CRUSHERS",
    "CVR": "COLLINSVILLE RAIDERS",
    "DAK": "DAKOTA WC",
    "DDH": "DUNDEE HIGHLANDERS",
    "DGC": "DOWNERS GROVE COUGARS",
    "DIX": "DIXON WC",
    "EDW": "EDWARDSVILLE WC",
    "EJD": "ELMHURST JR. DUKES",
    "EPG": "EL PASO / GRIDLEY WC",
    "FCY": "FALCON YOUTH WC",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FLC": "FALCON WC",
    "FOX": "FOX VALLEY WC",
    "GEN": "GENESEO WC",
    "GER": "GLENBARD EAST JR. RAMS",
    "GLA": "GLADIATORS",
    "GLD": "GOLDEN EAGLES",
    "HBJ": "HIGHLAND BULLDOG JR WC",
    "HER": "HERRIN WC",
    "HJT": "HILLSBORO JR. TOPPERS",
    "HON": "HONONEGAH KIDS WC",
    "HPG": "HIGHLAND PARK LITTLE GIANTS",
    "HPN": "HOOPESTON AREA WC",
    "HRD": "HINSDALE RED DEVIL WC",
    "HRL": "HARLEM COUGARS",
    "HTW": "HARVEY PARK DISTRICT TWISTERS",
    "LAK": "LAKELAND PREDATORS",
    "LEM": "LEMONT BEARS WC",
    "LHI": "LIONHEART INTENSE WRESTLING",
    "LJP": "LOCKPORT JR PORTERS WC",
    "LLC": "LITTLE CELTIC WC",
    "LLF": "LITTLE FALCONS WC",
    "LLS": "LIL' STORM YOUTH WRESTLING",
    "LNW": "LINCOLN-WAY WC",
    "MDW": "MAD DOG WRESTLING ACADEMY",
    "MED": "MEDALIST WC",
    "MFV": "MARTINEZ FOX VALLEY ELITE",
    "MIY": "MARENGO INDIANS YOUTH WRESTLING",
    "MLI": "MINOOKA LITTLE INDIANS",
    "MNE": "MAINE EAGLES WC",
    "MOL": "MOLINE WC",
    "MRB": "MURPHYSBORO WRESTLING",
    "MRS": "MORRISON STALLIONS WC",
    "NDW": "NOTRE DAME WRESTLING",
    "NPV": "NAPERVILLE WC",
    "OFW": "OAK FOREST WARRIORS",
    "OKW": "OAKWOOD WC",
    "OLP": "O'FALLON LITTLE PANTHERS",
    "OLW": "OAK LAWN P.D. WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTERS",
    "PAN": "PANTHER WC",
    "PEK": "BOYS & GIRLS CLUB OF PEKIN",
    "PLF": "PLAINFIELD WC",
    "PLT": "PLAINFIELD TORNADOES WC",
    "PLW": "PANTHER CUB WC",
    "PNP": "PANTHER POWERHOUSE WC",
    "PON": "PONTIAC PYTHONS",
    "PRP": "PROVISO POWERHOUSE WC",
    "RJR": "RIVERDALE JR RAMS WC",
    "RMD": "RICHMOND WC",
    "ROX": "ROXANA KIDS WC",
    "RVB": "RIVERBEND WC",
    "SCN": "SCN YOUTH WC",
    "SHM": "SHAMROCK WC",
    "SJO": "SJO SPARTAN YOUTH WC",
    "SJR": "SHELBYVILLE JR RAMS WRESTLING",
    "SKE": "SAUKEE YOUTH WC",
    "SKV": "SAUK VALLEY WC",
    "SOT": "SONS OF THUNDER",
    "SPR": "SPRINGFIELD CAPITAL KIDS WRESTLING",
    "STT": "ST. TARCISSUS",
    "TIG": "TIGER WC",
    "TLK": "TRIAD LITTLE KNIGHTS",
    "TPB": "TINLEY PARK BULLDOGS",
    "TRV": "TRI-VALLEY WC",
    "TTT": "TIGERTOWN TANGLERS",
    "TWW": "TEAM WEST WOLVES",
    "UNY": "UNITY WC",
    "VAN": "VANDALIA JR. WRESTLING",
    "VIT": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGARS",
    "WHT": "WHEATON TIGER WC",
    "WPK": "WOLFPAK WC",
    "WRF": "WRESTLING FACTORY",
    "WSV": "WESTVILLE YOUTH WC",
    "XTR": "XTREME WRESTLING",
    "YRK": "YORKVILLE WC",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ABC": "ALEDO BEAR COUNTRY WC",
    "ACE": "ACES WC",
    "AJP": "ALLEMAN JR PIONEER WC",
    "BJH": "BARTLETT JR. HAWKS",
    "BMH": "BISMARK HENNING WC",
    "CHR": "CHARLESTON WC",
    "CJT": "CARY JR. TROJAN MATMEN",
    "CLD": "CHILLI DAWGS WC",
    "CLP": "CLIPPER WC",
    "CNT": "CENTRAL WC",
    "CRL": "CARLINVILLE KIDS WC",
    "EMS": "ERIE MIDDLE SCHOOL WC",
    "FRR": "FAIRMONT ROUGH RIDERS",
    "FTT": "FIGHTIN TITAN WC",
    "GCW": "GC JR WARRIORS",
    "JBC": "JOLIET BOYS CLUB COBRAS",
    "KGT": "KNIGHTS WRESTLING",
    "LNS": "LIONS WC",
    "MLB": "MACOMB LITTLE BOMBERS",
    "MLM": "MORTON LITTLE MUSTANGS",
    "MRT": "MORTON YOUTH WRESTLING",
    "MST": "MUSTANG WC",
    "MTP": "MT. PULASKI WC",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MWC": "MIDWEST CENTRAL YOUTH",
    "PRZ": "PEORIA RAZORBACKS YOUTH WC",
    "RCL": "ROCHELLE WC",
    "RCT": "ROCHESTER WC",
    "RRT": "RICH RATTLERS WC",
    "SPD": "SPIDER WC",
    "SRD": "SHERRARD JR WC",
    "TAK": "TAKEDOWN WC",
    "TAY": "TAYLORVILLE WC",
    "TOM": "TOMCAT WC",
    "WHN": "WEST HANCOCK WC",
    "WJP": "WASHINGTON JR. PANTHERS",
    "WRC": "WARREN COUNTY WC",
    "YNG": "YOUNG CHAMPIONS",
}
SENIOR_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ARG": "ARGENTA / OREANA KIDS CLUB",
    "BKT": "BLACK KATS WC",
    "BLV": "BELVIDERE BANDITS",
    "BTN": "BENTON JR. WC",
    "CLA": "CENTRALIA",
    "CLD": "CHILLI DAWGS WC",
    "CMW": "CALUMET MEMORIAL P.D. WOLVERINES",
    "EFF": "EFFINGHAM JUNIOR WRESTLING TEAM",
    "ERV": "ERVIN WC",
    "GCW": "GC JR WARRIORS",
    "GRM": "GERMANTOWN WC",
    "GRY": "GEORGETOWN RUDEDOGS YOUTH WC",
    "HOF": "HOFFMAN ESTATES WC",
    "HUR": "HURRICANES",
    "IMP": "IMPACT WC",
    "JCG": "JR. COUGARS WC",
    "JMS": "JUNIOR MUSTANGS",
    "JVK": "JR. VIKINGS",
    "LAN": "LANCER WC",
    "LLB": "LITTLE BOILER WC",
    "LLH": "LITTLE HUSKIE WC",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WC",
    "LRS": "LITTLE REDSKINS WC",
    "MAT": "MATTOON YOUTH WC",
    "MEN": "MENDOTA MAT MASTERS",
    "PCC": "PRAIRIE CENTRAL-CHENOA HAWKS",
    "PLP": "PALATINE PANTHERS WC",
    "RAM": "RAMS WC",
    "RDW": "ROAD WARRIORS",
    "RKF": "ROCKFORD WC",
    "RKI": "ROCK ISLAND WC",
    "RKR": "ROCK RIDGE WC",
    "SAV": "SAVANNA REDHAWKS",
    "SCE": "ST. CHARLES EAST WC",
    "SIC": "SENECA IRISH CADETS",
    "STV": "STILLMAN VALLEY WC",
    "SYC": "SYCAMORE WC",
    "TVN": "TREVIAN WC",
    "UNT": "UNITED TOWNSHIP WC",
    "WBN": "WAUBONSIE WC",
    "WRB": "WARRENSBURG WC",
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
    if value.endswith("|"):
        value = value[:-1]

    # SPECIAL CASES
    if value.startswith("T-Fall "):
        value = f" {value} "

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
    with open(_HERE / "2005" / division / filename) as file_obj:
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
    with open(_HERE / "extracted.2005.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
