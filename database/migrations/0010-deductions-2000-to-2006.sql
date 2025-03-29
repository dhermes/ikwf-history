-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

-- NOTE: This is **NOT** a comprehensive list. It is just the teams that
--       finished with a negative score in either Novice or Senior or both.

INSERT INTO
  team_point_deduction (id, tournament_id, team_id, team_acronym, team_name, reason)
VALUES
  (1,  32, 171,   'HRD', 'HINSDALE RED DEVILS',        ''), -- 2001
  (2,  32, 171,   'HRD', 'HINSDALE RED DEVILS',        ''), -- 2001
  (3,  32, 468,   'WAR', 'WARRENSBURG WC',             ''), -- 2001
  (4,  32, 10110, 'WJP', 'WASHINGTON JR PANTHE',       ''), -- 2001
  (5,  33, 16,    'BAR', 'BARTLETT HAWK WC',           ''), -- 2002
  (6,  33, 53,    'CAR', 'CARBONDALE WC',              ''), -- 2002
  (7,  33, 10039, 'GLE', 'GLEN ELLYN DUNGEON WC',      ''), -- 2002
  (8,  33, 206,   'KNI', 'KNIGHTS WRESTLING',          ''), -- 2002
  (9,  33, 10171, 'LAO', 'LAN-OAK P.D. LITTLE REBELS', ''), -- 2002
  (10, 33, 229,   'LIO', 'LIONS WC',                   ''), -- 2002
  (11, 33, 400,   'STC', 'ST. CHARLES WC',             ''), -- 2002
  (12, 33, 10099, 'TBI', 'T-BIRD/RAIDER WRESTLING',    ''), -- 2002
  (13, 34, 10028, 'FEN', 'FENWICK FALCONS WC',         ''), -- 2003
  (14, 34, 10028, 'FEN', 'FENWICK FALCONS WC',         ''), -- 2003
  (15, 34, 10028, 'FEN', 'FENWICK FALCONS WC',         ''), -- 2003
  (16, 34, 134,   'FOX', 'FOX VALLEY WC',              ''), -- 2003
  (17, 34, 10061, 'LIM', 'LIMESTONE YOUTH WC',         ''), -- 2003
  (18, 34, 354,   'RIV', 'RIVERBEND WC',               ''), -- 2003
  (19, 34, 361,   'ROK', 'ROCK ISLAND WC',             ''), -- 2003
  (20, 34, 361,   'ROK', 'ROCK ISLAND WC',             ''), -- 2003
  (21, 34, 361,   'ROK', 'ROCK ISLAND WC',             ''), -- 2003
  (22, 34, 468,   'WAR', 'WARRENSBURG WC',             ''), -- 2003
  (23, 35, 8,     'ARG', 'ARGENTA/OREANA KIDS CLUB',   ''), -- 2004
  (24, 35, 24,    'BEV', 'BELVIDERE BANDITS',          ''), -- 2004
  (25, 35, 10020, 'DUR', 'DU-PEC CARNIVORES',          ''), -- 2004
  (26, 35, 10042, 'HER', 'HERRIN WC',                  ''), -- 2004
  (27, 35, 172,   'HOF', 'HOFFMAN ESTATES WC',         ''), -- 2004
  (28, 35, 206,   'KNI', 'KNIGHTS WRESTLING',          ''), -- 2004
  (29, 35, 248,   'MAR', 'MARENGO WC',                 ''), -- 2004
  (30, 35, 248,   'MAR', 'MARENGO WC',                 ''), -- 2004
  (31, 35, 263,   'MID', 'MIDWEST CENTRAL YOUTH',      ''), -- 2004
  (32, 35, 271,   'MLM', 'MORTON LITTLE MUSTANGS',     ''), -- 2004
  (33, 35, 271,   'MLM', 'MORTON LITTLE MUSTANGS',     ''), -- 2004
  (34, 35, 272,   'MRT', 'MORTON YOUTH WRESTLING',     ''), -- 2004
  (35, 35, 295,   'NOT', 'NOTRE DAME WRESTLING',       ''), -- 2004
  (36, 35, 326,   'PLA', 'PLAINFIELD WC',              ''), -- 2004
  (37, 35, 236,   '',    'RAMS WC',                    ''), -- 2004; no athletes?
  (38, 35, 349,   'RIC', 'RICH RATTLERS WC',           ''), -- 2004
  (39, 35, 349,   'RIC', 'RICH RATTLERS WC',           ''), -- 2004
  (40, 35, 397,   'SPR', 'SPRINGFIELD CAPITALS',       ''), -- 2004
  (41, 35, 10096, 'SCE', 'ST. CHARLES EAST WC',        ''), -- 2004
  (42, 35, 10096, 'SCE', 'ST. CHARLES EAST WC',        ''), -- 2004
  (43, 35, 10103, 'TIG', 'TIGER WC',                   ''), -- 2004
  (44, 35, 461,   'VAN', 'VANDALIA JR WRESTLING',      ''), -- 2004
  (45, 35, 461,   'VAN', 'VANDALIA JR WRESTLING',      ''), -- 2004
  (46, 36, 39,    'BRL', 'BRAWLERS',                   ''), -- 2005
  (47, 36, 266,   'MLI', 'MINOOKA LITTLE INDIANS',     ''), -- 2005
  (48, 36, 271,   'MLM', 'MORTON LITTLE MUSTANGS',     ''), -- 2005
  (49, 37, 10046, 'IRN', 'IRON MAN',                   ''), -- 2006
  (50, 37, 10048, 'JJS', 'JOLIET JUNIOR STEELMEN',     ''); -- 2006
