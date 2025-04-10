# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 52
TEAM_NAME_MAPPING: dict[str, int] = {
    "AJ Jr. Wildcats WC": 42000,
    "Aces WC": 42001,
    "Alber Athletics WC": 42002,
    "Alton Little Redbirds WC": 42003,
    "Arlington Cardinals WC": 42004,
    "Astro WC": 42005,
    "Aurora WC": 42006,
    "Barrington Broncos WC": 42007,
    "Batavia WC": 42008,
    "Beat the Streets-Chicago": 42009,
    "Belleville Little Devils WC": 42010,
    "Belvidere Bandits WC": 42011,
    "Benton WC": 42012,
    "Blackhawk WC": 42013,
    "Blue Line Training Academy": 42014,
    "Bolingbrook Junior Raiders WC": 42015,
    "Brawlers WC": 42016,
    "Bulldog Elite WC": 42017,
    "Bulls WC": 42018,
    "Callan Wrestling Academy": 42019,
    "Champaign WC": 42020,
    "Charleston WC": 42021,
    "Clipper WC": 42022,
    "Combative Sports Athletic Center": 42023,
    "Crawford County WC": 42024,
    "Crosstown Spartan Elite WC": 42025,
    "Crystal Lake Wizards WC": 42026,
    "Cumberland Youth WC": 42027,
    "DC WC": 42028,
    "Dakota WC": 42029,
    "Danville Chargers WC": 42030,
    "Demolition WC": 42031,
    "Dixon WC": 42032,
    "Downers Grove WC": 42033,
    "Dundee Highlanders WC": 42034,
    "Dwight WC": 42035,
    "East St. Louis WC": 42036,
    "Edwardsville WC": 42037,
    "Effingham Youth WC": 42038,
    "Elevate Wrestling Academy": 42039,
    "Elk Grove Junior Grens WC": 42040,
    "Elmhurst Titans Wrestling Academy": 42041,
    "Englewood Live Wire WC": 42042,
    "Evanston School of Wrestling": 42043,
    "Falcon Youth WC": 42044,
    "Fenton Jr. Bison WC": 42045,
    "Fighting Farmers WC": 42046,
    "Fitz Wrestling Academy": 42047,
    "Force Elite WC": 42048,
    "Fox Lake WC": 42049,
    "Fox Valley WC": 42050,
    "Frankfort Wildcats Wrestling": 42051,
    "G2 WC": 42052,
    "Gladiator Elite WC": 42053,
    "Glenbard East Jr Rams WC": 42054,
    "Golden Eagles WC": 42055,
    "Granite City Wrestling Association": 42056,
    "Guerrero`s Garage Wrestling": 42057,
    "HPL Wrestling": 42058,
    "Harvey Twisters": 42059,
    "Hawk WC": 42060,
    "Herrin Junior WC": 42061,
    "Highland Bulldog Jr. WC": 42062,
    "Hillsboro Jr Toppers WC": 42063,
    "Hononegah WC": 42064,
    "Hoopeston Area WC": 42065,
    "ISI WC": 42066,
    "Izzy Style Wrestling": 42067,
    "Junior Bronco WC": 42068,
    "Junior Kahoks WC": 42069,
    "Junior Pioneer WC": 42070,
    "Junior Raiders West WC": 42071,
    "Junior Titans Wrestling": 42072,
    "Kaneland Knights WC": 42073,
    "LaSalle Peru Crunching Cavs Youth WC": 42074,
    "Lakeland Predators WC": 42075,
    "Lemont Bears WC": 42076,
    "Lil` Coalers WC": 42077,
    "Limestone Blue Crew WC": 42078,
    "Lincoln-Way WC": 42079,
    "Lion`s Den Wrestling Academy": 42080,
    "Lionheart Intense Wrestling": 42081,
    "Lions WC": 42082,
    "Little Falcons WC": 42083,
    "Little Huskies WC": 42084,
    "Lockport Junior Porters WC": 42085,
    "MadDog Wrestling Academy": 42086,
    "Maine Eagles WC": 42087,
    "Marengo Youth WC": 42088,
    "Mat Rat WC": 42089,
    "Mattoon Youth WC": 42090,
    "Metamora Kids WC": 42091,
    "Morton Youth WC": 42092,
    "Mt. Zion Kids WC": 42093,
    "Murphysboro Wrestling": 42094,
    "Mustang WC": 42095,
    "Naperville WC": 42096,
    "Nomad Wrestling Academy": 42097,
    "North Boone WC": 42098,
    "Notre Dame WC": 42099,
    "O`Fallon Little Panthers WC": 42100,
    "Oak Forest Warriors WC": 42101,
    "Olney Cubs WC": 42102,
    "Olympia WC": 42103,
    "Oswego WC": 42104,
    "Panther WC": 42105,
    "Pekin Boys & Girls Club": 42106,
    "Peoria Heights Minutemen WC": 42107,
    "Peoria Razorbacks WC": 42108,
    "Peoria Wizards WC": 42109,
    "Polo WC": 42110,
    "Pontiac WC": 42111,
    "Proviso Township Gladiators WC": 42112,
    "RWC": 42113,
    "Rantoul Youth Wrestling": 42114,
    "Red Raiders Wrestling Team": 42115,
    "Richmond WC": 42116,
    "River Bend WC": 42117,
    "Rochelle WC": 42118,
    "Rockford WC": 42119,
    "SCN Youth WC": 42120,
    "SJO Youth WC": 42121,
    "SOT-C": 42122,
    "Sauk Valley WC": 42123,
    "Scorpion WC": 42124,
    "Southside Outlaws WC": 42125,
    "Sparta Junior Bulldogs WC": 42126,
    "Spartan WC": 42127,
    "Springs Elite WC": 42128,
    "St. Charles WC": 42129,
    "Stampede WC": 42130,
    "Stingers WC": 42131,
    "Stockton Renegades WC": 42132,
    "Storm Youth WC": 42133,
    "Super Soldiers WC": 42134,
    "Sycamore WC": 42135,
    "TJ Trained Wrestling": 42136,
    "Team 1006 Wrestling": 42137,
    "Team 312 WC": 42138,
    "Team El1te Wrestling": 42139,
    "Team Mascoutah WC": 42140,
    "Team Poeta": 42141,
    "The Law WC": 42142,
    "Timber Wolves WC": 42143,
    "Tinley Park Bulldogs WC": 42144,
    "Toss Em Up Wrestling Academy": 42145,
    "Triad Knights WC": 42146,
    "Tribe WC": 42147,
    "Trico WC": 42148,
    "Unity Youth WC": 42149,
    "Urbana Tigers WC": 42150,
    "Vandalia Jr WC": 42151,
    "Vittum Cats WC": 42152,
    "Waterloo Bulldog Wrestling": 42153,
    "West Hancock WC": 42154,
    "Wheaton Tigers WC": 42155,
    "Whips WC": 42156,
    "Williamsville WC": 42157,
    "Wolfpak WC": 42158,
    "Xtreme WC": 42159,
    "Yorkville WC": 42160,
    "nWo WC": 42161,
}
BRACKET_ID_MAPPING: dict[tuple[bracket_utils.Division, int], int] = {
    ("novice", 60): 732,
    ("novice", 64): 733,
    ("novice", 69): 734,
    ("novice", 74): 735,
    ("novice", 80): 736,
    ("novice", 86): 737,
    ("novice", 93): 738,
    ("novice", 100): 739,
    ("novice", 108): 740,
    ("novice", 116): 741,
    ("novice", 125): 742,
    ("novice", 134): 743,
    ("novice", 154): 744,
    ("novice", 178): 745,
    ("novice", 215): 746,
    ("senior", 70): 747,
    ("senior", 74): 748,
    ("senior", 79): 749,
    ("senior", 84): 750,
    ("senior", 90): 751,
    ("senior", 96): 752,
    ("senior", 103): 753,
    ("senior", 110): 754,
    ("senior", 118): 755,
    ("senior", 126): 756,
    ("senior", 135): 757,
    ("senior", 144): 758,
    ("senior", 154): 759,
    ("senior", 164): 760,
    ("senior", 176): 761,
    ("senior", 188): 762,
    ("senior", 215): 763,
    ("senior", 275): 764,
}


def main():
    with open(HERE / "extracted.2022.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    weight_classes = extracted.weight_classes
    team_acronym_mapping = {team: team for team in TEAM_NAME_MAPPING.keys()}

    start_id = 17351
    mapped_competitors = bracket_utils.get_competitors_for_sql(
        start_id,
        weight_classes,
        team_acronym_mapping,
        {},
        {},
        TEAM_NAME_MAPPING,
    )

    start_id = 32707
    mapped_matches = bracket_utils.get_matches_for_sql(
        start_id,
        weight_classes,
        mapped_competitors.team_competitor_by_info,
        BRACKET_ID_MAPPING,
    )
    bracket_utils.print_matches_sql(mapped_matches.match_rows)


if __name__ == "__main__":
    main()
