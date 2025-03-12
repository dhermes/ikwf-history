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
  (1, 'championship_r32_01'),
  (2, 'championship_r32_02'),
  (3, 'championship_r32_03'),
  (4, 'championship_r32_04'),
  (5, 'championship_r32_05'),
  (6, 'championship_r32_06'),
  (7, 'championship_r32_07'),
  (8, 'championship_r32_08'),
  (9, 'championship_r32_09'),
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
  (25, 'consolation_round1_01'),
  (26, 'consolation_round1_02'),
  (27, 'consolation_round1_03'),
  (28, 'consolation_round1_04'),
  (29, 'consolation_round1_05'),
  (30, 'consolation_round1_06'),
  (31, 'consolation_round1_07'),
  (32, 'consolation_round1_08'),
  (33, 'consolation_round2_01'),
  (34, 'consolation_round2_02'),
  (35, 'consolation_round2_03'),
  (36, 'consolation_round2_04'),
  (37, 'consolation_round2_05'),
  (38, 'consolation_round2_06'),
  (39, 'consolation_round2_07'),
  (40, 'consolation_round2_08'),
  (41, 'championship_quarter_01'),
  (42, 'championship_quarter_02'),
  (43, 'championship_quarter_03'),
  (44, 'championship_quarter_04'),
  (45, 'consolation_round3_01'),
  (46, 'consolation_round3_02'),
  (47, 'consolation_round3_03'),
  (48, 'consolation_round3_04'),
  (49, 'consolation_round4_blood_01'),
  (50, 'consolation_round4_blood_02'),
  (51, 'consolation_round4_blood_03'),
  (52, 'consolation_round4_blood_04'),
  (53, 'championship_semi_01'),
  (54, 'championship_semi_02'),
  (55, 'consolation_round5_01'),
  (56, 'consolation_round5_02'),
  (57, 'consolation_round6_semi_01'),
  (58, 'consolation_round6_semi_02'),
  (59, 'consolation_seventh_place'),
  (60, 'consolation_fifth_place'),
  (61, 'consolation_third_place'),
  (62, 'championship_first_place');

--------------------------------------------------------------------------------

CREATE TABLE division (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);

INSERT INTO
  division (id, key)
VALUES
  (1, 'bantam_boys'),
  (2, 'intermediate_boys'),
  (3, 'novice_boys'),
  (4, 'senior_boys'),
  (5, 'bantam_girls'),
  (6, 'intermediate_girls'),
  (7, 'novice_girls'),
  (8, 'senior_girls');

--------------------------------------------------------------------------------

CREATE TABLE team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
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

CREATE TABLE match (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bracket_id INTEGER REFERENCES bracket(id),
  bout_number INTEGER NOT NULL,
  match_slot TEXT NOT NULL REFERENCES match_slot(key),
  top_competitor_id INTEGER REFERENCES team_competitor(id),
  bottom_competitor_id INTEGER REFERENCES team_competitor(id),
  top_win BOOLEAN NOT NULL,
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
