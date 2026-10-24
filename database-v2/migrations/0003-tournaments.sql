-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  tournament (id, year, name, location, start_date, end_date, bracket_type)
VALUES
  (1, 1971, 'Illinois Wrestling Federation State Championship', 'Apollo Jr. High (Des Plaines)', '1971-03-01', '1971-03-01', '16_follow_leader_semifinal_place6'), -- Most fields not verified: `name`, `location`, `start_date`, `end_date`, `bracket_type`
  (2, 1972, 'Illinois Wrestling Federation Junior Program State Finals', 'Maine North HS (Des Plaines)', '1972-03-11', '1972-03-11', '16_follow_leader_semifinal_place6'), -- Not verified: `bracket_type`
  (3, 1973, 'Illinois Wrestling Federation State Championship', 'Maine North HS (Des Plaines)', '1973-03-01', '1973-03-01', '16_follow_leader_semifinal_place6'), -- Most fields not verified: `name`, `location`, `start_date`, `end_date`, `bracket_type`
  (4, 1974, 'Illinois Wrestling Federation Kids Program State Finals', 'Maine North HS (Des Plaines)', '1974-03-16', '1974-03-16', '16_follow_leader_semifinal_place6'),
  (5, 1975, 'Illinois Wrestling Federation State Championship', 'DeKalb HS', '1975-03-01', '1975-03-01', '16_follow_leader_semifinal_place6'), -- Most fields not verified: `name`, `location`, `start_date`, `end_date`, `bracket_type`
  (6, 1976, 'Illinois Wrestling Federation State Championship', 'Mattoon HS', '1976-03-01', '1976-03-01', '16_follow_leader_semifinal_place6'), -- Most fields not verified: `name`, `location`, `start_date`, `end_date`, `bracket_type`
  (7, 1977, 'Illinois Kids Wrestling Federation State Finals', 'East Moline HS', '1977-03-01', '1977-03-01', '16_follow_leader_semifinal_place6'), -- Most fields not verified: `location`, `start_date`, `end_date`, `bracket_type`
  (8, 1978, 'ILLINOIS "KID" WRESTLING FEDERATION State Finals', 'McArthur HS (Decatur)', '1978-03-17', '1978-03-18', '24_follow_leader_semifinal_place6'), -- Not verified: `bracket_type`
  (9, 1979, 'Illinois "Kid" Wrestling Federation State Finals', 'Joliet Central HS', '1979-03-16', '1979-03-17', '24_follow_leader_semifinal_place6'), -- Not verified: `bracket_type`
  (10, 1980, 'Illinois Wrestling Federation State Championship', 'McArthur HS (Decatur)', '1980-03-21', '1980-03-22', '24_follow_leader_semifinal_place6'), -- Most fields not verified: `name`, `location`, `bracket_type`
  (11, 1981, 'Illinois Kids Wrestling Federation State Championship', 'McGaw Hall (Northwestern U, Evanston)', '1981-03-20', '1981-03-21', '24_follow_leader_semifinal_place6'),
  (12, 1982, 'Illinois Kids Wrestling Federation State Championship', 'Harper College (Palatine)', '1982-03-26', '1982-03-27', '24_follow_leader_semifinal_place6'),
  (13, 1983, 'Illinois Kids Wrestling Federation State Championship', 'NIU', '1983-03-18', '1983-03-19', '24_follow_leader_semifinal_place6'),
  (14, 1984, 'Illinois Kids Wrestling Federation State Championship', 'NIU', '1984-03-16', '1984-03-17', '24_follow_leader_semifinal_place6'),
  (15, 1985, 'Illinois Kids Wrestling Federation State Championship', 'SIU Edwardsville', '1985-03-15', '1985-03-16', '24_follow_leader_semifinal_place6'),
  (16, 1986, 'Illinois Kids Wrestling Federation State Championship', 'NIU', '1986-03-21', '1986-03-22', '24_follow_leader_semifinal_place6'),
  (17, 1987, 'Illinois Kids Wrestling Federation State Championship', 'SIU Edwardsville', '1987-03-13', '1987-03-14', '24_follow_leader_semifinal_place6'),
  (18, 1988, 'Illinois Kids Wrestling Federation State Championship', 'NIU', '1988-03-11', '1988-03-12', '24_follow_leader_semifinal_place6'),
  (19, 1989, 'Illinois Kids Wrestling Federation State Championships', 'SIU Edwardsville', '1989-03-10', '1989-03-11', '24_follow_leader_semifinal_place6'),
  (20, 1990, 'Illinois Kids Wrestling Federation State Championships', 'Prairie Capital Convention Center (Springfield)', '1990-03-23', '1990-03-24', '24_follow_leader_semifinal_place6'),
  (21, 1991, 'Illinois Kids Wrestling Federation State Championships', 'Prairie Capital Convention Center (Springfield)', '1991-03-22', '1991-03-23', '24_follow_leader_semifinal_place6'),
  (22, 1992, 'Illinois Kids Wrestling Federation State Championship', 'Prairie Capital Convention Center (Springfield)', '1992-03-27', '1992-03-28', '24_follow_leader_semifinal_place6'),
  (23, 1993, 'Illinois Kids Wrestling Federation State Championship', 'Redbird Arena (Normal)', '1991-03-26', '1993-03-27', '24_follow_leader_semifinal_place6'),
  (24, 1994, 'Illinois Kids Wrestling Federation State Championship', 'Redbird Arena (Normal)', '1994-03-25', '1994-03-26', '24_follow_leader_semifinal_place6'),
  (25, 1995, 'Illinois Kids Wrestling Federation State Finals', 'Redbird Arena (Normal)', '1995-03-24', '1995-03-25', '24_follow_leader_semifinal_place6'),
  (26, 1996, 'IKWF State Finals', 'The Mark of the Quad Cities (Moline)', '1996-03-08', '1996-03-09', '24_follow_leader_semifinal_place6'),
  (27, 1997, 'IKWF State Finals', 'The Mark of the Quad Cities (Moline)', '1997-03-14', '1997-03-15', '24_follow_leader_semifinal_place6'),
  (28, 1998, 'IKWF State Finals', 'The Mark of the Quad Cities (Moline)', '1998-03-11', '1998-03-12', '24_follow_leader_semifinal_place6'),
  (10028, 1998, 'IWF Kids State Championships', '', '1998-03-01', '1998-03-01', '16_full_wrestleback_place6'), -- `location` not verified
  (29, 1999, 'IKWF State Championships', 'SIU Arena (Carbondale)', '1999-03-12', '1999-03-13', '24_follow_leader_semifinal_place6'),
  (10029, 1999, 'IWF Kids State Championships', '', '1999-03-19', '1999-03-20', '16_full_wrestleback_place6'), --`location` not verified
  (30, 2000, 'IKWF State Finals', 'SIU Arena (Carbondale)', '2000-03-09', '2000-03-11', '24_follow_leader_semifinal_place6'),
  (10030, 2000, 'IWF Kids State Championships', '', '2000-03-10', '2000-03-11', '16_full_wrestleback_place6'), -- `location` not verified
  (31, 2001, 'IKWF State Finals', 'SIU Arena (Carbondale)', '2001-03-08', '2001-03-10', '24_follow_leader_semifinal_place8'),
  (10031, 2001, 'IWF Kids State Championships', '', '2001-03-09', '2001-03-10', '16_full_wrestleback_place6'), -- `location` not verified
  (32, 2002, 'IKWF State Finals', 'SIU Arena (Carbondale)', '2002-03-08', '2002-03-09', '24_follow_leader_semifinal_place8'),
  (33, 2003, 'IKWF State Finals', 'MetroCentre (Rockford)', '2003-03-14', '2003-03-15', '24_follow_leader_semifinal_place8'),
  (34, 2004, 'IKWF State Finals', 'MetroCentre (Rockford)', '2004-03-12', '2004-03-13', '24_follow_leader_semifinal_place8'),
  (35, 2005, 'IKWF State Finals', 'MetroCentre (Rockford)', '2005-03-11', '2005-03-12', '24_follow_leader_semifinal_place8'),
  (36, 2006, 'IKWF State Finals', 'MetroCentre (Rockford)', '2006-03-10', '2006-03-11', '24_follow_leader_semifinal_place8'),
  (37, 2007, 'IKWF State Finals', 'MetroCentre (Rockford)', '2007-03-09', '2007-03-10', '24_follow_leader_semifinal_place8'),
  (38, 2008, 'IKWF State Finals', 'MetroCentre (Rockford)', '2008-03-07', '2008-03-08', '24_follow_leader_semifinal_place8'),
  (39, 2009, 'IKWF State Finals', 'MetroCentre (Rockford)', '2009-03-13', '2009-03-14', '24_follow_leader_semifinal_place8'),
  (40, 2010, 'IKWF State Finals', 'MetroCentre (Rockford)', '2010-03-12', '2010-03-13', '24_follow_leader_semifinal_place8'),
  (41, 2011, 'IKWF State Wrestling Finals', 'MetroCentre (Rockford)', '2011-03-11', '2011-03-12', '24_follow_leader_semifinal_place8'),
  (42, 2012, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2012-03-10', '2012-03-12', '24_follow_leader_semifinal_place8'),
  (43, 2013, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2013-03-08', '2013-03-09', '24_follow_leader_semifinal_place8'),
  (44, 2014, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2014-03-14', '2014-03-15', '24_follow_leader_semifinal_place8'),
  (45, 2015, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2015-03-13', '2015-03-14', '24_follow_leader_semifinal_place8'),
  (46, 2016, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2016-03-11', '2016-03-12', '24_follow_leader_semifinal_place8'),
  (47, 2017, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2017-03-10', '2017-03-11', '24_follow_leader_semifinal_place8'),
  (48, 2018, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2018-03-09', '2018-03-10', '24_follow_leader_semifinal_place8'),
  (49, 2019, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2019-03-08', '2019-03-09', '24_follow_leader_semifinal_place8'),
  (10050, 2020, 'IKWF State Finals (CANCELLED)', 'BMO Harris Bank Center (Rockford)', '2020-03-13', '2020-03-14', '24_follow_leader_semifinal_place8'),
  (50, 2022, 'IKWF State Finals', 'BMO Harris Bank Center (Rockford)', '2022-03-11', '2022-03-12', '24_full_wrestleback_place8'),
  (51, 2023, 'IKWF State Finals', 'BMO Center (Rockford)', '2023-03-10', '2023-03-11', '24_full_wrestleback_place8'),
  (52, 2024, 'IKWF Senior/Novice State Championships', 'BMO Center (Rockford)', '2024-03-08', '2024-03-09', '24_full_wrestleback_place8'),
  (10052, 2024, 'IKWF Int/Ban State Championships', 'Civic Center (Decatur)', '2024-03-16', '2024-03-17', '24_full_wrestleback_place8'),
  (53, 2025, 'IKWF State Wrestling Finals', 'Civic Center (Peoria)', '2025-03-07', '2025-03-08', '24_full_wrestleback_place8'),
  (54, 2026, 'IKWF State Finals', 'Civic Center (Peoria)', '2026-03-13', '2026-03-14', '24_full_wrestleback_place8');
