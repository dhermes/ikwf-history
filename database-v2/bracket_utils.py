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
    "bantam_girls",
    "intermediate_girls",
    "novice_girls",
    "senior_girls",
    "junior_iwf",
    "novice_iwf",
    "senior_iwf",
]


def division_sort_key(division: Division) -> int:
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


class Competitor(_ForbidExtra):
    full_name: str
    first_name: str
    last_name: str
    team_full: str
    team_acronym: str | None


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


WeightClassesByDivision = dict[Division, tuple[int, ...]]
WeightClassesByTournament = dict[int, WeightClassesByDivision]


class WeightClassesByYear(pydantic.RootModel[dict[int, WeightClassesByTournament]]):
    pass


TournamentFilename = dict[int, str]


class FilenamesByYear(pydantic.RootModel[dict[int, TournamentFilename]]):
    pass


class TeamNameSynonym(_ForbidExtra):
    name: str
    synonym: str


class TeamNameSynonyms(pydantic.RootModel[dict[int, list[TeamNameSynonym]]]):
    pass


def get_match_slot_id(match_slot: MatchSlot) -> int:
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


class TeamDuplicate(_ForbidExtra):
    tournament_id: int
    division: Division
    name: str

    def to_tuple(self) -> tuple[int, Division, str]:
        return self.tournament_id, self.division, self.name


class TeamDuplicates(pydantic.RootModel[dict[str, list[TeamDuplicate]]]):
    pass


def get_division_display(division: Division) -> str:
    if division == "bantam":
        return "Bantam"

    if division == "intermediate":
        return "Intermediate"

    if division == "novice":
        return "Novice"

    if division == "senior":
        return "Senior"

    if division == "bantam_girls":
        return "Girls Bantam"

    if division == "intermediate_girls":
        return "Girls Intermediate"

    if division == "novice_girls":
        return "Girls Novice"

    if division == "senior_girls":
        return "Girls Senior"

    raise NotImplementedError(division)


def get_division_path(division: Division) -> str:
    """Get division fragment for use in file and URL paths"""
    if division == "bantam":
        return "bantam"

    if division == "intermediate":
        return "intermediate"

    if division == "novice":
        return "novice"

    if division == "senior":
        return "senior"

    if division == "bantam_girls":
        return "bantam-girls"

    if division == "intermediate_girls":
        return "intermediate-girls"

    if division == "novice_girls":
        return "novice-girls"

    if division == "senior_girls":
        return "senior-girls"

    raise NotImplementedError(division)
