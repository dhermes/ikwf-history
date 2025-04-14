# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Kennedy": "Christopher Kennedy",
    "Christophe McCartney": "Christopher McCartney",
    "Christophe Middlebrooks": "Christopher Middlebrooks",
    "Christophe Santiago": "Christopher Santiago",
    "Christophe Whaley": "Christopher Whaley",
    "Fernando-A Irizarry-Tapia": "Fernando-Antonio Irizarry-Tapia",
    "Steven-O`N Swanson": "Steven-O`Neil Swanson",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Bryant Van Zuiden", "Riverbend WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Bryant",
        last_name="Van Zuiden",
        team="Riverbend WC",
    ),
    ("Garrett St. Clair", "Force WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Garrett",
        last_name="St. Clair",
        team="Force WC",
    ),
    ("Jared Van Vleet", "Stillman Valley WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Jared",
        last_name="Van Vleet",
        team="Stillman Valley WC",
    ),
    ("John Paul Smith", "Bison WC"): bracket_utils.Competitor(
        full_name="",
        first_name="John Paul",
        last_name="Smith",
        team="Bison WC",
    ),
    ("Lane Eric Reed", "A-J Jr. Wildcat Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Lane Eric",
        last_name="Reed",
        team="A-J Jr. Wildcat Wrestling",
    ),
    ("Lucas Van Poucke", "Force WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Lucas",
        last_name="Van Poucke",
        team="Force WC",
    ),
    ("Ronald Tucker Jr", "Bolingbrook Junior Raiders"): bracket_utils.Competitor(
        full_name="",
        first_name="Ronald",
        last_name="Tucker",
        team="Bolingbrook Junior Raiders",
    ),
}
_TEAM_FIXES: dict[str, tuple[str, str]] = {}


def _parse_rounds(
    selenium_rounds: Any,
    match_slots_by_bracket: trackwrestling.MatchSlotsByBracket,
) -> list[trackwrestling.MatchWithBracket]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    matches: list[trackwrestling.MatchWithBracket] = []

    matches.extend(
        trackwrestling.parse_r32(
            "Championship Preliminary",
            "Champ. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v1",
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Championship 1st Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v1",
        )
    )

    matches.extend(
        trackwrestling.parse_quarterfinal(
            "Championship Quarterfinals",
            "Quarterfinal",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v1",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round3(
            "Consolation Preliminary",
            "Cons. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round4(
            "Consolation 1st Round",
            "Cons. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_semi_mixed(
            "Champ Semi`s & Con Quarterfinal",
            "Semifinal",
            "Cons. Round 3",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v1",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_semi(
            "Consolation Semifinal",
            "Cons. Semi",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v1",
        )
    )

    matches.extend(
        trackwrestling.parse_place_matches_v2(
            "Place Bouts",
            "3rd Place Match",
            "5th Place Match",
            "7th Place Match",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_championship_matches(
            "Championship Bouts",
            "1st Place Match",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    if selenium_rounds:
        raise ValueError("Round not processed", selenium_rounds.keys())

    return matches


def main():
    root = HERE.parent / "raw-data" / "2013"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship Preliminary",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2013.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
