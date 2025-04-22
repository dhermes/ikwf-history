# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    55: bracket_utils.Placer(name="Ryan Ferguson", team="Lancers"),
    60: bracket_utils.Placer(name="Jim Soldan", team="Frankfort"),
    65: bracket_utils.Placer(name="Rich Weeden", team="Villa-Lombard"),
    70: bracket_utils.Placer(name="Ken Gerdes", team="Orland Park Pioneers"),
    75: bracket_utils.Placer(name="Ricky Harris", team="Tinley Park Bulldogs"),
    80: bracket_utils.Placer(name="Doug Hayes", team="Oak Forest Warriors"),
    85: bracket_utils.Placer(name="Mike Dusel", team="Villa-Lombard"),
    90: bracket_utils.Placer(name="Sean Bormet", team="Frankfort"),
    100: bracket_utils.Placer(name="Bill Guide", team="Vittum Cats"),
    105: bracket_utils.Placer(name="Ryan Shafer", team="Warrior WC"),
    111: bracket_utils.Placer(name="John Granat", team="Vittum Cats"),
    118: bracket_utils.Placer(name="Joe Gilbert", team="Tinley Park Bulldogs"),
    125: bracket_utils.Placer(name="Paul Andreotti", team="Orland Park Pioneers"),
    135: bracket_utils.Placer(name="Chuck Sparks", team="Granite City Coolidg"),
    145: bracket_utils.Placer(name="Kevin Nolan", team="Colts WC"),
    155: bracket_utils.Placer(name="Mike Manganiello", team="Vittum Cats"),
    170: bracket_utils.Placer(name="Sherif Zegar", team="Panther WC"),
    185: bracket_utils.Placer(name="Randy Scianna", team="Oak Forest Warriors"),
    275: bracket_utils.Placer(name="Andy Grimm", team="Villa Lombard"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "VITTUM CATS": 287.0,
    "BURBANK PANTHERS": 174.0,
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
    with open(HERE / "extracted.1985.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
