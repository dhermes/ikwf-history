# Copyright (c) 2026 - Present. IKWF History. All rights reserved.

import pathlib
from typing import Any

import bracket_utils
import usabracketing

_HERE = pathlib.Path(__file__).resolve().parent
_NAME_FIXES: dict[str, str] = {}
_NAME_EXCEPTIONS: dict[tuple[str, str], bracket_utils.Competitor] = {}
_TEAM_FIXES: dict[str, tuple[str, str]] = {}


def _parse_rounds(
    selenium_rounds: Any,
    match_slots_by_bracket: usabracketing.MatchSlotsByBracket,
) -> list[usabracketing.MatchWithBracket]:
    if not isinstance(selenium_rounds, dict):
        raise TypeError("Unexpected value", type(selenium_rounds))

    matches: list[usabracketing.MatchWithBracket] = []

    matches.extend(
        usabracketing.parse_r32(
            "Championship First Round",
            "Champ. Round 1",
            selenium_rounds,
            match_slots_by_bracket,
            _NAME_EXCEPTIONS,
            "v3",
        )
    )

    raise NotImplementedError

    # matches.extend(
    #     usabracketing.parse_r16(
    #         "Championship Second Round",
    #         "Champ. Round 2",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #         "v3",
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_consolation_round2(
    #         "Consolation Second Round",
    #         "Cons. Round 2",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_quarterfinal_mixed(
    #         "Champ Quarters & Consolation 3rd Round",
    #         "Quarterfinal",
    #         "Cons. Round 3",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #         "v3",
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_consolation_round4(
    #         "Consolation 4th Round",
    #         "Cons. Round 4",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_semi_mixed(
    #         "Champ Semis & Consolation 5th Round",
    #         "Semifinal",
    #         "Cons. Round 5",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #         "v3",
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_consolation_semi(
    #         "Consolation Semifinal",
    #         "Cons. Semi",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #         "v3",
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_place_matches_v2(
    #         "3rd, 5th, & 7th Place Bouts",
    #         "3rd Place Match",
    #         "5th Place Match",
    #         "7th Place Match",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #     )
    # )

    # matches.extend(
    #     usabracketing.parse_championship_matches(
    #         "Championship Bouts",
    #         "1st Place Match",
    #         selenium_rounds,
    #         match_slots_by_bracket,
    #         _NAME_EXCEPTIONS,
    #     )
    # )

    # if selenium_rounds:
    #     raise ValueError("Round not processed", selenium_rounds.keys())

    # return matches


def main() -> None:
    root = _HERE.parent / "raw-data" / "2026"
    extracted_tournament = usabracketing.extract_year(
        root,
        _parse_rounds,
        "Championship Round 1",
        "Champ. Rd of 32",
        _NAME_FIXES,
        _TEAM_FIXES,
    )
    print(extracted_tournament)
    # extracted_tournament.sort()
    # with open(_HERE / "extracted.2026.json", "w") as file_obj:
    #     file_obj.write(extracted_tournament.model_dump_json(indent=2))
    #     file_obj.write("\n")


if __name__ == "__main__":
    main()
