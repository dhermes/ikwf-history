# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Colvin": "Christopher Colvin",
    "Christophe Dranka": "Christopher Dranka",
    "Christophe Harrison": "Christopher Harrison",
    "Christophe Kennedy": "Christopher Kennedy",
    "Christophe Mccartney": "Christopher Mccartney",
    "Christophe Tucker": "Christopher Tucker",
    "Christophe Whaley": "Christopher Whaley",
    "Juan Isaia Tapia": "Juan Isaiah Tapia",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("J. Antonio Vargas", "Arlington Cardinals"): bracket_utils.Competitor(
        full_name="",
        first_name="J. Antonio",
        last_name="Vargas",
        team="Arlington Cardinals",
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
    ("John Paul Stedwill", "Central Elite Rebels"): bracket_utils.Competitor(
        full_name="",
        first_name="John Paul",
        last_name="Stedwill",
        team="Central Elite Rebels",
    ),
    ("Juan Isaiah Tapia", "Champbuilders Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Juan Isaiah",
        last_name="Tapia",
        team="Champbuilders Wrestling",
    ),
    ("Lucas Van Poucke", "Naperville WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Lucas",
        last_name="Van Poucke",
        team="Naperville WC",
    ),
    ("Nathan Van Hoorn", "Wolves Wrestling Club Inc."): bracket_utils.Competitor(
        full_name="",
        first_name="Nathan",
        last_name="Van Hoorn",
        team="Wolves Wrestling Club Inc.",
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
    root = HERE.parent / "raw-data" / "2012"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship Preliminary",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2012.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
