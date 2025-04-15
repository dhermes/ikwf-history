# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bracket_utils
import bs4

HERE = pathlib.Path(__file__).resolve().parent
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("ANTHONY RICH JR", "LPC"): bracket_utils.Competitor(
        full_name="ANTHONY RICH JR",
        first_name="ANTHONY",
        last_name="RICH",
        team_full="L-P CRUNCHING CAVS",
        team_acronym="LPC",
    ),
    ("BJ FUTRELL II", "HAE"): bracket_utils.Competitor(
        full_name="BJ FUTRELL II",
        first_name="BJ",
        last_name="FUTRELL",
        team_full="HARVEY TWISTERS",
        team_acronym="HAE",
    ),
    ("CARL FORESIDE, JR.", "GLA"): bracket_utils.Competitor(
        full_name="CARL FORESIDE, JR.",
        first_name="CARL",
        last_name="FORESIDE",
        team_full="GLADIATORS",
        team_acronym="GLA",
    ),
    ("CASEY MC MURRAY", "LIO"): bracket_utils.Competitor(
        full_name="CASEY MC MURRAY",
        first_name="CASEY",
        last_name="MC MURRAY",
        team_full="LIONS WC",
        team_acronym="LIO",
    ),
    ("DWIGHT MC CALL", "ROK"): bracket_utils.Competitor(
        full_name="DWIGHT MC CALL",
        first_name="DWIGHT",
        last_name="MC CALL",
        team_full="ROCK ISLAND WC",
        team_acronym="ROK",
    ),
    ("GINO DE FRANCISCO", "HOF"): bracket_utils.Competitor(
        full_name="GINO DE FRANCISCO",
        first_name="GINO",
        last_name="DE FRANCISCO",
        team_full="HOFFMAN ESTATES WC",
        team_acronym="HOF",
    ),
    ("JAMES VAN SOMEREN", "WHF"): bracket_utils.Competitor(
        full_name="JAMES VAN SOMEREN",
        first_name="JAMES",
        last_name="VAN SOMEREN",
        team_full="WHEATON FRANKLIN WC",
        team_acronym="WHF",
    ),
    ("JOSHUA VAN BEHREN", "UNI"): bracket_utils.Competitor(
        full_name="JOSHUA VAN BEHREN",
        first_name="JOSHUA",
        last_name="VAN BEHREN",
        team_full="UNITY WC",
        team_acronym="UNI",
    ),
    ("MARCUS MC CALL", "ROK"): bracket_utils.Competitor(
        full_name="MARCUS MC CALL",
        first_name="MARCUS",
        last_name="MC CALL",
        team_full="ROCK ISLAND JR. ROCKS",
        team_acronym="ROK",
    ),
    ("MICHAEL MATOZZI, JR.", "OSW"): bracket_utils.Competitor(
        full_name="MICHAEL MATOZZI, JR.",
        first_name="MICHAEL",
        last_name="MATOZZI",
        team_full="OSWEGO PANTHERS",
        team_acronym="OSW",
    ),
    ("REGINALD WILSON JR", "FOR"): bracket_utils.Competitor(
        full_name="REGINALD WILSON JR",
        first_name="REGINALD",
        last_name="WILSON",
        team_full="FORD HEIGHTS FALCONS",
        team_acronym="FOR",
    ),
    ("ROBERT PROVAX III", "NOT"): bracket_utils.Competitor(
        full_name="ROBERT PROVAX III",
        first_name="ROBERT",
        last_name="PROVAX",
        team_full="NOTRE DAME WC",
        team_acronym="NOT",
    ),
    ("RONALD REEVES JR", "TRI"): bracket_utils.Competitor(
        full_name="RONALD REEVES JR",
        first_name="RONALD",
        last_name="REEVES",
        team_full="TRIAD KNIGHTS",
        team_acronym="TRI",
    ),
    ("T. J. WARNER", "HOO"): bracket_utils.Competitor(
        full_name="T. J. WARNER",
        first_name="T. J.",
        last_name="WARNER",
        team_full="HOOPESTON AREA WC",
        team_acronym="HOO",
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
    "ROX": "ROXANA KIDS WRESTING CLUB",
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
        name=name,
        team_full=_get_team_full(team, division),
        team_acronym=team,
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
    with open(HERE / "2003" / division / filename) as file_obj:
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

    novice_reverse_acronym = bracket_utils.reverse_acronym_map(
        TEAM_ACRONYM_MAPPING, NOVICE_TEAM_ACRONYM_MAPPING
    )
    senior_reverse_acronym = bracket_utils.reverse_acronym_map(
        TEAM_ACRONYM_MAPPING, SENIOR_TEAM_ACRONYM_MAPPING
    )
    year_str = "2003"
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {
        "novice": bracket_utils.parse_team_scores(
            HERE / year_str, "novice", novice_reverse_acronym, TEAM_SCORE_EXCEPTIONS
        ),
        "senior": bracket_utils.parse_team_scores(
            HERE / year_str, "senior", senior_reverse_acronym, TEAM_SCORE_EXCEPTIONS
        ),
    }

    # Add a **CUSTOM** "missing" negative team score based on the rule that
    # "all team point deductions applied across all divisions"
    team_scores["novice"].append(
        bracket_utils.TeamScore(team="LIMESTONE YOUTH WC", acronym="LIM", score=-1.0)
    )

    deductions = bracket_utils.infer_deductions(team_scores)
    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=parsed, team_scores=team_scores, deductions=deductions
    )
    with open(HERE / "extracted.2003.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
