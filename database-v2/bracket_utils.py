# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

from typing import Literal

import pydantic


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


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


Division = Literal[
    "bantam",
    "intermediate",
    "novice",
    "senior",
    "novice_iwf",
    "senior_iwf",
    "bantam_girls",
    "intermediate_girls",
    "novice_girls",
    "senior_girls",
]


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
]


class Competitor(_ForbidExtra):
    full_name: str
    first_name: str
    last_name: str
    suffix: str | None
    team: str


class Match(_ForbidExtra):
    match_slot: MatchSlot
    top_competitor: Competitor | None
    bottom_competitor: Competitor | None
    result: str
    result_type: ResultType
    bout_number: int | None
    top_win: bool | None


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


class ExtractedTournament(_ForbidExtra):
    weight_classes: list[WeightClass]
    team_scores: dict[Division, list[TeamScore]]
    deductions: list[Deduction]
