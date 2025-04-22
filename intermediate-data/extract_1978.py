# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Mike O'Brien", team="Chicago Ridge"),
    65: bracket_utils.Placer(name="Chris Scott", team="Joliet YMCA"),
    70: bracket_utils.Placer(name="John Ruiter", team="Joliet YMCA"),
    75: bracket_utils.Placer(name="Scott Pierre", team="Wheaton Franklin"),
    80: bracket_utils.Placer(name="Mike Pierre", team="Wheaton Franklin"),
    85: bracket_utils.Placer(name="Brian Porter", team="Oak Forest Warriors"),
    90: bracket_utils.Placer(name="Jeff Schultz", team="Burbank"),
    95: bracket_utils.Placer(name="Tony Prate", team="Orland Park Pioneers"),
    100: bracket_utils.Placer(name="Rick Criscione", team="Joliet YMCA"),
    105: bracket_utils.Placer(name="Mike Smith", team="Stillman Valley"),
    112: bracket_utils.Placer(name="Guy Milburn", team="Dolton"),
    118: bracket_utils.Placer(name="Evan Dale", team="Joliet Washington"),
    125: bracket_utils.Placer(name="Ken Mansell", team="Joliet Boy's Club"),
    135: bracket_utils.Placer(name="Mike Rosman", team="Walter Sundling"),
    145: bracket_utils.Placer(name="Mike Prsybysz", team="Plainfield Indian Tra"),
    160: bracket_utils.Placer(name="Larry Leiparte", team="Mt. Greenwood"),
    185: bracket_utils.Placer(name="Rick Meier", team="DeKalb Huntley"),
    275: bracket_utils.Placer(name="Noah Tyree", team="Bolingbrook Ward"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "PLAINFIELD": 122.5,
    "JOLIET YMCA": 86.0,
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
    with open(HERE / "extracted.1978.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
