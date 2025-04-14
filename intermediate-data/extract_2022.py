# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Easley": "Christopher Easley",
    "Christophe Korduplewski": "Christopher Korduplewski",
    "Christophe Talbert": "Christopher Talbert",
    "Jose Octav Velazquez": "Jose Octavio Velazquez",
    "Pedro Albe Rangel": "Pedro Alberto Rangel",
    "Trae Jacks Griffiths": "Trae Jackson Griffiths",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Blake Vande Loo", "Batavia WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Blake",
        last_name="Vande Loo",
        team_acronym="Batavia WC",
    ),
    ("Carl Cody Weidner", "Highland Bulldog Jr. WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Carl Cody",
        last_name="Weidner",
        team_acronym="Highland Bulldog Jr. WC",
    ),
    ("Gabriel Del Toro", "TJ Trained Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Gabriel",
        last_name="Del Toro",
        team_acronym="TJ Trained Wrestling",
    ),
    ("James Talley Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        full_name="",
        first_name="James",
        last_name="Talley",
        team_acronym="Lincoln-Way WC",
    ),
    ("Jesus Reyes Jr.", "Dundee Highlanders WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Jesus",
        last_name="Reyes",
        team_acronym="Dundee Highlanders WC",
    ),
    ("Jose Octavio Velazquez", "Scorpion WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Jose Octavio",
        last_name="Velazquez",
        team_acronym="Scorpion WC",
    ),
    ("Orlando Hoye Iii", "Glenbard East Jr Rams WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Orlando",
        last_name="Hoye",
        team_acronym="Glenbard East Jr Rams WC",
    ),
    ("Pedro Alberto Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Alberto",
        last_name="Rangel",
        team_acronym="Storm Youth WC",
    ),
    ("Trae Jackson Griffiths", "Champaign WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Trae Jackson",
        last_name="Griffiths",
        team_acronym="Champaign WC",
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
            "v2",
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Championship 1st Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v2",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round2(
            "1st WB",
            "Cons. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_quarterfinal_mixed(
            "Quarters & 2nd WB",
            "Quarterfinal",
            "Cons. Round 3",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v2",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round4(
            "3rd WB",
            "Cons. Round 4",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_semi_mixed(
            "Semis & 4th WB",
            "Semifinal",
            "Cons. Round 5",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v2",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_semi(
            "Consolation Semifinal",
            "Cons. Semi",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v2",
        )
    )

    matches.extend(
        trackwrestling.parse_place_matches_v2(
            "3rd, 5th, & 7th",
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
    root = HERE.parent / "raw-data" / "2022"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship Preliminary",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2022.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
