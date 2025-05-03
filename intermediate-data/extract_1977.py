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
    90: bracket_utils.Placer(name="Kurt Law", team="Savanna"),
    95: bracket_utils.Placer(name="Mark Ruettiger", team="Joliet Boy's Club"),
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
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    85: [
        bracket_utils.Placer(name="Ed Giese", team="Franklin Park"),
        bracket_utils.Placer(name="Bill Kelly", team="Chicago Ridge"),
        bracket_utils.Placer(name="Keith Rogers", team="Plainfield"),
        bracket_utils.Placer(name="Ed DeBevec", team="Tinley Park"),
        bracket_utils.Placer(name="Jim Maddock", team="Marshall"),
        bracket_utils.Placer(name="Jerry Miller", team="Granite City"),
    ],
    100: [
        bracket_utils.Placer(name="Mark Barron", team="Aurora Franklin"),
        bracket_utils.Placer(name="Matt Twitty", team="Mattoon"),
        bracket_utils.Placer(name="Mike Daughters", team="Plainfield"),
        bracket_utils.Placer(name="Ken Mansell", team="Joliet Boy's Club"),
        bracket_utils.Placer(name="Mike Smith", team="Stillman Valley"),
        bracket_utils.Placer(name="Jack Sale", team="Mahomet"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Plainfield": 164.0,  # `143`?
    "Savanna": 119.0,
    "New Lenox Oakview": 85.0,
    "Panther": 73.0,
    "Joliet Boy's Club": 68.0,
    "Aurora Simmons": 58.0,
    "Hazel Crest": 58.0,
    "Aurora Franklin": 57.0,
    "West Chicago": 52.0,
    "Mattoon": 52.0,
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

    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
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
