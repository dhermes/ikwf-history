# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ABC": "ALEDO BEAR COUNTRY WC",
    "ANI": "ANIMALS WC",
    "ARG": "ARGENTA/OREANA KIDS CLUB",
    "ARL": "ARLINGTON CARDINALS",
    "BAB": "BARRINGTON BRONCOS",
    "BAD": "BADGER WC",
    "BAH": "BARTLETT JR HAWKS",
    "BAT": "BATAVIA PINNERS",
    "BEL": "BELLEVILLE LITTLE DEVILS",
    "BEN": "BENTON JR WC",
    "BET": "BETHALTO BULLS WC",
    "BEV": "BELVIDERE BANDITS",
    "BIS": "BISON WC",
    "BLA": "BLACKHAWK WC",
    "BLO": "BLOOMINGTON RAIDER WC",
    "BLZ": "BLAZER KIDS",
    "BRA": "BRAWLERS WC",
    "BSH": "BISMARCK HENNING WRESTLING CLUB",
    "CAL": "CARLINVILLE KIDS WC",
    "CAR": "CARBONDALE WC",
    "CAY": "CARY JR TROJAN MATMEN",
    "CEN": "CENTRAL WRESTLING CLUB",
    "CHA": "CHAMPAIGN KIDS WRESTLING",
    "CHE": "CHENOA MAT CATS",
    "CHL": "CHILLI DAWGS WC",
    "CHR": "CHARLESTON WC",
    "CRY": "CRYSTAL LAKE WIZARDS",
    "CUM": "CUMBERLAND YOUTH WC",
    "DAK": "DAKOTA WC",
    "DEK": "DEKALB WC",
    "DIX": "DIXON WC",
    "DOW": "DOWNERS GROVE COUGARS",
    "DUN": "DUNDEE HIGHLANDERS",
    "DUR": "DU-PEC CARNIVORES",
    "EDW": "EDWARDSVILLE WC",
    "EFF": "EFFINGHAM YOUTH WC",
    "ELP": "EL PASO WC",
    "ERI": "ERIE MIDDLE SCHOOL WC",
    "ERV": "ERVIN WC",
    "FAC": "FALCON YOUTH WC",
    "FAL": "FALCON WRESTLING CLUB",
    "FEN": "FENWICK FALCONS WC",
    "FIS": "FISHER WC",
    "FOX": "FOX VALLEY WC",
    "FTN": "FIGHTIN TITAN WC",
    "GAL": "GALESBURG JR STREAKS",
    "GEE": "GENESEO WC",
    "GEV": "GENEVA WC",
    "GLN": "GLENBARD EAST JR RAMS",
    "GRA": "GRANITE CITY JR WARRIORS",
    "GRD": "GRAPPLIN' DEVILS",
    "HAE": "HARVEY PARK DIST TWISTERS",
    "HAR": "HARLEM COUGARS",
    "HER": "HERRIN WC",
    "HIG": "HIGHLAND BULLDOG JR WC",
    "HIL": "HILLSBORO JR TOPPERS",
    "HIN": "HINSDALE RED DEVIL WC",
    "HOF": "HOFFMAN ESTATES WC",
    "HON": "HONONEGAH KIDS WC",
    "HOO": "HOOPESTON AREA WC",
    "JAC": "JACKSONVILLE WC",
    "JOL": "JOLIET BOYS CLUB COBRAS",
    "JRC": "JR. COUGARS WC",
    "JRG": "JR. GOLDEN EAGLES",
    "JRM": "JR. MAROON WC",
    "JRS": "JR. SENTINELS",
    "JRX": "JR. SAXONS WC",
    "KNI": "KNIGHTS WRESTLING",
    "LAE": "LAKELAND PREDATORS",
    "LAW": "LAWRENCE COUNTY WC",
    "LEM": "LEMONT BEARS WC",
    "LHI": "LIONHEART INTENSE WRESTLING",
    "LIM": "LIMESTONE YOUTH ROCKET WC",
    "LIN": "LINCOLN-WAY WC",
    "LIS": "LIL' STORM YOUTH WRESTLING",
    "LLC": "LITTLE CELTIC WC",
    "LLG": "LITTLE GIANTS WC",
    "LLH": "LITTLE HUSKIE WC",
    "LLI": "LITTLE INDIANS",
    "LLV": "LITTLE VIKING WC OF H-F",
    "LOC": "LOCKPORT GATORS WC",
    "LPC": "L-P CRUNCHING CAVS",
    "LRB": "LITTLE REDBIRD WC",
    "LRS": "LITTLE REDSKINS WC",
    "LWN": "PANTHER CUB WRESTLING CLUB",
    "M-S": "M-S KIDS CLUB",
    "MAC": "MACOMB LITTLE BOMBERS",
    "MAF": "MARTINEZ FOX VALLEY ELITE WC",
    "MAI": "MAINE EAGLES WC",
    "MAR": "MARENGO WC",
    "MAT": "MATTOON YOUTH WC",
    "MEN": "MENDOTA MAT MASTERS",
    "MET": "METAMORA KIDS WC",
    "MID": "MIDWEST CENTRAL YOUTH",
    "MLM": "MORTON LITTLE MUSTANGS",
    "MOL": "MOLINE WC",
    "MRS": "MORRISON STALLIONS WC",
    "MRT": "MORTON YOUTH WRESTLING",
    "MTV": "MT. VERNON LIONS",
    "MTZ": "MT. ZION WC",
    "MUR": "MURPHYSBORO WRESTLING",
    "MUS": "MUSTANG WC",
    "NAP": "NAPERVILLE WC",
    "NOT": "NOTRE DAME WRESTLING",
    "OAK": "OAK FOREST WARRIORS",
    "OAL": "OAK LAWN P.D. WILDCATS",
    "OAW": "OAKWOOD WC",
    "OFL": "O'FALLON LITTLE PANTHERS",
    "ORL": "ORLAND PARK PIONEERS",
    "OSW": "OSWEGO PANTHERS",
    "PAN": "PANTHER WC",
    "PJP": "PALATINE JUNIOR PIRATES",
    "PLA": "PLAINFIELD WC",
    "PLP": "PALATINE PANTHERS WC",
    "PLT": "PLAINFIELD TORNADOES WC",
    "POL": "POLO WC",
    "PON": "PONTIAC PYTHONS",
    "PRO": "PROVISO POWERHOUSE WC",
    "PWR": "PANTHER POWERHOUSE WC",
    "RCK": "REED CUSTER KNIGHTS",
    "RCM": "RICHMOND WRESTLING CLUB",
    "RCR": "ROCK RIDGE WC",
    "RDW": "ROAD WARRIORS",
    "RIC": "RICH RATTLERS WC",
    "RIV": "RIVERBEND WC",
    "ROC": "ROCHELLE WC",
    "ROF": "ROCKFORD WC",
    "ROK": "ROCK ISLAND WC",
    "ROX": "ROXANA KIDS WRESTLING CLUB",
    "RVD": "RIVERDALE JR. RAMS WC",
    "SAU": "SAUKEE YOUTH WC",
    "SAV": "SAVANNA REDHAWKS",
    "SBA": "SILVER & BLACK ATTACK",
    "SCE": "ST. CHARLES EAST WC",
    "SCN": "SCN YOUTH WC",
    "SEN": "SENECA IRISH CADETS",
    "SHA": "SHAMROCK WC",
    "SHB": "SHELBYVILLE JR RAMS WRESTLING",
    "SHR": "SHERRARD JR WC",
    "SJO": "SJO SPARTAN YOUTH WC",
    "SPR": "SPRINGFIELD CAPITALS",
    "STI": "STILLMAN VALLEY WC",
    "STR": "STERLING NEWMAN JR COMETS",
    "STT": "ST. TARCISSUS",
    "SYC": "SYCAMORE WC",
    "TAY": "TAYLORVILLE WC",
    "TBI": "T-BIRD RAIDER WRESTLING",
    "TIG": "TIGER WC",
    "TIN": "TINLEY PARK BULLDOGS",
    "TKD": "TAKEDOWN WC",
    "TOM": "TOMCAT WC",
    "TRC": "TRI-CITY BRAVES",
    "TRI": "TRIAD KNIGHTS",
    "TRV": "TREVIAN WC",
    "TTT": "TIGERTOWN TANGLERS",
    "TWC": "TWIN CITY WC",
    "UNI": "UNITY WC",
    "UNT": "UNITED TOWNSHIP WC",
    "VAN": "VANDALIA JR WRESTLING",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAR": "WARRENSBURG WC",
    "WAU": "WAUBONSIE WC",
    "WET": "WESTVILLE YOUTH WC",
    "WHM": "WHEATON MONROE EAGLES",
    "WHT": "WHEATON TIGER WC",
    "WOL": "WOLFPAK WC",
    "WRE": "WRESTLING FACTORY",
    "YNC": "YOUNG CHAMPIONS",
    "YOR": "YORKVILLE WRESTLING CLUB",
    "ZBS": "ZEE-BEE STINGERS",
}
TEAM_NAME_MAPPING = {
    "ACES WC": -40109,
    "ALEDO BEAR COUNTRY WC": -40109,
    "ALLEMAN JR PIONEER WC": -40109,
    "ANIMALS WC": -40109,
    "ARGENTA/OREANA KIDS CLUB": -40109,
    "ARLINGTON CARDINALS": -40109,
    "BADGER WC": -40109,
    "BARRINGTON BRONCOS": -40109,
    "BARTLETT JR HAWKS": -40109,
    "BATAVIA PINNERS": -40109,
    "BELLEVILLE LITTLE DEVILS": -40109,
    "BELVIDERE BANDITS": -40109,
    "BENTON JR WC": -40109,
    "BETHALTO BULLS WC": -40109,
    "BISMARCK HENNING WRESTLING CLUB": -40109,  # Senior
    "BISMARK-HENNING": -40109,  # Novice
    "BISON WC": -40109,
    "BLACK KATS WC": -40109,
    "BLACKHAWK WC": -40109,
    "BLAZER KIDS": -40109,
    "BLOOMINGTON RAIDER WC": -40109,
    "BOYS & GIRLS CLUB OF PEKIN": -40109,
    "BRAWLERS WC": -40109,
    "CALUMET MEMORIAL P.D. WOLVERINES": -40109,
    "CARBONDALE WC": -40109,
    "CARLINVILLE KIDS WC": -40109,
    "CARY JR TROJAN MATMEN": -40109,
    "CENTRAL WRESTLING CLUB": -40109,
    "CENTRALIA YOUTH WRESTLING": -40109,
    "CHAMPAIGN KIDS WRESTLING": -40109,
    "CHARLESTON WC": -40109,
    "CHATHAM WC": -40109,
    "CHENOA MAT CATS": -40109,
    "CHICAGO BULLDOG WC": -40109,
    "CHICAGO KNIGHTS": -40109,
    "CHICAGO WOLVES DEN": -40109,
    "CHILLI DAWGS WC": -40109,
    "CLINTON WC": -40109,
    "CLIPPER WC": -40109,
    "COAL CITY KIDS WC": -40109,
    "CRIMSON HEAT WC": -40109,
    "CROSSFACE WRESTLING": -40109,
    "CRYSTAL LAKE WIZARDS": -40109,
    "CUMBERLAND YOUTH WC": -40109,
    "DAKOTA WC": -40109,
    "DEKALB WC": -40109,
    "DIXON WC": -40109,
    "DOWNERS GROVE COUGARS": -40109,
    "DU-PEC CARNIVORES": -40109,
    "DUNDEE HIGHLANDERS": -40109,
    "DUNGEON WC": -40109,
    "DWIGHT WC": -40109,
    "EDWARDSVILLE WC": -40109,
    "EFFINGHAM YOUTH WC": -40109,
    "EL PASO WC": -40109,
    "ELGIN MIGHTY MAROONS": -40109,
    "ELMHURST JR. DUKES": -40109,
    "ERIE MIDDLE SCHOOL WC": -40109,
    "ERVIN WC": -40109,
    "FAIRMONT ROUGH RIDERS": -40109,
    "FALCON WRESTLING CLUB": -40109,
    "FALCON YOUTH WC": -40109,
    "FENWICK FALCONS WC": -40109,
    "FIGHTIN TITAN WC": -40109,
    "FISHER WC": -40109,
    "FOX VALLEY WC": -40109,
    "GALESBURG JR STREAKS": -40109,
    "GENESEO WC": -40109,
    "GENEVA WC": -40109,
    "GLENBARD EAST JR RAMS": -40109,
    "GRANITE CITY JR WARRIORS": -40109,
    "GRAPPLIN' DEVILS": -40109,
    "HARLEM COUGARS": -40109,
    "HARVARD WC": -40109,
    "HARVEY PARK DIST TWISTERS": -40109,
    "HERRIN WC": -40109,
    "HIGHLAND BULLDOG JR WC": -40109,
    "HILLSBORO JR TOPPERS": 170,
    "HILLTOPPERS WC": -40109,
    "HINSDALE RED DEVIL WC": -40109,
    "HOFFMAN ESTATES WC": -40109,
    "HONONEGAH KIDS WC": -40109,
    "HOOPESTON AREA WC": -40109,
    "HURRICANES": -40109,
    "ILLINI BLUFFS WC": -40109,
    "ILLINI WC": -40109,
    "JACKSONVILLE WC": -40109,
    "JOLIET BOYS CLUB COBRAS": -40109,
    "JR. COUGARS WC": -40109,
    "JR. GOLDEN EAGLES": -40109,
    "JR. MAROON WC": -40109,
    "JR. SAXONS WC": -40109,
    "JR. SENTINELS": -40109,
    "JUNIOR BULLDOGS": -40109,
    "JUNK YARD DOGS": -40109,
    "KISHWAUKEE WC": -40109,
    "KNIGHTS WRESTLING": -40109,
    "L-P CRUNCHING CAVS": -40109,
    "LAKELAND PREDATORS": -40109,
    "LANCER WC": -40109,
    "LAWRENCE COUNTY WC": -40109,
    "LEMONT BEARS WC": -40109,
    "LEROY WRESTLING KIDS CLUB": -40109,
    "LIL' STORM YOUTH WRESTLING": -40109,
    "LIMESTONE YOUTH ROCKET WC": -40109,
    "LINCOLN WC": -40109,
    "LINCOLN-WAY WC": -40109,
    "LIONHEART INTENSE WRESTLING": -40109,
    "LIONS WC": -40109,
    "LITCHFIELD KIDS WRESTLING": -40109,
    "LITTLE BOILER WC": -40109,
    "LITTLE CELTIC WC": -40109,
    "LITTLE FALCONS WC": -40109,
    "LITTLE GIANTS WC": -40109,
    "LITTLE HUSKIE WC": -40109,
    "LITTLE INDIANS": -40109,
    "LITTLE REDBIRD WC": -40109,
    "LITTLE REDSKINS WC": -40109,
    "LITTLE VIKING WC OF H-F": -40109,
    "LOCKPORT GATORS WC": -40109,
    "M-S KIDS CLUB": -40109,
    "MACOMB LITTLE BOMBERS": -40109,
    "MAINE EAGLES WC": -40109,
    "MANTENO JR. PANTHERS": -40109,
    "MARENGO WC": -40109,
    "MARTINEZ FOX VALLEY ELITE WC": -40109,
    "MATTOON YOUTH WC": -40109,
    "MENDOTA MAT MASTERS": -40109,
    "METAMORA KIDS WC": -40109,
    "MIDWEST CENTRAL YOUTH": -40109,
    "MOLINE WC": -40109,
    "MONTICELLO KIDS WC": -40109,
    "MORRISON STALLIONS WC": -40109,
    "MORTON LITTLE MUSTANGS": -40109,
    "MORTON YOUTH WRESTLING": -40109,
    "MT. VERNON LIONS": -40109,
    "MT. ZION WC": -40109,
    "MURPHYSBORO WRESTLING": -40109,
    "MUSTANG WC": -40109,
    "NAPERVILLE WC": -40109,
    "NORTHSHORE GATORS": -40109,
    "NOTRE DAME WRESTLING": -40109,
    "O'FALLON LITTLE PANTHERS": -40109,
    "OAK FOREST WARRIORS": -40109,
    "OAK LAWN P.D. WILDCATS": -40109,
    "OAKWOOD WC": -40109,
    "OLY WC": -40109,
    "ORLAND PARK PIONEERS": -40109,
    "OSWEGO PANTHERS": -40109,
    "OVERTIME SCHOOL OF WRESTLING": -40109,
    "PALATINE JUNIOR PIRATES": -40109,
    "PALATINE PANTHERS WC": -40109,
    "PANTHER CUB WRESTLING CLUB": -40109,
    "PANTHER POWERHOUSE WC": -40109,
    "PANTHER WC": -40109,
    "PEORIA HEIGHTS MINUTEMEN": -40109,
    "PEORIA RAZORBACKS YOUTH WC": -40109,
    "PLAINFIELD TORNADOES WC": -40109,
    "PLAINFIELD WC": -40109,
    "POLO WC": -40109,
    "PONTIAC PYTHONS": -40109,
    "PROVISO POWERHOUSE WC": -40109,
    "QUINCY WC": -40109,
    "RAMS WC": -40109,
    "REED CUSTER KNIGHTS": -40109,
    "RENEGADES": -40109,
    "RICH RATTLERS WC": -40109,
    "RICHMOND WRESTLING CLUB": -40109,
    "RIVERBEND WC": -40109,
    "RIVERDALE JR. RAMS WC": -40109,
    "ROAD WARRIORS": -40109,
    "ROCHELLE WC": -40109,
    "ROCK ISLAND WC": -40109,
    "ROCK RIDGE WC": -40109,
    "ROCKFORD WC": -40109,
    "ROMEOVILLE WC": -40109,
    "ROXANA KIDS WRESTLING CLUB": -40109,
    "SAUKEE YOUTH WC": -40109,
    "SAVANNA REDHAWKS": -40109,
    "SCN YOUTH WC": -40109,
    "SENECA IRISH CADETS": -40109,
    "SHAMROCK WC": -40109,
    "SHARKS WC": -40109,
    "SHELBYVILLE JR RAMS WRESTLING": -40109,
    "SHERRARD JR WC": -40109,
    "SILVER & BLACK ATTACK": -40109,
    "SJO SPARTAN YOUTH WC": -40109,
    "SOMONAUK WC": -40109,
    "SOUTHERN ILLINOIS UNITED THUNDER CATS": -40109,
    "SPIDER WC": -40109,
    "SPRINGFIELD CAPITALS": -40109,
    "ST. BEDE'S": -40109,
    "ST. CHARLES EAST WC": -40109,
    "ST. TARCISSUS": -40109,
    "STATELINE WILDCATS": -40109,
    "STERLING NEWMAN JR COMETS": -40109,
    "STILLMAN VALLEY WC": -40109,
    "SYCAMORE WC": -40109,
    "T-BIRD RAIDER WRESTLING": -40109,
    "TAKEDOWN WC": -40109,
    "TAYLORVILLE WC": -40109,
    "TEAM WEST WOLVES": -40109,
    "TEST": -40109,
    "THE ZOO WC": -40109,
    "TIGER WC": -40109,
    "TIGERTOWN TANGLERS": -40109,
    "TINLEY PARK BULLDOGS": -40109,
    "TITAN WC": -40109,
    "TOMCAT WC": -40109,
    "TREVIAN WC": -40109,
    "TRI-CITY BRAVES": -40109,
    "TRIAD KNIGHTS": -40109,
    "TWIN CITY WC": -40109,
    "UNITED TOWNSHIP WC": -40109,
    "UNITY WC": -40109,
    "VANDALIA JR WRESTLING": -40109,
    "VILLA LOMBARD COUGARS": -40109,
    "VITTUM CATS": -40109,
    "WARREN COUNTY WC": -40109,
    "WARRENSBURG WC": -40109,
    "WASHINGTON JR PANTHERS": -40109,
    "WAUBONSIE WC": -40109,
    "WEST FRANKFORT JR. WC": -40109,
    "WESTVILLE YOUTH WC": -40109,
    "WHEATON MONROE EAGLES": -40109,
    "WHEATON TIGER WC": -40109,
    "WILMINGTON WC": -40109,
    "WOLFPAK WC": -40109,
    "WRESTLING FACTORY": -40109,
    "YORKVILLE WRESTLING CLUB": -40109,
    "YOUNG CHAMPIONS": -40109,
    "ZEE-BEE STINGERS": -40109,
}


class Competitor(pydantic.BaseModel):
    first_name: str
    last_name: str
    suffix: str | None
    team: str


class Match(pydantic.BaseModel):
    match: str
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
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


TARGET_WEIGHT = 177
TARGET_DIVISION = "senior"
TARGET_NAMES = """BEN TREAT	EDWARDSVILLE WC		4- 0	100.00
BEN PERNA	ARLINGTON CARDINALS		5- 1	83.33
CODY FORCE	ARGENTA/OREANA KIDS CLUB		3- 1	75.00
GEORGE DONOVAN	BADGER WC		3- 2	60.00
DION EMBREY	ROCKFORD WC		3- 2	60.00
JONATHON BECKER	CARY JR TROJAN MATMEN		1- 1	50.00
JAKE SLEDGE	MT. VERNON LIONS		1- 1	50.00
CODY HILL	SJO SPARTAN YOUTH WC		1- 1	50.00
NATHAN LORANCE	WAUBONSIE WC		3- 3	50.00
MATT OPEL	TRIAD KNIGHTS		3- 3	50.00
ZACH KIRKHOVE	SHERRARD JR WC		1- 2	33.33
DANIEL MCSWEENEY	SCN YOUTH WC		1- 2	33.33
JEREMY RADER	VILLA LOMBARD COUGARS		1- 2	33.33
MIKE OLIPHANT	GENESEO WC		1- 2	33.33
JOE FOLLIS	BELVIDERE BANDITS		0- 1	0.00
BILL CARLSON	HARLEM COUGARS		0- 1	0.00
MARK HANE	WHEATON MONROE EAGLES		0- 2	0.00
JACOB GORSKI	DIXON WC		0- 1	0.00
CHRIS MONTOYA	PALATINE JUNIOR PIRATES		0- 1	0.00
NYKOLO PALOMBI	BLAZER KIDS		0- 1	0.00
WAYNE WARDEN	GALESBURG JR STREAKS		0- 1	0.00
CHARLES LEWIS	HARVEY PARK DIST TWISTERS		0- 1	0.00
DANNY CAREY	BLACKHAWK WC		0- 1	0.00"""


def main():
    with open(HERE / "extracted.2004.json") as file_obj:
        extracted = WeightClasses.model_validate_json(file_obj.read())

    weight_classes = extracted.root

    all_competitors_by_team: dict[str, list[CompetitorWithWeight]] = {}
    for weight_class in weight_classes:
        for match in weight_class.matches:
            top_competitor = match.top_competitor
            if top_competitor is not None:
                to_add = CompetitorWithWeight(
                    division=weight_class.division,
                    weight=weight_class.weight,
                    competitor=top_competitor,
                )
                existing = all_competitors_by_team.setdefault(
                    to_add.competitor.team, []
                )
                if not any(to_add == seen for seen in existing):
                    existing.append(to_add)

            bottom_competitor = match.bottom_competitor
            if bottom_competitor is not None:
                to_add = CompetitorWithWeight(
                    division=weight_class.division,
                    weight=weight_class.weight,
                    competitor=bottom_competitor,
                )
                existing = all_competitors_by_team.setdefault(
                    to_add.competitor.team, []
                )
                if not any(to_add == seen for seen in existing):
                    existing.append(to_add)

    team_acronyms = sorted(all_competitors_by_team.keys())
    for acronym in team_acronyms:
        known = TEAM_ACRONYM_MAPPING.get(acronym, "TODO")
        if known != "TODO":
            continue

        print(f"Team: {acronym}")
        for competitor in all_competitors_by_team[acronym]:
            print(f"  {competitor}")

    for line in TARGET_NAMES.split("\n"):
        name, team, _, _, _ = line.split("\t")
        try:
            first_name, last_name = name.split()
        except:
            print((name, team))
            raise
        matches = []
        for acronym in team_acronyms:
            for competitor in all_competitors_by_team[acronym]:
                if competitor.weight != TARGET_WEIGHT:
                    continue
                if competitor.division != TARGET_DIVISION:
                    continue
                if competitor.competitor.first_name != first_name:
                    continue
                if competitor.competitor.last_name != last_name:
                    continue
                matches.append(
                    (first_name, last_name, competitor.competitor.team, team)
                )
        if len(matches) != 1:
            raise RuntimeError(line)
        _, _, acronym, full = matches[0]
        known = TEAM_ACRONYM_MAPPING[acronym]
        if known != "TODO":
            if known != full:
                raise ValueError("Mismatch", acronym, full, known)
        else:
            TEAM_ACRONYM_MAPPING[acronym] = full

    # print(TEAM_ACRONYM_MAPPING)


if __name__ == "__main__":
    main()
