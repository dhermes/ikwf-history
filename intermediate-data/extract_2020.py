# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib

import bs4

import bracket_utils
import trackwrestling

HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {
    "Christophe Bern": "Christopher Bern",
    "Christophe Jenkins": "Christopher Jenkins",
    "Christophe Yirsa": "Christopher Yirsa",
    "Pedro Albe Rangel": "Pedro Albert Rangel",
    "Pedro Anto Rangel": "Pedro Antonio Rangel",
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Alec Del Toro", "TJ Trained Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Alec",
        last_name="Del Toro",
        suffix=None,
        team="TJ Trained Wrestling",
    ),
    ("Eyson Van Eycke", "Mt. Vernon Lions Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Eyson",
        last_name="Van Eycke",
        suffix=None,
        team="Mt. Vernon Lions Wrestling",
    ),
    ("Gage La Dere", "Lincoln-Way WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Gage",
        last_name="La Dere",
        suffix=None,
        team="Lincoln-Way WC",
    ),
    ("Hiran Lopez Marquez", "Tomcat WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Hiran",
        last_name="Lopez Marquez",
        suffix=None,
        team="Tomcat WC",
    ),
    ("James Talley Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        full_name="",
        first_name="James",
        last_name="Talley",
        suffix="Jr",
        team="Lincoln-Way WC",
    ),
    ("Jose Del Toro", "TJ Trained Wrestling"): bracket_utils.Competitor(
        full_name="",
        first_name="Jose",
        last_name="Del Toro",
        suffix=None,
        team="TJ Trained Wrestling",
    ),
    ("Justin Cobbs Jr", "Lincoln-Way WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Justin",
        last_name="Cobbs",
        suffix="Jr",
        team="Lincoln-Way WC",
    ),
    ("Lee Jr Smith", "Dakota WC"): bracket_utils.Competitor(
        full_name="", first_name="Lee", last_name="Smith", suffix="Jr", team="Dakota WC"
    ),
    ("Pedro Albert Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Albert",
        last_name="Rangel",
        suffix=None,
        team="Storm Youth WC",
    ),
    ("Pedro Antonio Rangel", "Storm Youth WC"): bracket_utils.Competitor(
        full_name="",
        first_name="Pedro Antonio",
        last_name="Rangel",
        suffix=None,
        team="Storm Youth WC",
    ),
}
_TEAM_FIXES: dict[str, tuple[str, str]] = {}
# NOTE: This is a hack just for 2020 since we know the bout numbers.
_OPENING_BOUT_NUMBER_STARTS: dict[tuple[bracket_utils.Division, int], int] = {
    ("novice", 178): 1,
    ("novice", 215): 9,
    ("novice", 60): 17,
    ("novice", 64): 25,
    ("novice", 69): 33,
    ("novice", 74): 41,
    ("novice", 80): 49,
    ("novice", 86): 57,
    ("novice", 93): 65,
    ("novice", 100): 73,
    ("novice", 108): 81,
    ("novice", 116): 89,
    ("novice", 125): 97,
    ("novice", 134): 105,
    ("novice", 154): 113,
    ("senior", 176): 1,
    ("senior", 188): 9,
    ("senior", 215): 17,
    ("senior", 275): 25,
    ("senior", 70): 33,
    ("senior", 74): 41,
    ("senior", 79): 49,
    ("senior", 84): 57,
    ("senior", 90): 65,
    ("senior", 96): 73,
    ("senior", 103): 81,
    ("senior", 110): 89,
    ("senior", 118): 97,
    ("senior", 126): 105,
    ("senior", 135): 113,
    ("senior", 144): 121,
    ("senior", 154): 129,
    ("senior", 164): 137,
}


def main():
    root = HERE.parent / "raw-data" / "2020"
    with open(root / "team_scores.selenium.json") as file_obj:
        selenium_team_scores = json.load(file_obj)

    team_scores = trackwrestling.parse_team_scores(selenium_team_scores)

    with open(root / "brackets.selenium.json") as file_obj:
        selenium_brackets = json.load(file_obj)

    weight_classes: list[bracket_utils.WeightClass] = []
    for bracket_key, html in selenium_brackets.items():
        division_display, weight_str = bracket_key.split(" - ")
        weight = int(weight_str)
        division = trackwrestling.normalize_division(division_display)
        division_scores = team_scores[division]
        key = (division, weight)
        opening_bout_number_start = _OPENING_BOUT_NUMBER_STARTS[key]
        opening_bouts = list(
            range(opening_bout_number_start, opening_bout_number_start + 8)
        )

        if not isinstance(html, str):
            raise TypeError("Unexpected value", type(html))

        soup = bs4.BeautifulSoup(html, features="html.parser")
        initial_match_slots = trackwrestling.initial_entries(
            soup, division_scores, _NAME_FIXES, _TEAM_FIXES, opening_bouts
        )

        matches: list[bracket_utils.Match] = []

        for i in range(16):
            slot_id = i + 1
            match_slot: bracket_utils.MatchSlot = f"championship_r32_{slot_id:02}"

            top_competitors = initial_match_slots[(match_slot, "top")]
            if i % 2 == 1:
                bout_number = opening_bouts[(i - 1) // 2]
                result = ""
                result_type = "default"
                bottom_competitors = initial_match_slots[(match_slot, "bottom")]
            else:
                bout_number = None
                result = "Bye"
                result_type = "bye"
                bottom_competitors = []

            if len(top_competitors) > 1:
                raise RuntimeError("Invariant violation")
            if len(bottom_competitors) > 1:
                raise RuntimeError("Invariant violation")

            top_competitor = None
            bottom_competitor = None
            if len(top_competitors) == 1:
                top_competitor = top_competitors[0]
            if len(bottom_competitors) == 1:
                bottom_competitor = bottom_competitors[0]

            if top_competitor is None and bottom_competitor is None:
                continue

            top_win = top_competitor is not None

            match = bracket_utils.Match(
                match_slot=match_slot,
                top_competitor=bracket_utils.competitor_from_raw(
                    top_competitor, _NAME_EXCEPTIONS
                ),
                bottom_competitor=bracket_utils.competitor_from_raw(
                    bottom_competitor, _NAME_EXCEPTIONS
                ),
                result=result,
                result_type=result_type,
                bout_number=bout_number,
                top_win=top_win,
            )
            matches.append(match)

        weight_class = bracket_utils.WeightClass(
            division=division, weight=weight, matches=matches
        )
        weight_classes.append(weight_class)

    extracted_tournament = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    with open(HERE / "extracted.2020.json", "w") as file_obj:
        file_obj.write(extracted_tournament.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
