# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {}
_NOVICE_CHAMPS: dict[int, bracket_utils.Placer] = {
    62: bracket_utils.Placer(name="CASSIO PERO", team="HARVEY TWISTERS"),
    66: bracket_utils.Placer(name="FRANK KEELER", team="DOLTON PARK"),
    70: bracket_utils.Placer(name="CALEB FERRY", team="HARLEM COUGARS"),
    74: bracket_utils.Placer(name="ISRAIL MARTINEZ", team="TOMCAT"),
    79: bracket_utils.Placer(name="DUSTY CARPENTER", team="BELEVILLE DEVIL"),
    84: bracket_utils.Placer(name="JOSH PRICE", team="RIVERDALE JR HIGH"),
    89: bracket_utils.Placer(name="ERICK NOVAK", team="TINLEY PARK"),
    95: bracket_utils.Placer(name="MICHAEL KIMBERLIN", team="BRADLEY BOUR"),
    101: bracket_utils.Placer(name="JERREL JONES", team="DOLTON PARK"),
    108: bracket_utils.Placer(name="BRIAN GLYNN", team="ORLAND PARK"),
    115: bracket_utils.Placer(name="CASEY CREGER", team="JORDAN SETON"),
    122: bracket_utils.Placer(name="JOHN HATFIELD", team="BOYS CLUB FREEPORT"),
    130: bracket_utils.Placer(name="ADAM SESSO", team="ADAMS JR COUGARS"),
    147: bracket_utils.Placer(name="ANDREW CURRAN", team="ST BAR/CHRIST KING"),
    166: bracket_utils.Placer(name="JARED BURRES", team="KELLER JR COUGARS"),
    215: bracket_utils.Placer(name="EDMUND NEGRON", team="CPS"),
}
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    70: bracket_utils.Placer(name="George Sims", team="Joliet Boys Club"),
    74: bracket_utils.Placer(name="Jim Brandau", team="Little Celtics"),
    79: bracket_utils.Placer(name="Jerad Karlen", team="Jr. Bears"),
    84: bracket_utils.Placer(name="Nathaniel Martinez", team="Tomcat WC"),
    89: bracket_utils.Placer(name="Deangelo Love", team="Joleit Boys Club"),
    95: bracket_utils.Placer(name="Kyle Oneill", team="Tinley Park Bulldogs"),
    101: bracket_utils.Placer(name="Jeremiah Hayes", team="Morton Youth"),
    108: bracket_utils.Placer(name="Nick Passolano", team="Little Celtic WC"),
    115: bracket_utils.Placer(name="Bill Walsh", team="Crystal Lake Wizards"),
    122: bracket_utils.Placer(name="Brad Schrader", team="Harlem Cougars WC"),
    130: bracket_utils.Placer(name="Tommy Meitus", team="Rosemont Cobras"),
    138: bracket_utils.Placer(name="Shawn Babcock", team="Rockford WC"),
    147: bracket_utils.Placer(name="Brendan Curran", team="St Bar/Christ King"),
    156: bracket_utils.Placer(name="Bill Kopecky", team="Rosemont Cobras"),
    166: bracket_utils.Placer(name="Nick Esposito", team="Villa Lombard"),
    177: bracket_utils.Placer(name="DJ Williams", team="Rockford"),
    189: bracket_utils.Placer(name=" Bill Sladek", team="Addison Indian Trail"),
    275: bracket_utils.Placer(name="Ben Temple", team="Granite City Coolidge"),
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
    with open(HERE / "extracted.1995.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
