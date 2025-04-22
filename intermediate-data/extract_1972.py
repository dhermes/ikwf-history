# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Pat Sterr", team="Joliet Boy's Club"),
    65: bracket_utils.Placer(name="Tom Gerdes", team="Arbor Park"),
    70: bracket_utils.Placer(name="Lee Goldsmith", team="Northfield"),
    77: bracket_utils.Placer(name="Jim Barrett", team="Des Plaines Apollo"),
    83: bracket_utils.Placer(name="Joe Williams", team="DeKalb Huntley"),
    90: bracket_utils.Placer(name="John Jackson", team="New Lenox Oakview"),
    97: bracket_utils.Placer(name="Jeff Gerdes", team="Oak Forest"),
    105: bracket_utils.Placer(name="Chip Connor", team="New Lenox Oakview"),
    112: bracket_utils.Placer(name="Carl Schultz", team="Northbrook"),
    118: bracket_utils.Placer(name="King Mueller", team="Romeoville Westview"),
    125: bracket_utils.Placer(name="Ron Cuevas", team="Sterling Challand"),
    132: bracket_utils.Placer(name="Jim Mouroukas", team="Des Plaines Park"),
    138: bracket_utils.Placer(name="Greg Enerson", team="Morris"),
    145: bracket_utils.Placer(name="Gehrig Dergo", team="Morris"),
    152: bracket_utils.Placer(name="Tim Cairns", team="Rock Falls"),
    275: bracket_utils.Placer(name="Rob Boehmer", team="Carol Stream"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "ARBOR PARK": 24.0,
    "NEW LENOX": 24.0,
    "DeKALB-HUNTLEY": 21.0,
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
    with open(HERE / "extracted.1972.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
