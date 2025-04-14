# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Cataleya Castillo-Cisner": "Cataleya Castillo-Cisneros",
    "Christophe Hilliard Jr.": "Christopher Hilliard Jr.",
    "Christophe Kucala": "Christopher Kucala",
    "Christophe Miroslaw": "Christopher Miroslaw",
    "Christophe Navarro": "Christopher Navarro",
    "Christophe Todd": "Christopher Todd",
    "Christophe Velasquez": "Christopher Velasquez",
    "Harrison England-Matthew": "Harrison England-Matthews",
    "Juan Gonzalez-Brasov": "Juan Gonzalez-Brasovan",
    "Justin-Car Jones": "Justin-Carter Jones",
    "Myles-Aver Holland": "Myles-Avery Holland",
    "Pedro Davi Rangel": "Pedro David Rangel",
    "Pedro Lege Rangel": "Pedro Legend Rangel",
    "Shawn Mari Omeara": "Shawn Marie Omeara",
    "Yesenia Gonzalez Carbaj": "Yesenia Gonzalez Carbajal",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Aaron Jones Jr", "Springs Elite WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Aaron",
        last_name="Jones",
        team_acronym="Springs Elite WC",
    ),
    ("Alta Jane McQuary", "Collinsville WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Alta Jane",
        last_name="McQuary",
        team_acronym="Collinsville WC",
    ),
    ("Antonio Reyes Ii", "BTS Chicago-Avondale"): bracket_utils.Competitor(
        full_name="",
        first_name="Antonio",
        last_name="Reyes",
        team_acronym="BTS Chicago-Avondale",
    ),
    ("Aydan Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Aydan",
        last_name="Del Muro",
        team_acronym="nWo WC",
    ),
    ("Azalea De La Torre", "Fox Lake WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Azalea",
        last_name="De La Torre",
        team_acronym="Fox Lake WC",
    ),
    ("Barbara Vargas Parra", "West Suburban Girls WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Barbara",
        last_name="Vargas Parra",
        team_acronym="West Suburban Girls WC",
    ),
    ("Bransyn Von Behren", "Monticello Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Bransyn",
        last_name="Von Behren",
        team_acronym="Monticello Youth WC",
    ),
    ("Caden St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Caden",
        last_name="St Angelo",
        team_acronym="PSF Wrestling Academy",
    ),
    ("Camila S Rodriguez", "BTS Chicago-Midway"): bracket_utils.Competitor(
        full_name="",
        first_name="Camila S",
        last_name="Rodriguez",
        team_acronym="BTS Chicago-Midway",
    ),
    (
        "Cecilia Van Oppen",
        "East Peoria River Bandits Wrestling",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Cecilia",
        last_name="Van Oppen",
        team_acronym="East Peoria River Bandits Wrestling",
    ),
    (
        "Christopher Hilliard Jr.",
        "Proviso Township Gladiators WC",
    ): bracket_utils.Competitor(
        full_name="",
        first_name="Christopher",
        last_name="Hilliard",
        team_acronym="Proviso Township Gladiators WC",
    ),
    ("Dai Zaria Christopher", "Astro WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Dai Zaria",
        last_name="Christopher",
        team_acronym="Astro WC",
    ),
    ("Daquain Hubbard Jr", "Urbana Tigers WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Daquain",
        last_name="Hubbard",
        team_acronym="Urbana Tigers WC",
    ),
    ("Darek Lee Iii", "Brawlers WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Darek",
        last_name="Lee",
        team_acronym="Brawlers WC",
    ),
    ("Decan Van Natta", "Roughnecks WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Decan",
        last_name="Van Natta",
        team_acronym="Roughnecks WC",
    ),
    ("Gabriel Travis Jr", "Will County Warriors WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Gabriel",
        last_name="Travis",
        team_acronym="Will County Warriors WC",
    ),
    ("Genevieve Del Muro", "nWo WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Genevieve",
        last_name="Del Muro",
        team_acronym="nWo WC",
    ),
    ("Glenn Harston Iii", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Glenn",
        last_name="Harston",
        team_acronym="Harvey Twisters WC",
    ),
    ("Henry Brown Iii", "Harvey Twisters WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Henry",
        last_name="Brown",
        team_acronym="Harvey Twisters WC",
    ),
    ("James Jackson Jr.", "Fox Valley WC"): bracket_utils.Competitor(
        full_name="",
        first_name="James",
        last_name="Jackson",
        team_acronym="Fox Valley WC",
    ),
    ("James Lima Iii", "Wolfpak WC"): bracket_utils.Competitor(
        full_name="",
        first_name="James",
        last_name="Lima",
        team_acronym="Wolfpak WC",
    ),
    ("James Newell Iii", "Springs Elite WC"): bracket_utils.Competitor(
        full_name="",
        first_name="James",
        last_name="Newell",
        team_acronym="Springs Elite WC",
    ),
    ("Jerome Turner Jr", "Springs Elite WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Jerome",
        last_name="Turner",
        team_acronym="Springs Elite WC",
    ),
    ("Joseph De La Torre", "Lake Zurich Cubs WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Joseph",
        last_name="De La Torre",
        team_acronym="Lake Zurich Cubs WC",
    ),
    ("Layla Ann Snarey", "West Suburban Girls WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Layla Ann",
        last_name="Snarey",
        team_acronym="West Suburban Girls WC",
    ),
    ("Lesly De La Cruz", "Irish WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Lesly",
        last_name="De La Cruz",
        team_acronym="Irish WC",
    ),
    ("Michael Krueger Jr.", "Demolition WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Michael",
        last_name="Krueger",
        team_acronym="Demolition WC",
    ),
    ("Nolan St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Nolan",
        last_name="St Angelo",
        team_acronym="PSF Wrestling Academy",
    ),
    ("Paxton De La Vega", "Tinley Park Bulldogs WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Paxton",
        last_name="De La Vega",
        team_acronym="Tinley Park Bulldogs WC",
    ),
    ("Pedro David Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro David",
        last_name="Rangel",
        team_acronym="Storm Youth WC",
    ),
    ("Pedro Legend Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Legend",
        last_name="Rangel",
        team_acronym="Storm Youth WC",
    ),
    ("Ricky Olszta Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Ricky",
        last_name="Olszta",
        team_acronym="Lincoln-Way WC",
    ),
    ("Robert Wiggins Jr", "East St. Louis WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Robert",
        last_name="Wiggins",
        team_acronym="East St. Louis WC",
    ),
    ("Shawn Marie Omeara", "Harlem Huskies WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Shawn Marie",
        last_name="Omeara",
        team_acronym="Harlem Huskies WC",
    ),
    ("Steven Griffith Jr.", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Steven",
        last_name="Griffith",
        team_acronym="Storm Youth WC",
    ),
    ("Travis Hinton Jr", "Toss Em Up Wrestling Academy"): bracket_utils.Competitor(
        full_name="",
        first_name="Travis",
        last_name="Hinton",
        team_acronym="Toss Em Up Wrestling Academy",
    ),
    ("Vada Jo Riley", "Antioch Predators WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Vada Jo",
        last_name="Riley",
        team_acronym="Antioch Predators WC",
    ),
    ("Yesenia Gonzalez Carbajal", "Blackhawk WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Yesenia",
        last_name="Gonzalez Carbajal",
        team_acronym="Blackhawk WC",
    ),
}
_TEAM_FIXES: dict[str, tuple[str, str]] = {
    "Cameron Ramp": ("Backyard Brawle", "Backyard Brawlers Midwest"),
    "Jack Wachstetter": ("Backyard Brawle", "Backyard Brawlers Midwest"),
    "Jeremiah Hayes": ("Backyard Brawle", "Backyard Brawlers Midwest"),
    "Colton Zabinski": ("Backyard Brawle", "Backyard Brawlers North Wrestling"),
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
    root = HERE.parent / "raw-data" / "2025"
    extracted_tournament = trackwrestling.extract_year(
        root,
        _parse_rounds,
        "Championship First Round",
        "Champ. Round 1",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    with open(HERE / "extracted.2025.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
