# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Todd Combes", team="Dolton Park Falcons"),
    64: bracket_utils.Placer(name="Matt Goldstein", team="Little Giants WC"),
    68: bracket_utils.Placer(name="Marc Zehr", team="Arlington Cardinals WC"),
    72: bracket_utils.Placer(name="Tony Davis", team="Harvey Park District Twisters"),
    77: bracket_utils.Placer(name="Don Bermudez", team="Lockport Grapplers Wrestling"),
    82: bracket_utils.Placer(name="Jason Pero", team="Harvey Park District Twisters"),
    87: bracket_utils.Placer(name="Tyler Hurry", team="Riverdale Jr. High WC"),
    93: bracket_utils.Placer(name="Dan Collins", team="Arlington Cardinals WC"),
    99: bracket_utils.Placer(
        name="Timothy Williams", team="Harvey Park District Twisters"
    ),
    105: bracket_utils.Placer(name="Tom Combes", team="Dolton Park Falcons"),
    112: bracket_utils.Placer(name="Manuel Villarreal", team="Arlington Cardinals WC"),
    119: bracket_utils.Placer(name="Ron Stonitsch", team="Crestwood Colts WC"),
    127: bracket_utils.Placer(name="Gerardo Quintanilla", team="Tomcats WC"),
    135: bracket_utils.Placer(name="Denny Hartwig", team="Oak Forest Warriors"),
    144: bracket_utils.Placer(name="Ryan Pape", team="Franklin Park Raiders"),
    153: bracket_utils.Placer(name="Jose Medina", team="Gordon Tech Rams WC Chicago"),
    163: bracket_utils.Placer(name="Andy Donaldson", team="Mead Jr. High"),
    173: bracket_utils.Placer(name="Ken Robinson", team="St. Charles WC"),
    185: bracket_utils.Placer(name="Mark Harvey", team="Mt. Zion WC"),
    275: bracket_utils.Placer(name="Peter Marx", team="Eisenhower Jr. High"),
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
    "Tomcats WC": 80.5,  # Was `Tomcat WC` in the program
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
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
        )
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
