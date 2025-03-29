# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal, NamedTuple

import bs4
import pydantic


# NOTE: In some years, a clearly accidentally added team name appeared in team
#       scores.
_TEAM_SCORE_ACCIDENTAL: frozenset[str] = frozenset(["Mike", "TEST"])


class CompetitorRaw(pydantic.BaseModel):
    name: str
    team: str


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


class MatchRaw(pydantic.BaseModel):
    match: str
    top_competitor: CompetitorRaw | None
    bottom_competitor: CompetitorRaw | None
    result: str
    bout_number: int | None
    winner: CompetitorRaw | None
    winner_from: tuple[str, str] | None


class Match(pydantic.BaseModel):
    match: str
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    result_type: ResultType
    bout_number: int | None
    top_win: bool | None


Division = Literal["senior", "novice"]


class WeightClass(pydantic.BaseModel):
    division: Division
    weight: int
    matches: list[Match]


class TeamScore(pydantic.BaseModel):
    team: str
    score: float


class ExtractedTournament(pydantic.BaseModel):
    weight_classes: list[WeightClass]
    team_scores: dict[Division, list[TeamScore]]


class CompetitorWithWeight(pydantic.BaseModel):
    division: Division
    weight: int
    competitor: Competitor


def to_int_with_commas(value: str) -> int:
    cleaned = value.strip()
    result = int(value.replace(",", ""))

    expected = f"{result:,}"
    if cleaned != expected:
        raise ValueError("Invariant violation", value)

    return result


def set_winner(match: MatchRaw, by_match: dict[str, MatchRaw]) -> None:
    if match.winner is not None:
        return

    if match.result == "Bye":
        if match.bottom_competitor is None:
            if match.top_competitor is None:
                match.winner = None
                return

            match.winner = match.top_competitor
            return

        if match.top_competitor is None:
            if match.bottom_competitor is None:
                raise ValueError("Invariant violation", match)
            match.winner = match.bottom_competitor
            return

        raise ValueError("Invariant violation", match)

    if match.winner_from is not None:
        match_key, competitor_key = match.winner_from
        competitor = getattr(by_match[match_key], competitor_key)
        match.winner = competitor
        return

    raise NotImplementedError(match)


def set_result(match: MatchRaw) -> None:
    result = match.result
    if result != "":
        return

    top_competitor = match.top_competitor
    bottom_competitor = match.bottom_competitor
    if top_competitor is None or bottom_competitor is None:
        match.result = "Bye"
        return

    raise NotImplementedError(match)


def set_top_competitor(match: MatchRaw) -> None:
    top_competitor = match.top_competitor
    bottom_competitor = match.bottom_competitor
    if top_competitor is not None or bottom_competitor is not None:
        return

    result = match.result
    if result != "Bye":
        raise ValueError("Invariant violation", match)

    winner = match.winner
    if winner is None:
        return

    if not isinstance(winner, CompetitorRaw):
        raise ValueError("Invariant violation", match)

    match.top_competitor = winner


def _competitor_from_raw(
    value: CompetitorRaw | None, name_exceptions: dict[tuple[str, str], Competitor]
) -> Competitor | None:
    if value is None:
        return None

    exception_key = value.name, value.team
    if exception_key in name_exceptions:
        return name_exceptions[exception_key]

    parts = value.name.split()
    if len(parts) != 2:
        raise RuntimeError(value.name, value.team)

    return Competitor(
        first_name=parts[0],
        last_name=parts[1],
        suffix=None,
        team=value.team,
    )


def _competitor_equal_enough(competitor1: Competitor, competitor2: Competitor) -> bool:
    if competitor1.team != competitor2.team:
        return False

    if competitor1.suffix != competitor2.suffix:
        return False

    if competitor1.last_name != competitor2.last_name:
        return False

    name1 = competitor1.first_name
    name2 = competitor2.first_name
    if name1 == name2:
        return True

    # Names get shortened to first letter in later rounds
    if len(name1) == 1:
        return name2[0] == name1
    if len(name2) == 1:
        return name1[0] == name2

    return False


def _ensure_no_name_duplicates(matches: list[Match]) -> None:
    competitors_with_canonical_names: list[Competitor] = []
    for match in matches:
        if not match.match.startswith("championship_r32_"):
            continue

        if match.top_competitor is not None:
            competitors_with_canonical_names.append(match.top_competitor)

        if match.bottom_competitor is not None:
            competitors_with_canonical_names.append(match.bottom_competitor)

    # Update names based on canonical
    for match in matches:
        if match.top_competitor is not None:
            canonical_competitors = [
                canonical
                for canonical in competitors_with_canonical_names
                if _competitor_equal_enough(match.top_competitor, canonical)
            ]
            if len(canonical_competitors) != 1:
                raise ValueError(
                    "Invariant violation",
                    match.top_competitor,
                    len(canonical_competitors),
                    canonical_competitors,
                )
            match.top_competitor = canonical_competitors[0]

        if match.bottom_competitor is not None:
            canonical_competitors = [
                canonical
                for canonical in competitors_with_canonical_names
                if _competitor_equal_enough(match.bottom_competitor, canonical)
            ]
            if len(canonical_competitors) != 1:
                raise ValueError(
                    "Invariant violation",
                    match.bottom_competitor,
                    len(canonical_competitors),
                    canonical_competitors,
                )
            match.bottom_competitor = canonical_competitors[0]


def _competitor_name_equal_enough(name1: str, name2: str) -> bool:
    if name1 == name2:
        return True

    parts1 = name1.split()
    parts2 = name2.split()
    if len(parts1) != len(parts2):
        return False

    if parts1[1:] != parts2[1:]:
        return False

    start1 = parts1[0]
    start2 = parts2[0]
    # Names get shortened to first letter in later rounds
    if len(start1) == 1:
        return start2[0] == start1
    if len(start2) == 1:
        return start1[0] == start2

    return False


def _competitor_raw_equal_enough(
    competitor1: CompetitorRaw | None, competitor2: CompetitorRaw | None
) -> bool:
    if competitor1 is None or competitor2 is None:
        return competitor1 == competitor2

    if competitor1.team != competitor2.team:
        return False

    return _competitor_name_equal_enough(competitor1.name, competitor2.name)


def _determine_result_type(result: str) -> ResultType:
    if result == "P-Dec" or result.startswith("P-Dec "):
        return "WALKOVER"

    if result == "Dec" or result.startswith("Dec "):
        return "DECISION"

    if result.startswith("MajDec ") or result.startswith("M-Dec "):
        return "MAJOR"

    if result == "T-Fall" or result.startswith("T-Fall "):
        return "TECH"

    if result == "Fall" or result.startswith("Fall "):
        return "FALL"

    if result == "Bye":
        return "BYE"

    if result == "Dflt" or result.startswith("Dflt "):
        return "DEFAULT"

    if result == "Dq" or result.startswith("Dq "):
        return "DISQUALIFICATION"

    if result == "Forf" or result.startswith("Forf "):
        return "FORFEIT"

    raise NotImplementedError(result)


def clean_raw_matches(
    matches: list[MatchRaw], name_exceptions: dict[tuple[str, str], Competitor]
) -> list[Match]:
    result: list[Match] = []
    for match in matches:
        top_win = None

        top_competitor = _competitor_from_raw(match.top_competitor, name_exceptions)
        bottom_competitor = _competitor_from_raw(
            match.bottom_competitor, name_exceptions
        )

        if top_competitor is not None and _competitor_raw_equal_enough(
            match.winner, match.top_competitor
        ):
            top_win = True

        if bottom_competitor is not None and _competitor_raw_equal_enough(
            match.winner, match.bottom_competitor
        ):
            top_win = False

        if top_win is None:
            if bottom_competitor is not None or top_competitor is not None:
                raise RuntimeError("Invariant violation")

        result.append(
            Match(
                match=match.match,
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result=match.result,
                result_type=_determine_result_type(match.result),
                bout_number=match.bout_number,
                top_win=top_win,
            )
        )

    _ensure_no_name_duplicates(result)

    return result


def _normalize_team_name(team: str, seen_teams: set[str]) -> str:
    if team not in seen_teams:
        seen_teams.add(team)
        return team

    for i in range(2, 10):
        alternate_name = f"{team} ({i})"
        if alternate_name in seen_teams:
            continue

        seen_teams.add(alternate_name)
        return alternate_name

    raise RuntimeError("Unexpected number of repeats for team name", team)


def parse_team_scores(
    root: pathlib.Path,
    division: Division,
    team_score_exceptions: dict[tuple[Division, str], float],
) -> list[TeamScore]:
    with open(root / division / "team-scores.html") as file_obj:
        html = file_obj.read()

    soup = bs4.BeautifulSoup(html, features="html.parser")
    result: list[TeamScore] = []

    all_tables: list[bs4.Tag] = soup.find_all("table")
    # NOTE: This assumes every year will have a team with `2.0` points (for
    #       advancement).
    score_tables = [table for table in all_tables if "2.0" in table.text]
    if len(score_tables) != 1:
        raise ValueError("Invariant violation", division, len(score_tables))

    score_table = score_tables[-1]

    all_tr: list[bs4.Tag] = score_table.find_all("tr")
    # NOTE: We track the team names we've seen to avoid duplicates / ensure
    #       all team names are unique.
    seen_teams: set[str] = set()
    for table_row in all_tr:
        if table_row.text.strip() == "":
            continue

        if tuple(table_row.text.split()) == ("Place", "Team", "Score"):
            continue

        all_td = table_row.find_all("td")
        if len(all_td) < 2:
            raise ValueError("Invariant violation", division, len(all_td), all_td)

        team = all_td[-2].text.strip()
        if team in _TEAM_SCORE_ACCIDENTAL:
            continue

        score = float(all_td[-1].text)

        exception_key = division, team
        score = team_score_exceptions.get(exception_key, score)

        team = _normalize_team_name(team, seen_teams)
        result.append(TeamScore(team=team, score=score))

    return result


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
    division_weight_classes = [
        weight_class
        for weight_class in weight_classes
        if weight_class.division == division
    ]
    division_team_scores = _compute_team_scores(division_weight_classes)
    print(f"{division.title()}:")
    _print_team_scores(division_team_scores)


def validate_acronym_mapping_names(
    weight_classes: list[WeightClass],
    team_acronym_mappings: tuple[dict[str, str]],
    extra_team_score_maps: tuple[dict[str, float]],
    team_name_mapping: dict[str, int],
):
    actual_acronyms: set[str] = set()
    for weight_class in weight_classes:
        for match in weight_class.matches:
            if match.top_competitor is not None:
                actual_acronyms.add(match.top_competitor.team)
            if match.bottom_competitor is not None:
                actual_acronyms.add(match.bottom_competitor.team)

    mapped_acronyms = set()
    actual_team_names = set()
    for team_acronym_mapping in team_acronym_mappings:
        mapped_acronyms.update(team_acronym_mapping.keys())
        actual_team_names.update(team_acronym_mapping.values())

    if actual_acronyms != mapped_acronyms:
        raise RuntimeError(
            "Unexpected team acronyms",
            mapped_acronyms - actual_acronyms,
            actual_acronyms - mapped_acronyms,
        )

    for extra_team_scores in extra_team_score_maps:
        actual_team_names.update(extra_team_scores.keys())

    mapped_team_names = set(team_name_mapping.keys())
    if actual_team_names != mapped_team_names:
        raise RuntimeError(
            "Unexpected team names",
            mapped_team_names - actual_team_names,
            actual_team_names - mapped_team_names,
        )


def validate_acronym_mappings_divisons(
    weight_classes: list[WeightClass],
    team_acronym_mapping: dict[str, str],
    novice_team_acronym_mapping: dict[str, str],
    senior_team_acronym_mapping: dict[str, str],
):
    novice_acronyms = set()
    senior_acronyms = set()
    for weight_class in weight_classes:
        if weight_class.division == "novice":
            division_acronyms = novice_acronyms
        else:
            division_acronyms = senior_acronyms

        for match_ in weight_class.matches:
            if match_.top_competitor is not None:
                division_acronyms.add(match_.top_competitor.team)
            if match_.bottom_competitor is not None:
                division_acronyms.add(match_.bottom_competitor.team)

    acronyms_both = novice_acronyms.intersection(senior_acronyms)
    novice_only = novice_acronyms - acronyms_both
    senior_only = senior_acronyms - acronyms_both

    wrong_both = {
        key: value
        for key, value in team_acronym_mapping.items()
        if key not in acronyms_both
    }
    if wrong_both:
        raise RuntimeError("Invalid", wrong_both)

    wrong_novice = {
        key: value
        for key, value in novice_team_acronym_mapping.items()
        if key not in novice_only
    }
    wrong_senior = {
        key: value
        for key, value in senior_team_acronym_mapping.items()
        if key not in senior_only
    }
    wrong_novice_keys = set(wrong_novice.keys())
    wrong_senior_keys = set(wrong_senior.keys())
    if wrong_novice_keys != wrong_senior_keys:
        raise RuntimeError(
            "Invalid",
            sorted(wrong_novice_keys - wrong_senior_keys),
            sorted(wrong_senior_keys - wrong_novice_keys),
        )

    for key in wrong_novice_keys:
        novice_value = wrong_novice[key]
        senior_value = wrong_senior[key]
        if novice_value == senior_value:
            raise RuntimeError("Invalid", key, novice_value, senior_value)


class TeamScoreRow(pydantic.BaseModel):
    id_: int = pydantic.Field(alias="id")
    tournament_id: int
    division: Division
    team_id: int
    score: float


def team_scores_for_sql(
    division: Division,
    tournament_id: int,
    extracted: ExtractedTournament,
    team_acronym_mapping: dict[str, str],
    division_team_acronym_mapping: dict[str, str],
    team_name_mapping: dict[str, int],
    extra_team_scores: dict[str, int],
) -> list[TeamScoreRow]:
    weight_classes = [
        weight_class
        for weight_class in extracted.weight_classes
        if weight_class.division == division
    ]

    actual_team_score_list = extracted.team_scores[division]
    actual_team_scores = {
        team_score.team: team_score.score for team_score in actual_team_score_list
    }
    if len(actual_team_scores) != len(actual_team_score_list):
        raise ValueError("Duplicate team name in actual team scores")

    computed_team_scores = _compute_team_scores(weight_classes)
    acronyms = sorted(computed_team_scores.keys())
    team_score_rows: list[TeamScoreRow] = []

    for acronym in acronyms:
        computed_team_score = computed_team_scores[acronym]
        if acronym in division_team_acronym_mapping:
            if acronym in team_acronym_mapping:
                raise ValueError("Invariant violation: acronym mapped twice", acronym)

            team_name = division_team_acronym_mapping[acronym]
        else:
            team_name = team_acronym_mapping[acronym]

        actual_team_score = actual_team_scores.pop(team_name, None)
        if actual_team_score is None:
            if computed_team_score != 0.0:
                raise ValueError(
                    "Team score missing from official but nonzero",
                    acronym,
                    computed_team_score,
                )
            actual_team_score = 0.0

        team_id = team_name_mapping[team_name]
        team_score_rows.append(
            TeamScoreRow(
                id=0,  # To be filled out later
                tournament_id=tournament_id,
                division=division,
                team_id=team_id,
                score=actual_team_score,
            )
        )

    # NOTE: Sometimes `0.0` scores were included even if the team did not have
    #       any competitors in the division. Typically it was because the team
    #       had a competitor in the year prior. For negative scores, these
    #       represent a team that had a deduction in a different division but
    #       had no scoring athletes in this one. Team point deductions are
    #       applied to all divisions. Any **POSITIVE** scores appear just to be
    #       errors.
    if actual_team_scores != extra_team_scores:
        raise ValueError(
            "Unexpected team scores not accounted for",
            actual_team_scores,
            extra_team_scores,
        )

    extra_team_names = sorted(extra_team_scores.keys())
    for team_name in extra_team_names:
        actual_team_score = extra_team_scores[team_name]
        team_id = team_name_mapping[team_name]
        team_score_rows.append(
            TeamScoreRow(
                id=0,  # To be filled out later
                tournament_id=tournament_id,
                division=division,
                team_id=team_id,
                score=actual_team_score,
            )
        )

    return team_score_rows


def set_team_score_ids(team_scores: list[TeamScoreRow], id_start: int) -> None:
    for i, team_score in enumerate(team_scores):
        team_score.id_ = id_start + i


def print_team_score_sql(team_scores: list[TeamScoreRow]) -> None:
    for team_score in team_scores:
        print(
            f"  ({team_score.id_}, {team_score.tournament_id}, "
            f"'{team_score.division}', {team_score.team_id}, {team_score.score}),"
        )


class CompetitorRow(pydantic.BaseModel):
    id_: int = pydantic.Field(alias="id")
    first_name: str
    last_name: str
    suffix: str | None


class TeamCompetitorRow(pydantic.BaseModel):
    id_: int = pydantic.Field(alias="id")
    team_id: int
    competitor_id: int


def _resolve_team_id(
    acronym: str,
    team_acronym_mapping: dict[str, str],
    division_acronym_mapping: dict[str, str],
    team_name_mapping: dict[str, int],
) -> int:
    if acronym in division_acronym_mapping:
        if acronym in team_acronym_mapping:
            raise ValueError("Invariant violation: acronym mapped twice", acronym)

        team_name = division_acronym_mapping[acronym]
    else:
        team_name = team_acronym_mapping[acronym]

    return team_name_mapping[team_name]


class MappedCompetitors(NamedTuple):
    competitor_rows: list[CompetitorRow]
    team_competitor_rows: list[TeamCompetitorRow]
    next_start_id: int


def _get_weight_class_competitors_for_sql(
    start_id: int,
    weight_class: WeightClass,
    team_acronym_mapping: dict[str, str],
    division_acronym_mapping: dict[str, str],
    team_name_mapping: dict[str, int],
) -> MappedCompetitors:
    competitor_rows: list[CompetitorRow] = []
    team_competitor_rows: list[TeamCompetitorRow] = []
    current_id = start_id - 1  # Decrement because we increment before use

    for match in weight_class.matches:
        if not match.match.startswith("championship_r32_"):
            continue

        if match.top_competitor is not None:
            current_id += 1

            team_id = _resolve_team_id(
                match.top_competitor.team,
                team_acronym_mapping,
                division_acronym_mapping,
                team_name_mapping,
            )
            competitor_rows.append(
                CompetitorRow(
                    id=current_id,
                    first_name=match.top_competitor.first_name,
                    last_name=match.top_competitor.last_name,
                    suffix=match.top_competitor.suffix,
                )
            )
            team_competitor_rows.append(
                TeamCompetitorRow(
                    id=current_id, team_id=team_id, competitor_id=current_id
                )
            )

        if match.bottom_competitor is not None:
            current_id += 1

            team_id = _resolve_team_id(
                match.bottom_competitor.team,
                team_acronym_mapping,
                division_acronym_mapping,
                team_name_mapping,
            )
            competitor_rows.append(
                CompetitorRow(
                    id=current_id,
                    first_name=match.bottom_competitor.first_name,
                    last_name=match.bottom_competitor.last_name,
                    suffix=match.bottom_competitor.suffix,
                )
            )
            team_competitor_rows.append(
                TeamCompetitorRow(
                    id=current_id, team_id=team_id, competitor_id=current_id
                )
            )

    return MappedCompetitors(
        competitor_rows=competitor_rows,
        team_competitor_rows=team_competitor_rows,
        next_start_id=current_id + 1,
    )


def get_competitors_for_sql(
    start_id: int,
    weight_classes: list[WeightClass],
    team_acronym_mapping: dict[str, str],
    novice_acronym_mapping: dict[str, str],
    senior_acronym_mapping: dict[str, str],
    team_name_mapping: dict[str, int],
) -> MappedCompetitors:
    competitor_rows: list[CompetitorRow] = []
    team_competitor_rows: list[TeamCompetitorRow] = []

    # NOTE: This is not complete yet / still in development (hence the `None`
    #       return value)
    for weight_class in weight_classes:
        if weight_class.division == "senior":
            division_acronym_mapping = senior_acronym_mapping
        else:
            division_acronym_mapping = novice_acronym_mapping

        mapped_competitors = _get_weight_class_competitors_for_sql(
            start_id,
            weight_class,
            team_acronym_mapping,
            division_acronym_mapping,
            team_name_mapping,
        )

        # Prepare for next iteration
        competitor_rows.extend(mapped_competitors.competitor_rows)
        team_competitor_rows.extend(mapped_competitors.team_competitor_rows)
        start_id = mapped_competitors.next_start_id

    # Print the **LAST** `next_start_id`
    return MappedCompetitors(
        competitor_rows=competitor_rows,
        team_competitor_rows=team_competitor_rows,
        next_start_id=start_id,
    )
