# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

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


class ManualBracket(_ForbidExtra):
    description: str | None
    wrestler_choices: list[WrestlerChoice] = pydantic.Field(alias="wrestlerChoices")
    matches: dict[MatchID, ManualMatch]

    @pydantic.field_validator("matches", mode="before")
    @classmethod
    def convert_keys(cls, matches_value):
        return {int(key): value for key, value in matches_value.items()}
