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
    cleaned = value.strip().rstrip("+").rstrip("-")
    name, team = cleaned.rsplit("-", 1)

    team = team.strip()

    if name == "" and team == "Bye":
        return None

    if len(team) not in (1, 2, 3):
        raise ValueError("Invariant violation", team, value)

    if name == "":
        raise ValueError("Invariant violation", name, cleaned, value)

    return {"name": name, "team": team}


def parse_bout_result(value):
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].strip().rsplit(None, 1)
    if len(parts) == 1:
        int(parts[0])  # Ensure the only part is a valid bout number
        return ""

    return parts[0].strip()


def parse_bout_number(value):
    if not value.endswith("|"):
        raise ValueError("Invariant violation", value)

    parts = value[:-1].strip().rsplit(None, 1)
    if len(parts) == 1:
        return int(parts[0])

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
    top_competitor_str = championship_lines[start_index][:26]
    if top_competitor_str != "                          ":
        top_competitor = parse_competitor(top_competitor_str)

    bottom_competitor = None
    bottom_competitor_str = championship_lines[start_index + 2][:26]
    if bottom_competitor_str != "                          ":
        bottom_competitor = parse_competitor(bottom_competitor_str)

    result_bout_number_str = championship_lines[start_index + 1][:26]
    result = ""
    bout_number = None
    if result_bout_number_str != "                          ":
        result = parse_bout_result(result_bout_number_str)
        bout_number = parse_bout_number(result_bout_number_str)

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
    with open(HERE / "2001" / divison / filename) as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_pre = soup.find_all("pre")
    if len(all_pre) != 4:
        raise RuntimeError("Invariant violation")

    championship_pre, consolation_pre, fifth_place_pre, seventh_place_pre = all_pre
    championship_lines = championship_pre.text.lstrip("\n").split("\n")
    consolation_lines = consolation_pre.text.lstrip("\n").split("\n")
    fifth_place_lines = fifth_place_pre.text.lstrip("\n").split("\n")
    seventh_place_lines = seventh_place_pre.text.lstrip("\n").split("\n")

    if divison == "senior" and weight == 84:
        consolation_round3_01_top_competitor = {"name": "KEITH WILLIAMS", "team": "JUN"}
    else:
        consolation_round3_01_top_competitor = parse_competitor(
            consolation_lines[4][:26]
        )

    matches = [
        {
            "match": "championship_r32_01",
            "top_competitor": parse_competitor(championship_lines[0][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            2,
            "championship_r32_02",
            "championship_r16_01",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            6,
            "championship_r32_03",
            "championship_r16_02",
            "top_competitor",
        ),
        {
            "match": "championship_r32_04",
            "top_competitor": parse_competitor(championship_lines[10][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        {
            "match": "championship_r32_05",
            "top_competitor": parse_competitor(championship_lines[12][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            14,
            "championship_r32_06",
            "championship_r16_03",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            18,
            "championship_r32_07",
            "championship_r16_04",
            "top_competitor",
        ),
        {
            "match": "championship_r32_08",
            "top_competitor": parse_competitor(championship_lines[22][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        {
            "match": "championship_r32_09",
            "top_competitor": parse_competitor(championship_lines[24][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            26,
            "championship_r32_10",
            "championship_r16_05",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            30,
            "championship_r32_11",
            "championship_r16_06",
            "top_competitor",
        ),
        {
            "match": "championship_r32_12",
            "top_competitor": parse_competitor(championship_lines[34][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        {
            "match": "championship_r32_13",
            "top_competitor": parse_competitor(championship_lines[36][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        maybe_r32_empty_bye(
            championship_lines,
            38,
            "championship_r32_14",
            "championship_r16_07",
            "bottom_competitor",
        ),
        maybe_r32_empty_bye(
            championship_lines,
            42,
            "championship_r32_15",
            "championship_r16_08",
            "top_competitor",
        ),
        {
            "match": "championship_r32_16",
            "top_competitor": parse_competitor(championship_lines[46][26:52]),
            "bottom_competitor": None,
            "result": "Bye",
            "bout_number": None,
        },
        ########################################################################
        {
            "match": "championship_r16_01",
            "top_competitor": parse_competitor(championship_lines[0][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[3][26:52]),
            "result": parse_bout_result(championship_lines[1][26:52]),
            "bout_number": parse_bout_number(championship_lines[1][26:52]),
            "winner": ("championship_quarter_01", "top_competitor"),
        },
        {
            "match": "championship_r16_02",
            "top_competitor": parse_competitor(championship_lines[7][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[10][26:52]),
            "result": parse_bout_result(championship_lines[9][26:52]),
            "bout_number": parse_bout_number(championship_lines[9][26:52]),
            "winner": ("championship_quarter_01", "bottom_competitor"),
        },
        {
            "match": "championship_r16_03",
            "top_competitor": parse_competitor(championship_lines[12][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[15][26:52]),
            "result": parse_bout_result(championship_lines[13][26:52]),
            "bout_number": parse_bout_number(championship_lines[13][26:52]),
            "winner": ("championship_quarter_02", "top_competitor"),
        },
        {
            "match": "championship_r16_04",
            "top_competitor": parse_competitor(championship_lines[19][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[22][26:52]),
            "result": parse_bout_result(championship_lines[21][26:52]),
            "bout_number": parse_bout_number(championship_lines[21][26:52]),
            "winner": ("championship_quarter_02", "bottom_competitor"),
        },
        {
            "match": "championship_r16_05",
            "top_competitor": parse_competitor(championship_lines[24][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[27][26:52]),
            "result": parse_bout_result(championship_lines[25][26:52]),
            "bout_number": parse_bout_number(championship_lines[25][26:52]),
            "winner": ("championship_quarter_03", "top_competitor"),
        },
        {
            "match": "championship_r16_06",
            "top_competitor": parse_competitor(championship_lines[31][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[34][26:52]),
            "result": parse_bout_result(championship_lines[33][26:52]),
            "bout_number": parse_bout_number(championship_lines[33][26:52]),
            "winner": ("championship_quarter_03", "bottom_competitor"),
        },
        {
            "match": "championship_r16_07",
            "top_competitor": parse_competitor(championship_lines[36][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[39][26:52]),
            "result": parse_bout_result(championship_lines[37][26:52]),
            "bout_number": parse_bout_number(championship_lines[37][26:52]),
            "winner": ("championship_quarter_04", "top_competitor"),
        },
        {
            "match": "championship_r16_08",
            "top_competitor": parse_competitor(championship_lines[43][26:52]),
            "bottom_competitor": parse_competitor(championship_lines[46][26:52]),
            "result": parse_bout_result(championship_lines[45][26:52]),
            "bout_number": parse_bout_number(championship_lines[45][26:52]),
            "winner": ("championship_quarter_04", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "championship_quarter_01",
            "top_competitor": parse_competitor(championship_lines[1][52:70]),
            "bottom_competitor": parse_competitor(championship_lines[9][52:70]),
            "result": parse_bout_result(championship_lines[5][52:70]),
            "bout_number": parse_bout_number(championship_lines[5][52:70]),
            "winner": ("championship_semi_01", "top_competitor"),
        },
        {
            "match": "championship_quarter_02",
            "top_competitor": parse_competitor(championship_lines[13][52:70]),
            "bottom_competitor": parse_competitor(championship_lines[21][52:70]),
            "result": parse_bout_result(championship_lines[17][52:70]),
            "bout_number": parse_bout_number(championship_lines[17][52:70]),
            "winner": ("championship_semi_01", "bottom_competitor"),
        },
        {
            "match": "championship_quarter_03",
            "top_competitor": parse_competitor(championship_lines[25][52:70]),
            "bottom_competitor": parse_competitor(championship_lines[33][52:70]),
            "result": parse_bout_result(championship_lines[29][52:70]),
            "bout_number": parse_bout_number(championship_lines[29][52:70]),
            "winner": ("championship_semi_02", "top_competitor"),
        },
        {
            "match": "championship_quarter_04",
            "top_competitor": parse_competitor(championship_lines[37][52:70]),
            "bottom_competitor": parse_competitor(championship_lines[45][52:70]),
            "result": parse_bout_result(championship_lines[41][52:70]),
            "bout_number": parse_bout_number(championship_lines[41][52:70]),
            "winner": ("championship_semi_02", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "championship_semi_01",
            "top_competitor": parse_competitor(championship_lines[5][70:88]),
            "bottom_competitor": parse_competitor(championship_lines[17][70:88]),
            "result": parse_bout_result(championship_lines[11][70:88]),
            "bout_number": parse_bout_number(championship_lines[11][70:88]),
            "winner": ("championship_first_place", "top_competitor"),
        },
        {
            "match": "championship_semi_02",
            "top_competitor": parse_competitor(championship_lines[29][70:88]),
            "bottom_competitor": parse_competitor(championship_lines[41][70:88]),
            "result": parse_bout_result(championship_lines[35][70:88]),
            "bout_number": parse_bout_number(championship_lines[35][70:88]),
            "winner": ("championship_first_place", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "championship_first_place",
            "top_competitor": parse_competitor(championship_lines[11][88:106]),
            "bottom_competitor": parse_competitor(championship_lines[35][88:106]),
            "result": parse_bout_result(championship_lines[23][88:106]),
            "bout_number": parse_bout_number(championship_lines[23][88:106]),
            "winner": parse_competitor(championship_lines[23][106:]),
        },
        ########################################################################
        # **********************************************************************
        ########################################################################
        {
            "match": "consolation_round3_01",
            "top_competitor": consolation_round3_01_top_competitor,
            "bottom_competitor": parse_competitor(consolation_lines[6][:26]),
            "result": parse_bout_result(consolation_lines[5][:26]),
            "bout_number": parse_bout_number(consolation_lines[5][:26]),
            "winner": ("consolation_round4_blood_01", "bottom_competitor"),
        },
        {
            "match": "consolation_round3_02",
            "top_competitor": parse_competitor(consolation_lines[8][:26]),
            "bottom_competitor": parse_competitor(consolation_lines[10][:26]),
            "result": parse_bout_result(consolation_lines[9][:26]),
            "bout_number": parse_bout_number(consolation_lines[9][:26]),
            "winner": ("consolation_round4_blood_02", "top_competitor"),
        },
        {
            "match": "consolation_round3_03",
            "top_competitor": parse_competitor(consolation_lines[18][:26]),
            "bottom_competitor": parse_competitor(consolation_lines[20][:26]),
            "result": parse_bout_result(consolation_lines[19][:26]),
            "bout_number": parse_bout_number(consolation_lines[19][:26]),
            "winner": ("consolation_round4_blood_03", "bottom_competitor"),
        },
        {
            "match": "consolation_round3_04",
            "top_competitor": parse_competitor(consolation_lines[22][:26]),
            "bottom_competitor": parse_competitor(consolation_lines[24][:26]),
            "result": parse_bout_result(consolation_lines[23][:26]),
            "bout_number": parse_bout_number(consolation_lines[23][:26]),
            "winner": ("consolation_round4_blood_04", "top_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_round4_blood_01",
            "top_competitor": parse_competitor(consolation_lines[1][26:52]),
            "bottom_competitor": parse_competitor(consolation_lines[5][26:52]),
            "result": parse_bout_result(consolation_lines[3][26:52]),
            "bout_number": parse_bout_number(consolation_lines[3][26:52]),
            "winner": ("consolation_round5_01", "top_competitor"),
        },
        {
            "match": "consolation_round4_blood_02",
            "top_competitor": parse_competitor(consolation_lines[9][26:52]),
            "bottom_competitor": parse_competitor(consolation_lines[13][26:52]),
            "result": parse_bout_result(consolation_lines[11][26:52]),
            "bout_number": parse_bout_number(consolation_lines[11][26:52]),
            "winner": ("consolation_round5_01", "bottom_competitor"),
        },
        {
            "match": "consolation_round4_blood_03",
            "top_competitor": parse_competitor(consolation_lines[15][26:52]),
            "bottom_competitor": parse_competitor(consolation_lines[19][26:52]),
            "result": parse_bout_result(consolation_lines[17][26:52]),
            "bout_number": parse_bout_number(consolation_lines[17][26:52]),
            "winner": ("consolation_round5_02", "top_competitor"),
        },
        {
            "match": "consolation_round4_blood_04",
            "top_competitor": parse_competitor(consolation_lines[23][26:52]),
            "bottom_competitor": parse_competitor(consolation_lines[27][26:52]),
            "result": parse_bout_result(consolation_lines[25][26:52]),
            "bout_number": parse_bout_number(consolation_lines[25][26:52]),
            "winner": ("consolation_round5_02", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_round5_01",
            "top_competitor": parse_competitor(consolation_lines[3][52:70]),
            "bottom_competitor": parse_competitor(consolation_lines[11][52:70]),
            "result": parse_bout_result(consolation_lines[7][52:70]),
            "bout_number": parse_bout_number(consolation_lines[7][52:70]),
            "winner": ("consolation_round6_semi_01", "bottom_competitor"),
        },
        {
            "match": "consolation_round5_02",
            "top_competitor": parse_competitor(consolation_lines[17][52:70]),
            "bottom_competitor": parse_competitor(consolation_lines[25][52:70]),
            "result": parse_bout_result(consolation_lines[21][52:70]),
            "bout_number": parse_bout_number(consolation_lines[21][52:70]),
            "winner": ("consolation_round6_semi_02", "top_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_round6_semi_01",
            "top_competitor": parse_competitor(consolation_lines[0][70:88]),
            "bottom_competitor": parse_competitor(consolation_lines[7][70:88]),
            "result": parse_bout_result(consolation_lines[2][70:88]),
            "bout_number": parse_bout_number(consolation_lines[2][70:88]),
            "winner": ("consolation_third_place", "top_competitor"),
        },
        {
            "match": "consolation_round6_semi_02",
            "top_competitor": parse_competitor(consolation_lines[21][70:88]),
            "bottom_competitor": parse_competitor(consolation_lines[28][70:88]),
            "result": parse_bout_result(consolation_lines[26][70:88]),
            "bout_number": parse_bout_number(consolation_lines[26][70:88]),
            "winner": ("consolation_third_place", "bottom_competitor"),
        },
        ########################################################################
        {
            "match": "consolation_third_place",
            "top_competitor": parse_competitor(consolation_lines[2][88:106]),
            "bottom_competitor": parse_competitor(consolation_lines[26][88:106]),
            "result": parse_bout_result(consolation_lines[14][88:106]),
            "bout_number": parse_bout_number(consolation_lines[14][88:106]),
            "winner": parse_competitor(consolation_lines[14][106:]),
        },
        ########################################################################
        # **********************************************************************
        ########################################################################
        {
            "match": "consolation_fifth_place",
            "top_competitor": parse_competitor(fifth_place_lines[0][52:70]),
            "bottom_competitor": parse_competitor(fifth_place_lines[2][52:70]),
            "result": parse_bout_result(fifth_place_lines[1][52:70]),
            "bout_number": parse_bout_number(fifth_place_lines[1][52:70]),
            "winner": parse_competitor(fifth_place_lines[1][70:]),
        },
        ########################################################################
        # **********************************************************************
        ########################################################################
        {
            "match": "consolation_seventh_place",
            "top_competitor": parse_competitor(seventh_place_lines[0][:26]),
            "bottom_competitor": parse_competitor(seventh_place_lines[2][:26]),
            "result": parse_bout_result(seventh_place_lines[1][:26]),
            "bout_number": parse_bout_number(seventh_place_lines[1][:26]),
            "winner": parse_competitor(seventh_place_lines[1][26:]),
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

    with open(HERE / "parsed.2001.json", "w") as file_obj:
        json.dump(parsed, file_obj, indent=2)
        file_obj.write("\n")


if __name__ == "__main__":
    main()
