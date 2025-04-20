# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    60: [
        bracket_utils.Placer(name="Ryan Meagher", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Cory Daker", team="Foreman Booster"),
        bracket_utils.Placer(name="Ben Gerdes", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Dan Collins", team="Bronco WC"),
        bracket_utils.Placer(name="Justin Weber", team="Villa Lombard WC"),
        bracket_utils.Placer(name="Steve Willard", team="Harlem Boys Club Cougar"),
    ],
    65: [
        bracket_utils.Placer(name="Nick Cina", team="Belvidere Bandits"),
        bracket_utils.Placer(name="Joey O'Sullivan", team="Colts WC"),
        bracket_utils.Placer(name="Jay Ford", team="Rich Wrestling Ltd"),
        bracket_utils.Placer(name="Eric Carter", team="Roxana Roughnecks"),
        bracket_utils.Placer(name="Tim Stringer", team="Dolton Falcons"),
        bracket_utils.Placer(name="James Crnich", team="Oak Forest Warriors"),
    ],
    70: [
        bracket_utils.Placer(name="Keith Snyder", team="Panther WC"),
        bracket_utils.Placer(name="Luke Pascale", team="Orland Park Pioneers"),
        bracket_utils.Placer(name="Dan Gilbert", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Kurt Kalchbrenner", team="Vittum Cats"),
        bracket_utils.Placer(name="Kevin Ryan", team="Colts WC"),
        bracket_utils.Placer(name="Gene Bonnette", team="Boys Club of Pekin"),
    ],
    75: [
        bracket_utils.Placer(name="Bill Walsh", team="Panther WC"),
        bracket_utils.Placer(name="Mike Eierman", team="Colts WC"),
        bracket_utils.Placer(name="Martin Sanchez", team="Belvidere Bandits"),
        bracket_utils.Placer(name="Richard Weeden", team="Villa Lombard WC"),
        bracket_utils.Placer(name="Shay Cordes", team="East Moline WC"),
        bracket_utils.Placer(name="Brian Brummitt", team="Crossface WC"),
    ],
    80: [
        bracket_utils.Placer(name="Steve Williams", team="Harvey Twisters"),
        bracket_utils.Placer(name="Brant Laroche", team="Panther WC"),
        bracket_utils.Placer(name="Dan Pargulski", team="Arlington Cardinals WC"),
        bracket_utils.Placer(name="Ray Callahan", team="DeKalb WC"),
        bracket_utils.Placer(name="Chris Shefts", team="Rich Wrestling Ltd"),
        bracket_utils.Placer(name="Shane Daker", team="Foreman Booster"),
    ],
    85: [
        bracket_utils.Placer(name="Jeff Mirabella", team="Elgin WC"),
        bracket_utils.Placer(name="Cass Lundgren", team="DeKalb WC"),
        bracket_utils.Placer(name="Tom Buenik", team="Vittum Cats"),
        bracket_utils.Placer(name="Steve Brito", team="Roxana Roughnecks"),
        bracket_utils.Placer(name="Kelly Hamill", team="Belvidere Bandits"),
        bracket_utils.Placer(name="Densel Herald", team="Bloomington JHS"),
    ],
    90: [
        bracket_utils.Placer(name="Chris Buenik", team="Vittum Cats"),
        bracket_utils.Placer(name="Richard Harris", team="Tinley Park Bulldogs"),
        bracket_utils.Placer(name="Roger Dourlet", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Sam Walt", team="DeKalb WC"),
        bracket_utils.Placer(name="Tim Guryn", team="Vittum Cats"),
        bracket_utils.Placer(name="Ken Lewis", team="Arlington Cardinals WC"),
    ],
    95: [
        bracket_utils.Placer(name="Ed Minet", team="Panther WC"),
        bracket_utils.Placer(name="Tony Chierico", team="Vittum Cats"),
        bracket_utils.Placer(name="Ray Broukal", team="Colts WC"),
        bracket_utils.Placer(name="Rody Rodriquez", team="Aurora Tomcats"),
        bracket_utils.Placer(name="Jason Roberson", team="Moline Booster"),
        bracket_utils.Placer(name="Tim Creighton", team="Dundee Highlanders"),
    ],
    100: [
        bracket_utils.Placer(name="Jim Czajkowski", team="Panther WC"),
        bracket_utils.Placer(name="Darren Ferguson", team="Medinah Lancer WC"),
        bracket_utils.Placer(name="Steve McDonnell", team="Moline Booster"),
        bracket_utils.Placer(name="Mark Rios", team="Sterling Warriors"),
        bracket_utils.Placer(name="Scott Ventmiglia", team="Roxana Roughnecks"),
        bracket_utils.Placer(name="Mike Tumilty", team="Boys Club of Pekin"),
    ],
    105: [
        bracket_utils.Placer(name="Hector Saldana", team="Aurora Tomcats"),
        bracket_utils.Placer(name="Tony Sanders", team="Indian Prairie"),
        bracket_utils.Placer(name="Vince Cascone", team="Vittum Cats"),
        bracket_utils.Placer(name="Tim O'Malley", team="Sterling Warriors"),
        bracket_utils.Placer(name="Dion Simmons", team="Decatur WC"),
        bracket_utils.Placer(name="Greg Licciardello", team="Tinley Park Bulldogs"),
    ],
    111: [
        bracket_utils.Placer(name="Chris Hruska", team="Medinah Lancer WC"),
        bracket_utils.Placer(name="Tim Houston", team="Oak Lawn PD"),
        bracket_utils.Placer(name="Ramon Terry", team="Harvey Twisters"),
        bracket_utils.Placer(name="Shawn Condon", team="Harvard WC"),
        bracket_utils.Placer(name="Jeremy Ufert", team="Roxana Roughnecks"),
        bracket_utils.Placer(name="Jeff Sutherland", team="Youth Razorbacks"),
    ],
    118: [
        bracket_utils.Placer(name="Bob Bartkowiak", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Lamon Terry", team="Harvey Twisters"),
        bracket_utils.Placer(name="Richard Rollyson", team="Foreman Booster"),
        bracket_utils.Placer(name="Mike Mitchell", team="Cahokia WC"),
        bracket_utils.Placer(name="Natan Fonville", team="Greenwood-Tumoro WC"),
        bracket_utils.Placer(name="Sam Berkland", team="Lil Reaper WC"),
    ],
    125: [
        bracket_utils.Placer(name="Corey Atwell", team="Geneseo WC"),
        bracket_utils.Placer(name="Tuhan Waller", team="Harvey Twisters"),
        bracket_utils.Placer(name="Byron Overton", team="Wilbur Trimpe JHS"),
        bracket_utils.Placer(name="Pat Duggan", team="St. Tarcissus Raiders"),
        bracket_utils.Placer(name="Mike Jones", team="Harvard WC"),
        bracket_utils.Placer(name="Andres Garcia", team="Rich Wrestling Ltd"),
    ],
    135: [
        bracket_utils.Placer(name="Eugene Browning", team="Harvey Twisters"),
        bracket_utils.Placer(name="Walter Pollack", team="Barrington Colts"),
        bracket_utils.Placer(name="James Walton", team="Oak Park-River Forest"),
        bracket_utils.Placer(name="Scott Gardner", team="Patriots WC"),
        bracket_utils.Placer(name="Lane Murray", team="Bloomington JHS"),
        bracket_utils.Placer(name="Nick Nieponski", team="Tinley Park Bulldogs"),
    ],
    145: [
        bracket_utils.Placer(name="Craig Manz", team="Panther WC"),
        bracket_utils.Placer(name="Rich Flores", team="Oak Forest Warriors"),
        bracket_utils.Placer(name="Geoffrey Matson", team="Patriots WC"),
        bracket_utils.Placer(name="Dave Schmidt", team="Moline Booster"),
        bracket_utils.Placer(name="Troy Schmotzer", team="Yorkville WC"),
        bracket_utils.Placer(name="Joe Ramos", team="Vittum Cats"),
    ],
    155: [
        bracket_utils.Placer(name="Kirk Stevens", team="Tigertown Tanglers"),
        bracket_utils.Placer(name="Ed Marevka", team="Peotone PD"),
        bracket_utils.Placer(name="John Vanderwall", team="Midlothian Saints"),
        bracket_utils.Placer(name="Rich Kim", team="St. Tarcissus Raiders"),
        bracket_utils.Placer(name="Jeff Hursh", team="Bloomington JHS"),
        bracket_utils.Placer(name="Charlie Vedder", team="Turk WC"),
    ],
    170: [
        bracket_utils.Placer(name="Jehad Hamdan", team="Lemont Bears WC"),
        bracket_utils.Placer(name="Greg Gresock", team="Batavia WC"),
        bracket_utils.Placer(name="John Paulak", team="Batavia WC"),
        bracket_utils.Placer(name="Ian Blache", team="Carbondale PD"),
        bracket_utils.Placer(name="Ted Galicia", team="Matburns WC"),
        bracket_utils.Placer(name="Sony Nuccio", team="Thomas Jefferson JHS"),
    ],
    185: [
        bracket_utils.Placer(name="Christopher Ziegler", team="Bensenville Bulldogs"),
        bracket_utils.Placer(name="Brad Gray", team="Batavia WC"),
        bracket_utils.Placer(name="Kevin Renner", team="Cooper's Cougars"),
        bracket_utils.Placer(name="Larry Mosko", team="Indian Prairie"),
        bracket_utils.Placer(name="Jason Miller", team="Bensenville Bulldogs"),
        bracket_utils.Placer(name="Justin Mitchel", team="DeKalb WC"),
    ],
    275: [
        bracket_utils.Placer(name="Brian Rose", team="Elgin WC"),
        bracket_utils.Placer(name="Bernie Engh", team="DeKalb WC"),
        bracket_utils.Placer(name="Kevin Scott", team="Geneseo WC"),
        bracket_utils.Placer(name="Tom Theres", team="Indian Trail JHS"),
        bracket_utils.Placer(name="Godfery Williams", team="Oak Park-River Forest"),
        bracket_utils.Placer(name="John Taylor", team="Bloomington JHS"),
    ],
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}

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
    with open(HERE / "extracted.1986.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
