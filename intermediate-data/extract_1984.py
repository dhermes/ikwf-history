# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    95: bracket_utils.Placer(name="Bryon Schultz", team="Lanphier Southeast"),
    100: bracket_utils.Placer(name="Bret Schultz", team="Lanphier Southeast"),
    105: bracket_utils.Placer(name="Bob Mena", team="Sterling Newman"),
}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    50: [
        bracket_utils.Placer(name="Ryan Ferguson", team="Lancers"),
        bracket_utils.Placer(name="Ryan Meagher", team="New Lenox Lions"),
        bracket_utils.Placer(name="Joe O'Sullivan", team="Mt. Greenwood"),
        bracket_utils.Placer(name="Len Jankowski", team="Vittum Cats"),
        bracket_utils.Placer(name="Cory Daker", team="Foreman"),
        bracket_utils.Placer(name="Mike Triolo", team="Tinley Park"),
    ],
    55: [
        bracket_utils.Placer(name="Jim Soldan", team="Frankfort"),
        bracket_utils.Placer(name="Robert Chihoski", team="Rosemont"),
        bracket_utils.Placer(name="Dan Walters", team="Panther WC"),  # `Burbank`
        bracket_utils.Placer(name="Dave Kinsey", team="Joliet YMCA"),
        bracket_utils.Placer(name="Bryant Thomas", team="Belleville"),
        bracket_utils.Placer(name="Phillip Schwing", team="Fischer"),
    ],
    60: [
        bracket_utils.Placer(name="Brent Laroche", team="Panther WC"),  # `Burbank`
        bracket_utils.Placer(name="Kurt Kalchbrenner", team="Vittum Cats"),
        bracket_utils.Placer(name="Jim Pesavento", team="Oak Forest"),
        bracket_utils.Placer(name="Dan Gilbert", team="Tinley Park"),
        bracket_utils.Placer(name="Luke Pascale", team="Orland Park"),
        bracket_utils.Placer(name="Doug Sawyer", team="West Chicago"),
    ],
    65: [
        # `Lanphier S.E`
        bracket_utils.Placer(name="Andy Gardner", team="Lanphier Southeast"),
        bracket_utils.Placer(name="Ken Gerdes", team="Orland Park"),
        bracket_utils.Placer(name="Ricky Harris", team="Tinley Park"),
        bracket_utils.Placer(name="Mike Eierman", team="Mt. Greenwood"),
        bracket_utils.Placer(name="Todd Ryan", team="Bensenville"),
        bracket_utils.Placer(name="Tom Buenik", team="Vittum Cats"),
    ],
    70: [
        bracket_utils.Placer(name="Chris Buenik", team="Vittum Cats"),
        bracket_utils.Placer(name="Dan Willis", team="New Lenox Lions"),
        bracket_utils.Placer(name="Bill Walsh", team="Mt. Greenwood"),
        bracket_utils.Placer(name="Shelly Resendez", team="Oak Forest"),
        bracket_utils.Placer(name="Jim Zeilenga", team="Oak Forest"),
        bracket_utils.Placer(name="Mark Olbrich", team="Harvard"),
    ],
    75: [
        bracket_utils.Placer(name="Sean Bormet", team="Frankfort"),
        bracket_utils.Placer(name="Matt Bartlett", team="St. Charles"),
        bracket_utils.Placer(name="Doug Hayes", team="Oak Forest"),
        bracket_utils.Placer(name="Chad Hamilton", team="Roxanna W.C."),
        bracket_utils.Placer(name="Dan Mahler", team="Oak Park"),
        bracket_utils.Placer(name="Brian Abraham", team="Lancers"),
    ],
    80: [
        bracket_utils.Placer(name="Paul Zina", team="Franklin Park"),
        bracket_utils.Placer(name="Jeff Vasquez", team="Barrington"),
        bracket_utils.Placer(name="Bill O'Brien", team="Panther WC"),  # `Burbank`
        bracket_utils.Placer(name="Tim Houston", team="Chicago Ridge"),
        bracket_utils.Placer(name="Ryan Hager", team="Sterling Redbirds"),
        bracket_utils.Placer(name="Dave Campbell", team="Dolton"),
    ],
    85: [
        bracket_utils.Placer(name="Matt Gruska", team="Indian Prairie"),
        bracket_utils.Placer(name="Steve Smerz", team="Franklin Park"),
        bracket_utils.Placer(name="William Gay", team="Rock Island"),
        bracket_utils.Placer(name="Ryan Schafer", team="Sterling Redbirds"),
        bracket_utils.Placer(name="Mike Sheehy", team="Dundee Highlande"),  # "Dundee"
        bracket_utils.Placer(name="Stan Valle", team="Park Ridge"),
    ],
    90: [
        bracket_utils.Placer(name="Sam Geraci", team="Lancers"),
        bracket_utils.Placer(name="Paul Lekousis", team="Vittum Cats"),
        bracket_utils.Placer(name="Joe Herrman", team="Sycamore"),
        bracket_utils.Placer(name="Robbie Jeffrey", team="Rich Township"),
        bracket_utils.Placer(name="Scott Richardson", team="New Lenox Lions"),
        bracket_utils.Placer(name="Lance Earl", team="DeKalb Rosette"),
    ],
    111: [
        # `Dundee`
        bracket_utils.Placer(name="Craig Goodchild", team="Dundee Highlande"),
        bracket_utils.Placer(name="Steve Cowan", team="Joliet YMCA"),
        bracket_utils.Placer(name="Tom Salvino", team="Mt. Greenwood"),
        bracket_utils.Placer(name="Rich Fenoglio", team="Granite City Coulidge"),
        bracket_utils.Placer(name="Joe Cortese", team="Mat Burns"),
        bracket_utils.Placer(name="Mike Bunning", team="Glencrest"),
    ],
    118: [
        bracket_utils.Placer(name="Larry Logan", team="Barrington"),
        bracket_utils.Placer(name="Victor Blackful", team="Rich Township"),
        bracket_utils.Placer(name="Brad Stockstill", team="Belhalto"),
        bracket_utils.Placer(name="Shawn Willett", team="Sterling Redbirds"),
        bracket_utils.Placer(name="Bret Milburn", team="DeKalb Rosette"),
        bracket_utils.Placer(name="Steve Helton", team="Mattoon"),
    ],
    125: [
        bracket_utils.Placer(name="Bill Novak", team="Panther WC"),  # `Burbank"`
        bracket_utils.Placer(name="Maurice Mance", team="Harvey"),
        bracket_utils.Placer(name="Shawn O'Neil", team="Rock Ridge"),
        bracket_utils.Placer(name="Dan Punkay", team="Champaign"),
        bracket_utils.Placer(name="Rich Bielik", team="Hickory Hills"),
        bracket_utils.Placer(name="M. Seelye", team="Lyons"),
    ],
    135: [
        bracket_utils.Placer(name="Richard Harvey", team="Decatur YMCA"),
        bracket_utils.Placer(name="Jack Schomig", team="Wheaton Falcons"),
        bracket_utils.Placer(name="Gary Dean", team="Rochelle"),
        bracket_utils.Placer(name="Tim Hinson", team="Rock Ridge"),
        bracket_utils.Placer(name="Charlie England", team="Plainfield"),
        bracket_utils.Placer(name="Dan Oswald", team="Lockport"),
    ],
    145: [
        bracket_utils.Placer(name="Pat Wheeler", team="Frankfort"),
        bracket_utils.Placer(name="Tim Propeck", team="Cardinal W.C."),
        bracket_utils.Placer(name="Tony Bopes", team="Rock Ridge"),
        bracket_utils.Placer(name="Brandon Bilyard", team="Bradley-Bourbonnais"),
        bracket_utils.Placer(name="John Ivlow", team="Plainfield"),
        bracket_utils.Placer(name="Steve Surma", team="Naperville"),
    ],
    155: [
        bracket_utils.Placer(name="Jesus Garcia", team="Rich Township"),
        bracket_utils.Placer(name="Charles Nied", team="West Chicago"),
        bracket_utils.Placer(name="Kevin Smith", team="DeKalb Rosette"),
        bracket_utils.Placer(name="Wayne Burke", team="Gibson City"),
        bracket_utils.Placer(name="Greg Davis", team="Rochelle"),
        bracket_utils.Placer(name="Matt Olson", team="Sterling Redbirds"),
    ],
    170: [
        bracket_utils.Placer(name="Andy Sharp", team="DeKalb Huntley"),
        bracket_utils.Placer(name="Joe Ori", team="Crusaders"),
        bracket_utils.Placer(name="Johan Lerch", team="Rock Ridge"),
        bracket_utils.Placer(name="Ed McDonald", team="Palos"),
        bracket_utils.Placer(name="Andre Mayon", team="Indian Prairie"),
        bracket_utils.Placer(name="Joe Minnitti", team="Wheaton Falcons"),
    ],
    185: [
        bracket_utils.Placer(name="Dana Dunklau", team="Frankfort"),
        bracket_utils.Placer(name="Brad Franzen", team="Naperville Warhawks"),
        bracket_utils.Placer(name="Buddy Estes", team="Round Lake"),
        bracket_utils.Placer(name="Kim Honn", team="Jefferson"),
        bracket_utils.Placer(name="Mike Rodriguez", team="Indian Prairie"),
        bracket_utils.Placer(name="Carey Lauder", team="Hickory Hills"),
    ],
    275: [
        bracket_utils.Placer(name="Adam Lang", team="Carol Stream"),
        bracket_utils.Placer(name="Jim Hannon", team="Naperville Patriots"),
        bracket_utils.Placer(name="Jim Meier", team="Plano"),
        bracket_utils.Placer(name="Dave Rapp", team="Vittum Cats"),
        bracket_utils.Placer(name="J. Wojcik", team="Panther WC"),  # `Burbank`
        bracket_utils.Placer(name="Scott Venter", team="Geneseo"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Vittum Cats": 134.0,  # `VITTUM CATS`
    "Panther WC": 128.0,  # `BURBANK PANTHERS`
}


def main():
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
    with open(HERE / "extracted.1984.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
