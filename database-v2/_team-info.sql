-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.
SELECT
  id, name_normalized
FROM
  team
WHERE
  id IN (:team_ids)
ORDER BY name_normalized, id
