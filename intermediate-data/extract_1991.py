# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils
import manual_entry

HERE = pathlib.Path(__file__).resolve().parent
_SENIOR_TEAM_REPLACE: dict[str, str] = {}
_SENIOR_PLACERS: dict[int, list[bracket_utils.Placer]] = {
    60: [
        bracket_utils.Placer(name="STEVEN BRYANT", team="BETHALTO JR. HIGH"),
        bracket_utils.Placer(name="ANTHONY OPIOLA", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="DAMIEN BILLOW", team="NAPERVILLE PATRIOTS"),
        bracket_utils.Placer(name="TONY DOUGHTY", team="FRANKLIN PARK RAIDERS"),
        bracket_utils.Placer(name="JEFFERY ANDERSON", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="BRENDEN JOYCE", team="TOMCAT"),
    ],
    64: [
        bracket_utils.Placer(name="TODD COMBES", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="LEONARD BOWENS", team="HARVEY PD TWISTERS"),
        bracket_utils.Placer(name="JOHN MURPHY", team="LOCKPORT GRAPPLERS"),
        bracket_utils.Placer(name="AMADOR ESTRADA", team="ROUND LAKE SPARTANS"),
        bracket_utils.Placer(name="ADAM WASON", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="JEFF JEZUIT", team="PANTHERS"),
    ],
    68: [
        bracket_utils.Placer(name="MATT GOLDSTEIN", team="LITTLE GIANTS"),
        bracket_utils.Placer(name="DAVID STOLTZ", team="ARLINGTON CARDINALS"),
        bracket_utils.Placer(name="JOSEPH SUKLEY", team="PLAINFIELD INDIAN TRAIL"),
        bracket_utils.Placer(name="JASON MALMSTROM", team="OSWEGO PANTHERS"),
        bracket_utils.Placer(name="ARCHIE GRIFFIN", team="WARHAWKS"),
        bracket_utils.Placer(name="MOSES REED", team="DANVILLE BOYS CLUB"),
    ],
    72: [
        bracket_utils.Placer(name="LAWAN GRAY", team="WARHAWKS"),
        bracket_utils.Placer(name="GRANT HOERR", team="MORTON YOUTH"),
        bracket_utils.Placer(name="TONY GILL", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="JOEL HOWARD", team="NAPERVILLE PATRIOTS"),
        bracket_utils.Placer(name="DAVID DOUGLAS", team="HARVEY PD TWISTERS"),
        bracket_utils.Placer(name="ROAMELLE KIZZEE", team="HARVEY PD TWISTERS"),
    ],
    77: [
        bracket_utils.Placer(name="MILTON BLAKELY", team="HARVEY PD TWISTERS"),
        bracket_utils.Placer(name="DANIEL BORLAND", team="BLUE CREW"),
        bracket_utils.Placer(name="ALAN CARTWRIGHT", team="WARHAWKS"),
        bracket_utils.Placer(name="JAMES ABERLE", team="ROUND LAKE SPARTANS"),
        bracket_utils.Placer(name="RYAN DELIRA", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="IAN PENZATO", team="VILLA LOMBARD COUGARS"),
    ],
    82: [
        bracket_utils.Placer(name="TONY DAVIS", team="HARVEY PD TWISTERS"),
        bracket_utils.Placer(name="FRANCISCO BERMUDEZ", team="LOCKPORT GRAPLERS"),
        bracket_utils.Placer(name="TOMMY LEE", team="OAK FOREST WARRIORS"),
        bracket_utils.Placer(name="TIM GLOVER", team="MORTON YOUTH"),
        bracket_utils.Placer(name="GRIFF POWELL", team="ARLINGTON CARDINALS"),
        bracket_utils.Placer(name="FRAN BLAKE", team="MUSTANGS"),
    ],
    87: [
        bracket_utils.Placer(name="REGINALD WRIGHT", team="WARHAWKS"),
        bracket_utils.Placer(name="JIM BRASHER", team="VITTUM CATS"),
        bracket_utils.Placer(name="MIKE ONEILL", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="SHAUN BOUBACK", team="BELVIDERE YMCA BANDITS"),
        bracket_utils.Placer(name="MICHAEL DELISLE", team="RAIDERS"),
        bracket_utils.Placer(name="DEREK STARR", team="HINSDALE RED DEVILS"),
    ],
    93: [
        bracket_utils.Placer(name="ROB ANDERSON", team="BELVIDERE YMCA BANDITS"),
        bracket_utils.Placer(name="BLAKE HOERR", team="MORTON YOUTH"),
        bracket_utils.Placer(name="PHILIP THORNE", team="OAK FOREST WARRIORS"),
        bracket_utils.Placer(name="TERRANCE SNAPP", team="JOLIET BOYS CLUB"),
        bracket_utils.Placer(name="HENRY FRANKLIN", team="BLACKHAWK"),
        bracket_utils.Placer(name="JAVIER PARRAS", team="TOMCATS"),
    ],
    105: [
        bracket_utils.Placer(name="TYLER HURRY", team="RIVERDALE JR. HIGH"),
        bracket_utils.Placer(name="MATT WEBSTER", team="METAMORA KIDS"),
        bracket_utils.Placer(name="TJ SLAY", team="GRANITE CITY GRIGSBY"),
        bracket_utils.Placer(name="AARON CHRISTIANSEN", team="TIGERTOWN TANGLERS"),
        bracket_utils.Placer(name="ANDY RAINS", team="MARION"),
        bracket_utils.Placer(name="DAN MCNULTY", team="ST. BARNABAS/CHRIST KING"),
    ],
    112: [
        bracket_utils.Placer(name="TIMOTHY WILLIAMS", team="HARVEY PD TWISTERS"),
        bracket_utils.Placer(name="CODY ABBOTT", team="URBANA KIDS"),
        bracket_utils.Placer(name="TIMOTHY DONNAHUE", team="PANTHERS"),
        bracket_utils.Placer(name="STEVEN TORRES", team="VITTUM CATS"),
        bracket_utils.Placer(name="KEVIN O'NIEL", team="ADAMS JR. HIGH"),
        bracket_utils.Placer(name="MATT FERGUSON", team="LITTLE DEVILS BELLEVILLE"),
    ],
    119: [
        bracket_utils.Placer(name="DANIEL WEBER", team="ADDAMS JR. HIGH"),
        bracket_utils.Placer(name="JOSEPH BRAUER", team="PANTHERS"),
        bracket_utils.Placer(name="GERMAINE LISHMAN", team="BLACKHAWK"),
        bracket_utils.Placer(name="TIMOTHY FORGEY", team="DECATUR"),
        bracket_utils.Placer(name="STEVEN CARROLL", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="LARRY ZOLDOWSKI", team="ST. TARDISSUS RAIDERS"),
    ],
    127: [
        bracket_utils.Placer(name="RUBEN SALDANA", team="TOMCATS"),
        bracket_utils.Placer(name="KEN MILLS", team="DOLTON PARK FALCONS"),
        bracket_utils.Placer(name="JOSH PEARSON", team="TRI-CITY BRAVES"),
        bracket_utils.Placer(name="TIM DUGGAN", team="ST. TARCISSUS RAIDERS"),
        bracket_utils.Placer(name="BRETT RUNKLE", team="YORKVILLE"),
        bracket_utils.Placer(name="CECIL SEVERADOGOER", team="GETOWN"),
    ],
    135: [
        bracket_utils.Placer(name="MIKE BERTONI", team="VITTUM CATS"),
        bracket_utils.Placer(name="CHRIS KUCHARSKI", team="INDIAN PRAIRIE PIONEERS"),
        bracket_utils.Placer(name="BRANDON PRESERN", team="FRANKLIN PARK RAIDERS"),
        bracket_utils.Placer(name="PAT OTTO", team="ORLAND PARK PIONEERS"),
        bracket_utils.Placer(name="DERIC SCHRADEYA", team="JORDAN"),
        bracket_utils.Placer(name="LEEANTWON JONES", team="ROCK ISLAND"),
    ],
    144: [
        bracket_utils.Placer(name="SHANE HUDNALL", team="GENESEO"),
        bracket_utils.Placer(name="RAY GUZAK", team="CRESTWOOD COLTS"),
        bracket_utils.Placer(name="LES WHITTAKER", team="LITTLE DEVILS BELLEVILLE"),
        bracket_utils.Placer(name="TONY BUCHEK", team="GRANITE CITY COOLIDGE"),
        bracket_utils.Placer(name="STEVEN ALF", team="ST. CHARLES"),
        bracket_utils.Placer(name="ANGEL MORALES", team="WAUKEGAN PD HAWKEYE"),
    ],
    153: [
        bracket_utils.Placer(name="ADAM MOOL", team="EL PASO"),
        bracket_utils.Placer(name="TIM ANGSTEN", team="TINLEY PARK BULLDOGS"),
        bracket_utils.Placer(name="JASON SALLEY", team="EISENHOWER JR. HIGH"),
        bracket_utils.Placer(name="BRENT ROGERS", team="EDWARDSVILLE"),
        bracket_utils.Placer(name="WILLIAM ARTHUR", team="VITTUM CATS"),
        bracket_utils.Placer(name="CHUCK BLAZER", team="HARVARD"),
    ],
    163: [
        bracket_utils.Placer(name="JOHN RUPPRECHT", team="GENESEO"),
        bracket_utils.Placer(name="NICK KNAPP", team="PEORIA RAZORBACKS YOUTH"),
        bracket_utils.Placer(name="GREG BAIRD", team="BISMARCK-HENNING"),
        bracket_utils.Placer(name="MATT HEISER", team="ELGIN MATT RATS"),
        bracket_utils.Placer(name="MATT MAJOR", team="MURPHY JR. HIGH"),
        bracket_utils.Placer(name="AL OLIEH", team="TRAILBLAZERS"),
    ],
    173: [
        bracket_utils.Placer(name="KRIS HERMANSEN", team="LEMONT"),
        bracket_utils.Placer(name="JERRY PLANEK", team="WEST CHICAGO PD"),
        bracket_utils.Placer(name="STEVEN HAVARD", team="EDISON MIDDLE SCH"),
        bracket_utils.Placer(name="BRIAN BILLETTH", team="HICKORY HILLS PD"),
        bracket_utils.Placer(name="PETER MIKHAIL", team="GORDON TECH RAMS"),
        bracket_utils.Placer(name="MARK KING", team="MURPHY JR. HIGH"),
    ],
    185: [
        bracket_utils.Placer(name="MARK HARVEY", team="MT. ZION"),
        bracket_utils.Placer(name="DAN VOLIPENDENTEST", team="LITTLE GIANTS"),
        bracket_utils.Placer(name="JOSE SAUCEDO", team="HARVARD"),
        bracket_utils.Placer(name="DAVID YOKLEY", team="UNITY YOUTH"),
        bracket_utils.Placer(name="CRAIG TURNER", team="TRAILBLAZERS"),
        bracket_utils.Placer(name="BRYAN EPTING", team="WARHAWKS"),
    ],
    275: [
        bracket_utils.Placer(name="RICHARD REYNOLDS", team="AURORA J HAWKS"),
        bracket_utils.Placer(name="ALBERT LICKA", team="VILLA LOMBARD COUGARS"),
        bracket_utils.Placer(name="LUIS AGUIRRE", team="FROST/BAD BOYZ"),
        bracket_utils.Placer(name="MICHAEL ROSSOW", team="BRADLEY-BOURBONNAIS"),
        bracket_utils.Placer(name="RICKY BIGGS", team="HARVEY PD TWISTERS"),
        bracket_utils.Placer(name="JEFF STICHT", team="BETHALTO JR. HIGH"),
    ],
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
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {}


def _handle_manual_entries() -> list[bracket_utils.WeightClass]:
    root = HERE.parent / "raw-data" / "1991"

    weight_classes: list[bracket_utils.WeightClass] = []
    for path in root.glob("manual-entry-*.json"):
        with open(path) as file_obj:
            manual_bracket = manual_entry.ManualBracket.model_validate_json(
                file_obj.read()
            )

        weight_class = manual_bracket.to_weight_class(1991, _NAME_EXCEPTIONS)
        weight_classes.append(weight_class)

    return weight_classes


def main():
    manual_weight_classes = _handle_manual_entries()

    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["senior"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior"].append(
            bracket_utils.TeamScore(team=team_name, acronym=None, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = manual_weight_classes
    for weight, placers in _SENIOR_PLACERS.items():
        weight_class = bracket_utils.create_weight_class_from_placers(
            "senior", weight, placers, _SENIOR_TEAM_REPLACE
        )
        if weight == 93:
            _, _, match_5th = weight_class.matches
            match_5th.top_competitor.full_name = "HENRY LEN FRANKLIN"
            match_5th.top_competitor.first_name = "HENRY LEN"
        if weight == 144:
            match_1st, _, _ = weight_class.matches
            match_1st.bottom_competitor.full_name = "RAY TODD GUZAK"
            match_1st.bottom_competitor.first_name = "RAY TODD"

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
