-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
    s.id AS match_slot_id,
    m.bout_number,
    m.match_slot,
    ----
    tc_top.full_name AS top_name,
    tt_top.name AS top_team,
    m.top_score,
    ----
    tc_bottom.full_name AS bottom_name,
    tt_bottom.name AS bottom_team,
    m.bottom_score,
    ----
    m.top_win,
    m.result
FROM
    "match" AS m
INNER JOIN bracket AS b ON m.bracket_id = b.id
INNER JOIN match_slot AS s ON m.match_slot = s.key
LEFT JOIN tournament_competitor AS tc_top ON m.top_competitor_id = tc_top.id
LEFT JOIN tournament_team AS tt_top ON tc_top.team_id = tt_top.id
LEFT JOIN
    tournament_competitor AS tc_bottom
    ON m.bottom_competitor_id = tc_bottom.id
LEFT JOIN tournament_team AS tt_bottom ON tc_bottom.team_id = tt_bottom.id
WHERE
    b.weight = :weight
    AND b.division = :division
    AND b.tournament_id = :tournament_id
ORDER BY s.id
