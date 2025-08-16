# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_CHAMPS: dict[int, bracket_utils.Placer] = {
    60: bracket_utils.Placer(name="Bob Sineni", team="Tinley Park Bulldogs"),
    70: bracket_utils.Placer(name="David Harris", team="Belleville"),
    75: bracket_utils.Placer(name="Paul Kelly", team="Chicago Ridge"),
    80: bracket_utils.Placer(name="Paul Dina", team="Burbank"),
    85: bracket_utils.Placer(name="Joe Blaney", team="Burbank"),
    90: bracket_utils.Placer(name="Eric Potts", team="Wilmette"),
    95: bracket_utils.Placer(name="Al Skiniotes", team="New Lenox Oakview"),
    100: bracket_utils.Placer(name="Dan Helminski", team="Dundee Highlanders"),
    105: bracket_utils.Placer(name="Jon Smith", team="Mattoon"),
    112: bracket_utils.Placer(name="Steve Bolsoni", team="Oak Forest"),
    118: bracket_utils.Placer(name="Tony Daidone", team="Oak Forest"),
    125: bracket_utils.Placer(name="Bob Mansell", team="Joliet Boy's Club"),
    135: bracket_utils.Placer(name="Ernie Vatch", team="Addison Indian Trail"),
    160: bracket_utils.Placer(name="Wayne Frase", team="Wheaton"),
    275: bracket_utils.Placer(name="Emilio Escamile", team="West Chicago"),
}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    145: [
        bracket_utils.Placer(name="George Dergo", team="Morris"),
        bracket_utils.Placer(name="Morris", team="Geneseo"),
        bracket_utils.Placer(name="Bryant", team="Marshall"),
        bracket_utils.Placer(name="Fuller", team="Addison Indian Trail"),
        bracket_utils.Placer(name="Franks", team="London"),
        bracket_utils.Placer(name="Ramirez", team="Spartans"),
    ],
}
_SENIOR_COMPETITORS: dict[int, list[str | None]] = {
    65: [
        "Chris Richards :: Hoopeston",
        "Silvey :: Murphysboro",
        None,
        "Gonnella :: Elmhurst :: 3",
        "Healy :: Burbank :: 2",
        None,
        "Royer :: Huntley",
        "O'Brien :: Asborn Park",
        None,
        "Anderson :: Batavia :: 6",
        "Quas :: Joliet Boy's Club",
        None,
        "Don Hansen :: Champaign W.C.",
        "Whelan :: Granite City :: 5",
        None,
        "Carpenter :: Holmes",
        "McCarthy :: Jefferson",
        None,
        "Hernandez :: Challand",
        "Rodriguez :: Hazel Crest :: 4",
        None,
        "Todd Sterr :: Joliet Boy's Club :: 1",
        "Callahan :: Highlanders",
        None,
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Burbank": 46.0,  # BURBANK PANTHERS
    "Oak Forest": 41.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Healy", "Burbank"): bracket_utils.Competitor(
        full_name="Healy",
        first_name="",
        last_name="Healy",
        team_full="Burbank",
    ),
    ("Gonnella", "Elmhurst"): bracket_utils.Competitor(
        full_name="Rodriguez",
        first_name="",
        last_name="Rodriguez",
        team_full="Elmhurst",
    ),
    ("Rodriguez", "Hazel Crest"): bracket_utils.Competitor(
        full_name="Gonnella",
        first_name="",
        last_name="Gonnella",
        team_full="Hazel Crest",
    ),
    ("Whelan", "Granite City"): bracket_utils.Competitor(
        full_name="Whelan",
        first_name="",
        last_name="Whelan",
        team_full="Granite City",
    ),
    ("Anderson", "Batavia"): bracket_utils.Competitor(
        full_name="Anderson",
        first_name="",
        last_name="Anderson",
        team_full="Batavia",
    ),
    ("Morris", "Geneseo"): bracket_utils.Competitor(
        full_name="Morris",
        first_name="",
        last_name="Morris",
        team_full="Geneseo",
    ),
    ("Bryant", "Marshall"): bracket_utils.Competitor(
        full_name="Bryant",
        first_name="",
        last_name="Bryant",
        team_full="Marshall",
    ),
    ("Fuller", "Addison Indian Trail"): bracket_utils.Competitor(
        full_name="Fuller",
        first_name="",
        last_name="Fuller",
        team_full="Addison Indian Trail",
    ),
    ("Franks", "London"): bracket_utils.Competitor(
        full_name="Franks",
        first_name="",
        last_name="Franks",
        team_full="London",
    ),
    ("Ramirez", "Spartans"): bracket_utils.Competitor(
        full_name="Ramirez",
        first_name="",
        last_name="Ramirez",
        team_full="Spartans",
    ),
    ("Royer", "Huntley"): bracket_utils.Competitor(
        full_name="Royer",
        first_name="",
        last_name="Royer",
        team_full="Huntley",
    ),
    ("Carpenter", "Holmes"): bracket_utils.Competitor(
        full_name="Carpenter",
        first_name="",
        last_name="Carpenter",
        team_full="Holmes",
    ),
    ("Hernandez", "Challand"): bracket_utils.Competitor(
        full_name="Hernandez",
        first_name="",
        last_name="Hernandez",
        team_full="Challand",
    ),
    ("Silvey", "Murphysboro"): bracket_utils.Competitor(
        full_name="Silvey",
        first_name="",
        last_name="Silvey",
        team_full="Murphysboro",
    ),
    ("O'Brien", "Asborn Park"): bracket_utils.Competitor(
        full_name="O'Brien",
        first_name="",
        last_name="O'Brien",
        team_full="Asborn Park",
    ),
    ("Quas", "Joliet Boy's Club"): bracket_utils.Competitor(
        full_name="Quas",
        first_name="",
        last_name="Quas",
        team_full="Joliet Boy's Club",
    ),
    ("McCarthy", "Jefferson"): bracket_utils.Competitor(
        full_name="McCarthy",
        first_name="",
        last_name="McCarthy",
        team_full="Jefferson",
    ),
    ("Callahan", "Highlanders"): bracket_utils.Competitor(
        full_name="Callahan",
        first_name="",
        last_name="Callahan",
        team_full="Highlanders",
    ),
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, champ in _SENIOR_CHAMPS.items():
        weight_class = bracket_utils.weight_class_from_champ(
            "senior",
            weight,
            champ,
            _SENIOR_TEAM_REPLACE,
            name_exceptions=_NAME_EXCEPTIONS,
        )
        weight_classes.append(weight_class)

    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior",
            weight,
            placers,
            _SENIOR_TEAM_REPLACE,
            name_exceptions=_NAME_EXCEPTIONS,
        )
        weight_classes.append(weight_class)

    for weight, competitors in _SENIOR_COMPETITORS.items():
        bout_numbers = {}
        weight_class = bracket_utils.weight_class_from_competitors(
            "senior",
            weight,
            competitors,
            _SENIOR_TEAM_REPLACE,
            _NAME_EXCEPTIONS,
            bout_numbers,
        )
        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1976.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
