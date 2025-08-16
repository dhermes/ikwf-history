# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Troy Doughman", team="Elmhurst"),
    65: bracket_utils.Placer(name="Pat Rajnic", team="Wheaton Franklin"),
    70: bracket_utils.Placer(name="Bill Horcher", team="Dundee Highlanders"),
    75: bracket_utils.Placer(name="Tony Pellegrini", team="Hazel Crest"),
    80: bracket_utils.Placer(name="Todd Sterr", team="Joliet Boy's Club"),
    90: bracket_utils.Placer(name="Kurt Law", team="Savanna"),
    95: bracket_utils.Placer(name="Mark Ruettiger", team="Joliet Boy's Club"),
    105: bracket_utils.Placer(name="Todd Ferris", team="Savanna"),
    112: bracket_utils.Placer(name="Mike Rosman", team="Naperville"),
    118: bracket_utils.Placer(name="Ray Villareal", team="West Chicago"),
    125: bracket_utils.Placer(name="Bill Klotz", team="New Lenox Oakview"),
    135: bracket_utils.Placer(name="Alan Porter", team="Oak Forest"),
    145: bracket_utils.Placer(name="Bill McCue", team="Aurora Simmons"),
    160: bracket_utils.Placer(name="Rich Constable", team="Addison"),
    185: bracket_utils.Placer(name="Bill George", team="St. Thecla"),
    275: bracket_utils.Placer(name="Jeff Sheppard", team="Savanna"),
}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    100: [
        bracket_utils.Placer(name="Mark Barron", team="Aurora Franklin"),
        bracket_utils.Placer(name="Matt Twitty", team="Mattoon"),
        bracket_utils.Placer(name="Mike Daughters", team="Plainfield"),
        bracket_utils.Placer(name="Ken Mansell", team="Joliet Boy's Club"),
        bracket_utils.Placer(name="Mike Smith", team="Stillman Valley"),
        bracket_utils.Placer(name="Jack Sale", team="Mahomet"),
    ],
}
_SENIOR_COMPETITORS: dict[int, list[str | None]] = {
    85: [
        "Jerry Miller :: Granite City :: 6",
        "Marcus Gunaka :: Tinley Park",
        "Walsh :: St. Thecla",
        "Sampson :: Moline",
        "Dempsey :: Naperville",
        None,
        "Cawson :: Huntley",
        "Bill Kelly :: Chicago Ridge :: 2",
        "Jaraczewski :: Panther",
        "Keith Rodgers :: Plainfield :: 3",
        "Nowak :: Wheaton Franklin",
        None,
        "Ed Giese :: Franklin Park :: 1",
        "Tieman :: Bellevile West",
        "Sloan :: Pontiac",
        "McCausland :: Wheaton Franklin",
        "Nelson :: Champaign",
        None,
        "Ed DeBevec :: Tinley Park :: 4",
        "Jim Maddock :: Marshall :: 5",
        None,
        "Vickens :: Lake Villa",
        "Govoni :: Joliet Boy's Club",
        None,
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Plainfield": 164.0,  # `143`?
    "Savanna": 119.0,
    "New Lenox Oakview": 85.0,
    "Panther": 73.0,
    "Joliet Boy's Club": 68.0,
    "Aurora Simmons": 58.0,
    "Hazel Crest": 58.0,
    "Aurora Franklin": 57.0,
    "West Chicago": 52.0,
    "Mattoon": 52.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Sampson", "Moline"): bracket_utils.Competitor(
        full_name="Sampson",
        first_name="",
        last_name="Sampson",
        team_full="Moline",
    ),
    ("Cawson", "Huntley"): bracket_utils.Competitor(
        full_name="Cawson",
        first_name="",
        last_name="Cawson",
        team_full="Huntley",
    ),
    ("McCausland", "Wheaton Franklin"): bracket_utils.Competitor(
        full_name="McCausland",
        first_name="",
        last_name="McCausland",
        team_full="Wheaton Franklin",
    ),
    ("Vickens", "Lake Villa"): bracket_utils.Competitor(
        full_name="Vickens",
        first_name="",
        last_name="Vickens",
        team_full="Lake Villa",
    ),
    ("Walsh", "St. Thecla"): bracket_utils.Competitor(
        full_name="Walsh",
        first_name="",
        last_name="Walsh",
        team_full="St. Thecla",
    ),
    ("Dempsey", "Naperville"): bracket_utils.Competitor(
        full_name="Dempsey",
        first_name="",
        last_name="Dempsey",
        team_full="Naperville",
    ),
    ("Jaraczewski", "Panther"): bracket_utils.Competitor(
        full_name="Jaraczewski",
        first_name="",
        last_name="Jaraczewski",
        team_full="Panther",
    ),
    ("Nowak", "Wheaton Franklin"): bracket_utils.Competitor(
        full_name="Nowak",
        first_name="",
        last_name="Nowak",
        team_full="Wheaton Franklin",
    ),
    ("Tieman", "Bellevile West"): bracket_utils.Competitor(
        full_name="Tieman",
        first_name="",
        last_name="Tieman",
        team_full="Bellevile West",
    ),
    ("Sloan", "Pontiac"): bracket_utils.Competitor(
        full_name="Sloan",
        first_name="",
        last_name="Sloan",
        team_full="Pontiac",
    ),
    ("Nelson", "Champaign"): bracket_utils.Competitor(
        full_name="Nelson",
        first_name="",
        last_name="Nelson",
        team_full="Champaign",
    ),
    ("Govoni", "Joliet Boy's Club"): bracket_utils.Competitor(
        full_name="Govoni",
        first_name="",
        last_name="Govoni",
        team_full="Joliet Boy's Club",
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
    all_weights = set(_SENIOR_CHAMPS.keys())
    all_weights.update(_SENIOR_PLACERS.keys())
    all_weights.update(_SENIOR_COMPETITORS.keys())
    weights = sorted(all_weights)

    raw_root = HERE.parent / "raw-data" / str(year)
    headshots = [
        Image.open(raw_root / "placers-headshot" / f"{weight}.jpg")
        for weight in weights
    ]
    names = [
        Image.open(raw_root / "placers-names" / f"{weight}.jpg") for weight in weights
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

    static_dir = HERE.parent / "static" / "static" / "images"
    save_location = static_dir / f"{year}-senior-placers.png"
    final_img.save(save_location)


def main():
    _generate_placers_image(1977)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    for weight, competitors in _SENIOR_COMPETITORS.items():
        bout_numbers = {}
        weight_class = bracket_utils.weight_class_from_competitors(
            "senior",
            weight,
            competitors,
            _SENIOR_TEAM_REPLACE,
            _NAME_EXCEPTIONS,
            bout_numbers,
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1977.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
