# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Darian Martinez-Willia": "Darian Martinez-Williams",
    "Hilal Nafi Saleem": "Hilal Nafisa Saleem",
    "Justin-Car Jones": "Justin-Carter Jones",
    "Pedro Lege Rangel": "Pedro Legend Rangel",
    "Trinity Gr Larsen": "Trinity Grace Larsen",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Aydan Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Aydan",
        last_name="Del Muro",
        team_full="nWo WC",
        team_acronym=None,  # TODO
    ),
    ("Brent Hills Ii", "Champions WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Brent",
        last_name="Hills",
        team_full="Champions WC",
        team_acronym=None,  # TODO
    ),
    ("Cleotha Spearman Lll", "East St. Louis WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Cleotha",
        last_name="Spearman",
        team_full="East St. Louis WC",
        team_acronym=None,  # TODO
    ),
    ("Dai Zaria Christopher", "Astro WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Dai Zaria",
        last_name="Christopher",
        team_full="Astro WC",
        team_acronym=None,  # TODO
    ),
    ("Daquain Hubbard Jr", "Urbana Tigers WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Daquain",
        last_name="Hubbard",
        team_full="Urbana Tigers WC",
        team_acronym=None,  # TODO
    ),
    ("Elina Del Rio", "Caravan Kids WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Elina",
        last_name="Del Rio",
        team_full="Caravan Kids WC",
        team_acronym=None,  # TODO
    ),
    ("Genevieve Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Genevieve",
        last_name="Del Muro",
        team_full="nWo WC",
        team_acronym=None,  # TODO
    ),
    ("Henry Brown Iii", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Henry",
        last_name="Brown",
        team_full="Harvey Twisters WC",
        team_acronym=None,  # TODO
    ),
    ("Hilal Nafisa Saleem", "Caravan Kids WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Hilal Nafisa",
        last_name="Saleem",
        team_full="Caravan Kids WC",
        team_acronym=None,  # TODO
    ),
    ("Jerome Rogers Iii", "O`Fallon Little Panthers WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Jerome",
        last_name="Rogers",
        team_full="O`Fallon Little Panthers WC",
        team_acronym=None,  # TODO
    ),
    ("Nolan St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Nolan",
        last_name="St Angelo",
        team_full="PSF Wrestling Academy",
        team_acronym=None,  # TODO
    ),
    ("Pedro Legend Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Legend",
        last_name="Rangel",
        team_full="Storm Youth WC",
        team_acronym=None,  # TODO
    ),
    ("Ricky Olszta Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Ricky",
        last_name="Olszta",
        team_full="Lincoln-Way WC",
        team_acronym=None,  # TODO
    ),
    ("Trinity Grace Larsen", "Fox Lake WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Trinity Grace",
        last_name="Larsen",
        team_full="Fox Lake WC",
        team_acronym=None,  # TODO
    ),
}
_TEAM_FIXES: dict[str, tuple[str, str]] = {
    "Jack Wachstetter": ("Backyard Brawle", "Backyard Brawlers Midwest"),
    "Kasen Cargo": ("Backyard Brawle", "Backyard Brawlers Midwest"),
    "Colton Zabinski": ("Backyard Brawle", "Backyard Brawlers North Wrestling"),
    "Drake Melton": ("Backyard Brawle", "Backyard Brawlers West Wrestling"),
    "Jordan Qualkinbush": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Kaydin Feliciano": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Noah Reyes": ("Beat the Street", "Beat the Streets Chicago-Avondale"),
    "Caiden Lehman": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Camila Rodriguez": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Eliana Ortega": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Julian Orozco": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Mason Vargas": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Temuulen Binderiya": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "William Dunn": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Zoey Rousseau": ("Beat the Street", "Beat the Streets Chicago-Midway"),
    "Alexa Nunn": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Antoine Yates": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Michael Burns": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
    "Victor Vargas": ("Beat the Street", "Beat the Streets Chicago-Oak Park"),
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
            "Championship 1st Round",
            "Champ. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_r16(
            "Championship 2nd Round",
            "Champ. Round 2",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    matches.extend(
        trackwrestling.parse_consolation_round2(
            "Consolation 2nd Round",
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
    root = HERE.parent / "raw-data" / "2024-intermediate"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship 1st Round",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2024-intermediate.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
