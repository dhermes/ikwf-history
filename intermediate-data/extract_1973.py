# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Dan Nasenbenny", team="Joliet Boy's Club"),
    65: bracket_utils.Placer(name="Gary Gerdes", team="Oak Forest"),
    70: bracket_utils.Placer(name="Tom Gerdes", team="Oak Forest"),
    75: bracket_utils.Placer(name="Dan Unruh", team="West Chicago"),
    80: bracket_utils.Placer(name="Lee Goldsmith", team="Northfield"),
    85: bracket_utils.Placer(name="Sean Sterr", team="Joliet Boy's Club"),
    90: bracket_utils.Placer(name="Fred Ferrin", team="Romeoville Westview"),
    97: bracket_utils.Placer(name="Bob Guerrero", team="West Chicago"),
    105: bracket_utils.Placer(name="Bill Turnmire", team="Harlem"),
    112: bracket_utils.Placer(name="Rich Konitski", team="Harlem"),
    118: bracket_utils.Placer(name="Jim Steen", team="New Lenox Oakview"),
    125: bracket_utils.Placer(name="Miguel Cortez", team="West Chicago"),
    134: bracket_utils.Placer(name="Scott Glander", team="Naperville Lincoln"),
    143: bracket_utils.Placer(name="Mike Mager", team="New Lenox Oakview"),
    152: bracket_utils.Placer(name="Mel Reglin", team="Sterling Challand"),
    275: bracket_utils.Placer(name="Mike Bardell", team="Glenwood"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "JOLIET BOYS CLUB": 52.0,
    "WEST CHICAGO": 49.0,
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
    with open(HERE / "extracted.1973.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
