-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

UPDATE
  match
SET
  bout_number = NULL
WHERE
  bout_number = -30788;
