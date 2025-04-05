# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Dranka": "Christopher Dranka",
    "Christophe Golden": "Christopher Golden",
    "Christophe Hiscock": "Christopher Hiscock",
    "Christophe Lewis": "Christopher Lewis",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Antonio Francis IV", "CHAMPAIGN KIDS WRESTLING"): bracket_utils.Competitor(
        first_name="Antonio",
        last_name="Francis",
        suffix="IV",
        team="CHAMPAIGN KIDS WRESTLING",
    ),
    ("Carl Witt Iii", "TOMCAT WC"): bracket_utils.Competitor(
        first_name="Carl", last_name="Witt", suffix="III", team="TOMCAT WC"
    ),
    ("Jacob Van Doren", "GENESEO SPIDER WC"): bracket_utils.Competitor(
        first_name="Jacob",
        last_name="Van Doren",
        suffix=None,
        team="GENESEO SPIDER WC",
    ),
    ("James Von Meding", "ST. TARCISSUS"): bracket_utils.Competitor(
        first_name="James", last_name="Von Meding", suffix=None, team="ST. TARCISSUS"
    ),
    ("Jean Louis Sawadogo", "ROCK ISLAND WC"): bracket_utils.Competitor(
        first_name="Jean Louis",
        last_name="Sawadogo",
        suffix=None,
        team="ROCK ISLAND WC",
    ),
    ("Joey Schott Jr", "CHAMPAIGN KIDS WRESTLING"): bracket_utils.Competitor(
        first_name="Joey",
        last_name="Schott",
        suffix="Jr",
        team="CHAMPAIGN KIDS WRESTLING",
    ),
    ("John Paul Stedwill", "CENTRAL ELITE REBELS"): bracket_utils.Competitor(
        first_name="John Paul",
        last_name="Stedwill",
        suffix=None,
        team="CENTRAL ELITE REBELS",
    ),
    ("Juan Blanco Iv", "MORTON LITTLE MUSTANGS"): bracket_utils.Competitor(
        first_name="Juan",
        last_name="Blanco",
        suffix="IV",
        team="MORTON LITTLE MUSTANGS",
    ),
    ("Juan Reyes Iv", "REBELS WC"): bracket_utils.Competitor(
        first_name="Juan", last_name="Reyes", suffix="IV", team="REBELS WC"
    ),
    ("Lonnie Cleveland Iii", "BULLS WC"): bracket_utils.Competitor(
        first_name="Lonnie", last_name="Cleveland", suffix="III", team="BULLS WC"
    ),
    ("Michael Johnson Jr", "DOWNERS GROVE COUGARS"): bracket_utils.Competitor(
        first_name="Michael",
        last_name="Johnson",
        suffix="Jr",
        team="DOWNERS GROVE COUGARS",
    ),
    ("Miguel Silva Jr", "MARTINEZ FOX VALLEY ELITE"): bracket_utils.Competitor(
        first_name="Miguel",
        last_name="Silva",
        suffix="Jr",
        team="MARTINEZ FOX VALLEY ELITE",
    ),
    ("Raul Marrero Jr", "SPRINGFIELD CAPITAL KIDS WC"): bracket_utils.Competitor(
        first_name="Raul",
        last_name="Marrero",
        suffix="Jr",
        team="SPRINGFIELD CAPITAL KIDS WC",
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
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Championship 1st Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_quarterfinal(
            "Championship Quarterfinals",
            "Quarterfinal",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
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
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_semi(
            "Consolation Semifinal",
            "Cons. Semi",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
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
    root = HERE.parent / "raw-data" / "2010"
    extracted_tournament = trackwrestling.extract_year(root, _parse_rounds, _NAME_FIXES)
    with open(HERE / "extracted.2010.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
