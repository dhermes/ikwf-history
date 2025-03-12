-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  competitor (id, first_name, last_name, suffix)
VALUES
  (1,  'Dexton',    'Pontnack',   NULL),
  (2,  'Hamza',     'Shakeel',    NULL),
  (3,  'Joey',      'Boggs',      NULL),
  (4,  'Kayden',    'Sicka',      NULL),
  (5,  'Emmett',    'Richardson', NULL),
  (6,  'Michael',   'Sims',       NULL),
  (7,  'Jack',      'Hermes',     NULL),
  (8,  'Darek',     'Lee',        'III'),
  (9,  'Levi',      'Schroeder',  NULL),
  (10, 'Jerome',    'Turner',     'Jr'),
  (11, 'Eris',      'Bybee',      NULL),
  (12, 'Bowyn',     'Schulz',     NULL),
  (13, 'William',   'Kochel',     NULL),
  (14, 'Bobby',     'O''Keefe',   NULL),
  (15, 'Aedan',     'Perez',      NULL),
  (16, 'Kingston',  'Hamilton',   NULL),
  (17, 'Roman',     'Oliver',     NULL),
  (18, 'Donavan',   'Shelby',     NULL),
  (19, 'Hunter',    'Voss',       NULL),
  (20, 'Max',       'Corbell',    NULL),
  (21, 'William',   'McConnell',  NULL),
  (22, 'Alexander', 'Cid',        NULL),
  (23, 'Declan',    'Druger',     NULL),
  (24, 'Ezra',      'Lindsey',    NULL);

INSERT INTO
  team_competitor (id, competitor_id, team_id)
VALUES
  (1,  1,  92),
  (2,  2,  630),
  (3,  3,  579),
  (4,  4,  517),
  (5,  5,  328),
  (6,  6,  488),
  (7,  7,  134),
  (8,  8,  39),
  (9,  9,  245),
  (10, 10, 399),
  (11, 11, 548),
  (12, 12, 112),
  (13, 13, 227),
  (14, 14, 97),
  (15, 15, 147),
  (16, 16, 600),
  (17, 17, 303),
  (18, 18, 407),
  (19, 19, 548),
  (20, 20, 134),
  (21, 21, 429),
  (22, 22, 474),
  (23, 23, 102),
  (24, 24, 162);

INSERT INTO
  bracket (id, weight, division, tournament_id)
VALUES
  (1, 84, 'bantam_boys', 56);

INSERT INTO
  match (id, bracket_id, bout_number, match_slot, top_competitor_id, bottom_competitor_id, top_win, result, top_team_acronym, bottom_team_acronym)
VALUES
  (1,  1, 0,    'championship_r32_01',         1,    NULL, TRUE,  'Bye',       NULL, NULL),
  (2,  1, 1089, 'championship_r32_02',         2,    3,    FALSE, 'TF 17-1',   NULL, NULL),
  (3,  1, 0,    'championship_r32_03',         4,    NULL, TRUE,  'Bye',       NULL, NULL),
  (4,  1, 1090, 'championship_r32_04',         5,    6,    TRUE,  'Fall 0:24', NULL, NULL),
  (5,  1, 0,    'championship_r32_05',         7,    NULL, TRUE,  'Bye',       NULL, NULL),
  (6,  1, 1091, 'championship_r32_06',         8,    9,    FALSE, 'Dec 9-4',   NULL, NULL),
  (7,  1, 0,    'championship_r32_07',         10,   NULL, TRUE,  'Bye',       NULL, NULL),
  (8,  1, 1092, 'championship_r32_08',         11,   12,   FALSE, 'Fall 1:53', NULL, NULL),
  (9,  1, 0,    'championship_r32_09',         13,   NULL, TRUE,  'Bye',       NULL, NULL),
  (10, 1, 1093, 'championship_r32_10',         14,   15,   TRUE,  'Fall 1:16', NULL, NULL),
  (11, 1, 0,    'championship_r32_11',         16,   NULL, TRUE,  'Bye',       NULL, NULL),
  (12, 1, 1094, 'championship_r32_12',         17,   18,   FALSE, 'Dec 6-3',   NULL, NULL),
  (13, 1, 0,    'championship_r32_13',         19,   NULL, TRUE,  'Bye',       NULL, NULL),
  (14, 1, 1095, 'championship_r32_14',         20,   21,   TRUE,  'TF 15-0',   NULL, NULL),
  (15, 1, 0,    'championship_r32_15',         22,   NULL, TRUE,  'Bye',       NULL, NULL),
  (16, 1, 1096, 'championship_r32_16',         23,   24,   TRUE,  'Maj 15-7',  NULL, NULL),
  (17, 1, 1193, 'championship_r16_01',         1,    3,    TRUE,  'Maj 21-9',  NULL, NULL),
  (18, 1, 1194, 'championship_r16_02',         4,    5,    FALSE, 'Maj 8-0',   NULL, NULL),
  (19, 1, 1195, 'championship_r16_03',         7,    9,    TRUE,  'Fall 1:19', NULL, NULL),
  (20, 1, 1196, 'championship_r16_04',         10,   12,   TRUE,  'Fall 1:26', NULL, NULL),
  (21, 1, 1197, 'championship_r16_05',         13,   14,   TRUE,  'Dec 7-1',   NULL, NULL),
  (22, 1, 1198, 'championship_r16_06',         16,   18,   TRUE,  'Fall 0:40', NULL, NULL),
  (23, 1, 1199, 'championship_r16_07',         19,   20,   TRUE,  'Maj 9-0',   NULL, NULL),
  (24, 1, 1200, 'championship_r16_08',         22,   23,   TRUE,  'Fall 0:49', NULL, NULL),
  (25, 1, 0,    'consolation_round1_01',       NULL, 2,    FALSE, 'Bye',       NULL, NULL),
  (26, 1, 0,    'consolation_round1_02',       NULL, 6,    FALSE, 'Bye',       NULL, NULL),
  (27, 1, 0,    'consolation_round1_03',       NULL, 8,    FALSE, 'Bye',       NULL, NULL),
  (28, 1, 0,    'consolation_round1_04',       NULL, 11,   FALSE, 'Bye',       NULL, NULL),
  (29, 1, 0,    'consolation_round1_05',       NULL, 15,   FALSE, 'Bye',       NULL, NULL),
  (30, 1, 0,    'consolation_round1_06',       NULL, 17,   FALSE, 'Bye',       NULL, NULL),
  (31, 1, 0,    'consolation_round1_07',       NULL, 21,   FALSE, 'Bye',       NULL, NULL),
  (32, 1, 0,    'consolation_round1_08',       NULL, 24,   FALSE, 'Bye',       NULL, NULL),
  (33, 1, 1297, 'consolation_round2_01',       23,   2,    TRUE,  'Dec 8-2',   NULL, NULL),
  (34, 1, 1298, 'consolation_round2_02',       20,   6,    TRUE,  'Dec 2-0',   NULL, NULL),
  (35, 1, 1299, 'consolation_round2_03',       18,   8,    TRUE,  'Dec 8-5',   NULL, NULL),
  (36, 1, 1300, 'consolation_round2_04',       14,   11,   TRUE,  'Maj 13-0',  NULL, NULL),
  (37, 1, 1301, 'consolation_round2_05',       15,   12,   FALSE, 'Maj 19-6',  NULL, NULL),
  (38, 1, 1302, 'consolation_round2_06',       17,   9,    FALSE, 'Dec 3-1',   NULL, NULL),
  (39, 1, 1303, 'consolation_round2_07',       21,   4,    FALSE, 'Dec 12-7',  NULL, NULL),
  (40, 1, 1304, 'consolation_round2_08',       24,   3,    TRUE,  'Dec 11-5',  NULL, NULL),
  (41, 1, 1401, 'championship_quarter_01',     1,    5,    TRUE,  'Maj 11-1',  NULL, NULL),
  (42, 1, 1402, 'championship_quarter_02',     7,    10,   FALSE, 'TF 17-0',   NULL, NULL),
  (43, 1, 1403, 'championship_quarter_03',     13,   16,   FALSE, 'Maj 14-1',  NULL, NULL),
  (44, 1, 1404, 'championship_quarter_04',     19,   22,   FALSE, 'Fall 0:48', NULL, NULL),
  (45, 1, 1405, 'consolation_round3_01',       23,   20,   TRUE,  'Dec 7-2',   NULL, NULL),
  (46, 1, 1406, 'consolation_round3_02',       18,   14,   FALSE, 'Dec 11-9',  NULL, NULL),
  (47, 1, 1407, 'consolation_round3_03',       12,   9,    TRUE,  'TF 16-1',   NULL, NULL),
  (48, 1, 1408, 'consolation_round3_04',       4,    24,   FALSE, 'Dec 7-3',   NULL, NULL),
  (49, 1, 1461, 'consolation_round4_blood_01', 7,    23,   FALSE, 'Dec 8-2',   NULL, NULL),
  (50, 1, 1462, 'consolation_round4_blood_02', 5,    14,   TRUE,  'Fall 1:33', NULL, NULL),
  (51, 1, 1463, 'consolation_round4_blood_03', 12,   19,   FALSE, 'Fall 1:29', NULL, NULL),
  (52, 1, 1464, 'consolation_round4_blood_04', 24,   13,   FALSE, 'TF 16-1',   NULL, NULL),
  (53, 1, 1513, 'championship_semi_01',        1,    10,   TRUE,  'Fall 0:34', NULL, NULL),
  (54, 1, 1514, 'championship_semi_02',        16,   22,   TRUE,  'Dec 6-4',   NULL, NULL),
  (55, 1, 1515, 'consolation_round5_01',       23,   5,    FALSE, 'Dec 6-4',   NULL, NULL),
  (56, 1, 1516, 'consolation_round5_02',       19,   13,   FALSE, 'Dec 10-7',  NULL, NULL),
  (57, 1, 1543, 'consolation_round6_semi_01',  22,   5,    TRUE,  'Fall 0:58', NULL, NULL),
  (58, 1, 1544, 'consolation_round6_semi_02',  13,   10,   FALSE, 'Fall 1:24', NULL, NULL),
  (59, 1, 1582, 'consolation_seventh_place',   23,   19,   FALSE, 'Dec 6-2',   NULL, NULL),
  (60, 1, 1581, 'consolation_fifth_place',     5,    13,   FALSE, 'Dec 10-5',  NULL, NULL),
  (61, 1, 1580, 'consolation_third_place',     22,   10,   TRUE,  'TF 17-2',   NULL, NULL),
  (62, 1, 1597, 'championship_first_place',    1,    16,   FALSE, 'Dec 1-0',   NULL, NULL);
