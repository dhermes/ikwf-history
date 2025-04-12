# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Bates": "Christopher Bates",
    "Christophe Durbin": "Christopher Durbin",
    "Christophe Moore": "Christopher Moore",
    "Christophe Yirsa": "Christopher Yirsa",
    "Hayden Dav Volz": "Hayden David Volz",
    "Noah Manue Tapia": "Noah Manuel Tapia",
    "Pedro Anto Rangel": "Pedro Antonio Rangel",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("David Burchett Jr.", "Mustang WC"): bracket_utils.Competitor(
        first_name="David", last_name="Burchett", suffix="Jr", team="Mustang WC"
    ),
    ("Eyson Van Eycke", "Mt. Vernon Lions WC"): bracket_utils.Competitor(
        first_name="Eyson",
        last_name="Van Eycke",
        suffix=None,
        team="Mt. Vernon Lions WC",
    ),
    ("Hayden David Volz", "Edwardsville WC"): bracket_utils.Competitor(
        first_name="Hayden David",
        last_name="Volz",
        suffix=None,
        team="Edwardsville WC",
    ),
    ("Hiran Lopez Marquez", "Tomcat WC"): bracket_utils.Competitor(
        first_name="Hiran Lopez", last_name="Marquez", suffix=None, team="Tomcat WC"
    ),
    ("Jose Del Toro", "TJ Trained Wrestling"): bracket_utils.Competitor(
        first_name="Jose",
        last_name="Del Toro",
        suffix=None,
        team="TJ Trained Wrestling",
    ),
    ("Jujuan Williams Jr", "Lionheart Intense Wrestling"): bracket_utils.Competitor(
        first_name="Jujuan",
        last_name="Williams",
        suffix="Jr",
        team="Lionheart Intense Wrestling",
    ),
    ("Justin Cobbs Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        first_name="Justin", last_name="Cobbs", suffix="Jr", team="Lincoln-Way WC"
    ),
    ("Lee Smith Jr.", "DAWC"): bracket_utils.Competitor(
        first_name="Lee", last_name="Smith", suffix="Jr", team="DAWC"
    ),
    ("Noah Manuel Tapia", "Moline WC"): bracket_utils.Competitor(
        first_name="Noah Manuel", last_name="Tapia", suffix=None, team="Moline WC"
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
    root = HERE.parent / "raw-data" / "2019"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship Preliminary",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2019.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
