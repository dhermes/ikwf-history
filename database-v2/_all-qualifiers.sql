-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
WITH tournament_qualifier AS (
  SELECT
    m.top_competitor_id AS competitor_id,
    b.division,
    b.weight,
    t.year
  FROM
    match AS m
    INNER JOIN tournament_competitor AS tc ON tc.id = m.top_competitor_id
    INNER JOIN tournament_team AS tt ON tt.id = tc.team_id
    INNER JOIN bracket AS b ON b.id = m.bracket_id
    INNER JOIN tournament AS t ON t.id = b.tournament_id
  WHERE
    tt.team_id = :team_id
  ----------------------------------------
  UNION
  ----------------------------------------
  SELECT
    m.bottom_competitor_id AS competitor_id,
    b.division,
    b.weight,
    t.year
  FROM
    match AS m
    INNER JOIN tournament_competitor AS tc ON tc.id = m.bottom_competitor_id
    INNER JOIN tournament_team AS tt ON tt.id = tc.team_id
    INNER JOIN bracket AS b ON b.id = m.bracket_id
    INNER JOIN tournament AS t ON t.id = b.tournament_id
  WHERE
    tt.team_id = :team_id
)

SELECT
  tq.competitor_id,
  tq.year,
  tq.division,
  tq.weight,
  tc.full_name
FROM
  tournament_competitor AS tc
  INNER JOIN tournament_qualifier AS tq ON tq.competitor_id = tc.id
  INNER JOIN division AS d ON d.key = tq.division
ORDER BY tq.year, d.id, tq.weight, tc.full_name, tc.id;
