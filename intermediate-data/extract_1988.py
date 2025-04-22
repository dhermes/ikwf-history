# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Milton Blakely", team="Harvey Twisters"),
    64: bracket_utils.Placer(name="Tony Davis", team="Harvey Twisters"),
    68: bracket_utils.Placer(name="Ben Gerdes", team="Orland Park Pioneers"),
    72: bracket_utils.Placer(name="Nathan Camer", team="Mustangs WC"),
    77: bracket_utils.Placer(name="Mike Renella", team="Naperville Patriots"),
    82: bracket_utils.Placer(name="Ryan Ferguson", team="Lancers"),
    87: bracket_utils.Placer(name="Bucky Randolph", team="Oak Forest Warrio"),
    93: bracket_utils.Placer(name="Dan Gilbert", team="Orland Park Pioneers"),
    99: bracket_utils.Placer(name="Steve Williams", team="Harvey Twisters"),
    105: bracket_utils.Placer(name="Alvin Jones", team="Harvey Twisters"),
    112: bracket_utils.Placer(name="Terry Dantzler", team="Harvey Twisters"),
    119: bracket_utils.Placer(name="Herbert House", team="Oak Park River Fore"),
    127: bracket_utils.Placer(name="Andre Davis", team="Harvey Twisters"),
    135: bracket_utils.Placer(name="Mike Barcena", team="Vittum Cats"),
    144: bracket_utils.Placer(name="Priest Wilson", team="Georgetown"),
    153: bracket_utils.Placer(name="Wayne McDaniel", team="Plainfield Indian"),
    163: bracket_utils.Placer(name="Darrin Orta", team="Tomcats WC"),
    # Should be `Sonny Dodd Junior`
    173: bracket_utils.Placer(name="Sonny Dodd", team="Bison WC"),
    185: bracket_utils.Placer(name="Joseph Ryan", team="Villa Lombard"),
    275: bracket_utils.Placer(name="Patrick McDonald", team="Harvey Twisters"),
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY TWISTERS": 345.0,
    "VITTUM CATS": 207.0,
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
        if weight == 173:
            (match,) = weight_class.matches
            match.top_competitor.full_name = "Sonny Dodd Junior"

        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1988.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
