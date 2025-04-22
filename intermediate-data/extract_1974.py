# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Ed DeBevec", team="Tinley Park Bulldogs"),
    65: bracket_utils.Placer(name="Bob Whitley", team="Joliet Boy's Club"),
    70: bracket_utils.Placer(name="Dane Nasenbenny", team="Joliet Boy's Club"),
    75: bracket_utils.Placer(name="Mark Trizzino", team="Joliet Boy's Club"),
    80: bracket_utils.Placer(name="Dan Unruh", team="West Chicago"),
    85: bracket_utils.Placer(name="Bob Porter", team="Northfield"),
    90: bracket_utils.Placer(name="Tony Cruz", team="West Chicago"),
    97: bracket_utils.Placer(name="Phil Walters", team="Franklin Park"),
    105: bracket_utils.Placer(name="Bob Ryan", team="Sterling Challand"),
    112: bracket_utils.Placer(name="Rich Yale", team="Northfield"),
    118: bracket_utils.Placer(name="Darrell Hasty", team="Granite City"),
    125: bracket_utils.Placer(name="Ed Pineda", team="West Chicago"),
    134: bracket_utils.Placer(name="Rick Sanders", team="Shorewood Troy"),
    143: bracket_utils.Placer(name="Trent Tayor", team="DeKalb Huntley"),
    152: bracket_utils.Placer(name="Dave Conciera", team="Des Plaines Gemini"),
    275: bracket_utils.Placer(name="Kurt Karras", team="Aurora Simmons"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "WEST CHICAGO": 42.0,
    "TINLEY PARK": 40.0,
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
    with open(HERE / "extracted.1974.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
