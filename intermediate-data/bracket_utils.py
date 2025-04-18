# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
import sqlite3
from typing import Literal, NamedTuple

import bs4
import pydantic

# NOTE: In some years, a clearly accidentally added team name appeared in team
#       scores.
_TEAM_SCORE_ACCIDENTAL: frozenset[str] = frozenset(["Mike", "TEST"])
_TEAMS_FROM_TOURNAMENT = """\
SELECT
  ts.team_id, t.name
FROM
  team_score AS ts
  INNER JOIN team AS t ON t.id = ts.team_id
WHERE
  ts.tournament_id = :tournament_id
"""


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class CompetitorRaw(_ForbidExtra):
    name: str
    team_full: str
    team_acronym: str | None

    @property
    def long_name(self) -> str:
        return f"{self.name} ({self.team_full})"


class CompetitorTuple(NamedTuple):
    first_name: str
    last_name: str
    team_full: str
    team_acronym: str | None


class Competitor(_ForbidExtra):
    full_name: str
    first_name: str
    last_name: str
    team_full: str
    team_acronym: str | None

    @property
    def as_tuple(self) -> CompetitorTuple:
        """Convert to a (hashable) tuple."""
        return CompetitorTuple(
            first_name=self.first_name,
            last_name=self.last_name,
            team_full=self.team_full,
            team_acronym=self.team_acronym,
        )


MatchSlot = Literal[
    "championship_r32_01",
    "championship_r32_02",
    "championship_r32_03",
    "championship_r32_04",
    "championship_r32_05",
    "championship_r32_06",
    "championship_r32_07",
    "championship_r32_08",
    "championship_r32_09",
    "championship_r32_10",
    "championship_r32_11",
    "championship_r32_12",
    "championship_r32_13",
    "championship_r32_14",
    "championship_r32_15",
    "championship_r32_16",
    "championship_r16_01",
    "championship_r16_02",
    "championship_r16_03",
    "championship_r16_04",
    "championship_r16_05",
    "championship_r16_06",
    "championship_r16_07",
    "championship_r16_08",
    "consolation_round2_01",
    "consolation_round2_02",
    "consolation_round2_03",
    "consolation_round2_04",
    "consolation_round2_05",
    "consolation_round2_06",
    "consolation_round2_07",
    "consolation_round2_08",
    "championship_quarter_01",
    "championship_quarter_02",
    "championship_quarter_03",
    "championship_quarter_04",
    "consolation_round3_01",
    "consolation_round3_02",
    "consolation_round3_03",
    "consolation_round3_04",
    "consolation_round4_blood_01",
    "consolation_round4_blood_02",
    "consolation_round4_blood_03",
    "consolation_round4_blood_04",
    "championship_semi_01",
    "championship_semi_02",
    "consolation_round5_01",
    "consolation_round5_02",
    "consolation_round6_semi_01",
    "consolation_round6_semi_02",
    "consolation_seventh_place",
    "consolation_fifth_place",
    "consolation_third_place",
    "championship_first_place",
]

BracketPosition = Literal["top", "bottom"]


class MatchRaw(_ForbidExtra):
    match_slot: MatchSlot
    top_competitor: CompetitorRaw | None
    bottom_competitor: CompetitorRaw | None
    result: str
    bout_number: int | None
    winner: CompetitorRaw | None
    winner_from: tuple[MatchSlot, BracketPosition] | None


ResultType = Literal[
    "bye",
    "decision",
    "default",
    "disqualification",
    "fall",
    "forfeit",
    "major",
    "tech",
    "walkover",
    "place",
]


class Match(_ForbidExtra):
    match_slot: MatchSlot
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    result_type: ResultType
    bout_number: int | None
    top_win: bool | None


Division = Literal[
    "bantam",
    "intermediate",
    "novice",
    "senior",
    "bantam_girls",
    "intermediate_girls",
    "novice_girls",
    "senior_girls",
]


class WeightClass(_ForbidExtra):
    division: Division
    weight: int
    matches: list[Match]


class TeamScore(_ForbidExtra):
    team: str
    acronym: str | None
    score: float


class Deduction(_ForbidExtra):
    team: str
    reason: str
    value: float


def _division_sort_key(division: Division) -> int:
    if division == "bantam":
        return 1

    if division == "intermediate":
        return 2

    if division == "novice":
        return 3

    if division == "senior":
        return 4

    if division == "bantam_girls":
        return 5

    if division == "intermediate_girls":
        return 6

    if division == "novice_girls":
        return 7

    if division == "senior_girls":
        return 8

    if division == "junior_iwf":
        return 9

    if division == "novice_iwf":
        return 10

    if division == "senior_iwf":
        return 11

    raise NotImplementedError(division)


def _weight_class_sort_key(weight_class: WeightClass) -> tuple[int, int]:
    division = weight_class.division
    return _division_sort_key(division), weight_class.weight


def _deduction_sort_key(deduction: Deduction) -> tuple[str, str, float]:
    return deduction.team, deduction.reason, deduction.value


def _team_score_sort_key(team_score: TeamScore) -> tuple[float, str]:
    return -team_score.score, team_score.team


class ExtractedTournament(_ForbidExtra):
    weight_classes: list[WeightClass]
    team_scores: dict[Division, list[TeamScore]]
    deductions: list[Deduction]

    def _sort_weight_classes(self):
        self.weight_classes.sort(key=_weight_class_sort_key)

    def _sort_team_scores(self):
        divisions = sorted(self.team_scores.keys(), key=_division_sort_key)
        ordered = {
            division: sorted(self.team_scores[division], key=_team_score_sort_key)
            for division in divisions
        }
        self.team_scores = ordered

    def _sort_deductions(self):
        self.deductions.sort(key=_deduction_sort_key)

    def sort(self):
        self._sort_weight_classes()
        self._sort_team_scores()
        self._sort_deductions()


class CompetitorWithWeight(_ForbidExtra):
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


def set_winner(match: MatchRaw, by_match: dict[MatchSlot, MatchRaw]) -> None:
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
        match_slot, bracket_position = match.winner_from
        if bracket_position == "top":
            competitor = by_match[match_slot].top_competitor
        else:
            competitor = by_match[match_slot].bottom_competitor
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


def competitor_from_raw(
    value: CompetitorRaw | None, name_exceptions: dict[tuple[str, str], Competitor]
) -> Competitor | None:
    if value is None:
        return None

    exception_key = value.name, value.team_acronym
    if exception_key in name_exceptions:
        competitor = name_exceptions[exception_key]
        competitor.full_name = value.name
        return competitor

    exception_key = value.name, value.team_full
    if exception_key in name_exceptions:
        competitor = name_exceptions[exception_key]
        competitor.full_name = value.name
        return competitor

    parts = value.name.split()
    if len(parts) != 2:
        raise RuntimeError(value.name, value.team_full, value.team_acronym)

    return Competitor(
        full_name=value.name,
        first_name=parts[0],
        last_name=parts[1],
        team_full=value.team_full,
        team_acronym=value.team_acronym,
    )


def _competitor_equal_enough(competitor1: Competitor, competitor2: Competitor) -> bool:
    if competitor1.team_acronym != competitor2.team_acronym:
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
        if not match.match_slot.startswith("championship_r32_"):
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

    if competitor1.team_full != competitor2.team_full:
        return False

    if competitor1.team_acronym != competitor2.team_acronym:
        return False

    return _competitor_name_equal_enough(competitor1.name, competitor2.name)


def _determine_result_type(result: str) -> ResultType:
    if result == "P-Dec" or result.startswith("P-Dec "):
        return "walkover"

    if result == "Dec" or result.startswith("Dec "):
        return "decision"

    if result.startswith("MajDec ") or result.startswith("M-Dec "):
        return "major"

    if result == "T-Fall" or result.startswith("T-Fall "):
        return "tech"

    if result == "Fall" or result.startswith("Fall "):
        return "fall"

    if result == "Bye":
        return "bye"

    if result == "Dflt" or result.startswith("Dflt "):
        return "default"

    if result == "Dq" or result.startswith("Dq "):
        return "disqualification"

    if result == "Forf" or result.startswith("Forf "):
        return "forfeit"

    raise NotImplementedError(result)


def clean_raw_matches(
    matches: list[MatchRaw], name_exceptions: dict[tuple[str, str], Competitor]
) -> list[Match]:
    result: list[Match] = []
    for match in matches:
        top_win = None

        top_competitor = competitor_from_raw(match.top_competitor, name_exceptions)
        bottom_competitor = competitor_from_raw(
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

        if top_win is None and (
            bottom_competitor is not None or top_competitor is not None
        ):
            raise RuntimeError("Invariant violation")

        result.append(
            Match(
                match_slot=match.match_slot,
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


def reverse_acronym_map(
    team_acronym_mapping: dict[str, str],
    division_team_acronym_mapping: dict[str, str],
) -> dict[str, str]:
    result: dict[str, str] = {}

    for acronym, team_name in division_team_acronym_mapping.items():
        if team_name in result:
            raise KeyError("Duplicate", team_name, acronym, result[team_name])

        result[team_name] = acronym

    for acronym, team_name in team_acronym_mapping.items():
        if team_name in result:
            raise KeyError("Duplicate", team_name, acronym, result[team_name])

        result[team_name] = acronym

    return result


def parse_team_scores(
    root: pathlib.Path,
    division: Division,
    reverse_acronym: dict[str, str],
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
        acronym = reverse_acronym.get(team)
        result.append(TeamScore(team=team, acronym=acronym, score=score))

    return result


def _get_advancement_points(match_slot: MatchSlot, winner: bool) -> float:
    if match_slot == "championship_first_place":
        return 16.0 if winner else 12.0

    if match_slot == "consolation_third_place":
        return 9.0 if winner else 7.0

    if match_slot == "consolation_fifth_place":
        return 5.0 if winner else 3.0

    if match_slot == "consolation_seventh_place":
        return 2.0 if winner else 1.0

    if match_slot.startswith("consolation_"):
        return 1.0 if winner else 0.0

    if match_slot.startswith("championship_"):
        return 2.0 if winner else 0.0

    raise NotImplementedError(match_slot, winner)


def _get_result_points(result_type: ResultType) -> float:
    if result_type == "bye":
        return 0.0

    if result_type == "decision":
        return 0.0

    if result_type == "default":
        return 2.0

    if result_type == "disqualification":
        return 2.0

    if result_type == "fall":
        return 2.0

    if result_type == "forfeit":
        return 2.0

    if result_type == "major":
        return 1.0

    if result_type == "tech":
        return 1.5

    if result_type == "walkover":
        return 0.0  # This is just an approximation

    raise NotImplementedError(result_type)


def next_match_position_lose_v1(
    match_slot: MatchSlot,
) -> tuple[MatchSlot, BracketPosition] | None:
    """In use from 2007-2019"""
    # NOTE: Earlier brackets used follow-the-leader so these are not guaranteed
    #       to happen unless the winner reached the semifinals.
    if match_slot == "championship_r32_02":
        return "consolation_round3_01", "bottom"

    if match_slot == "championship_r32_04":
        return "consolation_round3_01", "bottom"

    if match_slot == "championship_r32_06":
        return "consolation_round3_02", "bottom"

    if match_slot == "championship_r32_08":
        return "consolation_round3_02", "bottom"

    if match_slot == "championship_r32_10":
        return "consolation_round3_03", "bottom"

    if match_slot == "championship_r32_12":
        return "consolation_round3_03", "bottom"

    if match_slot == "championship_r32_14":
        return "consolation_round3_04", "bottom"

    if match_slot == "championship_r32_16":
        return "consolation_round3_04", "bottom"

    if match_slot == "championship_r16_01":
        return "consolation_round3_01", "top"

    if match_slot == "championship_r16_02":
        return "consolation_round3_01", "top"

    if match_slot == "championship_r16_03":
        return "consolation_round3_02", "top"

    if match_slot == "championship_r16_04":
        return "consolation_round3_02", "top"

    if match_slot == "championship_r16_05":
        return "consolation_round3_03", "top"

    if match_slot == "championship_r16_06":
        return "consolation_round3_03", "top"

    if match_slot == "championship_r16_07":
        return "consolation_round3_04", "top"

    if match_slot == "championship_r16_08":
        return "consolation_round3_04", "top"

    if match_slot == "championship_quarter_01":
        return "consolation_round4_blood_01", "top"

    if match_slot == "championship_quarter_02":
        return "consolation_round4_blood_02", "top"

    if match_slot == "championship_quarter_03":
        return "consolation_round4_blood_03", "bottom"

    if match_slot == "championship_quarter_04":
        return "consolation_round4_blood_04", "bottom"

    if match_slot == "championship_semi_01":
        return "consolation_round6_semi_01", "top"

    if match_slot == "championship_semi_02":
        return "consolation_round6_semi_02", "bottom"

    if match_slot == "consolation_round5_01":
        return "consolation_seventh_place", "top"

    if match_slot == "consolation_round5_02":
        return "consolation_seventh_place", "bottom"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_fifth_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_fifth_place", "bottom"

    raise NotImplementedError(match_slot)


def next_match_position_win(
    match_slot: MatchSlot,
) -> tuple[MatchSlot, BracketPosition] | None:
    if match_slot == "championship_r32_01":
        return "championship_r16_01", "top"

    if match_slot == "championship_r32_02":
        return "championship_r16_01", "bottom"

    if match_slot == "championship_r32_03":
        return "championship_r16_02", "top"

    if match_slot == "championship_r32_04":
        return "championship_r16_02", "bottom"

    if match_slot == "championship_r32_05":
        return "championship_r16_03", "top"

    if match_slot == "championship_r32_06":
        return "championship_r16_03", "bottom"

    if match_slot == "championship_r32_07":
        return "championship_r16_04", "top"

    if match_slot == "championship_r32_08":
        return "championship_r16_04", "bottom"

    if match_slot == "championship_r32_09":
        return "championship_r16_05", "top"

    if match_slot == "championship_r32_10":
        return "championship_r16_05", "bottom"

    if match_slot == "championship_r32_11":
        return "championship_r16_06", "top"

    if match_slot == "championship_r32_12":
        return "championship_r16_06", "bottom"

    if match_slot == "championship_r32_13":
        return "championship_r16_07", "top"

    if match_slot == "championship_r32_14":
        return "championship_r16_07", "bottom"

    if match_slot == "championship_r32_15":
        return "championship_r16_08", "top"

    if match_slot == "championship_r32_16":
        return "championship_r16_08", "bottom"

    if match_slot == "championship_r16_01":
        return "championship_quarter_01", "top"

    if match_slot == "championship_r16_02":
        return "championship_quarter_01", "bottom"

    if match_slot == "championship_r16_03":
        return "championship_quarter_02", "top"

    if match_slot == "championship_r16_04":
        return "championship_quarter_02", "bottom"

    if match_slot == "championship_r16_05":
        return "championship_quarter_03", "top"

    if match_slot == "championship_r16_06":
        return "championship_quarter_03", "bottom"

    if match_slot == "championship_r16_07":
        return "championship_quarter_04", "top"

    if match_slot == "championship_r16_08":
        return "championship_quarter_04", "bottom"

    if match_slot == "consolation_round2_01":
        return "consolation_round3_01", "top"

    if match_slot == "consolation_round2_02":
        return "consolation_round3_01", "bottom"

    if match_slot == "consolation_round2_03":
        return "consolation_round3_02", "top"

    if match_slot == "consolation_round2_04":
        return "consolation_round3_02", "bottom"

    if match_slot == "consolation_round2_05":
        return "consolation_round3_03", "top"

    if match_slot == "consolation_round2_06":
        return "consolation_round3_03", "bottom"

    if match_slot == "consolation_round2_07":
        return "consolation_round3_04", "top"

    if match_slot == "consolation_round2_08":
        return "consolation_round3_04", "bottom"

    if match_slot == "championship_quarter_01":
        return "championship_semi_01", "top"

    if match_slot == "championship_quarter_02":
        return "championship_semi_01", "bottom"

    if match_slot == "championship_quarter_03":
        return "championship_semi_02", "top"

    if match_slot == "championship_quarter_04":
        return "championship_semi_02", "bottom"

    if match_slot == "consolation_round3_01":
        return "consolation_round4_blood_01", "bottom"

    if match_slot == "consolation_round3_02":
        return "consolation_round4_blood_02", "bottom"

    if match_slot == "consolation_round3_03":
        return "consolation_round4_blood_03", "top"

    if match_slot == "consolation_round3_04":
        return "consolation_round4_blood_04", "top"

    if match_slot == "consolation_round4_blood_01":
        return "consolation_round5_01", "top"

    if match_slot == "consolation_round4_blood_02":
        return "consolation_round5_01", "bottom"

    if match_slot == "consolation_round4_blood_03":
        return "consolation_round5_02", "top"

    if match_slot == "consolation_round4_blood_04":
        return "consolation_round5_02", "bottom"

    if match_slot == "championship_semi_01":
        return "championship_first_place", "top"

    if match_slot == "championship_semi_02":
        return "championship_first_place", "bottom"

    if match_slot == "consolation_round5_01":
        return "consolation_round6_semi_01", "bottom"

    if match_slot == "consolation_round5_02":
        return "consolation_round6_semi_02", "top"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_third_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_third_place", "bottom"

    if match_slot == "consolation_seventh_place":
        return None

    if match_slot == "consolation_fifth_place":
        return None

    if match_slot == "consolation_third_place":
        return None

    if match_slot == "championship_first_place":
        return None

    raise NotImplementedError(match_slot)


def next_match_position_lose_v2(
    match_slot: MatchSlot,
) -> tuple[MatchSlot, BracketPosition] | None:
    """In use from 2022-2022"""
    if match_slot == "championship_r32_02":
        return "consolation_round2_01", "bottom"

    if match_slot == "championship_r32_04":
        return "consolation_round2_02", "bottom"

    if match_slot == "championship_r32_06":
        return "consolation_round2_03", "bottom"

    if match_slot == "championship_r32_08":
        return "consolation_round2_04", "bottom"

    if match_slot == "championship_r32_10":
        return "consolation_round2_05", "top"

    if match_slot == "championship_r32_12":
        return "consolation_round2_06", "top"

    if match_slot == "championship_r32_14":
        return "consolation_round2_07", "top"

    if match_slot == "championship_r32_16":
        return "consolation_round2_08", "top"

    if match_slot == "championship_r16_01":
        return "consolation_round2_08", "bottom"

    if match_slot == "championship_r16_02":
        return "consolation_round2_07", "bottom"

    if match_slot == "championship_r16_03":
        return "consolation_round2_06", "bottom"

    if match_slot == "championship_r16_04":
        return "consolation_round2_05", "bottom"

    if match_slot == "championship_r16_05":
        return "consolation_round2_04", "top"

    if match_slot == "championship_r16_06":
        return "consolation_round2_03", "top"

    if match_slot == "championship_r16_07":
        return "consolation_round2_02", "top"

    if match_slot == "championship_r16_08":
        return "consolation_round2_01", "top"

    if match_slot == "championship_quarter_01":
        return "consolation_round4_blood_03", "bottom"

    if match_slot == "championship_quarter_02":
        return "consolation_round4_blood_04", "bottom"

    if match_slot == "championship_quarter_03":
        return "consolation_round4_blood_01", "top"

    if match_slot == "championship_quarter_04":
        return "consolation_round4_blood_02", "top"

    if match_slot == "championship_semi_01":
        return "consolation_round6_semi_01", "top"

    if match_slot == "championship_semi_02":
        return "consolation_round6_semi_02", "bottom"

    if match_slot == "consolation_round5_01":
        return "consolation_seventh_place", "top"

    if match_slot == "consolation_round5_02":
        return "consolation_seventh_place", "bottom"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_fifth_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_fifth_place", "bottom"

    raise NotImplementedError(match_slot)


def next_match_position_lose_v3(
    match_slot: MatchSlot,
) -> tuple[MatchSlot, BracketPosition] | None:
    """In use from 2023-2025"""
    if match_slot == "championship_r32_02":
        return "consolation_round2_01", "bottom"

    if match_slot == "championship_r32_04":
        return "consolation_round2_02", "bottom"

    if match_slot == "championship_r32_06":
        return "consolation_round2_03", "bottom"

    if match_slot == "championship_r32_08":
        return "consolation_round2_04", "bottom"

    if match_slot == "championship_r32_10":
        return "consolation_round2_05", "top"

    if match_slot == "championship_r32_12":
        return "consolation_round2_06", "top"

    if match_slot == "championship_r32_14":
        return "consolation_round2_07", "top"

    if match_slot == "championship_r32_16":
        return "consolation_round2_08", "top"

    if match_slot == "championship_r16_01":
        return "consolation_round2_08", "bottom"

    if match_slot == "championship_r16_02":
        return "consolation_round2_07", "bottom"

    if match_slot == "championship_r16_03":
        return "consolation_round2_06", "bottom"

    if match_slot == "championship_r16_04":
        return "consolation_round2_05", "bottom"

    if match_slot == "championship_r16_05":
        return "consolation_round2_04", "top"

    if match_slot == "championship_r16_06":
        return "consolation_round2_03", "top"

    if match_slot == "championship_r16_07":
        return "consolation_round2_02", "top"

    if match_slot == "championship_r16_08":
        return "consolation_round2_01", "top"

    if match_slot == "championship_quarter_01":
        return "consolation_round4_blood_02", "top"

    if match_slot == "championship_quarter_02":
        return "consolation_round4_blood_01", "top"

    if match_slot == "championship_quarter_03":
        return "consolation_round4_blood_04", "bottom"

    if match_slot == "championship_quarter_04":
        return "consolation_round4_blood_03", "bottom"

    if match_slot == "championship_semi_01":
        return "consolation_round6_semi_02", "bottom"

    if match_slot == "championship_semi_02":
        return "consolation_round6_semi_01", "top"

    if match_slot == "consolation_round5_01":
        return "consolation_seventh_place", "top"

    if match_slot == "consolation_round5_02":
        return "consolation_seventh_place", "bottom"

    if match_slot == "consolation_round6_semi_01":
        return "consolation_fifth_place", "top"

    if match_slot == "consolation_round6_semi_02":
        return "consolation_fifth_place", "bottom"

    raise NotImplementedError(match_slot)


def _next_match_for_bye(match_slot: MatchSlot) -> MatchSlot | None:
    next_position = next_match_position_win(match_slot)
    if next_position is None:
        return None

    match_slot, _ = next_position
    return match_slot


def _bye_next_match_points(
    match_slot: MatchSlot, winner: Competitor | None, by_match: dict[MatchSlot, Match]
) -> float:
    next_match_str = _next_match_for_bye(match_slot)
    if next_match_str is None:
        return 0.0

    next_match = by_match[next_match_str]
    next_winner = next_match.bottom_competitor
    if next_match.top_win:
        next_winner = next_match.top_competitor

    if winner is None or next_winner is None or winner != next_winner:
        return 0.0

    if next_match.result_type == "bye":
        # No support (yet) for multiple consecutive byes
        return 0.0

    advancement_points = _get_advancement_points(next_match.match_slot, True)
    result_points = _get_result_points(next_match.result_type)
    return advancement_points + result_points


def _match_team_score_updates(
    match: Match, by_match: dict[MatchSlot, Match]
) -> dict[str, float]:
    result: dict[str, float] = {}

    loser_team = None
    if match.top_win:
        winner = match.top_competitor
        winner_team = match.top_competitor.team_acronym
        if match.bottom_competitor is not None:
            loser_team = match.bottom_competitor.team_acronym
    else:
        winner = match.bottom_competitor
        winner_team = match.bottom_competitor.team_acronym
        if match.top_competitor is not None:
            loser_team = match.top_competitor.team_acronym

    winner_advancement_points = _get_advancement_points(match.match_slot, True)
    loser_advancement_points = _get_advancement_points(match.match_slot, False)
    winner_result_points = _get_result_points(match.result_type)

    winner_points = winner_advancement_points + winner_result_points
    loser_points = loser_advancement_points

    if match.result_type == "bye":
        winner_points = _bye_next_match_points(match.match_slot, winner, by_match)

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
    by_match: dict[MatchSlot, Match] = {
        match.match_slot: match for match in weight_class.matches
    }
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
                actual_acronyms.add(match.top_competitor.team_acronym)
            if match.bottom_competitor is not None:
                actual_acronyms.add(match.bottom_competitor.team_acronym)

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


def validate_acronym_mappings_divisions(
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
                division_acronyms.add(match_.top_competitor.team_acronym)
            if match_.bottom_competitor is not None:
                division_acronyms.add(match_.bottom_competitor.team_acronym)

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


class TeamScoreRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    tournament_id: int
    division: Division
    team_id: int
    team_acronym: str
    team_name: str
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
                team_acronym=acronym,
                team_name=team_name,
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
                team_acronym="",
                team_name=team_name,
                score=actual_team_score,
            )
        )

    return team_score_rows


def set_team_score_ids(team_scores: list[TeamScoreRow], id_start: int) -> None:
    for i, team_score in enumerate(team_scores):
        team_score.id_ = id_start + i


def print_team_score_sql(team_scores: list[TeamScoreRow]) -> None:
    for row in team_scores:
        team_name_str = sql_nullable_str(row.team_name)
        print(
            f"  ({row.id_}, {row.tournament_id}, '{row.division}', "
            f"{row.team_id}, '{row.team_acronym}', "
            f"{team_name_str}, {row.score}),"
        )


class CompetitorRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    first_name: str
    last_name: str


class TeamCompetitorRow(_ForbidExtra):
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


class MappedCompetitors(_ForbidExtra):
    competitor_rows: list[CompetitorRow]
    team_competitor_rows: list[TeamCompetitorRow]
    team_competitor_by_info: dict[CompetitorTuple, int]
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
    team_competitor_by_info: dict[CompetitorTuple, int] = {}
    current_id = start_id - 1  # Decrement because we increment before use

    for match in weight_class.matches:
        if not match.match_slot.startswith("championship_r32_"):
            continue

        if match.top_competitor is not None:
            current_id += 1

            team_id = _resolve_team_id(
                match.top_competitor.team_acronym,
                team_acronym_mapping,
                division_acronym_mapping,
                team_name_mapping,
            )
            competitor_rows.append(
                CompetitorRow(
                    id=current_id,
                    first_name=match.top_competitor.first_name,
                    last_name=match.top_competitor.last_name,
                )
            )
            team_competitor_rows.append(
                TeamCompetitorRow(
                    id=current_id, team_id=team_id, competitor_id=current_id
                )
            )
            key = match.top_competitor.as_tuple
            if key in team_competitor_by_info:
                raise RuntimeError("Invariant violation: duplicate", key)
            team_competitor_by_info[key] = current_id

        if match.bottom_competitor is not None:
            current_id += 1

            team_id = _resolve_team_id(
                match.bottom_competitor.team_acronym,
                team_acronym_mapping,
                division_acronym_mapping,
                team_name_mapping,
            )
            competitor_rows.append(
                CompetitorRow(
                    id=current_id,
                    first_name=match.bottom_competitor.first_name,
                    last_name=match.bottom_competitor.last_name,
                )
            )
            team_competitor_rows.append(
                TeamCompetitorRow(
                    id=current_id, team_id=team_id, competitor_id=current_id
                )
            )
            key = match.bottom_competitor.as_tuple
            if key in team_competitor_by_info:
                raise RuntimeError("Invariant violation: duplicate", key)
            team_competitor_by_info[key] = current_id

    return MappedCompetitors(
        competitor_rows=competitor_rows,
        team_competitor_rows=team_competitor_rows,
        team_competitor_by_info=team_competitor_by_info,
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
    team_competitor_by_info: dict[CompetitorTuple, int] = {}

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
        start_id = mapped_competitors.next_start_id
        competitor_rows.extend(mapped_competitors.competitor_rows)
        team_competitor_rows.extend(mapped_competitors.team_competitor_rows)
        for key, value in mapped_competitors.team_competitor_by_info.items():
            if key in team_competitor_by_info:
                raise RuntimeError("Invariant violation: duplicate", key)
            team_competitor_by_info[key] = value

    # Print the **LAST** `next_start_id`
    return MappedCompetitors(
        competitor_rows=competitor_rows,
        team_competitor_rows=team_competitor_rows,
        team_competitor_by_info=team_competitor_by_info,
        next_start_id=start_id,
    )


def sql_nullable_str(value: str | None) -> str:
    if value is None:
        return "NULL"

    quoted = value.replace("'", "''")
    return f"'{quoted}'"


def print_competitors_sql(competitor_rows: list[CompetitorRow]) -> None:
    for row in competitor_rows:
        first_name = sql_nullable_str(row.first_name)
        last_name = sql_nullable_str(row.last_name)
        print(f"  ({row.id_}, {first_name}, {last_name}),")


def print_team_competitors_sql(team_competitor_rows: list[TeamCompetitorRow]) -> None:
    for row in team_competitor_rows:
        print(f"  ({row.id_}, {row.team_id}, {row.competitor_id}),")


class MatchRow(_ForbidExtra):
    id_: int = pydantic.Field(alias="id")
    bracket_id: int
    bout_number: int | None
    match_slot: MatchSlot
    top_competitor_id: int | None  # team_competitor(id)
    bottom_competitor_id: int | None  # team_competitor(id)
    top_win: bool
    result: str
    result_type: ResultType
    top_team_acronym: str | None
    bottom_team_acronym: str | None


class MappedMatches(_ForbidExtra):
    match_rows: list[MatchRow]
    next_start_id: int


def _get_weight_class_matches_for_sql(
    start_id: int,
    weight_class: WeightClass,
    bracket_id: int,
    team_competitor_by_info: dict[CompetitorTuple, int],
) -> MappedMatches:
    match_rows: list[MatchRow] = []
    current_id = start_id

    for match in weight_class.matches:
        top_win = match.top_win
        if top_win is None:
            # NOTE: Even bouts with no match may have a bout number, but for
            #       now we do not include them in the database.
            if match.top_competitor is not None or match.bottom_competitor is not None:
                raise RuntimeError("Invalid match", match)
            continue

        top_competitor_id = None
        top_team_acronym = None
        if match.top_competitor is not None:
            key = match.top_competitor.as_tuple
            top_competitor_id = team_competitor_by_info[key]
            top_team_acronym = match.top_competitor.team_acronym

        bottom_competitor_id = None
        bottom_team_acronym = None
        if match.bottom_competitor is not None:
            key = match.bottom_competitor.as_tuple
            bottom_competitor_id = team_competitor_by_info[key]
            bottom_team_acronym = match.bottom_competitor.team_acronym

        match_row = MatchRow(
            id=current_id,
            bracket_id=bracket_id,
            bout_number=match.bout_number,
            match_slot=match.match_slot,
            top_competitor_id=top_competitor_id,
            bottom_competitor_id=bottom_competitor_id,
            top_win=top_win,
            result=match.result,
            result_type=match.result_type,
            top_team_acronym=top_team_acronym,
            bottom_team_acronym=bottom_team_acronym,
        )
        match_rows.append(match_row)

        current_id += 1

    return MappedMatches(match_rows=match_rows, next_start_id=current_id)


def get_matches_for_sql(
    start_id: int,
    weight_classes: list[WeightClass],
    team_competitor_by_info: dict[CompetitorTuple, int],
    bracket_id_mapping: dict[tuple[Division, int], int],
) -> MappedMatches:
    match_rows: list[MatchRow] = []

    for weight_class in weight_classes:
        key = weight_class.division, weight_class.weight
        bracket_id = bracket_id_mapping[key]
        mapped_matches = _get_weight_class_matches_for_sql(
            start_id, weight_class, bracket_id, team_competitor_by_info
        )
        # Prepare for next iteration
        start_id = mapped_matches.next_start_id
        match_rows.extend(mapped_matches.match_rows)

    return MappedMatches(match_rows=match_rows, next_start_id=start_id)


def _sql_nullable_integer(value: int | None) -> str:
    if value is None:
        return "NULL"

    return str(value)


def _sql_boolean(value: bool) -> str:
    if value:
        return "TRUE"

    return "FALSE"


def print_matches_sql(match_rows: list[MatchRow]) -> None:
    for row in match_rows:
        bout_number_str = _sql_nullable_integer(row.bout_number)
        top_competitor_id_str = _sql_nullable_integer(row.top_competitor_id)
        bottom_competitor_id_str = _sql_nullable_integer(row.bottom_competitor_id)
        top_win_str = _sql_boolean(row.top_win)
        result_str = sql_nullable_str(row.result)
        print(
            f"  ({row.id_}, {row.bracket_id}, {bout_number_str}, "
            f"'{row.match_slot}', {top_competitor_id_str}, {bottom_competitor_id_str}, "
            f"{top_win_str}, {result_str}, '{row.result_type}', "
            f"'{row.top_team_acronym}', '{row.bottom_team_acronym}'),"
        )


def tournament_team_sql(
    start_id: int,
    tournament_id: int,
    team_acronym_mapping: dict[str, str],
    novice_team_acronym_mapping: dict[str, str],
    senior_team_acronym_mapping: dict[str, str],
    team_name_mapping: dict[str, int],
):
    current_id = start_id

    all_division_acronyms = set(team_acronym_mapping.keys())

    novice_acronyms = set(novice_team_acronym_mapping.keys())
    novice_acronyms = novice_acronyms.union(all_division_acronyms)
    for acronym in sorted(novice_acronyms):
        team_name = novice_team_acronym_mapping.get(acronym)
        if team_name is None:
            team_name = team_acronym_mapping[acronym]

        team_id = team_name_mapping[team_name]
        print(
            f"  ({current_id}, {tournament_id}, 'novice', {team_id}, "
            f"{sql_nullable_str(team_name)}, {sql_nullable_str(acronym)}),"
        )
        # Update ID for next iteration
        current_id += 1

    senior_acronyms = set(senior_team_acronym_mapping.keys())
    senior_acronyms = senior_acronyms.union(all_division_acronyms)
    for acronym in sorted(senior_acronyms):
        team_name = senior_team_acronym_mapping.get(acronym)
        if team_name is None:
            team_name = team_acronym_mapping[acronym]

        team_id = team_name_mapping[team_name]
        print(
            f"  ({current_id}, {tournament_id}, 'senior', {team_id}, "
            f"{sql_nullable_str(team_name)}, {sql_nullable_str(acronym)}),"
        )
        # Update ID for next iteration
        current_id += 1


def _get_teams_from_tournament(
    project_root: pathlib.Path, tournament_id: int
) -> dict[str, int]:
    database = project_root / "database-v1" / "ikwf.sqlite"
    with sqlite3.connect(database) as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        cursor.execute(
            _TEAMS_FROM_TOURNAMENT,
            {"tournament_id": tournament_id},
        )
        teams_from_tournament: dict[str, int] = {}
        for row in cursor.fetchall():
            team_name = row["name"]
            team_id = row["team_id"]
            if (
                team_name in teams_from_tournament
                and teams_from_tournament[team_name] != team_id
            ):
                raise RuntimeError("Invariant violation")
            teams_from_tournament[team_name] = team_id

        cursor.close()

    return teams_from_tournament


def print_tournament_team_sql(
    project_root: pathlib.Path,
    start_id: int,
    tournament_id: int,
    team_scores: dict[Division, list[TeamScore]],
    divisions: list[Division],
):
    teams_from_tournament = _get_teams_from_tournament(project_root, tournament_id)

    current_id = start_id
    if set(team_scores.keys()) != set(divisions):
        raise RuntimeError(
            "Invariant violation", set(team_scores.keys()), set(divisions)
        )

    for division in divisions:
        division_team_scores = team_scores[division]
        team_score_map = {
            team_score.team: team_score.acronym for team_score in division_team_scores
        }
        if len(team_score_map) != len(division_team_scores):
            raise RuntimeError("Invariant violation")

        team_names = sorted(team_score_map.keys())
        for team_name in team_names:
            team_id = teams_from_tournament[team_name]
            acronym = team_score_map[team_name]
            print(
                f"  ({current_id}, {tournament_id}, {sql_nullable_str(division)}, "
                f"{team_id}, {sql_nullable_str(team_name)}, "
                f"{sql_nullable_str(acronym)}),"
            )

            # Prepare for next iteration
            current_id += 1


def infer_deductions(team_scores: dict[Division, list[TeamScore]]) -> list[Deduction]:
    negative_scores: dict[str, list[float]] = {}
    for division_team_scores in team_scores.values():
        for team_score in division_team_scores:
            if team_score.score >= 0.0:
                continue

            negative_scores.setdefault(team_score.team, []).append(team_score.score)

    result: list[Deduction] = []
    for team_name, scores in negative_scores.items():
        score = min(scores)  # min() is the **MOST** negative
        num_deductions = -int(score)
        if num_deductions != -score:
            raise NotImplementedError(
                "No handling for non-integer deductions", team_name, score
            )
        if num_deductions <= 0:
            raise ValueError("Deductions should be negative", team_name, score)

        for _ in range(num_deductions):
            result.append(Deduction(team=team_name, reason="", value=-1.0))

    return result
