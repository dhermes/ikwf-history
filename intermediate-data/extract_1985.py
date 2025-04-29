# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    55: [
        bracket_utils.Placer(name="Ryan Ferguson", team="Lancers"),
        bracket_utils.Placer(name="Ryan Meagher", team="New Lenox Lions"),
        bracket_utils.Placer(name="Cory Daker", team="Foreman"),
        bracket_utils.Placer(name="Len Jankowski", team="Vittum Cats"),
        bracket_utils.Placer(name="Joey O'Sullivan", team="Colts W.C."),
        bracket_utils.Placer(name="Jerry Delira", team="Lan-Oak P.D. Wrest."),
    ],
    60: [
        bracket_utils.Placer(name="Jim Soldan", team="Frankfort Falcons"),
        bracket_utils.Placer(name="Eric Carter", team="Roxana P.D. Roughnecks"),
        bracket_utils.Placer(name="Randy Berke", team="DeKalb Huntley"),
        bracket_utils.Placer(name="Dave Kinsey", team="Joliet YMCA Wrest."),
        bracket_utils.Placer(name="Nick Cina", team="Belvidere YMCA Bandits"),
        bracket_utils.Placer(name="Tom Canagan", team="Vittum Cats"),
    ],
    65: [
        bracket_utils.Placer(name="Rich Weeden", team="Villa Lombard"),
        bracket_utils.Placer(name="Brent Laroche", team="Panther WC"),
        bracket_utils.Placer(name="Dan Gilbert", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Gene Bonnette", team="Pekin"),
        bracket_utils.Placer(name="Kurt Kalchbrenner", team="Vittum Cats"),
        bracket_utils.Placer(name="Jason LeMonier", team="Lan-Oak P.D. Wrest."),
    ],
    70: [
        bracket_utils.Placer(name="Ken Gerdes", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Kelly Hamill", team="Belvidere YMCA Bandits"),
        bracket_utils.Placer(name="Mike Elerman", team="Colts W.C."),
        bracket_utils.Placer(name="Dan Pargulski", team="Arlington Hghts. W.C."),
        bracket_utils.Placer(name="Timothy Currie", team="Redbird W.C."),
        bracket_utils.Placer(name="Jim Pesavento", team="Oak Forest Warriors"),
    ],
    75: [
        # `Ricky Harris`
        bracket_utils.Placer(name="Richard Harris", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Dave Neybert", team="Panther WC"),
        bracket_utils.Placer(name="Chris Buenik", team="Vittum Cats"),
        bracket_utils.Placer(name="Todd Ryan", team="Bensenville"),
        bracket_utils.Placer(name="Andrew Gardner", team="Lanphier-Southeast W.C."),
        bracket_utils.Placer(name="Tony Chierico", team="Vittum Cats"),
    ],
    80: [
        bracket_utils.Placer(name="Doug Hayes", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Scott Garelli", team="Villa Lombard"),
        bracket_utils.Placer(name="Shelly Resendez", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Dan Willis", team="New Lenox Lions"),
        bracket_utils.Placer(name="Tom Derro", team="Panther WC"),
        bracket_utils.Placer(name="Tom Buenik", team="Vittum Cats"),
    ],
    85: [
        bracket_utils.Placer(name="Mike Dusel", team="Villa Lombard"),
        bracket_utils.Placer(name="Dan Mahler", team="Oak Park-River Forest"),
        bracket_utils.Placer(name="Jim Czajkowski", team="Panther WC"),
        bracket_utils.Placer(name="Scott Miedona", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Chad Mueller", team="Champaign"),
        bracket_utils.Placer(name="John St.Clair", team="Rich Wrestling Ltd."),
    ],
    90: [
        bracket_utils.Placer(name="Sean Bormet", team="Frankfort Falcons"),
        bracket_utils.Placer(name="Stan Valle", team="Crusaders W.C."),
        bracket_utils.Placer(name="Dante Federighi", team="Vittum Cats"),
        bracket_utils.Placer(name="Jim Regan", team="Vittum Cats"),
        bracket_utils.Placer(name="Jim Hunziker", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Chad Hamilton", team="Roxana P.D. Roughnecks"),
    ],
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
        bracket_utils.Placer(name="George Hoffman", team="Joliet YMCA Wrest."),
        bracket_utils.Placer(name="Randy Saller", team="Dolton Falcons"),
        bracket_utils.Placer(name="Matt Cruszka", team="Indian Prairie"),
        bracket_utils.Placer(name="Andrew Larson", team="East Moline W.C."),
        bracket_utils.Placer(name="Dirk Dorn", team="Naperville Warhawks"),
    ],
    105: [
        bracket_utils.Placer(name="Ryan Shafer", team="Warrior W.C."),  # Sterling?
        bracket_utils.Placer(name="Steven Smerz", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="Patrick Henley", team="Harvey P.D. Twisters"),
        bracket_utils.Placer(name="Bob Bartkowaik", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Matt Rademaker", team="Illini Bluffs W.C."),
        bracket_utils.Placer(name="Sock Woodruff", team="Deerpath W.C."),
    ],
    111: [
        bracket_utils.Placer(name="John Granat", team="Vittum Cats"),
        bracket_utils.Placer(name="Jim Filipiak", team="Mattoon W.C."),
        bracket_utils.Placer(name="Tim Murphy", team="Belvidere YMCA Bandits"),
        bracket_utils.Placer(name="Robby Grayson", team="Foreman"),
        bracket_utils.Placer(name="Don Wicker", team="Harvard W.C."),
        bracket_utils.Placer(name="John Gagne", team="Villa Lombard"),
    ],
    118: [
        bracket_utils.Placer(name="Joe Gilbert", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Pat Gallagly", team="Harvard W.C."),
        bracket_utils.Placer(name="Sean McKeon", team="Unity Youth W.C."),
        bracket_utils.Placer(name="Jeffery Rosas", team="Generals W.C."),
        bracket_utils.Placer(name="Jim Collin", team="DeKalb Huntley"),
        bracket_utils.Placer(name="Don Neece", team="Rockridge Jr. High"),
    ],
    125: [
        bracket_utils.Placer(name="Paul Andreotti", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Lance Pelton", team="New Lenox Lions"),
        bracket_utils.Placer(name="Tim Major", team="Batavia W.C."),
        bracket_utils.Placer(name="Rich Fenoglio", team="Granite City-Coolidge"),
        bracket_utils.Placer(name="Shawn Willett", team="Warrior W.C."),
        bracket_utils.Placer(name="Shawn Muluaney", team="Rockridge Jr. High"),
    ],
    135: [
        bracket_utils.Placer(name="Chuck Sparks", team="Granite City-Coolidge"),
        bracket_utils.Placer(name="Steve Hartmann", team="Harvard W.C."),
        bracket_utils.Placer(name="David DiCarlo", team="Rich Wrestling Ltd."),
        bracket_utils.Placer(name="Craig Manz", team="Panther WC"),
        bracket_utils.Placer(name="Scott Ewing", team="Rockridge Jr. High"),
        bracket_utils.Placer(name="Kyle Kennedy", team="Rosemont Cobra"),
    ],
    145: [
        bracket_utils.Placer(name="Kevin Nolan", team="Colts W.C."),
        bracket_utils.Placer(name="Dean McWilliams", team="Vittum Cats"),
        bracket_utils.Placer(name="Matt Rood", team="Villa Lombard"),
        bracket_utils.Placer(name="Russell Davis", team="Chicago Ridge P.D."),
        bracket_utils.Placer(name="Marcus Adkins", team="Edwardsville W.C."),
        bracket_utils.Placer(name="Kyle Field", team="Youth Razorbacks"),
    ],
    155: [
        bracket_utils.Placer(name="Mike Manganiello", team="Vittum Cats"),
        bracket_utils.Placer(name="John Fiduccia", team="Bensenville"),
        bracket_utils.Placer(name="Jehad Hamdan", team="Lemont W.C."),
        bracket_utils.Placer(name="Derek Grable", team="Wilbur Trimpe Jr. High"),
        bracket_utils.Placer(name="James Newland", team="Morton Youth W.C."),
        bracket_utils.Placer(name="Darin Chambliss", team="Catlin W.C."),
    ],
    170: [
        bracket_utils.Placer(name="Sherif Zegar", team="Panther WC"),
        bracket_utils.Placer(name="Bill Johnson", team="Edwardsville W.C."),
        bracket_utils.Placer(name="Bradley George", team="St. Tarcissus Raiders"),
        bracket_utils.Placer(name="Craig Wall", team="Wilbur Trimpe Jr. High"),
        bracket_utils.Placer(name="Gilbert Rivera", team="Eisenhower"),
        bracket_utils.Placer(name="Chris Gadziak", team="Hickory Hills P.D."),
    ],
    185: [
        bracket_utils.Placer(name="Randy Scianna", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Brian Myers", team="Elgin W.C."),
        bracket_utils.Placer(name="Eric Keizer", team="Matburns W.C."),
        bracket_utils.Placer(name="Dave Day", team="Indian Trail-Plainfield"),
        bracket_utils.Placer(name="Charles Hisel", team="Bradley Bourbonnais W.C."),
        bracket_utils.Placer(name="Bill Dietz", team="Murphysboro Jr. High"),
    ],
    275: [
        bracket_utils.Placer(name="Andy Grimm", team="Villa Lombard"),
        bracket_utils.Placer(name="Todd Martins", team="Belvidere YMCA Bandits"),
        bracket_utils.Placer(name="Jason HillSelph", team="Carbondale Park Dist."),
        bracket_utils.Placer(name="Tim Honn", team="Jefferson"),
        bracket_utils.Placer(name="Rich Allison", team="Rich Wrestling Ltd."),
        bracket_utils.Placer(name="Jeff Carlson", team="Machesney Park Indp."),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Vittum Cats": 287.0,
    "Panther WC": 174.0,
    "Villa Lombard": 164.0,
    "Oak Forest Warriors": 133.0,
    "Tinley Park Bulldogs": 111.0,
    "Belvidere YMCA Bandits": 95.0,
    "Rich Wrestling Ltd": 93.0,
    "Colts WC": 87.0,
    "New Lenox Lions": 72.5,
    "Frankfort Falcons": 69.0,
    "Warrior WC": 68.0,
    "Harvard WC": 67.5,
    "Wilbur Trimpe Jr. High": 63.5,
    "DeKalb Huntley": 62.0,
    "Orland Park Pioneers": 58.5,
    "Granite City-Coolidge": 54.5,
    "Roxana PD Roughnecks": 54.5,
    "Rockridge Jr. High": 52.0,
    "Joliet YMCA Wrest": 51.0,
    "Harvey PD Twisters": 50.5,
    "Bensenville": 49.0,
    "Foreman": 44.0,
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
    "Carbondale Park Dist": 27.0,
    "Dolton Falcons": 27.0,
    "St. Tarcissus Raiders": 27.0,
    "East Moline WC": 26.5,
    "Franklin Park Raiders": 25.5,
    "Jefferson": 25.5,
    "Unity Youth WC": 25.0,
    "Lan-Oak PD West": 22.5,
    "Generals WC": 21.5,
    "Illini Bluffs WC": 21.5,
    "Chicago Ridge PD": 21.0,
    "Lanphier-Southeast WC": 21.0,
    "Lemont WC": 21.0,
    "Arlington Hgts WC": 20.5,
    "Crusaders WC": 20.0,
    "Mattoon WC": 20.0,
    "Champaign": 19.5,
    "Catlin WC": 19.0,
    "Lockport Grapplers": 19.0,
    "Murphysboro Jr. High": 19.0,
    "Belleville L'l Devils": 18.0,
    "Indian Prairie": 18.0,
    "Rosemont Cobra": 18.0,
    "Eisenhower": 17.0,
    "Fisher WC": 16.0,
    "Machesney Park Indp.": 16.0,
    "Deerpath WC": 15.5,
    "Pekin": 15.0,
    "Redbird WC": 15.0,
    "Morton Youth WC": 14.5,
    "Blackhawk WC": 14.0,
    "Hoopeston East Lynn": 14.0,
    "Stickers": 13.0,
    "Youth Razorbacks": 13.0,
    "Clinton Rosette MS": 12.5,
    "Palos South": 12.5,
    "Newman Middle School": 12.0,
    "Round Lake Area PD": 12.0,
    "Naperville Warhawks": 11.0,
    "Antioch Upper Grade": 10.5,
    "Danville Youth WC": 10.5,
    "Geneseo WC": 10.0,
    "Naperville Warriors": 10.0,
    "Peotone Park Dist.": 8.0,
    "Dundee Highlanders": 7.5,
    "Gower": 6.5,
    "Barrington Broncs": 6.0,
    "Mt. Zion WC": 6.0,
    "Georgetown": 5.0,
    "Gibson City Youth": 4.5,
    "Wheaton Falcons": 4.5,
    "Aurora Tomcats": 4.0,
    "Bethalto Boys Club": 4.0,
    "Bismarck-Henning WC": 4.0,
    "Hinsdale": 4.0,
    "Marquart": 4.0,
    "Rock Island 1": 4.0,
    "Urbana Kids Club": 4.0,
    "Sandwich": 3.0,
    "Midlothian PD Braves": 2.5,
    "Panther Kids": 2.0,
    "Taylorville WC": 2.0,
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
    all_weights = set(_SENIOR_PLACERS.keys())
    weights = sorted(all_weights)

    raw_root = HERE.parent / "raw-data" / str(year)
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

    static_dir = HERE.parent / "static" / "static" / "images"
    save_location = static_dir / f"{year}-senior-placers.png"
    final_img.save(save_location)


def main():
    _generate_placers_image(1985)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
        )

        if weight == 85:
            _, _, match_5th = weight_class.matches
            match_5th.bottom_competitor.full_name = "John St. Clair"
            match_5th.bottom_competitor.last_name = "St. Clair"

        if weight == 275:
            _, match_3rd, _ = weight_class.matches
            match_3rd.top_competitor.full_name = "Jason Hill Selph"
            match_3rd.top_competitor.last_name = "Hill Selph"

        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1985.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
