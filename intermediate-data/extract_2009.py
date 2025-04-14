# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Bartels": "Christopher Bartels",
    "Christophe Dranka": "Christopher Dranka",
    "Christophe Golden": "Christopher Golden",
    "Christophe Hiscock": "Christopher Hiscock",
    "Christophe Malone": "Christopher Malone",
    "Michael Mcnulty-ferguso": "Michael Mcnulty-ferguson",
    "Robert Vodicka-hirschm": "Robert Vodicka-hirschmann",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Carl Witt, Iii", "TOMCAT WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Carl",
        last_name="Witt",
        team="TOMCAT WC",
    ),
    (
        "Floyd Lomelino Iv",
        "JACKSONVILLE AREA YOUTH WRESTLING",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Floyd",
        last_name="Lomelino",
        team="JACKSONVILLE AREA YOUTH WRESTLING",
    ),
    ("James Zeigler Jr.", "EDWARDSVILLE WC"): bracket_utils.Competitor(
        full_name="",
        first_name="James",
        last_name="Zeigler",
        team="EDWARDSVILLE WC",
    ),
    ("Larry Thomas Jr", "IRON MAN"): bracket_utils.Competitor(
        full_name="",
        first_name="Larry",
        last_name="Thomas",
        team="IRON MAN",
    ),
    ("Lonnie Cleveland Iii", "UNITED SOUTHERN ALLSTARS"): bracket_utils.Competitor(
        full_name="",
        first_name="Lonnie",
        last_name="Cleveland",
        team="UNITED SOUTHERN ALLSTARS",
    ),
    ("Michael Johnson Jr", "DOWNERS GROVE COUGARS"): bracket_utils.Competitor(
        full_name="",
        first_name="Michael",
        last_name="Johnson",
        team="DOWNERS GROVE COUGARS",
    ),
    ("Miguel Silva Jr", "MARTINEZ FOX VALLEY ELITE"): bracket_utils.Competitor(
        full_name="",
        first_name="Miguel",
        last_name="Silva",
        team="MARTINEZ FOX VALLEY ELITE",
    ),
    ("Ronald Shafer Iii", "GRANITE CITY WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Ronald",
        last_name="Shafer",
        team="GRANITE CITY WC",
    ),
    ("Shavez Hawkins Jr", "CROSSTOWN WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Shavez",
        last_name="Hawkins",
        team="CROSSTOWN WC",
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
    root = HERE.parent / "raw-data" / "2009"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship Preliminary",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2009.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
