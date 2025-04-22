# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Troy Doughman", team="Elmhurst"),
    65: bracket_utils.Placer(name="Pat Rajnic", team="Wheaton Franklin"),
    70: bracket_utils.Placer(name="Bill Horcher", team="Dundee Highlanders"),
    75: bracket_utils.Placer(name="Tony Pellegrini", team="Hazel Crest"),
    80: bracket_utils.Placer(name="Todd Sterr", team="Joliet Boy's Club"),
    85: bracket_utils.Placer(name="Ed Giese", team="Franklin Park"),
    90: bracket_utils.Placer(name="Kurt Law", team="Savanna"),
    95: bracket_utils.Placer(name="Mark Ruettiger", team="Joliet Boy's Club"),
    100: bracket_utils.Placer(name="Mark Barron", team="Aurora Franklin"),
    105: bracket_utils.Placer(name="Todd Ferris", team="Savanna"),
    112: bracket_utils.Placer(name="Mike Rosman", team="Naperville"),
    118: bracket_utils.Placer(name="Ray Villareal", team="West Chicago"),
    125: bracket_utils.Placer(name="Bill Klotz", team="New Lenox Oakview"),
    135: bracket_utils.Placer(name="Alan Porter", team="Oak Forest"),
    145: bracket_utils.Placer(name="Bill McCue", team="Aurora Simmons"),
    160: bracket_utils.Placer(name="Rich Constable", team="Addison"),
    185: bracket_utils.Placer(name="Bill George", team="St. Thecia"),
    275: bracket_utils.Placer(name="Jeff Sheppard", team="avanna"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "PLAINFIELD": 164.0,
    "SAVANNA": 119.0,
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
    with open(HERE / "extracted.1977.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
