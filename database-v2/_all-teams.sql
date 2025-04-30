-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
    id,
    name_normalized AS name,
    url_path_slug AS slug
FROM
    team
ORDER BY name_normalized, id
