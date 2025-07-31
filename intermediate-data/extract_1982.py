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
        "Curt Bellone :: Palos",
        "R. Chihoski :: Rosemont Cobras :: 5",  # Program says "Rosement"
        "Phillip Schwing :: Fisher",
        "Mike Mostek :: John Deere Wrestling Club :: 2",
        # ^^^ Program says "John Deere Jr. High"
        "Luke Pascale :: Orland Park",
        None,
        None,
        "Steve Owens :: Decatur YMCA",
        "K. Kalchbrenner :: Vittum Park :: 3",
        "Jon Gladish :: Broncos",
        None,
        "Jim Soldan :: Frankfort",
        "K. Snyder :: Burbank :: 4",
        "Joey Wilhelm :: Calumet City",
        None,
        "Jay Ford :: New Lenox Lions :: 1",
        "Louis Montez :: Geneseo WC",
        "Chris Tointon :: Sequoit",
        "Peter Stanley :: Mattoon",
        None,
        "Kevin Givhan :: Dolton :: 6",
        "Bill Morris :: Bensenville",
        "Jim Foley :: Dundee",
        "Matt Snider :: Canton Wrestling Club",
    ],
    55: [
        "Mike Eierman :: Mt. Greenwood :: 6",
        "Sean Meagher :: New Lenox Lions :: 4",
        "Dave Sawyer :: West Chicago",
        "Darby Waggoner :: Lawrenceville",
        "Brett Camden :: Mahomet",  # Program says "Mohomet"
        "Marc Motzer :: Geneseo WC",
        "Chuck Collins :: Broncos",
        "John Vernich :: Lancers Wrestling Club",
        "Brian Dadigan :: New Lenox Lions",
        "Jim Czajkowski :: Burbank :: 1",
        "Sean Coultas :: Canton Wrestling Club",
        "Tom Currie :: Bloomington YMCA",
        "Jeff Turay :: Rich Township :: 2",
        "Sean McElligott :: Oak Forest",
        "Mike Pratt :: Round Lake",
        "Andrew Gardner :: Springfield W.C. :: 3",
        "Tom Gross :: Bethalto Boys Club",
        "V. Cascone :: Vittum Park",
        "Rich Weeden :: Wheaton Park District",
        "R. Swanson :: Dundee",
        "Brent LaRoche :: Oak Lawn",
        "Eric Denning :: Sterling Rock Falls YMCA :: 5",
        "T. Guryn :: Vittum Park",
        "Randy Tedesco :: Belleville Little Devils",  # Program says "Belleville"
    ],
    60: [
        "Jim Pellegrini :: Hazel Crest :: 3",
        "Jim Allen :: Delavan",
        "Jeff Killebrew :: Murphysboro",
        "Jeff Vasquez :: Broncos :: 2",
        "Todd Ryan :: Bensenville",
        "Larry LeFavre :: Sterling Rock Falls YMCA",
        # ^^^ Program says "Sterline Rock Falls"
        "C. Buenik :: Cicero Bobcats",
        "Brian Tiemier :: East Moline W.C.",
        "Jeff Creech :: Mahomet",  # Program says "Mohomet"
        "Brian Moon :: Joliet YMCA :: 5",
        "Derek Baugh :: Bethalto Boys Club",
        "Mike McElwee :: Gower",
        "Eric Fincham :: Urbana",
        "T. Chierico :: Cicero Bobcats",
        "C. Schneider :: Dundee",
        "Mike Dusel :: Wheaton Park District",
        "Jim Zeilenga :: Oak Forest :: 1",
        "Keith Ruiter :: New Lenox Oakview :: 4",
        "Bruce Tiemier :: East Moline W.C.",
        "Randy Slopes :: Neal Eagles",
        "Ed Flynn :: Chicago Ridge",
        "Derek Page :: Edwardsville",
        "Mike Burke :: New Lenox Oakview :: 6",
        "D. Federichi :: Park Ridge",
    ],
    65: [
        "Randy Saller :: Dolton",
        "Jeff McCue :: Simmons",
        "Reggie Fleming :: Rich Township :: 4",
        "Bob Fraher :: Villa-Lombard :: 2",
        "R. Lipsey :: St. Tarcissus",
        "Chad Mueller :: Champaign",
        "Tom Pyle :: Plano",
        "Jim Hilliard :: Lockport",
        "Eric Baumgart :: Broncos",
        "Craig McDougle :: Murphysboro :: 6",
        "Shane Louthan :: Mattoon",
        "K. O'Connor :: Cicero Bobcats",
        "George Bednarczyk :: Harvard :: 3",
        "Sam Geraci :: Lancers Wrestling Club",
        "Mike McInnes :: Mt. Greenwood",
        "Pat Coleman :: Burbank :: 1",
        "Joe Herrmann :: Sycamore",
        "Chad Hamilton :: Roxana Roughnecks",
        "Sean Bormet :: Frankfort",
        "Chuck Smith :: Roxana Roughnecks",
        "Jimmy Creasy :: Macomb YMCA",
        "Bryon Schultz :: Decatur YMCA",
        "Matt Kestian :: Oak Lawn :: 5",
        "Tom Marino :: Villa-Lombard",
    ],
    70: [
        "Angel Perez :: Chicago Ridge",
        "Mike Urwin :: Orland Park :: 1",
        "J.W. Wright :: Dundee",
        "Brett Schultz :: Decatur YMCA :: 5",
        "Steve Wilcox :: Murphysboro",
        "S. Smerz :: Franklin Park Raiders",
        "Jeff Yepez :: Lancers Wrestling Club",
        "Mark Lucas :: Dundee",
        "Richy Wilson :: Coolidge Granite City",
        "John W. Chapman :: Galesburg",
        "S. Beane :: Park Ridge :: 4",
        "Jim Placher :: Troy",
        "Eric Roberson :: Roxana Wrestling Club :: 3",
        "Jim Throw :: Dolton :: 2",
        "Scott Garelli :: Villa-Lombard",
        "Robert Ellis :: Neal Eagles",
        "Ryan Hagger :: Challand",
        "Cory Deck :: Urbana",
        "B. Albach :: Niles Weasles :: 6",
        "Cory Cullinan :: Villa-Lombard",
        "Matt Burright :: DeKalb Rosette",  # Program says "Rosette"
        "Scott Sheen :: Joliet YMCA",
        "David Bidwell :: Urbana",
        "Joe Gilbert :: Tinley Park",
    ],
    75: [
        "Brian Edelen :: Tinley Park :: 2",
        "Dennis Donovan :: Villa-Lombard",
        "Jerry Chapman :: Round Lake",
        "N. Chiappetta :: Cicero Bobcats",
        "Todd Murphy :: Pekin",
        "Kris Armstrong :: Belleville Little Devils",
        "Jeff Meagher :: New Lenox Lions :: 3",  # Program says "New Lenox"
        "Jeff Kindall :: Prather",
        "P.J. Manzari :: Gower",
        "Clarence Ralph :: Fisher",
        "Todd Carlig :: Broncos :: 6",
        "Bobby Mena :: Sterling Newman",
        "Ben Morris :: Bensenville",
        "Toby Willis :: New Lenox Lions :: 5",
        "J. Regan :: Vittum Park",
        "Mark Pustelnik :: East Moline W.C. :: 1",  # Program says "East Moline"
        "Cory Ronk :: Urbana",
        "Bob Kaleta :: Oak Forest",
        "Mark McMahan :: Edwardsville",
        "Dan Walsh :: Dolton",
        "Jeff Scott :: Decatur YMCA",  # Program says "Decatur"
        "Chad Stone :: Dundee",
        "Bill Guide :: Vittum Park :: 4",
        "Tim Chaplin :: Joliet YMCA",
    ],
    80: [
        "Dan O'Brien :: Chicago Ridge :: 1",
        "Matt Mostek :: John Deere Wrestling Club",
        "Dave Gruca :: Batavia",
        "Mike Lamonica :: Orland Park :: 3",
        "Steve Parker :: Lawrenceville",
        "B. Lechtenberg :: West Leyden",
        "Mike Gardner :: Springfield W.C. :: 5",
        "Allen Gullickson :: Harvard",
        "Nate Booth :: Geneseo WC",
        "Mike Coughlin :: Jefferson",
        "T. Lombardo :: Glenview Northbrook",
        "Brad Eller :: Roxana Wrestling Club",
        "Phillip Johns :: Canton Wrestling Club :: 2",
        "Dan Duh :: Mt. Greenwood",
        "Tom Fitzsimmons :: Urbana",
        "Ken Kindall :: Prather",
        "Parker Catlow :: Rich Township",
        "Mike Meluch :: Washington",
        "Greg Goodchild :: Dundee :: 4",
        "Jeff Adkins :: Decatur YMCA",
        "Bret Cassata :: Tinley Park",
        "R. Minauskas :: Vittum Park",
        "Mike Mokas :: Wheaton Franklin",  # Program says "Franklin"
        "Dare Duggan :: Troy :: 6",
    ],
    85: [
        "Dave Manson :: Palos :: 4",
        "M. Besler :: Park Ridge",
        "Shawn DeHaven :: Urbana",
        "Troy Pratsman :: Macomb YMCA :: 2",
        "Mike Ezell :: Frankfort",
        "Gregg Woodcock :: Hill Jr. High",
        "Thad Summers :: Edwardsville",
        "Dan Punkay :: Champaign",
        "M. Haggadus :: Burbank :: 6",
        "Jimmy Cole :: Neal Eagles",
        "Eric Monte :: Gower",
        "Todd Casagrande :: New Lenox Lions",  # Program says "New Lenox"
        "P. McGowean :: Arlington Heights Cardinals",
        "Ed Saller :: Dolton",
        "Craig Schwab :: Belleville Little Devils",
        "Ken Thompson :: Glenwood :: 1",
        "Chris Welsh :: John Deere Wrestling Club",
        "Keith Borchard :: Woodstock",
        "Bob Wansley :: Decatur YMCA",
        "Tracy Morrison :: Edwardsville",
        "Dan Campbell :: Dolton :: 3",
        "Tom Nauyen :: Glencrest :: 5",
        "Andy Warren :: Broncos",
        "Steve Gutierrez :: Huntley",
    ],
    90: [
        "John Crnich :: Oak Forest :: 3",
        "Henry Kijewski :: New Lenox Lions",
        "Paul Schewe :: Wheaton Franklin",  # Program says "Franklin"
        "Brad Stockstill :: Bethalto Boys Club",
        "Dave McClure :: Gibson City",
        "Darrin Cormier :: DeKalb Rosette",
        "Steve Herredia :: Simmons",
        "Perry Fulk :: Jay Stream",
        "Rich Brucato :: Glenwood",
        "J. Cascone :: Vittum Park :: 1",
        "Jeff Vacca :: Canton Wrestling Club :: 6",
        "Matt Madsen :: Urbana",
        "Kevin Kostos :: Huth",
        "LaParker Everett :: Dolton :: 2",
        "D. Schneider :: Dundee",
        "Don Force :: Decatur YMCA",
        "Phil Ellsworth :: Mascoutah",
        "T. Troyke :: Cicero Bobcats",
        "Rich Votava :: West Chicago",
        "Todd Veltman :: Antioch",
        "Tony Ventimiglia :: Oak Forest :: 4",
        "Tom Nelson :: Foreman Wrestling Club",  # Program says "Forman Wres. Club"
        "J. Loos :: Park Ridge :: 5",
        "Mike Wilkening :: Edwardsville",
    ],
    95: [
        "Jack Griffin :: Palos :: 2",
        "Dan Inskip :: Champaign",
        "Corey Henry :: Edwardsville",
        "Ceaser Barrera :: Belvidere :: 3",
        "John Llewellyn :: Hinsdale Wrestling Club",
        "Jason Butt :: Challand",
        "T. Guryn :: Vittum Park",
        "Sean Cunningham :: DeKalb Rosette",  # Program says "Rosette"
        "James Clifton :: Buffalo Tri City",  # Program says "Buffalo"
        "Keith Hutchinson :: Joliet YMCA",
        "Chris Marcy :: Murphysboro",
        "Kirk Siegler :: Hill Jr. High :: 6",
        "Richard Harvey :: Decatur YMCA",
        "J. Schabillion :: West Leyden",
        "Brad Demmitt :: Dundee",
        "Steve Kaltofen :: Wheaton Franklin :: 4",  # Program says "Franklin"
        "Eric Schultz :: Tinley Park",
        "G. Coles :: Frankfort",
        "Scott Holbrook :: Sterling Newman :: 1",
        "Larry Carrol :: Simmons",
        "Tino Gonzales :: Chicago Ridge :: 5",
        "Steve Knoebel :: Belleville Little Devils",
        "Pat Logan :: Troy",
        "L. Alongi :: Rosemont Cobras",
    ],
    100: [
        "Adam Caldwell :: Hazel Crest :: 1",
        "Steve Bushy :: Dundee",
        "Todd Matichtak :: New Lenox Lions :: 4",
        "Rob Gagne :: Villa-Lombard",
        "E. Higgin :: Chicago Mat Burns",
        "Rick Clevenger :: Bradley Bourbonnais",
        "John Davis :: East Moline W.C.",
        "Ken Abney :: Lockport :: 6",
        "Dan Weiskoff :: Woodstock",
        "Dean Webb :: Roxana Wrestling Club",
        "Jeff Sliva :: Georgetown",
        "M. Chihoski :: Rosemont Cobras",
        "Steve Kennicott :: Broncos",
        "Dan Kildane :: Naperville Park District",  # Program says "Naperville"
        "Jeff Anderson :: Tinley Park",
        "J. Lebron :: Vittum Park :: 3",
        "Jim Quilty :: Jordan",  # Program says "Jorden"
        "Mike Layne :: Murphysboro",
        "Dennis Duchene :: Rich Township",
        "Rodney Rutz :: Edwardsville",
        "George DePuy :: Challand :: 2",
        "Don Anderson :: Hoopeston",
        "Dan Moore :: Oak Forest",
        "Todd Cameron :: Bensenville :: 5",
    ],
    105: [
        "John O'Sullivan :: Dolton :: 2",
        "Tony Marchio :: New Lenox Lions :: 5",
        "Jim Hoppenworth :: Belvidere",
        "Brett Walker :: Champaign",
        "Bill Martin :: Murphysboro",
        "M. Reyes :: Chicago Mat Burns",
        "Jack Clark :: Monroe Jr. High",
        "Mark Smith :: Simmons",
        "Dwynn Isringhausen :: Edwardsville",
        "Mark Montgomery :: Sycamore :: 3",
        "R. Ranzonni :: Carl Sandburg Des Plaines",
        "T. Porter :: Glenwood",
        "Don Carter :: Roxana Wrestling Club :: 6",
        "Neal Gaynor :: Tinley Park",
        "Chris Kinser :: Addison",
        "Rob Vasquez :: Broncos :: 4",
        "Jeff Baker :: Plano",
        "Tim Summers :: Hoopeston",
        "M. Rodgers :: Oak Park Huskies :: 1",  # Program says "Oak Park"
        "Mark Sodago :: Wheaton Franklin",  # Program says "Franklin"
        "Chad Gilpin :: Hamilton",
        "Mike Tisza :: Rich Township",
        "Jeff Roedl :: Urbana",
        "Frank Connelly :: Hazel Crest",
    ],
    111: [
        "Rich Reichert :: Oak Forest",
        "Jose Ortez :: Bensenville",
        "Mike Busch :: Broncos",
        "B. Carlstrom :: Carl Sandburg Des Plaines",
        "Mark Wisdom :: DeKalb Rosette",  # Program says "Rosette"
        "Tom Sparks :: Coolidge Granite City",
        "Tom Blaha :: Frankfort :: 1",
        "Mark Heffner :: Roxana Wrestling Club",
        "Paul Foresberg :: Naperville Park District :: 6",
        "Kirk Mammen :: Urbana",
        "Larry Petit :: Batavia",
        "Mike Martin :: Foreman Wrestling Club :: 4",
        "Craig Witt :: West Chicago :: 5",
        "Mike Murry :: New Lenox Oakview",
        "D. O'Connor :: Chicago Mat Burns",
        "Jeff Norin :: Coolidge Granite City :: 3",  # Program says "Coolidge"
        "Charles Sprandle :: Decatur YMCA",
        "Alex Dumas :: Dolton",
        "Chuck Nelson :: Edwardsville",
        "Mike Triumph :: Tinley Park :: 2",
        "Scott Pruitt :: Urbana",
        "Dave Case :: Antioch",
        "D. Boidt :: Arlington Heights Cardinals",
        "Jim Lee :: Troy",
    ],
    118: [
        "Paul Dagenais :: Tinley Park :: 1",
        "Owen Doak :: Jordan",  # Program says "Jorden"
        "Jim Walker :: Geneseo WC",  # Program is missing team info
        "Pete Andreotti :: Orland Park :: 3",
        "Rob Trimpl :: Mascoutah",
        "M. Hufnus :: Carl Sandburg Des Plaines",
        "Andre Brown :: Urbana",
        "Bob Birdsell :: Woodstock",
        "Alan Reyna :: East Moline W.C.",
        "Mike Lewingham :: Lancers Wrestling Club :: 6",
        "B. McBride :: Burbank",
        "Kip Simpson :: Grigsby",
        "Matt Hagger :: DeKalb Rosette",  # Program says "Rosette"
        "Joe Liberatore :: Tinley Park :: 2",
        "Tom Johnson :: Hoopeston",
        "Bruce Musgrave :: Mascoutah",
        "Gary Slagle :: Lockport",
        "Skip Sparmann :: Eisenhower",
        "John Sehnert :: Broncos :: 5",
        "Dave Ebersol :: Bradley Bourbonnais",
        "Mike Harms :: Oak Forest :: 4",
        "E. Swenson :: Glenview Northbrook",
        "Greg Silitto :: Wheaton Franklin",  # Program says "Franklin"
        "Pat Wheeler :: Frankfort",
    ],
    125: [
        "Terry McGuire :: Oak Forest",
        "S. Case :: Franklin Park Raiders",
        "Todd Howell :: Rantoul",
        "Matt Roach :: DeKalb Rosette :: 2",  # Program says "Rosette"
        "Jack Baumann :: New Lenox Oakview",
        "Harry Leitner :: Eisenhower",
        "Chris Lindsay :: Mascoutah :: 6",
        "Greg Gardner :: Springfield W.C. :: 3",
        "D. Stawik :: Rosemont Cobras",
        "Jeff Harris :: Neal Eagles",
        "Brian Donnely :: Addison",
        "Steve Bogdan :: Plainfield",
        "J. Popp :: Burbank :: 1",
        "Gary Wyman :: Mt. Greenwood",
        "Fred Becker :: Grigsby",
        "John Dejarld :: Troy",
        "Troy Topia :: East Moline W.C.",
        "Eric Collins :: Broncos",
        "Mark Filipiak :: Mattoon :: 4",
        "David Patrick :: Prather",
        "Frank Kubisz :: Calumet Park",
        "John Arlis :: Villa-Lombard :: 5",
        "Mark Welch :: Dundee",
        "Nick Rinaldo :: Pekin",
    ],
    135: [
        "Pete Pasternak :: Calumet City :: 1",
        "David White :: Rich Township",
        "Rich Yanags :: Lombard",
        "Mike Fenoglio :: Prather",
        "Jim Garecht :: Mt. Zion",
        "Jon Elias :: Sycamore",
        "Anton Kossakowski :: Dundee",
        "Kevin Kerr :: Wheaton Franklin",  # Program says "Franklin"
        "Craig Buckland :: Joliet YMCA",
        "J. Miner :: Burbank :: 3",
        "Brad Cameran :: East Moline W.C. :: 5",
        "Mike Harden :: Mattoon",
        "Mike Klatt :: Joliet YMCA",
        "Meni Tripolitakis :: Dolton :: 4",
        "Tim Paull :: Broncos",
        "Dan Raup :: Rantoul",
        "David Thompson :: Murphysboro :: 6",
        "J. Tamburino :: Park Ridge",
        "Cory George :: Bensenville :: 2",
        "Mark Dowdell :: Batavia",
        "Nick Zegar :: Oak Lawn",
        "Darin Anderson :: Huntley",
        "M. Brown :: Oak Park Huskies",
        "Tracy McElroy :: Prather",
    ],
    145: [
        "Tino McCabe :: Mt. Greenwood :: 3",
        "Clif Wittey :: Hoopeston :: 6",
        "Dan Burk :: Roxana Wrestling Club",
        "Jerry DeGelder :: Woodstock",
        "Todd Nielson :: Hill Jr. High",
        "Greg McManus :: Rock Ridge",
        "R. Thurby :: Oak Park Huskies",
        "Jim Newton :: Canton Wrestling Club",
        "Bill Smith :: Gibson City",
        "E. Johnson :: Orland Park :: 1",
        "Jeff Smith :: Roxana Wrestling Club",
        "Bob Walters :: West Chicago",
        "Kevin Scudder :: Rantoul :: 2",
        "B. Bavowski :: Arlington Heights Cardinals",
        "Hal Foster :: Broncos",
        "Rick Janoski :: Westview Hills",
        "Dave Seastom :: Palos",
        "Kevin O'Connor :: Rich Township",
        "Tim Schmidt :: Rock Ridge :: 4",
        "Bill Gallagly :: Harvard",
        "John McCormack :: Oak Lawn",
        "Chris Gillian :: Murphysboro :: 5",
        "D. Akers :: Plainfield",
        "M. Montes :: Cicero Bobcats",
    ],
    155: [
        "Chuck Zickus :: Palos",
        "Lester Lentz :: Round Lake",
        "M. Root :: Huth",
        "Jeff Krash :: Hill Jr. High :: 3",
        "G. Sopoci :: Oak Park Huskies",
        "Tracy Benison :: Gibson City",
        "Aaron Faivre :: Huntley :: 1",
        "Dave LaPasa :: Troy",
        "Tim Halverson :: Batavia",
        "Scott Maberry :: Roxana Wrestling Club",
        "Jim Cruthird :: Decatur Boy's Club",
        "L. Boudreaux :: LaGrange Lions",
        "Charles Gayden :: Neal Eagles",
        "Harry Geller :: Washington",
        "Jim Glynn :: Palos :: 4",
        "B. Murphy :: Cicero Bobcats",
        "Jim Catterton :: East Moline W.C. :: 5",
        "Trevor Dumar :: Edwardsville",
        "Jim Neal :: Plainfield :: 2",
        "Chris Greer :: Prather",
        "Scott Johnson :: Oswego",
        "Jeff Rowley :: Decatur YMCA",
        "Bryan Lynch :: Hickory Hills :: 6",
        "Roco Tiberi :: Bensenville",
    ],
    170: [
        "Gary Wetzel :: Oak Forest",
        "Bill McGory :: New Lenox Lions",
        "Burnett :: Harvard :: 5",
        "Jim Hooper :: Mattoon",
        "Mike Dawson :: Murphysboro",
        "A. Faragoso :: Burbank",
        "Brian Larson :: Washington",
        "Norris Randolph :: Neal Eagles :: 4",
        "Pat Nuernberger :: Edwardsville",
        "Joe Traglia :: Huntley :: 2",
        "J. Murray :: Oak Park Huskies",
        "P. Junge :: Huth",
        "Floyd Roe :: Prather",
        None,
        "Vince Rolon :: West Chicago",
        "Jim Johnston :: Dundee :: 3",
        "Sam Anderson :: Huntley",
        "Pat Dillman :: Georgetown",
        "A. Parker :: West Leyden",
        "Jim Skillen :: Wheaton Franklin :: 6",  # Program says "Franklin"
        "David Hudson :: Canton Wrestling Club",
        "R. Webb :: Plainfield :: 1",
        "Rob Siders :: Urbana",
        None,
    ],
    185: [
        "Lyle Lake :: Oak Lawn",
        None,
        "Dewey Neuman :: Fox Lake",
        "K. Parker :: West Leyden :: 4",
        "Bob Taylor :: Huntley",
        None,
        "Mark Topping :: Huth :: 1",
        "Ben Richards :: Edwardsville",
        None,
        "Tim Lambert :: Decatur YMCA :: 5",
        "B. Stiltson :: Freeport",
        "Craig Smith :: DeKalb Rosette",  # Program says "Rosette"
        "Chuck Gehring :: Eisenhower",
        "Tony Gatlin :: Rich Township",
        "M. Scott :: Oak Park Huskies",
        "Ed Pederson :: Huntley :: 3",
        None,
        None,
        "Mike Newman :: Edwardsville :: 2",
        "Scott Krneta :: Palos",
        None,
        "Randy Larson :: Woodstock",
        "B. Metzger :: Oak Park Huskies",
        "S. Tighe :: Plainfield :: 6",
    ],
    275: [  # Program says "UNLIMITED"
        "J. Rickhoff :: Oak Lawn",
        "Bruce Goyen :: Canton Wrestling Club",
        "Scott Jahl :: Broncos",
        "James Washington :: Rich Township :: 1",
        "Tom Richmond :: Prather",
        None,
        "Dave Hart :: Decatur YMCA :: 3",
        "Bob Johnson :: Antioch",
        None,
        "Ed Konkolich :: Eisenhower :: 5",
        None,
        None,
        "Jeff Pedersen :: Huntley",
        "Eric Hallberg :: Dolton",
        "James Orange :: Rantoul",
        "Harold Pace :: Grigsby",
        "Pat Collins :: Huth",
        "Rich Randall :: Lancers Wrestling Club :: 6",
        "Dan Paulley :: Harvard :: 2",
        "Milt Johnson :: Buffalo Tri City",
        "Todd Hunzinga :: Lansing",
        "J. Galvan :: Burbank",
        "Dave Fank :: Wheaton Franklin :: 4",  # Program says "Franklin"
        "Dave Coughlin :: Glenwood",
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Burbank": 145.0,  # BURBANK PANTHERS
    "Dolton": 134.0,  # DOLTON FALCONS
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("John W. Chapman", "Galesburg"): bracket_utils.Competitor(
        full_name="John W. Chapman",
        first_name="John",
        last_name="Chapman",
        team_full="Galesburg",
    ),
    ("Burnett", "Harvard"): bracket_utils.Competitor(
        full_name="Burnett",
        first_name="",
        last_name="Burnett",
        team_full="Harvard",
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
    _generate_placers_image(1982)

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
    with open(_HERE / "extracted.1982.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
