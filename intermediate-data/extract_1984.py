# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    50: bracket_utils.Placer(name="Ryan Ferguson", team="Lancers"),
    55: bracket_utils.Placer(name="Jim Soldan", team="Frankfort"),
    60: bracket_utils.Placer(name="Brent Laroche", team="Panther WC"),
    65: bracket_utils.Placer(name="Andy Gardner", team="Lanphier Southeast"),
    70: bracket_utils.Placer(name="Chris Buenik", team="Vittum Cats"),
    75: bracket_utils.Placer(name="Sean Bormet", team="Frankfort"),
    80: bracket_utils.Placer(name="Paul Zina", team="Franklin Park"),
    85: bracket_utils.Placer(name="Matt Gruska", team="Indian Prairie"),
    90: bracket_utils.Placer(name="Sam Geraci", team="Lancers"),
    95: bracket_utils.Placer(name="Bryon Schultz", team="Lanphier Southeast"),
    100: bracket_utils.Placer(name="Bret Schultz", team="Lanphier Southeast"),
    105: bracket_utils.Placer(name="Bob Mena", team="Sterling Newman"),
    111: bracket_utils.Placer(name="Craig Goodchild", team="Dundee Highlande"),
    118: bracket_utils.Placer(name="Larry Logan", team="Barrington"),
    125: bracket_utils.Placer(name="Bill Novak", team="Panther WC"),
    135: bracket_utils.Placer(name="Richard Harvey", team="Decatur YMCA"),
    145: bracket_utils.Placer(name="Pat Wheeler", team="Frankfort"),
    155: bracket_utils.Placer(name="Jesus Garcia", team="Rich Township"),
    170: bracket_utils.Placer(name="Andy Sharp", team="DeKalb Huntley"),
    185: bracket_utils.Placer(name="Dana Dunklau", team="Frankfort"),
    275: bracket_utils.Placer(name="Adam Lang", team="Carol Stream"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "VITTUM CATS": 134.0,
    "BURBANK PANTHERS": 128.0,
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
    with open(HERE / "extracted.1984.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
