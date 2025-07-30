# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

from typing import Literal, NamedTuple

import pydantic


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class CompetitorRaw(_ForbidExtra):
    name: str
    team_full: str

    @property
    def long_name(self) -> str:
        return f"{self.name} ({self.team_full})"


class CompetitorTuple(NamedTuple):
    first_name: str
    last_name: str
    team_full: str


class Competitor(_ForbidExtra):
    full_name: str
    first_name: str
    last_name: str
    team_full: str

    @property
    def as_tuple(self) -> CompetitorTuple:
        """Convert to a (hashable) tuple."""
        return CompetitorTuple(
            first_name=self.first_name,
            last_name=self.last_name,
            team_full=self.team_full,
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


def _get_match_slot_id(match_slot: MatchSlot) -> int:
    if match_slot == "championship_r32_01":
        return 1

    if match_slot == "championship_r32_02":
        return 2

    if match_slot == "championship_r32_03":
        return 3

    if match_slot == "championship_r32_04":
        return 4

    if match_slot == "championship_r32_05":
        return 5

    if match_slot == "championship_r32_06":
        return 6

    if match_slot == "championship_r32_07":
        return 7

    if match_slot == "championship_r32_08":
        return 8

    if match_slot == "championship_r32_09":
        return 9

    if match_slot == "championship_r32_10":
        return 10

    if match_slot == "championship_r32_11":
        return 11

    if match_slot == "championship_r32_12":
        return 12

    if match_slot == "championship_r32_13":
        return 13

    if match_slot == "championship_r32_14":
        return 14

    if match_slot == "championship_r32_15":
        return 15

    if match_slot == "championship_r32_16":
        return 16

    if match_slot == "championship_r16_01":
        return 17

    if match_slot == "championship_r16_02":
        return 18

    if match_slot == "championship_r16_03":
        return 19

    if match_slot == "championship_r16_04":
        return 20

    if match_slot == "championship_r16_05":
        return 21

    if match_slot == "championship_r16_06":
        return 22

    if match_slot == "championship_r16_07":
        return 23

    if match_slot == "championship_r16_08":
        return 24

    if match_slot == "consolation_round2_01":
        return 25

    if match_slot == "consolation_round2_02":
        return 26

    if match_slot == "consolation_round2_03":
        return 27

    if match_slot == "consolation_round2_04":
        return 28

    if match_slot == "consolation_round2_05":
        return 29

    if match_slot == "consolation_round2_06":
        return 30

    if match_slot == "consolation_round2_07":
        return 31

    if match_slot == "consolation_round2_08":
        return 32

    if match_slot == "championship_quarter_01":
        return 33

    if match_slot == "championship_quarter_02":
        return 34

    if match_slot == "championship_quarter_03":
        return 35

    if match_slot == "championship_quarter_04":
        return 36

    if match_slot == "consolation_round3_01":
        return 37

    if match_slot == "consolation_round3_02":
        return 38

    if match_slot == "consolation_round3_03":
        return 39

    if match_slot == "consolation_round3_04":
        return 40

    if match_slot == "consolation_round4_blood_01":
        return 41

    if match_slot == "consolation_round4_blood_02":
        return 42

    if match_slot == "consolation_round4_blood_03":
        return 43

    if match_slot == "consolation_round4_blood_04":
        return 44

    if match_slot == "championship_semi_01":
        return 45

    if match_slot == "championship_semi_02":
        return 46

    if match_slot == "consolation_round5_01":
        return 47

    if match_slot == "consolation_round5_02":
        return 48

    if match_slot == "consolation_round6_semi_01":
        return 49

    if match_slot == "consolation_round6_semi_02":
        return 50

    if match_slot == "consolation_seventh_place":
        return 51

    if match_slot == "consolation_fifth_place":
        return 52

    if match_slot == "consolation_third_place":
        return 53

    if match_slot == "championship_first_place":
        return 54

    raise NotImplementedError(match_slot)


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
    "unknown",
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
    "junior_iwf",
    "novice_iwf",
    "senior_iwf",
]


def _match_sort_key(match: Match) -> int:
    return _get_match_slot_id(match.match_slot)


class WeightClass(_ForbidExtra):
    division: Division
    weight: int
    matches: list[Match]

    def _validate(self):
        all_slots: set[MatchSlot] = set()
        for match in self.matches:
            if match.match_slot in all_slots:
                raise ValueError(
                    "Slot already exists in weight",
                    self.division,
                    self.weight,
                    match.match_slot,
                )

            all_slots.add(match.match_slot)

    def _sort(self) -> None:
        self.matches.sort(key=_match_sort_key)


class TeamScore(_ForbidExtra):
    team: str
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
        for weight_class in self.weight_classes:
            weight_class._sort()

    def _sort_team_scores(self):
        divisions = sorted(self.team_scores.keys(), key=_division_sort_key)
        ordered = {
            division: sorted(self.team_scores[division], key=_team_score_sort_key)
            for division in divisions
        }
        self.team_scores = ordered

    def _sort_deductions(self):
        self.deductions.sort(key=_deduction_sort_key)

    def _validate_weight_classes(self):
        all_weights: set[tuple[Division, int]] = set()
        for weight_class in self.weight_classes:
            weight_key = weight_class.division, weight_class.weight
            if weight_key in all_weights:
                raise ValueError(
                    "Weight already exists in tournament",
                    weight_class.division,
                    weight_class.weight,
                )

            all_weights.add(weight_key)
            weight_class._validate()

    def sort(self):
        self._sort_weight_classes()
        self._sort_team_scores()
        self._sort_deductions()
        self._validate_weight_classes()


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

    exception_key = value.name, value.team_full
    if exception_key in name_exceptions:
        competitor = name_exceptions[exception_key]
        competitor.full_name = value.name
        return competitor

    parts = value.name.split()
    if len(parts) != 2:
        raise RuntimeError(value.name, value.team_full)

    return Competitor(
        full_name=value.name,
        first_name=parts[0],
        last_name=parts[1],
        team_full=value.team_full,
    )


def _competitor_equal_enough(competitor1: Competitor, competitor2: Competitor) -> bool:
    if competitor1.team_full != competitor2.team_full:
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

    return _competitor_name_equal_enough(competitor1.name, competitor2.name)


def _ensure_overtime_decision(result: str, prefix: str) -> None:
    without_prefix = result[len(prefix) :]
    score1_str, score2_str = without_prefix.split("-")
    score1 = int(score1_str)
    score2 = int(score2_str)
    delta = abs(score1 - score2)
    if delta >= 8:
        raise ValueError("OT match is not a Decision", result)


def _determine_result_type(result: str) -> ResultType:
    if result == "P-Dec" or result.startswith("P-Dec "):
        return "walkover"

    if result == "PD" or result.startswith("PD "):
        return "walkover"

    if result == "Dec" or result.startswith("Dec "):
        return "decision"

    if result.startswith("OT "):
        _ensure_overtime_decision(result, "OT ")
        return "decision"

    if (
        result.startswith("MajDec ")
        or result.startswith("M-Dec ")
        or result == "Maj Dec"
        or result.startswith("Maj Dec ")
        or result.startswith("MD ")
    ):
        return "major"

    if result == "T-Fall" or result.startswith("T-Fall "):
        return "tech"

    if result == "TF" or result.startswith("TF "):
        return "tech"

    if result == "Fall" or result.startswith("Fall "):
        return "fall"

    if result == "Bye":
        return "bye"

    if result == "Dflt" or result.startswith("Dflt ") or result.startswith("Df "):
        return "default"

    if result == "Default":
        return "default"

    if (
        result == "Dq"
        or result.startswith("Dq ")
        or result == "DQ"
        or result.startswith("DQ ")
    ):
        return "disqualification"

    if (
        result == "Forf"
        or result.startswith("Forf ")
        or result == "Ff"
        or result.startswith("Ff ")
        or result == "FF"
    ):
        return "forfeit"

    if result == "unknown":
        return "unknown"

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
        winner_team = match.top_competitor.team_full
        if match.bottom_competitor is not None:
            loser_team = match.bottom_competitor.team_full
    else:
        winner = match.bottom_competitor
        winner_team = match.bottom_competitor.team_full
        if match.top_competitor is not None:
            loser_team = match.top_competitor.team_full

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
        for team, score in match_updates.items():
            result.setdefault(team, 0.0)
            result[team] += score

    return result


def compute_team_scores(weight_classes: list[WeightClass]) -> dict[str, float]:
    result: dict[str, float] = {}
    for weight_class in weight_classes:
        weight_updates = _weight_team_score_updates(weight_class)
        for team, score in weight_updates.items():
            result.setdefault(team, 0.0)
            result[team] += score

    return result


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


class Placer(NamedTuple):
    """Very basic form of `Competitor`.

    Used to process brackets where we have a list of placers but not full
    brackets.
    """

    name: str
    team: str

    def to_competitor(self, team_replace: dict[str, str]) -> Competitor:
        team_full = team_replace.get(self.team, self.team)
        parts = self.name.split()
        if len(parts) != 2:
            raise NotImplementedError(self.name)

        first_name = parts[0]
        last_name = parts[1]
        return Competitor(
            full_name=self.name,
            first_name=first_name,
            last_name=last_name,
            team_full=team_full,
        )


def create_weight_class_from_placers(
    division: Division,
    weight: int,
    placers: list[Placer],
    team_replace: dict[str, str],
) -> WeightClass:
    if len(placers) != 6:
        raise RuntimeError("Invalid placers", division, weight)

    matches: list[Match] = [
        Match(
            match_slot="championship_first_place",
            top_competitor=placers[0].to_competitor(team_replace),
            bottom_competitor=placers[1].to_competitor(team_replace),
            result="",
            result_type="unknown",
            bout_number=None,
            top_win=True,
        ),
        Match(
            match_slot="consolation_third_place",
            top_competitor=placers[2].to_competitor(team_replace),
            bottom_competitor=placers[3].to_competitor(team_replace),
            result="",
            result_type="unknown",
            bout_number=None,
            top_win=True,
        ),
        Match(
            match_slot="consolation_fifth_place",
            top_competitor=placers[4].to_competitor(team_replace),
            bottom_competitor=placers[5].to_competitor(team_replace),
            result="",
            result_type="unknown",
            bout_number=None,
            top_win=True,
        ),
    ]

    return WeightClass(division=division, weight=weight, matches=matches)


def weight_class_from_champ(
    division: Division, weight: int, champ: Placer, team_replace: dict[str, str]
) -> WeightClass:
    return WeightClass(
        division=division,
        weight=weight,
        matches=[
            Match(
                match_slot="championship_first_place",
                top_competitor=champ.to_competitor(team_replace),
                bottom_competitor=None,
                result="",
                result_type="unknown",
                bout_number=None,
                top_win=True,
            ),
        ],
    )


def _placing_competitor_from_str(
    value: str | None, team_replace: dict[str, str]
) -> tuple[CompetitorRaw | None, int | None]:
    if value is None:
        return None, None

    # Values of the form:
    #   {NAME} :: {TEAM}
    # or
    #   {NAME} :: {TEAM} :: {PLACE}
    parts = value.split(" :: ")
    if len(parts) == 2:
        name, team = parts
        place = None
    elif len(parts) == 3:
        name, team, place_str = parts
        place = int(place_str)
    else:
        raise ValueError("Unexpected format", value)

    team_full = team_replace.get(team, team)
    competitor_raw = CompetitorRaw(name=name, team_full=team_full)
    return competitor_raw, place


def weight_class_from_competitors(
    division: Division,
    weight: int,
    competitors: list[str | None],
    team_replace: dict[str, str],
    name_exceptions: dict[tuple[str, str], Competitor],
    bout_numbers: dict[MatchSlot, int],
    *,
    placers_type: Literal["champ", "top6"] = "top6",
) -> WeightClass:
    if len(competitors) != 24:
        raise NotImplementedError("Unsupported bracket size", weight, len(competitors))

    champion_position: BracketPosition = "top"
    placers: dict[int, Competitor] = {}
    matches: list[Match] = []

    for i in range(8):
        match_id = 2 * i + 1
        match_slot: MatchSlot = f"championship_r32_{match_id:02}"

        competitor_str = competitors[3 * i]
        competitor_raw, place = _placing_competitor_from_str(
            competitor_str, team_replace
        )
        if competitor_raw is None:
            continue

        competitor = competitor_from_raw(competitor_raw, name_exceptions)

        if place is not None:
            placers[place] = competitor
            if place == 1 and i >= 4:
                champion_position = "bottom"

        matches.append(
            Match(
                match_slot=match_slot,
                top_competitor=competitor,
                bottom_competitor=None,
                result="Bye",
                result_type="bye",
                bout_number=bout_numbers.get(match_slot),
                top_win=True,
            )
        )

    for i in range(8):
        match_id = 2 * i + 2
        match_slot: MatchSlot = f"championship_r32_{match_id:02}"

        competitor1_str = competitors[3 * i + 1]
        competitor2_str = competitors[3 * i + 2]
        if competitor1_str is None and competitor2_str is None:
            continue

        competitor1_raw, place1 = _placing_competitor_from_str(
            competitor1_str, team_replace
        )
        competitor1 = competitor_from_raw(competitor1_raw, name_exceptions)

        competitor2_raw, place2 = _placing_competitor_from_str(
            competitor2_str, team_replace
        )
        competitor2 = competitor_from_raw(competitor2_raw, name_exceptions)

        if place1 is not None:
            placers[place1] = competitor1
            if place1 == 1 and i >= 4:
                champion_position = "bottom"

        if place2 is not None:
            placers[place2] = competitor2
            if place2 == 1 and i >= 4:
                champion_position = "bottom"

        matches.append(
            Match(
                match_slot=match_slot,
                top_competitor=competitor1,
                bottom_competitor=competitor2,
                result="",
                result_type="unknown",
                bout_number=bout_numbers.get(match_slot, i + 1),
                top_win=None,
            )
        )

    if placers_type == "top6":
        if placers.keys() != {1, 2, 3, 4, 5, 6}:
            raise ValueError("Missing placers", weight, division, placers.keys())

        matches.extend(
            [
                Match(
                    match_slot="consolation_third_place",
                    top_competitor=placers[3],
                    bottom_competitor=placers[4],
                    result="",
                    result_type="unknown",
                    bout_number=bout_numbers.get("consolation_third_place"),
                    top_win=True,
                ),
                Match(
                    match_slot="consolation_fifth_place",
                    top_competitor=placers[5],
                    bottom_competitor=placers[6],
                    result="",
                    result_type="unknown",
                    bout_number=bout_numbers.get("consolation_fifth_place"),
                    top_win=True,
                ),
            ]
        )

        top_competitor = placers[1]
        bottom_competitor = placers[2]
        top_win = True
        if champion_position == "bottom":
            top_competitor, bottom_competitor = bottom_competitor, top_competitor
            top_win = False

        matches.append(
            Match(
                match_slot="championship_first_place",
                top_competitor=top_competitor,
                bottom_competitor=bottom_competitor,
                result="",
                result_type="unknown",
                bout_number=bout_numbers.get("championship_first_place"),
                top_win=top_win,
            )
        )
    elif placers_type == "champ":
        if placers.keys() != {1}:
            raise ValueError("Missing placers", weight, division, placers.keys())

        top_competitor = placers[1]
        top_win = True
        matches.append(
            Match(
                match_slot="championship_first_place",
                top_competitor=top_competitor,
                bottom_competitor=None,
                result="",
                result_type="unknown",
                bout_number=bout_numbers.get("championship_first_place"),
                top_win=top_win,
            )
        )
    else:
        raise NotImplementedError(placers_type)

    return WeightClass(division=division, weight=weight, matches=matches)
