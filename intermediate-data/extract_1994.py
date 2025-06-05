# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {}
_NOVICE_CHAMPS: dict[int, bracket_utils.Placer] = {
    62: bracket_utils.Placer(name="GEORGE SIMS", team="JOLIET BOYS CLUB"),
    66: bracket_utils.Placer(name="ISRAEL MARTINEZ", team="TOMCATS"),
    70: bracket_utils.Placer(name="PAUL AUGLE", team="TINLEY PARK"),
    74: bracket_utils.Placer(name="TIMMY SPRINGS", team="HARVEY TWISTERS"),
    79: bracket_utils.Placer(name="BLAKE VERMILLION", team="CRYSTAL LAKE"),
    84: bracket_utils.Placer(name="RAYNELL KIZZEE", team="HARVEY TWISTERS"),
    89: bracket_utils.Placer(name="JERREL JONES", team="DOLTON FALCONS"),
    95: bracket_utils.Placer(name="STEVEN AMY", team="JR. ROCKET"),
    101: bracket_utils.Placer(name="JEFF SCHMERBACH", team="JR. ROCKET"),
    108: bracket_utils.Placer(name="TOM MEITUS", team="ROSEMONT COBRAS"),
    115: bracket_utils.Placer(name="AARON POWERS", team="ROCKFORD"),
    122: bracket_utils.Placer(name="JOE WEBER", team="ROSEMONT COBRAS"),
    138: bracket_utils.Placer(name="RAYMOND BOYD", team="VITTUM CATS"),
    156: bracket_utils.Placer(name="NICK ESPOSITO", team="VILLA LOMBARD"),
    177: bracket_utils.Placer(name="EDMUND NEGRON", team="CPS"),
    215: bracket_utils.Placer(name="BAILEY FERKEL", team="JR. ROCKET"),
}
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    70: bracket_utils.Placer(name="Jim Brandau", team="Little Celtics WC"),
    74: bracket_utils.Placer(name="Nick Cirrincione", team="Villa-Lombard"),
    79: bracket_utils.Placer(name="Kyle Oneill", team="Tinley Park Bulldogs"),
    84: bracket_utils.Placer(name="David Drew", team="Mustang WC"),
    89: bracket_utils.Placer(name="Amador Estrada", team="Round Lake"),
    95: bracket_utils.Placer(name="Brian Wilson", team="Crystal Lake Wizards"),
    101: bracket_utils.Placer(name="Anthony Opiola", team="Dolton Park Falcon"),
    108: bracket_utils.Placer(name="Brad Owens", team="Mt. Zion WC"),
    115: bracket_utils.Placer(name="Sandro Nunez", team="Lil Reaper Wrestling"),
    122: bracket_utils.Placer(name="Matt Lackey", team="Moline Tigers"),
    130: bracket_utils.Placer(name="Billy Izzi", team="Oak Forest Warriors"),
    138: bracket_utils.Placer(name="Andrew Harrison", team="Addison Indian Tr"),
    147: bracket_utils.Placer(name="Bill Kopecky", team="Rosemont Cobras"),
    156: bracket_utils.Placer(name="Joseph Chirumbolo", team="Eagle WC"),
    166: bracket_utils.Placer(name="Matthew Cordes", team="Moline Tigers"),
    177: bracket_utils.Placer(name="Jon Lovrich", team="Hickory Hills PD"),
    189: bracket_utils.Placer(name="Anthony Englese", team="Mead JH School"),
    275: bracket_utils.Placer(name="Benjamin Bertelsman", team="Little Devils"),
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
    with open(HERE / "extracted.1994.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
