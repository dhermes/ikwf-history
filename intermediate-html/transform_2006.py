# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 37
TEAM_SCORE_ID_START = 1633
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
TEAM_NAME_MAPPING: dict[str, int] = {
    "ACES WC": 3,
    "ALEDO BEAR COUNTRY WC": 10002,
    "ALLEMAN JR PIONEERS": 10003,
    "ANIMALS WC": 10004,
    "ARGENTA/OREANA KIDS CLUB": 8,
    "ARLINGTON CARDINALS": 9,
    "BADGER WC": 14,
    "BATAVIA PINNERS": 10005,
    "BATAVIA": 10005,
    "BELLEVILLE LITTLE DEVILS": 23,
    "BELVIDERE BANDITS": 24,
    "BENTON JR WC": 26,
    "BETHALTO BULLS WC": 10006,
    "BISMARCK HENNING WRESTLING CLUB": 28,
    "BISON WC": 126,
    "BLACKHAWK WC": 30,
    "BLOOMINGTON RAIDER WC": 32,
    "BRAWLERS WC": 39,
    "CALUMET MEMORIAL PD WOLVERINES": 49,
    "CARBONDALE WC": 53,
    "CARY JR TROJAN MATMEN": 59,
    "CENTRAL WRESTLING CLUB": 10010,
    "CHAMPAIGN KIDS WRESTLING": 65,
    "CHARLESTON WC": 69,
    "CHICAGO CRUSADERS": 71,
    "CHICAGO WOLVES DEN": 75,
    "CHILLI DAWGS WC": 10014,
    "CLIPPER WC": 80,
    "COLLINSVILLE RAIDERS": 338,
    "CROSSTOWN CRUSHERS": 10019,
    "CRYSTAL LAKE WIZARDS": 89,
    "CUMBERLAND YOUTH WC": 90,
    "DAKOTA WC": 92,
    "DEKALB WC": 96,
    "DIXON WC": 98,
    "DOWNERS GROVE COUGARS": 100,
    "DUNDEE HIGHLANDERS": 102,
    "EDWARDSVILLE WC": 110,
    "EFFINGHAM JUNIOR WRESTLING TEAM": 10021,
    "EL PASO/GRIDLEY WC": 112,
    "ELMHURST JR. DUKES": 10024,
    "ERIE MIDDLE SCHOOL WC": 10025,
    "FAIRMONT ROUGH RIDERS": 10027,
    "FALCON WRESTLING CLUB": 124,
    "FALCON YOUTH WC": 123,
    "FENWICK FALCONS WC": 10028,
    "FIGHTIN TITAN WC": 128,
    "FISHER WC": 130,
    "FOX VALLEY WC": 134,
    "GC JR WARRIORS": 10040,
    "GENESEO SPIDER WC": 10032,
    "GLADIATORS": 10038,
    "GLEN ELLYN DUNGEON WC": 10039,
    "GLENBARD EAST JR RAMS": 147,
    "GOLDEN EAGLES": 149,
    "GOMEZ WRESTLING ACADEMY": 150,
    "GRAPPLIN' DEVILS WRESTLING CLUB": 153,
    "HARLEM COUGARS": 10041,
    "HARVEY PARK DIST TWISTERS": 162,
    "HECOX TEAM BENAIAH": 165,
    "HERRIN JUNIOR WC": 10042,
    "HIGHLAND BULLDOG JR WC": 168,
    "HIGHLAND PARK LITTLE GIANTS": 169,
    "HILLTOPPERS WC": 10044,
    "HINSDALE RED DEVIL WC": 171,
    "HOFFMAN ESTATES WC": 172,
    "HONONEGAH KIDS WC": 173,
    "HOOPESTON AREA WC": 174,
    "HURRICANES": 10045,
    "IMPACT WC": 654,
    "IRON MAN": 10046,
    "JOLIET JUNIOR STEELMEN": 10048,
    "JR. COUGARS WC": 196,
    "JUNIOR GATORS WC": 10049,
    "JUNIOR VIKINGS": 10055,
    "KNIGHTS WRESTLING": 206,
    "L-P CRUNCHING CAVS": 241,
    "LAKELAND PREDATORS": 10057,
    "LANCER WC": 216,
    "LEMONT BEARS WC": 219,
    "LIMESTONE YOUTH WC": 10061,
    "LINCOLN-WAY WC": 227,
    "LIONHEART INTENSE WRESTLING": 228,
    "LIONS WC": 229,
    "LITCHFIELD KIDS WRESTLING": 231,
    "LITTLE CELTIC WC": 233,
    "LITTLE FALCONS WC": 10062,
    "LITTLE HUSKIE WC": 235,
    "LITTLE REDBIRD WC": 10065,
    "LITTLE REDSKINS WC": 10066,
    "LOCKPORT JR PORTERS WC": 202,
    "M-S KIDS CLUB": 10069,
    "MACOMB LITTLE BOMBERS": 243,
    "MAD DOG WRESTLING ACADEMY": 244,
    "MAINE EAGLES WC": 245,
    "MARENGO INDIANS YOUTH WRESTLING": 248,
    "MARTINEZ FOX VALLEY ELITE": 250,
    "MATTOON YOUTH WC": 252,
    "MCLEAN COUNTY WC": 10070,
    "MENDOTA WC": 261,
    "METAMORA KIDS WC": 262,
    "MIDWEST CENTRAL YOUTH": 263,
    "MINOOKA LITTLE INDIANS": 266,
    "MOLINE WC": 268,
    "MORRISON STALLIONS WC": 270,
    "MORTON LITTLE MUSTANGS": 271,
    "MORTON YOUTH WRESTLING": 272,
    "MT. PULASKI WC": 10073,
    "MT. VERNON LIONS": 275,
    "MT. ZION WC": 276,
    "MURPHYSBORO WRESTLING": 278,
    "MUSTANG WC": 279,
    "NAPERVILLE WC": 281,
    "NOTRE DAME WRESTLING": 295,
    "O'FALLON LITTLE PANTHERS": 296,
    "OAK FOREST WARRIORS": 297,
    "OAK LAWN P.D. WILDCATS": 10075,
    "OAKWOOD WC": 299,
    "ORLAND PARK PIONEERS": 306,
    "OSWEGO PANTHERS": 10076,
    "PALATINE PANTHERS": 10078,
    "PANTHER CUB WRESTLING CLUB": 10079,
    "PANTHER POWERHOUSE WC": 313,
    "PANTHER/REDHAWK WC": 10080,
    "PEORIA RAZORBACKS YOUTH WC": 321,
    "PLAINFIELD WC": 326,
    "POLO WC": 327,
    "PONTIAC PYTHONS": 10082,
    "PRAIRIE CENTRAL-CHENOA HAWKS": 10083,
    "PROVISO POWERHOUSE WC": 314,
    "QUINCY WC": 336,
    "REED CUSTER KNIGHTS": 10085,
    "RENEGADES": 10086,
    "RICH RATTLERS WC": 349,
    "RICHMOND WRESTLING CLUB": 350,
    "RIVERBEND WC": 354,
    "RIVERDALE JR. RAMS WC": 536,
    "ROAD WARRIORS": 357,
    "ROCHESTER WC": 10087,
    "ROCK ISLAND WC": 361,
    "ROCKFORD WC": 364,
    "ROCKRIDGE WC": 10088,
    "ROMEOVILLE WC": 368,
    "SAUK VALLEY WRESTLING CLUB": 375,
    "SAUKEE YOUTH WC": 376,
    "SCN YOUTH WC": 377,
    "SENECA IRISH CADETS": 379,
    "SHAMROCK WC": 380,
    "SHARKS WC": 381,
    "SHELBYVILLE JR RAMS WRESTLING": 382,
    "SJO SPARTAN YOUTH WC": 402,
    "SONS OF THUNDER": 10091,
    "SOUTHERN ILLINOIS UNITED THUNDER CATS": 10093,
    "SPIDER WC": 10094,
    "SPRINGFIELD CAPITAL KIDS WRESTLING": 397,
    "ST. CHARLES EAST WC": 10096,
    "STILLMAN VALLEY WC": 407,
    "STOCKTON RENEGADES": 408,
    "SYCAMORE WC": 418,
    "TAYLORVILLE WC": 420,
    "TEAM WEST WOLVES": 10101,
    "TIGER WC": 10103,
    "TIGERTOWN TANGLERS": 441,
    "TINLEY PARK BULLDOGS": 443,
    "TOMCAT WC": 448,
    "TREVIAN WC": 288,
    "TRI-VALLEY WC": 10105,
    "TRIAD LITTLE KNIGHTS": 452,
    "UNITY WC": 457,
    "VANDALIA JR WRESTLING": 461,
    "VERMILION VALLEY ELITE": 10108,
    "VILLA LOMBARD COUGARS": 10109,
    "VILLA PARK YOUNG WARRIORS": 464,
    "VITTUM CATS": 466,
    "WARRENSBURG WC": 468,
    "WASHINGTON JR PANTHERS": 10110,
    "WAUBONSIE WC": 473,
    "WAUKEGAN YOUTH WC": 10111,
    "WEST HANCOCK WC": 479,
    "WESTVILLE YOUTH WC": 482,
    "WHEATON TIGER WC": 483,
    "WOLFPAK WC": 490,
    "WRESTLING FACTORY": 10115,
    "XTREME WRESTLING": 496,
    "YORKVILLE WRESTLING CLUB": 497,
}
NOVICE_EXTRA_TEAM_SCORES: dict[str, float] = {
    "CLIPPER WC": 0.0,
}
SENIOR_EXTRA_TEAM_SCORES: dict[str, float] = {}
BRACKET_ID_MAPPING: dict[tuple[bracket_utils.Division, int], int] = {
    ("novice", 62): 209,
    ("novice", 66): 210,
    ("novice", 70): 211,
    ("novice", 74): 212,
    ("novice", 79): 213,
    ("novice", 84): 214,
    ("novice", 89): 215,
    ("novice", 95): 216,
    ("novice", 101): 217,
    ("novice", 108): 218,
    ("novice", 115): 219,
    ("novice", 122): 220,
    ("novice", 130): 221,
    ("novice", 147): 222,
    ("novice", 166): 223,
    ("novice", 215): 224,
    ("senior", 70): 225,
    ("senior", 74): 226,
    ("senior", 79): 227,
    ("senior", 84): 228,
    ("senior", 89): 229,
    ("senior", 95): 230,
    ("senior", 101): 231,
    ("senior", 108): 232,
    ("senior", 115): 233,
    ("senior", 122): 234,
    ("senior", 130): 235,
    ("senior", 138): 236,
    ("senior", 147): 237,
    ("senior", 156): 238,
    ("senior", 166): 239,
    ("senior", 177): 240,
    ("senior", 189): 241,
    ("senior", 215): 242,
    ("senior", 275): 243,
}


def main():
    with open(HERE / "extracted.2006.json") as file_obj:
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

    start_id = 5074
    mapped_competitors = bracket_utils.get_competitors_for_sql(
        start_id,
        weight_classes,
        TEAM_ACRONYM_MAPPING,
        NOVICE_TEAM_ACRONYM_MAPPING,
        SENIOR_TEAM_ACRONYM_MAPPING,
        TEAM_NAME_MAPPING,
    )

    start_id = 9672
    bracket_utils.get_matches_for_sql(
        start_id,
        weight_classes,
        mapped_competitors.team_competitor_by_info,
        BRACKET_ID_MAPPING,
    )


if __name__ == "__main__":
    main()
