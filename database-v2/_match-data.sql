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
  match AS m
  INNER JOIN bracket AS b ON b.id = m.bracket_id
  INNER JOIN match_slot AS s ON s.key = m.match_slot
  LEFT JOIN tournament_competitor AS tc_top ON tc_top.id = m.top_competitor_id
  LEFT JOIN tournament_team AS tt_top ON tt_top.id = tc_top.team_id
  LEFT JOIN tournament_competitor AS tc_bottom ON tc_bottom.id = m.bottom_competitor_id
  LEFT JOIN tournament_team AS tt_bottom ON tt_bottom.id = tc_bottom.team_id
WHERE
  b.weight = :weight
  AND b.division = :division
  AND b.tournament_id = :tournament_id
ORDER BY s.id
