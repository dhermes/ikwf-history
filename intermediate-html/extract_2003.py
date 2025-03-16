# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import json
import pathlib

import bs4

HERE = pathlib.Path(__file__).resolve().parent


def print_lines(search_lines):
    max_index = len(search_lines) - 1
    index_width = len(str(max_index))

    for i, line in enumerate(search_lines):
        index_str = str(i).rjust(index_width)
        print(f"{index_str}*** {line}")


def find_all_indices(search_lines, value):
    result = []
    for i, line in enumerate(search_lines):
        matches = line.count(value)
        if matches > 1:
            raise NotImplementedError(i, matches, line, value)
        if matches == 0:
            continue

        start_index = line.index(value)
        end_index = start_index + len(value)
        result.append((i, start_index, end_index))

    return result


def parse_competitor(value):
    cleaned = value.strip().rstrip("+").strip("-")
    if cleaned == "Bye":
        return None

    name, team = cleaned.rsplit(" ", 1)
    team = team.strip()

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return {"name": name, "team": team}


def parse_bout_result(value):
    if value.endswith("|"):
        value = value[:-1]

    if not value.endswith(" ") or not value.startswith(" "):
        raise ValueError("Invariant violation", value)

    parts = value.split("Bout:")
    if len(parts) > 2:
        raise ValueError("Invariant violation", value)

    return parts[0].strip()


def parse_bout_number(value):
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].split("Bout:")
    if len(parts) != 2:
        raise ValueError("Invariant violation", value)

    return int(parts[1])


def set_winner(match, by_match):
    winner = match.get("winner", None)
    if isinstance(winner, dict):
        return

    if match["result"] == "Bye":
        if match["bottom_competitor"] is not None:
            raise ValueError("Invariant violation", match)
        match["winner"] = match["top_competitor"]
        return

    if isinstance(winner, tuple):
        match_key, competitor_key = winner
        competitor = by_match[match_key][competitor_key]
        match["winner"] = competitor
        return

    raise NotImplementedError(winner)


def set_result(match):
    result = match["result"]
    if result != "":
        return

    top_competitor = match["top_competitor"]
    bottom_competitor = match["bottom_competitor"]
    if top_competitor is None or bottom_competitor is None:
        match["result"] = "Bye"
        return

    raise NotImplementedError(match)


def set_top_competitor(match):
    top_competitor = match["top_competitor"]
    bottom_competitor = match["bottom_competitor"]
    if top_competitor is not None or bottom_competitor is not None:
        return

    result = match["result"]
    if result != "Bye":
        raise ValueError("Invariant violation", match)

    winner = match["winner"]
    if winner is None:
        return

    if not isinstance(winner, dict):
        raise ValueError("Invariant violation", match)

    match["top_competitor"] = winner


def maybe_r32_empty_bye(
    championship_lines, start_index, match, winner_round, winner_key
):
    top_competitor = None
    top_competitor_str = championship_lines[start_index][:31]
    if top_competitor_str != "                          ":
        top_competitor = parse_competitor(top_competitor_str)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:31]
    if bottom_competitor_str != "                          ":
        bottom_competitor = parse_competitor(bottom_competitor_str)

    bout_number_str = championship_lines[start_index + 1][:31]
    bout_number = None
    if bout_number_str != "                               ":
        bout_number = parse_bout_number(bout_number_str)

    result_str = championship_lines[start_index + 2][31:62]
    result = ""
    if result_str != "                               ":
        result = parse_bout_result(result_str)

    return {
        "match": match,
        "top_competitor": top_competitor,
        "bottom_competitor": bottom_competitor,
        "result": result,
        "bout_number": bout_number,
        "winner": (winner_round, winner_key),
    }


def extract_bracket(weight, divison):
    filename = f"{weight}.html"
    with open(HERE / "2003" / divison / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre = soup.find_all("pre")
    if len(all_pre) != 4:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre, seventh_place_pre = all_pre
    championship_text = championship_pre.text

    championship_lines = championship_text.lstrip("\n").split("\n")
    consolation_lines = consolation_pre.text.lstrip("\n").split("\n")
    fifth_place_lines = fifth_place_pre.text.lstrip("\n").split("\n")
    seventh_place_lines = seventh_place_pre.text.lstrip("\n").split("\n")

    matches = [
        {
            "match": "championship_r32_01",
            "top_competitor": parse_competitor(championship_lines[0][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            1,
            "championship_r32_02",
            "championship_r16_01",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            5,
            "championship_r32_03",
            "championship_r16_02",
            "top_competitor",
        ),
        {
            "match": "championship_r32_04",
            "top_competitor": parse_competitor(championship_lines[8][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        {
            "match": "championship_r32_05",
            "top_competitor": parse_competitor(championship_lines[10][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            11,
            "championship_r32_06",
            "championship_r16_03",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            15,
            "championship_r32_07",
            "championship_r16_04",
            "top_competitor",
        ),
        {
            "match": "championship_r32_08",
            "top_competitor": parse_competitor(championship_lines[18][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        {
            "match": "championship_r32_09",
            "top_competitor": parse_competitor(championship_lines[20][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            21,
            "championship_r32_10",
            "championship_r16_05",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            25,
            "championship_r32_11",
            "championship_r16_06",
            "top_competitor",
        ),
        {
            "match": "championship_r32_12",
            "top_competitor": parse_competitor(championship_lines[28][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        {
            "match": "championship_r32_13",
            "top_competitor": parse_competitor(championship_lines[30][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            31,
            "championship_r32_14",
            "championship_r16_07",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            35,
            "championship_r32_15",
            "championship_r16_08",
            "top_competitor",
        ),
        {
            "match": "championship_r32_16",
            "top_competitor": parse_competitor(championship_lines[38][31:62]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        ########################################################################
        {
            "match": "championship_r16_01",
            "top_competitor": parse_competitor(championship_lines[0][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[2][31:62]),
            "result": parse_bout_result(championship_lines[2][62:93]),
            "bout_number": parse_bout_number(championship_lines[1][31:62]),
            "winner": ("championship_quarter_01", "top_competitor"),
        },
        {
            "match": "championship_r16_02",
            "top_competitor": parse_competitor(championship_lines[6][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[8][31:62]),
            "result": parse_bout_result(championship_lines[8][62:93]),
            "bout_number": parse_bout_number(championship_lines[7][31:62]),
            "winner": ("championship_quarter_01", "bottom_competitor"),
        },
        {
            "match": "championship_r16_03",
            "top_competitor": parse_competitor(championship_lines[10][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[12][31:62]),
            "result": parse_bout_result(championship_lines[12][62:93]),
            "bout_number": parse_bout_number(championship_lines[11][31:62]),
            "winner": ("championship_quarter_02", "top_competitor"),
        },
        {
            "match": "championship_r16_04",
            "top_competitor": parse_competitor(championship_lines[16][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[18][31:62]),
            "result": parse_bout_result(championship_lines[18][62:93]),
            "bout_number": parse_bout_number(championship_lines[17][31:62]),
            "winner": ("championship_quarter_02", "bottom_competitor"),
        },
        {
            "match": "championship_r16_05",
            "top_competitor": parse_competitor(championship_lines[20][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[22][31:62]),
            "result": parse_bout_result(championship_lines[22][62:93]),
            "bout_number": parse_bout_number(championship_lines[21][31:62]),
            "winner": ("championship_quarter_03", "top_competitor"),
        },
        {
            "match": "championship_r16_06",
            "top_competitor": parse_competitor(championship_lines[26][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[28][31:62]),
            "result": parse_bout_result(championship_lines[28][62:93]),
            "bout_number": parse_bout_number(championship_lines[27][31:62]),
            "winner": ("championship_quarter_03", "bottom_competitor"),
        },
        {
            "match": "championship_r16_07",
            "top_competitor": parse_competitor(championship_lines[30][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[32][31:62]),
            "result": parse_bout_result(championship_lines[32][62:93]),
            "bout_number": parse_bout_number(championship_lines[31][31:62]),
            "winner": ("championship_quarter_04", "top_competitor"),
        },
        {
            "match": "championship_r16_08",
            "top_competitor": parse_competitor(championship_lines[36][31:62]),
            "bottom_competitor": parse_competitor(championship_lines[38][31:62]),
            "result": parse_bout_result(championship_lines[38][62:93] + " "),
            "bout_number": parse_bout_number(championship_lines[37][31:62]),
            "winner": ("championship_quarter_04", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "championship_quarter_01",
            "top_competitor": parse_competitor(championship_lines[1][62:93]),
            "bottom_competitor": parse_competitor(championship_lines[7][62:93]),
            "result": parse_bout_result(championship_lines[5][93:124]),
            "bout_number": parse_bout_number(championship_lines[4][62:93]),
            "winner": ("championship_semi_01", "top_competitor"),
        },
        {
            "match": "championship_quarter_02",
            "top_competitor": parse_competitor(championship_lines[11][62:93]),
            "bottom_competitor": parse_competitor(championship_lines[17][62:93]),
            "result": parse_bout_result(championship_lines[15][93:124]),
            "bout_number": parse_bout_number(championship_lines[14][62:93]),
            "winner": ("championship_semi_01", "bottom_competitor"),
        },
        {
            "match": "championship_quarter_03",
            "top_competitor": parse_competitor(championship_lines[21][62:93]),
            "bottom_competitor": parse_competitor(championship_lines[27][62:93]),
            "result": parse_bout_result(championship_lines[25][93:124]),
            "bout_number": parse_bout_number(championship_lines[24][62:93]),
            "winner": ("championship_semi_02", "top_competitor"),
        },
        {
            "match": "championship_quarter_04",
            "top_competitor": parse_competitor(championship_lines[31][62:93]),
            "bottom_competitor": parse_competitor(championship_lines[37][62:93]),
            "result": parse_bout_result(championship_lines[35][93:124] + " "),
            "bout_number": parse_bout_number(championship_lines[34][62:93]),
            "winner": ("championship_semi_02", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "championship_semi_01",
            "top_competitor": parse_competitor(championship_lines[4][93:124]),
            "bottom_competitor": parse_competitor(championship_lines[14][93:124]),
            "result": parse_bout_result(championship_lines[10][124:155]),
            "bout_number": parse_bout_number(championship_lines[9][93:124]),
            "winner": ("championship_first_place", "top_competitor"),
        },
        {
            "match": "championship_semi_02",
            "top_competitor": parse_competitor(championship_lines[24][93:124]),
            "bottom_competitor": parse_competitor(championship_lines[34][93:124]),
            "result": parse_bout_result(championship_lines[30][124:155] + " "),
            "bout_number": parse_bout_number(championship_lines[29][93:124]),
            "winner": ("championship_first_place", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "championship_first_place",
            "top_competitor": parse_competitor(championship_lines[9][124:155]),
            "bottom_competitor": parse_competitor(championship_lines[29][124:155]),
            "result": parse_bout_result(championship_lines[21][155:] + " "),
            "bout_number": parse_bout_number(championship_lines[19][124:155]),
            "winner": parse_competitor(championship_lines[19][155:]),
        },
        ########################################################################
        # **********************************************************************
        ########################################################################
        {
            "match": "consolation_round3_01",
            "top_competitor": parse_competitor(consolation_lines[0][:31]),
            "bottom_competitor": parse_competitor(consolation_lines[2][:31]),
            "result": parse_bout_result(consolation_lines[2][31:62]),
            "bout_number": parse_bout_number(consolation_lines[1][:31]),
            "winner": ("consolation_round4_blood_01", "top_competitor"),
        },
        {
            "match": "consolation_round3_02",
            "top_competitor": parse_competitor(consolation_lines[4][:31]),
            "bottom_competitor": parse_competitor(consolation_lines[6][:31]),
            "result": parse_bout_result(consolation_lines[6][31:62]),
            "bout_number": parse_bout_number(consolation_lines[5][:31]),
            "winner": ("consolation_round4_blood_02", "top_competitor"),
        },
        {
            "match": "consolation_round3_03",
            "top_competitor": parse_competitor(consolation_lines[8][:31]),
            "bottom_competitor": parse_competitor(consolation_lines[10][:31]),
            "result": parse_bout_result(consolation_lines[10][31:62]),
            "bout_number": parse_bout_number(consolation_lines[9][:31]),
            "winner": ("consolation_round4_blood_03", "top_competitor"),
        },
        {
            "match": "consolation_round3_04",
            "top_competitor": parse_competitor(consolation_lines[12][:31]),
            "bottom_competitor": parse_competitor(consolation_lines[14][:31]),
            "result": parse_bout_result(consolation_lines[14][31:62]),
            "bout_number": parse_bout_number(consolation_lines[13][:31]),
            "winner": ("consolation_round4_blood_04", "top_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_round4_blood_01",
            "top_competitor": parse_competitor(consolation_lines[1][31:62]),
            "bottom_competitor": parse_competitor(consolation_lines[3][31:62]),
            "result": parse_bout_result(consolation_lines[3][62:93]),
            "bout_number": parse_bout_number(consolation_lines[2][31:62]),
            "winner": ("consolation_round5_01", "top_competitor"),
        },
        {
            "match": "consolation_round4_blood_02",
            "top_competitor": parse_competitor(consolation_lines[5][31:62]),
            "bottom_competitor": parse_competitor(consolation_lines[7][31:62]),
            "result": parse_bout_result(consolation_lines[7][62:93]),
            "bout_number": parse_bout_number(consolation_lines[6][31:62]),
            "winner": ("consolation_round5_01", "bottom_competitor"),
        },
        {
            "match": "consolation_round4_blood_03",
            "top_competitor": parse_competitor(consolation_lines[9][31:62]),
            "bottom_competitor": parse_competitor(consolation_lines[11][31:62]),
            "result": parse_bout_result(consolation_lines[11][62:93]),
            "bout_number": parse_bout_number(consolation_lines[10][31:62]),
            "winner": ("consolation_round5_02", "top_competitor"),
        },
        {
            "match": "consolation_round4_blood_04",
            "top_competitor": parse_competitor(consolation_lines[13][31:62]),
            "bottom_competitor": parse_competitor(consolation_lines[15][31:62]),
            "result": parse_bout_result(consolation_lines[15][62:93] + " "),
            "bout_number": parse_bout_number(consolation_lines[14][31:62]),
            "winner": ("consolation_round5_02", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_round5_01",
            "top_competitor": parse_competitor(consolation_lines[2][62:93]),
            "bottom_competitor": parse_competitor(consolation_lines[6][62:93]),
            "result": parse_bout_result(consolation_lines[5][93:124]),
            "bout_number": parse_bout_number(consolation_lines[4][62:93]),
            "winner": ("consolation_round6_semi_01", "bottom_competitor"),
        },
        {
            "match": "consolation_round5_02",
            "top_competitor": parse_competitor(consolation_lines[10][62:93]),
            "bottom_competitor": parse_competitor(consolation_lines[14][62:93]),
            "result": parse_bout_result(consolation_lines[13][93:124] + " "),
            "bout_number": parse_bout_number(consolation_lines[12][62:93]),
            "winner": ("consolation_round6_semi_02", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_round6_semi_01",
            "top_competitor": parse_competitor(consolation_lines[0][93:124]),
            "bottom_competitor": parse_competitor(consolation_lines[4][93:124]),
            "result": parse_bout_result(consolation_lines[3][124:155]),
            "bout_number": parse_bout_number(consolation_lines[2][93:124]),
            "winner": ("consolation_third_place", "top_competitor"),
        },
        {
            "match": "consolation_round6_semi_02",
            "top_competitor": parse_competitor(consolation_lines[8][93:124]),
            "bottom_competitor": parse_competitor(consolation_lines[12][93:124]),
            "result": parse_bout_result(consolation_lines[11][124:155] + " "),
            "bout_number": parse_bout_number(consolation_lines[10][93:124]),
            "winner": ("consolation_third_place", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_third_place",
            "top_competitor": parse_competitor(consolation_lines[2][124:155]),
            "bottom_competitor": parse_competitor(consolation_lines[10][124:155]),
            "result": parse_bout_result(consolation_lines[8][155:] + " "),
            "bout_number": parse_bout_number(consolation_lines[6][124:155]),
            "winner": parse_competitor(consolation_lines[6][155:]),
        },
        ########################################################################
        # **********************************************************************
        ########################################################################
        {
            "match": "consolation_fifth_place",
            "top_competitor": parse_competitor(fifth_place_lines[0][:31]),
            "bottom_competitor": parse_competitor(fifth_place_lines[2][:31]),
            "result": parse_bout_result(fifth_place_lines[3][31:] + " "),
            "bout_number": parse_bout_number(fifth_place_lines[1][:31]),
            "winner": parse_competitor(fifth_place_lines[1][31:]),
        },
        ########################################################################
        # **********************************************************************
        ########################################################################
        {
            "match": "consolation_seventh_place",
            "top_competitor": parse_competitor(seventh_place_lines[0][31:62]),
            "bottom_competitor": parse_competitor(seventh_place_lines[2][31:62]),
            "result": parse_bout_result(seventh_place_lines[3][62:] + " "),
            "bout_number": parse_bout_number(seventh_place_lines[1][31:62]),
            "winner": parse_competitor(seventh_place_lines[1][62:]),
        },
    ]

    by_match = {match["match"]: match for match in matches}
    if len(by_match) != len(matches):
        raise ValueError("Invariant violation")

    for match in matches:
        set_winner(match, by_match)
        set_result(match)
        # NOTE: This **MUST** happen after `set_winner()` and `set_result()`
        set_top_competitor(match)

    return matches


def main():
    novice_weights = (
        62,
        66,
        70,
        74,
        79,
        84,
        89,
        95,
        101,
        108,
        115,
        122,
        130,
        147,
        166,
        215,
    )
    senior_weights = (
        70,
        74,
        79,
        84,
        89,
        95,
        101,
        108,
        115,
        122,
        130,
        138,
        147,
        156,
        166,
        177,
        189,
        215,
        275,
    )

    parsed = []
    division = "novice"
    for weight in novice_weights:
        matches = extract_bracket(weight, division)
        parsed.append(
            {
                "division": division,
                "weight": weight,
                "matches": matches,
            }
        )

    division = "senior"
    for weight in senior_weights:
        matches = extract_bracket(weight, division)
        parsed.append(
            {
                "division": division,
                "weight": weight,
                "matches": matches,
            }
        )

    with open(HERE / "extracted.2003.json", "w") as file_obj:
        json.dump(parsed, file_obj, indent=2)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
