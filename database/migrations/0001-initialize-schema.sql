-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

CREATE TABLE match_slot (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

INSERT INTO
  match_slot (id, key)
VALUES
  (1,  'championship_r32_01'),
  (2,  'championship_r32_02'),
  (3,  'championship_r32_03'),
  (4,  'championship_r32_04'),
  (5,  'championship_r32_05'),
  (6,  'championship_r32_06'),
  (7,  'championship_r32_07'),
  (8,  'championship_r32_08'),
  (9,  'championship_r32_09'),
  (10, 'championship_r32_10'),
  (11, 'championship_r32_11'),
  (12, 'championship_r32_12'),
  (13, 'championship_r32_13'),
  (14, 'championship_r32_14'),
  (15, 'championship_r32_15'),
  (16, 'championship_r32_16'),
  (17, 'championship_r16_01'),
  (18, 'championship_r16_02'),
  (19, 'championship_r16_03'),
  (20, 'championship_r16_04'),
  (21, 'championship_r16_05'),
  (22, 'championship_r16_06'),
  (23, 'championship_r16_07'),
  (24, 'championship_r16_08'),
  (25, 'consolation_round2_01'),
  (26, 'consolation_round2_02'),
  (27, 'consolation_round2_03'),
  (28, 'consolation_round2_04'),
  (29, 'consolation_round2_05'),
  (30, 'consolation_round2_06'),
  (31, 'consolation_round2_07'),
  (32, 'consolation_round2_08'),
  (33, 'championship_quarter_01'),
  (34, 'championship_quarter_02'),
  (35, 'championship_quarter_03'),
  (36, 'championship_quarter_04'),
  (37, 'consolation_round3_01'),
  (38, 'consolation_round3_02'),
  (39, 'consolation_round3_03'),
  (40, 'consolation_round3_04'),
  (41, 'consolation_round4_blood_01'),
  (42, 'consolation_round4_blood_02'),
  (43, 'consolation_round4_blood_03'),
  (44, 'consolation_round4_blood_04'),
  (45, 'championship_semi_01'),
  (46, 'championship_semi_02'),
  (47, 'consolation_round5_01'),
  (48, 'consolation_round5_02'),
  (49, 'consolation_round6_semi_01'),
  (50, 'consolation_round6_semi_02'),
  (51, 'consolation_seventh_place'),
  (52, 'consolation_fifth_place'),
  (53, 'consolation_third_place'),
  (54, 'championship_first_place');

--------------------------------------------------------------------------------

CREATE TABLE division (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

INSERT INTO
  division (id, key)
VALUES
  (1, 'bantam'),
  (2, 'intermediate'),
  (3, 'novice'),
  (4, 'senior'),
  (5, 'bantam_girls'),
  (6, 'intermediate_girls'),
  (7, 'novice_girls'),
  (8, 'senior_girls');

--------------------------------------------------------------------------------

CREATE TABLE wrestleback_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

INSERT INTO
  wrestleback_type (id, key)
VALUES
  (1, 'follow_leader_semifinal'),
  (2, 'full');

--------------------------------------------------------------------------------

CREATE TABLE team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
  -- NOTE: A `UNIQUE` constraint has been removed and will be added back
  --       after teams have been merged after initial data load.
);

CREATE TABLE competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  suffix TEXT,
  full_name TEXT GENERATED ALWAYS AS (
    TRIM(
      TRIM(first_name) || ' ' || TRIM(last_name)
    ) ||
    CASE
      WHEN suffix IS NOT NULL AND TRIM(suffix) != ''
      THEN ' ' || TRIM(suffix)
      ELSE ''
    END
  ) STORED,
  CHECK (
    (first_name <> '' AND last_name <> '')
  )
);

CREATE TABLE team_competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  team_id INTEGER NOT NULL REFERENCES team(id),
  competitor_id INTEGER NOT NULL REFERENCES competitor(id),
  UNIQUE(team_id, competitor_id)
);

--------------------------------------------------------------------------------

CREATE TABLE tournament (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  year INTEGER NOT NULL,
  name TEXT NOT NULL,
  location TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  wrestleback_type TEXT NOT NULL REFERENCES wrestleback_type(key),
  UNIQUE(year, name)
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

CREATE TABLE result_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

INSERT INTO
  result_type (id, key)
VALUES
  (1, 'bye'),
  (2, 'decision'),
  (3, 'default'),
  (4, 'disqualification'),
  (5, 'fall'),
  (6, 'forfeit'),
  (7, 'major'),
  (8, 'tech'),
  (9, 'walkover'),
  (10, 'place'); -- placeholder value for partial results / place-only results

--------------------------------------------------------------------------------

CREATE TABLE match (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bracket_id INTEGER REFERENCES bracket(id),
  bout_number INTEGER,
  match_slot TEXT NOT NULL REFERENCES match_slot(key),
  top_competitor_id INTEGER REFERENCES team_competitor(id),
  bottom_competitor_id INTEGER REFERENCES team_competitor(id),
  top_win BOOLEAN NOT NULL,
  result TEXT NOT NULL,
  result_type TEXT NOT NULL REFERENCES result_type(key),
  top_team_acronym TEXT,
  bottom_team_acronym TEXT,
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

CREATE TABLE team_point_deduction (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  team_id INTEGER NOT NULL REFERENCES team(id),
  team_acronym TEXT NOT NULL, -- For a given tournament, one-off team acronyms were used
  team_name TEXT NOT NULL, -- For a given tournament, one-off team names were used
  reason TEXT NOT NULL,
  amount INTEGER NOT NULL
  -- NOTE: No unique index, multiple deductions are possible within a tournament
  -- NOTE: No `division` is provided here, team point deductions apply across
  --       **ALL** divisions
);

--------------------------------------------------------------------------------

CREATE TABLE team_score (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  division TEXT NOT NULL REFERENCES division(key),
  team_id INTEGER NOT NULL REFERENCES team(id),
  team_acronym TEXT NOT NULL, -- For a given tournament, one-off team acronyms were used
  team_name TEXT NOT NULL, -- For a given tournament, one-off team names were used
  score FLOAT NOT NULL
  -- NOTE: There is no UNIQUE(tournament_id, division, team_id) constraint.
  --       In some years, teams could have multiple team scores from
  --       scoring and non-scoring wrestlers.
);

--------------------------------------------------------------------------------

CREATE TABLE award (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

INSERT INTO
  award (id, key)
VALUES
  (1, 'marty_combes'),
  (2, 'ron_urwin');

--------------------------------------------------------------------------------

CREATE TABLE award_winner (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL REFERENCES tournament(id),
  division TEXT NOT NULL REFERENCES division(key),
  weight INTEGER NOT NULL,
  award TEXT NOT NULL REFERENCES award(key),
  competitor_id INTEGER REFERENCES team_competitor(id),
  UNIQUE(tournament_id, division)
);
