# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Brendan Ty Hall": "Brendan Tyler Hall",
    "Christophe Bartels": "Christopher Bartels",
    "Christophe Bernal": "Christopher Bernal",
    "Christophe Carton": "Christopher Carton",
    "Christophe Wright": "Christopher Wright",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Aaron Brewton Jr", "WAUKEGAN YOUTH WC"): bracket_utils.Competitor(
        first_name="Aaron",
        last_name="Brewton",
        suffix="Jr",
        team="WAUKEGAN YOUTH WC",
    ),
    ("Alvin Foster III", "HARVEY PARK DIST TWISTERS"): bracket_utils.Competitor(
        first_name="Alvin",
        last_name="Foster",
        suffix="III",
        team="HARVEY PARK DIST TWISTERS",
    ),
    ("Anthony Ferraris Jr", "MAINE EAGLES THE ELITE WC"): bracket_utils.Competitor(
        first_name="Anthony",
        last_name="Ferraris",
        suffix="Jr",
        team="MAINE EAGLES THE ELITE WC",
    ),
    ("Archie Williams Jr", "CHAMPAIGN KIDS WRESTLING"): bracket_utils.Competitor(
        first_name="Archie",
        last_name="Williams",
        suffix="Jr",
        team="CHAMPAIGN KIDS WRESTLING",
    ),
    ("Brendan Tyler Hall", "HARVEY PARK DIST TWISTERS"): bracket_utils.Competitor(
        first_name="Brendan Tyler",
        last_name="Hall",
        suffix=None,
        team="HARVEY PARK DIST TWISTERS",
    ),
    ("Greg Jacquez III", "BLACKHAWK WC"): bracket_utils.Competitor(
        first_name="Greg", last_name="Jacquez", suffix="III", team="BLACKHAWK WC"
    ),
    ("John Paul Stedwill", "CHILLI DAWGS WC"): bracket_utils.Competitor(
        first_name="John Paul",
        last_name="Stedwill",
        suffix=None,
        team="CHILLI DAWGS WC",
    ),
    ("Ken Raap Jr", "PALATINE PANTHERS WC"): bracket_utils.Competitor(
        first_name="Ken", last_name="Raap", suffix="Jr", team="PALATINE PANTHERS WC"
    ),
    ("Lonnie Cleveland III", "GC JR WARRIORS"): bracket_utils.Competitor(
        first_name="Lonnie",
        last_name="Cleveland",
        suffix="III",
        team="GC JR WARRIORS",
    ),
    ("Michael Johnson Jr", "ROMEOVILLE YOUTH WC"): bracket_utils.Competitor(
        first_name="Michael",
        last_name="Johnson",
        suffix="Jr",
        team="ROMEOVILLE YOUTH WC",
    ),
    ("Miguel Silva Jr", "MARTINEZ FOX VALLEY ELITE"): bracket_utils.Competitor(
        first_name="Miguel",
        last_name="Silva",
        suffix="Jr",
        team="MARTINEZ FOX VALLEY ELITE",
    ),
    ("Terry Calkins Jr.", "MAINE EAGLES THE ELITE WC"): bracket_utils.Competitor(
        first_name="Terry",
        last_name="Calkins",
        suffix="Jr",
        team="MAINE EAGLES THE ELITE WC",
    ),
    ("Travis Flute Jr", "A-J JUNIOR WILDCATS"): bracket_utils.Competitor(
        first_name="Travis",
        last_name="Flute",
        suffix="Jr",
        team="A-J JUNIOR WILDCATS",
    ),
    ("Wardell Rosemon Jr.", "DUNDEE HIGHLANDERS"): bracket_utils.Competitor(
        first_name="Wardell",
        last_name="Rosemon",
        suffix="Jr",
        team="DUNDEE HIGHLANDERS",
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
            "Champ Semis & Con Quarterfinal",
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
    root = HERE.parent / "raw-data" / "2008"
    extracted_tournament = trackwrestling.extract_year(root, _parse_rounds, _NAME_FIXES)
    with open(HERE / "extracted.2008.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
