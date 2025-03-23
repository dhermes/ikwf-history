# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

from typing import Literal

import pydantic


class Competitor(pydantic.BaseModel):
    first_name: str
    last_name: str
    suffix: str | None
    team: str


ResultType = Literal[
    "BYE",
    "DECISION",
    "DEFAULT",
    "DISQUALIFICATION",
    "FALL",
    "FORFEIT",
    "MAJOR",
    "TECH",
    "WALKOVER",
]


class Match(pydantic.BaseModel):
    match: str
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    result_type: ResultType
    bout_number: int | None
    top_win: bool | None


class WeightClass(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    matches: list[Match]


class WeightClasses(pydantic.RootModel[list[WeightClass]]):
    pass


class CompetitorWithWeight(pydantic.BaseModel):
    division: Literal["senior", "novice"]
    weight: int
    competitor: Competitor


def _get_advancement_points(match: str, winner: bool) -> float:
    if match == "championship_first_place":
        return 16.0 if winner else 12.0

    if match == "consolation_third_place":
        return 9.0 if winner else 7.0

    if match == "consolation_fifth_place":
        return 5.0 if winner else 3.0

    if match == "consolation_seventh_place":
        return 2.0 if winner else 1.0

    if match.startswith("consolation_"):
        return 1.0 if winner else 0.0

    if match.startswith("championship_"):
        return 2.0 if winner else 0.0

    raise NotImplementedError(match, winner)


def _get_result_points(result_type: ResultType) -> float:
    if result_type == "BYE":
        return 0.0

    if result_type == "DECISION":
        return 0.0

    if result_type == "DEFAULT":
        return 2.0

    if result_type == "DISQUALIFICATION":
        return 2.0

    if result_type == "FALL":
        return 2.0

    if result_type == "FORFEIT":
        return 2.0

    if result_type == "MAJOR":
        return 1.0

    if result_type == "TECH":
        return 1.5

    if result_type == "WALKOVER":
        return 0.0  # This is just an approximation

    raise NotImplementedError(result_type)


def _next_match_for_bye(match: str) -> str | None:
    if match == "championship_r32_01":
        return "championship_r16_01"

    if match == "championship_r32_02":
        return "championship_r16_01"

    if match == "championship_r32_03":
        return "championship_r16_02"

    if match == "championship_r32_04":
        return "championship_r16_02"

    if match == "championship_r32_05":
        return "championship_r16_03"

    if match == "championship_r32_06":
        return "championship_r16_03"

    if match == "championship_r32_07":
        return "championship_r16_04"

    if match == "championship_r32_08":
        return "championship_r16_04"

    if match == "championship_r32_09":
        return "championship_r16_05"

    if match == "championship_r32_10":
        return "championship_r16_05"

    if match == "championship_r32_11":
        return "championship_r16_06"

    if match == "championship_r32_12":
        return "championship_r16_06"

    if match == "championship_r32_13":
        return "championship_r16_07"

    if match == "championship_r32_14":
        return "championship_r16_07"

    if match == "championship_r32_15":
        return "championship_r16_08"

    if match == "championship_r32_16":
        return "championship_r16_08"

    if match == "championship_r16_01":
        return "championship_quarter_01"

    if match == "championship_r16_02":
        return "championship_quarter_01"

    if match == "championship_r16_03":
        return "championship_quarter_02"

    if match == "championship_r16_04":
        return "championship_quarter_02"

    if match == "championship_r16_05":
        return "championship_quarter_03"

    if match == "championship_r16_06":
        return "championship_quarter_03"

    if match == "championship_r16_07":
        return "championship_quarter_04"

    if match == "championship_r16_08":
        return "championship_quarter_04"

    if match == "consolation_round2_01":
        return "consolation_round3_01"

    if match == "consolation_round2_02":
        return "consolation_round3_01"

    if match == "consolation_round2_03":
        return "consolation_round3_02"

    if match == "consolation_round2_04":
        return "consolation_round3_02"

    if match == "consolation_round2_05":
        return "consolation_round3_03"

    if match == "consolation_round2_06":
        return "consolation_round3_03"

    if match == "consolation_round2_07":
        return "consolation_round3_04"

    if match == "consolation_round2_08":
        return "consolation_round3_04"

    if match == "championship_quarter_01":
        return "championship_semi_01"

    if match == "championship_quarter_02":
        return "championship_semi_01"

    if match == "championship_quarter_03":
        return "championship_semi_02"

    if match == "championship_quarter_04":
        return "championship_semi_02"

    if match == "consolation_round3_01":
        return "consolation_round4_blood_01"

    if match == "consolation_round3_02":
        return "consolation_round4_blood_02"

    if match == "consolation_round3_03":
        return "consolation_round4_blood_03"

    if match == "consolation_round3_04":
        return "consolation_round4_blood_04"

    if match == "consolation_round4_blood_01":
        return "consolation_round5_01"

    if match == "consolation_round4_blood_02":
        return "consolation_round5_01"

    if match == "consolation_round4_blood_03":
        return "consolation_round5_02"

    if match == "consolation_round4_blood_04":
        return "consolation_round5_02"

    if match == "championship_semi_01":
        return "championship_first_place"

    if match == "championship_semi_02":
        return "championship_first_place"

    if match == "consolation_round5_01":
        return "consolation_round6_semi_01"

    if match == "consolation_round5_02":
        return "consolation_round6_semi_02"

    if match == "consolation_round6_semi_01":
        return "consolation_third_place"

    if match == "consolation_round6_semi_02":
        return "consolation_third_place"

    if match == "consolation_seventh_place":
        return None

    if match == "consolation_fifth_place":
        return None

    if match == "consolation_third_place":
        return None

    if match == "championship_first_place":
        return None

    raise NotImplementedError(match)


def _bye_next_match_points(
    match: str, winner: Competitor | None, by_match: dict[str, Match]
) -> float:
    next_match_str = _next_match_for_bye(match)
    if next_match_str is None:
        return 0.0

    next_match = by_match[next_match_str]
    next_winner = next_match.bottom_competitor
    if next_match.top_win:
        next_winner = next_match.top_competitor

    if winner is None or next_winner is None or winner != next_winner:
        return 0.0

    if next_match.result_type == "BYE":
        # No support (yet) for multiple consecutive byes
        return 0.0

    advancement_points = _get_advancement_points(next_match.match, True)
    result_points = _get_result_points(next_match.result_type)
    return advancement_points + result_points


def _match_team_score_updates(
    match: Match, by_match: dict[str, Match]
) -> dict[str, float]:
    result: dict[str, float] = {}

    loser_team = None
    if match.top_win:
        winner = match.top_competitor
        winner_team = match.top_competitor.team
        if match.bottom_competitor is not None:
            loser_team = match.bottom_competitor.team
    else:
        winner = match.bottom_competitor
        winner_team = match.bottom_competitor.team
        if match.top_competitor is not None:
            loser_team = match.top_competitor.team

    winner_advancement_points = _get_advancement_points(match.match, True)
    loser_advancement_points = _get_advancement_points(match.match, False)
    winner_result_points = _get_result_points(match.result_type)

    winner_points = winner_advancement_points + winner_result_points
    loser_points = loser_advancement_points

    if match.result_type == "BYE":
        winner_points = _bye_next_match_points(match.match, winner, by_match)

    result[winner_team] = winner_points

    if loser_team is None:
        if loser_points != 0.0:
            raise RuntimeError("Invariant violation")
    elif loser_team == winner_team:
        result[winner_team] += loser_points
    else:
        result[loser_team] = loser_points

    return result


def _weight_team_score_updates(weight_class: WeightClass) -> dict[str, float]:
    result: dict[str, float] = {}
    by_match: dict[str, Match] = {match.match: match for match in weight_class.matches}
    for match in weight_class.matches:
        if match.top_win is None:
            continue

        match_updates = _match_team_score_updates(match, by_match)
        for acronym, score in match_updates.items():
            result.setdefault(acronym, 0.0)
            result[acronym] += score

    return result


def _compute_team_scores(weight_classes: list[WeightClass]) -> dict[str, float]:
    result: dict[str, float] = {}
    for weight_class in weight_classes:
        weight_updates = _weight_team_score_updates(weight_class)
        for acronym, score in weight_updates.items():
            result.setdefault(acronym, 0.0)
            result[acronym] += score

    return result


def _team_score_sort_reverse(value: tuple[str, float]) -> tuple[float, str]:
    acronym, score = value
    return -score, acronym


def _print_team_scores(team_scores: dict[str, float]) -> None:
    sorted_scores = sorted(team_scores.items(), key=_team_score_sort_reverse)
    for acronym, score in sorted_scores:
        print(f"  {acronym}: {score}")


def print_division_team_scores(
    weight_classes: list[WeightClass], division: str
) -> None:
    novice_weight_classes = [
        weight_class
        for weight_class in weight_classes
        if weight_class.division == division
    ]
    novice_team_scores = _compute_team_scores(novice_weight_classes)
    print(f"{division.title()}:")
    _print_team_scores(novice_team_scores)


def validate_acronym_mappings(
    weight_classes: list[WeightClass],
    team_acronym_mapping: dict[str, str],
    novice_team_acronym_mapping: dict[str, str],
    senior_team_acronym_mapping: dict[str, str],
    team_name_mapping: dict[str, int],
):
    actual_acronyms: set[str] = set()
    for weight_class in weight_classes:
        for match in weight_class.matches:
            if match.top_competitor is not None:
                actual_acronyms.add(match.top_competitor.team)
            if match.bottom_competitor is not None:
                actual_acronyms.add(match.bottom_competitor.team)

    mapped_acronyms = set(team_acronym_mapping.keys())
    mapped_acronyms.update(novice_team_acronym_mapping.keys())
    mapped_acronyms.update(senior_team_acronym_mapping.keys())

    if actual_acronyms != mapped_acronyms:
        raise RuntimeError(
            "Unexpected team acronyms",
            mapped_acronyms - actual_acronyms,
            actual_acronyms - mapped_acronyms,
        )

    actual_team_names = set(team_acronym_mapping.values())
    actual_team_names.update(novice_team_acronym_mapping.values())
    actual_team_names.update(senior_team_acronym_mapping.values())
    mapped_team_names = set(team_name_mapping.keys())

    if actual_team_names != mapped_team_names:
        raise RuntimeError(
            "Unexpected team names",
            mapped_team_names - actual_team_names,
            actual_team_names - mapped_team_names,
        )
