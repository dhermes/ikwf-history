-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

CREATE TABLE award (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

--------------------------------------------------------------------------------

CREATE TABLE division (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

--------------------------------------------------------------------------------

CREATE TABLE match_slot (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

--------------------------------------------------------------------------------

CREATE TABLE result_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

--------------------------------------------------------------------------------

CREATE TABLE wrestleback_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

--------------------------------------------------------------------------------

CREATE TABLE tournament (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  year INTEGER NOT NULL,
  name TEXT NOT NULL,
  location TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  wrestleback_type TEXT NOT NULL REFERENCES wrestleback_type(key)
);

--------------------------------------------------------------------------------

CREATE TABLE bracket (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  weight INTEGER NOT NULL,
  division TEXT NOT NULL REFERENCES division(key),
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  UNIQUE(weight, division, tournament_id)
);

--------------------------------------------------------------------------------

-- NOTE: A `team` is the singular record for a club to be used across time. The
--       name is `name_normalized` because team / club names were often
--       recorded differently from year to year. For example:
--       - 2001: A-O KIDS WC
--       - 2002: ARGENTA/OREANA KIDS CLUB
--       - 2003: ARGENTA/OREANA KIDS CLUB
--       - 2004: ARGENTA/OREANA KIDS CLUB
--       - 2005: ARGENTA-OREANA KIDS CLUB
--       - 2006: ARGENTA/OREANA KIDS CLUB
--       We store the **ACTUAL** name from a given tournament (year) in
--       `tournament_team` and refer back to this table for canonicalization
--       and record-keeping across time.

CREATE TABLE team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_normalized TEXT NOT NULL
);

--------------------------------------------------------------------------------

CREATE TABLE tournament_team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  division TEXT NOT NULL REFERENCES division(key),
  team_id INTEGER NOT NULL REFERENCES team(id),
  team_score FLOAT,
  name TEXT NOT NULL,
  acronym TEXT,
  UNIQUE(tournament_id, division, team_id),
  UNIQUE(tournament_id, division, name)
);

--------------------------------------------------------------------------------

CREATE TABLE team_point_deduction (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  team_id INTEGER NOT NULL REFERENCES tournament_team(id),
  reason TEXT NOT NULL,
  amount INTEGER NOT NULL
  -- NOTE: No unique index, multiple deductions are possible within a tournament
  -- NOTE: Although `division` is a component of `tournament_team`, team point
  --       deductions apply across **ALL** divisions
);

--------------------------------------------------------------------------------

-- NOTE: A `competitor` is the singular record for an athlete to be used across
--       time. The name is `full_name_normalized` because athlete names were
--       often recorded differently from year to year. For example:
--       - 2001: JOEY FAGIANO
--       - 2002: JOE FAGIANO
--       - 2003: JOSEPH FAGIANO
--       and
--       - 2002: BENARD FUTRELL II
--       - 2003: BJ FUTRELL II
--       - 2004: BJ FUTRELL II
--       We store the **ACTUAL** name from a given tournament (year) in
--       `tournament_competitor` and refer back to this table for
--       canonicalization and record-keeping across time.

CREATE TABLE competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name_normalized TEXT NOT NULL
);

--------------------------------------------------------------------------------

CREATE TABLE tournament_competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  competitor_id INTEGER NOT NULL REFERENCES competitor(id),
  team_id INTEGER NOT NULL REFERENCES tournament_team(id),
  full_name TEXT NOT NULL,
  -- NOTE: The `first_name` and `last_name` are used to help match rows in
  --       `tournament_competitor` across years to remove duplicate entries in
  --       `competitor`.
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  UNIQUE(competitor_id, team_id)
);

--------------------------------------------------------------------------------

CREATE TABLE match (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bracket_id INTEGER REFERENCES bracket(id),
  bout_number INTEGER,
  match_slot TEXT NOT NULL REFERENCES match_slot(key),
  top_competitor_id INTEGER REFERENCES tournament_competitor(id),
  bottom_competitor_id INTEGER REFERENCES tournament_competitor(id),
  top_win BOOLEAN,
  result TEXT NOT NULL,
  result_type TEXT NOT NULL REFERENCES result_type(key),
  top_score INTEGER,
  bottom_score INTEGER,
  match_time_minutes INTEGER,
  match_time_seconds INTEGER,
  UNIQUE(bracket_id, match_slot),
  CHECK (
    (top_competitor_id IS NOT NULL OR bottom_competitor_id IS NOT NULL)
  ), -- Ensures at most one competitor can be NULL
  CHECK (
    (top_win = TRUE AND top_competitor_id IS NOT NULL)
    OR (top_win = FALSE AND bottom_competitor_id IS NOT NULL)
    OR (top_win IS NULL)
  ) -- Ensures winner cannot be `NULL`
);

--------------------------------------------------------------------------------

CREATE TABLE award_winner (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  division TEXT NOT NULL REFERENCES division(key),
  weight INTEGER NOT NULL,
  award TEXT NOT NULL REFERENCES award(key),
  competitor_id INTEGER NOT NULL REFERENCES tournament_competitor(id),
  UNIQUE(tournament_id, division)
);

--------------------------------------------------------------------------------

-- NOTE: The table is **DENORMALIZED** data (already present in `match` table).
--       However it's complex enough that it's worth just denormalizing from
--       the place matches and storing here.
CREATE TABLE placer_denormalized (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  division TEXT NOT NULL REFERENCES division(key),
  weight INTEGER NOT NULL,
  competitor_id INTEGER REFERENCES tournament_competitor(id),
  place INTEGER NOT NULL,
  UNIQUE(competitor_id),
  UNIQUE(tournament_id, division, weight, place),
  CHECK (
    (1 <= place AND place <= 8)
  )
);
