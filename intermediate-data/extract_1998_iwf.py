# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib

import bracket_utils

HERE = pathlib.Path(__file__).resolve().parent
_JUNIOR_TEAM_SCORES: dict[str, float] = {
    "Harvey Twisters": 27.0,
    "Granite City Coolidge": 23.0,
    "Arlington Cardinals": 17.0,
    "Panther Wrestling Club": 12.0,
    "Wrestling Factory": 12.0,
}
_NOVICE_TEAM_SCORES: dict[str, float] = {
    "Wrestling Factory": 160.5,
    "Dolton Park Falcons": 119.0,
    "Carmel Corsair": 116.0,
    "Lions Wrestling Club": 105.0,
    "Harvey Twisters": 100.5,
    "Oak Forest Warriors": 93.5,
}
_SENIOR_TEAM_SCORES: dict[str, float] = {
    "Pekin": 132.0,
    "Lake Villa Lancers": 126.0,
    "Dolton Park Falcons": 122.5,
    "Moline": 111.0,
    "Jr. Bears": 89.5,
    "Joliet Boys Club": 83.5,
}
_JUNIOR_PLACERS_TEXT = """\
55
1st--D. Lund, Wrestling Factory, d, C. Nance, Granite City Coolidge, Dec 7-0.
3rd--T Webster, Harvey Twisters, md, D Moreno, West Chicago, MajDec 11-1.

58
1st--J. Kennedy, Wrestling Factory, f, M. Morgan, Harvey Twisters, Fall 2:44.
3rd--Tom Wolf, Rich Wrestling, d, J Green, Maywood, Dec 4-2.

62
1st--Troy Howell, Granite City Coolidge, d, Steve Walsh, Panther Wrestling Club, Dec 2-0.
3rd--Peter Zintac, Arlington Cardinals, md, B Gartner, Raiders, MajDec 10-0.

66
1st--J. Keske, Wrestling Factory, d, A. Wagoner, Granite City Coolidge, Dec 7-1.
3rd--M Benefield, Men In Black, d, C Sakovich, Calumet City, Dec 9-2.

70
1st--Jeff Carney, Granite City Coolidge, d, Erik Hanson, Lan-Oak, Dec 9-4.
3rd--Rob Lewandowski, Panther Wrestling Club, d, N George, Moline, Dec 5-4.

74
1st--Travis Hammons, Harvey Twisters, d, Jamie Smith, Bison, Dec 7-3.
3rd--Scott Zinzer, Tomcats, md, Brian Lange, Falcons, MajDec 9-1.

79
1st--Ben Petry, Blackhawk, d, David Wells, Collinsville, Dec 1-0.
3rd--A Walden, Raiders, md, J Pivoriunas, Calumet City, MajDec 12-1.

84
1st--Laquan Melvin, Tomcats, f, Sean Simon, Maywood, Fall :36.
3rd--Jamal Muhammad, Harvey Twisters, d, John Snyder, Pekin, Dec 6-4.

89
1st--TJ Nance, Granite City Coolidge, d, James Kernats, Panther Wrestling Club, Dec 6-4.
3rd--Craig Agree, Falcons, f, Jeff Daisy, Lan-Oak, Fall 2:50.

95
1st--Omar Abdullah, Lockport, tf, N. Howard, MS Kids, TF 17-0.
3rd--J Chaulsett, Granite City Coolidge, d, D Albergo, Arlington Cardinals, Dec 6-1.

108
1st--Jarvis Lowe, Harvey Twisters, f, Dustin Arnold, Falcons, Fall 2:41.
3rd--Jacob Blanton, Richmond, d, Nick Williams, Joliet Boys Club, Dec 5-2.

122
1st--Eric Lueders, Bison, md, Adrian Cerrillo, Joliet Boys Club, MajDec 10-0.
3rd--Chad Truetler, Palatine, md, Steve Cincotti, Lions Wrestling Club, MajDec 9-0.

138
1st--M. Jurkovic, Calumet City, f, T. Hefferman, Arlington Cardinals, Fall 1:52
3rd--Christian Brantley, Harvey Twisters, d, R Panayi, Palatine, Dec 14-9.

170
1st--Sean Johnson, Harvey Twisters, d, Zachary Hausner, Panther Wrestling Club, Dec 4-0.
3rd--Mike Chlamovski, Lions Wrestling Club, uncontested.
"""
_NOVICE_PLACERS_TEXT = """\
62
1st--Joey Lane, Pekin, f, Joe Rokowski, Panther Wrestling Club, Fall 2:28.
3rd--Charlie Wolf, Fenwick, d, Jerard Jones, Dolton Park Falcons, Dec 6-4.
5th--Keenan James, Maywood, md, Chris Alexander, Pekin, MajDec 13-3.

66
1st--Kenny Jordan, Dolton Park Falcons, d, Angel Escobedo, Dolton Park Falcons, Dec 3-1.
3rd--Jack Valin, Arlington Cardinals, md, Joe Kastens, Jr. Bears, MajDec 8-0.
5th--Vince Castillo, Lions Wrestling Club, d, G. Melvan, Oak Forest Warriors, Dec 9-2.

70
1st--Michael Simmons, Wrestling Factory, f, R. Overby, Lake Villa Lancers, Fall 2:03.
3rd--R. Stewart, Wrestling Factory, d, B. Peach, Granite City Coolidge, Dec 5-1.
5th--J. Kastens, Lake Zurich, disqualif.

74
1st--Dan Zeman, Lions Wrestling Club, f, K. Scholle, Carmel Corsair, Fall :48.
3rd--M. Fiordirosa, Wrestling Factory, md, D. Depyper, Oak Forest Warriors, MajDec 12-1.
5th--M. Smith, Bison, d, H. Felgar, Moline, Dec 5-2.

79
1st--Jeffery Canella, Wrestling Factory, f, T. Campbell, Granite City Coolidge, Fall :30.
3rd--P. Castillo, Lions Wrestling Club, d, B. Carey, Panther Wrestling Club, Dec 8-3.
5th--E. Munox, Joliet Boys Club, md, S. Stoltz, Arlington Cardinals, MajDec 16-4.

84
1st--Charles Lloyd, Harvey Twisters, d, Mark Friend, Wrestling Factory, Dec 4-2.
3rd--Alex Tsirtsis, Dolton Park Falcons, d, Aaron Benoel, St. Tars, Dec 12-8.
5th--Jeff Broadway, Joliet Boys Club, d, J. Clark, Arlington Cardinals, Dec 8-6.

89
1st--Jim Griffin, Oak Forest Warriors, md, A. Hernandez, Dolton Park Falcons, MajDec 13-4.
3rd--M. Burke, Bison, d, B. Malone, Tomcats, UTB 0-0.
5th--L. Silva, Blue Island, md, M. Cook, DeKalb, MajDec 16-3.

95
1st--G. Pruger, Fenwick, d, E. Dardanes, OPRF, Dec 6-0.
3rd--W. Goodman, Arlington Cardinals, f, V. Rizzi, Lan-Oak, Fall :55.
5th--B. Urbaniak, Hoffman Estates, md, M. Wojcik, Carmel Corsair, MajDec 10-0.

101
1st--Mark Kehm, St. Charles, d, Chris Mellender, Carmel Corsair, Dec 9-4.
3rd--J. Kelly, Oak Forest Warriors, d, M. Tamillo, Addison, Dec 7-1.
5th--D. Lyons, St. Tars, d, J. Polich, Panther Wrestling Club, Dec 8-1.

108
1st--Alonzo Noble, Harvey Twisters, d, Chris Potter, St. Charles, Dec 12-10.
3rd--Joshua Mellender, Carmel Corsair, f, Bobby Larson, DeKalb, Fall 3:49.
5th--Bobby Hopkins, Knights, fft.

115
1st--Michael Goede, Calumet City, d, Ben Bernal, Hoffman Estates, Dec 5-1.
3rd--A. Lowe, Harvey Twisters, f, T. Bowken, Blackhawk, Fall :39.
5th--A. Gilliand, El Paso, f, C. Price, El Paso, Fall 3:32.

122
1st--Tyler Watkins, OPRF, d, B. Suler, Blackhawk, Dec 13-8.
3rd--K. Brolsma, St. Charles, f, D. Ferrell, Blackhawk, Fall 3:15.
5th--P. McCormic, Central, f, J. Urrutia, Falcons, Fall 3:19.

130
1st--C. Muller, Rich Wrestling, d, M. Benson, Shamrock WC, Dec 4-3.
3rd--J. Lange, Falcons, md, C. Scholle, Carmel Corsair, MajDec 9-0.
5th--P. Szigetuari, Jr. Bears, d, K. Sigler, El Paso, Dec 10-9.

147
1st--Robby Walleck, Wrestling Factory, f, Jason James, Maywood, Fall :47.
3rd--John Hydo, Schaumburg, f, Sean Stowell, Pekin, Fall :17.
5th--D. Cozzi, St. Charles, f, T. Kuna, Raiders, Fall :51.

166
1st--Dave Herrera, Falcons, d, Russ Flanders, Knights, Dec 8-2.
3rd--Aidan Farrelly, Panther Wrestling Club, f, Jake Dteman, Lions Wrestling Club, Fall 3:59.
5th--Tyler Breusewitz, Elmhurst, d, T. Noonan, Raiders, Dec 5-0.

215
1st--Tim Fitzgerald, Lions Wrestling Club, f, Nathan Perez, West Chicago, Fall :43.
3rd--Mathew Hardy, Bison, f, A. Sawatski, Oak Forest Warriors, Fall :56.
5th--L. Bulow, Lockport, inj dflt, M. Walsh, DeKalb, Dflt.
"""
_SENIOR_PLACERS_TEXT = """\
70
1st--Mike Pearson, Lions Wrestling Club, f, Matt Outinen, Lake Villa Lancers, Fall 1:49.

74
1st--Frank Agnoli, Lake Villa Lancers, d, Joseph Neubauer, St. Charles, Dec 9-5.
3rd--Scott Bodziak, Schaumburg, d, Ryan Bourbon, Addison, Dec 13-8.
5th--Arturo Flores, Addison, fft.

79
1st--Cassio Pero, Harvey Twisters, f, Taylor Hosick, Lake Villa Lancers, Fall 1:39.
3rd--randy Kerby, Pekin, f, H. Hiller, Lincolnway, Fall :40.
5th--R. Schuster, Lake Villa Lancers, md, A. Hartline, Granite City Coolidge, MajDec 9-1.

84
1st--David Silva, Jr. Bears, f, Nick Fyock, Bison, Fall :46.
3rd--Kris Enger, St. Charles, md, S. Sammons, Arlington Cardinals, MajDec 11-3.
5th--A. Kernats, Panther Wrestling Club, md, A. Rex, Central, MajDec 12-1.

89
1st--Larry Amedio, Dolton Park Falcons, d, R. Estrada, Round Lake, Dec 7-5.
3rd--B. Wapolish, Jr. Bears, d, C. Chebny, Lake Villa Lancers, Dec 8-4.
5th--T. Aufmann, Jr. Bears, d, P. Ireland, West Chicago, Dec 11-5.

95
1st--Tom Tedesco, Granite City Coolidge, d, E. Gerdes, Oak Forest Warriors, OT 3-1.
3rd--J Friend, Wrestling Factory, f, J. Rich, Sycamore, Fall :17.
5th--J. Besse, Lan-Oak, d, B. Ghenardini, Charleston, Dec 2-0.

101
1st--Eric Scholle, Carmel Corsair, d, J. Curby, Lions Wrestling Club, Dec 7-5.
3rd--H. Diedrid, Crystal Lake, d, J. DeBias, Demons, Dec 7-2.
5th--B. Bairston, Wrestling Factory, d, D. Gibbs, Moline, Dec 7-2.

108
1st--S. Grece, Jr. Trojans, d, J. Yost, Grapplin Devils, Dec 4-2.
3rd--T. Bagby, Joliet Boys Club, md, B. Mathews, Knights, MajDec 11-0.
5th--A. VanKampen, Demons, f, M. Dombrowski, Fenwick, Fall :51.

115
1st--Frank Keeler, Dolton Park Falcons, f, Mike Zagorski, Jr. Bears, Fall :33.
3rd--Tony Catour, Moline, f, J. Coleman, Calumet City, Fall 1:37.
5th--N. Aye, West Chicago, d, B. Wyatt, Granite City Coolidge, Dec 6-3.

122
1st--Brandon Hill, Joliet Boys Club, f, Ryan McMurray, Lions Wrestling Club, Fall 1:42.
3rd--Joseph Kierzek, Schaumburg, d, R. Myers, Lake Villa Lancers, Dec 3-1.
5th--A. Clay, Lockport, f, D. Clifford, Granite City Coolidge, Fall :56.

130
1st--D. Bedoy, Dolton Park Falcons, tf, M. Haraf, Oak Forest Warriors, TF 15-0.
3rd--R. Henderson, Rich Wrestling, d, B. Neuberg, North Shore Gators, Dec 6-4.
5th--J. Curry, Raiders, f, S. Kehm, St. Charles, Fall 1:55.

138
1st--Michael Escobedo, Dolton Park Falcons, d, Derek Bly, Pekin, Dec 9-3.
3rd--Zach Frazier, Central, dflt, Jerry Bowker, J-Hawks, Dflt.
5th--Jim Treakle, Granite City Coolidge, f, M. Galloway, St. Charles, Fall 3:28.

147
1st--Dustin Doctor, Sycamore, f, B. Michalowski, Calumet City, Fall 2:00.
3rd--C. Johnson, Falcons, d, B. Hoye, Pekin, Dec 10-6.
5th--B. Sawer, Knights, f, K. Crawford, Renegades, Fall 2:24.

156
1st--Josh Hendricks, St. Charles, f, Tony Sosin, Sycamore, Fall 1:02.
3rd--Kyle Walker, Pekin, f, Matt Yena, Lions Wrestling Club, Fall 1:07.
5th--Brian Booth, Knights, f, J. Weber, Wrestling Factory, Fall 1:26.

166
1st--M. Johnson, Falcons, d, M. Echevarria, Carmel Corsair, Dec 11-8.
3rd--J. Halpert, J-Hawks, f, B. Doyle, Rich Wrestling, Fall 1:33.
5th--T. Chilcote, Lake Villa Lancers, f, C. Brazzele, Lan-Oak, Fall 2:27.

177
1st--Brain Galto, Sycamore, f, Robert Tamillo, Addison, Fall 1:20.
3rd--Jacob Janek, Granite City Coolidge, f, Jon Jump, Moline, Fall 2:21.
5th--S. Descoto, Blackhawk, d, J. Jacobs, Rochelle, Dec 8-2.

189
1st--David Love, Harvey Twisters, f, Brett Henderson, Raiders, Fall 1:29.
3rd--D. Olivia, Carmel Corsair, f, R. Clemons, Pekin, Fall 1:27.
5th--P. Hartsfield, Fenwick, f, W. Gosnell, Pekin, Fall 3:59.

275
1st--Jose Monarrez, Maywood, f, Wayne Desmet, Moline, Fall 3:58.
3rd--James Bradshaw, Raiders, f, J. Rosiles, Joliet Boys Club, Fall 1:27.
5th--PJ Conway, Panther Wrestling Club, f, M. Svast, West Chicago, Fall 1:28.
"""


def _get_match_slot(index: int, placement: str) -> bracket_utils.MatchSlot:
    if index == 0:
        if placement != "1st":
            raise ValueError("Invalid placement", index, placement)
        return "championship_first_place"

    if index == 1:
        if placement != "3rd":
            raise ValueError("Invalid placement", index, placement)
        return "consolation_third_place"

    if index == 2:
        if placement != "5th":
            raise ValueError("Invalid placement", index, placement)
        return "consolation_fifth_place"

    raise NotImplementedError(index, placement)


def _to_competitor(name: str, team: str) -> bracket_utils.Competitor:
    parts = name.split()
    if len(parts) != 2:
        raise NotImplementedError(name)

    first_name, last_name = parts
    return bracket_utils.Competitor(
        full_name=name,
        first_name=first_name,
        last_name=last_name,
        team_full=team,
    )


def _determine_result_type(result_desc: str, result: str) -> bracket_utils.ResultType:
    if result_desc == "d":
        return "decision"

    if result_desc == "md":
        return "major"

    if result_desc == "tf":
        return "tech"

    if result_desc == "f":
        return "fall"

    if result_desc == "inj dflt":
        return "default"

    if result_desc == "dflt":
        return "default"

    raise NotImplementedError(result_desc, result)


def _parse_match_info(
    match_slot: bracket_utils.MatchSlot, match_info: str
) -> bracket_utils.Match:
    parts = match_info.rstrip(".").split(", ")

    if len(parts) == 6:
        top_name, top_team, result_desc, bottom_name, bottom_team, result = parts
        top_competitor = _to_competitor(top_name, top_team)
        bottom_competitor = _to_competitor(bottom_name, bottom_team)
        result_type = _determine_result_type(result_desc, result)
    elif len(parts) == 3:
        top_name, top_team, remaining = parts
        if remaining == "uncontested":
            result = "Bye"
            result_type = "bye"
        elif remaining == "disqualif":
            result = "Dq"
            result_type = "disqualification"
        elif remaining == "fft":
            result = "Forf"
            result_type = "forfeit"
        else:
            raise NotImplementedError(match_info)

        top_competitor = _to_competitor(top_name, top_team)
        bottom_competitor = None
    else:
        raise NotImplementedError(match_info)

    return bracket_utils.Match(
        match_slot=match_slot,
        top_competitor=top_competitor,
        bottom_competitor=bottom_competitor,
        result_type=result_type,
        result=result,
        bout_number=None,
        top_win=True,
    )


def _parse_weight(value: str) -> tuple[int, list[bracket_utils.Match]]:
    weight_str, remaining = value.split("\n", 1)
    weight = int(weight_str)

    matches: list[bracket_utils.Match] = []
    for i, row in enumerate(remaining.strip().split("\n")):
        placement, match_info = row.split("--")
        match_slot = _get_match_slot(i, placement)
        matches.append(_parse_match_info(match_slot, match_info))

    return weight, matches


def _parse_weight_classes(
    division: bracket_utils.Division, value: str
) -> list[bracket_utils.WeightClass]:
    seen: set[int] = set()
    result: list[bracket_utils.WeightClass] = []

    parts = value.strip().split("\n\n")
    for part in parts:
        weight, matches = _parse_weight(part)

        if weight in seen:
            raise KeyError("Weight duplicate", weight)
        seen.add(weight)

        result.append(
            bracket_utils.WeightClass(division=division, weight=weight, matches=matches)
        )

    return result


def main():
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}
    team_scores["junior_iwf"] = []
    for team_name, score in _JUNIOR_TEAM_SCORES.items():
        team_scores["junior_iwf"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    team_scores["novice_iwf"] = []
    for team_name, score in _NOVICE_TEAM_SCORES.items():
        team_scores["novice_iwf"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    team_scores["senior_iwf"] = []
    for team_name, score in _SENIOR_TEAM_SCORES.items():
        team_scores["senior_iwf"].append(
            bracket_utils.TeamScore(team=team_name, score=score)
        )

    weight_classes: list[bracket_utils.WeightClass] = []
    weight_classes.extend(_parse_weight_classes("junior_iwf", _JUNIOR_PLACERS_TEXT))
    weight_classes.extend(_parse_weight_classes("novice_iwf", _NOVICE_PLACERS_TEXT))
    weight_classes.extend(_parse_weight_classes("senior_iwf", _SENIOR_PLACERS_TEXT))

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    extracted.sort()
    with open(HERE / "extracted.1998-iwf.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
