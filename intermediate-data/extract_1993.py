# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {}
_NOVICE_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    62: [
        bracket_utils.Placer(name="ISRAEL MARTINEZ", team="TOMCAT WC"),
        bracket_utils.Placer(name="JUSTIN CLUBB", team="HARLEM SCHOOL DIST. 122"),
        bracket_utils.Placer(name="CALEB FERRY", team="HARLEM SCHOOL DIST. 122"),
        bracket_utils.Placer(name="SHAUN DANNENBRINK", team="BETHALTO"),
        bracket_utils.Placer(name="GEORGE SIMS", team="JOLIET BOYS CLUB COBRAS"),
        bracket_utils.Placer(name="SIM BRANDAU", team="LITTLE CELTICS"),
    ],
    66: [
        bracket_utils.Placer(name="NICK CIRRINCIONE", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="PAUL AUGLE", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="SEAN CHINSKI", team="LITTLE CELTICS"),
        bracket_utils.Placer(name="ANDDREW PENA", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="MARK WARREN", team="LITTLE CELTICS"),
        bracket_utils.Placer(name="MICHAEL STANLEY", team="MATTOON"),
    ],
    70: [
        bracket_utils.Placer(name="NATHAN MARTINEZ", team="TOMCATS"),
        bracket_utils.Placer(name="JOSH PRICE", team="RIVERDALE JR. HIGH"),
        bracket_utils.Placer(name="JEFF JEZUIT", team="BURBANK PANTHERS"),
        bracket_utils.Placer(name="PATRICK HAMILTON", team="MORRISON"),
        bracket_utils.Placer(name="LONNIE CORBIN", team="BURBANK PANTERS"),
        bracket_utils.Placer(name="ANTHONY MULLINS", team="METAMORA"),
    ],
    74: [
        bracket_utils.Placer(name="KYLE ONEILL", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="TONY GANAS", team="ROSEMONT COBRAS"),
        bracket_utils.Placer(name="DUSTIN CHLOEMAN", team="LITTLE KNIGHTS"),
        bracket_utils.Placer(name="ZACK MAY", team="BETHALTO"),
        bracket_utils.Placer(name="JOSEPH CLARK", team="JOLIET COBRAS"),
        bracket_utils.Placer(name="ARAN ESPOSITO", team="MEAD"),
    ],
    79: [
        bracket_utils.Placer(name="DAVID DREW", team="MUSTANGS"),
        bracket_utils.Placer(name="RAYNELLE KIZZEE", team="HARVEY TWISTERS"),
        bracket_utils.Placer(
            name="ALLEN RODENBRG", team="ST. BARNABAS/CHRIST THE KING"
        ),
        bracket_utils.Placer(name="CHRIS ILIOPOULOS", team="ADDISON INDIAN TRAIL"),
        bracket_utils.Placer(name="DAN NILES", team="YORKVILLE"),
        bracket_utils.Placer(name="JORDAN WEBSTER", team="METAMORA"),
    ],
    84: [
        bracket_utils.Placer(name="NICK BINGHEIM", team="BETHALTO"),
        bracket_utils.Placer(name="ANGELO GERVASIO", team="LEMONT BEARS"),
        bracket_utils.Placer(name="PATRICK ROSS", team="MUSTANGS"),
        bracket_utils.Placer(name="BOB WHITE", team="MORRISON"),
        bracket_utils.Placer(name="RICKY OLSZTA", team="LITTLE CELTICS"),
        bracket_utils.Placer(name="CAL RYDER", team="MATTOON"),
    ],
    89: [
        bracket_utils.Placer(name="BRIAN CRAVENS", team="MT. ZION"),
        bracket_utils.Placer(name="MATTHEW SANDBURG", team="LIONS WC"),
        bracket_utils.Placer(name="BRAD SCHRADER", team="HARLEM SCHOOL DIST. 122"),
        bracket_utils.Placer(name="JOHN VILLARREAL", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="JUSTIN CARR", team="LITTLE CELTICS"),
        bracket_utils.Placer(name="TERRY GARBS", team="TRAILBLAZERS"),
    ],
    95: [
        bracket_utils.Placer(name="BRAD OWENS", team="MT. ZION"),
        bracket_utils.Placer(name="JASON ERWINSKI", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="MICHAEL POWELL", team="FISHER"),
        bracket_utils.Placer(name="DANNY QUARTZ", team="LITTLE DEVILS"),
        bracket_utils.Placer(name="DANA HOLLAND", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="MICHAEL POWELL(2)", team="FISHER"),  # BIG TYPO
    ],
    101: [
        bracket_utils.Placer(name="MATT LACKEY", team="MOLINE TIGERS"),
        bracket_utils.Placer(name="DENIS POOL", team="GLENDALE GRAPPLERS"),
        bracket_utils.Placer(name="NICK UPTON", team="MATTOON"),
        bracket_utils.Placer(name="AARON POWERS", team="ROCKFORD"),
        bracket_utils.Placer(name="DARLOS GOMEZ", team="ADDISON INDIAN TRAIL"),
        bracket_utils.Placer(name="BRANDON DOLEZAL", team="LOCKPORT"),
    ],
    108: [
        bracket_utils.Placer(name="SEAN CONSIDINE", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="MARK MCCUTCHEON", team="LOCKPORT"),
        bracket_utils.Placer(name="HORACE FLOURNOY", team="TRICITY BRAVES"),
        bracket_utils.Placer(name="SHAIN PRAHL", team="OSWEGO COUGARS"),
        bracket_utils.Placer(name="SHAWN MCDONNELL", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="PATRICK ARVIN", team="OSWEGO COUGARS"),
    ],
    115: [
        bracket_utils.Placer(name="CHAD KRNAC", team="PLAINFIELD IT"),
        bracket_utils.Placer(name="ANDREW HARRISON", team="ADDISON INDIAN TRAIL"),
        bracket_utils.Placer(name="ROD GRIFFIN", team="TRI-CITY BRAVES"),
        bracket_utils.Placer(name="TIM LEWIS", team="RIVERDALE JR. HIGH"),
        bracket_utils.Placer(name="CHRIS KERSTEN", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="RAYMOND BOYD", team="VITTUM CATS"),
    ],
    122: [
        bracket_utils.Placer(name="JOE MCCARTHY", team="HARVARD"),
        bracket_utils.Placer(name="BRET EVINS", team="JR. ROCKETS"),
        bracket_utils.Placer(name="LEITH CROWTHER", team="PLAINFIELD"),
        bracket_utils.Placer(name="ISAAC DIESSELHORST", team="UTCHFIELD"),
        bracket_utils.Placer(name="CHAD PEARSON", team="SYCAMORE"),
        bracket_utils.Placer(name="MARTIN ELLIS", team="JOLET"),
    ],
    130: [
        bracket_utils.Placer(name="BILL KOPECKY", team="ROSEMONT COBRAS"),
        bracket_utils.Placer(name="JESSE IZZO", team="BRONCO"),
        bracket_utils.Placer(name="GARY SHERWOOD", team="OAK LAWN"),
        bracket_utils.Placer(name="JUNSIN SORNSIN", team="ROCKFORD"),
        bracket_utils.Placer(name="BRYAN SCHULTZ", team="EAGLE WC"),
        bracket_utils.Placer(name="CHAD GRIGSBY", team="CHARLESTON"),
    ],
    138: [
        bracket_utils.Placer(name="MARCK GENTHE", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="NICK CURBY", team="LIONS WC"),
        bracket_utils.Placer(name="BRYAN ROUSE", team="MAIN TWP EAGLES"),
        bracket_utils.Placer(name="PARKER PINNELL", team="WAUKEGAN"),
        bracket_utils.Placer(name="ANDREW LINARES", team="HOOPESTON"),
        bracket_utils.Placer(name="JOHN DIETERLE", team="QUINCY"),
    ],
    147: [
        bracket_utils.Placer(name="JOE CHIRUMBOLO", team="EAGLE WC"),
        bracket_utils.Placer(name="NICHOLAS LATUS", team="EAGLE WC"),
        bracket_utils.Placer(name="ADAM VENTSIAS", team="PLAINFIELD IT"),
        bracket_utils.Placer(name="NICK POEHLMAN", team="MORTON"),
        bracket_utils.Placer(name="CK ESPOSITO", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="ADAM STIMPSON", team="JORDAN SETON"),
    ],
    215: [
        bracket_utils.Placer(name="BRAD RUNKLE", team="YORKVILLE"),
        bracket_utils.Placer(name="BRAD CRAIG", team="ROBBINS"),
        bracket_utils.Placer(name="TRAVIS MARTINEZ", team="LIL REAPER"),
        bracket_utils.Placer(name="JACOB ACORD", team="WESTVILLE"),
        bracket_utils.Placer(name="JASON MANGAWAN", team="RAMS"),
        bracket_utils.Placer(name="WILSON MOORE", team="MURPHYSBORO"),
    ],
}
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "VILLA LOMBARD COUGARS": 179.0,
    "LITTLE CELTICS": 93.0,
    "PLAINFIELD INDIAN TRAIL": 87.0,
    "MATTOON": 82.5,
    "ROSEMONT COBRAS": 78.0,
    "HARLEM COUGARS": 77.0,
    "TINLEY PARK BULLDOGS": 74.0,
    "EAGLE": 70.5,
    "BETHALTO JR. HIGH": 61.0,
    "ADDISON/INDIAN TRAIL": 58.0,
    "TOMCATS": 56.0,
    "MT. ZION": 55.0,
    "CRYSTAL LAKE": 53.5,
    "PANTHER WC": 53.5,
    "MUSTANG WC": 53.0,
    "LEMONT BEARS": 52.0,
    "ROCKFORD": 49.5,
    "JOLIET COBRAS": 49.0,
    "LIONS": 47.0,
    "YORKVILLE": 45.0,
    "LOCKPORT GRAPPLERS": 45.0,
    "TRI-CITY BRAVES": 42.5,
    "RIVERDALE RAMS": 42.0,
    "MORRISON": 42.0,
    "MOLINE TIGERS": 38.5,
    "ST. BARNABAS/CHRIST THE KING": 38.0,
    "HARVARD": 36.0,
    "JR. ROCKET": 34.5,
    "OAK LAWN": 34.0,
    "LITTLE DEVILS": 31.0,
    "DOLTON FALCONS": 28.0,
    "MAINE TOWNSHIP EAGLES": 27.0,
    "LIL REAPER": 26.0,
    "MEAD JR. HIGH": 25.0,
    "WESTVILLE": 24.0,
    "GLENDALE": 24.0,
    "METAMORA": 24.0,
    "ROBBINS": 23.0,
    "LITTLE KNIGHTS": 23.0,
    "WAUKEGAN": 21.0,
    "OSWEGO COUGARS": 21.0,
    "TRAILBLAZERS": 20.5,
    "BRONCO": 20.0,
    "HOOPESTON": 20.0,
    "HARVEY PD TWISTERS": 20.0,
    "LITCHFIELD": 19.0,
    "MURPHYSBORO": 19.0,
    "MORTON": 19.0,
    "VITTUM CATS": 18.0,
    "RAMS WC": 17.0,
}
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    70: [
        bracket_utils.Placer(name="STEVEN BRYANT", team="BETHALTO"),
        bracket_utils.Placer(name="MATTHEW FRITZ", team="HARLEM SCHOOL DIST. 122"),
        bracket_utils.Placer(name="JEFF ANDERSON", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(
            name="MATTHEW EARNER", team="ST. BARNABAS CHRIST THE KING"
        ),
        bracket_utils.Placer(name="ZACHARY ANDERSON", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="JASON ATHERTON", team="METAMORA"),
    ],
    74: [
        bracket_utils.Placer(name="TONY DOUGHTY", team="FRANKLIN PARK RAIDERS"),
        bracket_utils.Placer(name="ERIC WOLDIET", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="DENNIS PLECKHAM", team="RICH WRESTLING"),
        bracket_utils.Placer(name="CHAD KARLEN", team="ROUND LAKE SPARTANS"),
        bracket_utils.Placer(name="RONNIE DALLGE", team="MT. ZION"),
        bracket_utils.Placer(name="CHUCK BURROWS", team="BETHALTO"),
    ],
    79: [
        bracket_utils.Placer(name="DAVID STOLTZ", team="MEAD"),
        bracket_utils.Placer(name="AMADOR ESTRADA", team="ROUND LAKE SPARTANS"),
        bracket_utils.Placer(name="BRAD VERMILLION", team="CRYSTAL LAKE"),
        bracket_utils.Placer(name="SCOTT KENNY", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="MARK MANKOWSKI", team="HICKORY HILLS"),
        bracket_utils.Placer(name="SEAN PIPPIN", team="GENESEO"),
    ],
    84: [
        bracket_utils.Placer(name="ROAMELLE KIZZEE", team="HARVEY TWISTERS"),
        bracket_utils.Placer(name="JOE WZOREK", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="JC GAUNT", team="MT. VERNON"),
        bracket_utils.Placer(name="JAKE SULLIVAN", team="BETHALTO"),
        bracket_utils.Placer(name="BRIAN WILSON", team="CRYSTAL LAKE"),
        bracket_utils.Placer(name="STEVEN WERNSMAN", team="YORKVILLE"),
    ],
    89: [
        bracket_utils.Placer(name="DAVID DOUGLAS", team="HARVEY TWISTERS"),
        bracket_utils.Placer(name="DARNELL LOLLIS", team="HARVEY TWISTERS"),
        bracket_utils.Placer(name="LUKE EWANIO", team="ROSEMONT COBRAS"),
        bracket_utils.Placer(name="ANTHONY OPIOLA", team="DOLTON FALCONS"),
        bracket_utils.Placer(name="AARON GILSON", team="ST. CHARLES"),
        bracket_utils.Placer(name="CRAIG COLLINS", team="CALUMET CITY"),
    ],
    95: [
        bracket_utils.Placer(name="TODD COMBES", team="DOLTON FALCONS"),
        bracket_utils.Placer(name="ARCHIE GRIFFIN", team="PIRATES"),
        bracket_utils.Placer(name="GRANT HOERR", team="MORTON YOUTH"),
        bracket_utils.Placer(name="IKE SULLIVAN", team="BETHALTO"),
        bracket_utils.Placer(name="KEVIN RANDOLPH", team="OAK FOREST WARRIORS"),
        bracket_utils.Placer(name="ROBERT MURRAY", team="ORLAND PARK PIONEERS"),
    ],
    101: [
        bracket_utils.Placer(name="ALAN WILSON", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="CHRIS RODRIGUEZ", team="TOMCAT WC"),
        bracket_utils.Placer(name="TRAVIS ZIMMERMAN", team="BETHALTO"),
        bracket_utils.Placer(name="MICHAEL BRUNO", team="PLAINFIELD IT"),
        bracket_utils.Placer(name="STEVE NIELSEN", team="HICKORY HILLS"),
        bracket_utils.Placer(name="JACOB SMITH", team="VILLA LOMBARD COUGARS"),
    ],
    108: [
        bracket_utils.Placer(name="BRIAN JOSEPH", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="JOE JOHNSON", team="KNIGHTS"),
        bracket_utils.Placer(name="MICHAEL BRUCKER", team="DANVILLE"),
        bracket_utils.Placer(name="SANDRO NUNEZ", team="LIL REAPER"),
        bracket_utils.Placer(name="RYAN MASON", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="DAVID CLEMENTZ", team="GENESEO"),
    ],
    115: [
        bracket_utils.Placer(name="TY POWERS", team="ROCKFORD WC"),
        bracket_utils.Placer(name="DAVID BURTON", team="MORTON"),
        bracket_utils.Placer(name="BRAD KERR", team="BETHALTO"),
        bracket_utils.Placer(name="PATRICK MCENEANEY", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="LEO DELATORRE", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="BENJAMIN SUTMAN", team="DAKOTA"),
    ],
    122: [
        bracket_utils.Placer(name="TIM GLOVER", team="MORTON YOUTH"),
        bracket_utils.Placer(name="JOHN SCHULTZ", team="GENESEO"),
        bracket_utils.Placer(name="ROBERTO RODRIGUEZ", team="HARLEM SCHOOL DIST. 122"),
        bracket_utils.Placer(name="ANDY RAINS", team="MARION"),
        bracket_utils.Placer(name="DEVIN MILLIGAN", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="SHAWN FORST", team="TINLEY PARK BULLDOGS"),
    ],
    130: [
        bracket_utils.Placer(name="JASON GUISINGER", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="MIKE KANKE", team="GENESEO"),
        bracket_utils.Placer(name="DAN DEBRUN", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="BILL BIGGER", team="WAUKEGAN"),
        bracket_utils.Placer(name="EMIL ODLING", team="HARVARD"),
        bracket_utils.Placer(name="MIKE BERRY", team="JORDAN SEATON"),
    ],
    138: [
        bracket_utils.Placer(name="TOMMY GROSSMAN", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="DEREK STACHURA", team="MORTON YOUTH"),
        bracket_utils.Placer(name="HANK STOUT", team="VANDALIA"),
        bracket_utils.Placer(name="STANLEY EVANS", team="PIRATES"),
        bracket_utils.Placer(name="AARON SHADAB", team="ELGIN"),
        bracket_utils.Placer(name="MAATHAN SKELTON", team="BETHALTO"),
    ],
    147: [
        bracket_utils.Placer(name="JASON CHRISTESON", team="BETHALTO"),
        bracket_utils.Placer(name="DAVID POTTER", team="ST. CHARLES"),
        bracket_utils.Placer(name="CHARLES MCNEAL", team="ST. CHARLES"),
        bracket_utils.Placer(name="MORIO SANCHEZ", team="BELVIDERE"),
        bracket_utils.Placer(name="ADAM LYONS", team="DANVILLE"),
        bracket_utils.Placer(name="WILLIAM REIDY", team="DOLTON FALCONS"),
    ],
    156: [
        bracket_utils.Placer(name="BEN MENA", team="ROCKFORD WC"),
        bracket_utils.Placer(name="JON LOVRICH", team="HICKORY HILLS"),
        bracket_utils.Placer(name="ANDY MOORE", team="ARGENTA OREANA"),
        bracket_utils.Placer(name="KEVIN BROWER", team="JR. ROCKET"),
        bracket_utils.Placer(name="ERIC CASTANEDA", team="EISENHOWER JR. HAWK"),
        bracket_utils.Placer(name="JEFFREY BROUCEK", team="LEMONT"),
    ],
    166: [
        bracket_utils.Placer(name="THOMAS RIGGINS", team="BETHALTO"),
        bracket_utils.Placer(name="GENE BEARD", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="RYAN LEMBERG", team="YORKVILLE"),
        bracket_utils.Placer(name="ARMOND DAVIS", team="CORKERY COUGARS"),
        bracket_utils.Placer(name="ANDRE DENTON", team="PIRATES"),
        bracket_utils.Placer(name="ERIC POWELL", team="RICH WRESTLING"),
    ],
    177: [
        bracket_utils.Placer(name="TOBY ADAMS", team="W.F. THUNDERBIRD"),
        bracket_utils.Placer(name="JOHN MAILLET", team="DOWNERS GROVE"),
        bracket_utils.Placer(name="JASON BERG", team="DAKOTA"),
        bracket_utils.Placer(name="CHRIS PARCK", team="NAPERVILLE WARRIORS"),
        bracket_utils.Placer(name="MATTHEW KUEBEL", team="FULTON"),
        bracket_utils.Placer(name="SCOTT DAVES", team="PANTHER CUB"),
    ],
    189: [
        bracket_utils.Placer(name="ANTHONY ENGLESE", team="MEAD"),
        bracket_utils.Placer(name="JASON NAPE", team="CRESTWOOD"),
        bracket_utils.Placer(name="JEREMY DURBIN", team="VANDALIA"),
        bracket_utils.Placer(name="CHAD SHEPHERD", team="BRADLEY BOURBONAIS"),
        bracket_utils.Placer(name="GEORGE GARCIA", team="BLACKHAWK II"),
        bracket_utils.Placer(name="KOREY REID", team="CHARGER KIDS"),
    ],
    275: [
        bracket_utils.Placer(name="HUBERT THOMPSON", team="WARHAWK WC"),
        bracket_utils.Placer(name="ANDY MYERS", team="OAK LAWN"),
        bracket_utils.Placer(name="CHAD JENKINS", team="DAKOTA"),
        bracket_utils.Placer(name="MARTIN GONZALEZ", team="BRADLEY BOURBONAIS"),
        bracket_utils.Placer(name="DAVID WITTENBORN", team="EISENHOWER JR. HAWK"),
        bracket_utils.Placer(name="BALTAZAR NINO", team="BATAVIA"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "BETHALTO JR. HIGH": 242.0,
    "VILLA-LOMBARD COUGARS": 158.5,
    "HARVEY TWISTERS": 103.5,
    "ST. CHARLES SAINTS": 102.0,
    "TINLEY PARK BULLDOGS": 97.0,
    "MORTON YOUTH": 90.5,
    "CRYSTAL LAKE WIZARDS": 87.0,
    "DOLTON FALCONS": 87.0,
    "PIRATES": 81.0,
    "ORLAND PARK PIONEERS": 76.5,
    "GENESEO": 74.0,
    "ROCKFORD": 72.5,
    "HARLEM COUGARS": 69.0,
    "DAKOTA": 69.0,
    "MEAD JR. HIGH": 66.5,
    "VANDALIA": 64.5,
    "HICKORY HILLS": 58.0,
    "BRADLEY BOURBONNAIS": 52.0,
    "DANVILE": 49.0,
    "OAK FOREST WARRIORS": 46.0,
    "ROUND LAKE SPARTANS": 46.0,
    "LIL REAPER": 45.0,
    "RICH WRESTLING": 43.0,
    "YORKVILLE": 40.0,
    "CORKERY COUGARS": 39.0,
    "FRANKLIN PARK RAIDERS": 37.0,
    "W.F. THUNDERBIRDS": 37.0,
    "WARHAWKS": 36.0,
    "PLAINFIELD INDIAN TRAIL": 36.0,
    "KNIGHTS": 34.0,
    "PONTIAC": 30.0,
    "JR. ROCKET": 29.0,
    "TIGERTOWN TANGLERS": 29.0,
    "TOMCAT": 28.0,
    "ROSEMONT COBRAS": 27.0,
    "ST. BARNABAS/CHRIST THE KING": 26.0,
    "CRESTWOOD COLTS": 26.0,
    "ARGENTA ORENA": 25.0,
    "DOWNERS GROVE": 24.0,
    "ELGIN": 24.0,
    "MT. VERNON": 23.0,
    "EISENHOWER JR. HAWK": 23.0,
    "CHARGER KIDS": 22.0,
    "WAUKEGAN": 22.0,
    "NAPERVILLE WARRIORS": 21.0,
    "EISENHOWER JR. HIGH": 21.0,
    "FULTON": 21.0,
    "BELVIDERE": 20.0,
    "MARION": 20.0,
    "HARVARD": 19.0,
}


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["novice"] = []
    for team_name, score in _NOVICE_TEAM_SCORES.items():
        team_scores["novice"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    for weight, placers in _NOVICE_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "novice", weight, placers, _NOVICE_TEAM_REPLACE
        )
        weight_classes.append(weight_class)

    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
        )
        if weight == 130:
            _, match_3rd, _ = weight_class.matches
            match_3rd.top_competitor.full_name = "DAN DE BRUN"
            match_3rd.top_competitor.last_name = "DE BRUN"
        if weight == 138:
            _, match_3rd, _ = weight_class.matches
            match_3rd.bottom_competitor.full_name = "STANLEY EVANS JR."

        weight_classes.append(weight_class)

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1993.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
