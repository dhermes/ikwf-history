# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import manual_entry

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Tony Prate", team="Tinley Park Bulldogs"),
    70: bracket_utils.Placer(name="Bob Whitley", team="Joliet Boy's Club"),
    75: bracket_utils.Placer(name="Gary Gerdes", team="Oak Forest"),
    80: bracket_utils.Placer(name="Dane Nasenbenny", team="Joliet Boy's Club"),
    85: bracket_utils.Placer(name="Al Skiniotes", team="New Lenox Oakview"),
    90: bracket_utils.Placer(name="Pat McMahon", team="Tinley Park Bulldogs"),
    97: bracket_utils.Placer(name="John Polz", team="Franklin Park"),
    105: bracket_utils.Placer(name="John McGrath", team="Mundelein"),
    112: bracket_utils.Placer(name="Frank Villareal", team="West Chicago"),
    118: bracket_utils.Placer(name="Jim Farina", team="Franklin Park"),
    125: bracket_utils.Placer(name="Dave Feiner", team="Naperville Lincoln"),
    134: bracket_utils.Placer(name="Chris Vodicka", team="Lisle"),
    143: bracket_utils.Placer(name="Gary Meier", team="DeKalb Huntley"),
    152: bracket_utils.Placer(name="Bruce Armstrong", team="Wheaton"),
    275: bracket_utils.Placer(name="Chuck Schmidt", team="Oak Forest"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Oak Forest": 42.0,
    "Joliet Boy's Club": 37.0,
    "West Chicago": 37.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Davis", "Granite City"): bracket_utils.Competitor(
        full_name="Davis",
        first_name="",
        last_name="Davis",
        team_full="Granite City",
    ),
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes = manual_entry.load_manual_entries(
        _HERE.parent, 1975, _NAME_EXCEPTIONS, skip_duplicate_check=True
    )

    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1975.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
