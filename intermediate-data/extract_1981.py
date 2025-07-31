# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
The competitor list (from scans from Terry Weber) is contained below.
"""

import pathlib

import bracket_utils
from PIL import Image

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_COMPETITORS: dict[int, list[str | None]] = {
    50: [
        "Mike Mostek :: Moline Deere",
        "Erin McElligott :: Oak Forest",
        "Tom Buenik :: Cicero",
        "Jim Czajkowski :: Burbank :: 3",
        "Darby Waggoner :: Lawrenceville",
        "Tim Currie :: Bloomington YMCA",
        "Keith Ruiter :: Oak View :: 1",
        "Joe Reyes :: Matburns",
        "Chris Ciardetti :: Lansing",
        "Chuck Collins :: Barrington :: 6",
        "Shane Diepholtz :: Mattoon",
        "Randy Tedesco :: Belleville",
        "Sean McElligott :: Oak Forest :: 4",
        "Shawn Creasy :: Macomb",
        "Jay Ford :: Joliet YMCA",
        "Mark Smith :: Prather",
        "Dave Neybert :: Burbank :: 2",
        "Mark Pratt :: Round Lake",
        "Chris Trenhaile :: West Leyden",
        "Sean Meagher :: New Lenox Lions :: 5",
        "Travis Wise :: Freeport",
        "Brett Camden :: Fisher",
        "Tom Howard :: Dundee",
        "Rich Weeden :: Wheaton P.D.",
    ],
    55: [
        "Brian Tiemeier :: East Moline",
        "Ken Howell :: Bethalto",
        "Jeff Hollon :: Decatur",
        "Brian Moon :: Joliet YMCA :: 6",
        "John Kurtz :: Matburns :: 3",
        "Mike McElwee :: Gower",
        "Jeff Vasquez :: Barrington :: 1",
        "Andy Gardner :: Springfield",
        "Deak Baugh :: Bethalto",
        "Jim Zeilenga :: Oak Forest",
        "Larry Berndt :: Burbank",
        "Tony Chierico :: Cicero",
        "Derek Page :: Edwardsville",
        "Bruce Tiemeier :: East Moline :: 4",
        "Mark Desimone :: Dundee",
        "Chris Buenik :: Cicero :: 5",
        "Bill Wortel :: Orland Park",
        "Tim Houston :: Chicago Ridge",
        "Eric Fincham :: Urbana",
        "Jay McAlear :: Barrington",
        "Eric Denning :: Sterling YMCA",
        "Jack Maines :: Burbank",
        "Bill Walsh :: Dolton :: 2",
        "Sean Chiarodo :: Rich Township",
    ],
    60: [
        "Brian Williams :: East Moline",
        "Steve Smerz :: Franklin Park",
        "Sean Bormet :: Mokena :: 6",
        "George Bednarczyk :: Harvard",
        "Dave Donley :: Bloomington Jr.",
        "Tom Marino :: Lombard",
        "Matt Kestian :: Oak Lawn :: 2",
        "Bob Fraher :: Lombard",
        "Tom Kratz :: Matburns",
        "Craig McDougle :: Murphysboro",
        "Ray Palacious :: Troy :: 4",
        "Shane Louthan :: Mattoon",
        "Sam Geraci :: Bensenville :: 1",
        "Randy Saller :: Dolton",
        "Swopes :: Neal Jr.",
        "Brett Schultz :: Decatur",
        "Joe Herrmann :: Sycamore",
        "Mark Miller :: Prather",
        "Pat Coleman :: Burbank :: 5",
        "Mike Sheehy :: Dundee",
        "Jim Creasy :: Macomb",
        "Mike Urwin :: Orland Park :: 3",
        "Bob Shewmake :: Bi-City",
        "Jim Pellegrini :: Hazel Crest",
    ],
    65: [
        "Bobby Mena :: Sterling YMCA",
        "Pete Treadwill :: Round Lake :: 6",
        "Steve Wilcox :: Murphysboro",
        "Cory Ronk :: Urbana",
        "Bob Kaleta :: Oak Forest",
        "Ben Morris :: Bensenville",
        "Jeff Binder :: Darien",
        "Matt Averamavich :: Roxana",
        "Brian Zust :: Barrington",
        "Phil Hayes :: Orland Park :: 3",
        "Stan Beane :: Park Ridge",
        "Brian Edelen :: Tinley Park :: 1",
        "Len Ellis :: Neal Jr.",
        "Chad Roepenack :: Pekin",
        "Ryan Hager :: Sterling YMCA",
        "Jim Throw :: Dolton :: 2",
        "Eric Monte :: Gower",
        "John Peterson :: Plainfield",
        "Eric Roberson :: Roxana",
        "Scott Sheen :: Bolingbrook :: 4",
        "Don Massie :: Burbank",
        "Paul Zina :: Oak Park :: 5",
        "Matt Burright :: Rosette",
        "Robby Grayson :: Forman",
    ],
    70: [
        "Bam Bam Pustelnik :: East Moline :: 1",
        "Kris Armstrong :: Belleville",
        "Todd Carlig :: Barrington",
        "Nino Chiappetta :: Cicero",
        "Mike LaMonica :: Orland Park :: 3",
        "Joe Cascone :: Vittum Park",
        "Chuck Reed :: Forman",
        "Chad Stone :: Dundee",
        "Jeff Klotz :: Oak View",
        "Tom Ngoyen :: Wheaton P.D.",
        "Dan Walsh :: Dolton :: 5",
        "Marck Mahan :: Edwardsville",
        "Derek Smith :: Mokena :: 4",
        "Chris Welsh :: Moline Deere",  # Program says "John Deere"
        "Bill Grayson :: Forman",
        "Ron Covers :: Barrington",
        "Hugh Powers :: Lyons",
        "Joe Russo :: West Leyden",
        "Mike Walsh :: Dolton :: 2",
        "Walt Scott :: Decatur",
        "Mike Callif :: Lombard :: 6",
        "Steve Parker :: Lawrenceville",
        "Barry Alback :: Weasels",
        "Troy Settles :: Macomb",
    ],
    75: [
        "Duke Earl :: Rosette",
        "Jeff Adkins :: Decatur",
        "D. Hood :: Neal Jr.",
        "Mark Gaynor :: Tinley Park :: 2",
        "Rob Rincones :: West Chicago",
        "Toby Willis :: New Lenox Lions",
        "Craig Schwalb :: Belleville",
        "Ted Grant :: Orland Park",
        "Mike Gardner :: Springfield",
        "Matt Besler :: Park Ridge :: 4",
        "Rod Volling :: Antioch :: 6",
        "Brannon Lambert :: Gower",
        "Ken Filipiak :: Mattoon",
        "Thad Summers :: Edwardsville",
        "Dan O'Brien :: Chicago Ridge :: 5",
        "Chris Hurst :: Waldo :: 3",
        "Dino Karambelas :: Park Ridge",
        "Matt Mostek :: Moline Deere",  # Program says "Deere"
        "Ken Thompson :: Glenwood",
        "Wayne Davis :: Rock Falls",
        "Mike Chihoski :: Rosemont",
        "Ken Bishop :: Addams",
        "Dan Evensen :: Chicago Ridge :: 1",
        "Brian Hine :: Murphysboro",
    ],
    80: [
        "Scott Holbrook :: Challand :: 5",
        "Jon Martin :: Gower",
        "Brent Brumfield :: Harvard",
        "Jeff Dixon :: Roxana",
        "Bob Bonneau :: Rich Township",
        "Mike Pate :: Tinley Park",
        "Mike Cincinelli :: Rosemont",
        "John Bakis :: Big Hollow",
        "Bill Heimann :: Waldo",
        "Derold Doughty :: Mattoon :: 3",
        "Tony Ventimiglia :: Oak Forest :: 2",
        "Kevin Cooper :: Plainfield",
        "Mike Oostdyk :: Jay Stream",
        "Troy Protsman :: Macomb",
        "Jeff Schabilion :: West Leyden",
        "Steve Merrick :: Mokena",
        "Dave Ignotz :: Edwardsville",
        "Rich Harvey :: Decatur :: 6",
        "Kollin Stagnito :: Barrington",
        "John Loos :: Park Ridge :: 4",
        "Dave Baughenbaugh :: Belvidere",
        "Alan Crnich :: Oak Forest :: 1",
        "Rich Orr :: Mattoon",
        "Jeff Scott :: Grigsby",
    ],
    85: [
        "John Davis :: East Moline :: 3",
        "Jim Connolly :: Tinley Park",
        "Gary Owens :: Franklin Park",
        "Mark Becker :: Burbank :: 1",
        "Steve Knoebel :: Belleville",
        "Dan McClure :: Gibson City",
        "Craig Pallot :: Rich Township",
        "John Flanagan :: West Leyden",
        "John Crnich :: Oak Forest :: 6",
        "Calvin Knutsen :: Antioch",
        "Glen Daniels :: Champaign",
        "Rick Krug :: Prather",
        "Dean Souder :: Chicago Ridge :: 2",
        "Brett Tucker :: Sycamore",
        "Tony Marchio :: Joliet YMCA",
        "Ben Finke :: Roxana",
        "Roy Rodriguez :: Waldo",
        "R. Alex :: Big Hollow",
        "Mark Rogers :: Oak Park :: 5",
        "Bill Bembenek :: Troy",
        "Frank Herrmann :: Sycamore :: 4",
        "Tim Green :: Forman",
        "Carfagnini :: Addams",
        "Doug Hartz :: Darien",
    ],
    90: [
        "Ron Norin :: Coolidge",
        "Bill Martin :: Murphysboro",
        "Jeff Roedl :: Urbana",
        "Tom Blaha :: Mokena :: 6",
        "Matt Unterberger :: Weasels",
        "Bob Slowik :: Gower",
        "Greg Farnsworth :: Batavia :: 1",
        "Donnie Bright :: Urbana",
        "Jamie Etherton :: Murphysboro",
        "Tony Oddo :: Oak Forest",
        "Dale Klein :: Burbank :: 4",
        "Todd Cameron :: Bensenville",
        "Ken Baldwin :: Belleville",
        "George DePuy :: Challand",
        "Todd Thorpe :: Harvard",
        "Joe Chiappetta :: Cicero",
        "Mike Tisza :: Glenwood",
        "Adam Caldwell :: Hazel Crest :: 5",
        "Jeff Gardner :: Springfield :: 3",
        "Rob Vasquez :: Barrington",
        "Mark Montgomery :: Sycamore",
        "Steve Kaltofen :: Wheaton P.D.",  # Program says "Wheaton"
        "Neal Gaynor :: Tinley Park",
        "Duane Maue :: Mokena :: 2",
    ],
    95: [
        "Mark Wisdom :: Rosette",
        "Walt Wrona :: St. Tarcissus",
        "Al Drnec :: Orland Park",
        "K. Ryan :: Addams :: 3",
        "Jeff Radcliffe :: Bloomington Jr.",
        "Derrick Geich :: West Chicago :: 6",
        "Tom O'Brien :: Chicago Ridge :: 1",
        "Kurt Griesheim :: Westview",
        "Ken Cripe :: West Leyden",
        "Jim Jarman :: Prather",
        "Dave Bell :: Plainfield",
        "Mark Filipiak :: Mattoon",
        "Mike Haugen :: St. Tarcissus :: 5",
        "Dan Moore :: Oak Forest",
        "Mark Jones :: Neal Jr.",
        "Kirk Mammen :: Urbana",
        "Craig Frazier :: East Moline",
        "Jon Goff :: Edwardsville",
        "Mike Gonzales :: West Chicago :: 2",
        "M. Frey :: Big Hollow",
        "Rich Newton :: Rosette",
        "Steve Berman :: Joliet YMCA :: 4",
        "Don Carter :: Roxana",
        "Eric Phillips :: Chicago Ridge",  # Missing team name in program
    ],
    100: [
        "Jeff Mendoza :: Moline Deere :: 6",  # Program says "Deere"
        "Marty Turner :: Dundee",
        "Bob Tow :: Roxana",
        "Bob Edwards :: Pekin",
        "Ron Selby :: Oak Forest",
        "John Kane :: Matburns",
        "Jon Popp :: Burbank :: 1",
        "Roque Winchester :: Edwardsville",
        "Mark Welch :: Dundee",
        "Brian Wagnon :: Plainfield :: 4",
        "Dave Phillips :: Park Ridge",
        "Paul Dagenais :: Tinley Park",
        "Ken Sheppard :: Barrington :: 2",
        "Greg Gardner :: Springfield",
        "Dan Smith :: Moline Deere",  # Program says "Deere"
        "Ron Bednarczyk :: Tinley Park",
        "Brian Hendricks :: Gower",
        "Pete Andreotti :: Orland Park",
        "Glen March :: Prather",
        "Ron Hosford :: Plainfield :: 5",
        "Mark Vicencio :: Westview",
        "Rob Alexander :: Cicero :: 3",
        "Pat Burright :: Roselle",
        "Tony Tosh :: Bloomington Jr.",
    ],
    105: [
        "Grant Kessler :: Coolidge :: 5",
        "Mark Henry :: Edwardsville",
        "Marc Jaime :: Round Lake",
        "Eric Morrissey :: Rosemont :: 1",
        "Sean Healy :: Oak View",
        "Kurt Dietrich :: Palos South",
        "Todd Howell :: Rantoul",
        "Mike Mingle :: Barrington",
        "John DeJarld :: Troy",
        "Steve Holland :: Wheaton P.D.",  # Program says "Wheaton"
        "Greg Flores :: Chicago Ridge :: 3",
        "Chris Hall :: Roxana",
        "Mark Olsen :: Orland Park",
        "Dave Rapp :: Huntley :: 4",
        "Rich Henry :: Forman",
        "Pat Sheehy :: Dundee :: 2",
        "Matt Kramer :: Jefferson",
        "Mike Walsh :: West Leyden",
        "Rob Ledin :: Vittum Park :: 6",
        "Brian Brown :: Urbana",
        "Paul Forsberg :: Naperville",
        "Gregg Majac :: Edwardsville",
        "Steve Case :: Franklin Park",
        "Lance Nicklaus :: Challand",
    ],
    111: [
        "Matt Roach :: Rosette :: 5",
        "Matt Meyer :: Forman",
        "Tom Marschewski :: Barrington",
        "Brian Cascone :: Vittum Park :: 2",
        "Matt Heinzel :: Lyons",
        "Eddie Hicks :: Bradley",
        "Todd Cortkamp :: Murphysboro :: 4",
        "Tim Miczysak :: Oak View",
        "Kip Anderson :: Mattoon",
        "Mike Doyle :: West Leyden",
        "Bill Schuldt :: Harvard",
        "Ernesto Pretelt :: Jefferson",
        "Mark Mammen :: Urbana :: 6",
        "Rick Hawkins :: Lawrenceville",
        "Pete Pasternak :: Calumet City",  # Program says "Cal City"
        "Scott Pierre :: Wheaton P.D. :: 1",  # Program says "Wheaton"
        "Scott Gegenheimer :: Bensenville",
        "Mike Mahieu :: Moline Deere",  # Program says "Deere"
        "Joe Longhini :: Orland Park",
        "Marty Bowell :: Plano",
        "Tom Hennigan :: St. Tarcissus",
        "Dave Lehn :: Antioch",
        "Bob O'Sullivan :: Palos South :: 3",
        "Mark Rosecrans :: Roxana",
    ],
    118: [
        "Bryan Faivre :: Huntley :: 2",
        "Brandon Bily :: Jefferson",
        "Steve Skodacheck :: Harvard :: 6",
        "Mark Smith :: Roxana",
        "Steve Hale :: Rich Township",
        "Dave Walsh :: St. Barnabas",
        "Jeff Nudera :: Cicero",
        "Brian Bushy :: Dundee",
        "Willie Torres :: Waldo",
        "Mike Kelly :: Bloomington Jr.",
        "Pete Follenwieder :: Palos South",
        "Dwayne Tucker :: Glenwood :: 4",
        "Terry Navarro :: Burbank :: 1",
        "Jeff Dziekunskas :: East Moline",
        "Dan Wascher :: Sandburg",
        "Phil Marchio :: Joliet YMCA :: 5",
        "Terry Polk :: Murphysboro",
        "George Martinez :: Bloomington Jr.",
        "Bill Turner :: Dundee",
        "Mark Brooks :: Oak Park",
        "Paul Seidal :: Huntley",
        "Mike Neufeld :: Oak Forest :: 3",
        "Bill Logue :: Decatur",
        "Mike Fenoglio :: Prather",
    ],
    125: [
        "Ron Lynch :: Rosette",
        "Steve Pretto :: Hickory Hills :: 2",
        "John Kurz :: Sandburg",
        "Garry Hodonicky :: Jefferson",
        "Chris Gilliam :: Murphysboro",
        "Robbie Inskip :: Champaign",
        "Bob Kijewski :: Joliet YMCA :: 4",
        "Ken Hendrickson :: Bensenville",
        # NOTE: Assumed `Dave Walsh` scratched because `Mike Frawley` was
        #       from Palos (also Central Chicago) and he placed 5th. Other
        #       two qualifiers from Central Chicago also placed.
        # "Dave Walsh :: St. Barnabas",
        "Mike Frawley :: Palos :: 5",
        "Ski Rice :: Harvard",
        "Nick Foster :: Decatur",
        "Tim Brown :: Prather",
        "Brian Antonietti :: Calumet City :: 1",  # Program says "Cal City"
        "Don Smith :: Huntley",
        "Ron Snedic :: Plainfield",
        "Erik Anderson :: Edwardsville",
        "Louis Banuelos :: Waldo",
        "Eric Lunch :: Barrington",
        "Bill Heidrich :: St. Tarcissus :: 6",
        "Darrell Gilliam :: Huth",
        "Tony Lewis :: Challand",
        "Andy Ringer :: Bloomington Jr.",
        "D. Rowden :: Fox Lake :: 3",
        "Mike Kuefler :: Washington",
    ],
    135: [
        "Jeff Corwell :: Challand :: 4",
        "Melvin Rodgers :: Belleville",
        "Cliff Witty :: Hoopeston",
        "Scott Thomas :: Rich Township :: 5",
        "Scott Whitney :: Rosemont",
        "Bob Lukowski :: Jay Stream",
        "Steve Piron :: Batavia :: 2",
        "Mickey Clay :: Georgetown",
        "Mike Beyer :: Edwardsville",
        "Brian Morriarity :: Mt. Greenwood",
        "Elias Riviera :: Waldo",
        "Gary Rutter :: Sandburg",
        "Darrin Richardson :: Prather",
        "Carl Craig :: Challand",
        "Steve Gallaly :: Harvard",
        "Brian O'Neill :: Rosemont :: 3",
        "Tim Rath :: Huth",
        "Scott Lee :: Conrady",
        "Kevin Schudder :: Rantoul :: 6",
        "Charles Gayden :: Neal Jr.",
        "Aaron Faive :: Huntley",
        "John Cortez :: West Chicago :: 1",
        "Jim Power :: Christ the King",
        "Kevin Pearce :: Troy",
    ],
    145: [
        "Kip Westbrook :: East Moline :: 1",
        "Eric Stahmer :: Matburns",
        "Gary Ringenberg :: Oak View",
        "Jim Pattison :: Barrington",
        "Mark Williams :: Bloomington Jr.",
        "Tom Lupfer :: Lyons",
        "Curt Nehmzow :: Oak Lawn",
        "Bob Casto :: Naperville",
        "Jim Howe :: Sandburg :: 6",
        "John Michaels :: Coolidge :: 4",
        "Rich Gay :: Huth",
        "Rick Matthews :: Bloomington Jr.",
        "Mike Burke :: Matburns :: 2",
        "Tino McCabe :: Mt. Greenwood",
        "Mike Terpstra :: Harvard",
        "Myron Pender :: Decatur",
        "Derek Muller :: Huntley",
        "Dan Pullis :: Murphysboro",
        "Kurt Bednar :: Gower :: 5",
        "T. Mussel :: Addams",
        "Scott Birkett :: Rosette :: 3",
        "Juan Jodinez :: Plainfield",
        "Lester White :: Prather",
        "Jim Glynn :: Palos",
    ],
    155: [
        "Joe Traglia :: Huntley :: 5",
        "Brian Cavin :: Harvard",
        "Dan Self :: Belleville",
        "Dannell Vinson :: Decatur :: 1",
        "Al Oliver :: Lansing",
        "Bill Schoenberg :: Apollo",
        "Don Ferguson :: Naperville :: 3",
        "Mike Barton :: Roxana",
        "Tim Princing :: Antioch",
        "Jim Neal :: Plainfield",
        "John Pagan :: West Leyden",
        None,
        "Mark Schults :: Barrington :: 2",
        "Mike Razmus :: Georgetown",
        "Craig Smith :: Rosette",
        "Bill Perry :: Dolton :: 6",
        "Mike Basinger :: Lyons",
        "Mike Liberatore :: Troy",
        "Chuck Hoorman :: Roxana :: 4",
        "Scott Jewitt :: Glenwood",
        "Darrell Hunter :: Burbank",
        "Mike Rothman :: Matburns",
        "Jon Catterton :: East Moline",
        "Tony Hasbargen :: Hoopeston",
    ],
    170: [
        "Mark Conner :: Macomb",
        "Tim Moran :: Coolidge",
        "Joe Willsong :: Neal Jr.",
        "Rick Hufnus :: Sandburg :: 1",
        "Dave La Paso :: Troy",
        "Craig Pearson :: Palos",
        "Steve Bayne :: Bloomington Jr. :: 6",
        "Rich Longmire :: Big Hollow",
        "Gary Helsel :: Summit Hill",
        "Freeman Shaheen :: Jefferson",
        "Dave Blaha :: Hickory Hills :: 3",
        "Mike Dawson :: Murphysboro",
        "Ed Alexis :: Huth",
        "John Guderyon :: Freeport",
        "Rex Rexilius :: Argenta",
        "Eric Schimke :: Harvard :: 5",
        "Doug Bade :: Jay Stream",
        None,
        "Brian Krasowski :: Chicago Ridge :: 2",
        "Ken Brasher :: Urbana",
        "Tim Carmignani :: Hinsdale",
        "Tony Stanker :: Lawrenceville :: 4",
        "Mark Tamburino :: Oak Park",
        "Del Detweiler :: Freeport",
    ],
    185: [
        "Bill Smith :: Freeport :: 5",
        "Todd Smith :: Argenta",  # Program says "Argena"
        "Alex Mason :: Neal Jr.",
        "Scott Szymanski :: Conrady :: 3",
        "Mike Lambke :: Darien",
        None,
        "Joe Crawford :: Prather",
        "Chris Bartley :: Huth",
        "Norm Liles :: Rantoul",
        "Phil Messina :: Matburns :: 2",
        "Chris Buxton :: Antioch",
        None,
        "Dirrk McQueen :: Decatur",
        "Dave Kuhn :: Prather",
        "Bob Johnson :: Oak Forest",
        "Rich Manchester :: West Chicago :: 4",
        "Dan Malagoli :: Oak Park",
        "Ed Pederson :: Huntley",
        "Lee Harris :: Troy",
        "Doug Warren :: Plano",
        "Bob Hajdich :: Rosemont",
        "Pete Robson :: Dundee :: 1",
        "Nick DiCarlo :: Palos :: 6",
        "Clinton Taber :: Edwardsville",
    ],
    275: [  # Program says "UNLIMITED"
        "Frank Garza :: Challand :: 6",
        "Joe Kwasniak :: Burbank",
        "Dan Pauley :: Harvard",
        "Mike Newman :: Edwardsville",
        "Bob Meyers :: Troy",
        "Tim Noonan :: Mt. Greenwood",
        "Mike Mroczek :: Matburns :: 1",
        "Tony Rosa :: Batavia",
        "Chris Sakowski :: Burbank :: 3",
        "Dave Hart :: Decatur",
        "Scott Kerfman :: Palos",
        "Marion Lewis :: Summit Hill",
        "Rick Surma :: Naperville",
        "Mike McFadden :: Sycamore",
        "Louie Tamez :: Oak Park :: 2",
        "James Washington :: Rich Township :: 4",
        "Rip Tomlinson :: Murphysboro",
        "Jeff Huskisson :: Pekin",
        "Adams Evans :: Neal Jr.",
        "Paul Soto :: Bensenville",
        "Scott Bemis :: Huntley",
        "Frank Pesole :: Vittum Park :: 5",
        "Buff Clark :: Buffalo",
        "Tom Richmond :: Prather",
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Burbank": 195.0,  # BURBANK PANTHERS
    "Chicago Ridge": 145.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Swopes", "Neal Jr."): bracket_utils.Competitor(
        full_name="Swopes",
        first_name="",
        last_name="Swopes",
        team_full="Neal Jr.",
    ),
    ("Bam Bam Pustelnik", "East Moline"): bracket_utils.Competitor(
        full_name="Bam Bam Pustelnik",
        first_name="Bam Bam",
        last_name="Pustelnik",
        team_full="East Moline",
    ),
    ("Carfagnini", "Addams"): bracket_utils.Competitor(
        full_name="Carfagnini",
        first_name="",
        last_name="Carfagnini",
        team_full="Addams",
    ),
    ("Dave La Paso", "Troy"): bracket_utils.Competitor(
        full_name="Dave La Paso",
        first_name="Dave",
        last_name="La Paso",
        team_full="Troy",
    ),
}


def _get_bout_numbers() -> dict[bracket_utils.MatchSlot, int]:
    return {
        "championship_r32_02": 1,
        "championship_r32_04": 2,
        "championship_r32_06": 3,
        "championship_r32_08": 4,
        "championship_r32_10": 5,
        "championship_r32_12": 6,
        "championship_r32_14": 7,
        "championship_r32_16": 8,
        "consolation_fifth_place": 35,
        "consolation_third_place": 36,
        "championship_first_place": 37,
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
    all_weights = set(_SENIOR_COMPETITORS.keys())
    weights = sorted(all_weights)

    raw_root = _HERE.parent / "raw-data" / str(year)
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

    static_dir = _HERE.parent / "static" / "static" / "images"
    save_location = static_dir / f"{year}-senior-placers.png"
    final_img.save(save_location)


def main():
    _generate_placers_image(1981)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, competitors in _SENIOR_COMPETITORS.items():
        bout_numbers = _get_bout_numbers()
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
    with open(_HERE / "extracted.1981.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
