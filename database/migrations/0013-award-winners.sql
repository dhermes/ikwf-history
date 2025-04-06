-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  award_winner (id, tournament_id, division, weight, award, competitor_id)
VALUES
  -- 2000
  (1, 31, 'novice', 70, 'marty_combes', 299), -- Jimmy Kennedy - Wrestling Factory of Libertyville
  (2, 31, 'senior', 101, 'ron_urwin', 762), -- Michael Poeta – Highland Park Little Giants
  -- 2006
  (3, 37, 'novice', 89, 'marty_combes', 5241), -- Lucas Smith - Bison WC
  (4, 37, 'senior', 166, 'ron_urwin', 5796); -- Sterling Hecox - Hecox Team Benaiah
