# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    50: bracket_utils.Placer(name="Jay Ford", team="New Lenox Lions"),
    55: bracket_utils.Placer(name="Jim Czaikowski", team="Panther WC"),
    60: bracket_utils.Placer(name="Jim Zeilinga", team="Oak Forest"),
    65: bracket_utils.Placer(name="Pat Coleman", team="Burbank"),
    70: bracket_utils.Placer(name="Mike Urwin", team="Orland Park Pioneers"),
    75: bracket_utils.Placer(name="Mark Pustelnik", team="East Moline"),
    80: bracket_utils.Placer(name="Dan O'Brien", team="Chicago Ridge"),
    85: bracket_utils.Placer(name="Ken Thompson", team="Glenwood"),
    90: bracket_utils.Placer(name="Joe Cascone", team="Vittum Vikings"),
    95: bracket_utils.Placer(name="Scott Holbrook", team="Sterling Newman"),
    100: bracket_utils.Placer(name="Adam Caldwell", team="Hazel Crest"),
    105: bracket_utils.Placer(name="Mike Rogers", team="Oak Park"),
    111: bracket_utils.Placer(name="Tom Blaha", team="Frankfort"),
    118: bracket_utils.Placer(name="Paul Dagenais", team="Tinley Park Bulldogs"),
    125: bracket_utils.Placer(name="Jon Popp", team="Panther WC"),
    135: bracket_utils.Placer(name="Pete Pasternak", team="Calumet City"),
    145: bracket_utils.Placer(name="Cliff Wittey", team="Hoopeston"),
    155: bracket_utils.Placer(name="Aaron Faivre", team="DeKalb Huntley"),
    170: bracket_utils.Placer(name="Ron Webb", team="Plainfield"),
    185: bracket_utils.Placer(name="Mark Topping", team="Huth"),
    275: bracket_utils.Placer(name="James Washington", team="Rich Township"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "BURBANK PANTHERS": 145.0,
    "DOLTON FALCONS": 134.0,
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
    with open(HERE / "extracted.1982.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
