# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
Placer = bracket_utils.Placer
_SENIOR_PLACERS: dict[int, list[Placer]] = {
    60: [
        Placer(name="Ryan Meagher", team="Orland Park Pioneers"),
        Placer(name="Cory Daker", team="Foreman Booster"),
        Placer(name="Ben Gerdes", team="Orland Park Pioneers"),
        Placer(name="Dan Collins", team="Bronco W.C."),
        Placer(name="Justin Weber", team="Villa Lombard W.C"),
        Placer(name="Steve Willard", team="Harlem Boys Club Cougar"),
    ],
    65: [
        Placer(name="Nick Cina", team="Belvidere Bandits"),
        Placer(name="Joey O'Sullivan", team="Colts W.C."),
        Placer(name="Jay Ford", team="Rich Wrestling Ltd"),
        Placer(name="Eric Carter", team="Roxana Roughnecks"),
        Placer(name="Tim Stringer", team="Dolton Falcons"),
        Placer(name="James Crnich", team="Oak Forest Warriors"),
    ],
    70: [
        Placer(name="Keith Snyder", team="Panther W.C"),
        Placer(name="Luke Pascale", team="Orland Park Pioneers"),
        Placer(name="Dan Gilbert", team="Tinley Park Bulldogs"),
        Placer(name="Kurt Kalchbrenner", team="Vittum Cats"),
        Placer(name="Kevin Ryan", team="Colts W.C."),
        Placer(name="Gene Bonnette", team="Boys Club of Pekin"),
    ],
    75: [
        Placer(name="Bill Walsh", team="Panther W.C."),
        Placer(name="Mike Eierman", team="Colts W.C."),
        Placer(name="Martin Sanchez", team="Belvidere Bandits"),
        Placer(name="Richard Weeden", team="Villa Lombard W.C."),
        Placer(name="Shay Cordes", team="East Moline W.C."),
        Placer(name="Brian Brummitt", team="Crossface W.C."),
    ],
    80: [
        Placer(name="Steve Williams", team="Harvey Twisters"),
        Placer(name="Brant Laroche", team="Panther W.C"),
        Placer(name="Dan Pargulski", team="Arlington Cardinals"),
        Placer(name="Ray Callahan", team="DeKalb W.C."),
        Placer(name="Chris Shefts", team="Rich Wrestling Ltd"),
        Placer(name="Shane Daker", team="Foreman Booster"),
    ],
    85: [
        Placer(name="Jeff Mirabella", team="Elgin WC"),
        Placer(name="Cass Lundgren", team="DeKalb W.C."),
        Placer(name="Tom Buenik", team="Vittum Cats"),
        Placer(name="Steve Brito", team="Roxana Roughnecks"),
        Placer(name="Kelly Hamill", team="Belvidere Bandits"),
        Placer(name="Densel Herald", team="Bloomington JHS"),
    ],
    90: [
        Placer(name="Chris Buenik", team="Vittum Cats"),
        Placer(name="Richard Harris", team="Tinley Park Bulldogs"),
        Placer(name="Roger Dourlet", team="Oak Forest Warriors"),
        Placer(name="Sam Walt", team="DeKalb W.C."),
        Placer(name="Tim Guryn", team="Vittum Cats"),
        Placer(name="Ken Lewis", team="Arlington Cardinals W.C."),
    ],
    95: [
        Placer(name="Ed Minet", team="Panther W.C"),
        Placer(name="Tony Chierico", team="Vittum Cats"),
        Placer(name="Ray Broukal", team="Colts W.C."),
        Placer(name="Rody Rodriquez", team="Aurora Tomcats"),
        Placer(name="Jason Roberson", team="Moline Booster"),
        Placer(name="Tim Creighton", team="Dundee Highlanders"),
    ],
    105: [
        Placer(name="Hector Saldana", team="Aurora Tomcats"),
        Placer(name="Tony Sanders", team="Indian Prairie"),
        Placer(name="Vince Cascone", team="Vittum Cats"),
        Placer(name="Tim O'Malley", team="Sterling Warriors"),
        Placer(name="Dion Simmons", team="Decatur W.C."),
        Placer(name="Greg Licciardello", team="Tinley Park Bulldogs"),
    ],
    111: [
        Placer(name="Chris Hruska", team="Medinah Lancer W.C."),
        Placer(name="Tim Houston", team="Oak Lawn P.D."),
        Placer(name="Ramon Terry", team="Harvey Twisters"),
        Placer(name="Shawn Condon", team="Harvard W.C."),
        Placer(name="Jeremy Ufert", team="Roxana Roughnecks"),
        Placer(name="Jeff Sutherland", team="Youth Razorbacks"),
    ],
    118: [
        Placer(name="Bob Bartkowiak", team="Oak Forest Warriors"),
        Placer(name="Lamon Terry", team="Harvey Twisters"),
        Placer(name="Richard Rollyson", team="Foreman Booster"),
        Placer(name="Mike Mitchell", team="Cahokia W.C."),
        Placer(name="Natan Fonville", team="Greenwood-Tumoro W.C."),
        Placer(name="Sam Berkland", team="Lil Reaper W.C."),
    ],
    125: [
        Placer(name="Corey Atwell", team="Geneseo W.C."),
        Placer(name="Tuhan Waller", team="Harvey Twisters"),
        Placer(name="Byron Overton", team="Wilbur Trimpe JHS"),
        Placer(name="Pat Duggan", team="St. Tarcissus Raiders"),
        Placer(name="Mike Jones", team="Harvard W.C."),
        Placer(name="Andres Garcia", team="Rich Wrestling Ltd"),
    ],
    135: [
        Placer(name="Eugene Browning", team="Harvey Twisters"),
        Placer(name="Walter Pollack", team="Barrington Colts"),
        Placer(name="James Walton", team="Oak Park-River Forest"),
        Placer(name="Scott Gardner", team="Patriots W.C."),
        Placer(name="Lane Murray", team="Bloomington JHS"),
        Placer(name="Nick Nieponski", team="Tinley Park Bulldogs"),
    ],
    145: [
        Placer(name="Craig Manz", team="Panther W.C."),
        Placer(name="Rich Flores", team="Oak Forest Warriors"),
        Placer(name="Geoffrey Matson", team="Patriots W.C."),
        Placer(name="Dave Schmidt", team="Moline Booster"),
        Placer(name="Troy Schmotzer", team="Yorkville W.C."),
        Placer(name="Joe Ramos", team="Vittum Cats"),
    ],
    155: [
        Placer(name="Kirk Stevens", team="Tigertown Tanglers"),
        Placer(name="Ed Marevka", team="Peotone P.D."),
        Placer(name="John Vanderwall", team="Midlothian Saints"),
        Placer(name="Rich Kim", team="St. Tarcissus Raiders"),
        Placer(name="Jeff Hursh", team="Bloomington JHS"),
        Placer(name="Charlie Vedder", team="Turk W.C."),
    ],
    170: [
        Placer(name="Jehad Hamdan", team="Lemont Bears W.C."),
        Placer(name="Greg Gresock", team="Batavia W.C."),
        Placer(name="John Paulak", team="Batavia W.C."),
        Placer(name="Ian Blache", team="Carbondale P.D."),
        Placer(name="Ted Galicia", team="Matburns W.C."),
        Placer(name="Sony Nuccio", team="Thomas Jefferson JHS"),
    ],
    185: [
        Placer(name="Christopher Ziegler", team="Bensenville Bulldogs"),
        Placer(name="Brad Gray", team="Batavia W.C."),
        Placer(name="Kevin Renner", team="Cooper's Cougars"),
        Placer(name="Larry Mosko", team="Indian Prairie"),
        Placer(name="Jason Miller", team="Bensenville Bulldogs"),
        Placer(name="Justin Mitchel", team="DeKalb W.C."),
    ],
    275: [
        Placer(name="Brian Rose", team="Elgin W.C."),
        Placer(name="Bernie Engh", team="DeKalb W.C."),
        Placer(name="Kevin Scott", team="Geneseo W.C."),
        Placer(name="Tom Theres", team="Indian Trail JHS"),
        Placer(name="Godfery Williams", team="Oak Park-River Forest"),
        Placer(name="John Taylor", team="Bloomington JHS"),
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

    weight_classes.append(
        bracket_utils.WeightClass(
            division="senior",
            weight=100,
            matches=[
                bracket_utils.Match(
                    match_slot="championship_first_place",
                    top_competitor=bracket_utils.Competitor(
                        full_name="Paul Blaha",
                        first_name="Paul",
                        last_name="Blaha",
                        team_full="Frankfort",
                        team_acronym=None,
                    ),
                    bottom_competitor=None,
                    result="",
                    result_type="place",
                    bout_number=None,
                    top_win=True,
                ),
            ],
        )
    )
    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1986.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
