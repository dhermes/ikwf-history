SELECT
  id, first_name, last_name
FROM
  competitor
ORDER BY LOWER(last_name), LOWER(first_name), id
