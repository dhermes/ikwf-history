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
  (907, 84, 'bantam', 55);

INSERT INTO
  match (id, bracket_id, bout_number, match_slot, top_competitor_id, bottom_competitor_id, top_win, result, result_type, top_team_acronym, bottom_team_acronym)
VALUES
  (1,  907, NULL, 'championship_r32_01',         1,    NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (2,  907, 1089, 'championship_r32_02',         2,    3,    FALSE, 'TF 17-1',   'bye', NULL, NULL),
  (3,  907, NULL, 'championship_r32_03',         4,    NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (4,  907, 1090, 'championship_r32_04',         5,    6,    TRUE,  'Fall 0:24', 'bye', NULL, NULL),
  (5,  907, NULL, 'championship_r32_05',         7,    NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (6,  907, 1091, 'championship_r32_06',         8,    9,    FALSE, 'Dec 9-4',   'bye', NULL, NULL),
  (7,  907, NULL, 'championship_r32_07',         10,   NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (8,  907, 1092, 'championship_r32_08',         11,   12,   FALSE, 'Fall 1:53', 'bye', NULL, NULL),
  (9,  907, NULL, 'championship_r32_09',         13,   NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (10, 907, 1093, 'championship_r32_10',         14,   15,   TRUE,  'Fall 1:16', 'bye', NULL, NULL),
  (11, 907, NULL, 'championship_r32_11',         16,   NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (12, 907, 1094, 'championship_r32_12',         17,   18,   FALSE, 'Dec 6-3',   'bye', NULL, NULL),
  (13, 907, NULL, 'championship_r32_13',         19,   NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (14, 907, 1095, 'championship_r32_14',         20,   21,   TRUE,  'TF 15-0',   'bye', NULL, NULL),
  (15, 907, NULL, 'championship_r32_15',         22,   NULL, TRUE,  'Bye',       'bye', NULL, NULL),
  (16, 907, 1096, 'championship_r32_16',         23,   24,   TRUE,  'Maj 15-7',  'bye', NULL, NULL),
  (17, 907, 1193, 'championship_r16_01',         1,    3,    TRUE,  'Maj 21-9',  'bye', NULL, NULL),
  (18, 907, 1194, 'championship_r16_02',         4,    5,    FALSE, 'Maj 8-0',   'bye', NULL, NULL),
  (19, 907, 1195, 'championship_r16_03',         7,    9,    TRUE,  'Fall 1:19', 'bye', NULL, NULL),
  (20, 907, 1196, 'championship_r16_04',         10,   12,   TRUE,  'Fall 1:26', 'bye', NULL, NULL),
  (21, 907, 1197, 'championship_r16_05',         13,   14,   TRUE,  'Dec 7-1',   'bye', NULL, NULL),
  (22, 907, 1198, 'championship_r16_06',         16,   18,   TRUE,  'Fall 0:40', 'bye', NULL, NULL),
  (23, 907, 1199, 'championship_r16_07',         19,   20,   TRUE,  'Maj 9-0',   'bye', NULL, NULL),
  (24, 907, 1200, 'championship_r16_08',         22,   23,   TRUE,  'Fall 0:49', 'bye', NULL, NULL),
  (25, 907, 1297, 'consolation_round2_01',       23,   2,    TRUE,  'Dec 8-2',   'bye', NULL, NULL),
  (26, 907, 1298, 'consolation_round2_02',       20,   6,    TRUE,  'Dec 2-0',   'bye', NULL, NULL),
  (27, 907, 1299, 'consolation_round2_03',       18,   8,    TRUE,  'Dec 8-5',   'bye', NULL, NULL),
  (28, 907, 1300, 'consolation_round2_04',       14,   11,   TRUE,  'Maj 13-0',  'bye', NULL, NULL),
  (29, 907, 1301, 'consolation_round2_05',       15,   12,   FALSE, 'Maj 19-6',  'bye', NULL, NULL),
  (30, 907, 1302, 'consolation_round2_06',       17,   9,    FALSE, 'Dec 3-1',   'bye', NULL, NULL),
  (31, 907, 1303, 'consolation_round2_07',       21,   4,    FALSE, 'Dec 12-7',  'bye', NULL, NULL),
  (32, 907, 1304, 'consolation_round2_08',       24,   3,    TRUE,  'Dec 11-5',  'bye', NULL, NULL),
  (33, 907, 1401, 'championship_quarter_01',     1,    5,    TRUE,  'Maj 11-1',  'bye', NULL, NULL),
  (34, 907, 1402, 'championship_quarter_02',     7,    10,   FALSE, 'TF 17-0',   'bye', NULL, NULL),
  (35, 907, 1403, 'championship_quarter_03',     13,   16,   FALSE, 'Maj 14-1',  'bye', NULL, NULL),
  (36, 907, 1404, 'championship_quarter_04',     19,   22,   FALSE, 'Fall 0:48', 'bye', NULL, NULL),
  (37, 907, 1405, 'consolation_round3_01',       23,   20,   TRUE,  'Dec 7-2',   'bye', NULL, NULL),
  (38, 907, 1406, 'consolation_round3_02',       18,   14,   FALSE, 'Dec 11-9',  'bye', NULL, NULL),
  (39, 907, 1407, 'consolation_round3_03',       12,   9,    TRUE,  'TF 16-1',   'bye', NULL, NULL),
  (40, 907, 1408, 'consolation_round3_04',       4,    24,   FALSE, 'Dec 7-3',   'bye', NULL, NULL),
  (41, 907, 1461, 'consolation_round4_blood_01', 7,    23,   FALSE, 'Dec 8-2',   'bye', NULL, NULL),
  (42, 907, 1462, 'consolation_round4_blood_02', 5,    14,   TRUE,  'Fall 1:33', 'bye', NULL, NULL),
  (43, 907, 1463, 'consolation_round4_blood_03', 12,   19,   FALSE, 'Fall 1:29', 'bye', NULL, NULL),
  (44, 907, 1464, 'consolation_round4_blood_04', 24,   13,   FALSE, 'TF 16-1',   'bye', NULL, NULL),
  (45, 907, 1513, 'championship_semi_01',        1,    10,   TRUE,  'Fall 0:34', 'bye', NULL, NULL),
  (46, 907, 1514, 'championship_semi_02',        16,   22,   TRUE,  'Dec 6-4',   'bye', NULL, NULL),
  (47, 907, 1515, 'consolation_round5_01',       23,   5,    FALSE, 'Dec 6-4',   'bye', NULL, NULL),
  (48, 907, 1516, 'consolation_round5_02',       19,   13,   FALSE, 'Dec 10-7',  'bye', NULL, NULL),
  (49, 907, 1543, 'consolation_round6_semi_01',  22,   5,    TRUE,  'Fall 0:58', 'bye', NULL, NULL),
  (50, 907, 1544, 'consolation_round6_semi_02',  13,   10,   FALSE, 'Fall 1:24', 'bye', NULL, NULL),
  (51, 907, 1582, 'consolation_seventh_place',   23,   19,   FALSE, 'Dec 6-2',   'bye', NULL, NULL),
  (52, 907, 1581, 'consolation_fifth_place',     5,    13,   FALSE, 'Dec 10-5',  'bye', NULL, NULL),
  (53, 907, 1580, 'consolation_third_place',     22,   10,   TRUE,  'TF 17-2',   'bye', NULL, NULL),
  (54, 907, 1597, 'championship_first_place',    1,    16,   FALSE, 'Dec 1-0',   'bye', NULL, NULL);
