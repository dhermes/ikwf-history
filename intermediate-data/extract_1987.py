# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Ben Gerdes", team="Orland Park Pioneers"),
    65: bracket_utils.Placer(name="Cory Daker", team="Forman WC"),
    70: bracket_utils.Placer(name="Jay Ford", team="Rich Wrestling Ltd."),
    75: bracket_utils.Placer(name="Dan Gilbert", team="Tinley Park Bulldogs"),
    80: bracket_utils.Placer(name="Keith Snyder", team="Panther WC"),
    85: bracket_utils.Placer(name="Steve Williams", team="Harvey Twisters"),
    90: bracket_utils.Placer(name="Joe Williams", team="Harvey Twisters"),
    100: bracket_utils.Placer(name="Paul Blaha", team="Frankfort"),
    105: bracket_utils.Placer(name="Cass Lundgren", team="DeKalb WC"),
    111: bracket_utils.Placer(name="Terrell Sandifer", team="Harvey Twisters"),
    118: bracket_utils.Placer(name="Chris Ireland", team="Moline Wildcats"),
    125: bracket_utils.Placer(name="Jim Czajkowski", team="Panther WC"),
    135: bracket_utils.Placer(name="Bryan Rebhan", team="Naperville Warhawk"),
    145: bracket_utils.Placer(name="Doug Seehase", team="DeKalb WC"),
    155: bracket_utils.Placer(name="George Hollendoner", team="Tinley Park"),
    170: bracket_utils.Placer(name="James Quarles", team="Harvey Twisters"),
    185: bracket_utils.Placer(name="Patrick McDonald", team="Harvey Twisters"),
    275: bracket_utils.Placer(name="Todd Nesbitt", team="Harvey Twisters"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY TWISTERS": 248.0,
    "VITTUM CATS": 165.0,
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
    with open(HERE / "extracted.1987.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
