# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import argparse
import pathlib

import bracket_utils

_HERE = pathlib.Path(__file__).resolve().parent


def _get_args() -> tuple[str, str]:
    parser = argparse.ArgumentParser(prog="combine-duplicates")
    parser.add_argument(
        "--source-name-normalized",
        dest="source_name_normalized",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--target-name-normalized",
        dest="target_name_normalized",
        required=True,
        type=str,
    )
    parsed = parser.parse_args()
    return parsed.source_name_normalized, parsed.target_name_normalized


def main() -> None:
    source_name_normalized, target_name_normalized = _get_args()

    with open(_HERE / "_team-name-duplicates.json") as file_obj:
        as_json = file_obj.read()

    team_duplicates = bracket_utils.TeamDuplicates.model_validate_json(as_json)
    verified_teams = team_duplicates.root

    by_name_normalized: dict[str, bracket_utils.VerifiedTeam] = {}
    for verified_team in verified_teams:
        if verified_team.name_normalized in by_name_normalized:
            raise RuntimeError("Invariant violation")

        by_name_normalized[verified_team.name_normalized] = verified_team

    source_match = by_name_normalized.pop(source_name_normalized, None)
    target_match = by_name_normalized.get(target_name_normalized)

    if source_match is None:
        raise RuntimeError("Normalized name not found", source_name_normalized)

    if source_match.url_path_slug is not None:
        raise RuntimeError("Cannot merge from a source that already has a URL slug")

    if target_match is None:
        raise RuntimeError("Normalized name not found", target_name_normalized)

    target_match.duplicates.extend(source_match.duplicates)

    updated_team_duplicates = bracket_utils.TeamDuplicates(
        root=by_name_normalized.values()
    )
    updated_team_duplicates.sort()

    as_json = updated_team_duplicates.model_dump_json(indent=2)
    with open(_HERE / "_team-name-duplicates.json", "w") as file_obj:
        file_obj.write(as_json)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
