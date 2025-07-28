# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
The competitor list (from scans from Terry Weber) is contained below.

Note that 95, 100, and 105 are missing from the placer lists because those
pages were missing from the 1985 program.
"""

import pathlib

import bracket_utils
from PIL import Image

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_COMPETITORS: dict[int, list[str | None]] = {
    50: [
        "Dan Collins :: Barrington Colts",
        "John Stanley :: Mattoon",
        "Mike Erffmeyer :: Lan Oak",
        "Ryan Meagher :: New Lenox :: 2",
        "Justin Webber :: West Chicago",
        "Brian Davis :: Sterling Newman",
        "Len Jankowski :: Vittum Cats :: 4",
        "Mike Triola :: Tinley Park :: 6",
        "Chad Red :: Danville",
        "Mike Dickinson :: Roxana Park District",
        "Tom Grennan :: Sterling Newman",
        "Stacy Leach :: Eisenhower",
        "Cory Daker :: Foreman :: 5",
        "Steve Vasquez :: Barrington Colts",
        "Jason Kolecke :: Vittum Cats",
        "Ryan Ferguson :: Lancer W.C. :: 1",
        "Jo Jo Fleming :: Rich Township",
        "Joe Flanigan :: Little Comanches",
        "Joe O'Sullivan :: Mt. Greenwood :: 3",
        "Dan Neybert :: Burbank",
        "Mike Kearby :: Round Lake",
        "Boyd Stropes :: Aledo",
        "Steve Dickinson :: Roxana Park District",
        "Ernie Lopez :: Lockport",
    ],
    55: [
        "Nick Cina :: Belvidere",
        "Chris Wiehle :: Bensenville",
        "Randy Berke :: DeKalb / Huntley",
        "Robert Chihoski :: Rosemont :: 2",
        "Tom Hincks :: Mt. Greenwood",
        "Dave Kinsey :: Joliet YMCA :: 4",
        "Bryant Thomas :: Belleville :: 5",
        "Tad Taylor :: East Moline",
        "Jim Virnich :: Lancer W.C.",
        "Peter Stanley :: Mattoon",
        "Josh Mattio :: Rich Township",
        "Roy Brazeav :: Lan Oak",
        "Ferde Deguszman :: Gower",
        "Rick Kitsemble :: Belvidere",
        "Jason Johnson :: Roxana Park District",
        "Todd Kelley :: Dolton",
        "Dan Walters :: Burbank :: 3",
        "Mike French :: Mattoon",
        "Mike Mena :: Sterling Newman",
        "Eric Carter :: Roxana Park District",
        "Janil Swift :: Barrington Colts",
        "Jim Soldan :: Frankfort :: 1",
        "Philip Schwing :: Fisher :: 6",
        "Jeff Kennedy :: Rosemont",
    ],
    60: [
        "Ryne Radosh :: Barrington Colts",
        "Dan Gilbert :: Tinley Park :: 4",
        "Keith Snyder :: Burbank",
        "Ryan Smith :: Roxana Park District",
        "Louie Montez :: Geneseo",
        "Curt Bellone :: Palos",
        "Gene Bonnette :: Pekin",
        "Jay Ford :: New Lenox",
        "Jason Leminier :: Lan Oak",
        "Doug Sawyer :: West Chicago :: 6",
        "Brent LaRoche :: Burbank :: 1",
        "Mike Cliffe :: DeKalb / Rosette",
        "Jim Pesavento :: Oak Forest :: 3",
        "Aaron Rodis :: Decatur YMCA",
        "Steve Kuhl :: Roxana Park District",
        "Steve Hawkins :: Rock Island (I)",
        "Jay Hanson :: Cardinal Wrestling",
        "Josh Bulak :: Eisenhower",
        "Luke Pascale :: Orland Park :: 5",
        "Randy Deeke :: Belleville",
        "Chad Easterberg :: Round Lake",
        "Kurt Kalchbrenner :: Vittum Cats :: 2",
        "Duffy Daugherty :: Wheaton Falcons",
        "Randy Pierce :: Rantoul",
    ],
    65: [
        "Kelly Hamill :: Belvidere",
        "Darby Waggoner :: Lawrenceville",
        "Chris Perry :: Lancer W.C.",
        "Eric Denning :: Sterling Newman",
        "Eric Hermann :: Peoria Razorbacks",
        "Mike Eierman :: Mt. Greenwood :: 4",
        "Ken Gerdes :: Orland Park :: 2",
        "Todd Ryan :: Bensenville :: 5",
        "Randy Tedesco :: Belleville",
        "Tom Derro :: Burbank",
        "Sean McElligott :: Oak Forest",
        "Tim Currie :: Redbirds",
        "Jason Warner :: Roxana Park District",
        "Andy Neal :: DeKalb / Huntley",
        "John Gladish :: Barrington Colts",
        "Andy Gardner :: Lanphier South East :: 1",
        "Jeff Turay :: Rich Township",
        "Steve Gerstung :: Arlington (AR)",
        "Rich Weeden :: Villa-Lombard",
        "Tom Buenik :: Vittum Cats :: 6",
        "Brian Dadigan :: New Lenox",
        "Rick Harris :: Tinley Park :: 3",
        "Martin Sanchez :: Belvidere",
        "Shay Cordes :: East Moline",
    ],
    70: [
        "Mark Olbrich :: Harvard :: 6",
        "Nick Morrocco :: Lancer W.C.",
        "Heath Baedon :: Bethalto",
        "Shelly Resendez :: Oak Forest :: 4",
        "Tony Haubner :: Rosemont",
        "Todd Oliver :: Mt. Zion",
        "Cass Lundgren :: DeKalb / Huntley",
        "Jerry Hold :: Edwardsville",
        "Joe Reyes :: Matburns",
        "Dan Willis :: New Lenox :: 2",
        "Mike Goodale :: Pekin",
        "Brian Clark :: Naperville W.C.",
        "Chris Buenik :: Vittum Cats :: 1",
        "Chuck Collins :: Barrington Colts",
        "Joe Verlinden :: East Moline",
        "Jeff Killebrew :: Murphysboro",
        "George Strnad :: Plainfield",
        "Bill Walsh :: Mt. Greenwood :: 3",
        "Priest Wilson :: Danville",
        "Daryl Grennan :: Sterling Newman",
        "Mike Kelly :: Joliet YMCA",
        "Mike Ducel :: Glencrest",
        "Jim Zeilenga :: Oak Forest :: 5",
        "Todd Williams :: Barrington Colts",
    ],
    75: [
        "Matt Bartlett :: St. Charles :: 2",
        "Phil Fuhr :: Rockridge",
        "Jim Revelle :: Granite City / Grigsby",
        "Eric Fincham :: Urbana Knights",
        "Kurt Buhle :: Joliet YMCA",
        "Frank Arado :: Crusaders",
        "Brian Abraham :: Lancer W.C. :: 6",
        "Jim Czajkowski :: Burbank",
        "Raymond Olalde :: Sterling Newman",
        "Doug Hayes :: Oak Forest :: 3",
        "Derek Baugh :: Bethalto",
        "Bill Wortel :: Orland Park",
        "Jim Creasy :: Macomb",
        "Scott Garelli :: Bensenville",
        "Marvin Fitzwater :: Danville",
        "Sean Bormet :: Frankfort :: 1",
        "Scott Miedona :: Tinley Park",
        "Troy Robertson :: Barrington Colts",
        "Dan Mahler :: Oak Park :: 5",
        "Mark Arneson :: Rochelle",
        "Ed Minet :: Mt. Greenwood",
        "Chad Hamilton :: Roxana W.C. :: 4",
        "Jeff Hollon :: Decatur YMCA",
        "Todd Haskin :: Villa-Lombard",
    ],
    80: [
        "Jeff Vasquez :: Barrington Colts :: 2",
        "Brian Ezell :: Frankfort",
        "Brian Harrison :: Murphysboro",
        "Dave Fialka :: West Chicago",
        "Pete Schultz :: Oak Park",
        "Greg Liestman :: Fisher",
        "Jim Hunziker :: Oak Forest",
        "Jason Slayden :: Roxana W.C.",
        "C.J. Flores :: Plainfield",
        "Ryan Hager :: Sterling Red Birds :: 5",
        "Bill Griffis :: Peoria Razorbacks",
        "Billy O'Brien :: Burbank :: 3",
        "Sean Chiardo :: Rich Township",
        "Charlie Schnieder :: Dundee",
        "Dave Campbell :: Dolton :: 6",
        "Paul Zina :: Franklin Park :: 1",
        "Darren Ferguson :: Lancer W.C.",
        "Paul Swartsbock :: Sycamore",
        "Joe Abegg :: Belleville",
        "Tim Houston :: Chicago Ridge :: 4",
        "Tony Mills :: Harvard",
        "Kevin Denton :: Westville",
        "Tom Pyle :: Plano",
        "Scott Abraham :: Lancer W.C.",
    ],
    85: [
        "Mike Sheehy :: Dundee :: 5",
        "Wade Ryan :: Bradley Bourbonnais",
        "Randy Saller :: Dolton",
        "George Hoffman :: Joliet YMCA",
        "Jeff Yepez :: Bensenville",
        "Eric Weinert :: Rockridge",
        "Steve Smerz :: Franklin Park :: 2",
        "Dave Pericak :: Tinley Park",
        "Cory Deck :: Urbana Knights",
        "Richard Kalina :: Murphysboro",
        "Ryan Schafer :: Sterling Red Birds :: 4",
        "Brett Janis :: Lancer W.C.",
        "Ron Ruzic :: Lanphier South East",
        "Jesse Turner :: Dundee",
        "Jim Regan :: Vittum Cats",
        "Matt Gurszka :: Indian Prairie :: 1",
        "Bryan Bruns :: New Lenox",
        "Chip Fenoglio :: Granite City / Coolidge",
        "Pat Henley :: Harvey",
        "Stan Valle :: Park Ridge :: 6",
        "Dave Shepard :: Antioch",
        "William Gay :: Rock Island (II) :: 3",
        "Terrell Kempfer :: Murphysboro",
        "Jeff Cordova :: Lockport",
    ],
    90: [
        "Todd Carlig :: Barrington Colts",
        "Phil Esposito :: Gower",
        "Mike Coleman :: Geneseo",
        "Paul LeKousis :: Vittum Cats :: 2",
        "Mike Krause :: Oak Forest",
        "Pete Porzio :: Orland Park",
        "Jeff Tindall :: Granite City / Coolidge",
        "Lance Earl :: DeKalb / Rosette :: 6",
        "Mike Schwartz :: Lancer W.C.",
        "Rob Grayson :: Foreman",
        "Robbie Jeffrey :: Rich Township :: 4",
        "Greg Crnich :: Oak Forest",
        "Sam Geraci :: Lancer W.C. :: 1",
        "Rick Umland :: Harvard",
        "Jeremy Ufert :: Roxana Park District",
        "Todd Schmittel :: Lan Oak",
        "Bill Guide :: Vittum Cats",
        "Gunner Schwing :: Fisher",
        "Joe Herrmann :: Sycamore :: 3",
        "Brett Davis :: Granite City / Grigsby",
        "Tom Arneson :: Rochelle",
        "Scott Richardson :: New Lenox :: 5",
        "Chad Robpenack :: Pekin",
        "D. Spagnola :: Matburns",
    ],
    95: [
        "Jerry Chapman :: Round Lake",
        "Don Seban :: Chicago Ridge",
        "Max Smith :: Franklin Park",
        "Matt Auramovich :: Roxana W.C.",
        "Dennis Vesely :: Rock Island (I)",
        "Scott Flores :: Plainfield",
        "Bryon Schultz :: Lanphier South East :: 1",
        "Paul Andreotti :: Orland Park",
        "Mike McInnes :: Mt. Greenwood",
        "Dennis Donovan :: Villa-Lombard",
        "Jerry Simek :: Vittum Cats",
        "Brian Williams :: East Moline",
        "Joe Adamson :: Lan Oak",
        "Shane Anderson :: Decatur YMCA",
        "Steve Wilcox :: Murphysboro",
        "Nate Booth :: Geneseo",
        "Bill Eves :: Antioch",
        "Willie Diaz :: Indian Prairie",
        "Toby Willis :: New Lenox",
        "Byron Overton :: Bethalto",
        "Jim Kossakowski :: Dundee",
        "Sean Harrity :: St. Tarcissus",
        "John Gagne :: Villa-Lombard",
        "Rick Stroh :: Gibson City",
    ],
    100: [
        "Walter Sanabria :: Barrington Colts",
        "John Churchill :: Belleville",
        "P.J. Manzari :: Gower",
        "Dan Creger :: Sherrard",
        "Mike Anderson :: Hoopeston",
        "John Eierman :: Mt. Greenwood",
        "Shawn Kinder :: Joliet YMCA",
        "Peter Gamborinno :: Lancer W.C.",
        "Tim Johnston :: Marian Wildcats",
        "Jeff Jacobucci :: Crusaders",
        "T.C. Dantzler :: Harvey",
        "Jim Filipiak :: Mattoon",
        "Chad Carpenter :: Granite City / Coolidge",
        "Don Neece :: Rockridge",
        "Don Wicker :: Harvard",
        "Bret Schultz :: Lanphier South East :: 1",
        "Greg Olsen :: Orland Park",
        "Pete Heitrich :: St. Tarcissus",
        "Kip Hennelly :: Jefferson",
        "Paul Barnes :: Burbank",
        "Paul Katzman :: Palos",
        "Joe Gilbert :: Tinley Park",
        "Jack Wright :: Dundee",
        "Jason Arnold :: Aledo",
    ],
    105: [
        "Chad Stone :: Dundee",
        "Brian Gilbert :: Carol Stream",
        "Mark Bromlet :: Roxana W.C.",
        "Jim Mackowiak :: Tinley Park",
        "B. Rybak :: Oak Park",
        "Brian Hood :: Decatur YMCA",
        "Bob Mena :: Sterling Newman :: 1",
        "Scott Marks :: Granite City / Grigsby",
        "John Murabito :: Burbank",
        "Tim Chaplin :: Joliet YMCA",
        "Tony Bonic :: Mattoon",
        "Santiago Rios :: Naperville Warhawks",
        "Pat O'Malley :: Oak Park",
        "Erin Bell :: St. Charles",
        "Kevin Beasley :: DeKalb / Huntley",
        "Craig Schwab :: Belleville",
        "Randy Flores :: Frankfort",
        "Tom Strilko :: Mt. Greenwood",
        "Matt Madsen :: Urbana Kids",
        "Greg Lane :: Rockridge",
        "Dan Sudsberry :: Joliet YMCA",
        "John Hennessey :: Villa-Lombard",
        "Geoff Kwiatt :: Oak Forest",
        "Dave Blanke :: Barrington Colts",
    ],
    111: [
        "Craig Goodchild :: Dundee :: 1",
        "Scott Ewing :: Rockridge",
        "Mark Mitchell :: Murphysboro",
        "Dave Flies :: Decatur YMCA",
        "Les Quade :: New Lenox",
        "B. Kolwalski :: Hillside",
        "Mike Bunning :: Glencrest :: 6",
        "Steve Smith :: J.A. Stickers",
        "Bob Schaffer :: Plano",
        "Tom Salvino :: Mt. Greenwood :: 3",
        "Kris Armstrong :: Belleville",
        "Pat O'Sullivan :: Palos",
        "Brock Rude :: Sterling Newman",
        "Jim Nowak :: Gower",
        "Bill Grayson :: Foreman",
        "Steve Cowan :: Joliet YMCA :: 2",
        "Bill Clemente :: Hickory Hills",
        "Tim Sandrick :: Antioch",
        "Joe Cortese :: Matburns :: 5",
        "Dale Law :: Round Lake",
        "Eric Boghasian :: Chicago Ridge",
        "Rich Fenoglio :: Granite City / Coolidge :: 4",
        "Brad Reardon :: Peoria Razorbacks",
        "Jim Ferguson :: Naperville Warhawks",
    ],
    118: [
        "Larry Logan :: Barrington Colts :: 1",
        "Mike Kelly :: Lemont",
        "Bob Thomas :: Granite City / Grigsby",
        "Roger Matson :: Naperville Patriots",
        "R. Robinson :: Carl Sandburg",
        "Mike Tison :: Catlin W.C.",
        "Kevin Nolan :: Mt. Greenwood",
        "John Talbot :: Carbondale Park District",
        "Matt Piotrowski :: Plainfield",
        "Shawn Willett :: Sterling Challand :: 4",
        "Steve Helton :: Mattoon :: 6",
        "Dan Hansen :: Franklin Park",
        "Victor Blackful :: Rich Township :: 2",
        "Corey Laws :: Belvidere",
        "Mike Stringer :: Dolton",
        "Bill Faley :: Burbank",
        "Jack Gieck :: Tomcat W.C.",
        "Bret Milburn :: DeKalb / Rosette :: 5",
        "Brad Stockstill :: Bethalto :: 3",
        "Todd Auther :: Tinley Park",
        "Pat Hood :: Barrington Colts",
        "Dan Ritchie :: Pekin",
        "Lee Encapera :: Sherrard",
        "Pete Schubel :: Naperville W.C.",
    ],
    125: [
        "Brad Demmett :: Dundee",
        "Evan Erickson :: Rantoul",
        "Rich Bielik :: Hickory Hills :: 5",
        "Greg Stopka :: Frankfort",
        "Auggie Considine :: Villa-Lombard",
        "Shawn O'Neil :: Rockridge :: 3",
        "Bill Novak :: Burbank :: 1",
        "Mark Anderson :: Tinley Park",
        "Dave Mayberry :: Morton",
        "Demetrius Bennett :: East St. Louis",
        "Bud Bennington :: Geneseo",
        "Rich Julian :: Naperville Warhawks",
        "Dan Tunkay :: Champaign :: 4",
        "Eric Wapole :: Barrington Colts",
        "M. Steelye :: Lions W.C. :: 6",
        "Jeff Burkovsky :: Eisenhower",
        "Adam Gurra :: Palos",
        "Marcus Adkins :: Edwardsville",
        "Maurice Mance :: Harvey :: 2",
        "E. Hoffman :: Carl Sandburg",
        "Brandon Parkhurst :: Antioch",
        "Curt Mallory :: DeKalb / Rosette",
        "Jim Stout :: Granite City / Grigsby",
        "Bob Burke :: Plainfield",
    ],
    135: [
        "Gary Dean :: Rochelle :: 3",
        "Tony Rios :: Tomcat W.C.",
        "Brady Santamor :: Jordan",
        "Karl Cloherty :: St. Tarcissus",
        "Phil O'Connell :: Hickory Hills",
        "Ken Courtright :: Palos",
        "Tim Melosei :: Roxana W.C.",
        "Steve Pearson :: Rockridge",
        "Mark Fiore :: Marquardt Jr. High",
        "Richard Harvey :: Decatur YMCA :: 1",
        "Dan Oswald :: Lockport :: 6",
        "Keith Colbert :: Tinley Park",
        "Jack Schomig :: Wheaton Falcons :: 2",
        "Chris Ladd :: Barrington Colts",
        "Terry Arnold :: Roxana W.C.",
        "Sherman Adams :: Harvey",
        "Joe Gomez :: Burbank",
        "Rob Hammer :: Peoria Razorbacks",
        "Tim Hinson :: Rockridge :: 4",
        "Joe Singleton :: Murphysboro",
        "Jason Kleckner :: Harvard",
        "Charlie England :: Plainfield :: 5",
        "Scott Balsaniello :: Westville",
        "Anthony Belcaster :: Vittum Cats",
    ],
    145: [
        "Tim Propeck :: Cardinal Wrestling :: 2",
        "Jim Meagher :: Dolton",
        "Kevin Collins :: Vittum Cats",
        "Terry Stanley :: Granite City / Coolidge",
        "Scott Montavon :: DeKalb / Rosette",
        "Mike Grauer :: Palos",
        "Brandon Bilyard :: Bradley Bourbonnais :: 4",
        "John Ivlow :: Plainfield :: 5",
        "Jim Kurek :: Tinley Park",
        "Eric Kuehl :: Gower",
        "J. Olson :: Hillside",
        "Corey McDaniel :: Sherrard",
        "John Kristian :: Dolton",
        "Kevin Cooper :: Decatur YMCA",
        "Rusty Davis :: Granite City / Grigsby",
        "Tony Bolpes :: Rockridge :: 3",
        "Brenden Hannigan :: Antioch",
        "Steve Surma :: Naperville W.C. :: 6",
        "Pat Wheeler :: Frankfort :: 1",
        "Sean Nolan :: Edwardsville",
        "Grant Carlson :: Harvard",
        "S. Boyce :: J.A. Stickers",
        "John Fickett :: Jefferson",
        "Grant Horsch :: Fisher",
    ],
    155: [
        "Greg Davis :: Rochelle :: 5",
        "Joey Penny :: Granite City / Coolidge",
        "Blair Keppner :: Lancer W.C.",
        "Kevin Smith :: DeKalb / Rosette :: 3",
        "Darin Chamblis :: Catlin W.C.",
        "Roland Mansanarez :: Dolton",
        "Jesus Garcia :: Rich Township :: 1",
        "Scott Beverly :: Indian Prairie",
        None,
        "S. Zegar :: Burbank",
        "Sean Harris :: Harvey",
        "Chad Carver :: Decatur YMCA",
        "Brad Hill :: Murphysboro",
        "Matt Olson :: Sterling Challand :: 6",
        "Brian Crosby :: Harvard",
        "Wayne Burki :: Gibson City :: 4",
        "Jeff Basso :: Palos",
        "M. Davis :: Matburns",
        "Charles Nied :: West Chicago :: 2",
        "T. Moran :: J.A. Stickers",
        "Jehad Hamdan :: Lemont",
        "John Annolino :: Hickory Hills",
        "Richie Koch :: Harvard",
        "Waymond Momen :: Rockridge",
    ],
    170: [
        "Mike Brown :: Barrington Colts",
        "Joe Minitti :: Wheaton Falcons :: 6",
        "Shawn Hippey :: Edwardsville",
        "Randy Scianna :: Oak Forest",
        "M. Kulinski :: Lions W.C.",
        "Matt Maple :: Peoria Razorbacks",
        "Andy Sharp :: DeKalb / Huntley :: 1",
        "Bill Dietz :: Murphysboro",
        "J. Fiene :: J.A. Stickers",
        "Ed McDonald :: Palos :: 4",
        "Marvin McFalls :: Morton",
        "Todd Phillips :: Lancer W.C.",
        "Joe Ori :: Crusaders :: 2",
        "Ira Zahner :: St. Charles",
        "Ken Talbot :: Geneseo",
        "Pat O'Neal :: Bethalto",
        "Dave Day :: Plainfield",
        "Brian Hufnagl :: Dolton",
        "Tony Berardi :: Pekin",
        "Johan Lerch :: Rockridge :: 3",
        "Joe Lorenz :: Joliet YMCA",
        "Andre Mayon :: Indian Prairie :: 5",
        "Dave Mechnic :: Lan Oak",
        "Brett Heidtke :: Cardinal Wrestling",
    ],
    185: [
        "Andrew Ritter :: Barrington Colts",
        "Mike Johnston :: Rockridge",
        None,
        "Dreu Diekhoff :: Delavan",
        "Dan Gerecki :: Palos",
        None,
        "Brad Franzen :: Naperville Warhawks :: 2",
        "Mario Gutieriez :: Oak Park",
        "Berny Engh :: DeKalb / Rosette",
        "Carey Lauder :: Hickory Hills :: 6",
        None,
        "Ray Reks :: Plainfield",
        "Mark Diaz :: Sycamore",
        "Kim Honh :: Jefferson :: 4",
        None,
        "Dana Dunklau :: Frankfort :: 1",
        "Paul Lourich :: Hickory Hills",
        "Lester Wilfong :: Round Lake",
        "Bill Kuehn :: Park Ridge",
        "Buddy Estes :: Round Lake :: 3",
        None,
        "Brad Murray :: Edwardsville",
        "Gragg Hardesty :: Westville",
        "Mike Rodriguez :: Indian Prairie :: 5",
    ],
    275: [
        "Victor Krohn :: Harvard",
        "Lyle Bettenhausen :: Joliet YMCA",
        "Edgar Harris :: East St. Louis",
        "Kim Hannon :: Naperville Patriots :: 2",
        "J. Wojcik :: Burbank :: 5",
        "Britt Massey :: Westville",
        None,
        "Ross Karbarski :: Granite City / Coolidge",
        None,
        "Jim Meier :: Plano :: 3",
        "Jim Lee :: Hoopeston",
        "Rocco Zinc :: Matburns",
        "Tom Keasler :: Plainfield",
        "Dana Nelson :: Belvidere",
        None,
        "Dave Rapp :: Vittum Cats :: 4",
        "Ziggy Tkaczenko :: Lancer W.C.",
        "Jim Hickerson :: Moline W.C.",
        "Brian Jordan :: Murphysboro",
        None,
        None,
        "Martin Donath :: Pekin",
        "Scott Venter :: Geneseo :: 6",
        "Adam Lang :: Carol Stream :: 1",
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Vittum Cats": 134.0,  # VITTUM CATS
    "Burbank": 128.0,  # BURBANK PANTHERS / Panther WC
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Jo Jo Fleming", "Rich Township"): bracket_utils.Competitor(
        full_name="Jo Jo Fleming",
        first_name="Jo Jo",
        last_name="Fleming",
        team_full="Rich Township",
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
    all_weights = set(_SENIOR_COMPETITORS.keys())
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
    _generate_placers_image(1984)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, competitors in _SENIOR_COMPETITORS.items():
        bout_numbers = {}
        placers_type = "top6"
        if weight in (95, 100, 105):
            placers_type = "champ"

        weight_class = bracket_utils.weight_class_from_competitors(
            "senior",
            weight,
            competitors,
            _SENIOR_TEAM_REPLACE,
            _NAME_EXCEPTIONS,
            bout_numbers,
            placers_type=placers_type,
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1984.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
