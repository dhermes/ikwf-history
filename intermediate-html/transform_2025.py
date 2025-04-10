# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 55
TEAM_NAME_MAPPING: dict[str, int] = {
    "815 Stateline WC": 45000,
    "AJ Jr. Wildcats WC": 45001,
    "Aces WC": 45002,
    "Alber Athletics WC": 45003,
    "Alton Little Redbirds WC": 45004,
    "Antioch Predators WC": 45005,
    "Arlington Cardinals WC": 45006,
    "Assumption Elite WC": 45007,
    "Astro WC": 45008,
    "Aurora WC": 45009,
    "BTS Chicago-Avondale": 45010,
    "BTS Chicago-Midway": 45011,
    "BTS Chicago-Oak Park": 45012,
    "BTS Chicago-Roseland": 45013,
    "BTS Chicago-Tri Taylor": 45014,
    "Backyard Brawlers Midwest": 45015,
    "Backyard Brawlers North Wrestling": 45016,
    "Badger WC": 45017,
    "Barrington Broncos WC": 45018,
    "Batavia WC": 45019,
    "Belleville Little Devils WC": 45020,
    "Belvidere Bandits WC": 45021,
    "Benton WC": 45022,
    "Bismarck-Henning Youth WC": 45023,
    "Blackhawk WC": 45024,
    "Bloomingdale Bears WC": 45025,
    "Blue Line Training Academy": 45026,
    "Bolingbrook Junior Raiders WC": 45027,
    "Brawlers WC": 45028,
    "Built By Brunson Wrestling": 45029,
    "Bulldog Elite WC": 45030,
    "Bulldog Youth Sports Wrestling": 45031,
    "Bulls WC": 45032,
    "Callan Wrestling Academy": 45033,
    "Camp Point Youth Wrestling": 45034,
    "Caravan Kids WC": 45035,
    "Carbondale WC": 45036,
    "Cardinals WC": 45037,
    "Carlinville WC": 45038,
    "Carthage WC": 45039,
    "Celtic Wrestling Academy": 45040,
    "Central Illinois Bulldogs WC": 45041,
    "Centralia WC": 45042,
    "Champaign WC": 45043,
    "Champions WC": 45044,
    "Charleston WC": 45045,
    "Chatham WC": 45046,
    "Clinton WC": 45047,
    "Clipper": 45048,
    "Cogs WC": 45049,
    "Collinsville WC": 45050,
    "Combative Sports Athletic Center Wrestling": 45051,
    "Cory Clark Wrestling": 45052,
    "Crawford County WC": 45053,
    "Crosstown Spartan Elite WC": 45054,
    "Crystal Lake Wizards WC": 45055,
    "Cumberland Youth WC": 45056,
    "DC WC": 45057,
    "Dakota WC": 45058,
    "Danville Chargers WC": 45059,
    "DeKalb WC": 45060,
    "Decatur Dawgs WC": 45061,
    "Decatur Lakers WC": 45062,
    "Demolition WC": 45063,
    "Dinamo Wrestling": 45064,
    "Dixon WC": 45065,
    "Doom Wrestling": 45066,
    "Downers Grove WC": 45067,
    "Dubtown WC": 45068,
    "Dundee Highlanders WC": 45069,
    "Dungeon WC": 45070,
    "Dwight WC": 45071,
    "East Peoria River Bandits Wrestling": 45072,
    "East St. Louis WC": 45073,
    "Edwardsville WC": 45074,
    "Effingham Youth WC": 45075,
    "El Paso Gridley Youth WC": 45076,
    "Elk Grove Junior Grens WC": 45077,
    "Elmhurst Titans Wrestling Academy": 45078,
    "Englewood Live Wire WC": 45079,
    "Eureka WC": 45080,
    "Evanston School of Wrestling": 45081,
    "Falcon Youth Wrestling": 45082,
    "Fighting Farmers WC": 45083,
    "Fisher WC": 45084,
    "Fit & Fight Gym WC": 45085,
    "Force Elite WC": 45086,
    "Fox Lake WC": 45087,
    "Fox Valley WC": 45088,
    "Frankfort Gladiator Wrestling": 45089,
    "Frankfort Wildcats Wrestling": 45090,
    "Gators Elite WC": 45091,
    "Geneva Junior Vikings": 45092,
    "Gladiator Elite WC": 45093,
    "Glenbard East Jr Rams WC": 45094,
    "Golden Eagles WC": 45095,
    "Gomez Wrestling RTC": 45096,
    "Grayslake Youth WC": 45097,
    "Greg Gomez Trained Wrestling": 45098,
    "Harlem Huskies WC": 45099,
    "Harvard WC": 45100,
    "Harvey Twisters WC": 45101,
    "Hawk WC": 45102,
    "Headlock Wrestling Academy": 45103,
    "Herrin Tiger Wrestling": 45104,
    "Highland Bulldog Jr. WC": 45105,
    "Hillsboro Jr Toppers WC": 45106,
    "Hinsdale Red Devil WC": 45107,
    "Hononegah WC": 45108,
    "Hoopeston Area Youth Wrestling": 45109,
    "ISI WC": 45110,
    "Iguana WC": 45111,
    "Impact Wrestling": 45112,
    "Irish WC": 45113,
    "Izzy Style Wrestling": 45114,
    "J.R. Warrior WC": 45115,
    "Jacksonville Area Wrestling": 45116,
    "Jersey Junior Panthers Wrestling": 45117,
    "Junior Bulldog WC": 45118,
    "Junior Cougar WC": 45119,
    "Junior Cyclones WC": 45120,
    "Junior Pioneer WC": 45121,
    "Junior Titans Wrestling": 45122,
    "Knights WC": 45123,
    "LaSalle Peru Crunching Cavs Youth WC": 45124,
    "Lake County Stallions Wrestling Academy": 45125,
    "Lake Zurich Cubs WC": 45126,
    "Lawrence County Knights WC": 45127,
    "Lemont Bears WC": 45128,
    "Lil Reaper WC": 45129,
    "Lil` Coalers WC": 45130,
    "Limestone WC": 45131,
    "Lincoln-Way WC": 45132,
    "Lionheart Intense Wrestling": 45133,
    "Lions WC": 45134,
    "Lisle WC": 45135,
    "Litchfield WC": 45136,
    "Little Giants WC": 45137,
    "Lockport Junior Porters WC": 45138,
    "MS Youth WC": 45139,
    "Macomb Little Bombers Wrestling": 45140,
    "MadDog Wrestling Academy": 45141,
    "Maine Eagles WC": 45142,
    "Marengo Youth WC": 45143,
    "Marshall Red Rush Wrestling": 45144,
    "Martinez Fox Valley Elite WC": 45145,
    "Mat Rat WC": 45146,
    "Mattoon Youth WC": 45147,
    "McHenry WC": 45148,
    "Meridian Hawks Youth WC": 45149,
    "Metamora Kids WC": 45150,
    "Midwest Central Youth WC": 45151,
    "Moline WC": 45152,
    "Monticello Youth WC": 45153,
    "Morris WC": 45154,
    "Morton Youth WC": 45155,
    "Mt. Zion Kids WC": 45156,
    "Murphysboro Wrestling": 45157,
    "Mustang WC": 45158,
    "N.Y.A Jr. Rebels WC": 45159,
    "Naperville WC": 45160,
    "Nomad Wrestling Academy": 45161,
    "Notre Dame WC": 45162,
    "O`Fallon Little Panthers WC": 45163,
    "Oak Forest P. D. Warriors Wrestling": 45164,
    "Oakwood Youth WC": 45165,
    "Olney Cubs WC": 45166,
    "Olympia WC": 45167,
    "Orland Park Pioneers WC": 45168,
    "Oswego WC": 45169,
    "Ottawa Wolfpack WC": 45170,
    "P3 Warrior Wrestling Academy": 45171,
    "PSF Wrestling Academy": 45172,
    "Panther Paw WC": 45173,
    "Panther Powerhouse Wrestling": 45174,
    "Panther WC": 45175,
    "Pekin Boys & Girls Club": 45176,
    "Peoria Heights Minutemen WC": 45177,
    "Peoria Razorbacks WC": 45178,
    "Peoria Wizards WC": 45179,
    "Peotone Little Devils WC": 45180,
    "Petersburg WC": 45181,
    "Polo WC": 45182,
    "Pontiac WC": 45183,
    "Prairie Central Youth Wrestling": 45184,
    "Proviso Township Gladiators WC": 45185,
    "Quincy Little Raiders WC": 45186,
    "RWC": 45187,
    "Rantoul Youth Wrestling": 45188,
    "Red Raiders Wrestling Team": 45189,
    "Reed Custer Jr. Panthers WC": 45190,
    "Riot Room Wrestling": 45191,
    "River Bend WC": 45192,
    "Riverdale WC": 45193,
    "Rochelle Wrestling Club": 45194,
    "Rock Island WC": 45195,
    "Rocket Fuel WC": 45196,
    "Rockets WC": 45197,
    "Rockford WC": 45198,
    "Roughnecks WC": 45199,
    "Round Lake Jr. Panthers WC": 45200,
    "Roxana WC": 45201,
    "SCN Youth WC": 45202,
    "SJO Spartan YWC": 45203,
    "SOT-C": 45204,
    "Saber WC": 45205,
    "Salem WC": 45206,
    "Sandwich WC": 45207,
    "Sauk Valley WC": 45208,
    "Saukee Youth WC": 45209,
    "Shadow Wolves Wrestling": 45210,
    "Sharks WC": 45211,
    "Shelbyville Jr. Wrestling Rams": 45212,
    "Sherrard Jr. Tigers WC": 45213,
    "Southern Illinois Bulldogs WC": 45214,
    "Southside Outlaws WC": 45215,
    "Sparta Junior Bulldogs WC": 45216,
    "Spartan WC": 45217,
    "Springs Elite WC": 45218,
    "St. Charles WC": 45219,
    "Stateline Stingers WC": 45220,
    "Stillman Valley WC": 45221,
    "Stockton Renegades WC": 45222,
    "Storm Youth WC": 45223,
    "Streator WC": 45224,
    "Sycamore WC": 45225,
    "TJ Trained Wrestling": 45226,
    "Taylorville WC": 45227,
    "Team 312 WC": 45228,
    "Team El1te Wrestling": 45229,
    "Team Mascoutah WC": 45230,
    "Team Piasa WC": 45231,
    "The Island City Misfits Elite Wrestling": 45232,
    "The Law WC": 45233,
    "Thunder WC": 45234,
    "Tiger Elite Wrestling Inc.": 45235,
    "Tiger Town Tanglers WC": 45236,
    "Timber Wolves WC": 45237,
    "Tinley Park Bulldogs WC": 45238,
    "Tony Capriola Sr. WC": 45239,
    "Top Dog WC": 45240,
    "Toss Em Up Wrestling Academy": 45241,
    "Triad Knights WC": 45242,
    "Trico WC": 45243,
    "Unity Youth WC": 45244,
    "Urbana Tigers WC": 45245,
    "Vandalia Jr WC": 45246,
    "Victory Elite Wrestling": 45247,
    "Villa Park Young Warriors WC": 45248,
    "Vittum Cats WC": 45249,
    "Vortex WC": 45250,
    "Warrensburg-Latham Jr. Cardinals WC": 45251,
    "Warriors Wrestling Academy": 45252,
    "West Frankfort Jr. Redbirds WC": 45253,
    "West Suburban Girls WC": 45254,
    "Westville Youth Wrestling": 45255,
    "Wheaton WC": 45256,
    "Wheeling Wildcat WC": 45257,
    "Wildcats Wrestling Academy": 45258,
    "Will County Warriors WC": 45259,
    "Williamsville WC": 45260,
    "Wilmington WC": 45261,
    "Wolfpak WC": 45262,
    "Wolves WC": 45263,
    "Woodstock Cyclones WC": 45264,
    "Xtreme WC": 45265,
    "Yorkville WC": 45266,
    "Young Warrior Wrestling Academy": 45267,
    "Zero Fox Wrestling": 45268,
    "nWo WC": 45269,
}
BRACKET_ID_MAPPING: dict[tuple[bracket_utils.Division, int], int] = {
    ("bantam", 43): 897,
    ("bantam", 46): 898,
    ("bantam", 49): 899,
    ("bantam", 52): 900,
    ("bantam", 55): 901,
    ("bantam", 58): 902,
    ("bantam", 62): 903,
    ("bantam", 66): 904,
    ("bantam", 70): 905,
    ("bantam", 76): 906,
    ("bantam", 84): 907,
    ("bantam", 95): 908,
    ("bantam", 120): 909,
    ("intermediate", 55): 910,
    ("intermediate", 59): 911,
    ("intermediate", 64): 912,
    ("intermediate", 69): 913,
    ("intermediate", 74): 914,
    ("intermediate", 79): 915,
    ("intermediate", 84): 916,
    ("intermediate", 90): 917,
    ("intermediate", 98): 918,
    ("intermediate", 108): 919,
    ("intermediate", 122): 920,
    ("intermediate", 148): 921,
    ("intermediate", 177): 922,
    ("novice", 60): 923,
    ("novice", 64): 924,
    ("novice", 69): 925,
    ("novice", 74): 926,
    ("novice", 80): 927,
    ("novice", 86): 928,
    ("novice", 93): 929,
    ("novice", 100): 930,
    ("novice", 108): 931,
    ("novice", 116): 932,
    ("novice", 125): 933,
    ("novice", 134): 934,
    ("novice", 154): 935,
    ("novice", 178): 936,
    ("novice", 215): 937,
    ("senior", 74): 938,
    ("senior", 79): 939,
    ("senior", 84): 940,
    ("senior", 90): 941,
    ("senior", 96): 942,
    ("senior", 103): 943,
    ("senior", 110): 944,
    ("senior", 118): 945,
    ("senior", 126): 946,
    ("senior", 135): 947,
    ("senior", 144): 948,
    ("senior", 154): 949,
    ("senior", 164): 950,
    ("senior", 176): 951,
    ("senior", 188): 952,
    ("senior", 215): 953,
    ("senior", 275): 954,
    ("bantam_girls", 45): 955,
    ("bantam_girls", 50): 956,
    ("bantam_girls", 55): 957,
    ("bantam_girls", 61): 958,
    ("bantam_girls", 67): 959,
    ("bantam_girls", 74): 960,
    ("bantam_girls", 85): 961,
    ("bantam_girls", 95): 962,
    ("bantam_girls", 115): 963,
    ("intermediate_girls", 53): 964,
    ("intermediate_girls", 57): 965,
    ("intermediate_girls", 62): 966,
    ("intermediate_girls", 67): 967,
    ("intermediate_girls", 72): 968,
    ("intermediate_girls", 77): 969,
    ("intermediate_girls", 82): 970,
    ("intermediate_girls", 88): 971,
    ("intermediate_girls", 95): 972,
    ("intermediate_girls", 115): 973,
    ("intermediate_girls", 135): 974,
    ("novice_girls", 63): 975,
    ("novice_girls", 68): 976,
    ("novice_girls", 74): 977,
    ("novice_girls", 80): 978,
    ("novice_girls", 85): 979,
    ("novice_girls", 90): 980,
    ("novice_girls", 96): 981,
    ("novice_girls", 102): 982,
    ("novice_girls", 108): 983,
    ("novice_girls", 115): 984,
    ("novice_girls", 125): 985,
    ("novice_girls", 140): 986,
    ("novice_girls", 185): 987,
    ("senior_girls", 75): 988,
    ("senior_girls", 80): 989,
    ("senior_girls", 85): 990,
    ("senior_girls", 90): 991,
    ("senior_girls", 95): 992,
    ("senior_girls", 100): 993,
    ("senior_girls", 105): 994,
    ("senior_girls", 110): 995,
    ("senior_girls", 115): 996,
    ("senior_girls", 120): 997,
    ("senior_girls", 125): 998,
    ("senior_girls", 130): 999,
    ("senior_girls", 135): 1000,
    ("senior_girls", 145): 1001,
    ("senior_girls", 185): 1002,
    ("senior_girls", 240): 1003,
}


def main():
    with open(HERE / "extracted.2025.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    weight_classes = extracted.weight_classes
    team_acronym_mapping = {team: team for team in TEAM_NAME_MAPPING.keys()}

    start_id = 20759
    mapped_competitors = bracket_utils.get_competitors_for_sql(
        start_id,
        weight_classes,
        team_acronym_mapping,
        {},
        {},
        TEAM_NAME_MAPPING,
    )

    start_id = 41069
    mapped_matches = bracket_utils.get_matches_for_sql(
        start_id,
        weight_classes,
        mapped_competitors.team_competitor_by_info,
        BRACKET_ID_MAPPING,
    )
    bracket_utils.print_matches_sql(mapped_matches.match_rows)


if __name__ == "__main__":
    main()
