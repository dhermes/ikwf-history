-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, wrestleback_type)
VALUES
  (1,  1971, 'Illinois Wrestling Federation State Championship', '', '1971-03-01', '1971-03-01', 'follow_leader_semifinal'),
  (2,  1972, 'Illinois Wrestling Federation State Championship', '', '1972-03-01', '1972-03-01', 'follow_leader_semifinal'),
  (3,  1973, 'Illinois Wrestling Federation State Championship', '', '1973-03-01', '1973-03-01', 'follow_leader_semifinal'),
  (4,  1974, 'Illinois Wrestling Federation State Championship', '', '1974-03-01', '1974-03-01', 'follow_leader_semifinal'),
  (5,  1975, 'Illinois Wrestling Federation State Championship', '', '1975-03-01', '1975-03-01', 'follow_leader_semifinal'),
  (6,  1976, 'Illinois Wrestling Federation State Championship', '', '1976-03-01', '1976-03-01', 'follow_leader_semifinal'),
  (7,  1977, 'Illinois Wrestling Federation State Championship', '', '1977-03-01', '1977-03-01', 'follow_leader_semifinal'),
  (8,  1978, 'Illinois Wrestling Federation State Championship', '', '1978-03-01', '1978-03-01', 'follow_leader_semifinal'),
  (9,  1979, 'Illinois Wrestling Federation State Championship', '', '1979-03-01', '1979-03-01', 'follow_leader_semifinal'),
  (10, 1980, 'Illinois Wrestling Federation State Championship', '', '1980-03-01', '1980-03-01', 'follow_leader_semifinal'),
  (11, 1981, 'Illinois Wrestling Federation State Championship', '', '1981-03-01', '1981-03-01', 'follow_leader_semifinal'),
  (12, 1982, 'Illinois Wrestling Federation State Championship', '', '1982-03-01', '1982-03-01', 'follow_leader_semifinal'),
  (13, 1983, 'Illinois Wrestling Federation State Championship', '', '1983-03-01', '1983-03-01', 'follow_leader_semifinal'),
  (14, 1984, 'Illinois Wrestling Federation State Championship', '', '1984-03-01', '1984-03-01', 'follow_leader_semifinal'),
  (15, 1985, 'Illinois Wrestling Federation State Championship', '', '1985-03-01', '1985-03-01', 'follow_leader_semifinal'),
  (16, 1986, 'Illinois Wrestling Federation State Championship', '', '1986-03-01', '1986-03-01', 'follow_leader_semifinal'),
  (17, 1987, 'Illinois Wrestling Federation State Championship', '', '1987-03-01', '1987-03-01', 'follow_leader_semifinal'),
  (18, 1988, 'Illinois Wrestling Federation State Championship', '', '1988-03-01', '1988-03-01', 'follow_leader_semifinal'),
  (19, 1989, 'Illinois Wrestling Federation State Championship', '', '1989-03-01', '1989-03-01', 'follow_leader_semifinal'),
  (22, 1992, 'Illinois Wrestling Federation State Championship', '', '1992-03-01', '1992-03-01', 'follow_leader_semifinal'),
  (24, 1994, 'Illinois Wrestling Federation State Championship', '', '1994-03-01', '1994-03-01', 'follow_leader_semifinal'),
  (25, 1995, 'Illinois Wrestling Federation State Championship', '', '1995-03-01', '1995-03-01', 'follow_leader_semifinal'),
  (26, 1996, 'Illinois Wrestling Federation State Championship', '', '1996-03-01', '1996-03-01', 'follow_leader_semifinal'),
  (27, 1997, 'Illinois Wrestling Federation State Championship', '', '1997-03-01', '1997-03-01', 'follow_leader_semifinal'),
  (10028, 1998, 'IWF Kids State Championships', '', '1998-03-01', '1998-03-01', 'follow_leader_semifinal'),
  (10029, 1999, 'IWF Kids State Championships', '', '1999-03-19', '1999-03-20', 'follow_leader_semifinal'),
  (10030, 2000, 'IWF Kids State Championships', '', '2000-03-10', '2000-03-11', 'follow_leader_semifinal'),
  (10031, 2001, 'IWF Kids State Championships', '', '2001-03-09', '2001-03-10', 'follow_leader_semifinal');

--------------------------------------------------------------------------------

INSERT INTO
  bracket (id, weight, division, tournament_id)
VALUES
  -- 1971
  (1041, 60, 'senior', 1),
  (1042, 65, 'senior', 1),
  (1043, 70, 'senior', 1),
  (1044, 77, 'senior', 1),
  (1045, 83, 'senior', 1),
  (1046, 90, 'senior', 1),
  (1047, 97, 'senior', 1),
  (1048, 105, 'senior', 1),
  (1049, 112, 'senior', 1),
  (1050, 118, 'senior', 1),
  (1051, 125, 'senior', 1),
  (1052, 132, 'senior', 1),
  (1053, 138, 'senior', 1),
  (1054, 145, 'senior', 1),
  (1055, 152, 'senior', 1),
  (1056, 275, 'senior', 1),
  -- 1972
  (1057, 60, 'senior', 2),
  (1058, 65, 'senior', 2),
  (1059, 70, 'senior', 2),
  (1060, 77, 'senior', 2),
  (1061, 83, 'senior', 2),
  (1062, 90, 'senior', 2),
  (1063, 97, 'senior', 2),
  (1064, 105, 'senior', 2),
  (1065, 112, 'senior', 2),
  (1066, 118, 'senior', 2),
  (1067, 125, 'senior', 2),
  (1068, 132, 'senior', 2),
  (1069, 138, 'senior', 2),
  (1070, 145, 'senior', 2),
  (1071, 152, 'senior', 2),
  (1072, 275, 'senior', 2);
