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
        first_name="Aaron", last_name="Jones", suffix="Jr", team="Springs Elite WC"
    ),
    ("Alta Jane McQuary", "Collinsville WC"): bracket_utils.Competitor(
        first_name="Alta Jane", last_name="McQuary", suffix=None, team="Collinsville WC"
    ),
    ("Antonio Reyes Ii", "BTS Chicago-Avondale"): bracket_utils.Competitor(
        first_name="Antonio",
        last_name="Reyes",
        suffix="II",
        team="BTS Chicago-Avondale",
    ),
    ("Aydan Del Muro", "nWo WC"): bracket_utils.Competitor(
        first_name="Aydan", last_name="Del Muro", suffix=None, team="nWo WC"
    ),
    ("Azalea De La Torre", "Fox Lake WC"): bracket_utils.Competitor(
        first_name="Azalea", last_name="De La Torre", suffix=None, team="Fox Lake WC"
    ),
    ("Barbara Vargas Parra", "West Suburban Girls WC"): bracket_utils.Competitor(
        first_name="Barbara",
        last_name="Vargas Parra",
        suffix=None,
        team="West Suburban Girls WC",
    ),
    ("Bransyn Von Behren", "Monticello Youth WC"): bracket_utils.Competitor(
        first_name="Bransyn",
        last_name="Von Behren",
        suffix=None,
        team="Monticello Youth WC",
    ),
    ("Caden St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        first_name="Caden",
        last_name="St Angelo",
        suffix=None,
        team="PSF Wrestling Academy",
    ),
    ("Camila S Rodriguez", "BTS Chicago-Midway"): bracket_utils.Competitor(
        first_name="Camila S",
        last_name="Rodriguez",
        suffix=None,
        team="BTS Chicago-Midway",
    ),
    (
        "Cecilia Van Oppen",
        "East Peoria River Bandits Wrestling",
    ): bracket_utils.Competitor(
        first_name="Cecilia",
        last_name="Van Oppen",
        suffix=None,
        team="East Peoria River Bandits Wrestling",
    ),
    (
        "Christopher Hilliard Jr.",
        "Proviso Township Gladiators WC",
    ): bracket_utils.Competitor(
        first_name="Christopher",
        last_name="Hilliard",
        suffix="Jr",
        team="Proviso Township Gladiators WC",
    ),
    ("Dai Zaria Christopher", "Astro WC"): bracket_utils.Competitor(
        first_name="Dai Zaria", last_name="Christopher", suffix=None, team="Astro WC"
    ),
    ("Daquain Hubbard Jr", "Urbana Tigers WC"): bracket_utils.Competitor(
        first_name="Daquain", last_name="Hubbard", suffix="Jr", team="Urbana Tigers WC"
    ),
    ("Darek Lee Iii", "Brawlers WC"): bracket_utils.Competitor(
        first_name="Darek", last_name="Lee", suffix="III", team="Brawlers WC"
    ),
    ("Decan Van Natta", "Roughnecks WC"): bracket_utils.Competitor(
        first_name="Decan", last_name="Van Natta", suffix=None, team="Roughnecks WC"
    ),
    ("Gabriel Travis Jr", "Will County Warriors WC"): bracket_utils.Competitor(
        first_name="Gabriel",
        last_name="Travis",
        suffix="Jr",
        team="Will County Warriors WC",
    ),
    ("Genevieve Del Muro", "nWo WC"): bracket_utils.Competitor(
        first_name="Genevieve", last_name="Del Muro", suffix=None, team="nWo WC"
    ),
    ("Glenn Harston Iii", "Harvey Twisters WC"): bracket_utils.Competitor(
        first_name="Glenn", last_name="Harston", suffix="III", team="Harvey Twisters WC"
    ),
    ("Henry Brown Iii", "Harvey Twisters WC"): bracket_utils.Competitor(
        first_name="Henry", last_name="Brown", suffix="III", team="Harvey Twisters WC"
    ),
    ("James Jackson Jr.", "Fox Valley WC"): bracket_utils.Competitor(
        first_name="James", last_name="Jackson", suffix="Jr", team="Fox Valley WC"
    ),
    ("James Lima Iii", "Wolfpak WC"): bracket_utils.Competitor(
        first_name="James", last_name="Lima", suffix="III", team="Wolfpak WC"
    ),
    ("James Newell Iii", "Springs Elite WC"): bracket_utils.Competitor(
        first_name="James", last_name="Newell", suffix="III", team="Springs Elite WC"
    ),
    ("Jerome Turner Jr", "Springs Elite WC"): bracket_utils.Competitor(
        first_name="Jerome", last_name="Turner", suffix="Jr", team="Springs Elite WC"
    ),
    ("Joseph De La Torre", "Lake Zurich Cubs WC"): bracket_utils.Competitor(
        first_name="Joseph",
        last_name="De La Torre",
        suffix=None,
        team="Lake Zurich Cubs WC",
    ),
    ("Layla Ann Snarey", "West Suburban Girls WC"): bracket_utils.Competitor(
        first_name="Layla Ann",
        last_name="Snarey",
        suffix=None,
        team="West Suburban Girls WC",
    ),
    ("Lesly De La Cruz", "Irish WC"): bracket_utils.Competitor(
        first_name="Lesly", last_name="De La Cruz", suffix=None, team="Irish WC"
    ),
    ("Michael Krueger Jr.", "Demolition WC"): bracket_utils.Competitor(
        first_name="Michael", last_name="Krueger", suffix="Jr", team="Demolition WC"
    ),
    ("Nolan St Angelo", "PSF Wrestling Academy"): bracket_utils.Competitor(
        first_name="Nolan",
        last_name="St Angelo",
        suffix=None,
        team="PSF Wrestling Academy",
    ),
    ("Paxton De La Vega", "Tinley Park Bulldogs WC"): bracket_utils.Competitor(
        first_name="Paxton",
        last_name="De La Vega",
        suffix=None,
        team="Tinley Park Bulldogs WC",
    ),
    ("Pedro David Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        first_name="Pedro David", last_name="Rangel", suffix=None, team="Storm Youth WC"
    ),
    ("Pedro Legend Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        first_name="Pedro Legend",
        last_name="Rangel",
        suffix=None,
        team="Storm Youth WC",
    ),
    ("Ricky Olszta Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        first_name="Ricky", last_name="Olszta", suffix="Jr", team="Lincoln-Way WC"
    ),
    ("Robert Wiggins Jr", "East St. Louis WC"): bracket_utils.Competitor(
        first_name="Robert", last_name="Wiggins", suffix="Jr", team="East St. Louis WC"
    ),
    ("Shawn Marie Omeara", "Harlem Huskies WC"): bracket_utils.Competitor(
        first_name="Shawn Marie",
        last_name="Omeara",
        suffix=None,
        team="Harlem Huskies WC",
    ),
    ("Steven Griffith Jr.", "Storm Youth WC"): bracket_utils.Competitor(
        first_name="Steven", last_name="Griffith", suffix="Jr", team="Storm Youth WC"
    ),
    ("Travis Hinton Jr", "Toss Em Up Wrestling Academy"): bracket_utils.Competitor(
        first_name="Travis",
        last_name="Hinton",
        suffix="Jr",
        team="Toss Em Up Wrestling Academy",
    ),
    ("Vada Jo Riley", "Antioch Predators WC"): bracket_utils.Competitor(
        first_name="Vada Jo",
        last_name="Riley",
        suffix=None,
        team="Antioch Predators WC",
    ),
    ("Yesenia Gonzalez Carbajal", "Blackhawk WC"): bracket_utils.Competitor(
        first_name="Yesenia",
        last_name="Gonzalez Carbajal",
        suffix=None,
        team="Blackhawk WC",
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
