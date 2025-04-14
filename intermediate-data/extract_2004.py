# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bs4

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("BEN STUCKEY III", "MTV"): bracket_utils.Competitor(
        full_name="BEN STUCKEY III",
        first_name="BEN",
        last_name="STUCKEY",
        team_full="MT. VERNON LIONS",
        team_acronym="MTV",
    ),
    ("BILLY BYRD IV", "SYC"): bracket_utils.Competitor(
        full_name="BILLY BYRD IV",
        first_name="BILLY",
        last_name="BYRD",
        team_full="SYCAMORE WC",
        team_acronym="SYC",
    ),
    ("BJ FUTRELL II", "HAE"): bracket_utils.Competitor(
        full_name="BJ FUTRELL II",
        first_name="BJ",
        last_name="FUTRELL",
        team_full="HARVEY PARK DIST TWISTERS",
        team_acronym="HAE",
    ),
    ("CURTIS CRIMS JR.", "BLZ"): bracket_utils.Competitor(
        full_name="CURTIS CRIMS JR.",
        first_name="CURTIS",
        last_name="CRIMS",
        team_full="BLAZER KIDS",
        team_acronym="BLZ",
    ),
    ("EDDIE LANCE III", "GRA"): bracket_utils.Competitor(
        full_name="EDDIE LANCE III",
        first_name="EDDIE",
        last_name="LANCE",
        team_full="GRANITE CITY JR WARRIORS",
        team_acronym="GRA",
    ),
    ("GEORGE CANALES IV", "STR"): bracket_utils.Competitor(
        full_name="GEORGE CANALES IV",
        first_name="GEORGE",
        last_name="CANALES",
        team_full="STERLING NEWMAN JR COMETS",
        team_acronym="STR",
    ),
    ("NICKBRAMHALL", "EDW"): bracket_utils.Competitor(
        full_name="NICKBRAMHALL",
        first_name="NICK",
        last_name="BRAMHALL",
        team_full="EDWARDSVILLE WC",
        team_acronym="EDW",
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


def parse_competitor(value: str) -> bracket_utils.CompetitorRaw | None:
    cleaned = value.strip().rstrip("+").strip("-")
    if cleaned == "Bye":
        return None

    name, team = cleaned.rsplit(" ", 1)
    team = team.strip()

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return bracket_utils.CompetitorRaw(name=name, team=team)


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
) -> bracket_utils.MatchRaw:
    top_competitor = None
    top_competitor_str = championship_lines[start_index][:31]
    if top_competitor_str != EMPTY_SLOT:
        top_competitor = parse_competitor(top_competitor_str)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:31]
    if bottom_competitor_str != EMPTY_SLOT:
        bottom_competitor = parse_competitor(bottom_competitor_str)

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
    with open(HERE / "2004" / division / filename) as file_obj:
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

    if division == "novice" and weight == 108:
        consolation_fifth_place_bottom_competitor = bracket_utils.CompetitorRaw(
            name="SEPEHR KALHOR", team="ROK"
        )
    else:
        consolation_fifth_place_bottom_competitor = parse_competitor(
            fifth_place_lines[2][:31]
        )

    if division == "novice" and weight == 166:
        consolation_round6_semi_01_top_competitor = bracket_utils.CompetitorRaw(
            name="RYAN GAINES",
            team="MAR",
        )
        consolation_fifth_place_top_competitor = bracket_utils.CompetitorRaw(
            name="RYAN GAINES",
            team="MAR",
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
        ),
        maybe_r32_empty_bye(
            championship_lines, 5, "championship_r32_03", "championship_r16_02", "top"
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
        ),
        maybe_r32_empty_bye(
            championship_lines, 15, "championship_r32_07", "championship_r16_04", "top"
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
        ),
        maybe_r32_empty_bye(
            championship_lines, 25, "championship_r32_11", "championship_r16_06", "top"
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
        ),
        maybe_r32_empty_bye(
            championship_lines, 35, "championship_r32_15", "championship_r16_08", "top"
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

    novice_reverse_acronym = bracket_utils.reverse_acronym_map(
        TEAM_ACRONYM_MAPPING, NOVICE_TEAM_ACRONYM_MAPPING
    )
    senior_reverse_acronym = bracket_utils.reverse_acronym_map(
        TEAM_ACRONYM_MAPPING, SENIOR_TEAM_ACRONYM_MAPPING
    )
    year_str = "2004"
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {
        "novice": bracket_utils.parse_team_scores(
            HERE / year_str, "novice", novice_reverse_acronym, TEAM_SCORE_EXCEPTIONS
        ),
        "senior": bracket_utils.parse_team_scores(
            HERE / year_str, "senior", senior_reverse_acronym, TEAM_SCORE_EXCEPTIONS
        ),
    }

    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=parsed, team_scores=team_scores, deductions=[]
    )
    with open(HERE / "extracted.2004.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
