# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import manual_entry

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY PARK TWISTERS": 184.0,
    "VILLA-LOMBARD COUGARS": 137.0,
    "BETHALTO / JR. HIGH": 125.0,
    "TRAILBLAZER WC": 124.0,
    "TINLEY PARK BULLDOGS": 112.0,
    "ADDAMS JH WC": 103.5,
    "MUSTANG WC": 71.0,
    "MORTON YOUTH WC": 67.5,
    "ST. CHARLES WC DISTRICT 303": 67.0,
    "ROUND LAKE SPARTAN WC": 66.5,
    "ROSEMONT COBRAS": 65.0,
    "ARLINGTON CARDINALS WC": 64.5,
    "DOLTON PARK FALCONS": 64.5,
    "GRANITE CITY WC COOLIDGE": 64.0,
    "HARLEM SCHOOL DISTRICT 122 WC": 61.0,
    "CRYSTAL LAKE WIZARDS": 59.0,
    "PIRATES": 49.0,
    "MEAD JH WC": 47.5,
    "VITTUM CATS": 47.5,
    "ORLAND PARK PIONEERS": 44.5,
    "WARHAWK WC": 43.5,
    "ANTIOCH UPPER GRADE": 42.0,
    "HICKORY HILLS PD": 42.0,
    "ST. BARNABAS / CHRIST THE KING": 40.0,
    "ROCKFORD WC": 39.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("DALE SIMPSON JR", "WHEATON-WARRENVILLE"): bracket_utils.Competitor(
        full_name="DALE SIMPSON JR",
        first_name="DALE",
        last_name="SIMPSON",
        team_full="WHEATON-WARRENVILLE",
    ),
    ("ROBERT DELA FUENTE", "LOCKPORT GRAPPLERS WC"): bracket_utils.Competitor(
        full_name="ROBERT DELA FUENTE",
        first_name="ROBERT",
        last_name="DELA FUENTE",
        team_full="LOCKPORT GRAPPLERS WC",
    ),
    ("STANLEY EVANS JR", "PIRATES"): bracket_utils.Competitor(
        full_name="STANLEY EVANS JR",
        first_name="STANLEY",
        last_name="EVANS",
        team_full="PIRATES",
    ),
    ("MICHAEL O GRADNEY", "LOCKPORT GRAPPLERS WC"): bracket_utils.Competitor(
        full_name="MICHAEL O GRADNEY",
        first_name="MICHAEL",
        last_name="GRADNEY",
        team_full="LOCKPORT GRAPPLERS WC",
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
        _HERE.parent, 1992, _NAME_EXCEPTIONS
    )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1992.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
