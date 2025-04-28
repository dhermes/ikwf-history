# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    60: [
        bracket_utils.Placer(name="JEREMY HAYES", team="MORTON YOUTH WC"),
        bracket_utils.Placer(name="STEVE RODGERS", team="CROSSFACE WC"),
        bracket_utils.Placer(name="PAUL AUGLE", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="NICHOLAS CIRRINCIONE", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="DANNY MARTINEZ", team="BELVIDERE YMCA BANDITS"),
        bracket_utils.Placer(name="ANDREW PENNA", team="CRYSTAL LAKE WIZARDS"),
    ],
    64: [
        bracket_utils.Placer(name="AMADOR ESTRADA", team="ROUND LAKE SPARTAN WC"),
        bracket_utils.Placer(name="BLAKE VERMILLION", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="JEFF ANDERSON", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="LONNIE CORBIN", team="PANTHER WRESTLING"),
        bracket_utils.Placer(name="STEVEN BRYANT", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="SEAN CHINSKI", team="LITTLE CELTIC WC"),
    ],
    68: [
        bracket_utils.Placer(name="KYLE ONEILL", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="ANTHONY OPIOLA", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="SCOTT KENNY", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="ADAM WASON", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="MARK MANKOWSKI", team="HICKORY HILLS PD"),
        bracket_utils.Placer(name="TONY DOUGHTY", team="FRANKLIN PARK RAIDERS"),
    ],
    72: [
        bracket_utils.Placer(name="LEONARD BOWENS", team="HARVEY PARK TWISTERS"),
        bracket_utils.Placer(name="NICHOLAS BINGHEIM", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="DAVID STOLTZ", team="ARLINGTON CARDINALS WC"),
        bracket_utils.Placer(name="PAUL GARBIS", team="TRAILBLAZER WC"),
        bracket_utils.Placer(name="BRADLEE VERMILLION", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="SAM SCHAEFER", team="WHEATON WARRENVILLE"),
    ],
    77: [
        bracket_utils.Placer(
            name="MATTHEW GOLDSTEIN", team="HIGHLAND PK LITTLE GIANTS"
        ),
        bracket_utils.Placer(name="TODD COMBES", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="DAVID DOUGLAS", team="HARVEY PARK TWISTERS"),
        bracket_utils.Placer(name="BEN BLACK", team="HINSDALE RED DEVIL WC"),
        bracket_utils.Placer(name="JOEL HOWARD", team="NAPERVILE PATRIOTS"),
        bracket_utils.Placer(name="CRAIG COLLINS", team="CALUMET MEMORIAL PD"),
    ],
    82: [
        bracket_utils.Placer(name="JIM ABERLE", team="ROUND LAKE SPARTAN WC"),
        bracket_utils.Placer(name="MILTON BLAKELY", team="HARVEY PARK TWISTERS"),
        bracket_utils.Placer(name="LAWAN GRAY", team="PIRATES"),
        bracket_utils.Placer(name="JEREMY LARSEN", team="OSWEGO COUGARS"),
        bracket_utils.Placer(name="KEVIN RANDOLPH", team="OAK FOREST WARBIORS"),
        bracket_utils.Placer(name="BRIAN COMSTOCK", team="ST. CHARLES WC"),
    ],
    87: [
        bracket_utils.Placer(name="ANDY DOUGLAS", team="ADDAMS JH WC"),
        bracket_utils.Placer(name="MICHAEL BONDI", team="DUNDEE HIGHLANDERS WC"),
        bracket_utils.Placer(name="LUKE EWANIO", team="ROSEMONT COBRAS"),
        bracket_utils.Placer(name="IAN PENZATO", team="VILLA-LOMBARD"),
        bracket_utils.Placer(name="ALAN WILSON", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="DOMINIC CICCONE", team="TINLEY PARK BULLDOGS"),
    ],
    93: [
        bracket_utils.Placer(name="ALAN CARTWRIGHT", team="WARHAWK WC"),
        bracket_utils.Placer(name="GRIFF POWELL", team="ARLINGTON CARDINALS WC"),
        bracket_utils.Placer(name="FRANCISCO BERMUDEZ", team="LOCKPORT GRAPPLERS"),
        bracket_utils.Placer(name="BRYAN GIBBONS", team="KNIGHT WC"),
        bracket_utils.Placer(name="TRAVIS ZIMMERMAN", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="DAN DOYLE", team="DOLTON PARK FALCONS"),
    ],
    99: [
        bracket_utils.Placer(name="TONY DAVIS", team="HARVEY PARK TWISTERS"),
        bracket_utils.Placer(name="KEVIN SIPP", team="ADDAMS JH WC"),
        bracket_utils.Placer(name="LEO DELATORRE", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="MATHEW GUILFOYLE", team="PLAINFIELD I.T."),
        bracket_utils.Placer(name="BEN KING", team="LIONS WC"),
        bracket_utils.Placer(name="BART BROSNAN", team="ST. BARNABAS/CHRIST THE KING"),
    ],
    105: [
        bracket_utils.Placer(name="REGINALD WRIGHT", team="PIRATES"),
        bracket_utils.Placer(name="KEVIN MILLIGAN", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="RYAN DUGGAN", team="ST. TAR'S RAIDERS"),
        bracket_utils.Placer(name="TIM GLOVER", team="MORTON YOUTH WC"),
        bracket_utils.Placer(name="RYAN POZEN", team="KNIGHT WC"),
        bracket_utils.Placer(name="FRANSISCO VILLARREAL", team="VILLA-LOMBARD COUGARS"),
    ],
    112: [
        bracket_utils.Placer(name="JASON CHRISTESON", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="AARON EHLE", team="HARLEM SD. 122"),
        bracket_utils.Placer(name="STEVE LEVEREZ", team="MUSTANG WC"),
        bracket_utils.Placer(name="KEVIN NEVILLS", team="ADDAMS JH WC"),
        bracket_utils.Placer(name="ROY KING", team="JOLIET BOYS CLUB COBRAS"),
        bracket_utils.Placer(name="MIKE KANKE", team="GENESEO WC"),
    ],
    119: [
        bracket_utils.Placer(name="GREG VOEGTLE", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="LASHAUN JACKSON", team="HARVEY PARK TWISTERS"),
        bracket_utils.Placer(name="CODY ABBOTT", team="URBANA KIDS WC"),
        bracket_utils.Placer(name="ROBERTO RODRIQUEZ", team="HARLEM SD. 122"),
        bracket_utils.Placer(name="PETE CURRIE", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="TIM GRAY", team="PONTIAC WC"),
    ],
    127: [
        bracket_utils.Placer(name="TIMOTHY WILLIAMS", team="HARVEY PARK TWISTERS"),
        bracket_utils.Placer(name="DEREK STACHURA", team="MORTON YOUTH"),
        bracket_utils.Placer(name="CHAD ORR", team="RIVERDALE JH WC"),
        bracket_utils.Placer(name="JEFF EVANS", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="JEFF ESTRADA", team="GCWC GRIGSBY"),
        bracket_utils.Placer(name="JOHN VENNE", team="GCWC COOLIDGE"),
    ],
    135: [
        bracket_utils.Placer(name="DAN WEBER", team="ADDAMS JH WC"),
        bracket_utils.Placer(name="STEWART BURCHFIELD", team="EAGLE WC"),
        bracket_utils.Placer(name="TOM CIEZKI", team="MUSTANG WC"),
        bracket_utils.Placer(name="JOE SCOTT", team="GCWC COOLIDGE"),
        bracket_utils.Placer(name="DAVID POTTER", team="ST. CHARLES WC DIST 303"),
        bracket_utils.Placer(name="THOMAS DIIULIO", team="JORDAN WRESTLING"),
    ],
    144: [
        bracket_utils.Placer(name="JASON BREEN", team="ANTIOCH UPPER GRADE"),
        bracket_utils.Placer(name="MATT ANDRIANO", team="TRAILBLAZER WC"),
        bracket_utils.Placer(name="CORY CREGER", team="JORDAN WRESTLING"),
        bracket_utils.Placer(name="TONY TARANTO", team="HICKORY HILLS PD"),
        bracket_utils.Placer(name="TRAVIS KASKI", team="WAUKEGAN PD HAWKEYE WC"),
        bracket_utils.Placer(name="SCOTT BERGE", team="NEWMAN BLUE DEVILS"),
    ],
    153: [
        bracket_utils.Placer(name="RANDY ANDERSON", team="CRESTWOOD COLTS"),
        bracket_utils.Placer(name="MATT MOYNIHAN", team="ARLINGTON CARDINALS WC"),
        bracket_utils.Placer(name="SCOTT HAMPTON", team="YORKVILLE WC"),
        bracket_utils.Placer(name="ANDY MOORE", team="ARGENTA OREANA"),
        bracket_utils.Placer(name="GEO BROWN", team="ELMHURST JR. DUKES"),
        bracket_utils.Placer(name="PHILIP POWELL", team="EISENHOWER JH"),
    ],
    163: [
        bracket_utils.Placer(name="AARON VALLEY", team="ST. CHARLES WC DIST 303"),
        bracket_utils.Placer(name="WES INMAN", team="TRAILBLAZERS WC"),
        bracket_utils.Placer(name="ARMOND DAVIS", team="MASON SCHOOL PLAYGROUND"),
        bracket_utils.Placer(name="JOHN RUIZ", team="ST. BARNABAS/CHRIST THE KING"),
        bracket_utils.Placer(name="LOUIE SPONSEL", team="PALATINE CHARGERS"),
        bracket_utils.Placer(name="JOE GRIPPO", team="ST. TAR'S RAIDERS"),
    ],
    173: [
        bracket_utils.Placer(name="TERRY GRIFFIS", team="ROCKFORD WC"),
        bracket_utils.Placer(name="LUIS ARREDONDO", team="BLACKHAWK WC"),
        bracket_utils.Placer(name="JOHN JANEK", team="GCWC COOLIDGE"),
        bracket_utils.Placer(name="JASON HOLLENDONER", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="MATT CASELLA", team="LIONS WC"),
        bracket_utils.Placer(name="JOHNNY KNIGHT", team="MACOMB KIDS"),
    ],
    185: [
        bracket_utils.Placer(name="CHRIS ROWELL", team="VITTUM CATS"),
        bracket_utils.Placer(name="BRANDON KEEP", team="DAKOTA WC"),
        bracket_utils.Placer(name="ROSS WILLIAMS", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="ROBBIE BURGENER", team="GCWC COOLIDGE"),
        bracket_utils.Placer(name="NATHAN LABELLE", team="OLSON JR. HIGH"),
        bracket_utils.Placer(name="BOB ZINK", team="IRISH CADET WC"),
    ],
    275: [
        bracket_utils.Placer(name="MOSES KNAPP", team="DECATUR WC"),
        bracket_utils.Placer(name="TROY KIER", team="MT. ZION WC"),
        bracket_utils.Placer(name="STEVE OLEH", team="TRAILBLAZER WC"),
        bracket_utils.Placer(name="LEWIS LANG", team="RICH WRESTLING"),
        bracket_utils.Placer(name="MARCO ORDAZ", team="AURORA J-HAWKS"),
        bracket_utils.Placer(name="JEFF WINIARSKI", team="TRAILBLAZER WC"),
    ],
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
    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
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
