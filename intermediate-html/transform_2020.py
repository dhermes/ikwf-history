# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
TOURNAMENT_ID = 51
TEAM_NAME_MAPPING: dict[str, int] = {
    "AJ Jr. Wildcats": 40000,
    "Addison Street WC": 40001,
    "Alton Little Redbirds WC": 40002,
    "Arlington Cardinals WC": 40003,
    "Astro WC": 40004,
    "Badger WC": 40005,
    "Barrington Broncos WC": 40006,
    "Batavia WC": 40007,
    "Beat the Streets-Chicago": 40008,
    "Belleville Little Devils WC": 40009,
    "Belvidere Bandits WC": 40010,
    "Belvidere WC": 40011,
    "Benton WC": 40012,
    "Bismarck-Henning Youth WC": 40013,
    "Blackhawk WC": 40014,
    "Bolingbrook Junior Raiders": 40015,
    "Brawlers WC": 40016,
    "Bulls WC": 40017,
    "Caravan Kids WC": 40018,
    "Carbondale WC": 40019,
    "Celtics WC": 40020,
    "Champaign WC": 40021,
    "Champbuilders Wrestling": 40022,
    "Charger WC": 40023,
    "Chicago Park District": 40024,
    "Clinton WC": 40025,
    "Clipper WC": 40026,
    "Combative Sports Athletic Center": 40027,
    "Contender Wrestling": 40028,
    "Cornerstone Wrestling": 40029,
    "Crawford County WC": 40030,
    "Crosstown Spartan Elite WC": 40031,
    "Crystal Lake Wizards": 40032,
    "Cumberland Youth WC": 40033,
    "DAWC": 40034,
    "DC WC": 40035,
    "Dakota WC": 40036,
    "Danville Chargers": 40037,
    "DeKalb WC": 40038,
    "Dinamo Wrestling": 40039,
    "Dixon WC": 40040,
    "Downers Grove WC": 40041,
    "Dundee Highlanders WC": 40042,
    "East St. Louis WC": 40043,
    "Edwardsville WC": 40044,
    "Effingham Youth WC": 40045,
    "El Paso Gridley Youth Wrestlng Club": 40046,
    "Elevate Wrestling Academy": 40047,
    "Elk Grove Junior Grens": 40048,
    "Evanston School of Wrestling": 40049,
    "Fenton Jr. Bison": 40050,
    "Fisher WC": 40051,
    "Force Elite": 40052,
    "Fox Lake WC": 40053,
    "Fox Valley WC": 40054,
    "Frankfort Gladiator Wrestling": 40055,
    "Frankfort Wildcats Wrestling": 40056,
    "Fulton County Stingers": 40057,
    "Geneva Junior Vikings": 40058,
    "Gladiator Elite": 40059,
    "Glenbard East Jr Rams WC": 40060,
    "Golden Eagles WC": 40061,
    "Granite City Wrestling Association": 40062,
    "Greg Gomez Trained Wrestling": 40063,
    "Guerrero`s Garage Wrestling": 40064,
    "Harlem Cougars WC": 40065,
    "Harvey Twisters": 40066,
    "Hawk WC": 40067,
    "Headlock Wrestling Academy": 40068,
    "Highland Bulldog Jr. WC": 40069,
    "Hononegah WC": 40070,
    "Iguana WC": 40071,
    "Izzy Style Wrestling": 40072,
    "Junior Eagles WC": 40073,
    "Junior Kahoks WC": 40074,
    "Junior Pioneer WC": 40075,
    "Kaneland Knights WC": 40076,
    "LaSalle Peru Crunching Cavs Youth WC": 40077,
    "Lakeland Predators WC": 40078,
    "Lawrence County WC": 40079,
    "Lemont Bears WC": 40080,
    "Libertyville Wildcats WC": 40081,
    "Lil Reaper WC": 40082,
    "Limestone Blue Crew": 40083,
    "Lincoln Youth WC": 40084,
    "Lincoln-Way WC": 40085,
    "Lion`s Den Wrestling Academy": 40086,
    "Lionheart Intense Wrestling": 40087,
    "Lions WC": 40088,
    "Little Falcons WC": 40089,
    "Little Huskies WC": 40090,
    "Lockport Junior Porters WC": 40091,
    "MS Youth WC": 40092,
    "MadDog Wrestling Academy": 40093,
    "Maine Eagles WC": 40094,
    "Marengo Youth WC": 40095,
    "Mattoon Youth WC": 40096,
    "Mendota Mat Masters": 40097,
    "Metamora Kids WC": 40098,
    "Minooka Indians Elite Wrestling": 40099,
    "Moline WC": 40100,
    "Mt. Vernon Lions Wrestling": 40101,
    "Mt. Zion Kids WC": 40102,
    "Murphysboro Wrestling": 40103,
    "Mustang WC": 40104,
    "Naperville Hammer Huskies": 40105,
    "Naperville WC": 40106,
    "Notre Dame WC": 40107,
    "O`Fallon Little Panthers WC": 40108,
    "Oak Forest Warriors": 40109,
    "Oakwood Youth WC": 40110,
    "Olympia WC": 40111,
    "Oswego WC": 40112,
    "Palatine Cobras WC": 40113,
    "Panther WC": 40114,
    "Pekin Boys & Girls Club": 40115,
    "Peoria Heights Minutemen WC": 40116,
    "Peoria Razorbacks WC": 40117,
    "Peoria Wizards WC": 40118,
    "Pitbull Wrestling Alliance": 40119,
    "Plainfield WC": 40120,
    "Pontiac WC": 40121,
    "Push Wrestling": 40122,
    "Quincy Cyclones WC": 40123,
    "RWC": 40124,
    "Rams WC": 40125,
    "Red Raiders Wrestling Team": 40126,
    "Reed Custer Jr. Panthers WC": 40127,
    "Respect Wrestling": 40128,
    "Richmond WC": 40129,
    "Riverton-Williamsville Youth Wrestling": 40130,
    "Road Warriors WC": 40131,
    "Robbins Park District Jayhawks": 40132,
    "Rochelle WC": 40133,
    "Rock Falls Junior Rocket Wrestling": 40134,
    "Rockets WC": 40135,
    "Roughnecks WC": 40136,
    "SCN Youth WC": 40137,
    "SOT-C": 40138,
    "Saber WC": 40139,
    "Sauk Valley WC": 40140,
    "Saukee Youth WC": 40141,
    "Scorpion WC": 40142,
    "Southside Outlaws WC": 40143,
    "Sparta Junior Bulldogs": 40144,
    "Spartan WC": 40145,
    "Springs Elite": 40146,
    "St. Charles WC": 40147,
    "St. Joseph Ogden Youth WC": 40148,
    "Stockton Renegades": 40149,
    "Storm Youth WC": 40150,
    "Super Soldiers WC": 40151,
    "Sycamore WC": 40152,
    "TJ Trained Wrestling": 40153,
    "Team 1006 Wrestling": 40154,
    "Team 312": 40155,
    "Team Poeta": 40156,
    "The Law": 40157,
    "Tiger Town Tanglers WC": 40158,
    "Timber Wolves WC": 40159,
    "Tinley Park Bulldogs": 40160,
    "Titan 2028 WC": 40161,
    "Tomcat WC": 40162,
    "Toss Em Up Wrestling Academy": 40163,
    "Triad Knights WC": 40164,
    "Tribe WC": 40165,
    "Unity Youth WC": 40166,
    "Urbana Tigers WC": 40167,
    "Vandal Kings": 40168,
    "Vandalia Jr WC": 40169,
    "Villa Park Young Warriors": 40170,
    "Villa-Lombard Cougars": 40171,
    "Vittum Cats": 40172,
    "Waterloo Bulldog Wrestling": 40173,
    "West Hancock WC": 40174,
    "Wheaton Warrenville Tiger WC": 40175,
    "Wheeling Wildcat WC": 40176,
    "Will County Warriors": 40177,
    "Wolves WC": 40178,
    "Wrestling Inc": 40179,
    "Xtreme WC": 40180,
    "Yorkville WC": 40181,
    "nWo WC": 40182,
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
    base_index = 40000
    with open(HERE / "extracted.2020.json") as file_obj:
        extracted = bracket_utils.ExtractedTournament.model_validate_json(
            file_obj.read()
        )

    team_scores = extracted.team_scores
    for division, division_team_scores in team_scores.items():
        for team_score in division_team_scores:
            id_ = base_index
            team_name = bracket_utils.sql_nullable_str(team_score.team)
            team_id = TEAM_NAME_MAPPING[team_score.team]
            score = team_score.score
            print(
                f"  ({id_}, {TOURNAMENT_ID}, '{division}', {team_id}, '', "
                f"{team_name}, {score}),"
            )
            # Prepare for next iteration
            base_index += 1


if __name__ == "__main__":
    main()
