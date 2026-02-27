import bracket_utils
import write_bracket_html

_WEIGHTS: dict[bracket_utils.Division, tuple[int, ...]] = {
    "bantam": (43, 46, 49, 52, 55, 58, 62, 66, 70, 76, 84, 95, 120),
    "intermediate": (55, 59, 64, 69, 74, 79, 84, 90, 98, 108, 122, 148, 177),
    "novice": (60, 64, 69, 74, 80, 86, 93, 100, 108, 116, 125, 134, 154, 178, 215),
    "senior": (
        74,
        79,
        84,
        90,
        96,
        103,
        110,
        118,
        126,
        135,
        144,
        154,
        164,
        176,
        188,
        215,
        275,
    ),
    "bantam_girls": (45, 50, 55, 61, 67, 74, 85, 95, 115),
    "intermediate_girls": (53, 57, 62, 67, 72, 77, 82, 88, 95, 115, 135),
    "novice_girls": (63, 68, 74, 80, 85, 90, 96, 102, 108, 115, 125, 140, 185),
    "senior_girls": (
        75,
        80,
        85,
        90,
        95,
        100,
        105,
        110,
        115,
        120,
        125,
        130,
        135,
        145,
        185,
        240,
    ),
}


def main() -> None:
    static_root = write_bracket_html.HERE.parent / "static" / "static"
    dummy_match = write_bracket_html.MatchData(
        match_slot_id=1,
        match_slot="championship_r32_01",
        top_name="Ben Davino",
        top_team="Team USA",
        bottom_name=None,
        bottom_team=None,
        bout_number=None,
        top_score=None,
        bottom_score=None,
        top_win=True,
        result="Bye",
    )
    dummy_match_girls = write_bracket_html.MatchData(
        match_slot_id=1,
        match_slot="championship_r32_01",
        top_name="Kennedy Blades",
        top_team="Team USA",
        bottom_name=None,
        bottom_team=None,
        bout_number=None,
        top_score=None,
        bottom_score=None,
        top_win=True,
        result="Bye",
    )
    for division, weights in _WEIGHTS.items():
        if division.endswith("_girls"):
            match_data_rows = [dummy_match_girls]
        else:
            match_data_rows = [dummy_match]
        for weight in weights:
            config = write_bracket_html.TournamentConfig(
                id=54, year=2026, wrestleback_type="full", medalist_count=8
            )
            write_bracket_html._render_bracket_html(
                static_root,
                config,
                division,
                weight,
                match_data_rows,
                _hazmat_skip_backside=True,
            )

    write_bracket_html._render_brackets_year_html(static_root, 2026, _WEIGHTS)


if __name__ == "__main__":
    main()


# TODO: Back button on the page

# JS TO HELP FILTERING ALL athlete rows
# function involvesSectional(tr, allowedSectionals) {
#   return allowedSectionals.includes(tr.dataset.sectional);
# }

# JS TO HELP FILTERING ALL head to head rows
# function involvesOnlySectionals(tr, allowedSectionals) {
#   const tds = tr.querySelectorAll("td[data-sectional]");
#
#   // Must have exactly 2 (winner + loser)
#   if (tds.length !== 2) {
#     return false;
#   }
#
#   return Array.from(tds).every(td =>
#     allowedSectionals.includes(td.dataset.sectional)
#   );
# }
