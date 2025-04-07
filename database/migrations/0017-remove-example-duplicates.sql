-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

-- This removes "unused" competitor rows that were duplicated because of
-- the presence of `0004-example-bracket.sql`. (The `0004` migration was
-- created early in the process to help define the schema.)

DELETE FROM
  team_competitor
WHERE
  id IN (
    21199,
    21200,
    21201,
    21202,
    21203,
    21204,
    21205,
    21206,
    21207,
    21208,
    21209,
    21210,
    21211,
    21212,
    21213,
    21214,
    21215,
    21216,
    21217,
    21218,
    21219,
    21220,
    21221,
    21222
  );

DELETE FROM
  competitor
WHERE
  id IN (
    21199,
    21200,
    21201,
    21202,
    21203,
    21204,
    21205,
    21206,
    21207,
    21208,
    21209,
    21210,
    21211,
    21212,
    21213,
    21214,
    21215,
    21216,
    21217,
    21218,
    21219,
    21220,
    21221,
    21222
  );
