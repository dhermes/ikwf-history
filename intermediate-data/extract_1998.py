# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent

_NOVICE_WEIGHT_CLASSES = (
    62,
    66,
    70,
    74,
    79,
    84,
    89,
    95,
    101,
    108,
    115,
    122,
    130,
    147,
    166,
    215,
)
_SENIOR_WEIGHT_CLASSES = (
    70,
    74,
    79,
    84,
    89,
    95,
    101,
    108,
    115,
    122,
    130,
    138,
    147,
    156,
    166,
    177,
    189,
    275,
)


def main():
    weight_classes: list[bracket_utils.WeightClass] = []

    for weight in _NOVICE_WEIGHT_CLASSES:
        matches: list[bracket_utils.Match] = []
        if weight == 84:
            matches.append(
                bracket_utils.Match(
                    match_slot="championship_first_place",
                    top_competitor=bracket_utils.Competitor(
                        full_name="Collin McKillip",
                        first_name="Collin",
                        last_name="McKillip",
                        team_full="Tinley Park Bulldogs",
                        team_acronym=None,
                    ),
                    bottom_competitor=None,
                    result="",
                    result_type="unknown",
                    bout_number=None,
                    top_win=True,
                )
            )

        weight_classes.append(
            bracket_utils.WeightClass(division="novice", weight=weight, matches=matches)
        )

    for weight in _SENIOR_WEIGHT_CLASSES:
        weight_classes.append(
            bracket_utils.WeightClass(division="senior", weight=weight, matches=[])
        )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores={}, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1998.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
