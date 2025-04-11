SELECT
  s.id AS match_slot_id,
  m.bout_number,
  m.match_slot,
  ----
  c_top.full_name AS top_full_name,
  t_top.name AS top_team,
  m.top_score,
  ----
  c_bottom.full_name AS bottom_full_name,
  t_bottom.name AS bottom_team,
  m.bottom_score,
  ----
  m.top_win,
  m.result
FROM
  match AS m
  INNER JOIN bracket AS b ON b.id = m.bracket_id
  INNER JOIN match_slot AS s ON s.key = m.match_slot
  LEFT JOIN tournament_competitor AS tc_top ON tc_top.id = m.top_competitor_id
  LEFT JOIN team AS t_top ON t_top.id = tc_top.team_id
  LEFT JOIN competitor AS c_top ON c_top.id = tc_top.competitor_id
  LEFT JOIN tournament_competitor AS tc_bottom ON tc_bottom.id = m.bottom_competitor_id
  LEFT JOIN team AS t_bottom ON t_bottom.id = tc_bottom.team_id
  LEFT JOIN competitor AS c_bottom ON c_bottom.id = tc_bottom.competitor_id
WHERE
  b.weight = :weight
  AND b.division = :division
  AND b.tournament_id = :tournament_id
ORDER BY s.id
