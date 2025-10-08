# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

"""
Note, there were three competitors listed that do not show up in brackets.
These are likely alternates:

- 60: "Grant Hoerr :: CHILLICOTHE WC"
- 119: "Marcos Navarro :: GORDON TECH RAMS WC CHICAGO"
- 173: "Mark Conmy :: PALATINE P.D. CHARGERS"
"""

import pathlib

import bracket_utils
import manual_entry

_HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "HARVEY PARK DISTRICT TWISTERS": 195.0,
    "DOLTON PARK FALCONS": 143.5,
    "VITTUM CATS": 103.5,
    "AURORA J-HAWKS": 102.0,
    "OAK FOREST WARRIORS": 101.5,
    "ARLINGTON CARDINALS WC": 93.0,
    "FRANKLIN PARK RAIDERS": 83.5,
    "OAK PARK RIVER FOREST WARHAWKS": 82.5,
    "TOMCAT WC": 80.5,
    "LOCKPORT GRAPPLERS WC": 80.0,
    "GENESEO WC": 68.0,
    "NEWMAN BLUE DEVILS": 66.5,
    "MEADE JR. WC": 66.0,
    "PLAINFIELD INDIAN TRAIL WILDCATS": 64.0,
    "ST. BARNABAS / CHRIST THE KING": 59.0,
    "TRI-CITY BRAVES": 57.5,
    "HOOPESTON-EAST LYNN JR. HIGH": 56.0,
    "ORLAND PARK PIONEERS": 54.5,
    "ARGENTA-OREANA WC": 42.0,
    "ROSEMONT COBRAS WRESTLING": 41.0,
    "CRESTWOOD COLTS WC": 40.5,
    "MATTOON WC": 40.5,
    "EDWARDSVILLE": 39.0,
    "INDIAN PRAIRIE TRAILBLAZERS": 39.0,
    "ROUND LAKE SPARTANS": 39.0,
    "THORNWOOD KIDS WC": 36.5,
    "CATLIN YOUTH WC": 36.0,
    "LEMONT WC": 36.0,
    "MT. ZION WC": 36.0,
    "FORMAN WC": 34.0,
    "ST. CHARLES WC": 33.0,
    "GORDON TECH RAMS WC CHICAGO": 33.0,
    "NAPERVILLE PATRIOTS WRESTLING": 32.0,
    "WESTVILLE JR. HIGH": 31.0,
    "BELLEVILLE LITTLE DEVILS": 31.0,
    "RIVERDALE JR. HIGH WC": 31.0,
    "WARRIOR WC (NILES)": 31.0,
    "EISENHOWER JR. HIGH WC": 30.0,
    "UNITY YOUTH": 29.0,
    "TINLEY PARK BULLDOGS": 28.5,
    "BELVIDERE YMCA BANDITS": 28.0,
    "LITTLE GIANTS WC": 28.0,
    "OSWEGO PANTHERS": 28.0,
    "JR. BISON WC": 27.0,
    "PANTHER WC": 26.0,
    "ANTIOCH UPPER GRADE": 24.0,
    "TIGERTOWN TANGLERS": 24.0,
    "BISMARCK-HENNING WRESTLING": 23.5,
    "TRIMPE JUNIOR HIGH": 23.0,
    "DUNDEE HIGHLANDERS": 22.0,
    "HARLEM-PARK BOYS CLUB": 21.0,
    "MOLINE TIGERS": 21.0,
    "HARVARD WC": 20.0,
    "VILLA-LOMBARD COUGARS": 20.0,
    "YORKVILLE WC": 20.0,
    "CAROL STREAM P.D. PANTHERS": 17.5,
    "BLUE CREW WRESTLING CLUB": 17.0,
    "CALUMET MEMORIAL PARK DISTRICT": 17.0,
    "CHILLICOTHE WC": 17.0,
    "GIBSON CITY YOUTH WRESTLING": 17.0,
    "LIL' REAPER": 17.0,
    "BLACKHAWK WC": 16.0,
    "MARQUART MIDDLE JR. HIGH": 16.0,
    "MURPHYSBORO JR. HIGH": 16.0,
    "CENTRALIA WC": 15.0,
    "INDIAN PRAIRIE PIONEERS": 15.0,
    "BETHALTO BOYS CLUB BULLS": 14.0,
    "GRANITE CITY WC COOLIDGE": 14.0,
    "MACOMB YMCA KIDS WRESTLING": 14.0,
    "MORTON YOUTH WRESTLING": 14.0,
    "CARBONDALE WC": 12.0,
    "DANVILLE WC": 12.0,
    "RICH WRESTLING LTD.": 12.0,
    "METAMORA KIDS WC": 11.0,
    "WEST CHICAGO WILDCATS P.D.": 11.0,
    "DAKOTA MATT RATS": 10.0,
    "REDBIRD WC": 10.0,
    "STREATOR JUNIOR BULLDOGS": 10.0,
    "BRADLEY BOURBONNAIS WC": 9.0,
    "ADDAMS JR. HIGH SCHOOL W.C.": 7.0,
    "HINSDALE RED DEVIL WC": 7.0,
    "MUSTANG WC": 7.0,
    "ELGIN MATT RATS": 6.0,
    "HICKORY HILLS PARK DISTRICT": 6.0,
    "KNIGHTS WC": 6.0,
    "WOODSTOCK CARDINAL WRESTLING": 6.0,
    "GENEVA PARK DISTRICT": 5.0,
    "DECATUR WC": 4.0,
    "JR. FALCON WRESTLING": 4.0,
    "NAPERVILLE WARRIORS": 4.0,
    "SPARTANS WC": 4.0,
    "ST. TARCISSUS RAIDERS": 4.0,
    "SYCAMORE WC": 4.0,
    "TAYLORVILLE WC": 4.0,
    "URBANA KIDS WC": 4.0,
    "GRANITE CITY WC GRIGSBY": 3.5,
    # "JR. BISON WC": 3.0,  # Unclear why this shows up twice in scores?
    "PALATINE P.D. SUNDLING": 3.0,
    "PEKIN BOY'S CLUB": 3.0,
    "ELGIN GRAPPLERS": 2.0,
    "HIGHLAND JUNIOR BULLDOGS": 2.0,
    "ILLINI BLUFFS WC": 2.0,
    "JOLIET BOYS CLUB COBRAS": 2.0,
    "LIONS WC": 2.0,
}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {
    ("Michael Murphy, Jr", "LOCKPORT GRAPPLERS WC"): bracket_utils.Competitor(
        full_name="Michael Murphy, Jr",
        first_name="Michael",
        last_name="Murphy",
        team_full="LOCKPORT GRAPPLERS WC",
    ),
    ("Ryan De Lira", "DOLTON PARK FALCONS"): bracket_utils.Competitor(
        full_name="Ryan De Lira",
        first_name="Ryan",
        last_name="De Lira",
        team_full="DOLTON PARK FALCONS",
    ),
    ("Phillip J. Foster", "NEWMAN BLUE DEVILS"): bracket_utils.Competitor(
        full_name="Phillip J. Foster",
        first_name="Phillip",
        last_name="Foster",
        team_full="NEWMAN BLUE DEVILS",
    ),
    ("Ray Todd Guzak", "CRESTWOOD COLTS WC"): bracket_utils.Competitor(
        full_name="Ray Todd Guzak",
        first_name="Ray Todd",
        last_name="Guzak",
        team_full="CRESTWOOD COLTS WC",
    ),
    ("Jessie Whitton Jr.", "EL PASO WRESTLING"): bracket_utils.Competitor(
        full_name="Jessie Whitton Jr.",
        first_name="Jessie",
        last_name="Whitton",
        team_full="EL PASO WRESTLING",
    ),
    ("Joe De Voss Jr.", "RIVERDALE JR. HIGH WC"): bracket_utils.Competitor(
        full_name="Joe De Voss Jr.",
        first_name="Joe",
        last_name="De Voss",
        team_full="RIVERDALE JR. HIGH WC",
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
        _HERE.parent, 1990, _NAME_EXCEPTIONS
    )

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(_HERE / "extracted.1990.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
