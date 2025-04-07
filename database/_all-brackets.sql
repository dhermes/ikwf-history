SELECT
  b.division,
  b.weight
FROM
  bracket AS b
  INNER JOIN division AS d ON d.key = b.division
WHERE
  b.tournament_id = :tournament_id
ORDER BY d.id, b.weight
