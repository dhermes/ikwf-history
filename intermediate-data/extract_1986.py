# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
The competitor list (from scans from Corey Atwell) is contained below.

In 145 pound bracket, the placers (listed in 1987 program) are not possible
based on the Corey Atwell semifinalists written in. We went with the Corey
Atwell bracket, so there may be a discrepancy.
"""

import pathlib

import bracket_utils
import manual_entry
from PIL import Image

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Panther WC": 189.0,  # "Burbank Panthers"
    "Vittum Cats": 154.5,
    "Harvey Twisters": 133.5,
    "DeKalb Wrestling": 128.5,
    "Tinley Park Bulldogs": 95.5,
    "Oak Forest Warriors": 93.0,
    "Colts WC": 92.5,
    "Batavia WC": 89.0,
    "Orland Park Pioneers": 69.5,
    "Elgin WC": 69.0,
    "Roxana Roughnecks": 67.0,
    "OPRF Jr. Wrestling Club": 65.5,
    "Belvidere Bandits": 63.5,
    "Bloomington Jr. High": 63.5,
    "Geneseo WC": 62.5,
    "Villa Lombard WC": 59.5,
    "Rich Wrestling Ltd.": 57.5,
    "Forman Wrestling Boosters": 55.5,
    "Bensenville Bulldogs": 53.0,
    "Patriot WC": 51.0,
    "Medinah Lancer WC": 49.0,
    "Moline Booster": 49.0,
    "Tomcat WC": 47.0,
    "Sterling Warrior WC": 46.5,
    "Arlington Cardinals WC": 46.0,
    "Harvard WC": 38.0,
    "Indian Prairie WC": 38.0,
    "Lemont Bears WC": 38.0,
    "Tigertown Tanglers": 38.0,
    "St. Tarcissus Raiders": 37.0,
    "Oak Lawn PD": 35.5,
    "Boys Club of Pekin": 34.5,
    "Bronco WC": 32.0,
    "Indian Trail Jr. High": 32.0,
    "Lil Reaper WC": 32.0,
    "Peotone PD WC": 32.0,
    "Wilbur Trimpe JH": 29.0,
    "Cooper's Cougars": 28.0,
    "Lockport Grapplers WC": 26.5,
    "Midlothian Saints": 25.5,
    "Cahokia WC": 24.0,
    "Carbondale Park District": 23.0,
    "Barrington Colts": 22.0,
    "Mattoon WC": 20.0,
    "Matburns WC": 19.0,
    "Frankfort Falcons WC": 18.0,
    "Dolton Wrestling Falcons": 17.0,
    "Lan-Oak PD": 17.0,
    "Yorkville WC": 17.0,
    "Edwardsville WC": 16.0,
    "Gibson City Youth WC": 16.0,
    "Murphysboro Jr. High": 16.0,
    "Redbird WC": 16.0,
    "Roxana Vikings": 16.0,
    "Decatur WC": 15.0,
    "Dundee Highlanders": 15.0,
    "East Moline WC": 15.0,
    "Turk Wrestling Club": 15.0,
    "Razorbacks": 14.5,
    "Hoopeston-East Lynn Jr.": 14.0,
    "Rockridge Jr. High": 14.0,
    "St. Charles Saints": 13.5,
    "Crossface WC": 13.0,
    "Greenwood / Tumaro WC": 13.0,
    "Cardinals": 12.5,
    "Champaign WC": 12.0,
    "Mokena WC": 12.0,
    "West Frankfort WC": 12.0,
    "Harlem Boys Club": 11.0,
    "Georgetown WC": 9.0,
    "Sycamore WC": 9.0,
    "Thomas Jefferson JH": 9.0,
    "Westville Jr. High": 8.5,
    "Eisenhower Jr. High": 8.0,
    "Lions WC": 8.0,
    "Northwood Warhawks WC": 8.0,
    "Niles WC": 7.0,
    "Morton Youth WC": 6.5,
    "Bethalto Boys Club": 6.0,
    "Naperville Warhawks": 6.0,
    "Hazel Crest Jr. Hawks": 4.5,
    "Bismarck-Henning WC": 4.0,
    "Black Hawk WC": 4.0,
    "Chillicothe WC": 4.0,
    "Mt. Zion WC": 4.0,
    "St. Bede's": 4.0,
    "Wheaton Falcons": 4.0,
    "Newman Middle School": 3.0,
    "Naperville Wrestlers": 2.5,
    "Antioch Upper Grade": 2.0,
    "Belleville Little Devils": 2.0,
    "Calumet Memorial PD": 2.0,
    "Danville Youth WC": 2.0,
    "Franklin Park Raiders": 2.0,
    "Granite City-Grigsby": 2.0,
    "Jordan WC": 2.0,
    "Metamora Kids Wrestling Club": 2.0,
    "Round Lake Area PD": 2.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("James Boyd Jr.", "Bensenville Bulldogs"): bracket_utils.Competitor(
        full_name="James Boyd Jr.",
        first_name="James",
        last_name="Boyd",
        team_full="Bensenville Bulldogs",
    ),
    ("Jason De Bello", "Bensenville Bulldogs"): bracket_utils.Competitor(
        full_name="Jason De Bello",
        first_name="Jason",
        last_name="De Bello",
        team_full="Bensenville Bulldogs",
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
    _generate_placers_image(1986)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes = manual_entry.load_manual_entries(
        _HERE.parent, 1986, _NAME_EXCEPTIONS
    )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1986.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
