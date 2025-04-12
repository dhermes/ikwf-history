-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

-- 1999: 29th annual tournament; change ID from 30 to 29

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 30;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 30;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 30;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 30;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 30;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 30;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 30;
DELETE FROM tournament                                             WHERE            id = 30;
UPDATE tournament SET year = year - 100000                         WHERE            id = 30 - 1;

--------------------------------------------------------------------------------

-- 2000: 30th annual tournament; change ID from 31 to 30

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 31;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 31;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 31;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 31;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 31;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 31;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 31;
DELETE FROM tournament                                             WHERE            id = 31;
UPDATE tournament SET year = year - 100000                         WHERE            id = 31 - 1;

--------------------------------------------------------------------------------

-- 2001: 31st annual tournament; change ID from 32 to 31

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 32;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 32;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 32;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 32;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 32;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 32;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 32;
DELETE FROM tournament                                             WHERE            id = 32;
UPDATE tournament SET year = year - 100000                         WHERE            id = 32 - 1;

--------------------------------------------------------------------------------

-- 2002: 32nd annual tournament; change ID from 33 to 32

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 33;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 33;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 33;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 33;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 33;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 33;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 33;
DELETE FROM tournament                                             WHERE            id = 33;
UPDATE tournament SET year = year - 100000                         WHERE            id = 33 - 1;

--------------------------------------------------------------------------------

-- 2003: 33rd annual tournament; change ID from 34 to 33

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 34;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 34;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 34;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 34;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 34;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 34;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 34;
DELETE FROM tournament                                             WHERE            id = 34;
UPDATE tournament SET year = year - 100000                         WHERE            id = 34 - 1;

--------------------------------------------------------------------------------

-- 2004: 34th annual tournament; change ID from 35 to 34

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 35;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 35;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 35;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 35;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 35;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 35;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 35;
DELETE FROM tournament                                             WHERE            id = 35;
UPDATE tournament SET year = year - 100000                         WHERE            id = 35 - 1;

--------------------------------------------------------------------------------

-- 2005: 35th annual tournament; change ID from 36 to 35

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 36;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 36;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 36;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 36;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 36;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 36;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 36;
DELETE FROM tournament                                             WHERE            id = 36;
UPDATE tournament SET year = year - 100000                         WHERE            id = 36 - 1;

--------------------------------------------------------------------------------

-- 2006: 36th annual tournament; change ID from 37 to 36

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 37;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 37;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 37;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 37;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 37;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 37;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 37;
DELETE FROM tournament                                             WHERE            id = 37;
UPDATE tournament SET year = year - 100000                         WHERE            id = 37 - 1;

--------------------------------------------------------------------------------

-- 2007: 37th annual tournament; change ID from 38 to 37

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 38;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 38;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 38;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 38;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 38;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 38;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 38;
DELETE FROM tournament                                             WHERE            id = 38;
UPDATE tournament SET year = year - 100000                         WHERE            id = 38 - 1;

--------------------------------------------------------------------------------

-- 2008: 38th annual tournament; change ID from 39 to 38

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 39;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 39;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 39;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 39;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 39;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 39;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 39;
DELETE FROM tournament                                             WHERE            id = 39;
UPDATE tournament SET year = year - 100000                         WHERE            id = 39 - 1;

--------------------------------------------------------------------------------

-- 2009: 39th annual tournament; change ID from 40 to 39

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 40;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 40;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 40;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 40;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 40;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 40;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 40;
DELETE FROM tournament                                             WHERE            id = 40;
UPDATE tournament SET year = year - 100000                         WHERE            id = 40 - 1;

--------------------------------------------------------------------------------

-- 2010: 40th annual tournament; change ID from 41 to 40

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 41;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 41;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 41;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 41;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 41;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 41;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 41;
DELETE FROM tournament                                             WHERE            id = 41;
UPDATE tournament SET year = year - 100000                         WHERE            id = 41 - 1;

--------------------------------------------------------------------------------

-- 2011: 41st annual tournament; change ID from 42 to 41

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 42;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 42;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 42;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 42;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 42;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 42;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 42;
DELETE FROM tournament                                             WHERE            id = 42;
UPDATE tournament SET year = year - 100000                         WHERE            id = 42 - 1;

--------------------------------------------------------------------------------

-- 2012: 42nd annual tournament; change ID from 43 to 42

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 43;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 43;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 43;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 43;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 43;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 43;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 43;
DELETE FROM tournament                                             WHERE            id = 43;
UPDATE tournament SET year = year - 100000                         WHERE            id = 43 - 1;

--------------------------------------------------------------------------------

-- 2013: 43rd annual tournament; change ID from 44 to 43

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 44;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 44;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 44;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 44;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 44;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 44;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 44;
DELETE FROM tournament                                             WHERE            id = 44;
UPDATE tournament SET year = year - 100000                         WHERE            id = 44 - 1;

--------------------------------------------------------------------------------

-- 2014: 44th annual tournament; change ID from 45 to 44

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 45;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 45;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 45;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 45;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 45;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 45;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 45;
DELETE FROM tournament                                             WHERE            id = 45;
UPDATE tournament SET year = year - 100000                         WHERE            id = 45 - 1;

--------------------------------------------------------------------------------

-- 2015: 45th annual tournament; change ID from 46 to 45

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 46;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 46;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 46;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 46;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 46;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 46;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 46;
DELETE FROM tournament                                             WHERE            id = 46;
UPDATE tournament SET year = year - 100000                         WHERE            id = 46 - 1;

--------------------------------------------------------------------------------

-- 2016: 46th annual tournament; change ID from 47 to 46

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 47;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 47;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 47;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 47;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 47;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 47;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 47;
DELETE FROM tournament                                             WHERE            id = 47;
UPDATE tournament SET year = year - 100000                         WHERE            id = 47 - 1;

--------------------------------------------------------------------------------

-- 2017: 47th annual tournament; change ID from 48 to 47

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 48;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 48;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 48;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 48;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 48;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 48;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 48;
DELETE FROM tournament                                             WHERE            id = 48;
UPDATE tournament SET year = year - 100000                         WHERE            id = 48 - 1;

--------------------------------------------------------------------------------

-- 2018: 48th annual tournament; change ID from 49 to 48

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 49;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 49;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 49;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 49;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 49;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 49;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 49;
DELETE FROM tournament                                             WHERE            id = 49;
UPDATE tournament SET year = year - 100000                         WHERE            id = 49 - 1;

--------------------------------------------------------------------------------

-- 2019: 49th annual tournament; change ID from 50 to 49

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 1, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 50;
UPDATE award_winner          SET tournament_id = tournament_id - 1 WHERE tournament_id = 50;
UPDATE bracket               SET tournament_id = tournament_id - 1 WHERE tournament_id = 50;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 1 WHERE tournament_id = 50;
UPDATE team_score            SET tournament_id = tournament_id - 1 WHERE tournament_id = 50;
UPDATE tournament_competitor SET tournament_id = tournament_id - 1 WHERE tournament_id = 50;
UPDATE tournament_team       SET tournament_id = tournament_id - 1 WHERE tournament_id = 50;
DELETE FROM tournament                                             WHERE            id = 50;
UPDATE tournament SET year = year - 100000                         WHERE            id = 50 - 1;

--------------------------------------------------------------------------------

-- 2020: 50th annual tournament; change ID from 51 to 10050

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  10050, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 51;
UPDATE award_winner          SET tournament_id = 10050             WHERE tournament_id = 51;
UPDATE bracket               SET tournament_id = 10050             WHERE tournament_id = 51;
UPDATE team_point_deduction  SET tournament_id = 10050             WHERE tournament_id = 51;
UPDATE team_score            SET tournament_id = 10050             WHERE tournament_id = 51;
UPDATE tournament_competitor SET tournament_id = 10050             WHERE tournament_id = 51;
UPDATE tournament_team       SET tournament_id = 10050             WHERE tournament_id = 51;
DELETE FROM tournament                                             WHERE            id = 51;
UPDATE tournament SET year = year - 100000                         WHERE            id = 10050;

--------------------------------------------------------------------------------

-- 2022: 50th annual tournament; change ID from 52 to 50

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 2, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 52;
UPDATE award_winner          SET tournament_id = tournament_id - 2 WHERE tournament_id = 52;
UPDATE bracket               SET tournament_id = tournament_id - 2 WHERE tournament_id = 52;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 2 WHERE tournament_id = 52;
UPDATE team_score            SET tournament_id = tournament_id - 2 WHERE tournament_id = 52;
UPDATE tournament_competitor SET tournament_id = tournament_id - 2 WHERE tournament_id = 52;
UPDATE tournament_team       SET tournament_id = tournament_id - 2 WHERE tournament_id = 52;
DELETE FROM tournament                                             WHERE            id = 52;
UPDATE tournament SET year = year - 100000                         WHERE            id = 52 - 2;

--------------------------------------------------------------------------------

-- 2023: 51st annual tournament; change ID from 53 to 51

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 2, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 53;
UPDATE award_winner          SET tournament_id = tournament_id - 2 WHERE tournament_id = 53;
UPDATE bracket               SET tournament_id = tournament_id - 2 WHERE tournament_id = 53;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 2 WHERE tournament_id = 53;
UPDATE team_score            SET tournament_id = tournament_id - 2 WHERE tournament_id = 53;
UPDATE tournament_competitor SET tournament_id = tournament_id - 2 WHERE tournament_id = 53;
UPDATE tournament_team       SET tournament_id = tournament_id - 2 WHERE tournament_id = 53;
DELETE FROM tournament                                             WHERE            id = 53;
UPDATE tournament SET year = year - 100000                         WHERE            id = 53 - 2;

--------------------------------------------------------------------------------

-- 2024: 52nd annual tournament; change ID from 54 to 52

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 2, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 54;
UPDATE award_winner          SET tournament_id = tournament_id - 2 WHERE tournament_id = 54;
UPDATE bracket               SET tournament_id = tournament_id - 2 WHERE tournament_id = 54;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 2 WHERE tournament_id = 54;
UPDATE team_score            SET tournament_id = tournament_id - 2 WHERE tournament_id = 54;
UPDATE tournament_competitor SET tournament_id = tournament_id - 2 WHERE tournament_id = 54;
UPDATE tournament_team       SET tournament_id = tournament_id - 2 WHERE tournament_id = 54;
DELETE FROM tournament                                             WHERE            id = 54;
UPDATE tournament SET year = year - 100000                         WHERE            id = 54 - 2;

--------------------------------------------------------------------------------

-- 2024: 52nd annual tournament; change ID from 10054 to 10052

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 2, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 10054;
UPDATE award_winner          SET tournament_id = tournament_id - 2 WHERE tournament_id = 10054;
UPDATE bracket               SET tournament_id = tournament_id - 2 WHERE tournament_id = 10054;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 2 WHERE tournament_id = 10054;
UPDATE team_score            SET tournament_id = tournament_id - 2 WHERE tournament_id = 10054;
UPDATE tournament_competitor SET tournament_id = tournament_id - 2 WHERE tournament_id = 10054;
UPDATE tournament_team       SET tournament_id = tournament_id - 2 WHERE tournament_id = 10054;
DELETE FROM tournament                                             WHERE            id = 10054;
UPDATE tournament SET year = year - 100000                         WHERE            id = 10054 - 2;

--------------------------------------------------------------------------------

-- 2025: 53rd annual tournament; change ID from 55 to 53

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
SELECT
  -- NOTE: Temporarily add 100,000 to `year` to side-step a UNIQUE constraint
  t.id - 2, t.year + 100000, t.name, t.location, t.start_date, t.end_date, t.wrestleback_type
FROM
  tournament AS t                                                  WHERE          t.id = 55;
UPDATE award_winner          SET tournament_id = tournament_id - 2 WHERE tournament_id = 55;
UPDATE bracket               SET tournament_id = tournament_id - 2 WHERE tournament_id = 55;
UPDATE team_point_deduction  SET tournament_id = tournament_id - 2 WHERE tournament_id = 55;
UPDATE team_score            SET tournament_id = tournament_id - 2 WHERE tournament_id = 55;
UPDATE tournament_competitor SET tournament_id = tournament_id - 2 WHERE tournament_id = 55;
UPDATE tournament_team       SET tournament_id = tournament_id - 2 WHERE tournament_id = 55;
DELETE FROM tournament                                             WHERE            id = 55;
UPDATE tournament SET year = year - 100000                         WHERE            id = 55 - 2;
