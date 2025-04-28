# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    60: [
        bracket_utils.Placer(name="Marc Zehr", team="Arlington Cardinals"),
        bracket_utils.Placer(name="Gerry Hilton", team="Thornwood Kids"),
        bracket_utils.Placer(name="Daniel Burland", team="Bartonville Blue Crew"),
        bracket_utils.Placer(name="Joey Sukley", team="Indian Trail Wild Cats"),
        bracket_utils.Placer(name="Ryan Delira", team="Dolton Park"),
        bracket_utils.Placer(name="Todd Combes", team="Dolton Park"),
    ],
    64: [
        bracket_utils.Placer(name="Milton Blakely", team="Harvey Twisters"),
        bracket_utils.Placer(name="Jim Aberle", team="Round Lake Area P.D."),
        bracket_utils.Placer(name="Francisco Bermudez", team="Lockport Grapplers"),
        bracket_utils.Placer(name="James Johnson", team="Crossface"),
        bracket_utils.Placer(name="Brian Hastings", team="Vittum Cats"),
        bracket_utils.Placer(name="Michael Bondi", team="Dundee Highlanders"),
    ],
    68: [
        bracket_utils.Placer(name="Tony Davis", team="Harvey Twisters"),
        bracket_utils.Placer(name="Tommy Lee", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Jim Brasher", team="Vittum Cats"),
        bracket_utils.Placer(name="Mike Hasty", team="Morton Youth"),
        bracket_utils.Placer(name="John Ivers", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="John Fair", team="Dundee Highlanders"),
    ],
    72: [
        bracket_utils.Placer(name="Russell Guerrero", team="West Chicago Wildcats"),
        bracket_utils.Placer(name="Tom Marek", team="Arlington Cardinals"),
        bracket_utils.Placer(name="Chad Red", team="Danville Youth"),
        bracket_utils.Placer(name="Thomas Grennan", team="Newman Blue Devils"),
        bracket_utils.Placer(name="Terrance O'Brien", team="Panther W.C."),
        bracket_utils.Placer(name="Jareo Camer", team="Mustangs W.C."),
    ],
    77: [
        bracket_utils.Placer(name="Thomas Combes", team="Dolton Park"),
        bracket_utils.Placer(name="Jason Chappell", team="Villa-Lombard Cougars"),
        bracket_utils.Placer(name="Jason Pero", team="Harvey Twisters"),
        bracket_utils.Placer(name="Ben King", team="Lions W.C."),
        bracket_utils.Placer(name="Brad Schnowske", team="Geneseo"),
        bracket_utils.Placer(name="Jim Ancona", team="Lancers W.C."),
    ],
    82: [
        bracket_utils.Placer(name="Justin Weber", team="Villa-Lombard Cougars"),
        bracket_utils.Placer(name="Ben Gerdes", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Mark Bybee", team="Vittum Cats"),
        bracket_utils.Placer(name="Dan Collins", team="Arlington Cardinals"),
        bracket_utils.Placer(name="Jimmy Knapp", team="Mid-Markham Apaches"),
        bracket_utils.Placer(name="Bobby Remily", team="Harlem Boys Club"),
    ],
    87: [
        bracket_utils.Placer(name="Michael French", team="Mattoon W.C."),
        bracket_utils.Placer(name="Jason Eierman", team="Mustangs W.C."),
        bracket_utils.Placer(name="Mike Triolo", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Matt Atilano", team="Newman Blue Devils"),
        bracket_utils.Placer(name="Kurt Hudson", team="Redbird"),
        bracket_utils.Placer(name="Jim Wissig", team="Arlington Cardinals"),
    ],
    93: [
        bracket_utils.Placer(name="Nicholas Cina", team="YMCA Bandits"),
        bracket_utils.Placer(name="Mickey Griffin", team="Rich Wrestling LTD"),
        bracket_utils.Placer(name="Brent Henschel", team="Mt. Zion"),
        bracket_utils.Placer(name="Jeff Harvey", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Curtis Owen", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="Kevin Barrales", team="Mid-Markham Apaches"),
    ],
    99: [
        bracket_utils.Placer(name="Curt Bee", team="Lanphier-Springfield"),
        bracket_utils.Placer(name="Jesse Kennedy", team="Rosemont Cobras"),
        bracket_utils.Placer(name="Peter Smith", team="Carbondale"),
        bracket_utils.Placer(name="Ben Kulbartz", team="Oswego Cougars"),
        bracket_utils.Placer(name="Kevin Level", team="Mid-Markham Apaches"),
        bracket_utils.Placer(name="Todd Hillard", team="Bismarck Henning"),
    ],
    105: [
        bracket_utils.Placer(name="Bucky Randolph", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Eric Caldwell", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Eric Kubatzke", team="Geneseo"),
        bracket_utils.Placer(name="Israel Castro", team="Elgin Matt Rats"),
        bracket_utils.Placer(name="Jay Hansen", team="Woodstock Cardinals"),
        bracket_utils.Placer(name="Theo Hodges", team="OPRF Warhawks"),
    ],
    112: [
        bracket_utils.Placer(name="Scott Radosevich", team="Vittum Cats"),
        bracket_utils.Placer(name="Mike Douglas", team="Harvey Twisters"),
        bracket_utils.Placer(name="Joel Stockwell", team="Riverdale Rams"),
        bracket_utils.Placer(name="Robert Ott", team="Indian Prairie T'Blazers"),
        bracket_utils.Placer(name="Gary Bailey", team="Round Lake Area P.D."),
        bracket_utils.Placer(name="Joe Bee", team="Lanphier-Springfield"),
    ],
    119: [
        bracket_utils.Placer(name="John Stickler", team="Riverdale Rams"),
        bracket_utils.Placer(name="Courtney Taylor", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="David Robinson", team="Harvey Twisters"),
        bracket_utils.Placer(name="Brian Weiskopf", team="Warhawk W.C. Woodstock"),
        bracket_utils.Placer(name="Roger Pascual", team="Arlington Cardinals"),
        bracket_utils.Placer(name="Beau Wright", team="Bismarck Henning"),
    ],
    127: [
        bracket_utils.Placer(name="Lenard Randall", team="Harvey Twisters"),
        bracket_utils.Placer(name="Andy Buschon", team="Taylorville"),
        bracket_utils.Placer(name="Devon Herman", team="St. Charles J.H."),
        bracket_utils.Placer(name="Johnny Milam", team="Wheaton Warrenville"),
        bracket_utils.Placer(name="Ryan Pape", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="Chris Rink", team="Carbondale"),
    ],
    135: [
        bracket_utils.Placer(name="Joseph Williams", team="Harvey Twisters"),
        bracket_utils.Placer(name="Eric Johnson", team="Bismarck Henning"),
        bracket_utils.Placer(name="Ryan Followell", team="Murphysboro Jr. High"),
        bracket_utils.Placer(name="Chris Capps", team="Dundee Highlanders"),
        bracket_utils.Placer(name="Kasey Alexander", team="Mattoon W.C"),
        bracket_utils.Placer(name="Kyle Ryan", team="Wheaton-Warrenville"),
    ],
    144: [
        bracket_utils.Placer(name="Joseph Cartwright", team="OPRF Warhawks"),
        bracket_utils.Placer(name="Dustin Keenan", team="Tomcat W.C."),
        bracket_utils.Placer(name="Troy Wienk", team="YMCA Bandits"),
        bracket_utils.Placer(name="T.J. Ribbe", team="Bismarck Henning"),
        bracket_utils.Placer(name="Chris Klaska", team="Decatur"),
        bracket_utils.Placer(name="Jason Hart", team="Indian Trail Wildcats"),
    ],
    153: [
        bracket_utils.Placer(name="Tracy Sanborn", team="Belleville Little Devils"),
        bracket_utils.Placer(name="Joe Adkins", team="Edwardsville"),
        bracket_utils.Placer(name="Josh Charlton", team="Forman W.C."),
        bracket_utils.Placer(name="Scott Wulft", team="Panther Oswego"),
        bracket_utils.Placer(name="Brian Rochacz", team="Hickory Hills P.D."),
        bracket_utils.Placer(name="Jayme Sondag", team="Forman W.C."),
    ],
    163: [
        bracket_utils.Placer(name="Joe O'Rourke", team="Mustangs W.C."),
        bracket_utils.Placer(name="Dan Hollendoner", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Mike Vakos", team="Naperville Patriots"),
        bracket_utils.Placer(name="Mike Miller", team="Westville Jr. High"),
        bracket_utils.Placer(name="Sean Kuriger", team="Indian Trail Wildcats"),
        bracket_utils.Placer(name="Casey Inch", team="Geneseo"),
    ],
    173: [
        bracket_utils.Placer(name="Pedro Martinez", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Justin Chambers", team="OPRF Warhawks"),
        bracket_utils.Placer(name="Enrique Melgoza", team="Indian Trail Wildcats"),
        bracket_utils.Placer(name="Aaron Franz", team="Redbird"),
        bracket_utils.Placer(name="Albert Mendoza", team="Dolton Park"),
        bracket_utils.Placer(name="Matt Feltz", team="Harlem Sch. Dist."),
    ],
    185: [
        bracket_utils.Placer(name="Jeff Staffeldt", team="Indian Prairie Pioneers"),
        bracket_utils.Placer(name="Matthen Sheets", team="Downers Grove P.D. Cougars"),
        bracket_utils.Placer(name="Philip Lagioia", team="Mead W.C."),
        bracket_utils.Placer(name="Eddie Beltran", team="Hinsdale Falcons"),
        bracket_utils.Placer(name="Andrew Seibert", team="Carbondale"),
        bracket_utils.Placer(name="Mike Scaggs", team="Knights"),
    ],
    275: [
        bracket_utils.Placer(name="Hillus Butler", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Glen Pryor", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Jason Owen", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="John Carlson", team="Harlem Sch. Dist"),
        bracket_utils.Placer(name="Chad Richards", team="Mt. Zion"),
        bracket_utils.Placer(name="Chris Landis", team="Bismarck Henning"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Harvey Twisters": 194.5,
    "Aurora J-Hawks": 139.5,
    "Dolton Park Falcons": 108.0,  # Was `Dolton Park Wrestlers` in program
    "Vittum Cats WC": 108.0,
    "Tinley Park Bulldogs": 106.0,
    "Arlington Cardinals WC": 102.0,
    "Bismarck Henning WC": 85.0,
    "Indian Trail Wildcats": 77.0,
    "Oak Forest Warriors": 77.0,
    "Edwardsville": 66.0,
    "Villa Lombard Cougars WC": 65.5,
    "Geneseo WC": 65.0,
    "Mustangs WC": 65.0,
    "OPRF Warhawks JR WC": 64.0,
    "Carbondale WC": 63.5,
    "Mid-Markham Apaches": 63.5,
    "Forman WC": 57.5,
    "YMCA Bandits Wrestling": 56.0,
    "Riverdale (Rams) Jr. High": 55.0,
    "Tomcats WC": 55.0,  # Was `Tomcat WC` in program
    "Franklin Park Raiders": 53.0,
    "Mattoon WC": 53.0,
    "Redbird": 46.0,
    "Mt. Zion WC": 45.0,
    "Harlem School District": 44.5,  # Was `Harlam` in program
    "Newman Blue Devils": 44.0,
    "Lockport Grapplers WC": 41.5,
    "Dundee Highlanders": 40.0,
    "Round Lake Area PD": 40.0,
    "Rosemont Cobras": 39.0,
    "Lanphier-Springfield WC": 38.5,
    "Bethalto Boys Club": 35.0,
    "St. Charles JH WC": 34.0,
    "Wheaton-Warrenville Wrestling": 33.5,
    "Murphysboro Jr. High": 33.0,
    "Belleville Little Devils": 31.0,
    "Indian Prairie Pioneers": 31.0,
    "Panther WC": 29.0,
    "Indian Prairie Trailblaze": 28.0,
    "Rich Wrestling Ltd": 28.0,
    "Thornwood Kids WC": 26.5,
    "Meade Jr. WC": 26.0,
    "Knights WC": 25.0,
    "Downers Grove PD Cougars": 24.0,
    "Taylorville WC": 24.0,
    "West Chicago Wildcats": 24.0,
    "Decatur WC": 23.0,
    "Westville Jr. High": 23.0,
    "Naperville Patriots": 22.5,
    "Lions WC (LaGrange)": 22.0,
}


def main():
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
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1989.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
