# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Mike O'Brien", team="Chicago Ridge"),
    65: bracket_utils.Placer(name="Chris Scott", team="Joliet YMCA"),
    70: bracket_utils.Placer(name="John Ruiter", team="Joliet YMCA"),
    75: bracket_utils.Placer(name="Scott Pierre", team="Wheaton Franklin"),
    80: bracket_utils.Placer(name="Mike Pierre", team="Wheaton Franklin"),
    85: bracket_utils.Placer(name="Brian Porter", team="Oak Forest Warriors"),
    90: bracket_utils.Placer(name="Jeff Schultz", team="Burbank"),
    95: bracket_utils.Placer(name="Tony Prate", team="Orland Park Pioneers"),
    100: bracket_utils.Placer(name="Rick Criscione", team="Joliet YMCA"),
    105: bracket_utils.Placer(name="Mike Smith", team="Stillman Valley"),
    112: bracket_utils.Placer(name="Guy Milburn", team="Dolton"),  # Milbourn?
    118: bracket_utils.Placer(name="Evan Dale", team="Joliet Washington"),
    125: bracket_utils.Placer(name="Ken Mansell", team="Joliet Boy's Club"),
    135: bracket_utils.Placer(name="Mike Rosman", team="Walter Sundling"),
    145: bracket_utils.Placer(name="Mike Prsybysz", team="Plainfield Indian Tra"),
    160: bracket_utils.Placer(name="Larry Leiparte", team="Mt. Greenwood"),
    185: bracket_utils.Placer(name="Rick Meier", team="DeKalb Huntley"),
    275: bracket_utils.Placer(name="Noah Tyree", team="Bolingbrook Ward"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "PLAINFIELD": 122.5,
    "JOLIET YMCA": 86.0,
}
_TEAM_ACRONYM_MAPPING: dict[str, str] = {
    "Alt": "Alton",
    "AnUP": "Antioch Upper Grade",
    "Apo": "Apollo",
    "BatWc": "Batavia Wrestling Club",
    "Bel R": "Belleville Red",
    "Bel W": "Belleville White",
    "Belvd Y": "Belvidere Y",
    "Ben": "Bensenville",
    "Bism": "Bismark-Henning",
    "Blm": "Bloomington",
    "Bridge": "Bridgeview",
    "Cal C": "Calumet City",
    "Carb": "Carbondale",
    "Carl S": "Carl Sandburg/Mundelein",
    "CSRM": "Carl Sandburg/Rolling Meadows",
    "Champ": "Champaign",
    "CR": "Chicago Ridge",
    "Bob C": "Cicero Bobcats",
    "Coal C": "Coal City",
    "Cool": "Coolidge",
    "Coop": "Cooper",
    "CLN": "Crystal Lake North",
    "Dec": "Decatur",
    "Deer P": "Deerpath",
    "Dix": "Dixon",
    "Dol": "Dolton",
    "Dn Gr": "Downers Grove",
    "High": "Dundee",
    "EM": "East Moline",
    "Edw": "Edwardsville",
    "Eis": "Eisenhower",
    "Elm": "Elmhurst",
    "Gen": "Geneseo",
    "Geog T": "Georgetown",
    "Gom": "Gompers",
    "Gow": "Gower",
    "Hins": "Hinsdale",
    "Hart": "Hartford",
    "Har": "Harvard",
    "HC": "Hazelcrest",
    "Holmes": "Holmes",
    "Hoop": "Hoopeston",
    "Hunt": "Huntley",
    "In Tr": "Indian Trails/Addison",
    "JL": "Jack London",
    "Jane Ad": "Jane Adams",
    "Jeff": "Jefferson/Woodridge",
    "Jol B C": "Joliet Boys Club",
    "Jol Y": "Joliet Y",
    "Jor": "Jordan",
    "Lk Vil": "Lake Villa",
    "Lk Zur WC": "Lake Zurich Wr. Club",
    "Lan": "Lancers",
    "Lin": "Lincoln/Cicero",
    "LJH": "Lincoln Jr. High/Lincoln",
    "Lock": "Lockport",
    "Lund": "Lundahl",
    "Mah": "Mahomet Seymour",
    "Mat": "Mattoon",  # ALSO: Matburns?
    "Mink": "Minooka",
    "Mok": "Mokena",
    "Mt. G": "Mt. Greenwood",
    "Mur": "Murphysboro",
    "Nap": "Naperville Wrestlers",
    "NL": "New Lenox",
    "Nor PD": "Norridge Pk Dist",
    "Nor": "Normal",
    "OF": "Oak Forest",
    "Or Pk": "Orland Park",
    "PPD": "Palatine Park Dist",
    "Pan": "Panthers",
    "Pk For": "Park Forest",
    "Pek": "Pekin Boys Club",
    "Plian": "Plainfield",
    "Pon": "Pontiac",
    "Raid": "Raiders",
    "Riv D": "Riverdale",
    "Riv Tr": "River Trails",
    "Ros": "Rosemont",
    "Rox": "Roxana",
    "Shab": "Shabbona",
    "Sh Ln": "Shady Lane",
    "Spring": "Springfield",
    "St V": "Stillman Valley",
    "St P": "St. Phillip Neri",
    "St T": "St. Thecla",
    "Sum H": "Summit Hill",
    "Syc": "Sycamore",
    "TP": "Tinley Park",
    "Trim": "Trimpe",
    "Troy": "Troy",
    "Urb": "Urbana",
    "Vil Pk": "Villa Park",
    "Vit PK": "Vittum Park",
    "Wal S": "Walter Sundling",
    "Ward": "Ward Middle School",
    "Wash": "Washington",
    "Wv": "Westville",
    "Wh Fr": "Wheaton/Franklin",
    "Wood Wil": "Woodrow Wilson",
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
    headshots = [image.convert("RGBA") for image in headshots]
    names = [
        Image.open(raw_root / "placers-names" / f"{weight}.jpg") for weight in weights
    ]
    names = [image.convert("RGBA") for image in names]

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
    _generate_placers_image(1978)

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
    with open(HERE / "extracted.1978.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
