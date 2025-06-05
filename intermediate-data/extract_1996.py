# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {}
_NOVICE_CHAMPS: dict[int, bracket_utils.Placer] = {
    62: bracket_utils.Placer(name="CASSIO PERO", team="HARVEY TWISTERS"),
    66: bracket_utils.Placer(name="BRIAN DYER", team="NAPERVILLE WC"),
    70: bracket_utils.Placer(name="CHARLES LLOYD", team="HARVEY TWISTERS"),
    74: bracket_utils.Placer(name="FRANK KEELER", team="DOLTON PARK"),
    79: bracket_utils.Placer(name="DONNELL BRADLEY", team="JOLIET BOYS CLUB"),
    84: bracket_utils.Placer(name="DUSTY CARPENTER", team="BELLEVILLE"),
    89: bracket_utils.Placer(name="LAMBRO FOTOS", team="EAST MOLINE"),
    95: bracket_utils.Placer(name="NATHAN MCMILLIN", team="MT. ZION"),
    101: bracket_utils.Placer(name="TIM SPRINGS", team="HARVEY TWISTERS"),
    108: bracket_utils.Placer(name="ERIC RAFFERTY", team="BLACKHAWK"),
    115: bracket_utils.Placer(name="PHILIP NEWELL", team="WHEATON BULLDOGS"),
    122: bracket_utils.Placer(name="MICHAEL BOYD", team="VITTUM CATS"),
    130: bracket_utils.Placer(name="DAVID WOOSLEY", team="BELVIDERE BANDITS"),
    147: bracket_utils.Placer(name="MICHAEL HAMILTON", team="HARLEM"),
    166: bracket_utils.Placer(name="MATTHEW SEIDEL", team="TIGERTOWN"),
    215: bracket_utils.Placer(name="MATT FLETCHER", team="L-P CRUNCHING CAVS"),
}
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    70: bracket_utils.Placer(name="Luke Jones", team="Tinley Park Bulldogs"),
    74: bracket_utils.Placer(name="Dale Burke", team="Vittum Cats"),
    79: bracket_utils.Placer(name="Israel Martinez", team="Tomcats"),
    84: bracket_utils.Placer(name="Justin Clubb", team="Harlem Cougars"),
    89: bracket_utils.Placer(name="Gary Oxford", team="Granite City Cool"),
    95: bracket_utils.Placer(name="Paul Collum", team="Lemont Bears"),
    101: bracket_utils.Placer(name="Danny Alcocer", team="Waubonsie Braves"),
    108: bracket_utils.Placer(name="Eric Novak", team="Tinley Park Bulldogs"),
    115: bracket_utils.Placer(name="Jerrell Jones", team="Dolton Park Falcons"),
    122: bracket_utils.Placer(name="Brian Glynn", team="Orland Park Pioneers"),
    130: bracket_utils.Placer(name="Steve Amy", team="Jr. Rocket WC"),
    138: bracket_utils.Placer(name="Dan Niles", team="Yorkville WC"),
    147: bracket_utils.Placer(name="Andrew Curran", team="St.Bar/Christ King"),
    156: bracket_utils.Placer(name="Jared Burress", team="Junior Cougars"),
    166: bracket_utils.Placer(name="Jerard Burress", team="Junior Cougar WC"),
    177: bracket_utils.Placer(name="Michael Collier", team="Pekin Boys Club"),
    189: bracket_utils.Placer(name="Shawn Richmond", team="Morrison Stallion"),
    275: bracket_utils.Placer(name="Timothy Daly", team="Villa Lombard Couga"),
}


def main():
    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _NOVICE_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "novice", weight, champ, _NOVICE_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores={}, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1996.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
