# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
The competitor list (from scans from Corey Atwell) is contained below.

There are a few matches where the winner is not written and I have guessed for
bracket continuity.

Also the 275 bracket doesn't make sense.
"""

import pathlib

import bracket_utils
import manual_entry

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Harvey Twisters": 248.0,
    "Vittum Cats": 165.0,
    "DeKalb WC": 137.5,
    "Geneseo WC": 111.0,
    "Arlington Cardinals WC": 106.0,
    "Panther Wrestling Club": 105.0,
    "Colts WC": 101.0,
    "Tinley Park Bulldogs": 95.0,
    "Villa Lombard WC": 89.0,
    "Frankfort Falcons": 78.0,
    "Moline Wildcats": 75.0,
    "Belvidere Bandits YMCA WC": 71.5,
    "LaGrange Lions": 68.0,
    "Rich Wrestling LTD": 60.5,
    "Dolton Park Jr. Falcons": 58.0,
    "Lil' Reaper WC": 54.5,
    "Eisenhower Jr. High": 53.5,
    "Forman WC": 45.5,
    "Lanphier-Southeast WC": 45.0,
    "Wheaton P.D. Falcons": 45.0,
    "Roxana Jr. High Vikings": 43.0,
    "Unity Youth WC": 43.0,
    "Oak Forest Warriors": 42.0,
    "Oak Park River Forest WC": 41.5,
    "Mattoon WC": 40.0,
    "Orland Park Pioneers": 40.0,
    "Sycamore WC": 40.0,
    "Lan-Oak Park District": 37.0,
    "Dundee Highlanders": 36.5,
    "Turk WC": 33.5,
    "Catlin WC": 33.0,
    "Newman Middle School": 33.0,
    "Rockridge Jr. High": 33.0,
    "Belleville Little Devils": 32.0,
    "Naperville Warhawks": 32.0,
    "Medinah Lancers WC": 31.5,
    "Lemont Bears WC": 31.0,
    "Moline Spartans": 27.5,
    "Bismarck-Henning WC": 26.0,
    "Elgin Matt Rats WC": 25.5,
    "Lockport Grapplers WC": 24.0,
    "Morton Youth WC": 23.5,
    "J-Hawk WC": 23.0,
    "Illinois Valley WC": 22.0,
    "Roxana Roughnecks": 21.5,
    "Naperville Wrestlers": 20.5,
    "Naperville Patriots": 19.0,
    "Rams WC": 17.5,
    "H.P. Little Giant WC": 16.0,
    "Matburns Wrestling Club": 16.0,
    "Crossface WC": 15.0,
    "Danville YMCA WC": 13.5,
    "Oak Lawn PD": 13.0,
    "Centralia WC": 12.0,
    "Dixon WC": 12.0,
    "Georgetown WC": 12.0,
    "Mascoutah Jr. High": 12.0,
    "Westville Jr. High": 12.0,
    "Harvard WC": 11.0,
    "Hoopeston-East Lynn Jr. High": 11.0,
    "Bloomington Jr. High": 10.5,
    "Jordan WC": 10.5,
    "Bethalto Boys Club": 10.0,
    "Round Lake P.D. Spartans": 10.0,
    "Crestwood Colts WC": 8.0,
    "Granite City Grigsby WC": 8.0,
    "Woodstock Cardinals": 8.0,
    "Cahokia WC South": 7.0,
    "Harlem-Franklin Boys Club": 6.5,
    "St. Charles J.H. WC": 6.0,
    "Yorkville WC": 6.0,
    "Bartonville Blue Crew": 4.0,
    "Blackhawk WC": 4.0,
    "Carol Stream P.D.": 4.0,
    "Fisher WC": 4.0,
    "Franklin Park Raiders": 4.0,
    "Gibson City Youth WC": 4.0,
    "Jefferson Wolverines": 4.0,
    "Mt. Zion WC": 4.0,
    "St. Tarcissus Raiders": 4.0,
    "Urbana Kids WC": 4.0,
    "Lawrence County WC": 3.0,
    "Murphysboro Jr. High": 3.0,
    "Rosemont Cobras": 3.0,
    "Tomcat WC": 2.5,
    "Geneva Vikings": 2.5,
    "Chillicothe WC": 2.0,
    "East Moline WC": 2.0,
    "Hickory Hills Park District": 2.0,
    "Naperville Warriors": 2.0,
    "Wood River Marooners": 2.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Harvie Link, Jr.", "Belleville Little Devils"): bracket_utils.Competitor(
        full_name="Harvie Link, Jr.",
        first_name="Harvie",
        last_name="Link",
        team_full="Belleville Little Devils",
    ),
    ("Howard Dean, III", "Centralia WC"): bracket_utils.Competitor(
        full_name="Howard Dean, III",
        first_name="Howard",
        last_name="Dean",
        team_full="Centralia WC",
    ),
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes = manual_entry.load_manual_entries(
        _HERE.parent, 1987, _NAME_EXCEPTIONS
    )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1987.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
