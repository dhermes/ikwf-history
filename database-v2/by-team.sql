WITH top_and_bottom AS (
    SELECT
        b.division,
        b.weight,
        ms.id AS match_id,
        tc.full_name,
        tt.name AS team_name,
        1 AS top_bottom
    FROM
        bracket AS b
    INNER JOIN `match` AS m ON b.id = m.bracket_id
    INNER JOIN match_slot AS ms ON m.match_slot = ms.key
    INNER JOIN tournament_competitor AS tc ON m.top_competitor_id = tc.id
    INNER JOIN tournament_team AS tt ON tc.team_id = tt.id
    WHERE
        b.tournament_id = 31
        AND ms.id BETWEEN 1 AND 16
    ----------------
    UNION ALL
    ----------------
    SELECT
        b.division,
        b.weight,
        ms.id AS match_id,
        tc.full_name,
        tt.name AS team_name,
        2 AS top_bottom
    FROM
        bracket AS b
    INNER JOIN `match` AS m ON b.id = m.bracket_id
    INNER JOIN match_slot AS ms ON m.match_slot = ms.key
    INNER JOIN tournament_competitor AS tc ON m.bottom_competitor_id = tc.id
    INNER JOIN tournament_team AS tt ON tc.team_id = tt.id
    WHERE
        b.tournament_id = 31
        AND ms.id BETWEEN 1 AND 16
)

SELECT
    division,
    team_name,
    weight,
    full_name
FROM
    top_and_bottom
ORDER BY
    division, team_name, weight;
