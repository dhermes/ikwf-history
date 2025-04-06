# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TEAM_NAME_MAPPING: dict[str, int] = {}


def _collect_all_names(weight_classes: list[bracket_utils.WeightClass]) -> list[str]:
    teams: set[str] = set()
    for weight_class in weight_classes:
        for match in weight_class.matches:
            if match.top_competitor is not None:
                teams.add(match.top_competitor.team)

            if match.bottom_competitor is not None:
                teams.add(match.bottom_competitor.team)

    return sorted(teams)


def main():
    base_index = 40000
    with open(HERE / "extracted.2020.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    weight_classes = extracted.weight_classes
    for i, name in enumerate(_collect_all_names(weight_classes)):
        if "'" in name:
            raise NotImplementedError(name)
        # ALSO: print(f"{base_index + i}: {name!r},")
        print(f"  ({name!r}, {base_index + i}),")


if __name__ == "__main__":
    main()
