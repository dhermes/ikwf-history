# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 35
TEAM_SCORE_ID_START = 875
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
    "FAL": "FALCON WRESTLING CLUB",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "FTN": "FIGHTIN TITAN WC",
    "GAL": "GALESBURG JR STREAKS",
    "GEE": "GENESEO WC",
    "GLN": "GLENBARD EAST JR RAMS",
    "GRA": "GRANITE CITY JR WARRIORS",
    "HAE": "HARVEY PARK DIST TWISTERS",
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
    "LWN": "PANTHER CUB WRESTLING CLUB",
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
    "ROX": "ROXANA KIDS WRESTLING CLUB",
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
    "YOR": "YORKVILLE WRESTLING CLUB",
}
# NOTE: Sometimes acronyms (or team names) differ between Novice and Senior
#       in the Team Scores.
NOVICE_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "ABC": "ALEDO BEAR COUNTRY WC",
    "ANI": "ANIMALS WC",
    "BAB": "BARRINGTON BRONCOS",
    "BET": "BETHALTO BULLS WC",
    "BLO": "BLOOMINGTON RAIDER WC",
    "BSH": "BISMARK-HENNING",
    "CEN": "CENTRAL WRESTLING CLUB",
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
    "ARG": "ARGENTA/OREANA KIDS CLUB",
    "BEN": "BENTON JR WC",
    "BEV": "BELVIDERE BANDITS",
    "BSH": "BISMARCK HENNING WRESTLING CLUB",
    "CAL": "CARLINVILLE KIDS WC",
    "CHR": "CHARLESTON WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "FAC": "FALCON YOUTH WC",
    "GEV": "GENEVA WC",
    "GRD": "GRAPPLIN' DEVILS",
    "HIL": "HILLSBORO JR TOPPERS",
    "JRC": "JR. COUGARS WC",
    "JRM": "JR. MAROON WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAW": "LAWRENCE COUNTY WC",
    "MRS": "MORRISON STALLIONS WC",
    "MUS": "MUSTANG WC",
    "PJP": "PALATINE JUNIOR PIRATES",
    "RCM": "RICHMOND WRESTLING CLUB",
    "RCR": "ROCK RIDGE WC",
    "RDW": "ROAD WARRIORS",
    "ROF": "ROCKFORD WC",
    "SAV": "SAVANNA REDHAWKS",
    "SEN": "SENECA IRISH CADETS",
    "SHR": "SHERRARD JR WC",
    "SPR": "SPRINGFIELD CAPITALS",
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
TEAM_NAME_MAPPING: dict[str, int] = {
    "ACES WC": 3,
    "ALEDO BEAR COUNTRY WC": 10002,
    "ALLEMAN JR PIONEER WC": 10003,
    "ANIMALS WC": 10004,
    "ARGENTA/OREANA KIDS CLUB": 8,
    "ARLINGTON CARDINALS": 9,
    "BADGER WC": 14,
    "BARRINGTON BRONCOS": 15,
    "BARTLETT JR HAWKS": 16,
    "BATAVIA PINNERS": 10005,
    "BELLEVILLE LITTLE DEVILS": 23,
    "BELVIDERE BANDITS": 24,
    "BENTON JR WC": 26,
    "BETHALTO BULLS WC": 10006,
    "BISMARCK HENNING WRESTLING CLUB": 28,
    "BISMARK-HENNING": 28,
    "BISON WC": 126,
    "BLACK KATS WC": 10007,
    "BLACKHAWK WC": 30,
    "BLAZER KIDS": 10008,
    "BLOOMINGTON RAIDER WC": 32,
    "BOYS & GIRLS CLUB OF PEKIN": 319,
    "BRAWLERS WC": 39,
    "CALUMET MEMORIAL P.D. WOLVERINES": 49,
    "CARBONDALE WC": 53,
    "CARLINVILLE KIDS WC": 54,
    "CARY JR TROJAN MATMEN": 59,
    "CENTRAL WRESTLING CLUB": 10010,
    "CENTRALIA YOUTH WRESTLING": 64,
    "CHAMPAIGN KIDS WRESTLING": 65,
    "CHARLESTON WC": 69,
    "CHATHAM WC": 604,
    "CHENOA MAT CATS": 10011,
    "CHICAGO BULLDOG WC": 10012,
    "CHICAGO KNIGHTS": 10013,
    "CHICAGO WOLVES DEN": 75,
    "CHILLI DAWGS WC": 10014,
    "CLINTON WC": 79,
    "CLIPPER WC": 80,
    "COAL CITY KIDS WC": 10015,
    "CRIMSON HEAT WC": 10017,
    "CROSSFACE WRESTLING": 10018,
    "CRYSTAL LAKE WIZARDS": 89,
    "CUMBERLAND YOUTH WC": 90,
    "DAKOTA WC": 92,
    "DEKALB WC": 96,
    "DIXON WC": 98,
    "DOWNERS GROVE COUGARS": 100,
    "DU-PEC CARNIVORES": 10020,
    "DUNDEE HIGHLANDERS": 102,
    "DUNGEON WC": 103,
    "DWIGHT WC": 106,
    "EDWARDSVILLE WC": 110,
    "EFFINGHAM YOUTH WC": 111,
    "EL PASO WC": 10022,
    "ELGIN MIGHTY MAROONS": 10023,
    "ELMHURST JR. DUKES": 10024,
    "ERIE MIDDLE SCHOOL WC": 10025,
    "ERVIN WC": 10026,
    "FAIRMONT ROUGH RIDERS": 10027,
    "FALCON WRESTLING CLUB": 124,
    "FALCON YOUTH WC": 123,
    "FENWICK FALCONS WC": 10028,
    "FIGHTIN TITAN WC": 128,
    "FISHER WC": 130,
    "FOX VALLEY WC": 134,
    "GALESBURG JR STREAKS": 10030,
    "GENESEO WC": 10033,
    "GENEVA WC": 10034,
    "GLENBARD EAST JR RAMS": 147,
    "GRANITE CITY JR WARRIORS": 10040,
    "GRAPPLIN' DEVILS": 153,
    "HARLEM COUGARS": 10041,
    "HARVARD WC": 161,
    "HARVEY PARK DIST TWISTERS": 162,
    "HERRIN WC": 10042,
    "HIGHLAND BULLDOG JR WC": 168,
    "HILLSBORO JR TOPPERS": 170,
    "HILLTOPPERS WC": 10044,
    "HINSDALE RED DEVIL WC": 171,
    "HOFFMAN ESTATES WC": 172,
    "HONONEGAH KIDS WC": 173,
    "HOOPESTON AREA WC": 174,
    "HURRICANES": 10045,
    "ILLINI BLUFFS WC": 181,
    "ILLINI WC": 182,
    "JACKSONVILLE WC": 189,
    "JOLIET BOYS CLUB COBRAS": 10047,
    "JR. COUGARS WC": 196,
    "JR. GOLDEN EAGLES": 10050,
    "JR. MAROON WC": 538,
    "JR. SAXONS WC": 10053,
    "JR. SENTINELS": 10054,
    "JUNIOR BULLDOGS": 194,
    "JUNK YARD DOGS": 205,
    "KISHWAUKEE WC": 10056,
    "KNIGHTS WRESTLING": 206,
    "L-P CRUNCHING CAVS": 241,
    "LAKELAND PREDATORS": 10057,
    "LANCER WC": 216,
    "LAWRENCE COUNTY WC": 217,
    "LEMONT BEARS WC": 219,
    "LEROY WRESTLING KIDS CLUB": 10058,
    "LIL' STORM YOUTH WRESTLING": 10060,
    "LIMESTONE YOUTH ROCKET WC": 10061,
    "LINCOLN WC": 226,
    "LINCOLN-WAY WC": 227,
    "LIONHEART INTENSE WRESTLING": 228,
    "LIONS WC": 229,
    "LITCHFIELD KIDS WRESTLING": 231,
    "LITTLE BOILER WC": 232,
    "LITTLE CELTIC WC": 233,
    "LITTLE FALCONS WC": 10062,
    "LITTLE GIANTS WC": 641,
    "LITTLE HUSKIE WC": 235,
    "LITTLE INDIANS": 10063,
    "LITTLE REDBIRD WC": 10065,
    "LITTLE REDSKINS WC": 10066,
    "LITTLE VIKING WC OF H-F": 10067,
    "LOCKPORT GATORS WC": 10068,
    "M-S KIDS CLUB": 10069,
    "MACOMB LITTLE BOMBERS": 243,
    "MAINE EAGLES WC": 245,
    "MANTENO JR. PANTHERS": 247,
    "MARENGO WC": 248,
    "MARTINEZ FOX VALLEY ELITE WC": 250,
    "MATTOON YOUTH WC": 252,
    "MENDOTA MAT MASTERS": 10072,
    "METAMORA KIDS WC": 262,
    "MIDWEST CENTRAL YOUTH": 263,
    "MOLINE WC": 268,
    "MONTICELLO KIDS WC": 269,
    "MORRISON STALLIONS WC": 270,
    "MORTON LITTLE MUSTANGS": 271,
    "MORTON YOUTH WRESTLING": 272,
    "MT. VERNON LIONS": 275,
    "MT. ZION WC": 276,
    "MURPHYSBORO WRESTLING": 278,
    "MUSTANG WC": 279,
    "NAPERVILLE WC": 281,
    "NORTHSHORE GATORS": 10074,
    "NOTRE DAME WRESTLING": 295,
    "O'FALLON LITTLE PANTHERS": 296,
    "OAK FOREST WARRIORS": 297,
    "OAK LAWN P.D. WILDCATS": 10075,
    "OAKWOOD WC": 299,
    "OLY WC": 304,
    "ORLAND PARK PIONEERS": 306,
    "OSWEGO PANTHERS": 10076,
    "OVERTIME SCHOOL OF WRESTLING": 309,
    "PALATINE JUNIOR PIRATES": 10077,
    "PALATINE PANTHERS WC": 10078,
    "PANTHER CUB WRESTLING CLUB": 10079,
    "PANTHER POWERHOUSE WC": 313,
    "PANTHER WC": 346,
    "PEORIA HEIGHTS MINUTEMEN": 320,
    "PEORIA RAZORBACKS YOUTH WC": 321,
    "PLAINFIELD TORNADOES WC": 10081,
    "PLAINFIELD WC": 326,
    "POLO WC": 327,
    "PONTIAC PYTHONS": 10082,
    "PROVISO POWERHOUSE WC": 314,
    "QUINCY WC": 336,
    "RAMS WC": 236,
    "REED CUSTER KNIGHTS": 10085,
    "RENEGADES": 10086,
    "RICH RATTLERS WC": 349,
    "RICHMOND WRESTLING CLUB": 350,
    "RIVERBEND WC": 354,
    "RIVERDALE JR. RAMS WC": 536,
    "ROAD WARRIORS": 357,
    "ROCHELLE WC": 358,
    "ROCK ISLAND WC": 361,
    "ROCK RIDGE WC": 10088,
    "ROCKFORD WC": 364,
    "ROMEOVILLE WC": 368,
    "ROXANA KIDS WRESTLING CLUB": 371,
    "SAUKEE YOUTH WC": 376,
    "SAVANNA REDHAWKS": 10089,
    "SCN YOUTH WC": 377,
    "SENECA IRISH CADETS": 379,
    "SHAMROCK WC": 380,
    "SHARKS WC": 381,
    "SHELBYVILLE JR RAMS WRESTLING": 382,
    "SHERRARD JR WC": 383,
    "SILVER & BLACK ATTACK": 10090,
    "SJO SPARTAN YOUTH WC": 402,
    "SOMONAUK WC": 387,
    "SOUTHERN ILLINOIS UNITED THUNDER CATS": 10093,
    "SPIDER WC": 10094,
    "SPRINGFIELD CAPITALS": 397,
    "ST. BEDE'S": 10095,
    "ST. CHARLES EAST WC": 10096,
    "ST. TARCISSUS": 403,
    "STATELINE WILDCATS": 10097,
    "STERLING NEWMAN JR COMETS": 10098,
    "STILLMAN VALLEY WC": 407,
    "SYCAMORE WC": 418,
    "T-BIRD RAIDER WRESTLING": 10099,
    "TAKEDOWN WC": 10100,
    "TAYLORVILLE WC": 420,
    "TEAM WEST WOLVES": 10101,
    "THE ZOO WC": 10102,
    "TIGER WC": 10103,
    "TIGERTOWN TANGLERS": 441,
    "TINLEY PARK BULLDOGS": 443,
    "TITAN WC": 128,
    "TOMCAT WC": 448,
    "TREVIAN WC": 288,
    "TRI-CITY BRAVES": 10104,
    "TRIAD KNIGHTS": 452,
    "TWIN CITY WC": 10106,
    "UNITED TOWNSHIP WC": 10107,
    "UNITY WC": 457,
    "VANDALIA JR WRESTLING": 461,
    "VILLA LOMBARD COUGARS": 10109,
    "VITTUM CATS": 466,
    "WARREN COUNTY WC": 467,
    "WARRENSBURG WC": 468,
    "WASHINGTON JR PANTHERS": 10110,
    "WAUBONSIE WC": 473,
    "WEST FRANKFORT JR. WC": 478,
    "WESTVILLE YOUTH WC": 482,
    "WHEATON MONROE EAGLES": 10114,
    "WHEATON TIGER WC": 483,
    "WILMINGTON WC": 488,
    "WOLFPAK WC": 490,
    "WRESTLING FACTORY": 10115,
    "YORKVILLE WRESTLING CLUB": 497,
    "YOUNG CHAMPIONS": 10116,
    "ZEE-BEE STINGERS": 501,
}
NOVICE_EXTRA_TEAM_SCORES: dict[str, float] = {
    "ACES WC": 0.0,
    "ALLEMAN JR PIONEER WC": 0.0,
    "BENTON JR WC": 0.0,
    "BLACK KATS WC": 0.0,
    "BOYS & GIRLS CLUB OF PEKIN": 0.0,
    "CALUMET MEMORIAL P.D. WOLVERINES": 0.0,
    "CARLINVILLE KIDS WC": 0.0,
    "CENTRALIA YOUTH WRESTLING": 0.0,
    "CHARLESTON WC": 0.0,
    "CHATHAM WC": 0.0,
    "CHICAGO BULLDOG WC": 0.0,
    "CHICAGO KNIGHTS": 0.0,
    "CHICAGO WOLVES DEN": 0.0,
    "CLINTON WC": 0.0,
    "CLIPPER WC": 0.0,
    "COAL CITY KIDS WC": 0.0,
    "CRIMSON HEAT WC": 0.0,
    "CROSSFACE WRESTLING": 0.0,
    "DUNGEON WC": 0.0,
    "DWIGHT WC": 0.0,
    "EFFINGHAM YOUTH WC": 0.0,
    "ELGIN MIGHTY MAROONS": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "FAIRMONT ROUGH RIDERS": 0.0,
    "FALCON YOUTH WC": 0.0,
    "GENEVA WC": 0.0,
    "HARVARD WC": 0.0,
    "HILLSBORO JR TOPPERS": 0.0,
    "HILLTOPPERS WC": 0.0,
    "HURRICANES": 0.0,
    "ILLINI BLUFFS WC": 0.0,
    "ILLINI WC": 0.0,
    "JR. COUGARS WC": 0.0,
    "JR. MAROON WC": 0.0,
    "JUNIOR BULLDOGS": 0.0,
    "JUNK YARD DOGS": 0.0,
    "KISHWAUKEE WC": 0.0,
    "LANCER WC": 0.0,
    "LAWRENCE COUNTY WC": 0.0,
    "LEROY WRESTLING KIDS CLUB": 0.0,
    "LINCOLN WC": 0.0,
    "LIONS WC": 0.0,
    "LITCHFIELD KIDS WRESTLING": 0.0,
    "LITTLE BOILER WC": 0.0,
    "LITTLE FALCONS WC": 0.0,
    "MANTENO JR. PANTHERS": 0.0,
    "MONTICELLO KIDS WC": 0.0,
    "MORRISON STALLIONS WC": 0.0,
    "MUSTANG WC": 0.0,
    "NORTHSHORE GATORS": 0.0,
    "OLY WC": 0.0,
    "OVERTIME SCHOOL OF WRESTLING": 0.0,
    "PALATINE JUNIOR PIRATES": 0.0,
    "PEORIA HEIGHTS MINUTEMEN": 0.0,
    "PEORIA RAZORBACKS YOUTH WC": 0.0,
    "QUINCY WC": 0.0,
    "RAMS WC": 0.0,
    "RENEGADES": 0.0,
    "RICHMOND WRESTLING CLUB": 0.0,
    "ROAD WARRIORS": 0.0,
    "ROCK RIDGE WC": 0.0,
    "ROCKFORD WC": 0.0,
    "ROMEOVILLE WC": 0.0,
    "SAVANNA REDHAWKS": 0.0,
    "SENECA IRISH CADETS": 0.0,
    "SHARKS WC": 0.0,
    "SHERRARD JR WC": 0.0,
    "SOMONAUK WC": 0.0,
    "SOUTHERN ILLINOIS UNITED THUNDER CATS": 0.0,
    "SPIDER WC": 0.0,
    "ST. BEDE'S": 0.0,
    "STATELINE WILDCATS": 0.0,
    "STILLMAN VALLEY WC": 0.0,
    "T-BIRD RAIDER WRESTLING": 0.0,
    "TEAM WEST WOLVES": 0.0,
    "THE ZOO WC": 0.0,
    "TITAN WC": 0.0,
    "TREVIAN WC": 0.0,
    "TRIAD KNIGHTS": 0.0,
    "TWIN CITY WC": 0.0,
    "UNITED TOWNSHIP WC": 0.0,
    "WARREN COUNTY WC": 0.0,
    "WARRENSBURG WC": 0.0,
    "WASHINGTON JR PANTHERS": 0.0,
    "WEST FRANKFORT JR. WC": 0.0,
    "WHEATON MONROE EAGLES": 0.0,
    "WILMINGTON WC": 0.0,
    "ZEE-BEE STINGERS": 0.0,
    ########################################
    "ARGENTA/OREANA KIDS CLUB": -1.0,
    "BELVIDERE BANDITS": -1.0,
    "KNIGHTS WRESTLING": -1.0,
    "SPRINGFIELD CAPITALS": -1.0,
    ########################################
    "VANDALIA JR WRESTLING": -2.0,
}
SENIOR_EXTRA_TEAM_SCORES: dict[str, float] = {
    "ACES WC": 0.0,
    "ALEDO BEAR COUNTRY WC": 0.0,
    "ALLEMAN JR PIONEER WC": 0.0,
    "ANIMALS WC": 0.0,
    "BARRINGTON BRONCOS": 0.0,
    "BETHALTO BULLS WC": 0.0,
    "BLACK KATS WC": 0.0,
    "BLOOMINGTON RAIDER WC": 0.0,
    "BOYS & GIRLS CLUB OF PEKIN": 0.0,
    "CALUMET MEMORIAL P.D. WOLVERINES": 0.0,
    "CENTRAL WRESTLING CLUB": 0.0,
    "CENTRALIA YOUTH WRESTLING": 0.0,
    "CHATHAM WC": 0.0,
    "CHICAGO BULLDOG WC": 0.0,
    "CHICAGO KNIGHTS": 0.0,
    "CHICAGO WOLVES DEN": 0.0,
    "CLINTON WC": 0.0,
    "CLIPPER WC": 0.0,
    "COAL CITY KIDS WC": 0.0,
    "CRIMSON HEAT WC": 0.0,
    "CROSSFACE WRESTLING": 0.0,
    "DEKALB WC": 0.0,
    "DUNGEON WC": 0.0,
    "DWIGHT WC": 0.0,
    "EL PASO WC": 0.0,
    "ELGIN MIGHTY MAROONS": 0.0,
    "ELMHURST JR. DUKES": 0.0,
    "ERIE MIDDLE SCHOOL WC": 0.0,
    "ERVIN WC": 0.0,
    "FAIRMONT ROUGH RIDERS": 0.0,
    "HARVARD WC": 0.0,
    "HILLTOPPERS WC": 0.0,
    "HURRICANES": 0.0,
    "ILLINI BLUFFS WC": 0.0,
    "ILLINI WC": 0.0,
    "JACKSONVILLE WC": 0.0,
    "JUNIOR BULLDOGS": 0.0,
    "JUNK YARD DOGS": 0.0,
    "KISHWAUKEE WC": 0.0,
    "LANCER WC": 0.0,
    "LEROY WRESTLING KIDS CLUB": 0.0,
    "LINCOLN WC": 0.0,
    "LIONHEART INTENSE WRESTLING": 0.0,
    "LIONS WC": 0.0,
    "LITCHFIELD KIDS WRESTLING": 0.0,
    "LITTLE BOILER WC": 0.0,
    "LITTLE FALCONS WC": 0.0,
    "LITTLE HUSKIE WC": 0.0,
    "LITTLE INDIANS": 0.0,
    "LITTLE REDSKINS WC": 0.0,
    "LOCKPORT GATORS WC": 0.0,
    "M-S KIDS CLUB": 0.0,
    "MACOMB LITTLE BOMBERS": 0.0,
    "MAINE EAGLES WC": 0.0,
    "MANTENO JR. PANTHERS": 0.0,
    "MONTICELLO KIDS WC": 0.0,
    "NORTHSHORE GATORS": 0.0,
    "O'FALLON LITTLE PANTHERS": 0.0,
    "OAK FOREST WARRIORS": 0.0,
    "OLY WC": 0.0,
    "OSWEGO PANTHERS": 0.0,
    "OVERTIME SCHOOL OF WRESTLING": 0.0,
    "PANTHER POWERHOUSE WC": 0.0,
    "PEORIA HEIGHTS MINUTEMEN": 0.0,
    "PEORIA RAZORBACKS YOUTH WC": 0.0,
    "PONTIAC PYTHONS": 0.0,
    "QUINCY WC": 0.0,
    "REED CUSTER KNIGHTS": 0.0,
    "RENEGADES": 0.0,
    "RIVERDALE JR. RAMS WC": 0.0,
    "ROCHELLE WC": 0.0,
    "ROMEOVILLE WC": 0.0,
    "SAUKEE YOUTH WC": 0.0,
    "SHARKS WC": 0.0,
    "SILVER & BLACK ATTACK": 0.0,
    "SOMONAUK WC": 0.0,
    "SOUTHERN ILLINOIS UNITED THUNDER CATS": 0.0,
    "SPIDER WC": 0.0,
    "ST. BEDE'S": 0.0,
    "ST. TARCISSUS": 0.0,
    "STATELINE WILDCATS": 0.0,
    "STERLING NEWMAN JR COMETS": 0.0,
    "TAKEDOWN WC": 0.0,
    "TEAM WEST WOLVES": 0.0,
    "THE ZOO WC": 0.0,
    "TOMCAT WC": 0.0,
    "TRI-CITY BRAVES": 0.0,
    "UNITY WC": 0.0,
    "WARREN COUNTY WC": 0.0,
    "WASHINGTON JR PANTHERS": 0.0,
    "WEST FRANKFORT JR. WC": 0.0,
    "WILMINGTON WC": 0.0,
    "YOUNG CHAMPIONS": 0.0,
    ########################################
    "DU-PEC CARNIVORES": -1.0,
    "HOFFMAN ESTATES WC": -1.0,
    "MORTON YOUTH WRESTLING": -1.0,
    "NOTRE DAME WRESTLING": -1.0,
    "RAMS WC": -1.0,
    ########################################
    "MARENGO WC": -2.0,
    "ST. CHARLES EAST WC": -2.0,
}
BRACKET_ID_MAPPING: dict[tuple[bracket_utils.Division, int], int] = {
    ("novice", 62): 139,
    ("novice", 66): 140,
    ("novice", 70): 141,
    ("novice", 74): 142,
    ("novice", 79): 143,
    ("novice", 84): 144,
    ("novice", 89): 145,
    ("novice", 95): 146,
    ("novice", 101): 147,
    ("novice", 108): 148,
    ("novice", 115): 149,
    ("novice", 122): 150,
    ("novice", 130): 151,
    ("novice", 147): 152,
    ("novice", 166): 153,
    ("novice", 215): 154,
    ("senior", 70): 155,
    ("senior", 74): 156,
    ("senior", 79): 157,
    ("senior", 84): 158,
    ("senior", 89): 159,
    ("senior", 95): 160,
    ("senior", 101): 161,
    ("senior", 108): 162,
    ("senior", 115): 163,
    ("senior", 122): 164,
    ("senior", 130): 165,
    ("senior", 138): 166,
    ("senior", 147): 167,
    ("senior", 156): 168,
    ("senior", 166): 169,
    ("senior", 177): 170,
    ("senior", 189): 171,
    ("senior", 215): 172,
    ("senior", 275): 173,
}


def main():
    with open(HERE / "extracted.2004.json") as file_obj:
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

    bracket_utils.validate_acronym_mappings_divisons(
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

    start_id = 3451
    mapped_competitors = bracket_utils.get_competitors_for_sql(
        start_id,
        weight_classes,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
    )

    start_id = 6457
    bracket_utils.get_matches_for_sql(
        start_id,
        weight_classes,
        mapped_competitors.team_competitor_by_info,
        BRACKET_ID_MAPPING,
    )


if __name__ == "__main__":
    main()
