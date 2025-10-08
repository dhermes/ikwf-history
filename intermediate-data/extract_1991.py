# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
Note, there were five competitors listed that do not show up in brackets. These
are likely alternates:

- 60: "Peter Ruffino :: FALCONS MAYWOOD"
- 64: "Tim Nelson :: BARRINGTON"
- 112: "Nick Schumacher :: ADDISON / INDIAN TRAIL ANIMALS"
- 153: "John Deligiannis :: HICKORY HILLS PD"
- 173: "Matthew Jacobs :: MURPHY JR. HIGH"

Another curiosity, either the "official" 2nd placer at 135 from the 1992
program is incorrect or the manually written bracket is. We went with the
manually written bracket (official from IKWF / Mike Urwin) because the backside
also seems to indicate that `Bill Zeman` placed 2nd, not `Chris Kucharski`.
"""

import pathlib

import bracket_utils
import manual_entry

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY PD TWISTERS": 169.0,
    "DOLTON PARK FALCONS": 146.5,
    "WARHAWKS": 109.0,
    "VITTUM CATS": 93.0,
    "BETHALTO JR. HIGH SCHOOL": 92.5,
    "TOMCATS": 89.5,
    "FRANKLIN PARK RAIDERS": 70.0,
    "PANTHERS": 68.0,
    "GENESEO": 66.0,
    "VILLA LOMBARD COUGARS": 65.5,
    "BELVIDERE YMCA BANDITS": 65.0,
    "LITTLE DEVILS BELLEVILLE": 63.5,
    "MORTON YOUTH": 60.0,
    "ARLINGTON CARDINALS": 58.0,
    "OAK FOREST WARRIORS": 55.0,
    "LOCKPORT GRAPPLERS": 54.0,
    "TINLEY PARK BULLDOGS": 53.0,
    "LITTLE GIANTS": 52.0,
    "HARVARD": 50.0,
    "AURORA J HAWKS": 46.0,
    "NAPERVILLE PATRIOTS": 46.0,
    "MT. ZION": 43.5,
    "TRAILBLAZERS": 43.5,
    "ADDAMS JR. HIGH SCHOOL W.C.": 42.0,
    "PLAINFIELD INDIAN TRAIL": 42.0,
    "BLACKHAWK": 41.0,
    "TIGERTOWN TANGLERS": 41.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Darnell D Lollis", "HARVEY PD TWISTERS"): bracket_utils.Competitor(
        full_name="Darnell D Lollis",
        first_name="Darnell",
        last_name="Lollis",
        team_full="HARVEY PD TWISTERS",
    ),
    ("Robert Dela Fuente", "LOCKPORT GRAPPLERS"): bracket_utils.Competitor(
        full_name="Robert Dela Fuente",
        first_name="Robert",
        last_name="Dela Fuente",
        team_full="LOCKPORT GRAPPLERS",
    ),
    ("Henry Len Franklin", "BLACKHAWK"): bracket_utils.Competitor(
        full_name="Henry Len Franklin",
        first_name="Henry",
        last_name="Len Franklin",
        team_full="BLACKHAWK",
    ),
    ("Ray Todd Guzak", "CRESTWOOD COLTS"): bracket_utils.Competitor(
        full_name="Ray Todd Guzak",
        first_name="Ray Todd",
        last_name="Guzak",
        team_full="CRESTWOOD COLTS",
    ),
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes = manual_entry.load_manual_entries(
        _HERE.parent, 1991, _NAME_EXCEPTIONS
    )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1991.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
