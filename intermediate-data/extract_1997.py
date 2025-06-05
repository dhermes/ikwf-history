# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {}
_NOVICE_CHAMPS: dict[int, bracket_utils.Placer] = {
    62: bracket_utils.Placer(name="ZACHARY BERMAN", team="LITTLE CELTICS"),
    66: bracket_utils.Placer(name="BRIAN DYER", team="NAPERVILLE WC"),
    70: bracket_utils.Placer(name="CASSIO PERO", team="HARVEY TWISTERS"),
    74: bracket_utils.Placer(name="KEVIN KENNEDY", team="ORLAND PARK"),
    79: bracket_utils.Placer(name="ERIC TANNENBAUM", team="NAPERVILLE WC"),
    84: bracket_utils.Placer(name="JACOB KIRBY", team="LIONS WC"),
    89: bracket_utils.Placer(name="FRANK KEELER", team="DOLTON PARK"),
    95: bracket_utils.Placer(name="DUSTY CARPENTER", team="BELLEVILLE"),
    101: bracket_utils.Placer(name="MIKE CLIMEK", team="ORLAND PARK PIONEERS"),
    108: bracket_utils.Placer(name="MATT WINTERHALTER", team="DAKOTA"),
    115: bracket_utils.Placer(name="JASON SHOWALTER", team="WHEATON"),
    122: bracket_utils.Placer(name="EVAN MCCALLISTER", team="RIVERBEND WC"),
    130: bracket_utils.Placer(name="MILAN ECHVARRIA", team="HAWKEYES"),
    147: bracket_utils.Placer(name="JASON AMBLE", team="JORDAN SETAN WC"),
    166: bracket_utils.Placer(name="COREY FORD", team=" BELLEVILLE"),
    215: bracket_utils.Placer(name="MURPHY MAHALIK", team=" LITTLE CELTICS"),
}
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    70: bracket_utils.Placer(name="Brian Arko", team="Villa Lombard Cougars"),
    74: bracket_utils.Placer(name="Dan Kunzer", team="Little Celtics"),
    79: bracket_utils.Placer(name="Matt Kucula", team="Little Celtics"),
    84: bracket_utils.Placer(name="Ray Blake", team="Tinley Park Bulldogs"),
    89: bracket_utils.Placer(name="Aaron Rujuwitz", team="Belleville Devils"),
    95: bracket_utils.Placer(name="Israel Martinez", team="Tomcat"),
    101: bracket_utils.Placer(name="Jim Preston", team="Orland Park Pioneers"),
    108: bracket_utils.Placer(name="Labro Fotos", team="East Moline"),
    115: bracket_utils.Placer(name="Timothy Springs", team="Harvey Twisters"),
    122: bracket_utils.Placer(name="Dustin Scholeman", team="Metro Stallions"),
    130: bracket_utils.Placer(name="Michael Kimberlin", team="Bradly Bourb."),
    138: bracket_utils.Placer(name="Michael Boyd", team="Vittum Cats"),
    147: bracket_utils.Placer(name="David Woosley", team="Belvidere Bandits"),
    156: bracket_utils.Placer(name="Chad Beasley", team="Belvidere Bandits"),
    166: bracket_utils.Placer(name="Sergio Escobar", team="Ram WC"),
    177: bracket_utils.Placer(name="Anthony Clauss", team="???"),
    189: bracket_utils.Placer(name="Julius Word", team="Murphysboro Blue Dev"),
    275: bracket_utils.Placer(name="David Crouch", team="Granite City"),
}


def main():
    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _NOVICE_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "novice", weight, champ, _NOVICE_TEAM_REPLACE
        )

        if weight == 130:
            (champ_match,) = weight_class.matches
            champ_match.top_competitor.full_name = "MILAN ECHVARRIA III"

        weight_classes.append(weight_class)

    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )

        if weight == 275:
            (champ_match,) = weight_class.matches
            champ_match.top_competitor.full_name = "David Crouch II"

        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores={}, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1997.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
