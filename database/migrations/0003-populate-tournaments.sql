-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  tournament (id, year, name, location, start_date, end_date)
VALUES
  (31, 2000, 'IKWF State Championships',               'SIU Arena (Carbondale)',            '2000-03-09', '2000-03-11'),
  (32, 2001, 'IKWF State Championships',               'SIU Arena (Carbondale)',            '2001-03-08', '2001-03-10'),
  (33, 2002, 'IKWF State Championships',               'SIU Arena (Carbondale)',            '2002-03-08', '2002-03-09'),
  -- Junior State Championships: 2002-03-15 to 2002-03-17
  (34, 2003, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2003-03-14', '2003-03-15'),
  (35, 2004, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2004-03-12', '2004-03-13'),
  (36, 2005, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2005-03-11', '2005-03-12'),
  (37, 2006, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2006-03-10', '2006-03-11'),
  (38, 2007, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2007-03-10', '2007-03-10'),
  (39, 2008, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2008-03-08', '2008-03-08'),
  (40, 2009, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2009-03-12', '2009-03-14'),
  (41, 2010, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2010-03-12', '2010-03-13'),
  (42, 2011, 'IKWF State Championships',               'MetroCentre (Rockford)',            '2011-03-11', '2011-03-12'),
  (43, 2012, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2012-03-09', '2012-03-12'),
  (44, 2013, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2013-03-08', '2013-03-09'),
  (45, 2014, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2014-03-13', '2014-03-15'),
  (46, 2015, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2015-03-13', '2015-03-14'),
  (47, 2016, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2016-03-10', '2016-03-12'),
  (48, 2017, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2017-03-09', '2017-03-11'),
  (49, 2018, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2018-03-08', '2018-03-10'),
  (50, 2019, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2019-03-08', '2019-03-09'),
  (51, 2020, 'IKWF State Championships (CANCELLED)',   'BMO Harris Bank Center (Rockford)', '2020-03-13', '2020-03-14'),
  (52, 2022, 'IKWF State Championships',               'BMO Harris Bank Center (Rockford)', '2022-03-11', '2022-03-12'),
  (53, 2023, 'IKWF State Championships',               'BMO Center (Rockford)',             '2023-03-10', '2023-03-11'),
  (54, 2024, 'IKWF Senior/Novice State Championships', 'BMO Center (Rockford)',             '2024-03-08', '2024-03-09'),
  (55, 2024, 'IKWF Int/Ban State Championships',       'Civic Center (Decatur)',            '2024-03-16', '2024-03-17'),
  (56, 2025, 'IKWF State Championships',               'Civic Center (Peoria)',             '2025-03-07', '2025-03-08');
