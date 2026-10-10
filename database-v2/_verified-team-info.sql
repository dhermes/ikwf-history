-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

WITH team_synonym AS (
    SELECT DISTINCT
        tt.team_id,
        tt.name
    FROM
        tournament_team AS tt
    ORDER BY tt.team_id, tt.name
)

SELECT
    t.id,
    t.name_normalized,
    t.url_path_slug,
    JSON_GROUP_ARRAY(ts.name) AS synonyms_json
FROM
    team AS t
INNER JOIN team_synonym AS ts ON t.id = ts.team_id
WHERE
    t.verified
GROUP BY t.id
ORDER BY t.name_normalized, t.id
