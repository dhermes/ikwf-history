-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
    tt.id,
    tt.tournament_id,
    tt.division,
    tt.name,
    tt.team_id,
    t.name_normalized
FROM
    tournament_team AS tt
    INNER JOIN team AS t ON tt.team_id = t.id
WHERE
    NOT t.verified
ORDER BY tt.id
