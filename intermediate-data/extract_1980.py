# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Mark Pustelnik", team="East Moline"),
    65: bracket_utils.Placer(name="Dan Evensen", team="Chicago Ridge"),
    70: bracket_utils.Placer(name="Darrell Williams", team="Rich Township"),
    75: bracket_utils.Placer(name="Mike O'Brien", team="Chicago Ridge"),
    80: bracket_utils.Placer(name="Tom O'Brien", team="Chicago Ridge"),
    85: bracket_utils.Placer(name="Craig DeBevec", team="Oak Forest Warriors"),
    90: bracket_utils.Placer(name="Mike Vasquez", team="Sterling Challand"),
    95: bracket_utils.Placer(name="Scott Pierre", team="Wheaton Franklin"),
    100: bracket_utils.Placer(name="Steve Crnich", team="Oak Forest Warriors"),
    105: bracket_utils.Placer(name="Mike Hruska", team="West Leyden"),
    111: bracket_utils.Placer(name="Jim Schultz", team="Burbank"),
    118: bracket_utils.Placer(name="John Jackson", team="East Moline"),
    125: bracket_utils.Placer(name="Chris Rosman", team="Barrington"),
    135: bracket_utils.Placer(name="Steve Meyers", team="Hickory Hills"),
    145: bracket_utils.Placer(name="Andy Lehn", team="Antioch"),
    155: bracket_utils.Placer(name="Tony Savegnago", team="Carol Stream"),
    170: bracket_utils.Placer(name="Jeff Adams", team="Glenwood"),
    185: bracket_utils.Placer(name="Mark Antonietti", team="Calumet City"),
    275: bracket_utils.Placer(name="Jim McCoy", team="Barrington"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "CHICAGO RIDGE": 192.0,
    "PLAINFIELD": 139.0,
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
    with open(HERE / "extracted.1980.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
