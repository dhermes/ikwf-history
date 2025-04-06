# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TEAM_NAME_MAPPING: dict[str, int] = {
    43000: "Alber Athletics WC",
    43001: "Argenta-Oreana Kids WC",
    43002: "Arlington Cardinals WC",
    43003: "Aurora WC",
    43004: "Badger WC",
    43005: "Barrington Broncos WC",
    43006: "Batavia WC",
    43007: "Beat the Streets Chicago-Avondale",
    43008: "Beat the Streets Chicago-Bellwood",
    43009: "Beat the Streets Chicago-Hyde Park",
    43010: "Beat the Streets Chicago-Midway",
    43011: "Beat the Streets Chicago-Oak Park",
    43012: "Belleville Little Devils WC",
    43013: "Belvidere Bandits WC",
    43014: "Blackhawk WC",
    43015: "Blue Crew WC",
    43016: "Blue Line Training Academy",
    43017: "Bolingbrook Junior Raiders WC",
    43018: "Built By Brunson Wrestling",
    43019: "Bulldog Elite WC",
    43020: "Bulls WC",
    43021: "Callan Wrestling Academy",
    43022: "Caravan Kids WC",
    43023: "Carlinville WC",
    43024: "Champaign WC",
    43025: "Champbuilders Wrestling",
    43026: "Charleston WC",
    43027: "Clipper WC",
    43028: "Collinsville WC",
    43029: "Combative Sports Athletic Center Wrestling",
    43030: "Contender Wrestling",
    43031: "Crawford County WC",
    43032: "Crosstown Spartan Elite WC",
    43033: "Crystal Lake Wizards WC",
    43034: "Cumberland Youth WC",
    43035: "DC WC",
    43036: "Danville Chargers WC",
    43037: "Demolition WC",
    43038: "Dinamo Wrestling",
    43039: "Dixon WC",
    43040: "Downers Grove WC",
    43041: "Dwight WC",
    43042: "East Peoria River Bandits Wrestling",
    43043: "East St. Louis WC",
    43044: "Edwardsville WC",
    43045: "Effingham Youth WC",
    43046: "El Paso Gridley Youth WC",
    43047: "Elevate Wrestling Academy",
    43048: "Elk Grove Junior Grens WC",
    43049: "Elmhurst Titans Wrestling Academy",
    43050: "Englewood Live Wire WC",
    43051: "Eureka WC",
    43052: "Evanston School of Wrestling",
    43053: "Falcon Youth WC",
    43054: "Fenton Jr. Bison WC",
    43055: "Fighting Farmers WC",
    43056: "Fitz Wrestling Academy",
    43057: "Force Elite WC",
    43058: "Fox Lake WC",
    43059: "Fox Valley WC",
    43060: "Frankfort Wildcats Wrestling",
    43061: "G2 WC",
    43062: "Gladiator Elite WC",
    43063: "Glenbard East Jr Rams WC",
    43064: "Granite City Wrestling Association",
    43065: "Greg Gomez Trained Wrestling",
    43066: "Harvard WC",
    43067: "Harvey Twisters WC",
    43068: "Hawk WC",
    43069: "Headlock Wrestling Academy",
    43070: "Herrin Junior WC",
    43071: "Highland Bulldog Jr. WC",
    43072: "Hinsdale Red Devil WC",
    43073: "Hononegah WC",
    43074: "Hoopeston Area WC",
    43075: "ISI WC",
    43076: "Izzy Style Wrestling",
    43077: "Junior Cougar WC",
    43078: "Junior Cyclones WC",
    43079: "Junior Titans Wrestling",
    43080: "LaSalle Peru Crunching Cavs Youth WC",
    43081: "Lakeland Predators WC",
    43082: "Lemont Bears WC",
    43083: "Lincoln-Way WC",
    43084: "Lion`s Den Wrestling Academy",
    43085: "Lionheart Intense Wrestling",
    43086: "Lions WC",
    43087: "Little Falcons WC",
    43088: "Lockport Junior Porters WC",
    43089: "Macomb Little Bombers Wrestling",
    43090: "MadDog Wrestling Academy",
    43091: "Maine Eagles WC",
    43092: "Marengo Youth WC",
    43093: "Martinez Fox Valley Elite WC",
    43094: "Mat Rat WC",
    43095: "Mattoon Youth WC",
    43096: "Moline WC",
    43097: "Mt. Zion Kids WC",
    43098: "Murphysboro Wrestling",
    43099: "Mustang WC",
    43100: "Naperville WC",
    43101: "Nomad Wrestling Academy",
    43102: "Notre Dame WC",
    43103: "O`Fallon Little Panthers WC",
    43104: "Oak Forest Warriors WC",
    43105: "Olney Cubs WC",
    43106: "Orland Park Pioneers WC",
    43107: "Oswego WC",
    43108: "Ottawa Wolfpack WC",
    43109: "PSF Wrestling Academy",
    43110: "Panther WC",
    43111: "Pekin Boys & Girls Club",
    43112: "Peoria Heights Minutemen WC",
    43113: "Peoria Razorbacks WC",
    43114: "Pontiac WC",
    43115: "Rantoul Youth Wrestling",
    43116: "Red Raiders Wrestling Team",
    43117: "Richmond WC",
    43118: "Riot Room Wrestling",
    43119: "River Bend WC",
    43120: "Road Warriors WC",
    43121: "Rochelle WC",
    43122: "Rock Island WC",
    43123: "SCN Youth WC",
    43124: "SJO Youth WC",
    43125: "SOT-C",
    43126: "Saber WC",
    43127: "Sauk Valley WC",
    43128: "Scorpion WC",
    43129: "Southern Illinois Bulldogs WC",
    43130: "Southside Outlaws WC",
    43131: "Sparta Junior Bulldogs WC",
    43132: "Springs Elite WC",
    43133: "St. Charles WC",
    43134: "Stampede WC",
    43135: "Stockton Renegades WC",
    43136: "Storm Youth WC",
    43137: "Sycamore WC",
    43138: "TJ Trained Wrestling",
    43139: "Team 312 WC",
    43140: "Team El1te Wrestling",
    43141: "Team Mascoutah WC",
    43142: "The Law WC",
    43143: "Tiger Town Tanglers WC",
    43144: "Tinley Park Bulldogs WC",
    43145: "Toss Em Up Wrestling Academy",
    43146: "Triad Knights WC",
    43147: "Tribe WC",
    43148: "Trico WC",
    43149: "Unity Youth WC",
    43150: "Urbana Tigers WC",
    43151: "Vandalia Jr WC",
    43152: "Vittum Cats WC",
    43153: "Warrior Wrestling",
    43154: "West Frankfort Jr. Redbirds WC",
    43155: "Wheaton Tigers WC",
    43156: "Will County Warriors WC",
    43157: "Williamsville WC",
    43158: "Wolfpak WC",
    43159: "Xtreme WC",
    43160: "Yorkville WC",
    43161: "nWo WC",
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
    base_index = 43000
    with open(HERE / "extracted.2023.json") as file_obj:
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
