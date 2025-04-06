# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TEAM_NAME_MAPPING: dict[str, int] = {
    42000: "AJ Jr. Wildcats WC",
    42001: "Aces WC",
    42002: "Alber Athletics WC",
    42003: "Alton Little Redbirds WC",
    42004: "Arlington Cardinals WC",
    42005: "Astro WC",
    42006: "Aurora WC",
    42007: "Barrington Broncos WC",
    42008: "Batavia WC",
    42009: "Beat the Streets-Chicago",
    42010: "Belleville Little Devils WC",
    42011: "Belvidere Bandits WC",
    42012: "Benton WC",
    42013: "Blackhawk WC",
    42014: "Blue Line Training Academy",
    42015: "Bolingbrook Junior Raiders WC",
    42016: "Brawlers WC",
    42017: "Bulldog Elite WC",
    42018: "Bulls WC",
    42019: "Callan Wrestling Academy",
    42020: "Champaign WC",
    42021: "Charleston WC",
    42022: "Clipper WC",
    42023: "Combative Sports Athletic Center",
    42024: "Crawford County WC",
    42025: "Crosstown Spartan Elite WC",
    42026: "Crystal Lake Wizards WC",
    42027: "Cumberland Youth WC",
    42028: "DC WC",
    42029: "Dakota WC",
    42030: "Danville Chargers WC",
    42031: "Demolition WC",
    42032: "Dixon WC",
    42033: "Downers Grove WC",
    42034: "Dundee Highlanders WC",
    42035: "Dwight WC",
    42036: "East St. Louis WC",
    42037: "Edwardsville WC",
    42038: "Effingham Youth WC",
    42039: "Elevate Wrestling Academy",
    42040: "Elk Grove Junior Grens WC",
    42041: "Elmhurst Titans Wrestling Academy",
    42042: "Englewood Live Wire WC",
    42043: "Evanston School of Wrestling",
    42044: "Falcon Youth WC",
    42045: "Fenton Jr. Bison WC",
    42046: "Fighting Farmers WC",
    42047: "Fitz Wrestling Academy",
    42048: "Force Elite WC",
    42049: "Fox Lake WC",
    42050: "Fox Valley WC",
    42051: "Frankfort Wildcats Wrestling",
    42052: "G2 WC",
    42053: "Gladiator Elite WC",
    42054: "Glenbard East Jr Rams WC",
    42055: "Golden Eagles WC",
    42056: "Granite City Wrestling Association",
    42057: "Guerrero`s Garage Wrestling",
    42058: "HPL Wrestling",
    42059: "Harvey Twisters",
    42060: "Hawk WC",
    42061: "Herrin Junior WC",
    42062: "Highland Bulldog Jr. WC",
    42063: "Hillsboro Jr Toppers WC",
    42064: "Hononegah WC",
    42065: "Hoopeston Area WC",
    42066: "ISI WC",
    42067: "Izzy Style Wrestling",
    42068: "Junior Bronco WC",
    42069: "Junior Kahoks WC",
    42070: "Junior Pioneer WC",
    42071: "Junior Raiders West WC",
    42072: "Junior Titans Wrestling",
    42073: "Kaneland Knights WC",
    42074: "LaSalle Peru Crunching Cavs Youth WC",
    42075: "Lakeland Predators WC",
    42076: "Lemont Bears WC",
    42077: "Lil` Coalers WC",
    42078: "Limestone Blue Crew WC",
    42079: "Lincoln-Way WC",
    42080: "Lion`s Den Wrestling Academy",
    42081: "Lionheart Intense Wrestling",
    42082: "Lions WC",
    42083: "Little Falcons WC",
    42084: "Little Huskies WC",
    42085: "Lockport Junior Porters WC",
    42086: "MadDog Wrestling Academy",
    42087: "Maine Eagles WC",
    42088: "Marengo Youth WC",
    42089: "Mat Rat WC",
    42090: "Mattoon Youth WC",
    42091: "Metamora Kids WC",
    42092: "Morton Youth WC",
    42093: "Mt. Zion Kids WC",
    42094: "Murphysboro Wrestling",
    42095: "Mustang WC",
    42096: "Naperville WC",
    42097: "Nomad Wrestling Academy",
    42098: "North Boone WC",
    42099: "Notre Dame WC",
    42100: "O`Fallon Little Panthers WC",
    42101: "Oak Forest Warriors WC",
    42102: "Olney Cubs WC",
    42103: "Olympia WC",
    42104: "Oswego WC",
    42105: "Panther WC",
    42106: "Pekin Boys & Girls Club",
    42107: "Peoria Heights Minutemen WC",
    42108: "Peoria Razorbacks WC",
    42109: "Peoria Wizards WC",
    42110: "Polo WC",
    42111: "Pontiac WC",
    42112: "Proviso Township Gladiators WC",
    42113: "RWC",
    42114: "Rantoul Youth Wrestling",
    42115: "Red Raiders Wrestling Team",
    42116: "Richmond WC",
    42117: "River Bend WC",
    42118: "Rochelle WC",
    42119: "Rockford WC",
    42120: "SCN Youth WC",
    42121: "SJO Youth WC",
    42122: "SOT-C",
    42123: "Sauk Valley WC",
    42124: "Scorpion WC",
    42125: "Southside Outlaws WC",
    42126: "Sparta Junior Bulldogs WC",
    42127: "Spartan WC",
    42128: "Springs Elite WC",
    42129: "St. Charles WC",
    42130: "Stampede WC",
    42131: "Stingers WC",
    42132: "Stockton Renegades WC",
    42133: "Storm Youth WC",
    42134: "Super Soldiers WC",
    42135: "Sycamore WC",
    42136: "TJ Trained Wrestling",
    42137: "Team 1006 Wrestling",
    42138: "Team 312 WC",
    42139: "Team El1te Wrestling",
    42140: "Team Mascoutah WC",
    42141: "Team Poeta",
    42142: "The Law WC",
    42143: "Timber Wolves WC",
    42144: "Tinley Park Bulldogs WC",
    42145: "Toss Em Up Wrestling Academy",
    42146: "Triad Knights WC",
    42147: "Tribe WC",
    42148: "Trico WC",
    42149: "Unity Youth WC",
    42150: "Urbana Tigers WC",
    42151: "Vandalia Jr WC",
    42152: "Vittum Cats WC",
    42153: "Waterloo Bulldog Wrestling",
    42154: "West Hancock WC",
    42155: "Wheaton Tigers WC",
    42156: "Whips WC",
    42157: "Williamsville WC",
    42158: "Wolfpak WC",
    42159: "Xtreme WC",
    42160: "Yorkville WC",
    42161: "nWo WC",
}


def _collect_all_names(weight_classes: list[bracket_utils.WeightClass]) -> list[str]:
    teams: set[str] = set()
    for weight_class in weight_classes:
        for match in weight_class.matches:
            if match.top_competitor is not None:
                teams.add(match.top_competitor.team)

            if match.bottom_competitor is not None:
                teams.add(match.bottom_competitor.team)

    return sorted(teams)


def main():
    base_index = 42000
    with open(HERE / "extracted.2022.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    weight_classes = extracted.weight_classes
    for i, name in enumerate(_collect_all_names(weight_classes)):
        if "'" in name:
            raise NotImplementedError(name)
        print(f"{base_index + i}: {name!r},")
        # print(f"  ({name!r}, {base_index + i}),")


if __name__ == "__main__":
    main()
