# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Carr": "Christopher Carr",
    "Christophe Durbin": "Christopher Durbin",
    "Christophe Moore": "Christopher Moore",
    "Christophe Yirsa": "Christopher Yirsa",
    "David-Jose Rice": "David-Joseph Rice",
    "Noah Manue Tapia": "Noah Manuel Tapia",
    "Pedro Anto Rangel": "Pedro Antonio Rangel",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Anthony Lopez Marquez", "Tomcat WC"): bracket_utils.Competitor(
        first_name="Anthony Lopez", last_name="Marquez", suffix=None, team="Tomcat WC"
    ),
    ("J Guido Pigoni", "SCN Youth WC"): bracket_utils.Competitor(
        first_name="J Guido", last_name="Pigoni", suffix=None, team="SCN Youth WC"
    ),
    ("Julian Espinosa Lopez", "Blackhawk WC"): bracket_utils.Competitor(
        first_name="Julian Espinosa",
        last_name="Lopez",
        suffix=None,
        team="Blackhawk WC",
    ),
    ("Noah Manuel Tapia", "Young Guns"): bracket_utils.Competitor(
        first_name="Noah Manuel", last_name="Tapia", suffix=None, team="Young Guns"
    ),
    ("Pedro Antonio Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        first_name="Pedro Antonio",
        last_name="Rangel",
        suffix=None,
        team="Storm Youth WC",
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
    root = HERE.parent / "raw-data" / "2018"
    extracted_tournament = trackwrestling.extract_year(
        root, _parse_rounds, _NAME_FIXES, _TEAM_FIXES
    )
    with open(HERE / "extracted.2018.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
