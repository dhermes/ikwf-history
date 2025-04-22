# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Phil Gray", team="Naperville"),
    65: bracket_utils.Placer(name="Mike O'Brien", team="Chicago Ridge"),
    70: bracket_utils.Placer(name="Tim Meagher", team="Joliet YMCA"),
    75: bracket_utils.Placer(name="Rob Milazzo", team="Roxana"),
    80: bracket_utils.Placer(name="Chris Scott", team="Joliet YMCA"),
    85: bracket_utils.Placer(name="Nick Quaz", team="Plainfield"),
    90: bracket_utils.Placer(name="Keith Healy", team="Burbank"),
    95: bracket_utils.Placer(name="Jerry Blaney", team="Burbank"),
    100: bracket_utils.Placer(name="Brian Capodice", team="Mokena"),
    105: bracket_utils.Placer(name="Tony Evensen", team="Chicago Ridge"),
    111: bracket_utils.Placer(name="Bob Guirriero", team="West Leyden"),
    118: bracket_utils.Placer(name="Rich Henderson", team="Plainfield Indian Tr"),
    125: bracket_utils.Placer(name="Tim Cocco", team="Chicago Ridge"),
    135: bracket_utils.Placer(name="George Bessette", team="Antioch"),
    145: bracket_utils.Placer(name="Dale Schmidt", team="Oak Forest Warriors"),
    155: bracket_utils.Placer(name="Dave Vohaska", team="Franklin Park"),
    170: bracket_utils.Placer(name="Rod Martin", team="St. Philip Neri"),
    185: bracket_utils.Placer(name="Dennis Stabl", team="Champaign"),
    275: bracket_utils.Placer(name="Ray Tyree", team="Bolingbrook Ward"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "PLAINFIELD": 146.0,
    "JOLIET YMCA": 119.0,
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
    with open(HERE / "extracted.1979.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
