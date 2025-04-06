# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 47
TEAM_NAME_MAPPING: dict[str, int] = {
    "AJ Junior Wildcats WC": 36000,
    "Aces WC": 36001,
    "Arlington Cardinals WC": 36002,
    "Badger WC": 36003,
    "Barrington Broncos WC": 36004,
    "Batavia WC": 36005,
    "Belleville Little Devils WC": 36006,
    "Belvidere Bandits WC": 36007,
    "Benton WC": 36008,
    "Bolingbrook Junior Raiders": 36009,
    "Brawlers WC": 36010,
    "Bulls WC": 36011,
    "Caravan Kids WC": 36012,
    "Carbondale WC": 36013,
    "Carlinville WC": 36014,
    "Carmi Bulldog WC": 36015,
    "Carterville Jr WC": 36016,
    "Cary Matmen WC": 36017,
    "Celtic Elite": 36018,
    "Central Illinois Wrestling Academy": 36019,
    "Champaign WC": 36020,
    "Champbuilders Wrestling": 36021,
    "Champions WC": 36022,
    "Charleston WC": 36023,
    "Chatham WC": 36024,
    "Chicago Park District": 36025,
    "Contender Wrestling": 36026,
    "Crawford County WC": 36027,
    "Crosstown Wrestling": 36028,
    "Crusaders` Elite": 36029,
    "Crystal Lake Wizards": 36030,
    "Cumberland Youth WC": 36031,
    "Dakota WC": 36032,
    "Danville Chargers Wrestling": 36033,
    "Downers Grove Cougars": 36034,
    "DuPage WC": 36035,
    "Dundee Highlanders WC": 36036,
    "East St. Louis Wrestling": 36037,
    "Edwardsville WC": 36038,
    "Elk Grove Junior Grens": 36039,
    "Elmhurst Jr Dukes": 36040,
    "Epic Wrestling": 36041,
    "Evanston School of Wrestling": 36042,
    "Falcon Elite WC": 36043,
    "Force WC": 36044,
    "Fox Lake WC": 36045,
    "Fox Valley WC": 36046,
    "Fuel WC": 36047,
    "Geneva Junior Vikings": 36048,
    "Glenbard East Jr Rams": 36049,
    "Golden Eagles WC": 36050,
    "Gomez Wrestling Academy": 36051,
    "Granite City Wrestling Association": 36052,
    "Grayslake WC": 36053,
    "Greg Gomez Trained Wrestling": 36054,
    "HF Spartan Elite WC": 36055,
    "Harlem Cougars WC": 36056,
    "Harvey Twisters WC": 36057,
    "Hawk WC Ltd.": 36058,
    "Headlock Wrestling Academy": 36059,
    "Hecox Team Benaiah": 36060,
    "Hinsdale Red Devil WC": 36061,
    "Hononegah WC": 36062,
    "Hoopeston Area WC": 36063,
    "Iguana WC": 36064,
    "Izzy Style Wrestling": 36065,
    "Jacksonville Area Wrestling": 36066,
    "Jersey Junior Panthers Wrestling": 36067,
    "Junior Comanche WC": 36068,
    "Junior Cougar WC": 36069,
    "Junior Kahoks": 36070,
    "Junior Pioneer WC": 36071,
    "LP Crunching Cavs": 36072,
    "Lakeland Predators WC": 36073,
    "Lemont Bears": 36074,
    "Lil Bucs WC": 36075,
    "Lincoln-Way Vittum Cats": 36076,
    "Lionheart Intense Wrestling": 36077,
    "Lions WC": 36078,
    "Little Boilers WC": 36079,
    "Little Huskies WC": 36080,
    "Little Rams Wrestling": 36081,
    "Little Redskins WC": 36082,
    "Maddog Wrestling Academy": 36083,
    "Maine Eagles WC": 36084,
    "Manteno Jr Panthers WC": 36085,
    "Marengo Youth WC": 36086,
    "Martinez Fox Valley Elite": 36087,
    "Mattoon Youth WC": 36088,
    "Maywood Bucs/Powerhouse": 36089,
    "Mean Green Machine": 36090,
    "Mendota Mat Masters": 36091,
    "Metamora Kids WC": 36092,
    "Midwest Central Youth WC": 36093,
    "Minooka Indians Elite": 36094,
    "Moline WC": 36095,
    "Morton Little Mustangs": 36096,
    "Mt. Olive Cats Kids Wrestling": 36097,
    "Mt. Vernon Lions WC": 36098,
    "Murphysboro WC": 36099,
    "Mustang/SKT WC": 36100,
    "Naperville WC": 36101,
    "North Shore Edge": 36102,
    "O`Fallon Little Panthers WC": 36103,
    "Oak Forest Warriors": 36104,
    "Olney Cubs WC": 36105,
    "Olympia WC": 36106,
    "Orland Park Pioneers": 36107,
    "Ottawa Crushers Kids WC": 36108,
    "Palatine Cobras WC": 36109,
    "Pekin Boys & Girls Club": 36110,
    "Peoria Heights Minutemen WC": 36111,
    "Peoria Razorbacks WC": 36112,
    "Pitbull Wrestling Alliance": 36113,
    "Pontiac WC": 36114,
    "Prairie Central Hawks": 36115,
    "Quincy Cyclones Wrestling": 36116,
    "Red Raiders Wrestling Team": 36117,
    "Redhawk WC": 36118,
    "Richmond WC": 36119,
    "Riverton Youth Wrestling": 36120,
    "Rock Island WC": 36121,
    "Rockets Youth WC": 36122,
    "Rockford WC": 36123,
    "Roxana Outlaws": 36124,
    "SCN Youth WC": 36125,
    "SIWA": 36126,
    "Saber WC": 36127,
    "Sauk Valley WC": 36128,
    "Saukee Youth WC": 36129,
    "Scorpion WC": 36130,
    "Sharks WC": 36131,
    "Somonauk Wrestlers Club": 36132,
    "Sparta Junior Bulldogs": 36133,
    "Springfield Capitals Kids WC": 36134,
    "St. Charles WC": 36135,
    "St. Joseph Ogden Youth WC": 36136,
    "St. Tarcissus WC": 36137,
    "Stillman Valley WC": 36138,
    "Stockton Renegades": 36139,
    "Storm Youth WC": 36140,
    "Super Soldiers WC": 36141,
    "Sycamore WC": 36142,
    "TJ Trained": 36143,
    "TJ Trained-Springfield": 36144,
    "Team 1006 Wrestling": 36145,
    "Team 312": 36146,
    "Team Mascoutah WC": 36147,
    "Team No Ego WC": 36148,
    "Team TopNotch Wrestling": 36149,
    "The Law": 36150,
    "The Wrestling Factory": 36151,
    "Thundercat Wrestling": 36152,
    "Tiger Town Tanglers WC": 36153,
    "Tinley Park Bulldogs WC": 36154,
    "Triad Little Knights WC": 36155,
    "Unity Youth WC": 36156,
    "Urbana Tigers WC": 36157,
    "Vandalia Jr WC": 36158,
    "Villa Park Young Warriors": 36159,
    "Villa-Lombard Cougars": 36160,
    "Warrior Wrestling": 36161,
    "Waukegan Youth WC": 36162,
    "West Frankfort Jr. Redbirds": 36163,
    "Wheaton Warrenville Tiger WC": 36164,
    "Will County Warriors": 36165,
    "Windy City Wrestling of Notre Dame": 36166,
    "Wolfpak WC": 36167,
    "Wolves WC": 36168,
    "Wrestling 365": 36169,
    "Xtreme WC": 36170,
    "Yorkville WC": 36171,
    "Young Guns Wrestling": 36172,
    "Z`s Team Pena": 36173,
    "Zee-Bee Stingers WC": 36174,
}


def _deduction_amount(value: float) -> int:
    if value >= 0:
        raise ValueError("Should be negative", value)

    as_int = int(value)
    if value != as_int:
        raise ValueError("Expect exact integer", value)

    return -as_int


def main():
    base_index = 300
    with open(HERE / "extracted.2016.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    deductions = extracted.deductions
    for i, deduction in enumerate(deductions):
        id_ = base_index + i
        team_name = bracket_utils.sql_nullable_str(deduction.team)
        team_id = TEAM_NAME_MAPPING[deduction.team]
        reason = bracket_utils.sql_nullable_str(deduction.reason)
        amount = _deduction_amount(deduction.value)
        print(
            f"  ({id_}, {TOURNAMENT_ID}, {team_id}, '', {team_name}, "
            f"{reason}, {amount}),"
        )


if __name__ == "__main__":
    main()
