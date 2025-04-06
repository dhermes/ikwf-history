# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TEAM_NAME_MAPPING: dict[str, int] = {
    37000: "AJ Junior Wildcats WC",
    37001: "Aces WC",
    37002: "Arlington Cardinals WC",
    37003: "Badger WC/B.E.T.A.",
    37004: "Barrington Broncos WC",
    37005: "Batavia WC",
    37006: "Beat the Streets-Chicago",
    37007: "Belleville Little Devils WC",
    37008: "Belvidere Bandits WC",
    37009: "Benton WC",
    37010: "Bismarck-Henning Youth WC",
    37011: "Blackhawk WC",
    37012: "Bolingbrook Junior Raiders",
    37013: "Brawlers WC",
    37014: "Bulls WC",
    37015: "Carbondale WC",
    37016: "Carlinville WC",
    37017: "Carlyle WC",
    37018: "Celtic Elite",
    37019: "Champaign WC",
    37020: "Champbuilders Wrestling",
    37021: "Charleston WC",
    37022: "Chatham WC",
    37023: "Chicago Park District",
    37024: "Contender Wrestling",
    37025: "Crawford County WC",
    37026: "Crosstown Spartan Elite WC",
    37027: "Crusaders` Elite",
    37028: "Crystal Lake Wizards",
    37029: "Cumberland Youth WC",
    37030: "Da WC",
    37031: "Dakota WC",
    37032: "Danville Chargers",
    37033: "Downers Grove WC",
    37034: "DuPage WC",
    37035: "Dundee Highlanders WC",
    37036: "East St. Louis Wrestling",
    37037: "Edwardsville WC",
    37038: "Elk Grove Junior Grens",
    37039: "Elmhurst Jr Dukes WC",
    37040: "Epic Wrestling",
    37041: "Evanston School of Wrestling",
    37042: "Evolution Wrestling Institute",
    37043: "Force WC",
    37044: "Fox Lake WC",
    37045: "Fox Valley WC",
    37046: "G2 WC",
    37047: "Gladiator Elite",
    37048: "Glenbard East Jr Rams WC",
    37049: "Golden Eagles WC",
    37050: "Gomez Wrestling Academy",
    37051: "Granite City Wrestling Association",
    37052: "Greg Gomez Trained Wrestling",
    37053: "Harlem Cougars WC",
    37054: "Harvey Twisters",
    37055: "Hawk WC",
    37056: "Headlock Wrestling Academy",
    37057: "Herrin Jr WC",
    37058: "Hillsboro Jr Toppers",
    37059: "Hinsdale Red Devil WC",
    37060: "Hononegah WC",
    37061: "Hoopeston Area WC",
    37062: "Iguana WC",
    37063: "Illini Bluffs Kids WC",
    37064: "Izzy Style Wrestling",
    37065: "Jacksonville Area Wrestling",
    37066: "Junior Comanche WC",
    37067: "Junior Cougar WC",
    37068: "Junior Kahoks",
    37069: "Junior Pioneer WC",
    37070: "Junior Porters WC",
    37071: "LP Crunching Cavs",
    37072: "Lakeland Predators WC",
    37073: "Lemont Bears",
    37074: "Libertyville Wildcats WC",
    37075: "Lincoln-Way WC",
    37076: "Lionheart Intense Wrestling",
    37077: "Lions WC",
    37078: "Little Huskies WC",
    37079: "Little Rams Wrestling",
    37080: "MC Bulldog WC",
    37081: "Maddog Wrestling Academy",
    37082: "Maine Eagles WC",
    37083: "Marengo Youth WC",
    37084: "Martinez Fox Valley Elite",
    37085: "Mattoon Youth WC",
    37086: "Maywood Bucs",
    37087: "Mean Green Machine",
    37088: "Mendota Mat Masters",
    37089: "Metamora Kids WC",
    37090: "Midwest Central Youth WC",
    37091: "Minooka Indians Elite",
    37092: "Moline WC",
    37093: "Morton Little Mustangs",
    37094: "Mt. Vernon Lions WC",
    37095: "Mt. Zion Kids WC",
    37096: "Murphysboro WC",
    37097: "Mustang WC",
    37098: "Naperville Hammer Huskies",
    37099: "Naperville WC",
    37100: "North Boone WC",
    37101: "North Shore Edge",
    37102: "Notre Dame WC",
    37103: "O`Fallon Little Panthers WC",
    37104: "Oak Forest Warriors",
    37105: "Oakwood Youth WC",
    37106: "Olney Cubs WC",
    37107: "Orland Park Pioneers",
    37108: "Palatine Cobras WC",
    37109: "Panther WC",
    37110: "Pekin Boys & Girls Club",
    37111: "Peoria Heights Minutemen WC",
    37112: "Peoria Razorbacks WC",
    37113: "Pitbull Wrestling Alliance",
    37114: "Pontiac WC",
    37115: "Prairie Central Hawks",
    37116: "Quincy Cyclones Wrestling",
    37117: "Rambler WC",
    37118: "Red Raiders Wrestling Team",
    37119: "Redhawk WC/Panther WC",
    37120: "Richmond WC",
    37121: "Riverton/Williamsville Youth Wrestling",
    37122: "Rochelle WC",
    37123: "Rochester WC",
    37124: "Rock Island WC",
    37125: "Rogue Wrestling",
    37126: "Roxana Outlaws",
    37127: "SCN Youth WC",
    37128: "Saber WC",
    37129: "Sauk Valley WC",
    37130: "Scorpion WC",
    37131: "Springfield Capitals Kids WC",
    37132: "St. Charles WC",
    37133: "St. Joseph Ogden Youth WC",
    37134: "Stillman Valley WC",
    37135: "Stockton Renegades",
    37136: "Storm Youth WC",
    37137: "Super Soldiers WC",
    37138: "Sycamore WC",
    37139: "TJ Trained",
    37140: "TJ Trained-Springfield",
    37141: "Team 1006 Wrestling",
    37142: "Team 312",
    37143: "Team Mascoutah WC",
    37144: "Team No Ego WC",
    37145: "The Law",
    37146: "The Wrestling Factory",
    37147: "Thundercats",
    37148: "Tiger Town Tanglers WC",
    37149: "Tinley Park Bulldogs WC",
    37150: "Tomcat WC",
    37151: "Triad Little Knights WC",
    37152: "UP Town WC",
    37153: "Unity Youth WC",
    37154: "Urbana Tigers WC",
    37155: "Vandalia Jr WC",
    37156: "Villa-Lombard Cougars",
    37157: "Waukegan Youth WC",
    37158: "Wheaton Warrenville Tiger WC",
    37159: "Will County Warriors",
    37160: "Wolves WC",
    37161: "Woodstock Cyclones",
    37162: "Wrestling 365",
    37163: "Xtreme WC",
    37164: "Yorkville WC",
    37165: "Young Guns",
    37166: "Z`s Team Pena",
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
    base_index = 37000
    with open(HERE / "extracted.2017.json") as file_obj:
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
