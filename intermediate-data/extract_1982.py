# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    50: bracket_utils.Placer(name="Jay Ford", team="New Lenox Lions"),
    55: bracket_utils.Placer(name="Jim Czaikowski", team="Panther WC"),
    60: bracket_utils.Placer(name="Jim Zeilinga", team="Oak Forest"),
    65: bracket_utils.Placer(name="Pat Coleman", team="Burbank"),
    70: bracket_utils.Placer(name="Mike Urwin", team="Orland Park Pioneers"),
    75: bracket_utils.Placer(name="Mark Pustelnik", team="East Moline"),
    80: bracket_utils.Placer(name="Dan O'Brien", team="Chicago Ridge"),
    85: bracket_utils.Placer(name="Ken Thompson", team="Glenwood"),
    90: bracket_utils.Placer(name="Joe Cascone", team="Vittum Vikings"),
    95: bracket_utils.Placer(name="Scott Holbrook", team="Sterling Newman"),
    100: bracket_utils.Placer(name="Adam Caldwell", team="Hazel Crest"),
    105: bracket_utils.Placer(name="Mike Rogers", team="Oak Park"),
    111: bracket_utils.Placer(name="Tom Blaha", team="Frankfort"),
    118: bracket_utils.Placer(name="Paul Dagenais", team="Tinley Park Bulldogs"),
    125: bracket_utils.Placer(name="Jon Popp", team="Panther WC"),
    135: bracket_utils.Placer(name="Pete Pasternak", team="Calumet City"),
    145: bracket_utils.Placer(name="Cliff Wittey", team="Hoopeston"),
    155: bracket_utils.Placer(name="Aaron Faivre", team="DeKalb Huntley"),
    170: bracket_utils.Placer(name="Ron Webb", team="Plainfield"),
    185: bracket_utils.Placer(name="Mark Topping", team="Huth"),
    275: bracket_utils.Placer(name="James Washington", team="Rich Township"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "BURBANK PANTHERS": 145.0,
    "DOLTON FALCONS": 134.0,
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
    _generate_placers_image(1982)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1982.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
