# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    60: [
        bracket_utils.Placer(name="Ben Gerdes", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Justin Weber", team="Villa Lombard WC"),
        bracket_utils.Placer(name="Tony Davis", team="Harvey Twisters"),
        bracket_utils.Placer(name="Jerry Delira", team="Lan-Oak Park District"),
        bracket_utils.Placer(name="Chad Red", team="Danville YMCA WC"),
        bracket_utils.Placer(name="Jim Brasher", team="Vittum Cats"),
    ],
    65: [
        bracket_utils.Placer(name="Cory Daker", team="Forman WC"),
        bracket_utils.Placer(name="Jason Eierman", team="Colts WC"),
        bracket_utils.Placer(name="Derrick Noble", team="Arlington Cardinals WC"),
        bracket_utils.Placer(name="Nathan Camer", team="Colts WC"),
        bracket_utils.Placer(name="Mark Bybee", team="Vittum Cats"),
        bracket_utils.Placer(name="Jason Pero", team="Lan-Oak Park District"),
    ],
    70: [
        bracket_utils.Placer(name="Jason Ford", team="Rich Wrestling Ltd."),
        bracket_utils.Placer(name="Ryan Ferguson", team="Medinah Lancers WC"),
        bracket_utils.Placer(name="Matt Bouback", team="Belvidere Bandits YMCA WC"),
        bracket_utils.Placer(name="Tim Stringer", team="Dolton Park Jr. Falcons"),
        bracket_utils.Placer(name="Daniel Schickel", team="Colts WC"),
        bracket_utils.Placer(name="Bryant Crawford", team="Geneseo WC"),
    ],
    75: [
        bracket_utils.Placer(name="Dan Gilbert", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Jim Soldan", team="Frankfort Falcons"),
        bracket_utils.Placer(name="Michael Griffin", team="Rich Wrestling Ltd"),
        bracket_utils.Placer(name="Curt Bee", team="Lanphier-Southeast WC"),
        bracket_utils.Placer(name="Kevin Dunn", team="Vittum Cats"),
        bracket_utils.Placer(name="Chuy Villarreal", team="Medinah Lancers WC"),
    ],
    80: [
        bracket_utils.Placer(name="Keith Snyder", team="Panther Wrestling Club"),
        bracket_utils.Placer(name="Eric Siebert", team="Illinois Valley WC"),
        bracket_utils.Placer(name="William Graham", team="Villa Lombard WC"),
        bracket_utils.Placer(name="Kevin Ryan", team="Colts WC"),
        bracket_utils.Placer(name="Douglas Sawyer", team="Villa Lombard WC"),
        bracket_utils.Placer(name="Bobby McKinney", team="Forman WC"),
    ],
    85: [
        bracket_utils.Placer(name="Steve Williams", team="Harvey Twisters"),
        bracket_utils.Placer(name="Martin Sanchez", team="Belvidere Bandits YMCA WC"),
        bracket_utils.Placer(name="Mike Torres", team="Vittum Cats"),
        bracket_utils.Placer(name="Mike Mena", team="Newman Middle School"),
        bracket_utils.Placer(name="Steve Gerstung", team="Arlington Cardinals WC"),
        bracket_utils.Placer(name="Erin Johnson", team="Hoopeston-East Lynn Jr. H."),
    ],
    90: [
        bracket_utils.Placer(name="Joseph Williams", team="Harvey Twisters"),
        bracket_utils.Placer(name="Mike Eierman", team="Colts WC"),
        bracket_utils.Placer(name="Frank Laccone", team="DeKalb WC"),
        bracket_utils.Placer(name="Ryan Smith", team="Roxana Jr. High Vikings"),
        bracket_utils.Placer(name="Phil Benjamin", team="Catlin WC"),
        bracket_utils.Placer(name="Terry Cantorna", team="Orland Park Pioneers"),
    ],
    95: [
        bracket_utils.Placer(name="Peter Stanley", team="Mattoon WC"),
        bracket_utils.Placer(name="Kelly Hamill", team="Belvidere Bandits YMCA WC"),
        bracket_utils.Placer(name="Tom Buenik", team="Vittum Cats"),
        bracket_utils.Placer(name="G.W. Fuhr", team="Rockridge Jr. High"),
        bracket_utils.Placer(name="Nick Gryga", team="Panther Wrestling Club"),
        bracket_utils.Placer(name="Terry Dantzler", team="Harvey Twisters"),
    ],
    100: [
        bracket_utils.Placer(name="Paul Blaha", team="Frankfort Falcons"),
        bracket_utils.Placer(name="Mike Derro", team="Panther Wrestling Club"),
        bracket_utils.Placer(name="Will Lepsi", team="Vittum Cats"),
        bracket_utils.Placer(name="Steven Brito", team="Roxana Jr. High Vikings"),
        bracket_utils.Placer(name="Herbert House", team="Oak Park River Forest WC"),
        bracket_utils.Placer(name="Jayson Querciagrossa", team="Crossface WC"),
    ],
    105: [
        bracket_utils.Placer(name="Cass Lundgren", team="DeKalb WC"),
        bracket_utils.Placer(name="Jeff Wallace", team="Geneseo WC"),
        bracket_utils.Placer(name="Jerimy Chambers", team="Frankfort Falcons"),
        bracket_utils.Placer(name="Rob Felstead", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Mike Devos", team="Morton Youth WC"),
        bracket_utils.Placer(name="Robert O'Connor", team="Oak Lawn PD"),
    ],
    111: [
        bracket_utils.Placer(name="Terrell Sandifer", team="Harvey Twisters"),
        bracket_utils.Placer(name="Troy Copeland", team="Geneseo WC"),
        bracket_utils.Placer(name="Andy Bednarczyk", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Ray Pena", team="Elgin Matt Rats WC"),
        bracket_utils.Placer(name="Steve McDonnell", team="Moline Wildcats"),
        bracket_utils.Placer(name="Andre Davis", team="Harvey Twisters"),
    ],
    118: [
        bracket_utils.Placer(name="Christopher Ireland", team="Moline Wildcats"),
        bracket_utils.Placer(name="Matt Sell", team="DeKalb WC"),
        bracket_utils.Placer(name="Mike Ahrens", team="LaGrange Lions"),
        bracket_utils.Placer(name="Patrick Mahoney", team="Villa Lombard WC"),
        bracket_utils.Placer(name="Scott Ventimiglia", team="Roxana Roughnecks"),
        bracket_utils.Placer(name="Priest Wilson", team="Georgetown WC"),
    ],
    125: [
        bracket_utils.Placer(name="Jim Czajkowski", team="Panther Wrestling Club"),
        bracket_utils.Placer(name="Pat Ahrens", team="LaGrange Lions"),
        bracket_utils.Placer(name="Mark Back", team="Wheaton P.D. Falcons"),
        bracket_utils.Placer(name="Troy Christopherson", team="Geneseo WC"),
        bracket_utils.Placer(name="Bob Profeta", team="Naperville Wrestlers"),
        bracket_utils.Placer(name="Gary Davis", team="Bethalto Boys Club"),
    ],
    135: [
        bracket_utils.Placer(name="Bryan Rebhan", team="Naperville Warhawks"),
        bracket_utils.Placer(name="Joseph Lamantia", team="Eisenhower Jr. High"),
        bracket_utils.Placer(name="Brad Gardner", team="Lanphier-Southeast WC"),
        bracket_utils.Placer(name="Mike Barcena", team="Vittum Cats"),
        bracket_utils.Placer(name="Dan Limon", team="Lil' Reaper WC"),
        bracket_utils.Placer(name="Brad Wood", team="Metamora Kids WC"),
    ],
    145: [
        bracket_utils.Placer(name="Doug Seehase", team="DeKalb WC"),
        bracket_utils.Placer(name="Alex Cortez", team="Lockport Grapplers WC"),
        bracket_utils.Placer(name="Brett Gautcher", team="Sycamore WC"),
        bracket_utils.Placer(name="Tosh Gibbs", team="Naperville Patriots"),
        bracket_utils.Placer(name="Mark Hussar", team="Catlin WC"),
        bracket_utils.Placer(name="Carlos Flores", team="Dolton Park Jr. Falcons"),
    ],
    155: [
        bracket_utils.Placer(name="George Hollendoner", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Russ Bannister", team="DeKalb WC"),
        bracket_utils.Placer(name="Charlie Bedder", team="Turk WC"),
        bracket_utils.Placer(name="Steve Davis", team="Unity Youth WC"),
        bracket_utils.Placer(name="Bill Sullivan", team="Dundee Highlanders"),
        bracket_utils.Placer(name="Rovon Jones", team="Matburns Wrestlling Club"),
    ],
    170: [
        bracket_utils.Placer(name="James Quarles", team="Harvey Twisters"),
        bracket_utils.Placer(name="Brad Kastor", team="Geneseo WC"),
        bracket_utils.Placer(name="Curt Kock", team="Lemont Bears WC"),
        bracket_utils.Placer(name="Mike Rivera", team="J-Hawk WC"),
        bracket_utils.Placer(name="Denzil Batlin", team="Moline Spartans"),
        bracket_utils.Placer(name="Bill Little", team="Dundee Highlanders"),
    ],
    185: [
        bracket_utils.Placer(name="Patrick McDonald", team="Harvey Twisters"),
        bracket_utils.Placer(name="Juan Molina", team="Unity Youth WC"),
        bracket_utils.Placer(name="Jason Lewis", team="Moine Wildcats"),
        # Harvie Link, Jr.
        bracket_utils.Placer(name="Harvie Link", team="Belleville Little Devils"),
        bracket_utils.Placer(name="Hector Figueroa", team="Vittum Cats"),
        bracket_utils.Placer(name="Greg Stec", team="LaGrange Lions"),
    ],
    275: [
        bracket_utils.Placer(name="Todd Nesbitt", team="Harvey Twisters"),
        bracket_utils.Placer(name="Gary Cole", team="Bismarck-Henning WC"),
        bracket_utils.Placer(name="Curtis Tomac", team="Lil' Reaper WC"),
        bracket_utils.Placer(name="Terence Durkin", team="Eisenhower Jr. High"),
        bracket_utils.Placer(name="Michael Adams", team="H.P. Little Giant WC"),
        bracket_utils.Placer(name="Delira Humberto", team="Rams WC"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Harvey Twisters": 248.0,
    "Vittum Cats": 165.0,
    "DeKalb WC": 137.5,
    "Geneseo WC": 111.0,
    "Arlington Cardinals WC": 106.0,
    "Panther WC": 105.0,
    "Colts WC": 101.0,
    "Tinley Park Bulldogs": 95.0,
    "Villa Lombard WC": 89.0,
    "Frankfort Falcons": 78.0,
    "Moline Wildcats": 75.0,
    "Belvidere Bandits YMCA": 71.5,
    "LaGrange Lions": 68.0,
    "Rich Wrestling Ltd": 60.5,
    "Dolton Park Jr. Falcons": 58.0,
    "Lil' Reaper WC": 54.5,
    "Eisenhower JHS": 53.5,
    "Foreman WC": 45.5,
    "Lanphier-Southeast WC": 45.0,
    "Wheaton PD Falcons": 45.0,
    "Roxana Vikings": 43.0,
    "Unity Youth WC": 43.0,
    "Oak Forest Warriors": 42.0,
    "Oak Park-River Forest WC": 41.5,
    "Mattoon WC": 40.0,
    "Orland Park Pioneers": 40.0,
    "Sycamore WC": 40.0,
    "Lan-Oak PD": 37.0,
    "Dundee Highlanders": 36.5,
    "Turk WC": 33.5,
    "Catlin WC": 33.0,
    "Newman Middle School": 33.0,
    "Rockridge JHS": 33.0,
    "Belleville L'I Devils": 32.0,
    "Naperville Warhawks": 32.0,
    "Medinah Lancer WC": 31.5,
    "Lemont Bears WC": 31.0,
    "Moline Spartans": 27.5,
    "Bismark-Henning WC": 26.0,
    "Elgin Matt Rats WC": 25.5,
    "Lockport Grapplers": 24.0,
    "Morton Youth WC": 23.5,
    "J-Hawk WC": 23.0,
    "Illinois Valley WC": 22.0,
    "Roxana Roughnecks": 21.5,
    "Naperville Wrestlers": 20.5,
    "Naperville Patriots": 19.0,
    "Rams WC": 17.5,
    "HP Little Giant WC": 16.0,
    "Matburns WC": 16.0,
    "Crossface WC": 15.0,
    "Danville YMCA WC": 13.5,
    "Oak Lawn PD": 13.0,
    "Centralia WC": 12.0,
    "Dixon WC": 12.0,
    "Georgetown WC": 12.0,
    "Mascoutah JHS": 12.0,
    "Westville JHS": 12.0,
    "Harvard WC": 11.0,
    "Hoopeston-East Lynn": 11.0,
    "Bloomington JHS": 10.5,
    "Jordan WC": 10.5,
    "Bethalto Boys Club": 10.0,
    "Round Lake PD Spartans": 10.0,
    "Crestwood Colts": 8.0,
    "Granite City-Grigsby": 8.0,
    "Woodstock Cardinals": 8.0,
    "Cahokia WC": 7.0,
    "Harlem-Franklin Boys Club": 6.5,
    "St. Charles WC": 6.0,
    "Yorkville WC": 6.0,
    "Bartonville Blue Crew": 4.0,
    "Blackhawk WC": 4.0,
    "Carol Stream PD": 4.0,
    "Fisher WC": 4.0,
    "Franklin Park Raiders": 4.0,
    "Gibson City Youth": 4.0,
    "Jefferson Wolverines": 4.0,
    "Mt. Zion WC": 4.0,
    "St. Tarcissus Raiders": 4.0,
    "Urbana Kids Club": 4.0,
    "Lawrence County WC": 3.0,
    "Murphysboro JHS": 3.0,
    "Rosemont Cobra": 3.0,
    "Tomcat WC": 2.5,
    "Geneva Vikings": 2.5,
    "Chillicothe WC": 2.0,
    "East Moline WC": 2.0,
    "Hickory Hills PD": 2.0,
    "Naperville Warriors": 2.0,
    "Wood River Marooners": 2.0,
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
        if weight == 185:
            _, match_3rd, _ = weight_class.matches
            match_3rd.bottom_competitor.full_name = "Harvie Link, Jr."

        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1987.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
