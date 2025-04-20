# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Jeremy Hayes", team="MORTON YOUTH WC"),
    64: bracket_utils.Placer(name="Amador Estrada", team="ROUND LAKE SPARTAN WC"),
    68: bracket_utils.Placer(name="Kyle Oneill", team="TINLEY PARK BULLDOGS"),
    72: bracket_utils.Placer(name="Leonard Bowens", team="HARVEY TWISTERS"),
    77: bracket_utils.Placer(name="Matthew Goldstein", team="Highland Pk."),
    82: bracket_utils.Placer(name="Jim Aberle", team="ROUND LAKE SPARTAN WC"),
    87: bracket_utils.Placer(name="Andy Douglas", team="ADDAMS JR. HIGH"),
    93: bracket_utils.Placer(name="Alan Cartwright", team="WARHAWK WC"),
    99: bracket_utils.Placer(name="Tony Davis", team="HARVEY TWISTERS"),
    105: bracket_utils.Placer(name="Reginald Wright", team="PIRATES"),
    112: bracket_utils.Placer(name="Jason Christeson", team="BETHALTO JR. HIGH"),
    119: bracket_utils.Placer(name="Greg Voegtle", team="Belleville Little Devil"),
    127: bracket_utils.Placer(name="Timothy Williams", team="HARVEY TWISTERS"),
    135: bracket_utils.Placer(name="Dan Weber", team="ADDAMS JR. HIGH"),
    144: bracket_utils.Placer(name="Jason Breen", team="ANTIOCH UPPER GRADE"),
    153: bracket_utils.Placer(name="Randy Anderson", team="Crestwood Colts"),
    163: bracket_utils.Placer(name="Aaron Valley", team="ST. CHARLES WC"),
    173: bracket_utils.Placer(name="Terry Griffis", team="ROCKFORD WC"),
    185: bracket_utils.Placer(name="Chris Rowell", team="VITTUM CATS"),
    275: bracket_utils.Placer(name="Moses Knapp", team="Decatur WC"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY TWISTERS": 184.0,
    "VILLA-LOMBARD COUGARS": 137.0,
    "BETHALTO JR. HIGH": 125.0,
    "TRAILBLAZER WC": 124.0,
    "TINLEY PARK BULLDOGS": 112.0,
    "ADDAMS JR. HIGH": 103.5,
    "MUSTANG WC": 71.0,
    "MORTON YOUTH WC": 67.5,
    "ST. CHARLES WC": 67.0,
    "ROUND LAKE SPARTAN WC": 66.5,
    "ROSEMONT COBRAS": 65.0,
    "ARLINGTON CARDINALS": 64.5,
    "DOLTON PARK FALCONS": 64.5,
    "GRANITE CITY COOLIDGE": 64.0,
    "HARLEM SCHOOL DIST 122": 61.0,
    "CRYSTAL LAKE WIZARDS": 59.0,
    "PIRATES": 49.0,
    "MEAD JR HIGH WC": 47.5,
    "VITTUM CATS": 47.5,
    "ORLAND PARK PIONEERS": 44.5,
    "WARHAWK WC": 43.5,
    "ANTIOCH UPPER GRADE": 42.0,
    "HICKORY HILLS PK. DIST": 42.0,
    "ST. BARNABAS/CHRIST THE KING": 40.0,
    "ROCKFORD WC": 39.0,
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
    with open(HERE / "extracted.1992.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
