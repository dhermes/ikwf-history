# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
The competitor list (from scans from Corey Atwell) is contained below.

Note that 95, 100, and 105 are missing from the competitor lists.

A few edits to team names from the program:

- Barrington Broncs -> Barrington Broncos
- Foreman -> Foreman WC
- Forman WC -> Foreman WC
- Harvey PD Twisters -> Harvey Twisters
"""

import pathlib

import bracket_utils
import manual_entry
from PIL import Image

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    95: [
        bracket_utils.Placer(name="Bill O'Brien", team="Panther WC"),
        bracket_utils.Placer(name="Vince Cascone", team="Vittum Cats"),
        bracket_utils.Placer(name="Brent Davis", team="Granite City-Grigsby"),
        bracket_utils.Placer(name="Jeff Cordova", team="Lockport Grapplers"),
        bracket_utils.Placer(name="Brian Ezell", team="Frankfort Falcons"),
        bracket_utils.Placer(name="Scott Carfagnini", team="Stickers"),
    ],
    100: [
        bracket_utils.Placer(name="Bill Guide", team="Vittum Cats"),
        bracket_utils.Placer(name="George Hoffman", team="Joliet YMCA Wrestling"),
        bracket_utils.Placer(name="Randy Saller", team="Dolton Falcons"),
        bracket_utils.Placer(name="Matt Cruszka", team="Indian Prairie"),
        bracket_utils.Placer(name="Andrew Larson", team="East Moline WC"),
        bracket_utils.Placer(name="Dirk Dorn", team="Naperville Warhawks"),
    ],
    105: [
        bracket_utils.Placer(name="Ryan Shafer", team="Warrior WC"),  # Sterling?
        bracket_utils.Placer(name="Steven Smerz", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="Patrick Henley", team="Harvey Twisters"),
        bracket_utils.Placer(name="Bob Bartkowaik", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Matt Rademaker", team="Illini Bluffs WC"),
        bracket_utils.Placer(name="Sock Woodruff", team="Deerpath WC"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Vittum Cats": 287.0,
    "Panther WC": 174.0,
    "Villa Lombard": 164.0,
    "Oak Forest Warriors": 133.0,
    "Tinley Park Bulldogs": 111.0,
    "Belvidere YMCA Bandits": 95.0,
    "Rich Wrestling Ltd.": 93.0,
    "Colts WC": 87.0,
    "New Lenox Lions": 72.5,
    "Frankfort Falcons": 69.0,
    "Warrior WC": 68.0,
    "Harvard WC": 67.5,
    "Wilbur Trimpe Jr. High": 63.5,
    "DeKalb-Huntley": 62.0,
    "Orland Park Pioneers": 58.5,
    "Granite City-Coolidge": 54.5,
    "Roxana PD": 54.5,  # Roughnecks
    "Rockridge Jr. High": 52.0,
    "Joliet YMCA Wrestling": 51.0,
    "Harvey Twisters": 50.5,
    "Bensenville": 49.0,
    "Foreman WC": 44.0,
    "Hickory Hills PD": 41.5,
    "Lancers": 41.0,
    "Elgin WC": 40.0,
    "Edwardsville WC": 39.5,
    "Granite City-Grigsby": 36.5,
    "Indian Trail-Plainfield": 33.5,
    "Oak Park-River Forest": 33.5,
    "Batavia WC": 33.0,
    "Boys Club of Pekin": 28.0,
    "Matburns WC": 28.0,
    "Bradley Bourbonnais WC": 27.0,
    "Carbondale PD": 27.0,
    "Dolton Falcons": 27.0,
    "St. Tarcissus Raiders": 27.0,
    "East Moline WC": 26.5,
    "Franklin Park Raiders": 25.5,
    "Jefferson": 25.5,
    "Unity Youth WC": 25.0,
    "Lan-Oak PD Wrestling": 22.5,
    "Generals WC": 21.5,
    "Illini Bluffs WC": 21.5,
    "Chicago Ridge PD": 21.0,
    "Lanphier-Southeast WC": 21.0,
    "Lemont WC": 21.0,
    "Arlington Heights WC": 20.5,
    "Crusaders WC": 20.0,
    "Mattoon WC": 20.0,
    "Champaign": 19.5,
    "Catlin WC": 19.0,
    "Lockport Grapplers": 19.0,
    "Murphysboro Jr. High": 19.0,
    "Belleville Little Devils": 18.0,
    "Indian Prairie": 18.0,
    "Rosemont Cobra": 18.0,
    "Eisenhower": 17.0,
    "Fischer WC": 16.0,
    "Machesney Park Independent": 16.0,
    "Deerpath WC": 15.5,
    "Pekin": 15.0,
    "Redbird WC": 15.0,
    "Morton Youth WC": 14.5,
    "Blackhawk WC": 14.0,
    "Hoopeston East Lynn": 14.0,
    "Stickers": 13.0,
    "Youth Razorbacks": 13.0,
    "Clinton Rosette M.S.": 12.5,
    "Palos South": 12.5,
    "Newman Middle School": 12.0,
    "Round Lake Area PD": 12.0,
    "Naperville Warhawks": 11.0,
    "Antioch Upper Grade": 10.5,
    "Danville Youth WC": 10.5,
    "Geneseo WC": 10.0,
    "Naperville Warriors": 10.0,
    "Peotone PD": 8.0,
    "Dundee Highlanders": 7.5,
    "Gower": 6.5,
    "Barrington Broncos": 6.0,
    "Mt. Zion WC": 6.0,
    "Georgetown WC": 5.0,
    "Gibson City Youth": 4.5,
    "Wheaton Falcons": 4.5,
    "Aurora Tomcats": 4.0,
    "Bethalto Boys Club": 4.0,
    "Bismarck-Henning WC": 4.0,
    "Hinsdale": 4.0,
    "Marquart": 4.0,
    "Rock Island 1": 4.0,
    "Urbana Kids Club": 4.0,
    "Sandwich": 3.0,  # No athletes in programs, probably added after a scratch?
    "Midlothian PD Braves": 2.5,
    "Panther Kids": 2.0,
    "Taylorville WC": 2.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("John St. Clair", "Rich Wrestling Ltd."): bracket_utils.Competitor(
        full_name="John St. Clair",
        first_name="John",
        last_name="St. Clair",
        team_full="Rich Wrestling Ltd.",
    ),
}


def _create_placers_image_row(
    headshot_img, names_img, headshot_width, headshot_height, name_width, name_height
):
    # Create padded headshot box
    headshot_box = Image.new("RGBA", (headshot_width, headshot_height), (0, 0, 0, 0))
    headshot_box.paste(
        headshot_img,
        (
            (headshot_width - headshot_img.width) // 2,
            (headshot_height - headshot_img.height) // 2,
        ),
    )

    # Create padded name box
    name_box = Image.new("RGBA", (name_width, name_height), (0, 0, 0, 0))
    name_box.paste(
        names_img,
        ((name_width - names_img.width) // 2, (name_height - names_img.height) // 2),
    )

    # Stack horizontally
    row = Image.new(
        "RGBA",
        (
            headshot_width + name_width,
            max(headshot_height, name_height),
        ),
        (0, 0, 0, 0),
    )
    row.paste(headshot_box, (0, (row.height - headshot_height) // 2))
    row.paste(name_box, (headshot_width, (row.height - name_height) // 2))

    return row


def _generate_placers_image(year: int):
    all_weights = set(
        [
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
            105,
            111,
            118,
            125,
            135,
            145,
            155,
            170,
            185,
            275,
        ]
    )
    weights = sorted(all_weights)

    raw_root = _HERE.parent / "raw-data" / str(year)
    headshots = [
        Image.open(raw_root / "placers-headshot" / f"{weight}.png")
        for weight in weights
    ]
    names = [
        Image.open(raw_root / "placers-names" / f"{weight}.png") for weight in weights
    ]

    max_headshot_width = max(img.width for img in headshots)
    max_headshot_height = max(img.height for img in headshots)
    max_name_width = max(img.width for img in names)
    max_name_height = max(img.height for img in names)

    rows = [
        _create_placers_image_row(
            headshot_img,
            names_img,
            max_headshot_width,
            max_headshot_height,
            max_name_width,
            max_name_height,
        )
        for headshot_img, names_img in zip(headshots, names, strict=True)
    ]

    midpoint = (len(rows) + 1) // 2  # extra one on left if odd
    left_column = rows[:midpoint]
    right_column = rows[midpoint:]

    row_width = max_headshot_width + max_name_width
    row_height = max(max_headshot_height, max_name_height)
    column_height = midpoint * row_height
    total_width = 2 * row_width

    # Create final canvas
    final_img = Image.new("RGBA", (total_width, column_height), (0, 0, 0, 0))

    # Paste left column
    for i, row in enumerate(left_column):
        width_offset = 0
        height_offset = i * row_height
        final_img.paste(
            row, (width_offset + (row_width - row.width) // 2, height_offset)
        )

    # Paste right column
    for i, row in enumerate(right_column):
        width_offset = row_width
        height_offset = i * row_height
        final_img.paste(
            row, (width_offset + (row_width - row.width) // 2, height_offset)
        )

    static_dir = _HERE.parent / "static" / "static" / "images"
    save_location = static_dir / f"{year}-senior-placers.png"
    final_img.save(save_location)


def main():
    _generate_placers_image(1985)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes = manual_entry.load_manual_entries(
        _HERE.parent, 1985, _NAME_EXCEPTIONS
    )

    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1985.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
