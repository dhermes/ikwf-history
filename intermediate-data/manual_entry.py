# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Literal

import bracket_utils
import pydantic

WrestlerID = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
]
MatchID = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    52,
    53,
    54,
    1001,
    1003,
    1005,
]
_EXTRA_MATCH_IDS = (1001, 1003, 1005)


class _ForbidExtra(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class WrestlerChoice(_ForbidExtra):
    id_: WrestlerID = pydantic.Field(alias="id")
    name: str
    team: str


class MatchPosition(_ForbidExtra):
    choice: WrestlerID | None
    choices: list[WrestlerID]


class ManualMatch(_ForbidExtra):
    top: MatchPosition
    bottom: MatchPosition
    winner: bracket_utils.BracketPosition | None
    bout_number: int | None = pydantic.Field(alias="boutNumber")
    result: str

    def top_win(self) -> bool | None:
        if self.winner is None:
            return None

        if self.winner == "top":
            return True

        if self.winner == "bottom":
            return False

        raise NotImplementedError(self.winner)


def _description_division(division_text: str) -> bracket_utils.Division:
    if division_text == "Senior":
        return "senior"

    if division_text == "Novice":
        return "novice"

    raise NotImplementedError(division_text)


def _parse_description(
    description: str | None,
) -> tuple[int, bracket_utils.Division, int]:
    """
    Parse text like `Senior 99 (1991)`
    """
    if description is None:
        raise ValueError("Cannot parse description", description)

    parts = description.split()
    if len(parts) != 3:
        raise ValueError("Cannot parse description", description)

    division = _description_division(parts[0])
    weight = int(parts[1])

    year_str = parts[2]
    if not year_str.startswith("(") or not year_str.endswith(")"):
        raise ValueError("Cannot parse description", description)

    year = int(year_str[1:-1])

    return year, division, weight


def _get_match_slot_from_id(match_slot_id: int) -> bracket_utils.MatchSlot:
    if match_slot_id == 1:
        return "championship_r32_01"

    if match_slot_id == 2:
        return "championship_r32_02"

    if match_slot_id == 3:
        return "championship_r32_03"

    if match_slot_id == 4:
        return "championship_r32_04"

    if match_slot_id == 5:
        return "championship_r32_05"

    if match_slot_id == 6:
        return "championship_r32_06"

    if match_slot_id == 7:
        return "championship_r32_07"

    if match_slot_id == 8:
        return "championship_r32_08"

    if match_slot_id == 9:
        return "championship_r32_09"

    if match_slot_id == 10:
        return "championship_r32_10"

    if match_slot_id == 11:
        return "championship_r32_11"

    if match_slot_id == 12:
        return "championship_r32_12"

    if match_slot_id == 13:
        return "championship_r32_13"

    if match_slot_id == 14:
        return "championship_r32_14"

    if match_slot_id == 15:
        return "championship_r32_15"

    if match_slot_id == 16:
        return "championship_r32_16"

    if match_slot_id == 17:
        return "championship_r16_01"

    if match_slot_id == 18:
        return "championship_r16_02"

    if match_slot_id == 19:
        return "championship_r16_03"

    if match_slot_id == 20:
        return "championship_r16_04"

    if match_slot_id == 21:
        return "championship_r16_05"

    if match_slot_id == 22:
        return "championship_r16_06"

    if match_slot_id == 23:
        return "championship_r16_07"

    if match_slot_id == 24:
        return "championship_r16_08"

    if match_slot_id == 25:
        return "consolation_round2_01"

    if match_slot_id == 26:
        return "consolation_round2_02"

    if match_slot_id == 27:
        return "consolation_round2_03"

    if match_slot_id == 28:
        return "consolation_round2_04"

    if match_slot_id == 29:
        return "consolation_round2_05"

    if match_slot_id == 30:
        return "consolation_round2_06"

    if match_slot_id == 31:
        return "consolation_round2_07"

    if match_slot_id == 32:
        return "consolation_round2_08"

    if match_slot_id == 33:
        return "championship_quarter_01"

    if match_slot_id == 34:
        return "championship_quarter_02"

    if match_slot_id == 35:
        return "championship_quarter_03"

    if match_slot_id == 36:
        return "championship_quarter_04"

    if match_slot_id == 37:
        return "consolation_round3_01"

    if match_slot_id == 38:
        return "consolation_round3_02"

    if match_slot_id == 39:
        return "consolation_round3_03"

    if match_slot_id == 40:
        return "consolation_round3_04"

    if match_slot_id == 41:
        return "consolation_round4_blood_01"

    if match_slot_id == 42:
        return "consolation_round4_blood_02"

    if match_slot_id == 43:
        return "consolation_round4_blood_03"

    if match_slot_id == 44:
        return "consolation_round4_blood_04"

    if match_slot_id == 45:
        return "championship_semi_01"

    if match_slot_id == 46:
        return "championship_semi_02"

    if match_slot_id == 47:
        return "consolation_round5_01"

    if match_slot_id == 48:
        return "consolation_round5_02"

    if match_slot_id == 49:
        return "consolation_round6_semi_01"

    if match_slot_id == 50:
        return "consolation_round6_semi_02"

    if match_slot_id == 51:
        return "consolation_seventh_place"

    if match_slot_id == 52:
        return "consolation_fifth_place"

    if match_slot_id == 53:
        return "consolation_third_place"

    if match_slot_id == 54:
        return "championship_first_place"

    raise NotImplementedError(match_slot_id)


class ManualBracket(_ForbidExtra):
    description: str | None
    wrestler_choices: list[WrestlerChoice | None] = pydantic.Field(
        alias="wrestlerChoices"
    )
    matches: dict[MatchID, ManualMatch]

    @pydantic.field_validator("matches", mode="before")
    @classmethod
    def convert_keys(cls, matches_value):
        return {int(key): value for key, value in matches_value.items()}

    def _to_competitor_raw(
        self, wrestler_id: WrestlerID | None
    ) -> bracket_utils.CompetitorRaw | None:
        if wrestler_id is None:
            return None

        wrestler_choice = self.wrestler_choices[wrestler_id]
        return bracket_utils.CompetitorRaw(
            name=wrestler_choice.name,
            team_full=wrestler_choice.team,
            team_acronym=None,
        )

    def to_weight_class(
        self,
        year: int,
        name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
    ) -> bracket_utils.WeightClass:
        actual_year, division, weight = _parse_description(self.description)
        if actual_year != year:
            raise ValueError("Mismatched description", year, self.description)

        raw_matches: list[bracket_utils.MatchRaw] = []
        match_ids = sorted(self.matches.keys())
        for match_id in match_ids:
            if match_id in _EXTRA_MATCH_IDS:
                continue

            manual_match = self.matches[match_id]

            match_slot = _get_match_slot_from_id(match_id)
            top_competitor_raw = self._to_competitor_raw(manual_match.top.choice)
            bottom_competitor_raw = self._to_competitor_raw(manual_match.bottom.choice)

            top_win = manual_match.top_win()
            if top_win is None:
                winner = None
            elif top_win:
                winner = top_competitor_raw
            else:
                winner = bottom_competitor_raw

            match_raw = bracket_utils.MatchRaw(
                match_slot=match_slot,
                top_competitor=top_competitor_raw,
                bottom_competitor=bottom_competitor_raw,
                result=manual_match.result or "unknown",
                bout_number=manual_match.bout_number,
                winner=winner,
                winner_from=None,
            )
            raw_matches.append(match_raw)

        matches = bracket_utils.clean_raw_matches(raw_matches, name_exceptions)
        for match in matches:
            if match.result == "unknown":
                match.result = ""

        return bracket_utils.WeightClass(
            division=division, weight=weight, matches=matches
        )


def load_manual_entries(
    root: pathlib.Path,
    year: int,
    name_exceptions: dict[tuple[str, str], bracket_utils.Competitor],
) -> list[bracket_utils.WeightClass]:
    year_raw = root / "raw-data" / str(year)

    weight_classes: list[bracket_utils.WeightClass] = []
    for path in year_raw.glob("manual-entry-*.json"):
        with open(path) as file_obj:
            manual_bracket = ManualBracket.model_validate_json(file_obj.read())

        weight_class = manual_bracket.to_weight_class(year, name_exceptions)
        weight_classes.append(weight_class)

    return weight_classes
