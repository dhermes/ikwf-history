# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import Literal

import pydantic

HERE = pathlib.Path(__file__).resolve().parent
TEAM_ACRONYM_MAPPING = {
    "ALE": "TODO",
    "ALL": "TODO",
    "ARG": "TODO",
    "ARL": "TODO",
    "BAD": "TODO",
    "BAH": "TODO",
    "BAT": "TODO",
    "BEL": "TODO",
    "BEN": "TODO",
    "BET": "TODO",
    "BEV": "TODO",
    "BIO": "TODO",
    "BIS": "TODO",
    "BLA": "TODO",
    "BLK": "TODO",
    "BLO": "TODO",
    "BRA": "TODO",
    "CAL": "TODO",
    "CAR": "TODO",
    "CAY": "TODO",
    "CHA": "TODO",
    "CHB": "TODO",
    "CHE": "TODO",
    "CHL": "TODO",
    "CHR": "TODO",
    "CRI": "TODO",
    "CRY": "TODO",
    "CUM": "TODO",
    "DAK": "TODO",
    "DEK": "TODO",
    "DIX": "TODO",
    "DOW": "TODO",
    "DUN": "TODO",
    "DUP": "TODO",
    "EDW": "TODO",
    "EFF": "TODO",
    "ELM": "TODO",
    "ELP": "TODO",
    "FAC": "TODO",
    "FAI": "TODO",
    "FAL": "TODO",
    "FEN": "TODO",
    "FIG": "TODO",
    "FIS": "TODO",
    "FOR": "TODO",
    "FOX": "TODO",
    "GAL": "TODO",
    "GEE": "TODO",
    "GEN": "TODO",
    "GEO": "TODO",
    "GLA": "TODO",
    "GLN": "TODO",
    "GRA": "TODO",
    "GRP": "TODO",
    "HAE": "TODO",
    "HAR": "TODO",
    "HER": "TODO",
    "HIG": "TODO",
    "HIL": "TODO",
    "HIN": "TODO",
    "HOF": "TODO",
    "HON": "TODO",
    "HOO": "TODO",
    "JAC": "TODO",
    "JOL": "TODO",
    "JRG": "TODO",
    "JRP": "TODO",
    "JRR": "TODO",
    "JRS": "TODO",
    "JRX": "TODO",
    "JUP": "TODO",
    "KNI": "TODO",
    "LAE": "TODO",
    "LAN": "TODO",
    "LAW": "TODO",
    "LEM": "TODO",
    "LIB": "TODO",
    "LIC": "TODO",
    "LII": "TODO",
    "LIL": "TODO",
    "LIM": "TODO",
    "LIN": "TODO",
    "LIO": "TODO",
    "LIP": "TODO",
    "LIR": "TODO",
    "LIV": "TODO",
    "LOC": "TODO",
    "LPC": "TODO",
    "MAC": "TODO",
    "MAF": "TODO",
    "MAI": "TODO",
    "MAN": "TODO",
    "MAR": "TODO",
    "MAT": "TODO",
    "MEN": "TODO",
    "MET": "TODO",
    "MID": "TODO",
    "MOL": "TODO",
    "MOT": "TODO",
    "MTZ": "TODO",
    "MUR": "TODO",
    "MUS": "TODO",
    "NAP": "TODO",
    "NOT": "TODO",
    "OAK": "TODO",
    "OAL": "TODO",
    "OAW": "TODO",
    "ORL": "TODO",
    "OSW": "TODO",
    "PAL": "TODO",
    "PAN": "TODO",
    "PAT": "TODO",
    "PLA": "TODO",
    "POL": "TODO",
    "PON": "TODO",
    "QUI": "TODO",
    "RAI": "TODO",
    "RAM": "TODO",
    "RIC": "TODO",
    "RIV": "TODO",
    "RJH": "TODO",
    "ROC": "TODO",
    "ROF": "TODO",
    "ROK": "TODO",
    "ROX": "TODO",
    "SAU": "TODO",
    "SAV": "TODO",
    "SCN": "TODO",
    "SEN": "TODO",
    "SHA": "TODO",
    "SHE": "TODO",
    "SIL": "TODO",
    "SJO": "TODO",
    "SOU": "TODO",
    "SPR": "TODO",
    "STC": "TODO",
    "STI": "TODO",
    "STT": "TODO",
    "SYC": "TODO",
    "TAK": "TODO",
    "TAY": "TODO",
    "TBI": "TODO",
    "TIG": "TODO",
    "TIN": "TODO",
    "TOM": "TODO",
    "TRE": "TODO",
    "TRI": "TODO",
    "TTT": "TODO",
    "UNI": "TODO",
    "UNT": "TODO",
    "VAN": "TODO",
    "VIL": "VILLA LOMBARD COUGARS",
    "VIT": "VITTUM CATS",
    "WAR": "TODO",
    "WAU": "TODO",
    "WEC": "TODO",
    "WES": "TODO",
    "WET": "TODO",
    "WHF": "TODO",
    "WHM": "TODO",
    "WHT": "TODO",
    "WIL": "TODO",
    "WOL": "TODO",
    "WRE": "TODO",
    "YOR": "TODO",
    "ZEE": "TODO",
}
TEAM_NAME_MAPPING = {
    "ALEDO BEAR COUNTRY WC": -20802,
    "ALLEMAN JR. PIONEER WC": -20802,
    "ARGENTA/OREANA KIDS CLUB": -20802,
    "ARLINGTON CARDINALS": -20802,
    "BADGER WC": -20802,
    "BARRINGTON BRONCOS": -20802,
    "BARTLETT HAWK WC": -20802,
    "BATAVIA PINNERS": -20802,
    "BELLEVILLE LITTLE DEVILS": -20802,
    "BELVIDERE BANDITS": -20802,
    "BENTON JR. WC": -20802,
    "BETHALTO BULLS WC": -20802,
    "BISMARCK-HENNING WC": -20802,
    "BISON WC": -20802,
    "BLACKHAWK WC": -20802,
    "BLAZER KIDS": -20802,
    "BLOOMINGTON RAIDER WC": -20802,
    "BRAWLERS WC": -20802,
    "CARBONDALE WC": -20802,
    "CARLINVILLE KIDS WC": -20802,
    "CARY JR. TROJAN MATMEN": -20802,
    "CHAMPAIGN KIDS WRESTLING": -20802,
    "CHARLESTON WC": -20802,
    "CHENOA MAT CATS": -20802,
    "CHICAGO BULLDOG WC": -20802,
    "CHILLI DAWGS WC": -20802,
    "CRIMSON HEAT WC": -20802,
    "CRYSTAL LAKE WIZARDS": -20802,
    "CUMBERLAND YOUTH WC": -20802,
    "DAKOTA WC": -20802,
    "DEKALB WC": -20802,
    "DIXON WC": -20802,
    "DOWNERS GROVE COUGARS": -20802,
    "DU-PEC CARNIVORES": -20802,
    "DUNDEE HIGHLANDERS": -20802,
    "EDWARDSVILLE WC": -20802,
    "EFFINGHAM YOUTH WC": -20802,
    "EL PASO WC": -20802,
    "ELMHURST JR. DUKES": -20802,
    "FAIRMONT ROUGH RIDERS": -20802,
    "FALCON WC": -20802,
    "FALCON YOUTH WC": -20802,
    "FENWICK FALCONS WC": -20802,
    "FIGHTIN TITAN WC": -20802,
    "FISHER WC": -20802,
    "FORD HEIGHTS FALCONS": -20802,
    "FOX VALLEY WC": -20802,
    "GALESBURG JR STREAKS": -20802,
    "GENESEO WC": -20802,
    "GENEVA WC": -20802,
    "GEORGETOWN YOUTH WC": -20802,
    "GLADIATORS": -20802,
    "GLENBARD EAST JR RAMS": -20802,
    "GRANITE CITY JR WARRIORS": -20802,
    "GRAPPLIN' DEVILS WC": -20802,
    "HARLEM COUGARS": -20802,
    "HARVEY TWISTERS": -20802,
    "HERRIN WC": -20802,
    "HIGHLAND BULLDOG JR WC": -20802,
    "HILLSBORO JR TOPPERS": -20802,
    "HINSDALE RED DEVIL WC": -20802,
    "HOFFMAN ESTATES WC": -20802,
    "HONONEGAH KIDS WC": -20802,
    "HOOPESTON AREA WC": -20802,
    "JACKSONVILLE WC": -20802,
    "JOLIET BOYS CLUB COBRAS": -20802,
    "JR. GOLDEN EAGLES": -20802,
    "JR. PANTHERS WRESTLING": -20802,
    "JR. ROCKET WC": -20802,
    "JR. SAXONS WC": -20802,
    "JR. SENTINELS WC": -20802,
    "JUNIOR PIRATE WC": -20802,
    "KNIGHTS WRESTLING": -20802,
    "L-P CRUNCHING CAVS": -20802,
    "LAKELAND PREDATORS": -20802,
    "LANCER WC": -20802,
    "LAWRENCE COUNTY WC": -20802,
    "LEMONT BEARS WC": -20802,
    "LIL' ROUGHNECKS": -20802,
    "LIL' STORM YOUTH WRESTLING": -20802,
    "LIMESTONE YOUTH WC": -20802,
    "LINCOLN-WAY WC": -20802,
    "LIONS WC": -20802,
    "LITTLE BOILER WC": -20802,
    "LITTLE CELTIC WC": -20802,
    "LITTLE INDIANS WC": -20802,
    "LITTLE PANTHERS WC": -20802,
    "LITTLE REDBIRD WC": -20802,
    "LITTLE VIKINGS OF H-F": -20802,
    "LOCKPORT GATORS": -20802,
    "MACOMB LITTLE BOMBERS": -20802,
    "MAINE EAGLES WC": -20802,
    "MANTENO JR PANTHERS": -20802,
    "MARENGO WC": -20802,
    "MARTINEZ FOX VALLEY ELITE WC": -20802,
    "MATTOON YOUTH WC": -20802,
    "MENDOTA MAT MASTERS": -20802,
    "METAMORA KIDS WC": -20802,
    "MIDWEST CENTRAL YOUTH": -20802,
    "MOLINE WC": -20802,
    "MORTON LITTLE MUSTANGS": -20802,
    "MORTON YOUTH WC": -20802,
    "MT. ZION WC": -20802,
    "MURPHYSBORO WRESTLING": -20802,
    "MUSTANG WC": -20802,
    "Mike": -20802,
    "NAPERVILLE WC": -20802,
    "NOTRE DAME WC": -20802,
    "OAK FOREST WARRIORS": -20802,
    "OAK LAWN P.D. WILDCATS": -20802,
    "OAKWOOD WC": -20802,
    "ORLAND PARK PIONEERS": -20802,
    "OSWEGO PANTHERS": -20802,
    "PALATINE PANTHERS": -20802,
    "PANTHER CUB WC": -20802,
    "PANTHER WC": -20802,
    "PLAINFIELD WC": -20802,
    "POLO WC": -20802,
    "PONTIAC PYTHONS": -20802,
    "QUINCY WC": -20802,
    "RAIDER WC": -20802,
    "RAMS WC": -20802,
    "RICH RATTLERS": -20802,
    "RIVERBEND WC": -20802,
    "RIVERDALE JR. HIGH": -20802,
    "ROCHELLE WC": -20802,
    "ROCK ISLAND JR. ROCKS": -20802,
    "ROCK ISLAND WC": -20802,
    "ROCKFORD WC": -20802,
    "ROXANA KIDS WRESTING CLUB": -20802,
    "SAUKEE YOUTH WC": -20802,
    "SAVANNA REDHAWKS": -20802,
    "SCN YOUTH WC": -20802,
    "SENECA IRISH CADETS": -20802,
    "SHAMROCK WC": -20802,
    "SHELBYVILLE JR. RAMS WC": -20802,
    "SILVER & BLACK ATTACK": -20802,
    "SJO YOUTH WC": -20802,
    "SOUTHERN ILLINOIS EAGLES": -20802,
    "SPRINGFIELD CAPITALS": -20802,
    "ST. CHARLES WC": -20802,
    "ST. TARCISSUS": -20802,
    "STILLMAN VALLEY WC": -20802,
    "SYCAMORE WC": -20802,
    "T-BIRD/RAIDER WRESTLING": -20802,
    "TAKEDOWN WC": -20802,
    "TAYLORVILLE WC": -20802,
    "TIGER WC": -20802,
    "TIGERTOWN TANGLERS": -20802,
    "TINLEY PARK BULLDOGS": -20802,
    "TOMCAT WC": -20802,
    "TREVIAN WC": -20802,
    "TRIAD KNIGHTS": -20802,
    "UNITED TOWNSHIP WC": -20802,
    "UNITY WC": -20802,
    "VANDALIA JR WRESTLING": -20802,
    "VILLA LOMBARD COUGARS": -20802,
    "VITTUM CATS": -20802,
    "WARRENSBURG WC": -20802,
    "WAUBONSIE WC": -20802,
    "WEST CHICAGO SPIDER WC": -20802,
    "WEST FRANKFORT JR. WC": -20802,
    "WESTVILLE YOUTH WC": -20802,
    "WHEATON FRANKLIN WC": -20802,
    "WHEATON MONROE EAGLES": -20802,
    "WHEATON TIGER WC": -20802,
    "WILMINGTON WC": -20802,
    "WOLFPAK WC": -20802,
    "WRESTLING FACTORY": -20802,
    "YORKVILLE WC": -20802,
    "ZEE-BEE STINGERS": -20802,
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


def main():
    with open(HERE / "extracted.2003.json", "rb") as file_obj:
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

    print({team: "TODO" for team in sorted(all_competitors_by_team.keys())})

    team_name = "VIT"
    print(f"Team: {team_name}")
    for competitor in all_competitors_by_team[team_name]:
        print(f"  {competitor}")

    raise NotImplementedError(len(weight_classes))


if __name__ == "__main__":
    main()
