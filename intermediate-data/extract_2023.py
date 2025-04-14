# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Abdulrahma Abukhdeir": "Abdulrahman Abukhdeir",
    "Christophe Easley": "Christopher Easley",
    "Christophe Fernandez": "Christopher Fernandez",
    "Christophe Korduplewski": "Christopher Korduplewski",
    "Christophe Navarro": "Christopher Navarro",
    "Pedro Albe Rangel": "Pedro Alberto Rangel",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Aaron Griffin Jr", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Aaron",
        last_name="Griffin",
        team_acronym="Harvey Twisters WC",
    ),
    (
        "Arkail Griffin Edwards",
        "Beat the Streets Chicago-Midway",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Arkail",
        last_name="Griffin Edwards",
        team_acronym="Beat the Streets Chicago-Midway",
    ),
    ("Blake Vande Loo", "Batavia WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Blake",
        last_name="Vande Loo",
        team_acronym="Batavia WC",
    ),
    (
        "Carl Cody Weidner",
        "Combative Sports Athletic Center Wrestling",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Carl Cody",
        last_name="Weidner",
        team_acronym="Combative Sports Athletic Center Wrestling",
    ),
    ("Eddie Woody Jr.", "Edwardsville WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Eddie",
        last_name="Woody",
        team_acronym="Edwardsville WC",
    ),
    ("Gabriel Travis Jr", "Will County Warriors WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Gabriel",
        last_name="Travis",
        team_acronym="Will County Warriors WC",
    ),
    ("Jeremy Powell Jr", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Jeremy",
        last_name="Powell",
        team_acronym="Harvey Twisters WC",
    ),
    ("Logan Van Vlymen", "Macomb Little Bombers Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Logan",
        last_name="Van Vlymen",
        team_acronym="Macomb Little Bombers Wrestling",
    ),
    ("Pedro Alberto Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Alberto",
        last_name="Rangel",
        team_acronym="Storm Youth WC",
    ),
    ("Saul Pulido III", "Izzy Style Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Saul",
        last_name="Pulido",
        team_acronym="Izzy Style Wrestling",
    ),
    ("Travis Hinton Jr", "Toss Em Up Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Travis",
        last_name="Hinton",
        team_acronym="Toss Em Up Wrestling Academy",
    ),
    ("Travis Kinkead Jr.", "Blue Line Training Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Travis",
        last_name="Kinkead",
        team_acronym="Blue Line Training Academy",
    ),
}
_TEAM_FIXES: dict[str, tuple[str, str]] = {
    "Aedan Dillow": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Antonio Reyes": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Harrison Yankellow": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Hunter Wahtola": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Allante Jackson": ("Beat the Street", "Beat the Streets Chicago-Bellwood"),
    "Anthony Brown": ("Beat the Street", "Beat the Streets Chicago-Bellwood"),
    "Cardevion Gordon": ("Beat the Street", "Beat the Streets Chicago-Bellwood"),
    "Isaiah Robinson": ("Beat the Street", "Beat the Streets Chicago-Bellwood"),
    "Jamiel Castleberry": ("Beat the Street", "Beat the Streets Chicago-Bellwood"),
    "Nino Capuano": ("Beat the Street", "Beat the Streets Chicago-Hyde Park"),
    "Andrew Ayala-Mendoza": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Andrew Lehman": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Arkail Griffin Edwards": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Axel Rodriguez": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Josiah Willis": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Kenneth Seggerson": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Malakai Davis": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Obadiah Willis": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Sergio Calleros": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Charlotte Nold": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Harrison Sneathen": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Zachary Michaud": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
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
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Championship 1st Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round2(
            "Consolation First Round",
            "Cons. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_quarterfinal_mixed(
            "Champ Quarters & Consolation 2nd Round",
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
            "Consolation 3rd Round",
            "Cons. Round 4",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
        )
    )

    matches.extend(
        trackwrestling.parse_semi_mixed(
            "Champ Semis & Consolation 4th Round",
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
    root = HERE.parent / "raw-data" / "2023"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship Preliminary",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2023.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
