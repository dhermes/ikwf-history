# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import NamedTuple

import bracket_utils
import bs4

HERE = pathlib.Path(__file__).resolve().parent
_NOVICE_TEAM_REPLACE: dict[str, str] = {
    "Crystal Lake Wiz.": "Crystal Lake Wizards",
    "Harlem Cou.": "Harlem Cougars",
    "Little Celtic WC": "Little Celtics",
    "Mattoon Youth": "Mattoon Youth WC",
    "Orland Park": "Orland Park Pioneers",
    "Sterling-Newman": "Sterling Newman",
    "Tinley Park": "Tinley Park Bulldogs",
    "Villa-Lombard": "Villa-Lombard Cougars",
}
_SENIOR_TEAM_REPLACE: dict[str, str] = {
    "Bradley Bour.": "Bradley-Bourbonnais WC",
    "Bradley-Bour.": "Bradley-Bourbonnais WC",
    "Crystal Lake": "Crystal Lake Wizards",
    "Little Celtic WC": "Little Celtics",
    "Little Celtics WC": "Little Celtics",
    "Morton Youth": "Morton Youth WC",
    "Orland Park": "Orland Park Pioneers",
    "Tinley Park": "Tinley Park Bulldogs",
    "Villa-Lombard": "Villa-Lombard Cougars",
}


def _extract_team_score(
    line: str, team_replace: dict[str, str]
) -> bracket_utils.TeamScore:
    line = line.replace("9. (tie) ", "9. ")
    if line.startswith("Springfield Capitals"):
        line = f"9. {line}"

    _, after_place = line.split(". ", 1)
    team_name, score = after_place.split(" - ")
    team_name = team_name.strip()
    team_name = team_replace.get(team_name, team_name)
    score = float(score)

    return bracket_utils.TeamScore(team=team_name, acronym=None, score=score)


def _parse_weight(element: bs4.Tag) -> int:
    as_text = element.text.strip()
    parts = as_text.split()
    if len(parts) != 2 or parts[1] != "lbs.":
        raise ValueError("Unexpected weight", as_text)

    return int(parts[0])


def _as_lines(element: bs4.Tag) -> list[str]:
    return [line.strip() for line in element.stripped_strings]


class Placer(NamedTuple):
    name: str
    team: str

    def to_competitor(self, team_replace: dict[str, str]) -> bracket_utils.Competitor:
        team_full = team_replace.get(self.team, self.team)
        parts = self.name.split()
        if len(parts) != 2:
            raise NotImplementedError(self.name)

        first_name = parts[0]
        last_name = parts[1]
        return bracket_utils.Competitor(
            full_name=self.name,
            first_name=first_name,
            last_name=last_name,
            team_full=team_full,
            team_acronym=None,
        )


def _parse_placers(
    element: bs4.Tag,
) -> list[Placer]:
    lines = _as_lines(element)
    if len(lines) != 12:
        raise ValueError("Unexpected element", len(lines), element)

    if lines[::2] != ["1st", "2nd", "3rd", "4th", "5th", "6th"]:
        raise ValueError("Unexpected element", lines[::2], element)

    placers: list[Placer] = []
    for i in range(6):
        line = lines[2 * i + 1]
        line = line.strip("-").strip()

        parts = line.split(" - ")
        if len(parts) != 2:
            raise ValueError("Unexpected placer", i, line)
        placers.append(Placer(name=parts[0], team=parts[1]))

    return placers


def _create_weight_class(
    division: bracket_utils.Division,
    weight_element: bs4.Tag,
    placers_element: bs4.Tag,
) -> bracket_utils.WeightClass:
    weight = _parse_weight(weight_element)
    placers = _parse_placers(placers_element)
    if len(placers) != 6:
        raise RuntimeError("Invalid placers", division, weight)

    if division == "novice":
        team_replace = _NOVICE_TEAM_REPLACE
    elif division == "senior":
        team_replace = _SENIOR_TEAM_REPLACE
    else:
        raise NotImplementedError(division)

    matches: list[bracket_utils.Match] = [
        bracket_utils.Match(
            match_slot="championship_first_place",
            top_competitor=placers[0].to_competitor(team_replace),
            bottom_competitor=placers[1].to_competitor(team_replace),
            result="",
            result_type="place",
            bout_number=None,
            top_win=True,
        ),
        bracket_utils.Match(
            match_slot="consolation_third_place",
            top_competitor=placers[2].to_competitor(team_replace),
            bottom_competitor=placers[3].to_competitor(team_replace),
            result="",
            result_type="place",
            bout_number=None,
            top_win=True,
        ),
        bracket_utils.Match(
            match_slot="consolation_fifth_place",
            top_competitor=placers[4].to_competitor(team_replace),
            bottom_competitor=placers[5].to_competitor(team_replace),
            result="",
            result_type="place",
            bout_number=None,
            top_win=True,
        ),
    ]

    return bracket_utils.WeightClass(division=division, weight=weight, matches=matches)


def _extract_novice(
    raw_dir: pathlib.Path,
) -> tuple[list[bracket_utils.WeightClass], list[bracket_utils.TeamScore]]:
    novice_path = (
        raw_dir / "novice" / "1999 IKWF Novice Division State Championships.html"
    )
    with open(novice_path, "rb") as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")

    # Team Scores
    all_p = soup.find_all("p")
    team_score_p = [
        element for element in all_p if "1. Little Celtic WC - 181" in element.text
    ]
    if len(team_score_p) != 1:
        raise RuntimeError("Invariant violation")

    team_scores: list[bracket_utils.TeamScore] = [
        _extract_team_score(line, _NOVICE_TEAM_REPLACE)
        for line in _as_lines(team_score_p[0])
    ]

    # Weights (left column): <td width="241">; <tr> alternate header + content
    left_tds = soup.find_all("td", attrs={"width": "241"})
    if len(left_tds) != 16:
        raise RuntimeError("Invariant violation", len(left_tds))

    # Weights (right column): <td width="243">; <tr> alternate header + content
    right_tds = soup.find_all("td", attrs={"width": "243"})
    if len(right_tds) != len(left_tds):
        raise RuntimeError("Invariant violation", len(right_tds))

    weight_classes: list[bracket_utils.WeightClass] = []
    for i in range(8):
        weight_class1 = _create_weight_class(
            "novice", left_tds[2 * i], left_tds[2 * i + 1]
        )
        weight_classes.append(weight_class1)
        weight_class2 = _create_weight_class(
            "novice", right_tds[2 * i], right_tds[2 * i + 1]
        )
        weight_classes.append(weight_class2)

    return weight_classes, team_scores


def _extract_senior(
    raw_dir: pathlib.Path,
) -> tuple[list[bracket_utils.WeightClass], list[bracket_utils.TeamScore]]:
    senior_path = (
        raw_dir / "senior" / "1999 IKWF Senior Division State Championships.html"
    )
    with open(senior_path, "rb") as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")

    # Team Scores
    all_p = soup.find_all("p")
    team_score_p = [
        element for element in all_p if "1. Fox Valley WC - 352.5" in element.text
    ]
    if len(team_score_p) != 1:
        raise RuntimeError("Invariant violation")

    team_scores: list[bracket_utils.TeamScore] = [
        _extract_team_score(line, _SENIOR_TEAM_REPLACE)
        for line in _as_lines(team_score_p[0])
    ]

    # Weights (left column): <td width="246">; <tr> alternate header + content
    left_tds = soup.find_all("td", attrs={"width": "246"})
    if len(left_tds) != 18:
        raise RuntimeError("Invariant violation", len(left_tds))

    # Weights (right column): <td width="250">; <tr> alternate header + content
    right_tds = soup.find_all("td", attrs={"width": "250"})
    if len(right_tds) != len(left_tds):
        raise RuntimeError("Invariant violation", len(right_tds))

    weight_classes: list[bracket_utils.WeightClass] = []
    for i in range(9):
        weight_class1 = _create_weight_class(
            "senior", left_tds[2 * i], left_tds[2 * i + 1]
        )
        weight_classes.append(weight_class1)
        weight_class2 = _create_weight_class(
            "senior", right_tds[2 * i], right_tds[2 * i + 1]
        )
        weight_classes.append(weight_class2)

    return weight_classes, team_scores


def main():
    raw_dir = HERE.parent / "raw-data" / "1999"

    weight_classes: list[bracket_utils.WeightClass] = []
    team_scores: dict[bracket_utils.Division, list[bracket_utils.TeamScore]] = {}

    division_weight_classes, division_team_scores = _extract_novice(raw_dir)
    weight_classes.extend(division_weight_classes)
    team_scores["novice"] = division_team_scores

    division_weight_classes, division_team_scores = _extract_senior(raw_dir)
    weight_classes.extend(division_weight_classes)
    team_scores["senior"] = division_team_scores

    extracted = bracket_utils.ExtractedTournament(
        weight_classes=weight_classes, team_scores=team_scores, deductions=[]
    )
    with open(HERE / "extracted.1999.json", "w") as file_obj:
        file_obj.write(extracted.model_dump_json(indent=2))
        file_obj.write("\n")


if __name__ == "__main__":
    main()
