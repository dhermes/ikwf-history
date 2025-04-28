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
    "VITTUM CATS": 165.0,
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
