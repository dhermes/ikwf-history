# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_COMPETITORS: dict[int, list[str | None]] = {
    50: [
        "Robert Chihoski :: Rosemont :: 2",
        "Randy Berke :: DeKalb Huntley",
        "Tim Condit :: Oak Forest",
        "Josh Mattio :: Rich Township :: 4",
        "Mike Dickinson :: Roxana Park District",
        "John Zuspann :: Jefferson",
        "Ryan Ferguson :: Lancer :: 6",
        "Tom Hincks :: Mt. Greenwood",
        None,
        "John Stanley :: Mattoon",
        "Chris Tointon :: Sequoits",
        "Sam Hogue :: Belleville Little Devils",
        "Mike Mena :: Sterling Newman",
        "George Macey :: Vittum Park :: 3",
        "Justin Weber :: West Chicago",
        "Eric Carter :: Roxana Park District",
        "Todd Kelly :: Glenwood :: 5",
        "Phil Schwing :: Fisher",
        "Joe O'Sullivan :: Dolton",
        "Chris Wheile :: Bensenville",
        "Steven Dubois :: Burbank :: 1",
        "Nick Cina :: Belvidere",
        "Corey Daker :: Foreman",
        "Dave Kinsey :: Joliet YMCA",
    ],
    55: [
        "Kurt Kalchbrenner :: Vittum Park :: 5",
        "Ryan Smith :: Roxana Park District",
        "Jim Foley :: Dundee",
        "John Virnich :: Lancer",
        "Joe Wilhelm :: Calumet City :: 3",
        "Jim Soldan :: Frankfort",
        "Aron Roddis :: Decatur",
        "Ryan Radosh :: Bronco Wrestling Club",
        "Jason Johnson :: Roxana Park District",
        "Mike Mostek :: John Deere :: 2",
        "Luke Pascale :: Orland Park",
        "Jim Pasvento :: Oak Forest",
        "Randy Deeke :: Belleville Little Devils",
        "Keith Snyder :: Burbank :: 1",
        "John Lieb :: Fisher",
        "Dan Gilbert :: Tinley Park :: 6",
        "Doug Sawyer :: West Chicago",
        "Jason Derry :: Macomb",
        "John Gladish :: Bronco Wrestling Club",
        "Peter Stanley :: Mattoon",
        "Dan Walters :: Burbank",
        "Sean Meagher :: New Lenox Lions :: 4",
        "Louie Montez :: Geneseo",
        "Adrian Parades :: Gower",
    ],
    60: [
        "Jim Czajkowski :: Burbank",
        "Mike Eierman :: Mt. Greenwood",
        "Bill Morris :: Bensenville",
        "Andy Gardner :: Springfield :: 3",
        "Mike Pratt :: Round Lake",
        "Paul Blaha :: Frankfort",
        "Eric Denning :: Sterling Newman :: 5",
        "Ken Gerdes :: Orland Park :: 2",
        "Andy Bednarczyk :: Tinley Park",
        "Jason Warner :: Roxana Park District",
        "Vince Nanone :: Wheaton Park District",
        "Kelly Hamill :: Belvidere",
        "Sean McElligott :: Oak Forest :: 4",
        "Troy Finnestad :: DeKalb Huntley",
        "Tim Currie :: Redbirds",
        "Chuck Collins :: Bronco Wrestling Club",
        "Mike Roach :: Burbank",
        "Randy Tedesco :: Belleville Little Devils",
        "Jeff Turay :: Rich Township :: 6",
        "Shane Dipholz :: Mattoon",
        "Chris Buenik :: Bobcats :: 1",
        "Rick Weeden :: Villa Lombard",
        "Darby Waggoner :: Lawrenceville",
        "Darin Cowan :: Geneseo",
    ],
    65: [
        "Tony Chierico :: Bobcats",
        "Bill Walsh :: Dolton",
        "Fred Ray :: Edwardsville",
        "Jeff Vasquez :: Bronco Wrestling Club :: 3",
        "Daryl Grennan :: Sterling Newman",
        "Ricky Harris :: Tinley Park :: 5",
        "Dan Willis :: New Lenox Lions :: 2",
        "Ken Howell :: Bethalto Boys Club",
        "Chad Mueller :: Champaign",
        "Scott Garelli :: Villa Lombard",
        "Todd Oliver :: Mt. Zion",
        "Manual Olalde :: Sterling Newman",
        "Jeff Hollon :: Decatur",
        "Charlie Schneider :: Dundee",
        "Tim Guryn :: Vittum Park :: 6",
        "Andy Neal :: DeKalb Huntley",
        "Ed Flynn :: Palos",
        "Mike Dusal :: Glencrest",
        "Jeff Kellebrew :: Murphysboro",
        "Todd Ryan :: Bensenville",
        "Shelly Resendes :: Glenwood :: 4",
        "Jim Zeilenga :: Oak Forest :: 1",
        "Lavell Stennis :: Masson",
        "Tom Williams :: Bronco Wrestling Club",
    ],
    70: [
        "Pete Schulte :: Oak Park :: 2",
        "Derek Baugh :: Bethalto Boys Club",
        "Scott Cinnamon :: Champaign",
        "Matt Kestian :: Oak Lawn :: 4",
        "John Walker :: Eisenhower",
        "Tim McCarthy :: DeKalb Rosette",
        "Mike Sheehy :: Dundee",
        "Shane Louther :: Mattoon",
        "Brian Abraham :: Lancers",
        "Sean Bormet :: Frankfort :: 5",
        "Jim Creasy :: Macomb",
        "Chris Cochran :: Murphysboro",
        "Bob Fraher :: Villa Lombard :: 3",
        "Bill O'Brien :: Burbank :: 6",
        "Erik Baumgart :: Bronco Wrestling Club",
        "Dion Simmons :: Decatur",
        "Ed Cordova :: Lockport",
        "Steve Kestian :: Oak Lawn",
        "Ryan Hager :: Sterling Newman",
        "M. Olbrich :: Harvard",
        "Brian Ezell :: Frankfort",
        "Chad Hamilton :: Roxana Park District",
        "Jim Pellegrini :: Hazel Crest",
        "Paul Zina :: Oak Park :: 1",
    ],
    75: [
        "Paul LeKousis :: Bobcats :: 4",
        "M. Bartlett :: St. Charles Haines",
        "Chad Burcham :: Mattoon",
        "Joe Herrmann :: Sycamore :: 5",
        "Sean Chiarodo :: Rich Township",
        "Cory Cullian :: Villa Lombard",
        "Richie Wilson :: Granite City Coolidge",
        "Craig Dourherty :: Naperville",
        "Rich Umland :: Harvard",
        "Joe Gilbert :: Tinley Park :: 1",
        "Ron Ruzic :: Springfield",
        "Jim Hillard :: Lockport",
        "Rob Ellis :: Bronco Wrestling Club :: 2",
        "Jason Sladen :: Roxana Park District",
        "Ron Berko :: DeKalb Huntley",
        "Scott Richardson :: New Lenox Lions",
        "Dave Campbell :: Dolton",
        "Stan Valle :: Park Ridge",
        "Sam Geraci :: Lancer :: 3",
        "Steve Smerz :: Franklin Park",
        "Mike McInnes :: Mt. Greenwood",
        "Bryan Schultz :: Decatur :: 6",
        "Larry Tiesort :: John Deere",
        "Joe Abegg :: Belleville Little Devils",
    ],
    80: [
        "Nino Chiappetta :: Bobcats :: 3",
        "Paul Andreotti :: Orland Park",
        "Kevin Denton :: Westville",
        "Jeff Kindall :: Prather Granite City",
        "Jeff Yapez :: Bensenville",
        "Todd Finnestad :: DeKalb Huntley",
        "Mike MacKowiak :: Tinley Park :: 1",
        "Bill Bradon :: Unity",
        "Rob Jeffreys :: Glenwood",
        "Todd Carlig :: Bronco Wrestling Club :: 6",
        "Lance Earl :: DeKalb Rosette",
        "John Westmass :: Monroe",
        "Toby Willis :: New Lenox Lions :: 4",
        "Jim Regan :: Vittum Park",
        "Mike Spatz :: Mt. Greenwood :: 5",
        "Mike Melluch :: Warriors",
        "Randy Maykoset :: Granite City South",
        "Brian Zust :: Bronco Wrestling Club",
        "Robbie Grayson :: Foreman",
        "Joe Rzepinski :: Lansing :: 2",
        "Bob Toth :: Vitum Park",
        "Brian Williams :: East Moline",
        "Mark Lucas :: Dundee",
        "Jeff Heimkamp :: Roxana Jr. High",
    ],
    85: [
        "Don O'Brien :: Burbank :: 1",
        "Matt Mostek :: John Deere",
        "Kevin Walsh :: Hickory Hills",
        "Shawn Kinder :: Joliet YMCA",
        "Jake Varadian :: Prather Granite City",
        "Jerry Chapman :: Round Lake",
        "Dennis Donnovan :: Villa Lombard :: 6",
        "Jerad Desanto :: Chicago Ridge",
        "Tyler Allen :: DeKalb Rosette",
        "Brett Schultz :: Decatur :: 4",
        "J. Kossakowski :: Dundee",
        "Angelo Alvarez :: Belleville Little Devils",
        "Bob Mena :: Sterling Newman",
        "Bill Guide :: Vitum Park :: 5",
        "T.J. Manzeri :: Gower",
        "Eric Roberson :: Roxana Jr. High :: 3",
        "Terry Rich :: Lockport",
        "Mike Anderson :: Hoopeston",
        "Dan Duh :: Mt. Greenwood :: 2",
        "Matt Gruska :: Hill Jr. High",
        "Brian Lechtenburg :: Franklin Park",
        "Chad Stone :: Dundee",
        "John Ritchie :: Pekin",
        "Scott Pustarer :: Huth",
    ],
    90: [
        "Ray Serbick :: Franklin Park :: 4",
        "Brent Davis :: Prather Granite City",
        "M. Dailey :: Royal Wrestling Club",
        "Chuck Black :: West Chicago",
        "Lou Debs :: Dolton :: 2",
        "Tim Chaplin :: Joliet YMCA",
        "Clarence Ralph :: Fisher",
        "Pat Hood :: Bronco Wrestling Club",
        "Chad Carpenter :: Granite City Coolidge",
        "Tom Allen :: DeKalb Rosette",
        "Bob Wortel :: Orland Park",
        "Paul Reidy :: Oak Forest :: 6",
        "Steve Parker :: Lawrenceville",
        "Angelo Auriemma :: Bobcats",
        "Terry Beebe :: Foreman",
        "Brian Edelen :: Tinley Park :: 1",
        "Craig Pfotenhauer :: Jay Stream",
        "Nate Booth :: Geneseo",
        "A.T. Arneson :: Royal Wrestling Club :: 3",
        "Dave Flies :: Dectaur",
        "Kean :: Burbank",
        "Justin Gaeta :: Palos :: 5",
        "Tom Juenger :: Wilson",
        "Al Dvorak :: Villa Lombard",
    ],
    95: [
        "Gino Fioravanti :: Oak Park",
        "Bob Apatto :: Oak Lawn",
        "Frank Trossen :: Warriors",
        "Pat Rinaldo :: Pekin",
        "Craig Goodchild :: Dundee",
        "Jeff Meagher :: New Lenox Lions :: 3",
        "John Massa :: East Moline :: 6",
        "Dave Manson :: Palos :: 2",
        "John Eierman :: Mt. Greenwood",
        "Tracy Morrison :: Edwardsville",
        "Rich George :: Patriots",
        "Matt Colangelo :: Woodstock",
        "Tim McDonald :: Hickory Hills",
        "Darren Cue :: Oswego",
        "Matt Madsen :: Urbana",
        "Jim Cole :: Bronco Wrestling Club",
        "Faley :: Burbank",
        "Brian Hine :: Murphysboro :: 5",
        "Mike LaMonica :: Orland Park :: 1",
        "Cory Ronk :: Urbana :: 4",
        "Don Hansen :: Franklin Park",
        "Eric Monte :: Gower",
        "Joe Johnston :: Williamson County",
        "Matt Engstrom :: DeKalb Huntley",
    ],
    100: [
        "David Frencl :: Vitum Park",
        "Dave McClure :: Gibson City :: 6",
        "Marty Evans :: Edwardsville",
        "Mike Cheatham :: Bronco Wrestling Club",
        "Tony Benitez :: Oswego :: 4",
        "Brian Schiller :: Mt. Greenwood",
        "Ken Thompson :: Glenwood",
        "Brad Stockstill :: Bethalto",
        "Tony Woods :: Illini Bluff",
        "Ben Morris :: Bensenville :: 1",
        "Mike Gryga :: Oak Lawn",
        "Scott Blankenship :: Rock Ridge",
        "Tom Dunniway :: Pekin",
        "M. Lockhart :: St. Charles Haines",
        "Gino Vegetable :: Burbank",
        "Troy Protsman :: Macomb :: 2",
        "Larry VonArb :: Palos",
        "Rich Votava :: West Chicago :: 5",
        "David Marlow :: Williamson County :: 3",
        "Matt Beck :: Jay Stream",
        "Henry Kijewski :: New Lenox Lions",
        "Bill Clemente :: Hickory Hills",
        "Bill Novak :: Burbank",
        "J. Kerner :: St. Charles Thompson",
    ],
    105: [
        "Joe Cascone :: Vittum Park :: 1",
        "Corey Henry :: Edwardsville",
        "Bob Ekin :: Catlin",
        "Pat Fritz :: Oak Lawn",
        "Terry Fulk :: Jay Stream",
        "Sean Cunningham :: DeKalb Rosette :: 5",
        "James Gratz :: Harvard",
        "Pat McGarrghn :: Catlin",
        "Dave Schield :: Warriors",
        "Paco Hernandez :: Lockport :: 3",
        "Chris Welsch :: John Deere",
        "Mike Layne :: Murphysboro",
        "Bob Marmolejo :: West Chicago :: 6",
        "Burt Downing :: Mason",
        "Brad Demmitt :: Dundee",
        "Dwight Simmons :: Decatur",
        "Victor Blackful :: Rich Township",
        "Kevin Nolan :: Mt. Greenwood",
        "Pat Nestor :: Sterling Newman :: 4",
        "T. Sader :: Royal Wrestling Club :: 2",
        "Greg Stopka :: Frankfort",
        "Jon Anderson :: Prather Granite City",
        "Scott Grannes :: Mt. Greenwood",
        "Pete Tragos :: Arlington",
    ],
    111: [
        "Tom Guryn :: Vittum Park",
        "T. Morgan :: St. Charles Thompson",
        "Jim Russell :: Fisher",
        "Chad Gilpin :: Hamilton :: 1",
        "Jay Barickello :: Joliet YMCA",
        "Curt Newingham :: Lancers :: 6",
        "Tim Melosci :: Roxana Jr. High",
        "Jim Palazzo :: Jay Stream",
        "R. Camacho :: Waldo",
        "Dan Campbell :: Dolton :: 4",
        "Brett Walker :: Champaign",
        "Ray Nunez :: Frankfort",
        "Scott Welch :: Dundee",
        "Rich Fenoglio :: Prather Granite City",
        "Curt Mallory :: DeKalb Rosette",
        "Ken Abney :: Lockport :: 2",
        "Maurice Mance :: Harvey",
        "Ken Brown :: Rosemont",
        "Jim Sick :: Patriots :: 5",
        "Ryan :: Carl Sandburg",
        "Ron Stewart :: Tinley Park",
        "John Johnson :: Catlin",
        "Jason Butt :: Sterling :: 3",
        "Chuck Sparks :: Granite City Coolidge",
    ],
    118: [
        "Emmit Higgin :: Mattburns :: 5",
        "Sean Cantorna :: Palos",
        "Tim Summers :: Hoopeston",
        "Eric Chisman :: Carbondale Park District",
        "Bob Gagne :: Villa Lombard :: 4",
        "Bryan Eyrich :: Geneseo",
        "Rich Bielek :: Hickory Hills :: 2",
        "Doug Price :: Urbana",
        "John Ivlow :: Plainfield",
        "Rich Powers :: Harvard",
        "Brian Kish :: Sandwich",
        "Tom Casey :: Gower",
        "Mickey Smith :: Joliet YMCA",
        "Shin :: Carl Sandburg",
        "Eric Schultz :: Tinley Park :: 6",
        "Chris Pradel :: Patriots",
        "Dave Pollard :: Roxana Jr. High",
        "Tim Winger :: Bronco Wrestling Club",
        "Richard Harvey :: Decatur :: 3",
        "Jeff Anderson :: Tinley Park",
        "Karl Cloherty :: St. Tars",
        "Mark Montgomery :: DeKalb Huntley :: 1",
        "Rob Russo :: Round Lake",
        "Paul Brandt :: Prather Granite City",
    ],
    125: [
        "John Skelton :: Oak Park",
        "Dave Schultz :: DeKalb Huntley",
        "Sherif Zezar :: Oak Lawn",
        "Oscar Godinez :: Plainfield :: 6",
        "Chris Mueller :: Carbondale Park District",
        "Scott Steiger :: Woodstock",
        "Jack Schomig :: Franklin Jr. High :: 4",
        "Jerry Joyce :: Dolton",
        "Pec Callahan :: DeKalb Huntley",
        "Kirk Mammen :: Urbana :: 2",
        "Gary Denn :: Royal Wrestling Club",
        "Glen Goodman :: Prather Granite City",
        "Tim Shelton :: Geneseo",
        "Dave Boldt :: Arlington",
        "Steve Farnero :: Villa Lombard",
        "Bill Martin :: Murphysboro",
        "Brian Heisner :: Frankfort :: 5",
        "Craig Clark :: Gibson City",
        "Mike Harms :: Oak Forest :: 3",
        "Juan Varges :: West Chicago",
        "Mark Warta :: Bobcats",
        "John Sehnert :: Bronco Wrestling Club :: 1",
        "Lamount Perkins :: Georgetown",
        "Kevin Saunders :: New Lenox Lions",
    ],
    135: [
        "Brian McBride :: Burbank :: 3",
        "Pat O'Neal :: Bethalto Boys Club",
        "K. Marchesi :: Royal Wrestling Club",
        "Mike Newingham :: Lancers :: 2",
        "Mark Koselke :: Lansing",
        "Jim Champion :: Palos",
        "Scott Walton :: Decatur",
        "Todd Denenger :: Woodstock",
        "Brett Coffey :: Edwardsville",
        "Chris Lanier :: DeKalb Huntley",
        "Pat Wheeler :: Frankfort :: 6",
        "Geno Giuntoli :: Chicago Ridge",
        "Terry Stanley :: Prather Granite City",
        "Shawn Roselieb :: Rosemont",
        "Mike Douglas :: Decatur",
        "Mike Triumph :: Tinley Park :: 4",
        "Joe Mox :: Patriots",
        "Doug Mack :: DeKalb Huntley",
        "S. Gray :: St. Charles Thompson",
        "John Rodermaker :: Illini Bluff",
        "Matt McDermot :: Oak Park",
        "Tom Blaha :: Frankfort :: 1",
        "John Pierce :: Sterling :: 5",
        "Chris Wesolik :: Warhawks",
    ],
    145: [
        "James DeShane :: Rosemont",
        "Greg Phillips :: Hazel Crest",
        "Scott Lockmiller :: Lancers :: 6",
        "Brian Williams :: Pekin",
        "Dan Barnes :: Barrington Colts",
        "Jesus Garcia :: Rich Township",
        "Darin Anderson :: DeKalb Huntley :: 1",
        "Steve Bogdon :: Plainfield :: 4",
        "Derrick Henderson :: Harvey",
        "David Thompson :: Murphysboro",
        "Harry Letterman :: Eisenhower",
        "G. Davis :: Royal Wrestling Club",
        "Paul Garcia :: Oak Forest",
        "Justin Fleetwood :: Sycamore :: 2",
        "Joe Tucker :: Illini Bluff",
        "Lonnie Johnston :: Dundee",
        "Tony Mroczek :: Mattburns",
        "Matt Piazzo :: Roxana Jr. High",
        "Pete Lellos :: Palos",
        "Wayne Burke :: Gibson City",
        "Mike Skoury :: Arlington",
        "Scott Jablonski :: Jay Stream :: 3",
        "Dwayne Davis :: Edwardsville",
        "Owen Doak :: Jordan :: 5",
    ],
    155: [
        "Brian Murphy :: Bobcats",
        "Tracy Benson :: Gibson City",
        "Marvin Lampkin :: Little Comanches",
        "Bill Gallagly :: Harvard :: 2",
        "Andy Sharp :: DeKalb Huntley",
        "Pete Fulton :: Dolton",
        "Jeff Licciardello :: Palos",
        "Rich Fish :: Roxana Jr. High",
        "Scott Harter :: Illini Bluff",
        "Rich Villareal :: Eisenhower :: 3",
        "Jerry Judd :: Oak Lawn :: 6",
        "Dave Tertipes :: Wilson",
        "Brian Hollett :: Catlin",
        "Ralph Espareza :: Jefferson",
        "Joe Ori :: Crusaders",
        "Johan Lerch :: Rock Ridge",
        "Phil Scroppo :: Palos :: 5",
        "Chuck Sodaro :: Hill Jr. High",
        "Darrin Mills :: Murphysboro",
        "Robert Chebulski :: Jay Stream",
        "David White :: Rich Township :: 4",
        "Pete Pasternak :: Calumet City :: 1",
        "D.J. Becek :: Lyons",
        "K. Pazonka :: St. Charles Haines",
    ],
    170: [
        "Kevin Saunders :: Oak Park",
        "Bryan Wilkins :: Little Comanches",
        "Cory Barton :: Westville",
        "Scott McCabe :: Mt. Greenwood :: 3",
        "Andre Mayon :: Hill Jr. High :: 6",
        "Davin Isiackson :: Orion",
        "John Reader :: St. Charles Haines",
        "Doug Hodges :: Decatur",
        "Scott Miller :: Gower",
        "Dave Seastrom :: Palos :: 1",
        "Sam Switzer :: Peoria",
        "Mike Crane :: Murphysboro",
        "Mark Kuehl :: Gower :: 2",
        "Steve Sippos :: Mattburns",
        "Bill Anderson :: Harvard",
        "Mark Fells :: Westville",
        "Joe Englert :: Plainfield",
        "Mike Pietrzycki :: Calumet City",
        "Dave Tennant :: Rock Ridge :: 4",
        "Henry Davis :: Harvard",
        "Bill Junge :: Huth",
        "Craig Floyd :: Roxana Jr. High",
        "Joe Dolce :: Oak Lawn :: 5",
        "Scott Walker :: Mattburns",
    ],
    185: [
        "Roco Zink :: Mattburns",
        "Joe Thompson :: Harvard",
        "Tim Howard :: Westville :: 3",
        "Jim Shaffer :: DeKalb Rosette :: 5",
        "Mark Topping :: Huth",
        "Glen Bourdueox :: Gower",
        "Adam Lang ::  Murphysboro",
        "Mark Crawford :: Bensenville",
        "Buddy Estes :: Round Lake",
        "Eric Sebahar :: Calumet City",
        "Dan Carter :: Mt. Zion",
        "Dana Dunklau :: Frankfort :: 1",
        "Richard Zalud :: Harvard",
        "Vance Morgan :: Edwardsville",
        "Rich Burklund :: East Moline",
        "Scott Krneta :: Palos :: 4",
        "George Ordozo :: Oak Lawn",
        None,
        "Mike Rodrigues :: Hill Jr. High",
        "Dan Matticks :: Oak Park",
        "Spero Uithoulkas :: Mt. Greenwood",
        "Charles Young :: Decatur :: 2",
        "Blair Hatten :: Geneseo :: 6",
        "Ross Karbarski :: Granite City Coolidge",
    ],
    275: [
        "Andy Low :: Northbrook",
        "Kin Hau :: Frankfort :: 3",
        None,
        "Ken Shields :: Belleville Little Devils :: 5",
        "Rich Dedic :: Hill Jr. High",
        "Paul Feltz :: DeKalb Huntley",
        "Gary Wetzel :: Oak Forest :: 1",
        "Brett Massey :: Westville",
        "Ed Hutton :: James Hart",
        "Victor Krohn :: Harvard",
        "Tim Meier :: Plano",
        "Philip :: Gower",
        "Delray Williams :: Huth",
        "Lynn Burnet :: Mason",
        "Harry Thanos :: Mt. Greenwood :: 6",
        "Rick Swanson :: Eisenhower",
        "John Strickland :: Prather Granite City",
        None,
        "Rob Hamann :: Illini Bluff :: 2",
        "Chris Head :: Oak Lawn",
        "Greg Sorenson :: Crusaders",
        "Art Sturms :: Geneseo :: 4",
        None,
        "David Kaltmayer :: Granite City Coolidge",
    ],
}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    50: bracket_utils.Placer(name="Steve DuBois", team="Panther WC"),
    55: bracket_utils.Placer(name="Keith Snyder", team="Panther WC"),
    60: bracket_utils.Placer(name="Chris Buenik", team="Cicero Bobcats"),
    65: bracket_utils.Placer(name="Jim Zeilenga", team="Oak Forest Warriors"),
    70: bracket_utils.Placer(name="Paul Zina", team="Oak Park"),
    75: bracket_utils.Placer(name="Joe Gilbert", team="Tinley Park Bulldogs"),
    80: bracket_utils.Placer(name="Mike Mackowiak", team="Tinley Park"),
    85: bracket_utils.Placer(name="Dan O'Brien", team="Panther WC"),
    90: bracket_utils.Placer(name="Brian Edelen", team="Tinley Park Bulldogs"),
    95: bracket_utils.Placer(name="Mike Lamonica", team="Orland Park Pionee"),
    100: bracket_utils.Placer(name="Ben Morris", team="Bensenville"),
    111: bracket_utils.Placer(name="Chad Gilpin", team="Hamilton"),
    118: bracket_utils.Placer(name="Mark Montgomery", team="DeKalb Huntley"),
    125: bracket_utils.Placer(name="John Sehnert", team="Barrington"),
    135: bracket_utils.Placer(name="Tom Blaha", team="Frankfort"),
    145: bracket_utils.Placer(name="Darin Anderson", team="DeKalb Huntley"),
    155: bracket_utils.Placer(name="Pete Pasternak", team="Calumet City"),
    170: bracket_utils.Placer(name="Dave Seastrom", team="Palos"),
    185: bracket_utils.Placer(name="Dana Dunklau", team="Frankfort"),
    275: bracket_utils.Placer(name="Gary Wetzel", team="Oak Forest Warriors"),
}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    105: [
        bracket_utils.Placer(name="Joe Cascone", team="Vittum Vikings"),
        bracket_utils.Placer(name="C. Fisher", team="Byron WC"),  # ??
        bracket_utils.Placer(name="Paco Hernandez", team="Lockport"),  # ??
        bracket_utils.Placer(name="Pat Nestor", team="Sterling Newman"),  # ??
        bracket_utils.Placer(name="Sean Cunningham", team="DeKalb Rosette"),
        bracket_utils.Placer(name="Bob Marmolejo", team="West Chicago"),  # ??
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "TINLEY PARK": 149.0,
    "Panther WC": 129.0,
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
    _generate_placers_image(1983)

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

    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1983.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
