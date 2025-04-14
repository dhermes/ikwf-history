# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import functools
import pathlib

import bs4

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
EMPTY_SLOT = "                               "
NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("AARON BREWTON II", "WAUK"): bracket_utils.Competitor(
        full_name="AARON BREWTON II",
        first_name="AARON",
        last_name="BREWTON",
        team_full="WAUKEGAN YOUTH WC",
        team_acronym="WAUK",
    ),
    ("ALVIN FOSTER III", "HPDT"): bracket_utils.Competitor(
        full_name="ALVIN FOSTER III",
        first_name="ALVIN",
        last_name="FOSTER",
        team_full="HARVEY PARK DIST TWISTERS",
        team_acronym="HPDT",
    ),
    ("ANTHONY FERRARIS JR", "MNE"): bracket_utils.Competitor(
        full_name="ANTHONY FERRARIS JR",
        first_name="ANTHONY",
        last_name="FERRARIS",
        team_full="MAINE EAGLES WC",
        team_acronym="MNE",
    ),
    ("ANTWYONE BROWN JR.", "CRST"): bracket_utils.Competitor(
        full_name="ANTWYONE BROWN JR.",
        first_name="ANTWYONE",
        last_name="BROWN",
        team_full="CROSSTOWN CRUSHERS",
        team_acronym="CRST",
    ),
    ("BRENDAN TYLER HALL", "HPDT"): bracket_utils.Competitor(
        full_name="BRENDAN TYLER HALL",
        first_name="BRENDAN TYLER",
        last_name="HALL",
        team_full="HARVEY PARK DIST TWISTERS",
        team_acronym="HPDT",
    ),
    ("CURTIS CRIMS JR.", "CRST"): bracket_utils.Competitor(
        full_name="CURTIS CRIMS JR.",
        first_name="CURTIS",
        last_name="CRIMS",
        team_full="CROSSTOWN CRUSHERS",
        team_acronym="CRST",
    ),
    ("GEORGE CANALES IV", "DIX"): bracket_utils.Competitor(
        full_name="GEORGE CANALES IV",
        first_name="GEORGE",
        last_name="CANALES",
        team_full="DIXON WC",
        team_acronym="DIX",
    ),
    ("JIM JERNIGAN JR.", "MOL"): bracket_utils.Competitor(
        full_name="JIM JERNIGAN JR.",
        first_name="JIM",
        last_name="JERNIGAN",
        team_full="MOLINE WC",
        team_acronym="MOL",
    ),
    ("JOSE MANUEL DEAVILA", "COL"): bracket_utils.Competitor(
        full_name="JOSE MANUEL DEAVILA",
        first_name="JOSE MANUEL",
        last_name="DEAVILA",
        team_full="COLLINSVILLE RAIDERS",
        team_acronym="COL",
    ),
    ("LUSIANO JR. CANTU", "GOM"): bracket_utils.Competitor(
        full_name="LUSIANO JR. CANTU",
        first_name="LUSIANO",
        last_name="CANTU",
        team_full="GOMEZ WRESTLING ACADEMY",
        team_acronym="GOM",
    ),
    ("MATTHEW SCHEFKE JR.", "NAP"): bracket_utils.Competitor(
        full_name="MATTHEW SCHEFKE JR.",
        first_name="MATTHEW",
        last_name="SCHEFKE",
        team_full="NAPERVILLE WC",
        team_acronym="NAP",
    ),
    ("ROSS FERRARO III", "GOM"): bracket_utils.Competitor(
        full_name="ROSS FERRARO III",
        first_name="ROSS",
        last_name="FERRARO",
        team_full="GOMEZ WRESTLING ACADEMY",
        team_acronym="GOM",
    ),
    ("TRAVIS BUCHANAN / WILL", "HPDT"): bracket_utils.Competitor(
        full_name="TRAVIS BUCHANAN / WILL",
        first_name="TRAVIS / WILL",
        last_name="BUCHANAN",
        team_full="HARVEY PARK DIST TWISTERS",
        team_acronym="HPDT",
    ),
    ("TYRONE  SALLY JR.", "HPDT"): bracket_utils.Competitor(
        full_name="TYRONE  SALLY JR.",
        first_name="TYRONE",
        last_name="SALLY",
        team_full="HARVEY PARK DIST TWISTERS",
        team_acronym="HPDT",
    ),
    ("WARDELL ROSEMAN JR.", "DUN"): bracket_utils.Competitor(
        full_name="WARDELL ROSEMAN JR.",
        first_name="WARDELL",
        last_name="ROSEMAN",
        team_full="DUNDEE HIGHLANDERS",
        team_acronym="DUN",
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
    with open(HERE / "2006" / division / filename) as file_obj:
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
    year_str = "2006"
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
    with open(HERE / "extracted.2006.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
