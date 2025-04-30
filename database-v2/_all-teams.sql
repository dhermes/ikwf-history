-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
    t.id,
    t.name_normalized AS name,
    t.url_path_slug AS slug,
    tou.year,
    tt.division
FROM
    team AS t
    INNER JOIN tournament_team AS tt ON t.id = tt.team_id
    INNER JOIN tournament AS tou ON tt.tournament_id = tou.id
ORDER BY t.name_normalized, t.id;
