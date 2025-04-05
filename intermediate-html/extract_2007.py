# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib
from typing import Any

import bs4

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Aaron Brewton III": "Aaron Brewton II",
    "Brendan Ty Hall": "Brendan Tyler Hall",
    "Christophe Bartels": "Christopher Bartels",
    "Christophe Carton": "Christopher Carton",
    "Christophe Lopez": "Christopher Lopez",
    "Christophe Wright": "Christopher Wright",
    "Malik - Ja Taylor": "Malik - Jabri Taylor",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Tyrone Sally Jr.", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Tyrone",
        last_name="Sally",
        suffix="Jr",
        team="Harvey Park Dist Twisters",
    ),
    ("Wardell Rosemon Jr.", "Dundee Highlanders"): bracket_utils.Competitor(
        first_name="Wardell",
        last_name="Rosemon",
        suffix="Jr",
        team="Dundee Highlanders",
    ),
    ("Archie Williams Jr.", "Champaign Kids Wrestling"): bracket_utils.Competitor(
        first_name="Archie",
        last_name="Williams",
        suffix="Jr",
        team="Champaign Kids Wrestling",
    ),
    ("Anthony Ferraris Jr", "Maine Eagles WC"): bracket_utils.Competitor(
        first_name="Anthony", last_name="Ferraris", suffix="Jr", team="Maine Eagles WC"
    ),
    ("Lusiano Cantu Jr.", "Gomez Wrestling Academy"): bracket_utils.Competitor(
        first_name="Lusiano",
        last_name="Cantu",
        suffix="Jr",
        team="Gomez Wrestling Academy",
    ),
    ("Antwyone Brown Jr.", "Crosstown WC"): bracket_utils.Competitor(
        first_name="Antwyone", last_name="Brown", suffix="Jr", team="Crosstown WC"
    ),
    ("Brendan Tyler Hall", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Brendan Tyler",
        last_name="Hall",
        suffix=None,
        team="Harvey Park Dist Twisters",
    ),
    ("Lonne Cleveland III", "GC Jr Warriors"): bracket_utils.Competitor(
        first_name="Lonne",
        last_name="Cleveland",
        suffix="III",
        team="GC Jr Warriors",
    ),
    ("Aaron Brewton II", "Waukegan Youth WC"): bracket_utils.Competitor(
        first_name="Aaron", last_name="Brewton", suffix="II", team="Waukegan Youth WC"
    ),
    ("Malik - Jabri Taylor", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Malik - Jabri",
        last_name="Taylor",
        suffix=None,
        team="Harvey Park Dist Twisters",
    ),
    ("Michael Aldrich Jr", "Peoria Razorbacks Youth WC"): bracket_utils.Competitor(
        first_name="Michael",
        last_name="Aldrich",
        suffix="Jr",
        team="Peoria Razorbacks Youth WC",
    ),
    ("Ross Ferraro III", "Gomez Wrestling Academy"): bracket_utils.Competitor(
        first_name="Ross",
        last_name="Ferraro",
        suffix="III",
        team="Gomez Wrestling Academy",
    ),
    ("Alvin Foster III", "Harvey Park Dist Twisters"): bracket_utils.Competitor(
        first_name="Alvin",
        last_name="Foster",
        suffix="III",
        team="Harvey Park Dist Twisters",
    ),
}


def _parse_rounds(
    selenium_rounds: Any,
    match_slots_by_bracket: trackwrestling.MatchSlotsByBracket,
) -> list[trackwrestling.MatchWithBracket]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    matches: list[trackwrestling.MatchWithBracket] = []

    matches.extend(
        trackwrestling.parse_r32(
            "Champ Round 1 (32 Man)",
            "Champ. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Champ Round 2 (32 Man)",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_quarterfinal(
            "Quarters (32 Man)",
            "Quarterfinal",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round3(
            "1st Wrestleback (32 Man)",
            "Cons. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round4(
            "2nd Wrestleback (32 Man)",
            "Cons. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_semi_mixed(
            "Semis & WB (32 Man)",
            "Semifinal",
            "Cons. Round 3",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_semi(
            "Cons. Semis (32 Man)",
            "Cons. Semi",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_place_matches_v1(
            "Placement Matches (32 Man)",
            "1st Place Match",
            "3rd Place Match",
            "5th Place Match",
            "7th Place Match",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    if selenium_rounds:
        raise ValueError("Round not processed", selenium_rounds.keys())

    return matches


def main():
    root = HERE.parent / "raw-data" / "2007"
    extracted_tournament = trackwrestling.extract_year(root, _parse_rounds, _NAME_FIXES)
    with open(HERE / "extracted.2007.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
