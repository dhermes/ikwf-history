-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

-- NOTE: This is a replacement for `team_competitor`

CREATE TABLE tournament_competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  competitor_id INTEGER NOT NULL REFERENCES competitor(id),
  team_id INTEGER NOT NULL REFERENCES team(id),
  -- NOTE: Some athletes used different names year to year (e.g Joe and Joseph)
  --       so this preserves the name they used in a given year. Additionally,
  --       athletes occasionally switched teams (e.g. Mike Mucha wrestled for
  --       "Lemont Bears WC" and then "Vittum Cats Wrestling Club").
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  suffix TEXT,
  UNIQUE(tournament_id, competitor_id)
);

--------------------------------------------------------------------------------

WITH tournament_competitor_map AS (
    SELECT
      b.tournament_id,
      tc.competitor_id
    FROM
      match AS m
      INNER JOIN bracket AS b ON b.id = m.bracket_id
      INNER JOIN team_competitor AS tc ON tc.id = m.top_competitor_id
    ----
    UNION
    ----
    SELECT
      b.tournament_id,
      tc.competitor_id
    FROM
      match AS m
      INNER JOIN bracket AS b ON b.id = m.bracket_id
      INNER JOIN team_competitor AS tc ON tc.id = m.bottom_competitor_id
),

tournament_competitor_insert AS (
  SELECT
    tc.id,
    (SELECT tcm.tournament_id FROM tournament_competitor_map AS tcm WHERE tcm.competitor_id = tc.competitor_id) AS tournament_id,
    tc.competitor_id,
    tc.team_id,
    c.first_name,
    c.last_name,
    c.suffix
  FROM
    team_competitor AS tc
    INNER JOIN competitor AS c ON c.id = tc.competitor_id
)

INSERT INTO
  tournament_competitor (id, tournament_id, competitor_id, team_id, first_name, last_name, suffix)
SELECT
  id, tournament_id, competitor_id, team_id, first_name, last_name, suffix
FROM
  tournament_competitor_insert;

--------------------------------------------------------------------------------

ALTER TABLE match RENAME TO match_deprecated;

--------------------------------------------------------------------------------

CREATE TABLE match (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bracket_id INTEGER REFERENCES bracket(id),
  bout_number INTEGER,
  match_slot TEXT NOT NULL REFERENCES match_slot(key),
  top_competitor_id INTEGER REFERENCES tournament_competitor(id),
  bottom_competitor_id INTEGER REFERENCES tournament_competitor(id),
  top_win BOOLEAN NOT NULL,
  result TEXT NOT NULL,
  result_type TEXT NOT NULL REFERENCES result_type(key),
  top_score INTEGER,
  bottom_score INTEGER,
  UNIQUE(bracket_id, match_slot),
  CHECK (
    (top_competitor_id IS NOT NULL OR bottom_competitor_id IS NOT NULL)
  ), -- Ensures at most one competitor can be NULL
  CHECK (
    (top_win = TRUE AND top_competitor_id IS NOT NULL)
    OR (top_win = FALSE AND bottom_competitor_id IS NOT NULL)
  ) -- Ensures winner cannot be `NULL`
);

--------------------------------------------------------------------------------

INSERT INTO
  match (id, bracket_id, bout_number, match_slot, top_competitor_id, bottom_competitor_id, top_win, result, result_type, top_score, bottom_score)
SELECT
  id, bracket_id, bout_number, match_slot, top_competitor_id, bottom_competitor_id, top_win, result, result_type, top_score, bottom_score
FROM
  match_deprecated;

--------------------------------------------------------------------------------

DROP TABLE match_deprecated;

--------------------------------------------------------------------------------

ALTER TABLE award_winner RENAME TO award_winner_deprecated;

--------------------------------------------------------------------------------

CREATE TABLE award_winner (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  division TEXT NOT NULL REFERENCES division(key),
  weight INTEGER NOT NULL,
  award TEXT NOT NULL REFERENCES award(key),
  competitor_id INTEGER REFERENCES tournament_competitor(id),
  UNIQUE(tournament_id, division)
);

--------------------------------------------------------------------------------

INSERT INTO
  award_winner (id, tournament_id, division, weight, award, competitor_id)
SELECT
  id, tournament_id, division, weight, award, competitor_id
FROM
  award_winner_deprecated;

--------------------------------------------------------------------------------

DROP TABLE award_winner_deprecated;

--------------------------------------------------------------------------------

DROP TABLE team_competitor;
