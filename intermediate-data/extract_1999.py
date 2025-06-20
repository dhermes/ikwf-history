# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import manual_entry

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_SCORES: dict[str, float] = {}
_SENIOR_TEAM_SCORES: dict[str, float] = {}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    (
        "ANTHONY (A.J.) CICCARELLI",
        "ROXANA KIDS WRESTLING CLUB",
    ): bracket_utils.Competitor(
        full_name="ANTHONY (A.J.) CICCARELLI",
        first_name="AJ",
        last_name="CICCARELLI",
        team_full="ROXANA KIDS WRESTLING CLUB",
        team_acronym=None,
    ),
    (
        "PATRICK GADIENT YOUNG",
        "ERIE MIDDLE SCHOOL WRESTLING CLUB",
    ): bracket_utils.Competitor(
        full_name="PATRICK GADIENT YOUNG",
        first_name="PATRICK",
        last_name="YOUNG",
        team_full="ERIE MIDDLE SCHOOL WRESTLING CLUB",
        team_acronym=None,
    ),
    ("RYAN JAMES GLENN", "ELGIN LARKIN JR. ROYALS"): bracket_utils.Competitor(
        full_name="RYAN JAMES GLENN",
        first_name="RYAN",
        last_name="GLENN",
        team_full="ELGIN LARKIN JR. ROYALS",
        team_acronym=None,
    ),
    ("RYAN ST. JOSEPH", "CRYSTAL LAKE WIZARDS"): bracket_utils.Competitor(
        full_name="RYAN ST. JOSEPH",
        first_name="RYAN",
        last_name="ST. JOSEPH",
        team_full="CRYSTAL LAKE WIZARDS",
        team_acronym=None,
    ),
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["novice"] = []
    for team_name, score in _NOVICE_TEAM_SCORES.items():
        team_scores["novice"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    weight_classes = manual_entry.load_manual_entries(
        HERE.parent, 1999, _NAME_EXCEPTIONS
    )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1999.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
