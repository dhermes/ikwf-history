-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
    b.division,
    b.weight
FROM
    bracket AS b
INNER JOIN division AS d ON b.division = d.key
WHERE
    b.tournament_id = :tournament_id
ORDER BY d.id, b.weight
