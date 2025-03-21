# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "AOK": "A-O KIDS WC",
    "BAD": "BADGER WC",
    "BAR": "TODO",
    "BAT": "BATAVIA PINNERS",
    "BB": "BELVIDERE BANDITS",
    "BBW": "BRADLEY BOURBONNAIS WRESTLING CLUB",
    "BGP": "BOYS & GIRLS CLUB",  # ... of Pekin
    "BH": "BISMARCK-HENNING WC",
    "BJH": "BETHALTO JR HIGH",
    "BJW": "BENTON JR. WC",
    "BLD": "BELLEVILLE LITTLE DE",
    "BRO": "BRONCO WRESTLING",
    "CCK": "CHAMPAIGN CHARGER KI",
    "CDW": "CHILLI DAWGS WC",
    "CEN": "CENTRALIA WC",
    "CHE": "CHENOA MAT CATS",
    "CJT": "CARY JR TROJAN MATME",
    "CLW": "CRYSTAL LAKE WIZARDS",
    "CW": "CROSSFACE WRESTLING",
    "CYW": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DEC": "DECATUR WC",
    "DGC": "DOWNERS GROVE COUGARS WC",
    "DH": "DUNDEE HIGHLANDERS",
    "DPC": "DURAND-PECATONICA",
    "EBK": "TODO",
    "EMP": "EAST MOLINE PANTHER",
    "EMS": "ERIE MIDDLE SCHOOL W",
    "EP": "EDISON PANTHERS",
    "EWC": "EDWARDSVILLE WC",
    "FAW": "TODO",  # Shelbyville?
    "FBG": "TODO",  # Freeport?
    "FPR": "FRANKLIN PARK RAIDER",
    "FVW": "FOX VALLEY WC",
    "FWC": "FISHER WC",
    "FYW": "FALCON YOUTH WC",
    "GDW": "GRAPPLIN DEVILS WC",
    "GED": "GLEN ELLYN DUNGEON W",
    "GEJ": "GLENBARD EAST JR RAM",
    "GEN": "GENERALS",
    "GJS": "GALESBURG JR STREAKS",  # Duplicate
    "GWC": "GENESEO WC",
    "HAW": "HOOPESTON AREA WC",
    "HBJ": "HIGHLAND BULLDOG JR",
    "HC": "HARLEM COUGARS",
    "HIL": "TODO",  # all athletes went to Waubonsie Valley High School
    "HJT": "HILLSBORO JR TOPPERS",
    "HON": "HONONEGAH KIDS WC",
    "HPL": "HIGHLAND PARK LITTLE GIANTS",
    "HRD": "HINSDALE RED DEVILS",
    "HUS": "HUSKIES WC",
    "IB": "ILLINI BLUFFS WC",
    "JAC": "JACKSONVILLE WC",
    "JGE": "JR GOLDEN EAGLES",
    "JRB": "TODO",  # Lake Zurich
    "JRM": "JR MAROON WC",
    "JRW": "JR ROCKET WRESTLING",
    "JS2": "GALESBURG JR STREAKS",  # Duplicate; GALESBURG JR STREAKS 2
    "LB": "LEMONT BEARS WC",
    "LC": "LITTLE CELTIC WC",
    "LCW": "LAWRENCE COUNTY WC",
    "LKW": "LITCHFIELD WRESTLING CLUB",
    "LLP": "LAKELAND PREDATORS",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WC",
    "LSW": "LIL STORM YOUTH",
    "LVL": "LAKE VILLA LANCERS",
    "LYW": "LIMESTONE YOUTH ROCK",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "MCY": "MIDWEST CENTRAL YOUT",
    "ME": "MAINE EAGLES WC",
    "MET": "METAMORA KIDS WC",
    "MFV": "MARTINEZ FOX VALLEY",
    "MK": "MONTICELLO YOUTH WRESTLING CLUB",
    "MKW": "MACOMB KIDS WRESTLIN",
    "MMM": "TODO",  # OSWEGO (-> 2001:MFV, -> 2002: MAF)
    "MON": "TODO",  # OSWEGO
    "MOR": "MORTON YOUTH WRESTLI",
    "MS": "METRO STALLIONS",
    "MTV": "MT VERNON LIONS",
    "MTZ": "MT ZION WC",
    "MUR": "MURPHYSBORO WRESTLIN",
    "NAP": "NAPERVILLE WC",
    "NE": "NAPERVILLE EAGLES",
    "OAK": "OAKWOOD WC",
    "OC": "OSWEGO COUGARS",
    "OLW": "OAK LAWN PD WILDCATS",
    "OPP": "ORLAND PARK PIONEERS",
    "OSP": "OSWEGO PANTHERS",
    "PCW": "PANTHER CUB WC",
    "PIN": "PINCKNEYVILLE JR",
    "POL": "POLO WC",
    "PPW": "PONTIAC PYTHONS",
    "PR": "TODO",
    "PWC": "PLAINFIELD WC",
    "RAM": "RAMS WC",
    "RCK": "REED CUSTER KNIGHTS",
    "RFW": "ROCK FALLS JUNIOR ROCKET WRESTLING",
    "RIV": "RIVERBEND WC",
    "RJH": "RIVERDALE JR HIGH",
    "ROC": "ROCHELLE WC",
    "ROX": "ROXANA KIDS WC",
    "RWC": "ROCKFORD WC",
    "SAN": "TODO",  # SANDWICH / Ottawa High School??
    "SC": "SPRINGFIELD CAPITALS",
    "SHA": "SHARKS WC",
    "SHE": "SHERRARD JR WC",
    "SIE": "SOUTHERN IL EAGLES",
    "SII": "TODO",  # ST. CHARLES EAST
    "SJO": "SJO YOUTH WRESTLING",
    "SJW": "SHELBYVILLE JR RAMS",
    "SN": "STERLING NEWMAN JR",
    "SSW": "SOUTHSIDE WC",
    "STB": "ST BEDE WC",
    "STC": "TODO",  # ST. CHARLES EAST
    "SVW": "STILLMAN VALLEY WC",
    "SW": "STATELINE WILDCATS",
    "SYW": "SAUKEE YOUTH WC",
    "T1": "TODO",  # Belvidere?
    "TAY": "TAYLORVILLE WC",
    "TAZ": "TODO",  # PEKIN / Illini Bluffs (Glasford)
    "TCB": "TRI-CITY BRAVES",
    "TPB": "TINLEY PARK BULLDOGS",
    "TRI": "TRIAD KNIGHTS WRESTLING CLUB",
    "TTT": "TIGERTOWN TANGLERS",
    "TWC": "TIGER WC",
    "UNI": "UNITY WRESTLING CLUB",
    "VAN": "VANDALIA JR WRESTLIN",
    "VC": "VITTUM CATS",
    "VLC": "VILLA LOMBARD COUGAR",
    "VPY": "VILLA PARK YOUNG",
    "WB": "WHEATON BULLDOGS",
    "WES": "WESTVILLE YOUTH WC",
    "WF": "WEST FRANKFORT JR WC",
    "WFL": "WRESTLING FACTORY",
    "WJP": "WASHINGTON JR PANTHE",
    "WME": "WHEATON MONROE EAGLE",
    "WWC": "WOLFPAK WC",
    "YWC": "YORKVILLE WC",
}
TEAM_NAME_MAPPING = {
    "A-O KIDS WC": 8,
    "BADGER WC": 14,
    "BATAVIA PINNERS": 10005,
    "BELLEVILLE LITTLE DE": 23,
    "BELVIDERE BANDITS": 24,
    "BENTON JR. WC": 26,
    "BETHALTO JR HIGH": 10118,
    "BISMARCK-HENNING WC": 28,
    "BOYS & GIRLS CLUB": 319,
    "BRADLEY BOURBONNAIS WRESTLING CLUB": 37,
    "BRONCO WRESTLING": 41,
    "CARY JR TROJAN MATME": 59,
    "CENTRALIA WC": 64,
    "CHAMPAIGN CHARGER KI": 10124,
    "CHENOA MAT CATS": 10011,
    "CHILLI DAWGS WC": 10014,
    "CROSSFACE WRESTLING": 10018,
    "CRYSTAL LAKE WIZARDS": 89,
    "CUMBERLAND YOUTH WC": 90,
    "DAKOTA WC": 92,
    "DECATUR WC": -20401,
    "DOWNERS GROVE COUGARS WC": 100,
    "DUNDEE HIGHLANDERS": 102,
    "DURAND-PECATONICA": -20401,
    "EAST MOLINE PANTHER": 10121,
    "EDISON PANTHERS": 10131,
    "EDWARDSVILLE WC": 110,
    "ERIE MIDDLE SCHOOL W": 10025,
    "FALCON YOUTH WC": 123,
    "FISHER WC": 130,
    "FOX VALLEY WC": 134,
    "FRANKLIN PARK RAIDER": -20401,
    "GALESBURG JR STREAKS": 10030,
    "GENERALS": -20401,
    "GENESEO WC": 10033,
    "GLEN ELLYN DUNGEON W": 10039,
    "GLENBARD EAST JR RAM": 147,
    "GRAPPLIN DEVILS WC": 153,
    "HARLEM COUGARS": 10041,
    "HIGHLAND BULLDOG JR": 168,
    "HIGHLAND PARK LITTLE GIANTS": 10043,
    "HILLSBORO JR TOPPERS": 170,
    "HINSDALE RED DEVILS": 171,
    "HONONEGAH KIDS WC": 173,
    "HOOPESTON AREA WC": 174,
    "HUSKIES WC": -20401,
    "ILLINI BLUFFS WC": 181,
    "JACKSONVILLE WC": 189,
    "JR GOLDEN EAGLES": 10050,
    "JR MAROON WC": 538,
    "JR ROCKET WRESTLING": 10052,
    "L-P CRUNCHING CAVS": 241,
    "LAKE VILLA LANCERS": -20401,
    "LAKELAND PREDATORS": 10057,
    "LAWRENCE COUNTY WC": 217,
    "LEMONT BEARS WC": 219,
    "LIL STORM YOUTH": 10060,
    "LIMESTONE YOUTH ROCK": 10061,
    "LITCHFIELD WRESTLING CLUB": 231,
    "LITTLE CELTIC WC": 233,
    "LITTLE REDBIRD WC": 10065,
    "MACOMB KIDS WRESTLIN": 243,
    "MAINE EAGLES WC": 245,
    "MARENGO WC": 248,
    "MARTINEZ FOX VALLEY": 250,
    "MATTOON YOUTH WC": 252,
    "METAMORA KIDS WC": 262,
    "METRO STALLIONS": -20401,
    "MIDWEST CENTRAL YOUT": 263,
    "MONTICELLO YOUTH WRESTLING CLUB": 269,
    "MORTON YOUTH WRESTLI": 272,
    "MT VERNON LIONS": 275,
    "MT ZION WC": 276,
    "MURPHYSBORO WRESTLIN": 278,
    "NAPERVILLE EAGLES": -20401,
    "NAPERVILLE WC": 281,
    "OAK LAWN PD WILDCATS": 10075,
    "OAKWOOD WC": 299,
    "ORLAND PARK PIONEERS": 306,
    "OSWEGO COUGARS": -20401,
    "OSWEGO PANTHERS": 10076,
    "PANTHER CUB WC": 10079,
    "PINCKNEYVILLE JR": 10122,
    "PLAINFIELD WC": 326,
    "POLO WC": 327,
    "PONTIAC PYTHONS": 10082,
    "RAMS WC": -20401,
    "REED CUSTER KNIGHTS": 10085,
    "RIVERBEND WC": 354,
    "RIVERDALE JR HIGH": 536,
    "ROCHELLE WC": 358,
    "ROCK FALLS JUNIOR ROCKET WRESTLING": 360,
    "ROCKFORD WC": 364,
    "ROXANA KIDS WC": 371,
    "SAUKEE YOUTH WC": 376,
    "SHARKS WC": 381,
    "SHELBYVILLE JR RAMS": 382,
    "SHERRARD JR WC": 383,
    "SJO YOUTH WRESTLING": 402,
    "SOUTHERN IL EAGLES": 10092,
    "SOUTHSIDE WC": -20401,
    "SPRINGFIELD CAPITALS": 397,
    "ST BEDE WC": 10095,
    "STATELINE WILDCATS": 10097,
    "STERLING NEWMAN JR": 10098,
    "STILLMAN VALLEY WC": 407,
    "TAYLORVILLE WC": 420,
    "TIGER WC": 10103,
    "TIGERTOWN TANGLERS": 441,
    "TINLEY PARK BULLDOGS": 443,
    "TRI-CITY BRAVES": 10104,
    "TRIAD KNIGHTS WRESTLING CLUB": 452,
    "UNITY WRESTLING CLUB": 457,
    "VANDALIA JR WRESTLIN": 461,
    "VILLA LOMBARD COUGAR": 10109,
    "VILLA PARK YOUNG": 464,
    "VITTUM CATS": 466,
    "WASHINGTON JR PANTHE": 10110,
    "WEST FRANKFORT JR WC": 478,
    "WESTVILLE YOUTH WC": 482,
    "WHEATON BULLDOGS": 10120,
    "WHEATON MONROE EAGLE": 10114,
    "WOLFPAK WC": 490,
    "WRESTLING FACTORY": 10115,
    "YORKVILLE WC": 497,
}


class Competitor(pydantic.BaseModel):
    first_name: str
    last_name: str
    suffix: str | None
    team: str


ResultType = Literal[
    "BYE",
    "DECISION",
    "DEFAULT",
    "DISQUALIFICATION",
    "FALL",
    "FORFEIT",
    "MAJOR",
    "TECH",
]


class Match(pydantic.BaseModel):
    match: str
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    result_type: ResultType
    bout_number: int | None
    top_win: bool | None


class WeightClass(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    matches: list[Match]


class WeightClasses(pydantic.RootModel[list[WeightClass]]):
    pass


class CompetitorWithWeight(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    competitor: Competitor


def main():
    with open(HERE / "extracted.2000.json") as file_obj:
        extracted = WeightClasses.model_validate_json(file_obj.read())

    actual_teams: set[str] = set()
    weight_classes = extracted.root
    for weight_class in weight_classes:
        for match in weight_class.matches:
            if match.top_competitor is not None:
                actual_teams.add(match.top_competitor.team)
            if match.bottom_competitor is not None:
                actual_teams.add(match.bottom_competitor.team)

    missing_teams = sorted(
        team for team in actual_teams if team not in TEAM_ACRONYM_MAPPING
    )
    extra_teams = sorted(
        team for team in TEAM_ACRONYM_MAPPING if team not in actual_teams
    )
    print(missing_teams)
    print("****************************************")
    print(extra_teams)


if __name__ == "__main__":
    main()
