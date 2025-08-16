# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Bob Porter", team="Parkview"),  # Bobby?
    65: bracket_utils.Placer(name="Lee Goldsmith", team="Northfield"),
    70: bracket_utils.Placer(name="Kurt Schmidt", team="Des Plaines Gemini"),
    77: bracket_utils.Placer(name="Kevin Walsh", team="Des Plaines Gemini"),
    83: bracket_utils.Placer(name="Jesse Shaw", team="Joliet Boy's Club"),
    90: bracket_utils.Placer(name="Jerry LaBaude", team="Rockford"),  # LA BANDE?
    97: bracket_utils.Placer(name="Albert Sullivan", team="DeKalb Rosette"),
    105: bracket_utils.Placer(name="Rick Morris", team="Grove"),
    112: bracket_utils.Placer(name="Joe Eisen", team="Northfield"),
    118: bracket_utils.Placer(name="Dan Prellberg", team="Deerfield"),
    125: bracket_utils.Placer(name="John Stanaway", team="Sterling Challand"),
    132: bracket_utils.Placer(name="Joe Perez", team="Joliet Park District"),
    138: bracket_utils.Placer(name="Chip Tyler", team="New Lenox Oakview"),
    145: bracket_utils.Placer(name="Earl Meyerhoff", team="Des Plaines Gemini"),
    152: bracket_utils.Placer(name="Claudio Balli", team="DeKalb Rosette"),
    275: bracket_utils.Placer(name="John Gurka", team="New Lenox Oakview"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "New Lenox Oakview": 53.0,  # NEW LENOX
    "Des Plaines Gemini": 30.0,  # GEMINI JR. HIGH
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
    with open(HERE / "extracted.1971.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
