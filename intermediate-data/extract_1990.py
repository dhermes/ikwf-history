# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    60: [
        bracket_utils.Placer(name="Todd Combes", team="Dolton Park Falcons"),
        bracket_utils.Placer(
            name="Leonard Bowens", team="Harvey Park District Twisters"
        ),
        bracket_utils.Placer(name="Michael Mathews", team="Naperville Patriots WC"),
        bracket_utils.Placer(name="John Murphy", team="Lockport Grapplers WC"),
        bracket_utils.Placer(name="Michael Murphy", team="Lockport Grapplers WC"),
        bracket_utils.Placer(name="Anthony Opiola", team="Dolton Park Falcons"),
    ],
    64: [
        bracket_utils.Placer(name="Matt Goldstein", team="Little Giants WC"),
        bracket_utils.Placer(
            name="David Douglas", team="Harvey Park District Twisters"
        ),
        bracket_utils.Placer(name="Sean Hastings", team="Vittum Cats"),
        bracket_utils.Placer(name="Chris Bonati", team="Dundee Highlanders"),
        bracket_utils.Placer(name="Gerry Hilton", team="Thornwood Kids WC"),
        bracket_utils.Placer(name="Ryan DeLira", team="Dolton Park Falcons"),
    ],
    68: [
        bracket_utils.Placer(name="Marc Zehr", team="Arlington Cardinals"),
        bracket_utils.Placer(name="Francisco Bermudez", team="Lockport Grapplers WC"),
        bracket_utils.Placer(name="Danny Borland", team="Blue Crew WC"),
        bracket_utils.Placer(name="Jim Aberle", team="Round Lake Spartans"),
        bracket_utils.Placer(
            name="Milton Blakely", team="Harvey Park District Twisters"
        ),
        bracket_utils.Placer(name="Joel Howard", team="Naperville Patriots WC"),
    ],
    72: [
        bracket_utils.Placer(name="Tony Davis", team="Harvey Park District Twisters"),
        bracket_utils.Placer(name="Jim Gahagan", team="Vittum Cats"),
        bracket_utils.Placer(name="Matthew Wegner", team="Warrior WC Niles"),
        bracket_utils.Placer(name="Alan Cartwright", team="OPRF Warhawks"),
        bracket_utils.Placer(name="Tommy Lee", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Tim Glover", team="Morton Youth Wrestling"),
    ],
    77: [
        bracket_utils.Placer(name="Don Bermudez", team="Lockport Grapplers WC"),
        bracket_utils.Placer(name="Thomas Grennan", team="Newman Blue Devils"),
        bracket_utils.Placer(name="Blake Hoerr", team="Chillicothe Wrestling"),
        bracket_utils.Placer(
            name="Durand Womack", team="Harvey Park District Twisters"
        ),
        bracket_utils.Placer(name="Jim Brasher", team="Vittum Cats"),
        bracket_utils.Placer(name="Andrew O'Malley", team="St. Barnabas"),
    ],
    82: [
        bracket_utils.Placer(name="Jason Pero", team="Harvey Park District Twisters"),
        bracket_utils.Placer(name="Javier Quintanilla", team="Tomcat WC"),
        bracket_utils.Placer(name="Bradley Schnowske", team="Geneseo WC"),
        bracket_utils.Placer(name="Patrick Sheahan", team="St. Barnabas"),
        bracket_utils.Placer(name="Rafael Avila", team="Belvidere YMCA Bandits"),
        bracket_utils.Placer(name="Reginald Wright", team="OPRF Warhawks"),
    ],
    87: [
        bracket_utils.Placer(name="Tyler Hurry", team="Riverdale Jr. High WC"),
        bracket_utils.Placer(name="Mark Bybee", team="Vittum Cats"),
        bracket_utils.Placer(name="Terry O'Brien", team="Panther WC"),
        bracket_utils.Placer(name="Ronnie Hansen", team="Edwardsville"),
        bracket_utils.Placer(name="Mark Pishotta", team="Rosemont Cobras WC"),
        bracket_utils.Placer(name="Robbie Cox", team="Belvidere YMCA Bandits"),
    ],
    93: [
        bracket_utils.Placer(name="Dan Collins", team="Arlington Cardinals"),
        bracket_utils.Placer(name="James Crnich", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Joseph Opiola", team="Dolton Park Falcons"),
        bracket_utils.Placer(name="Stephen Stanley", team="Mattoon WC"),
        bracket_utils.Placer(name="Ken Biala", team="Villa-Lombard Cougars"),
        bracket_utils.Placer(
            name="Timothy Miller", team="Plainfield Indian Trail Wrest."
        ),
    ],
    99: [
        bracket_utils.Placer(
            name="Timothy Williams", team="Harvey Park District Twisters"
        ),
        bracket_utils.Placer(name="Ben Gerdes", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Scott Benjamin", team="Catlin Youth WC"),
        bracket_utils.Placer(name="Danny Jovanovic", team="Dolton Park Falcons"),
        bracket_utils.Placer(name="Jermaine White", team="OPRF Warhawks"),
        bracket_utils.Placer(name="Brody Rude", team="Newman Blue Devils"),
    ],
    105: [
        bracket_utils.Placer(name="Thomas Combes", team="Dolton Park Falcons"),
        bracket_utils.Placer(name="Sam Watts", team="Foreman WC"),
        bracket_utils.Placer(name="Curtis Owen", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="Ryan Ewanio", team="Rosemont Cobras WC"),
        bracket_utils.Placer(name="Bob Remily", team="Harlem Park Boys Club"),
        bracket_utils.Placer(name="Aren Arechiga", team="Thornwood Kids WC"),
    ],
    112: [
        bracket_utils.Placer(name="Manuel Villarreal", team="Arlington Cardinals"),
        bracket_utils.Placer(name="Kristian Wahlgren", team="Tigertown Tanglers"),
        bracket_utils.Placer(name="Jeremy Neufeld", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Dan Schmidt", team="Moline Tigers"),
        bracket_utils.Placer(
            name="Aaron Mihaljevich.", team="Cal. Mem. Pk. Dist. Wolv."
        ),
        bracket_utils.Placer(name="Chris Papanek", team="Mead Jr. WC"),
    ],
    119: [
        bracket_utils.Placer(name="Ron Stonitsch", team="Crestwood Colts WC"),
        bracket_utils.Placer(name="Ryan Casey", team="St. Barnabas"),
        bracket_utils.Placer(name="Ruben Saldana", team="Tomcat WC"),
        bracket_utils.Placer(name="Ryan Reinhart", team="Unity Youth"),
        bracket_utils.Placer(name="Jim Leduc", team="Indian Prairie Trailblazers"),
        bracket_utils.Placer(name="Brian Martin", team="Edwardsville"),
    ],
    127: [
        bracket_utils.Placer(name="Gerardo Quintanilia", team="Tomcat WC"),
        bracket_utils.Placer(name="Matt McDonnell", team="Newman Blue Devils"),
        bracket_utils.Placer(name="Mike Powell", team="Oak Park River Forest Warhawks"),
        bracket_utils.Placer(name="Willie Morris", team="Danville WC"),
        bracket_utils.Placer(
            name="Colin Thompson", team="Plainfield Indian Tr. Wrest."
        ),
        bracket_utils.Placer(name="Jeff Defauw", team="Geneseo WC"),
    ],
    135: [
        bracket_utils.Placer(name="Denny Hartwig", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Kevin Singletary", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Austin Collins", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="C.J. Protsman", team="Macomb YMCA Kids Wrestling"),
        bracket_utils.Placer(
            name="Steve Bailey", team="Plainfield Indian Trail Wrestling"
        ),
        bracket_utils.Placer(name="Mike Etzkorn", team="Lemont WC"),
    ],
    144: [
        bracket_utils.Placer(name="Ryan Pape", team="Franklin Park Raiders"),
        bracket_utils.Placer(name="Chris Timmons", team="Hoopeston East Lynn Jr. High"),
        bracket_utils.Placer(name="Ryan Beivenue", team="Trimpe Junior High"),
        bracket_utils.Placer(name="Jeremy Judd", team="Lil Reaper"),
        bracket_utils.Placer(name="Dave Cardin", team="Metamora Kids WC"),
        bracket_utils.Placer(name="RayTodd Guzak", team="Crestwood Colts WC"),
    ],
    153: [
        bracket_utils.Placer(name="Jose Medina", team="Gordon Tech Rams WC Chicago"),
        bracket_utils.Placer(name="Matthew Beeler", team="Mattoon WC"),
        bracket_utils.Placer(name="John Rupprecht", team="Geneseo WC"),
        bracket_utils.Placer(name="Brandon Dahlke", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Dean Phillips", team="Bison WC B"),
        bracket_utils.Placer(name="Brian Dill", team="Centralia WC"),
    ],
    163: [
        bracket_utils.Placer(name="Andy Donaldson", team="Mead Hr. WC"),
        bracket_utils.Placer(name="Michael Acord", team="Westville Jr. High"),
        bracket_utils.Placer(name="Scott Wulff", team="Oswego Panthers"),
        bracket_utils.Placer(name="Ray Jebsen", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Chris Williams", team="Indian Prairie Pioneers"),
        bracket_utils.Placer(name="John Sherrill", team="Murphysboro Jr. High"),
    ],
    173: [
        bracket_utils.Placer(name="Ken Robinson", team="St. Charles WC"),
        bracket_utils.Placer(name="Glen Humphrey", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Larry Fong", team="Mead Jr. WC"),
        bracket_utils.Placer(name="Chris McCay", team="Hoopeston East Lynn Jr. High"),
        bracket_utils.Placer(name="Chuck Morin", team="Indian Prairie Trailblazers"),
        bracket_utils.Placer(name="Matthew Weidner", team="Gibson City Youth Wrest."),
    ],
    185: [
        bracket_utils.Placer(name="Mark Harvey", team="Mt. Zion WC"),
        bracket_utils.Placer(name="Nathan Shelton", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Don Madenis", team="Harvard WC"),
        bracket_utils.Placer(name="L.T. Garrett", team="Hoopeston East Lynn Jr. High"),
        bracket_utils.Placer(name="Brian Washington", team="Dolton Park Falcons"),
        bracket_utils.Placer(name="Jeffrey Rohde", team="Yorkville WC"),
    ],
    275: [
        bracket_utils.Placer(name="Peter Marx", team="Eisenhower Jr. High WC"),
        bracket_utils.Placer(name="Jerry Jontry", team="Argenta/Oreana WC"),
        bracket_utils.Placer(name="Mike Johnson", team="Tri-City Braves"),
        bracket_utils.Placer(
            name="Cameron Randolph", team="Harvey Park District Twisters"
        ),
        bracket_utils.Placer(name="Richard Reynolds", team="Aurora J-Hawks"),
        bracket_utils.Placer(name="Patrick Parham", team="Tri-City Braves"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Harvey Park District Twisters": 195.0,
    "Dolton Park Falcons": 143.5,
    "Vittum Cats": 103.5,
    "Aurora J-Hawks": 102.0,
    "Oak Forest Warriors": 101.5,
    "Arlington Cardinals WC": 93.0,
    "Franklin Park Raiders": 83.5,
    "Oak Park River Forest Warhawks": 82.5,
    "Tomcat WC": 80.5,
    "Lockport Grapplers Wrestling": 80.0,
    "Geneseo WC": 68.0,
    "Newman Blue Devils": 66.5,
    "Mead Jr. High": 66.0,  # Was `Mead Jr. WC` in the program
    "Plainfield Indian Trail Wrestling": 64.0,
    "St. Barnabas/Christ The King": 59.0,
    "Tri-City Braves": 57.5,
    "Hoopeston E. Lynn Jr. High": 56.0,
    "Orland Park Pioneers": 54.5,
    "Argenta/Oreana WC": 42.0,
    "Rosemont Cobras WC": 41.0,
    "Crestwood Colts WC": 40.5,
    "Mattoon WC": 40.5,
    "Edwardsville": 39.0,
    "Indian Prairie Trailblazers": 39.0,
    "Round Lake Spartans": 39.0,
    "Thornwood Kids WC": 36.5,
    "Catlin Youth WC": 36.0,
    "Lemont WC": 36.0,
    "Mt. Zion WC": 36.0,
    "Forman WC": 34.0,
    "St. Charles WC": 33.0,
    "Gordon Tech Rams WC Chicago": 33.0,
    "Naperville Patriots Wrestling": 32.0,
    "Westville Jr. High": 31.0,
    "Belleville Little Devils": 31.0,
    "Riverdale Jr. High WC": 31.0,
    "Warrior WC Niles": 31.0,
    "Eisenhower Jr. High": 30.0,  # Was `Eisenhower Jr. High WC` in the program
    "Unity Youth": 29.0,
    "Tinley Park Bulldogs": 28.5,
    "Belvidere YMCA Bandits": 28.0,
    "Little Giants WC": 28.0,
    "Oswego Panthers": 28.0,
    "Jr. Bison WC": 27.0,
    "Panthers WC": 26.0,
    "Antioch Upper Grade School": 24.0,
    "Tigertown Tanglers": 24.0,
    "Bismarck-Henning Wrestling": 23.5,
    "Trimpe Junior High": 23.0,
    "Dundee Highlanders": 22.0,
    "Harlem-Park Boys Club": 21.0,
    "Moline Tigers": 21.0,
    "Harvard WC": 20.0,
    "Villa-Lombard Cougars": 20.0,
    "Yorkville WC": 20.0,
    "Carol Stream Park Dist": 17.5,
    "Blue Crew WC": 17.0,
    "Calumet Memorial PD": 17.0,
    "Chillicothe Wrestling": 17.0,
    "Gibson City Youth Wrestling": 17.0,
    "Lil Reaper": 17.0,
    "Blackhawk WC": 16.0,
    "Marquardt Middle Jr. High": 16.0,
    "Murphysboro Jr. High": 16.0,
    "Centralia WC": 15.0,
    "Indian Prairie Pioneers": 15.0,
    "Bethalto Boys Club Bulls": 14.0,
    "Granite City WC Coolidge": 14.0,
    "Macomb YMCA Kids Wrestling": 14.0,
    "Morton Youth Wrestling": 14.0,
    "Carbondale WC": 12.0,
    "Danville WC": 12.0,
    "Rich Wrestling LTD": 12.0,
    "Metamora Kids WC": 11.0,
    "West Chicago Wildcats PD": 11.0,
    "Dakota Matt Rats": 10.0,
    "Redbird WC": 10.0,
    "Streator Junior Bulldogs": 10.0,
    "Bradley-Bourbonnais": 9.0,
    "Addams Jr. High School WC": 7.0,
    "Hinsdale Red Devil WC": 7.0,
    "Mustang WC": 7.0,
    "Elgin Matt Rats": 6.0,
    "Hickory Hills Park District": 6.0,
    "Knights Wrestling lub": 6.0,
    "Woodstock Cardinal Wrestling": 6.0,
    "Geneva Park Dist": 5.0,
    "Decatur WC": 4.0,
    "Jr. Falcon Wrestling": 4.0,
    "Naperville Warriors": 4.0,
    "Spartans WC": 4.0,
    "St. Tarcissus Raiders": 4.0,
    "Sycamore WC": 4.0,
    "Taylorville WC": 4.0,
    "Urbana Kids WC": 4.0,
    "Granite City WC Grigsby": 3.5,
    "Jr. Bison WC (2)": 3.0,
    "Palatine PD Sundling": 3.0,
    "Pekin Boy's Club": 3.0,
    "Elgin Grapplers": 2.0,
    "Highland Junior Bulldogs": 2.0,
    "Illini Bluffs WC": 2.0,
    "Joliet Boy's Club Cobras": 2.0,
    "Lions WC": 2.0,
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
        if weight == 60:
            _, _, match_5th = weight_class.matches
            match_5th.top_competitor.full_name = "Michael Murphy Jr."
        if weight == 64:
            _, _, match_5th = weight_class.matches
            match_5th.bottom_competitor.full_name = "Ryan De Lira"
            match_5th.bottom_competitor.last_name = "De Lira"
        if weight == 144:
            _, _, match_5th = weight_class.matches
            match_5th.bottom_competitor.full_name = "Ray Todd Guzak"
            match_5th.bottom_competitor.first_name = "Ray Todd"
        if weight == 153:
            _, _, match_5th = weight_class.matches
            match_5th.bottom_competitor.full_name = "Dean Phillips Jr."

        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1990.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
