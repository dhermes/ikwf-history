-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  award (id, key)
VALUES
  (1, 'marty_combes'),
  (2, 'ron_urwin');

--------------------------------------------------------------------------------

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
  (8, 'senior_girls'),
  (9, 'junior_iwf'),
  (10, 'novice_iwf'),
  (11, 'senior_iwf');

--------------------------------------------------------------------------------

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

INSERT INTO
  wrestleback_type (id, key)
VALUES
  (1, 'follow_leader_semifinal'),
  (2, 'full');
