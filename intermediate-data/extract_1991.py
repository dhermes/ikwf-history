# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Steven Bryant", team="BETHALTO JH BULLS"),
    64: bracket_utils.Placer(name="Todd Combes", team="DOLTON PARK FALCONS"),
    68: bracket_utils.Placer(name="Matt Goldstein", team="LITTLE GIANTS"),
    72: bracket_utils.Placer(name="Lawan Gray", team="WARHAWKS WC"),
    77: bracket_utils.Placer(name="Milton Blakely", team="HARVEY TWISTERS"),
    82: bracket_utils.Placer(name="Tony Davis", team="HARVEY TWISTERS"),
    87: bracket_utils.Placer(name="Reggie Wright", team="WARHAWKS WC"),
    93: bracket_utils.Placer(name="Rob Anderson", team="BELVIDERE YMCA BANDITS"),
    99: bracket_utils.Placer(name="Javier Quintanilla", team="TOMCATS WC"),
    105: bracket_utils.Placer(name="Tyler Hurry", team="Riverdale Jr. High"),
    112: bracket_utils.Placer(name="Timothy Williams", team="HARVEY TWISTERS"),
    119: bracket_utils.Placer(name="Daniel Weber", team="ADDAMS JR. HIGH"),
    127: bracket_utils.Placer(name="Ruben Saldana", team="TOMCATS WC"),
    135: bracket_utils.Placer(name="Mike Bertoni", team="VITTUM CATS"),
    144: bracket_utils.Placer(name="Shane Hudnall", team="GENESEO"),
    153: bracket_utils.Placer(name="Adam Mool", team="El Paso"),
    163: bracket_utils.Placer(name="John Ruprecht", team="GENESEO"),
    173: bracket_utils.Placer(name="Kris Hermansen", team="Lemont Bears"),
    185: bracket_utils.Placer(name="Mark Harvey", team="MT. ZION"),
    275: bracket_utils.Placer(name="Richard Reynolds", team="AURORA J-HAWKS"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY TWISTERS": 169.0,
    "DOLTON PARK FALCONS": 146.5,
    "WARHAWKS WC": 109.0,
    "VITTUM CATS": 93.0,
    "BETHALTO JH BULLS": 92.5,
    "TOMCATS WC": 89.5,
    "FRANKLIN PARK RAIDERS": 70.0,
    "PANTHERS WC": 68.0,
    "GENESEO": 66.0,
    "VILLA-LOMBARD COUGARS": 65.5,
    "BELVIDERE YMCA BANDITS": 65.0,
    "BELLEVILLE LIL' DEVILS": 63.5,
    "MORTON YOUTH": 60.0,
    "ARLINGTON CARDINALS": 58.0,
    "OAK FOREST WARRIORS": 55.0,
    "LOCKPORT GRAPPLERS": 54.0,
    "TINLEY PARK BULLDOGS": 53.0,
    "LITTLE GIANTS": 52.0,
    "HARVARD": 50.0,
    "AURORA J-HAWKS": 46.0,
    "NAPERVILLE PATRIOTS": 46.0,
    "MT. ZION": 43.5,
    "TRAILBLAZERS": 43.5,
    "ADDAMS JR. HIGH": 42.0,
    "PLAINFIELD INDIAN TRAIL": 42.0,
    "BLACKHAWK WC": 41.0,
    "TIGERTOWN TANGLERS": 41.0,
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
    with open(HERE / "extracted.1991.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
