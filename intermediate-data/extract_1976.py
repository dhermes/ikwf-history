# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Bob Sineni", team="Tinley Park Bulldogs"),
    65: bracket_utils.Placer(name="Todd Sterr", team="Joliet Boy's Club"),
    70: bracket_utils.Placer(name="David Harris", team="Belleville"),
    75: bracket_utils.Placer(name="Paul Kelly", team="Chicago Ridge"),
    80: bracket_utils.Placer(name="Paul Dina", team="Burbank"),
    85: bracket_utils.Placer(name="Joe Blaney", team="Burbank"),
    90: bracket_utils.Placer(name="Eric Potts", team="Wilmette"),
    95: bracket_utils.Placer(name="Al Skiniotes", team="New Lenox Oakview"),
    100: bracket_utils.Placer(name="Dan Helminski", team="Dundee Highlanders"),
    105: bracket_utils.Placer(name="Jon Smith", team="Mattoon"),
    112: bracket_utils.Placer(name="Steve Bolsoni", team="Oak Forest"),
    118: bracket_utils.Placer(name="Tony Daidone", team="Oak Forest"),
    125: bracket_utils.Placer(name="Bob Mansell", team="Joliet Boy's Club"),
    135: bracket_utils.Placer(name="Ernie Vatch", team="Addison Indian Trail"),
    145: bracket_utils.Placer(name="George Dergo", team="Morris"),
    160: bracket_utils.Placer(name="Wayne Frase", team="Wheaton"),
    275: bracket_utils.Placer(name="Emilio Escamile", team="West Chicago"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "BURBANK PANTHERS": 46.0,
    "OAK FOREST": 41.0,
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
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
    with open(HERE / "extracted.1976.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
