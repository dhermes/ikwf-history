-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
  id, name_normalized, url_path_slug
FROM
  team
WHERE
  verified
ORDER BY name_normalized, id
