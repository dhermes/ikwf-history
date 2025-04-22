# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    50: bracket_utils.Placer(name="Keith Ruiter", team="New Lenox Oakview"),
    55: bracket_utils.Placer(name="Jeff Vasques", team="Barrington"),
    60: bracket_utils.Placer(name="Sam Geraci", team="Bensenville"),
    65: bracket_utils.Placer(name="Brian Edelen", team="Tinley Park Bulldogs"),
    70: bracket_utils.Placer(name="Mark Pustelnik", team="East Moline"),
    75: bracket_utils.Placer(name="Dan Evensen", team="Chicago Ridge"),
    80: bracket_utils.Placer(name="Alan Crnich", team="Oak Forest Warriors"),
    85: bracket_utils.Placer(name="Mark Becker", team="Panther WC"),
    90: bracket_utils.Placer(name="Greg Farnsworth", team="Batavia"),
    95: bracket_utils.Placer(name="Tom O'Brien", team="Chicago Ridge"),
    100: bracket_utils.Placer(name="Jon Popp", team="Panther WC"),
    105: bracket_utils.Placer(name="Eric Morrissey", team="Rosemont"),
    111: bracket_utils.Placer(name="Scott Pierre", team="Wheaton Franklin"),
    118: bracket_utils.Placer(name="Terry Navarro", team="Panther WC"),
    125: bracket_utils.Placer(name="Brian Antonietti", team="Calumet City"),
    135: bracket_utils.Placer(name="John Cortez", team="West Chicago"),
    145: bracket_utils.Placer(name="Kip Westbrook", team="East Moline"),
    155: bracket_utils.Placer(name="Dannell Vinson", team="Decatur"),
    170: bracket_utils.Placer(name="Rick Hufnus", team="???"),
    185: bracket_utils.Placer(name="Pete Obson", team="Dundee Highlanders"),
    275: bracket_utils.Placer(name="Mike Mroczek", team="Matburns"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "BURBANK PANTHERS": 195.0,
    "CHICAGO RIDGE": 145.0,
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1981.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
