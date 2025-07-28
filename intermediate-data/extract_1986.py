# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
The competitor list (from scans from Corey Atwell) is contained below.
"""

import pathlib

import bracket_utils
from PIL import Image

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_COMPETITORS: dict[int, list[str | None]] = {
    60: [
        "Mike Dickinson :: Roxana Roughnecks",
        "Chris Cape :: Biue Crew WC",
        "Ernie Lopez :: Lockport Grapplers WC",
        "Justin Weber :: Villa Lombard WC :: 5",
        "Mike Kearby :: Round Lake Area PD",
        "Matt Hayes :: Arlington Cardinals WC",
        "Chad Red :: Danville Youth WC",
        "Ryan Meagher :: Orland Park Pioneers :: 1",
        "Andy Snook :: Geneseo WC",
        "Nathan Camer :: Colts WC",
        "Dan Collins :: Bronco WC :: 4",
        "Tom Grennan :: Newman Middle School",
        "Cory Daker :: Forman Wrestling Boosters :: 2",
        "Michael Shields :: Belleville Little Devils",
        "Phil Benjamin :: Catlin WC",
        "Steve Willard :: Harlem Boys Club :: 6",
        "Ben Green :: Patriot WC",
        "Dan Neybert :: Panther WC",
        "Ben Gerdes :: Orland Park Pioneers :: 3",
        "Jason Hospelhorn :: Redbird WC",
        "Jason Slade :: Cahokia WC",
        "Len Jankowski :: Vittum Cats",
        "Jason Eierman :: Colts WC",
        "Mike Renella :: Patriot WC",
    ],
    65: [
        "Eric Carter :: Roxana Roughnecks :: 4",
        "Chris Tointon :: Antioch Upper Grade",
        "Jesse Kennedy :: Rosemont Cobra Booster",
        "Mike French :: Mattoon WC",
        "James Crnich :: Oak Forest Warriors :: 6",
        "Chad Downey :: Wheaton Falcons",
        "Joey O'Sullivan :: Colts WC :: 2",
        "Lance Keating :: Arlington Cardinals WC",
        "Justin Zdeb :: Round Lake Area PD",
        "Jerrett Bernahl :: Geneseo WC",
        "Jim Virnich :: St. Charles Saints",
        "Michael Griffen :: Rich Wrestling Ltd.",
        "Nick Cina :: Belvidere Bandits :: 1",
        "Jason Johnson :: Roxana Roughnecks",
        "John Sroka :: Panther WC",
        "Jay Ford :: Rich Wrestling Ltd. :: 3",
        "John Stanley :: Mattoon WC",
        "Van Whitcanack :: Moline Booster",
        "Derek Noble :: Bronco WC",
        "Tim Stringer :: Dolton Wrestling Falcons :: 5",
        "Mike Dickinson :: Roxana Vikings",
        "Ryan Ferguson :: Medinah Lancer WC",
        "Brad Wernsman :: Metamora Kids Wrestling Club",
        "Kurt Hudson :: Redbird WC",
    ],
    70: [
        "Bryant Thomas :: Belleville Little Devils",
        "Dan Gilbert :: Tinley Park Bulldogs :: 3",
        "Randy Pierce :: Rantoul Rec. WC",
        "Keith Snyder :: Panther WC :: 1",
        "Bill Morris :: Bensenville Bulldogs",
        "Steve Leppert :: Thomas Jefferson JH",
        "Gene Bonnette :: Boys Club of Pekin :: 6",
        "Brad Oblak :: Villa Lombard WC",
        "Jim Soldan :: Frankfort Falcons WC",
        "Mike Pratt :: Round Lake Area PD",
        "Mike Vonebers :: Bloomington Jr. High",
        "Jamil Swift :: Bronco WC",
        "Luke Pascale :: Orland Park Pioneers :: 2",
        "Louie Montez :: Geneseo WC",
        "Tim Combes :: Dolton Wrestling Falcons",
        "Kurt Kalchbrenner :: Vittum Cats :: 4",
        "Brad Chasteen :: Edwardsville WC",
        "Mike Mena :: Newman Middle School",
        "Chris Solfa :: Batavia WC",
        "Kevin Ryan :: Colts WC :: 5",
        "Chris Hankins :: Granite City-Grigsby",
        "Phillip Schwing :: Fisher WC",
        "Jay Hansen :: Cardinals",
        "Damien Prieto :: Moline Booster",
    ],
    75: [
        "Ryan Smith :: Roxana Vikings",
        "Dan Walters :: Panther WC",
        "Jamie Malady :: Harlem Boys Club",
        "Steve Gerstung :: Arlington Cardinals WC",
        "Brian Brummitt :: Crossface WC :: 6",
        "Pat O'Donnel :: Oak Forest Warriors",
        "Richard Weeden :: Villa Lombard WC :: 4",
        "Jared Gratz :: Harvard WC",
        "Mike Eierman :: Colts WC :: 2",
        "Peter Stanley :: Mattoon WC",
        "Josh Mattio :: Rich Wrestling Ltd.",
        "Jeff Day :: Morton Youth WC",
        "Bill Walsh :: Panther WC :: 1",
        "Sean Duggan :: St. Tarcissus Raiders",
        "Steve Kuhl :: Roxana Roughnecks",
        "Shay Cordes :: East Moline WC :: 5",
        "Douglas Sawyer :: Villa Lombard WC",
        "Aaron Johnson :: Hoopeston-East Lynn Jr.",
        "Martin Sanchez :: Belvidere Bandits :: 3",
        "Timothy Currie :: Redbird WC",
        "Bill Graham :: J-Stream",
        "Ralph Wals :: Lockport Grapplers WC",
        "Todd Hutchison :: Granite City-Grigsby",
        "Dan Parker :: OPRF Jr. Wrestling Club",
    ],
    80: [
        "Jason Warner :: Roxana Vikings",
        "Jerry Gille :: Belvidere Bandits",
        "Charles Ciardetti :: Lan-Oak PD",
        "Chris Shefts :: Rich Wrestling Ltd. :: 5",
        "Marshall Mayfield :: Mt. Zion WC",
        "Russell Sweeney :: Morton Youth WC",
        "Dan Pargulski :: Arlington Cardinals WC :: 3",
        "Brent Laroche :: Panther WC :: 2",
        "Scott Benjamin :: Catlin WC",
        "Christopher Perry :: Patriot WC",
        "Troy Glover :: Morton Youth WC",
        "Brandon Singer :: Dundee Highlanders",
        "Josh Chestney :: Redbird WC",
        "Scott Wlson :: Lakeland Cardinals",
        "Richard Alexander :: OPRF Jr. Wrestling Club",
        "Steve Williams :: Harvey Twisters :: 1",
        "John Virnich :: St. Charles Saints",
        "Scott Churlin :: Rich Wrestling Ltd.",
        "Shane Daker :: Forman Wrestling Boosters :: 6",
        "Mike Torres :: Vittum Cats",
        "Lance Pfeifer :: Batavia WC",
        "Ray Callahan :: DeKalb Wrestling :: 4",
        "Jeff Finley :: Orland Park Pioneers",
        "Dominic Dunnavant :: Granite City-Coolidge",
    ],
    85: [
        "Steve Brito :: Roxana Roughnecks :: 4",
        "Herb House :: OPRF Jr. Wrestling Club",
        "Doug Griffith :: Lan-Oak PD",
        "Glenn Klopp :: Geneseo WC",
        "Bob Domena :: Tomcat WC",
        "Densel Herald :: Bloomington Jr. High :: 6",
        "Jeff Mirabella :: Elgin WC :: 1",
        "Cory Roop :: Redbird WC",
        "Chuck Collins :: Bronco WC",
        "Ken Gerdes :: Orland Park Pioneers",
        "Dennis Slomski :: Oak Lawn PD",
        "Brian Stabich :: Eisenhower Jr. High",
        "Tom Buenik :: Vittum Cats :: 3",
        "Cass Lundgren :: DeKalb Wrestling :: 2",
        "Tony Stone :: Rockridge Jr. High",
        "Mike Schomig :: Wheaton Falcons",
        "Shawn Daly :: Peotone PD WC",
        "Larry Wright :: Granite City-Grigsby",
        "Tray Chesser :: Taylorville WC",
        "Chris Wilson :: Roxana Roughnecks",
        "Paul Blaha :: Frankfort Falcons WC",
        "Mike D'Angelo :: St. Bede's",
        "Brooke Hoerr :: Morton Youth WC",
        "Kelly Hamill :: Belvidere Bandits :: 5",
    ],
    90: [
        "Derek Baugh :: Edwardsville WC",
        "Dustin Schadt :: Naperville Wrestlers",
        "Alvin Jones :: Harvey Twisters",
        "Sam Walt :: DeKalb Wrestling :: 4",
        "Shane Diepholz :: Mattoon WC",
        "Jayson Querciagrossa :: Razorbacks",
        "Richard Harris :: Tinley Park Bulldogs :: 2",
        "Bucky Parsons :: Lan-Oak PD",
        "Jason Kuefler :: Patriot WC",
        "Tim Guryn :: Vittum Cats :: 5",
        "Aaron Rasmussen :: Rockridge Jr. High",
        "Joey Yeager :: Urbana Kid Wrestling",
        "David Sullivan :: Patriot WC",
        "Todd Hughes :: Murphysboro Jr. High",
        "Jeremy Chambers :: Frankfort Falcons WC",
        "Erik Hill :: Catlin WC",
        "John Rizzo :: Cardinals",
        "Ken Lewis :: Arlington Cardinals WC :: 6",
        "Jason Bever :: Colts WC",
        "Roger Dourlet :: Oak Forest Warriors :: 3",
        "Scott Schwab :: Belleville Little Devils",
        "Jett Walles :: Geneseo WC",
        "Chris Buenik :: Vittum Cats :: 1",
        "Mike Cain :: Antioch Upper Grade",
    ],
    95: [
        "Mark Smith :: Granite City-Grigsby",
        "Kipp Wahlgren :: Tigertown Tanglers",
        "Louie Vela :: Lockport Wrestling Club",
        "Rody Rodriguez :: Tomcat WC :: 4",
        "Tim Creighton :: Dundee Highlanders :: 6",
        "Brian Moreno :: Matburns WC",
        "Eric Short :: Bloomington Jr. High",
        "Rob Felstead :: Oak Forest Warriors",
        "Matt McClister :: Boys Club of Pekin",
        "Ed Minet :: Panther WC :: 1",
        "Will Lepsi :: Vittum Cats",
        "Kevin Fitzgerald :: Elgin WC",
        "Jason Roberson :: Moline Booster :: 5",
        "Bryan Kohring :: Murphysboro Jr. High",
        "James Cochran :: Bloomington Jr. High",
        "Jason Troye :: Sterling Warrior WC",
        "Brian Griffin :: Batavia WC",
        "Bill Dudeck :: Hazel Crest Jr. Hawks",
        "Ed Flynn :: Tinley Park Bulldogs",
        "John Miller :: Westville Jr. High",
        "Tom Cochran :: Murphysboro Jr. High",
        "Tony Chierico :: Vittum Cats :: 2",
        "Ray Broukal :: Colts WC :: 3",
        "Phillip Bartlett :: St. Charles Saints",
    ],
    100: [
        "Scott Ventimiglia :: Roxana Roughnecks :: 5",
        "Brett McCammen :: Harvard WC",
        "Travis Riordon :: Arlington Cardinals WC",
        "Scott Wilson :: Hoopeston-East Lynn Jr.",
        "Dan Collofello :: Lockport Wrestling Club",
        "John Meiser :: Naperville Wrestlers",
        "Jim Czajkowski :: Panther WC :: 1",
        "Craig Swenson :: Franklin Park Raiders",
        "Scott Collins :: Round Lake Area PD",
        "Steve McDonnell :: Moline Booster :: 3",
        "Todd Farls :: Razorbacks",
        "John Kucala :: Mokena WC",
        "Mark Rios :: Sterling Warrior WC :: 4",
        "Lenord Rawlings :: Bethalto Boys Club",
        "Ed Enright :: Colts WC",
        "Andy Bednarczyk :: Tinley Park Bulldogs",
        "Tim Mitra :: Lanphier-Southeast WC",
        "Brad Dzedunskas :: East Moline WC",
        "Kevin Bracken :: Vittum Cats",
        "Robert O’Connor :: Oak Lawn PD",
        "Bob Nelson :: Edwardsville WC",
        "Darren Ferguson :: Medinah Lancer WC :: 2",
        "Mike Tumilty :: Boys Club of Pekin :: 6",
        "Travis Wilson :: Champaign WC",
    ],
    105: [
        "Richard Carlile :: Bethalto Boys Club",
        "Bret Geijer :: Tinley Park Bulldogs",
        "Duane Parks :: Bradley Bourbonnais WC",
        "Joseph Penkala :: Calumet Memorial PD",
        "Frank Olsen :: Niles WC",
        "Tony Sanders :: Indian Prairie WC :: 2",
        "Henry Stropes :: Rockridge Jr. High",
        "Rob Crnic :: Villa Lombard WC",
        "Curt Ivins :: Indian Trail Jr. High",
        "Tim O'Malley :: Sterling Warrior WC :: 4",
        "Dion Simmons :: Decatur WC :: 5",
        "Timothy Marino :: Franklin Park Raiders",
        "Greg Licciardello :: Tinley Park Bulldogs :: 6",
        "Donnie Wilson :: Morton Youth WC",
        "Steven Hock :: Panther WC",
        "Vince Cascone :: Vittum Cats :: 3",
        "Travis Stockstill :: Bethalto Boys Club",
        "Matt Sell :: DeKalb Wrestling",
        "Hector Saldana :: Tomcat WC :: 1",
        "Larry Brendt :: Panther WC",
        "Brian Moeghlin :: Murphysboro Jr. High",
        "Priest Wilson :: Georgetown WC",
        "Brian Lucas :: Dundee Highlanders",
        "Chris Irland :: Moline Booster",
    ],
    111: [
        "Jeremy Ufert :: Roxana Roughnecks :: 5",
        "Ramon Terry :: Harvey Twisters :: 3",
        "David Cavazos :: Sterling Warrior WC",
        "Marc Tadelman :: Niles WC",
        "Troy Christropherson :: Geneseo WC",
        "Tim Fix :: Indian Trail Jr. High",
        "Chris Hruska :: Medinah Lancer WC :: 1",
        "Roger Votaw :: DeKalb Wrestling",
        "Joe Gatz :: Lan-Oak PD",
        "Woody Bagwell :: Unity Youth Wrestling",
        "Michael Miklos :: Mokena WC",
        "Rob McDonald :: Turk Wrestling Club",
        "Tim Houston :: Oak Lawn PD :: 2",
        "Pete Montgomery :: Arlington Cardinals WC",
        "Jon Martin :: Murphysboro Jr. High",
        "Jeff Sutherland :: Razorbacks :: 6",
        "Chris Galetto :: Patriot WC",
        "Jon Ridgeway :: Bloomington Jr. High",
        "Shawn Condon :: Harvard WC :: 4",
        "Bob Howell :: Mt. Zion WC",
        "David Suthard :: Thomas Jefferson JH",
        "Andy Koning :: Lockport Grapplers WC",
        "Bill Ramirez :: Cahokia WC",
        "Todd D'Aprile :: Lions WC",
    ],
    118: [
        "Mike Mitchell :: Cahokia WC :: 4",
        "Marc Braun :: Harvard WC",
        "Albert Nelson :: Dolton Wrestling Falcons",
        "Bob Bartkowiak :: Oak Forest Warriors :: 1",
        "Daniel Stricklett :: Westville Jr. High",
        "Chris McFarland :: Crossface WC",
        "Tom Matsuda :: OPRF Jr. Wrestling Club",
        "Ken Maas :: Hazel Crest Jr. Hawks",
        "Natan Fonvile :: Greenwood / Tumaro WC :: 5",
        "Dean Callis :: Villa Lombard WC",
        "John Mettes :: Chillicothe WC",
        "Justin Keck :: DeKalb Wrestling",
        "Kurt Miller :: Hoopeston-East Lynn Jr.",
        "Doug Edwards :: Granite City-Coolidge",
        "Tom Gigiano :: Franklin Park Raiders",
        "Lamon Terry :: Harvey Twisters :: 2",
        "Rob Major :: Batavia WC",
        "Vic Sebastian :: Peotone PD WC",
        "Richard Rollyson :: Forman Wrestling Boosters :: 3",
        "James Boyd Jr. :: Bensenville Bulldogs",
        "Glen Michiels :: Villa Lombard WC",
        "Sam Berkland :: Lil Reaper WC :: 6",
        "Sean Chiarodo :: Rich Wrestling Ltd.",
        "Chris Duncan :: Roxana Roughnecks",
    ],
    125: [
        "Byron Overton :: Wilbur Trimpe JH :: 3",
        "Rad Watkins :: OPRF Jr. Wrestling Club",
        "Danny Minet :: Panther WC",
        "Corey Atwell :: Geneseo WC :: 1",
        "Pat Holden :: Patriot WC",
        "Jason Owens :: Bismarck-Henning WC",
        "Dan Lemon :: Lil Reaper WC",
        "David Frizzell :: Bloomington Jr. High",
        "Mike Barcena :: Vittum Cats",
        "Andres Garcia :: Rich Wrestling Ltd. :: 6",
        "Tom Koziol :: Hickory Hills",
        "Bill Czyzyk :: Villa Lombard WC",
        "Pat Duggan :: St. Tarcissus Raiders :: 4",
        "Matt Shafer :: Northwood Warhawks WC",
        "John Jacobs :: Boys Club of Pekin",
        "Bryan Rebhan :: Naperville Warhawks",
        "Ted Vantilburg :: Indian Trail Jr. High",
        "Jeff Thompson :: Granite City-Grigsby",
        "Chad Pitcher :: Champaign WC",
        "James Bratten :: Edwardsville WC",
        "George Hollendoner :: Tinley Park Bulldogs",
        "Tuhan Waller :: Harvey Twisters :: 2",
        "Barty Shaffer :: Chillicothe WC",
        "Mike Jones :: Harvard WC :: 5",
    ],
    135: [
        "Chris Hottman :: Granite City-Coolidge",
        "Dan Lavery :: Eisenhower Jr. High",
        "Larry Parham :: Dolton Wrestling Falcons",
        "Walter Pollach :: Barrington Colts :: 2",
        "Chad Acree :: Gibson City Youth WC",
        "Scott Bluhm :: Delavan Mat Rats WC",
        "Nick Nieponski :: Tinley Park Bulldogs :: 6",
        "Craig Mihaljevich :: Dolton Wrestling Falcons",
        "Jay McLaughlin :: Cooper's Cougars",
        "James Walton :: OPRF Jr. Wrestling Club :: 3",
        "Stan Olive :: Rockridge Jr. High",
        "Hugo Garcia :: Hoopeston-East Lynn Jr.",
        "Scott Gardner :: Patriot WC :: 4",
        "Richard Dunnavant :: Edwardsville WC",
        "Jeff Haag :: Peotone PD WC",
        "Lane Murray :: Bloomington Jr. High :: 5",
        "Jason Keck :: DeKalb Wrestling",
        "Chad Arnholt :: OPRF Jr. Wrestling Club",
        "Eugene Browning :: Harvey Twisters :: 1",
        "Brad Blankenship :: Indian Trail Jr. High",
        "Jeff Baker :: Wilbur Trimpe JH",
        "Greg Herr :: Geneseo WC",
        "Gregory Lechtenberg :: Franklin Park Raiders",
        "Chad Gautcher :: Sycamore WC",
    ],
    145: [
        "Travis Simmons :: Murphysboro Jr. High",
        "Doug Thomer :: Jordan WC",
        "Keith Hermansen :: Lemont Bears WC",
        "Geoffrey Matson :: Patriot WC :: 3",
        "Matt Wallace :: DeKalb Wrestling",
        "Jason De Bello :: Bensenville Bulldogs",
        "Scott Davis :: Gibson City Youth WC",
        "Rich Mishka :: Oak Forest Warriors",
        "Matt Salmon :: Geneseo WC",
        "Craig Manz :: Panther WC :: 1",
        "Rich Cisek :: Vittum Cats",
        "Kurt Schmotzer :: Yorkville WC :: 5",
        "Dave Schmidt :: Moline Booster :: 4",
        "Tony Vogel :: Wilbur Trimpe JH",
        "Mario Fillipponi :: Redbird WC",
        "Kurt Schardt :: Belvidere Bandits",
        "Glen Mundell :: Batavia WC",
        "John Lewis :: Robbin Eagles",
        "Rich Flores :: Oak Forest Warriors :: 2",
        "Rob Bykowski :: Bloomington Jr. High",
        "Justin Smart :: Roxana Vikings",
        "Joe Ramos :: Vittum Cats :: 6",
        "Matthew Kundrat :: Calumet Memorial PD",
        "Ray Soto :: Cooper's Cougars",
    ],
    155: [
        "Sean McGraw :: Wilbur Trimpe JH",
        "Josh Willman :: Newman Middle School",
        "Mark Register :: OPRF Jr. Wrestling Club",
        "Jeff Hursh :: Bloomington Jr. High :: 5",
        "Tony Bocek :: Tinley Park Bulldogs",
        "Jeff Bratz :: Eisenhower Jr. High",
        "John Vanderwall :: Midlothian Saints :: 3",
        "Xavier Bolando :: OPRF Jr. Wrestling Club",
        "Russ Bannister :: DeKalb Wrestling",
        "Kirk Stevens :: Tigertown Tanglers :: 1",
        "Joe Kaplinski :: Patriot WC",
        "Dan Bogdanic :: Oak Forest Warriors",
        "Eric DeGelder :: Northwood Warhawks WC",
        "Pat Lawrence :: Roxana Vikings",
        "Scott Niemoth :: Crestwood Wrestling",
        "Ed Marevka :: Peotone PD WC :: 2",
        "Chad Hale :: Mt. Zion WC",
        "Charlie Vedder :: Turk Wrestling Club :: 6",
        "Rich Kim :: St. Tarcissus Raiders :: 4",
        "Ed Lynch :: Panther WC",
        "Heath Neibch :: West Frankfort WC",
        "Todd Knill :: Wheaton Falcons",
        "James Walker :: Geneseo WC",
        "Zack Hileman :: Bloomington Jr. High",
    ],
    170: [
        "Ian Blache :: Carbondale Park District :: 4",
        "Brian Byjak :: Rich Wrestling Ltd.",
        "Donald Frichtl :: Champaign WC",
        None,
        "Paul Silich :: St. Tarcissus Raiders",
        "Sony Nuccio :: Thomas Jefferson JH :: 6",
        "Jason Lewis :: Moline Booster",
        "Greg Gresock :: Batavia WC :: 2",
        "Joseph Huber :: Bloom Trail Kids",
        "Jamie Poff :: DeKalb Wrestling",
        "David Stiles :: Bloomington Jr. High",
        "Antony Hayes :: OPRF Jr. Wrestling Club",
        "Jehad Hamdan :: Lemont Bears WC :: 1",
        "Clint Petersen :: Tigertown Tanglers",
        None,
        "Ted Galicia :: Matburns WC :: 5",
        "Mike Lavite :: Edwardsville WC",
        "Rob Way :: Cardinals",
        "John Paulak :: Batavia WC :: 3",
        None,
        "Joe Regna :: Edwardsville WC",
        "Timothy Platz :: Mattoon WC",
        "Peter Henze :: Lil Reaper WC",
        "Kevin Parker :: Geneseo WC",
    ],
    185: [
        "Ron Johnson :: Edwardsville WC",
        "Alan Gotsch :: Oak Lawn PD",
        "John Parvin :: Sterling Warrior WC",
        "Christopher Ziegler :: Bensenville Bulldogs :: 1",
        "Jason Radford :: Turk Wrestling Club",
        "Mike Moeller :: Indian Trail Jr. High",
        "Kevin Renner :: Cooper's Cougars :: 3",
        "Justin Mitchel :: DeKalb Wrestling :: 6",
        None,
        "Juan Molina :: Unity Youth Wrestling",
        "Matt Wilke :: Mokena WC",
        "Matt Newberry :: Jordan WC",
        "Erik Whitehead :: Lan-Oak PD",
        "Jay Ford :: Vittum Cats",
        "Kelly Reliford :: Wilbur Trimpe JH",
        "Matt Yanick :: Morton Youth WC",
        "Brad Gray :: Batavia WC :: 2",
        "Robert Brooks :: Westville Jr. High",
        "Scott Novak :: Lil Reaper WC",
        "Michael Clayion :: Taylorville WC",
        "Larry Mosko :: Indian Prairie WC :: 4",
        "Ken Barry :: Oak Forest Warriors",
        "Matt Cripps :: Murphysboro Jr. High",
        "Jason Miller :: Bensenville Bulldogs :: 5",
    ],
    275: [
        "Travis LaPierre :: Edwardsville WC",
        "Bernie Engh :: DeKalb Wrestling :: 2",
        None,
        "Tom Theres :: Indian Trail Jr. High :: 4",
        "Jason Crawlord :: Decatur WC",
        "Terry Hutter :: Boys Club of Pekin",
        "George Brady :: Lions WC",
        None,
        "John Taylor :: Bloomington Jr. High :: 6",
        "Chad McCrimmon :: Black Hawk WC",
        "Travis Leopard :: Rockridge Jr. High",
        "Brian Bohn :: Sterling Warrior WC",
        "Gary Cole :: Bismarck-Henning WC",
        "Kevin Sanders :: Wilbur Trimpe JH",
        "Godfrey Williams :: OPRF Jr. Wrestling Club :: 5",
        "Carl Tiderman :: Panther WC",
        "Terry Durkin :: Eisenhower Jr. High",
        None,
        "Kevin Scott :: Geneseo WC :: 3",
        "Phil Sisto :: Matburns WC",
        "Willie Barnes :: Batavia WC",
        "Brian Rose :: Elgin WC :: 1",
        "Tomas Bylaitis :: Lemont Bears WC",
        "Mike Lamere :: Wilbur Trimpe JH",
    ],
}
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
    _generate_placers_image(1986)

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
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
    with open(_HERE / "extracted.1986.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
