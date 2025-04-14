# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Thompson": "Christopher Thompson",
    "Christophe Velasquez": "Christopher Velasquez",
    "Mia Izabel Nevarez": "Mia Izabella Nevarez",
    "Myles-Aver Holland": "Myles-Avery Holland",
    "Octavian Giampaoli-Marti": "Octavian Giampaoli-Martinez",
    "Pedro Albe Rangel": "Pedro Alberto Rangel",
    "Ruby Bolanos-Carbaja": "Ruby Bolanos-Carbajal",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Aaron Griffin Jr", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Aaron",
        last_name="Griffin",
        team_full="Harvey Twisters WC",
        team_acronym="HT",
    ),
    ("Antonio Reyes Ii", "Beat the Streets Chicago-Avondale"): bracket_utils.Competitor(
        full_name="",
        first_name="Antonio",
        last_name="Reyes",
        team_full="Beat the Streets Chicago-Avondale",
        team_acronym="BTSA",
    ),
    ("Blake Vande Loo", "Batavia WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Blake",
        last_name="Vande Loo",
        team_full="Batavia WC",
        team_acronym="BAT",
    ),
    ("Caden St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Caden",
        last_name="St Angelo",
        team_full="PSF Wrestling Academy",
        team_acronym="PSF",
    ),
    (
        "Carl Cody Weidner",
        "Combative Sports Athletic Center Wrestling",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Carl Cody",
        last_name="Weidner",
        team_full="Combative Sports Athletic Center Wrestling",
        team_acronym="CSAC",
    ),
    (
        "Cecilia Van Oppen",
        "East Peoria River Bandits Wrestling",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Cecilia",
        last_name="Van Oppen",
        team_full="East Peoria River Bandits Wrestling",
        team_acronym="EPRB",
    ),
    ("Dalton St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Dalton",
        last_name="St Angelo",
        team_full="PSF Wrestling Academy",
        team_acronym="PSF",
    ),
    ("David Pointer Jr", "East St. Louis WC"): bracket_utils.Competitor(
        full_name="",
        first_name="David",
        last_name="Pointer",
        team_full="East St. Louis WC",
        team_acronym="ESL",
    ),
    ("Eddie Woody Jr.", "Edwardsville WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Eddie",
        last_name="Woody",
        team_full="Edwardsville WC",
        team_acronym="EDW",
    ),
    ("Glenn Harston Iii", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Glenn",
        last_name="Harston",
        team_full="Harvey Twisters WC",
        team_acronym="HT",
    ),
    ("Lesly De La Cruz", "Blue Crew WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Lesly",
        last_name="De La Cruz",
        team_full="Blue Crew WC",
        team_acronym="BLUE",
    ),
    ("Mia Izabella Nevarez", "West Suburban Girls WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Mia Izabella",
        last_name="Nevarez",
        team_full="West Suburban Girls WC",
        team_acronym="WSGW",
    ),
    ("Pedro Alberto Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Alberto",
        last_name="Rangel",
        team_full="Storm Youth WC",
        team_acronym="SYWC",
    ),
    ("Robert Wiggins Jr", "East St. Louis WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Robert",
        last_name="Wiggins",
        team_full="East St. Louis WC",
        team_acronym="ESL",
    ),
    ("Rogelio Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Rogelio",
        last_name="Del Muro",
        team_full="nWo WC",
        team_acronym="NWO",
    ),
    ("Travis Hinton Jr", "Toss Em Up Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Travis",
        last_name="Hinton",
        team_full="Toss Em Up Wrestling Academy",
        team_acronym="TOSS",
    ),
}
_TEAM_FIXES: dict[str, tuple[str, str]] = {
    "Antonio Reyes Ii": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Eila Barbour": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Jordan Hooks": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Jack Wahtola": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Paige Finnegan": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Harrison Yankellow": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Lucis Rios": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Damarion Johnson": ("Beat the Street", "Beat the Streets Chicago-Hyde Park"),
    "Andrew Ayala-Mendoza": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Andrew Lehman": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Andrew Tucker": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Axel Rodriguez": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Carola Garduno": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Demetria Griffin": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Jeremy Sikorski": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Joseph Franklin": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Lila Vazquez": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Mia Vargas": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Obadiah Willis": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Belen Vargas": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Charlotte Nold": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Diego Navarro": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Frank Valle": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Jade Zambrano": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Luke Sanchez": ("Beat the Street", "Beat the Streets Chicago-Tri Taylor"),
    "Nino Capuano": ("Beat the Street", "Beat the Streets Chicago-Tri Taylor"),
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
            "Championship First Round",
            "Champ. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Championship Second Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round2(
            "Consolation Second Round",
            "Cons. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_quarterfinal_mixed(
            "Champ Quarters & Consolation 3rd Round",
            "Quarterfinal",
            "Cons. Round 3",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round4(
            "Consolation 4th Round",
            "Cons. Round 4",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_semi_mixed(
            "Champ Semis & Consolation 5th Round",
            "Semifinal",
            "Cons. Round 5",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_semi(
            "Consolation Semifinal",
            "Cons. Semi",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_place_matches_v2(
            "3rd, 5th, & 7th Place Bouts",
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
    root = HERE.parent / "raw-data" / "2024"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship First Round",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2024.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
