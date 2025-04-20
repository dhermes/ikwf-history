# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Marc Zehr", team="Arlington Cardinals WC"),
    64: bracket_utils.Placer(name="Milton Blakely", team="Harvey Twisters"),
    68: bracket_utils.Placer(name="Tony Davis", team="Harvey Twisters"),
    72: bracket_utils.Placer(name="Russell Guerrero", team="West Chicago Wildcats"),
    77: bracket_utils.Placer(name="Tom Combes", team="Dolton Park Falcons"),
    82: bracket_utils.Placer(name="Justin Weber", team="Villa Lombard Cougars WC"),
    87: bracket_utils.Placer(name="Michael French", team="Mattoon WC"),
    93: bracket_utils.Placer(name="Nick Cina", team="Belvidere Bandits"),
    99: bracket_utils.Placer(name="Curt Bee", team="Lanphier-Springfield WC"),
    105: bracket_utils.Placer(name="Bucky Randolph", team="Oak Forest Warriors"),
    112: bracket_utils.Placer(name="Scott Radosevich", team="Vittum Cats WC"),
    119: bracket_utils.Placer(name="John Stickler", team="Riverdale (Rams) Jr. High"),
    127: bracket_utils.Placer(name="Lenard Randall", team="Harvey Twisters"),
    135: bracket_utils.Placer(name="Joe Williams", team="Harvey Twisters"),
    144: bracket_utils.Placer(name="Joe Cartwright", team="Oak Park River Fore"),
    153: bracket_utils.Placer(name="Tracy Sanborn", team="Belleville Little Devils"),
    163: bracket_utils.Placer(name="Joe O'Roarke", team="Mustangs WC"),
    173: bracket_utils.Placer(name="Pedro Martinez", team="Aurora J-Hawks"),
    185: bracket_utils.Placer(name="Jeff Staffeldt", team="Indian Prairie Pioneers"),
    275: bracket_utils.Placer(name="Hillus Butler", team="Aurora J-Hawks"),
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
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior", weight, champ, _SENIOR_TEAM_REPLACE
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
