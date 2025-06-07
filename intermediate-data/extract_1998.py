# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {}
_NOVICE_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    62: [
        bracket_utils.Placer(name="NICK FANTHORPE", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="JOSH HARPER", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="MICHAEL ORI", team="GIANTS WC"),
        bracket_utils.Placer(name="BRANDON ZERFOWSKI", team="MT. ZION WC"),
        bracket_utils.Placer(name="CONOR BEEBE", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="SCOTT HORCHER", team="JR. GOLDEN EAGLES"),
    ],
    66: [
        bracket_utils.Placer(name="DAVID MURPHY", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="ANTHONY MARTINEZ", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="JORDAN KOLINSKI", team="ROCKFORD WC"),
        bracket_utils.Placer(name="CHUCKIE PATTEN", team="CROSSFACE WC"),
        bracket_utils.Placer(name="DAN LEONARD", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="BOBBIE UNSELL", team="ROXANA WC"),
    ],
    70: [
        bracket_utils.Placer(name="DAN MANZELLA", team="VITTUM CATS WC"),
        bracket_utils.Placer(name="NICK MARINARO", team="HARLEM COUGARS"),
        bracket_utils.Placer(name="BRAD MEDCHILL", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="SHANE SAYLOR", team="EAST ALTON RAMS"),
        bracket_utils.Placer(name="BRAD DARGAN", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="JONATHAN WOLF", team="MUSTANG WC"),
    ],
    74: [
        bracket_utils.Placer(name="JUSTIN HASKETT", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="MARTY ENGWALL", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="KYLE KRUEGER", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="DAVID LATTIMORE", team="CROSSFACE WC"),
        bracket_utils.Placer(name="MICHAEL REESE", team="L-P CRUNCHING CAVS"),
        bracket_utils.Placer(name="MIKE GLOSSER", team="MATTOON YOUTH WC"),
    ],
    79: [
        bracket_utils.Placer(name="MICHAEL POETA", team="GIANTS WC"),
        bracket_utils.Placer(name="CHASE BEEBE", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="ANDREW LUKANICH", team="VITTUM CATS WC"),
        bracket_utils.Placer(name="DAVID ELLIOTT", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="MATTHEW JONES", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="MICHAEL GLOSSER", team="MATTOON YOUTH WC"),
    ],
    84: [
        bracket_utils.Placer(name="COLLIN MCKILLIP", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="CODY OVERTON", team="MATTOON YOUTH WC"),
        bracket_utils.Placer(name="KEVIN SHEBER", team="LEMONT BEARS"),
        bracket_utils.Placer(name="BRAD MUTHART", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="BRANDON TAYLOR", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="ANDREW NELSON", team="STERLING NEWMAN WC"),
    ],
    89: [
        bracket_utils.Placer(name="ERIC TANNENBAUM", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="MIKE MUCHA", team="LEMONT BEARS"),
        bracket_utils.Placer(name="COLIN DEPRATT", team="PLAINFIELD WOLVES WC"),
        bracket_utils.Placer(name="BOB MCCLELLAN", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="RYAN BURK", team="METAMORA KIDS WC"),
        bracket_utils.Placer(name="CLAYTON NORBERG", team="STERLING NEWMAN WC"),
    ],
    95: [
        bracket_utils.Placer(name="MATT COLLUM", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="DREW MCMAHON", team="CHARGER KIDS WC"),
        bracket_utils.Placer(name="TONY PRETTO", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="BUTCH SCHLOEMANN", team="METRO STALLIONS"),
        bracket_utils.Placer(name="MITCH HANSEN", team="LEMONT BEARS"),
        bracket_utils.Placer(name="J.P. ELMORE", team="BELLEVILLE LITTLE DEVILS"),
    ],
    101: [
        bracket_utils.Placer(name="JOSEPH GOMEZ", team="ELGIN LARKIN ROYALS"),
        bracket_utils.Placer(name="ROBERTO TORRES", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="KEVIN LUEBBERT", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="ANTHONY SILVA", team="PLT PROPHETS"),
        bracket_utils.Placer(name="RICK GOFFRON", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="RAY TERRONEZ", team="EAST MOLINE WC"),
    ],
    108: [
        bracket_utils.Placer(name="KYLE WILLIAMS", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="BILL SMITH", team="MUSTANG WC"),
        bracket_utils.Placer(name="MIKE WHETSTONE", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="DAVID KUNTZ", team="VITTUM CATS"),
        bracket_utils.Placer(name="TYLER WILLIAMS", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="BUDDY DUDCZAK", team="WOLFPAK WC"),
    ],
    115: [
        bracket_utils.Placer(name="MICHAEL STEPHENS", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="JOSH ALONZO", team="WOODSTOCK PANTHERS"),
        bracket_utils.Placer(name="JASON RINGO", team="LEMONT BEARS"),
        bracket_utils.Placer(name="JOEY BENEFIEL", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="DAVID CROCKER", team="POLO WC"),
        bracket_utils.Placer(name="SEAN MCGINNIS", team="ST. BARNABAS/CTK"),
    ],
    122: [
        bracket_utils.Placer(name="MARTY COX", team="YORKVILLE WC"),
        bracket_utils.Placer(name="GRANT FREDRICKSEN", team="WOODSTOCK PANTHERS"),
        bracket_utils.Placer(name="BRIAN GOLDEN", team="VITTUM CATS"),
        bracket_utils.Placer(name="BEN LAUX", team="LITTLE REDBIRDS WC"),
        bracket_utils.Placer(name="JUSTIN OCHOA", team="BATAVIA PINNERS"),
        bracket_utils.Placer(name="DEANDRE NUNN", team="LITTLE CELTIC WC"),
    ],
    130: [
        bracket_utils.Placer(name="LANDON JAKSE", team="L-P CRUNCHING CAVS"),
        bracket_utils.Placer(name="DUSTIN SIEDEL", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="DEREK HILLERY", team="BISMARK-HENNING"),
        bracket_utils.Placer(name="DEREK O'DELL", team="EAST ALTON RAMS"),
        bracket_utils.Placer(name="JOHN VEACH", team="FARMINGTON WC"),
        bracket_utils.Placer(name="MARK COX", team="YORKVILLE WC"),
    ],
    147: [
        bracket_utils.Placer(name="SONNY LAMBERT", team="UNITY WC"),
        bracket_utils.Placer(name="PATRICK BROWNSON", team="BROWNSON WC"),
        bracket_utils.Placer(name="SEAN GUSTAFSON", team="YORKVILLE WC"),
        bracket_utils.Placer(name="KYLE MEEK", team="LAWRENCE COUNTY WC"),
        bracket_utils.Placer(name="SHANE BUTLER", team="MIDWEST CENTRAL YOUTH"),
        bracket_utils.Placer(name="JAKE TRADER", team="LEMONT BEARS"),
    ],
    166: [
        bracket_utils.Placer(name="GRANT MILLER", team="BELVIDERE BANDITS"),
        bracket_utils.Placer(name="ROBERT CHAVIRA", team="BELVIDERE BANDITS"),
        bracket_utils.Placer(name="RYAN JONES", team="HARLEM COUGARS"),
        bracket_utils.Placer(name="SEAN STAFFELDT", team="OSWEGO COUGARS"),
        bracket_utils.Placer(name="FREDDIE DERAMUS", team="VITTUM CATS"),
        bracket_utils.Placer(name="BRETT VALLE", team="L-P CRUNCHING CAVS"),
    ],
    215: [
        bracket_utils.Placer(name="LEOPOLDO GARCIA", team="ELGIN LARKIN ROYALS"),
        bracket_utils.Placer(name="ZACHARY MANTLE", team="METAMORA KIDS WC"),
        bracket_utils.Placer(name="JOEY SZALTIS", team='YOUNG ZIPS "Y" WC'),
        bracket_utils.Placer(name="RUSS WHEAT", team="ROXANA WC"),
        bracket_utils.Placer(name="CHARLES DOERGE", team="EDWARDSVILLE WC"),
        bracket_utils.Placer(name="KEITH MUNT", team="JR. PANTHER WC"),
    ],
}
_NOVICE_TEAM_SCORES: dict[str, float] = {}
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    70: [
        bracket_utils.Placer(name="ZAC BERMAN", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="DANE SHAW", team="EDWARDSVILLE WC"),
        bracket_utils.Placer(name="JUSTIN GREY", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="KURTIS HARTWIG", team="HARVARD WC"),
        bracket_utils.Placer(name="PATRICK KENNEDY", team="HUSKIES WC"),
        bracket_utils.Placer(name="TIM HAYES", team="JR. GOLDEN EAGLES"),
    ],
    74: [
        bracket_utils.Placer(name="BRIAN DYER", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="RYAN KIMBERLIN", team="BRADLEY-BOURBONNAIS"),
        bracket_utils.Placer(name="TONY EMMA", team="WHEATON MONROE EAGLES"),
        bracket_utils.Placer(name="STEVE SCREMENTI", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="RHETT GOTLUND", team="LEMONT BEARS"),
        bracket_utils.Placer(name="ROBERT LOFTUS", team="YORKVILLE WC"),
    ],
    79: [
        bracket_utils.Placer(name="PAT BARTH", team="MORTON YOUTH"),
        bracket_utils.Placer(name="CHARLIE MANNING", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="RYAN GIULANO", team="WOLFPAK WC"),
        bracket_utils.Placer(name="BRIAN TAYLOR", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="JOSEPH SOJKA", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="KEVIN MCNICHOLAS", team="VITTUM CATS"),
    ],
    84: [
        bracket_utils.Placer(name="KEVIN KENNEDY", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="JONATHAN MICHL", team="JORDAN/SETON WC"),
        bracket_utils.Placer(name="JOSEPH HOPKINS", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="MARTIN MCNICHOLAS", team="VITTUM CATS"),
        bracket_utils.Placer(name="DANIEL THOMPSON", team="CHARGER KIDS WC"),
        bracket_utils.Placer(name="DAVID WISENAUER", team="EDISON PANTHERS"),
    ],
    89: [
        bracket_utils.Placer(name="DAN KUNZER", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="TYLER LUDWIG", team="WHEATON MONROE EAGLES"),
        bracket_utils.Placer(name="NATHAN WANGELIN", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="ANTHONY BROWN", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="CHARLES ATCHISON", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="KEVIN DUNNE", team="ORLAND PARK PIONEERS"),
    ],
    95: [
        bracket_utils.Placer(name="DONNY REYNOLDS", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="GEORGE KAPPAS", team="PLAINFIELD WC"),
        bracket_utils.Placer(name="BRIAN DALY", team="VITTUM CATS WC"),
        bracket_utils.Placer(name="LUKE JONES", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="JEFF KROCKO", team="DUNDEE HIGHLANDERS"),
        bracket_utils.Placer(name="MIKE OGANEKU", team="BADGER WC"),
    ],
    101: [
        bracket_utils.Placer(name="RUBEN VILLAREAL", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="JUSTIN BEER", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="JASON PERDUE", team="OREGON-MT. MORRIS WC"),
        bracket_utils.Placer(name="JOHN SILOSKI", team="PLAINFIELD WC"),
        bracket_utils.Placer(name="JOSH OSTER", team="LEMONT BEARS"),
        bracket_utils.Placer(name="BOB BOHACZYK", team="BADGER WC"),
    ],
    108: [
        bracket_utils.Placer(name="AARON RUJAWITZ", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="SEAN WELCH", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="JOHN DECEAULT", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="MIKE TURNMIRE", team="HARLEM COUGARS"),
        bracket_utils.Placer(name="DREW WEIMER", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="JOHN LITCHFIELD", team="SJO YOUTH WC"),
    ],
    115: [
        bracket_utils.Placer(name="LAMBROS FOTOS", team="EAST MOLINE WC"),
        bracket_utils.Placer(name="DUSTY CARPENTER", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="CHAD ISACSON", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="STEVE LOFTON", team="HUSKIES WC"),
        bracket_utils.Placer(name="BRYAN HARNEY", team="VITTUM CATS"),
        bracket_utils.Placer(name="DANNY FINNEY", team="LITTLE CELTIC WC"),
    ],
    122: [
        bracket_utils.Placer(name="MIKE MALIZZIO", team="VILLA-LOMBARD COUGARS"),
        bracket_utils.Placer(name="MARK MENDOZA", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="MATT WINTERHALTER", team="DAKOTA WC"),
        bracket_utils.Placer(name="JIMMY KIM", team="TAZEWELL YOUTH WC"),
        bracket_utils.Placer(name="JIM PRESTON", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="DREW PULLEN", team='YOUNG ZIPS "Y" WC'),
    ],
    130: [
        bracket_utils.Placer(name="MIKE CIABATTONI", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="KYLE JOHNSON", team="SJO YOUTH WC"),
        bracket_utils.Placer(name="DANNY BURK", team="METAMORA KIDS WC"),
        bracket_utils.Placer(name="ROBERT PALUMBO", team="OAK LAWN WILDCATS"),
        bracket_utils.Placer(name="AARON GUISINGER", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="NICK HOLLIS", team="POLO WC"),
    ],
    138: [
        bracket_utils.Placer(name="TOM TREADWAY", team="LEMONT BEARS"),
        bracket_utils.Placer(name="DANNY BROWN", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="KRIS ROBERTS", team="MARION WC"),
        bracket_utils.Placer(name="ADAM LOWE", team="JR. ROCKET WC"),
        bracket_utils.Placer(name="EVAN MCCALLISTER", team="RIVERBEND/FULTON WC"),
        bracket_utils.Placer(name="BEN BAKER", team="CHARGER KIDS WC"),
    ],
    147: [
        bracket_utils.Placer(name="NICK METCALF", team="VILLA PARK YOUNG WARRIORS"),
        bracket_utils.Placer(name="ANDY CVENGROS", team="WHEATON MONROE EAGLES"),
        bracket_utils.Placer(name="MITCH HILDEN", team="BELVIDERE BANDITS"),
        bracket_utils.Placer(name="CHRIS MARKELZ", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="NIALL CAMPBELL", team="LEMONT BEARS"),
        bracket_utils.Placer(name="JAMES EARLYWINE", team="DAKOTA WC"),
    ],
    156: [
        bracket_utils.Placer(name="STEVE ZANONI", team="HARLEM COUGARS"),
        bracket_utils.Placer(name="COREY FORD", team="BELLEVILLE LITTLE DEVILS"),
        bracket_utils.Placer(name="NICHOLAS ORLANDO", team="LEMONT BEARS"),
        bracket_utils.Placer(name="TOM RICHMOND", team="MORRISON STALLIONS"),
        bracket_utils.Placer(name="TERRY BURNER", team="CENTRALIA WC"),
        bracket_utils.Placer(name="RUBEN HERNANDEZ", team="FOX VALLEY WC"),
    ],
    166: [
        bracket_utils.Placer(name="RASHAWN THURMAN", team="COLT & BRAVES WC"),
        bracket_utils.Placer(name="JOEL POWERS", team="ROCKFORD WC"),
        bracket_utils.Placer(name="STEVE MAGINITY", team="CRYSTAL LAKE WIZARDS"),
        bracket_utils.Placer(name="MICHAEL PELKOWSKI", team="BADGER WC"),
        bracket_utils.Placer(name="PHIL SINETOS", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="ROBERTO MARTINEZ", team="VILLA-LOMBARD COUGARS"),
    ],
    177: [
        bracket_utils.Placer(name="TOM SMITH", team="MUSTANG WC"),
        bracket_utils.Placer(name="JUAN APONTE", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="DAN KUNDINGER", team="GLENBARD EAST JR. RAMS"),
        bracket_utils.Placer(name="JIM SCHRIMSHER", team="JR. GOLDEN EAGLES"),
        bracket_utils.Placer(name="ERIC STRAIT", team="SENECA IRISH CADETS"),
        bracket_utils.Placer(name="KEVIN RUSH", team="JACKSONVILLE WC"),
    ],
    189: [
        bracket_utils.Placer(name="MIKE BEHNKE", team="VILLA PARK YOUNG WARRIORS"),
        bracket_utils.Placer(name="DAVID JILES", team="BADGER WC"),
        bracket_utils.Placer(name="JAY GILLETTE", team="FOX VALLEY WC"),
        bracket_utils.Placer(name="MURPHY MAHALIK", team="LITTLE CELTIC WC"),
        bracket_utils.Placer(name="KYLE CROTTY", team="ROXANA WC"),
        bracket_utils.Placer(name="ELJUN WATSON", team="ROCKFORD WC"),
    ],
    275: [
        bracket_utils.Placer(name="DAVID BENNETT", team="HARLEM COUGARS"),
        bracket_utils.Placer(name="JEFF HALL", team="ROCKFORD WC"),
        bracket_utils.Placer(name="NATHAN STREET", team="VANDALIA JR. WC"),
        bracket_utils.Placer(name="JESSE MANNING", team="A-O KIDS WC"),
        bracket_utils.Placer(name="JOSH WURTSBAUGH", team="MATTOON YOUTH WC"),
        bracket_utils.Placer(name="JUSTIN KLITZING", team="VANDALIA JR. WC"),
    ],
}
_SENIOR_TEAM_SCORES: dict[str, float] = {}


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
    with open(HERE / "extracted.1998.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
