-- Copyright (c) 2025 - Present. IKWF History. All rights reserved.

PRAGMA foreign_keys = ON;
PRAGMA encoding = 'UTF-8';
PRAGMA integrity_check;

--------------------------------------------------------------------------------

INSERT INTO
  competitor (id, first_name, last_name, suffix)
VALUES
  (25,  'Tim',       'Haneberg',    NULL),
  (26,  'Scott',     'Horcher',     NULL),
  (27,  'Thomas',    'Gagan',       NULL),
  (28,  'Dalton',    'Bullard',     NULL),
  (29,  'Brian',     'Spangler',    NULL),
  (30,  'Steve',     'Templin',     NULL),
  (31,  'Nick',      'Fanthorpe',   NULL),
  (32,  'Brian',     'Martin',      NULL),
  (33,  'Josh',      'Harper',      NULL),
  (34,  'Matt',      'Cusick',      NULL),
  (35,  'Mitch',     'Jones',       NULL),
  (36,  'Adam',      'Canty',       NULL),
  (37,  'Michael',   'Benefiel',    NULL),
  (38,  'Conor',     'Beebe',       NULL),
  (39,  'Marcus',    'White',       NULL),
  (40,  'Brandon',   'Nice',        NULL),
  (41,  'Tyler',     'Babcock',     NULL),
  (42,  'Matt',      'Shapiro',     NULL),
  (43,  'Gerald',    'Starzyk',     NULL),
  (44,  'Mike',      'Riley',       NULL),
  (45,  'Chuckie',   'Patten',      NULL),
  (46,  'Nate',      'Britt',       NULL),
  (47,  'Michael',   'Anello',      NULL),
  (48,  'Billy',     'Cascone',     NULL),
  (49,  'Kyle',      'Krueger',     NULL),
  (50,  'Robbie',    'Unsell',      NULL),
  (51,  'Danny',     'Ruettiger',   NULL),
  (52,  'Jon',       'Isacson',     NULL),
  (53,  'Jacob',     'Murphy',      NULL),
  (54,  'Carlos',    'Lopez',       NULL),
  (55,  'Marty',     'Engwall',     NULL),
  (56,  'Scott',     'Sheber',      NULL),
  (57,  'Nick',      'Marinaro',    NULL),
  (58,  'Brad',      'Fiorito',     NULL),
  (59,  'Gary',      'Conrad',      NULL),
  (60,  'Bobby',     'Wolf',        NULL),
  (61,  'Michael',   'Poeta',       NULL),
  (62,  'Jefferi',   'Broadway',    NULL),
  (63,  'Scott',     'Sands',       NULL),
  (64,  'Zach',      'Enderle',     NULL),
  (65,  'Billy',     'Dragonetti',  NULL),
  (66,  'Scott',     'DeChant',     NULL),
  (67,  'Clayton',   'Norberg',     NULL),
  (68,  'Shane',     'Dintelman',   NULL),
  (69,  'Mark',      'Lukaszewski', NULL),
  (70,  'Tim',       'Golden',      NULL),
  (71,  'Joseph',    'Graves',      NULL),
  (72,  'Matt',      'Wenger',      NULL),
  (73,  'Steven',    'Rodgers',     NULL),
  (74,  'Matthew',   'Smith',       NULL),
  (75,  'Brandon',   'Lozdowski',   NULL),
  (76,  'John',      'Murphy',      NULL),
  (77,  'Will',      'Mekeel',      NULL),
  (78,  'Aaron',     'Lipe',        NULL),
  (79,  'Mike',      'Mucha',       NULL),
  (80,  'Austin',    'Jones',       NULL),
  (81,  'Drew',      'Jones',       NULL),
  (82,  'Robert',    'Wallon',      NULL),
  (83,  'Nathan',    'Troye',       NULL),
  (84,  'Michael',   'McIntyre',    NULL),
  (85,  'Andrew',    'Zidow',       NULL),
  (86,  'Ryan',      'Bittle',      NULL),
  (87,  'Chris',     'Smith',       NULL),
  (88,  'Joshua',    'Mohr',        NULL),
  (89,  'Dan',       'Haeflinger',  NULL),
  (90,  'Jon',       'Crettol',     NULL),
  (91,  'Liam',      'Kelly',       NULL),
  (92,  'Jared',     'Sugden',      NULL),
  (93,  'Kyle',      'Williams',    NULL),
  (94,  'Phil',      'Grant',       NULL),
  (95,  'Jason',     'Johnson',     NULL),
  (96,  'Keith',     'Hauter',      NULL),
  (97,  'De''Andre', 'Nunn',        NULL),
  (98,  'Buddy',     'Dudczak',     NULL),
  (99,  'Billy',     'Pyszka',      NULL),
  (100, 'Nicholas',  'Miller',      NULL),
  (101, 'Jonathan',  'Wyatt',       NULL),
  (102, 'Ryan',      'Francis',     NULL),
  (103, 'Shane',     'Butler',      NULL),
  (104, 'Jesus',     'Ordaz',       NULL),
  (105, 'Marcus',    'McDowell',    NULL),
  (106, 'Jeffrey',   'Janicki',     NULL),
  (107, 'Joe',       'Youngberg',   NULL),
  (108, 'Gary',      'Cox',         NULL),
  (109, 'Chris',     'Espinoza',    NULL),
  (110, 'Brian',     'Kerr',        NULL),
  (111, 'Jim',       'Huffman',     NULL),
  (112, 'Christian', 'Bunyan',      NULL),
  (113, 'Casey',     'Hicks',       NULL),
  (114, 'Mike',      'Scheibel',    NULL),
  (115, 'Rusty',     'Wheat',       NULL),
  (116, 'Ray',       'Stuthers',    NULL),
  (117, 'Brandon',   'Sutton',      NULL),
  (118, 'Ben',       'Lawrence',    NULL),
  (119, 'Vinnie',    'Salmieri',    NULL),
  (120, 'Ryan',      'Weaver',      NULL),
  (121, 'David',     'Murphy',      NULL),
  (122, 'Cody',      'Dietze',      NULL),
  (123, 'Brandon',   'Zerfowski',   NULL),
  (124, 'Scott',     'Eichberger',  NULL),
  (125, 'John',      'Wienert',     NULL),
  (126, 'Jerry',     'Fischer',     NULL),
  (127, 'Jordan',    'Kolinski',    NULL),
  (128, 'Eric',      'Bauer',       NULL),
  (129, 'Daniel',    'Leonard',     NULL),
  (130, 'Josiah',    'Wooten',      NULL),
  (131, 'Tony',      'Martinez',    NULL),
  (132, 'Chris',     'Maynor',      NULL),
  (133, 'Josh',      'Taylor',      NULL),
  (134, 'Brad',      'Medchill',    NULL),
  (135, 'Dan',       'Manzella',    NULL),
  (136, 'Justin',    'Grey',        NULL),
  (137, 'Steve',     'Scrementi',   NULL),
  (138, 'Shane',     'Saylor',      NULL),
  (139, 'Brian',     'Dyer',        NULL),
  (140, 'Justin',    'Haskett',     NULL),
  (141, 'Brad',      'Dargan',      NULL),
  (142, 'Tony',      'Emma',        NULL),
  (143, 'Thomas',    'Tapia',       NULL),
  (144, 'Branden',   'Mackey',      NULL),
  (145, 'Pat',       'Barth',       NULL),
  (146, 'Zac',       'Berman',      NULL),
  (147, 'Ryan',      'Kimberlin',   NULL),
  (148, 'Kevin',     'McNicholas',  NULL),
  (149, 'Michael',   'Reese',       NULL),
  (150, 'Chad',      'Vandiver',    NULL),
  (151, 'Chase',     'Beebe',       NULL),
  (152, 'Robert',    'Loftus',      NULL),
  (153, 'Kevin',     'Sheber',      NULL),
  (154, 'Andrew',    'Lukanich',    NULL),
  (155, 'Adam',      'Beeler',      NULL),
  (156, 'Mike',      'Whalen',      NULL),
  (157, 'Eric',      'Tannenbaum',  NULL),
  (158, 'Ryan',      'Klinger',     NULL),
  (159, 'Bob',       'McClellan',   NULL),
  (160, 'Jacob',     'Jones',       NULL),
  (161, 'Ryan',      'Giulano',     NULL),
  (162, 'Ryne',      'Bird',        NULL),
  (163, 'Collin',    'McKillip',    NULL),
  (164, 'Joe',       'Gomez',       NULL),
  (165, 'Matt',      'Wellner',     NULL),
  (166, 'Matt',      'Collum',      NULL),
  (167, 'Mitch',     'Fonner',      NULL),
  (168, 'Matt',      'Anderson',    NULL),
  (169, 'Jakob',     'Bottoms',     NULL),
  (170, 'Ryan',      'DeVriendt',   NULL),
  (171, 'Tyler',     'Williams',    NULL),
  (172, 'Roberto',   'Torres',      NULL),
  (173, 'Drew',      'McMahon',     NULL),
  (174, 'Matthew',   'Wahl',        NULL),
  (175, 'Ruben',     'Villareal',   NULL),
  (176, 'Michael',   'Pila',        NULL),
  (177, 'Bryan',     'Casey',       NULL),
  (178, 'David',     'Kuntz',       NULL),
  (179, 'Jake',      'Mekeel',      NULL),
  (180, 'Jeremy',    'Doss',        NULL),
  (181, 'Bryan',     'Harney',      NULL),
  (182, 'Josh',      'Bednarek',    NULL),
  (183, 'Ben',       'Murray',      NULL),
  (184, 'Josh',      'Hartman',     NULL),
  (185, 'Tyler',     'Worthington', NULL),
  (186, 'Mike',      'Kerr',        NULL),
  (187, 'Mark',      'Mendoza',     NULL),
  (188, 'Marty',     'Cox',         NULL),
  (189, 'Justin',    'Ochoa',       NULL),
  (190, 'Rick',      'Hoke',        NULL),
  (191, 'Bill',      'Smith',       NULL),
  (192, 'Kevin',     'Tobola',      NULL),
  (193, 'Danney',    'Finney',      NULL),
  (194, 'Kris',      'Roberts',     NULL),
  (195, 'Adam',      'Clay',        NULL),
  (196, 'Byran',     'Golden',      NULL),
  (197, 'Nick',      'Derry',       NULL),
  (198, 'Adam',      'Hock',        NULL),
  (199, 'Evan',      'McCallister', NULL),
  (200, 'Kevin',     'Brush',       NULL),
  (201, 'Patrick',   'Brownson',    NULL),
  (202, 'Derek',     'Hunsinger',   NULL),
  (203, 'Sonny',     'Lambert',     NULL),
  (204, 'Eric',      'Vari',        NULL),
  (205, 'Terry',     'Burner',      NULL),
  (206, 'Chris',     'Norberg',     NULL),
  (207, 'Roberto',   'Chavira',     NULL),
  (208, 'Jason',     'DePolo',      NULL),
  (209, 'Dustin',    'Jackson',     NULL),
  (210, 'Oscar',     'Herrara',     NULL),
  (211, 'Jason',     'Ortiz',       NULL),
  (212, 'Mario',     'Caraveo',     NULL),
  (213, 'Freddie',   'Deramus',     NULL),
  (214, 'Matthew',   'Barron',      NULL),
  (215, 'Rashad',    'Stewart',     NULL),
  (216, 'Chris',     'Johnston',    NULL),
  (217, 'Murphy',    'Mahalik',     NULL),
  (218, 'Zach',      'Schroeder',   NULL),
  (219, 'Grant',     'Miller',      NULL),
  (220, 'Matthew',   'Stern',       NULL),
  (221, 'Michael',   'Minton',      NULL),
  (222, 'Caleb',     'Bridges',     NULL),
  (223, 'Kyle',      'Crotty',      NULL),
  (224, 'Robert',    'Taylor',      NULL),
  (225, 'Ron',       'Pena',        NULL),
  (226, 'Ben',       'Bradfield',   NULL),
  (227, 'Matt',      'Richards',    NULL),
  (228, 'Charles',   'Doerge',      NULL);

--------------------------------------------------------------------------------

INSERT INTO
  team (name, id)
VALUES
  ('Montego Matmen',       10117),
  ('Bethalto Junior High', 10118),
  ('St. Barnabas/CTK',     10119),
  ('Wheaton Bulldogs',     10120),
  ('East Moline WC',       10121),
  ('Pinckneyville WC',     10122),
  ('Urbana Kids Club',     10123),
  ('Champaign Chargers',   10124),
  ('Rock Island Edison',   10125),
  ('Brownson WC',          10126),
  ('PLT Prophets',         10127),
  ('Chenoa WC',            10128),
  ('Mustangs WC',          10129),
  ('Marion WC',            10130),
  ('Edison Panthers WC',   10131); -- Wheaton


--------------------------------------------------------------------------------

INSERT INTO
  team_competitor (id, competitor_id, team_id)
VALUES
  (25,  25,  306  ),
  (26,  26,  10050),
  (27,  27,  233  ),
  (28,  28,  24   ),
  (29,  29,  134  ),
  (30,  30,  10117),
  (31,  31,  134  ),
  (32,  32,  490  ),
  (33,  33,  23   ),
  (34,  34,  306  ),
  (35,  35,  276  ),
  (36,  36,  466  ),
  (37,  37,  134  ),
  (38,  38,  134  ),
  (39,  39,  233  ),
  (40,  40,  90   ),
  (41,  41,  10118),
  (42,  42,  134  ),
  (43,  43,  466  ),
  (44,  44,  443  ),
  (45,  45,  10018),
  (46,  46,  10098),
  (47,  47,  306  ),
  (48,  48,  466  ),
  (49,  49,  134  ),
  (50,  50,  10118),
  (51,  51,  233  ),
  (52,  52,  10109),
  (53,  53,  443  ),
  (54,  54,  466  ),
  (55,  55,  443  ),
  (56,  56,  219  ),
  (57,  57,  10041),
  (58,  58,  102  ),
  (59,  59,  490  ),
  (60,  60,  10118),
  (61,  61,  10043),
  (62,  62,  233  ),
  (63,  63,  443  ),
  (64,  64,  10041),
  (65,  65,  490  ),
  (66,  66,  233  ),
  (67,  67,  10098),
  (68,  68,  23   ),
  (69,  69,  10109),
  (70,  70,  466  ),
  (71,  71,  10005),
  (72,  72,  92   ),
  (73,  73,  10118),
  (74,  74,  10109),
  (75,  75,  10041),
  (76,  76,  10119),
  (77,  77,  10098),
  (78,  78,  10030),
  (79,  79,  219  ),
  (80,  80,  37   ),
  (81,  81,  173  ),
  (82,  82,  219  ),
  (83,  83,  10098),
  (84,  84,  10089),
  (85,  85,  241  ),
  (86,  86,  10001),
  (87,  87,  326  ),
  (88,  88,  497  ),
  (89,  89,  161  ),
  (90,  90,  306  ),
  (91,  91,  443  ),
  (92,  92,  8    ),
  (93,  93,  134  ),
  (94,  94,  89   ),
  (95,  95,  10098),
  (96,  96,  231  ),
  (97,  97,  233  ),
  (98,  98,  10109),
  (99,  99,  241  ),
  (100, 100, 252  ),
  (101, 101, 482  ),
  (102, 102, 219  ),
  (103, 103, 263  ),
  (104, 104, 89   ),
  (105, 105, 252  ),
  (106, 106, 10109),
  (107, 107, 278  ),
  (108, 108, 461  ),
  (109, 109, 10120),
  (110, 110, 10121),
  (111, 111, 10109),
  (112, 112, 10123),
  (113, 113, 10082),
  (114, 114, 168  ),
  (115, 115, 371  ),
  (116, 116, 278  ),
  (117, 117, 10122),
  (118, 118, 10018),
  (119, 119, 8    ),
  (120, 120, 6    ),
  (121, 121, 233  ),
  (122, 122, 443  ),
  (123, 123, 276  ),
  (124, 124, 306  ),
  (125, 125, 466  ),
  (126, 126, 272  ),
  (127, 127, 364  ),
  (128, 128, 134  ),
  (129, 129, 10109),
  (130, 130, 10123),
  (131, 131, 233  ),
  (132, 132, 10092),
  (133, 133, 441  ),
  (134, 134, 10109),
  (135, 135, 466  ),
  (136, 136, 443  ),
  (137, 137, 233  ),
  (138, 138, 10118),
  (139, 139, 134  ),
  (140, 140, 443  ),
  (141, 141, 89   ),
  (142, 142, 10114),
  (143, 143, 10121),
  (144, 144, 10123),
  (145, 145, 272  ),
  (146, 146, 233  ),
  (147, 147, 37   ),
  (148, 148, 466  ),
  (149, 149, 241  ),
  (150, 150, 10041),
  (151, 151, 134  ),
  (152, 152, 497  ),
  (153, 153, 219  ),
  (154, 154, 466  ),
  (155, 155, 110  ),
  (156, 156, 110  ),
  (157, 157, 134  ),
  (158, 158, 10075),
  (159, 159, 443  ),
  (160, 160, 276  ),
  (161, 161, 490  ),
  (162, 162, 441  ),
  (163, 163, 443  ),
  (164, 164, 10109),
  (165, 165, 134  ),
  (166, 166, 134  ),
  (167, 167, 252  ),
  (168, 168, 10041),
  (169, 169, 278  ),
  (170, 170, 383  ),
  (171, 171, 10109),
  (172, 172, 134  ),
  (173, 173, 10124),
  (174, 174, 10050),
  (175, 175, 134  ),
  (176, 176, 306  ),
  (177, 177, 219  ),
  (178, 178, 466  ),
  (179, 179, 10098),
  (180, 180, 10002),
  (181, 181, 466  ),
  (182, 182, 89   ),
  (183, 183, 37   ),
  (184, 184, 10052),
  (185, 185, 10128),
  (186, 186, 10121),
  (187, 187, 134  ),
  (188, 188, 497  ),
  (189, 189, 10005),
  (190, 190, 383  ),
  (191, 191, 10129),
  (192, 192, 443  ),
  (193, 193, 233  ),
  (194, 194, 10130),
  (195, 195, 134  ),
  (196, 196, 466  ),
  (197, 197, 10041),
  (198, 198, 10033),
  (199, 199, 354  ),
  (200, 200, 443  ),
  (201, 201, 10126),
  (202, 202, 10022),
  (203, 203, 457  ),
  (204, 204, 134  ),
  (205, 205, 64   ),
  (206, 206, 10098),
  (207, 207, 24   ),
  (208, 208, 233  ),
  (209, 209, 461  ),
  (210, 210, 10125),
  (211, 211, 134  ),
  (212, 212, 10125),
  (213, 213, 466  ),
  (214, 214, 10127),
  (215, 215, 10124),
  (216, 216, 3    ),
  (217, 217, 233  ),
  (218, 218, 10014),
  (219, 219, 10041),
  (220, 220, 10109),
  (221, 221, 6    ),
  (222, 222, 397  ),
  (223, 223, 371  ),
  (224, 224, 397  ),
  (225, 225, 134  ),
  (226, 226, 28   ),
  (227, 227, 10131),
  (228, 228, 110  );

--------------------------------------------------------------------------------

INSERT INTO
  match (id, bracket_id, bout_number, match_slot, top_competitor_id, bottom_competitor_id, top_win, result, top_team_acronym, bottom_team_acronym)
VALUES
  -- bracket_id=1004 (Novice 62)
  -- 1st - Tim Haneberg - Orland Park
  -- 2nd - Scott Horcher - Jr. Golden Eagles
  -- 3rd - Thomas Gagan - Little Celtics
  -- 4th - Dalton Bullard - Belvidere Bandits
  -- 5th - Brian Spangler - Fox Valley WC
  -- 6th - Steve Templin - Montego Matmen
  (55, 1004, NULL, 'championship_first_place', 25, 26, TRUE, '', NULL, NULL),
  (56, 1004, NULL, 'consolation_third_place',  27, 28, TRUE, '', NULL, NULL),
  (57, 1004, NULL, 'consolation_fifth_place',  29, 30, TRUE, '', NULL, NULL),
  -- bracket_id=1005 (Novice 66)
  -- 1st - Nick Fanthorpe - Fox Valley WC
  -- 2nd - Brian Martin - Wolfpak WC
  -- 3rd - Josh Harper - Belleville L.D.
  -- 4th - Matt Cusick - Orland Park
  -- 5th - Mitch Jones - Mt. Zion WC
  -- 6th - Adam Canty - Vittum Cats
  (58, 1005, NULL, 'championship_first_place', 31, 32, TRUE, '', NULL, NULL),
  (59, 1005, NULL, 'consolation_third_place',  33, 34, TRUE, '', NULL, NULL),
  (60, 1005, NULL, 'consolation_fifth_place',  35, 36, TRUE, '', NULL, NULL),
  -- bracket_id=1006 (Novice 70)
  -- 1st - Michael Benefiel - Fox Valley WC
  -- 2nd - Conor Beebe - Fox Valley WC
  -- 3rd - Marcus White - Little Celtics
  -- 4th - Brandon Nice - Cumberland WC
  -- 5th - Tyler Babcock - Bethalto Jr. High
  -- 6th - Matt Shapiro - Fox Valley WC
  (61, 1006, NULL, 'championship_first_place', 37, 38, TRUE, '', NULL, NULL),
  (62, 1006, NULL, 'consolation_third_place',  39, 40, TRUE, '', NULL, NULL),
  (63, 1006, NULL, 'consolation_fifth_place',  41, 42, TRUE, '', NULL, NULL),
  -- bracket_id=1007 (Novice 74)
  -- 1st - Gerald Starzyk - Vittum Cats
  -- 2nd - Mike Riley - Tinley Park
  -- 3rd - Chuckie Patten - Crossface WC
  -- 4th - Nate Britt - Sterling-Newman
  -- 5th - Michael Anello - Orland Park
  -- 6th - Billy Cascone - Vittum Cats
  (64, 1007, NULL, 'championship_first_place', 43, 44, TRUE, '', NULL, NULL),
  (65, 1007, NULL, 'consolation_third_place',  45, 46, TRUE, '', NULL, NULL),
  (66, 1007, NULL, 'consolation_fifth_place',  47, 48, TRUE, '', NULL, NULL),
  -- bracket_id=1008 (Novice 79)
  -- 1st - Kyle Krueger - Fox Valley WC
  -- 2nd - Robbie Unsell - Bethalto Jr. High
  -- 3rd - Danny Ruettiger - Little Celtic WC
  -- 4th - Jon Isacson - Villa-Lombard
  -- 5th - Jacob Murphy - Tinley Park
  -- 6th - Carlos Lopez - Vittum Cats
  (67, 1008, NULL, 'championship_first_place', 49, 50, TRUE, '', NULL, NULL),
  (68, 1008, NULL, 'consolation_third_place',  51, 52, TRUE, '', NULL, NULL),
  (69, 1008, NULL, 'consolation_fifth_place',  53, 54, TRUE, '', NULL, NULL),
  -- bracket_id=1009 (Novice 84)
  -- 1st - Marty Engwall - Tinley Park
  -- 2nd - Scott Sheber - Lemont Bears
  -- 3rd - Nick Marinaro - Harlem Cougars
  -- 4th - Brad Fiorito - Dundee Highlanders
  -- 5th - Gary Conrad - Wolfpak WC
  -- 6th - Bobby Wolf - Bethalto Jr. High
  (70, 1009, NULL, 'championship_first_place', 55, 56, TRUE, '', NULL, NULL),
  (71, 1009, NULL, 'consolation_third_place',  57, 58, TRUE, '', NULL, NULL),
  (72, 1009, NULL, 'consolation_fifth_place',  59, 60, TRUE, '', NULL, NULL),
  -- bracket_id=1010 (Novice 89)
  -- 1st - Michael Poeta - Highland Park
  -- 2nd - Jefferi Broadway - Little Celtics
  -- 3rd - Scott Sands - Tinley Park
  -- 4th - Zach Enderle - Harlem Cougars
  -- 5th - Billy Dragonetti - Wolfpak WC
  -- 6th - Scott DeChant - Little Celtics
  (73, 1010, NULL, 'championship_first_place', 61, 62, TRUE, '', NULL, NULL),
  (74, 1010, NULL, 'consolation_third_place',  63, 64, TRUE, '', NULL, NULL),
  (75, 1010, NULL, 'consolation_fifth_place',  65, 66, TRUE, '', NULL, NULL),
  -- bracket_id=1011 (Novice 95)
  -- 1st - Clayton Norberg - Sterling-Newman
  -- 2nd - Shane Dintelman - Belleville L.D.
  -- 3rd - Mark Lukaszewski - Villa-Lombard
  -- 4th - Tim Golden - Vittum Cats
  -- 5th - Joseph Graves - Batavia Pinners
  -- 6th - Matt Wenger - Dakota WC
  (76, 1011, NULL, 'championship_first_place', 67, 68, TRUE, '', NULL, NULL),
  (77, 1011, NULL, 'consolation_third_place',  69, 70, TRUE, '', NULL, NULL),
  (78, 1011, NULL, 'consolation_fifth_place',  71, 72, TRUE, '', NULL, NULL),
  -- bracket_id=1012 (Novice 101)
  -- 1st - Steven Rodgers - Bethalto Jr. High
  -- 2nd - Matthew Smith - Villa-Lombard
  -- 3rd - Brandon Lozdowski - Harlem Cou.
  -- 4th - John Murphy - St. Barnabas/CTK
  -- 5th - Will Mekeel - Sterling-Newman
  -- 6th - Aaron Lipe - Galesburg Jr. Streaks
  (79, 1012, NULL, 'championship_first_place', 73, 74, TRUE, '', NULL, NULL),
  (80, 1012, NULL, 'consolation_third_place',  75, 76, TRUE, '', NULL, NULL),
  (81, 1012, NULL, 'consolation_fifth_place',  77, 78, TRUE, '', NULL, NULL),
  -- bracket_id=1013 (Novice 108)
  -- 1st - Mike Mucha - Lemont Bears
  -- 2nd - Austin Jones - Bradley-Bour. WC
  -- 3rd - Drew Jones - Hononegah Kids WC
  -- 4th - Robert Wallon - Lemont Bears
  -- 5th - Nathan Troye - Sterling-Newman
  -- 6th - Michael McIntyre - Savanna R.hawk
  (82, 1013, NULL, 'championship_first_place', 79, 80, TRUE, '', NULL, NULL),
  (83, 1013, NULL, 'consolation_third_place',  81, 82, TRUE, '', NULL, NULL),
  (84, 1013, NULL, 'consolation_fifth_place',  83, 84, TRUE, '', NULL, NULL),
  -- bracket_id=1014 (Novice 115)
  -- 1st - Andrew Zidow - LaSalle-Peru
  -- 2nd - Ryan Bittle - A-J Jr. Wildcats
  -- 3rd - Chris Smith - Plainfield WC
  -- 4th - Joshua Mohr - Yorkville WC
  -- 5th - Dan Haeflinger - Harvard WC
  -- 6th - Jon Crettol - Orland Park
  (85, 1014, NULL, 'championship_first_place', 85, 86, TRUE, '', NULL, NULL),
  (86, 1014, NULL, 'consolation_third_place',  87, 88, TRUE, '', NULL, NULL),
  (87, 1014, NULL, 'consolation_fifth_place',  89, 90, TRUE, '', NULL, NULL),
  -- bracket_id=1015 (Novice 122)
  -- 1st - Liam Kelly - Tinley Park
  -- 2nd - Jared Sugden - A-O Kids WC
  -- 3rd - Kyle Williams - Fox Valley WC
  -- 4th - Phil Grant - Crystal Lake Wizards
  -- 5th - Jason Johnson - Sterling-Newman
  -- 6th - Keith Hauter - Litchfield Kids WC
  (88, 1015, NULL, 'championship_first_place', 91, 92, TRUE, '', NULL, NULL),
  (89, 1015, NULL, 'consolation_third_place',  93, 94, TRUE, '', NULL, NULL),
  (90, 1015, NULL, 'consolation_fifth_place',  95, 96, TRUE, '', NULL, NULL),
  -- bracket_id=1016 (Novice 130)
  -- 1st - De'Andre Nunn - Little Celtics
  -- 2nd - Buddy Dudczak - Villa-Lombard
  -- 3rd - Billy Pyszka - LaSalle-Peru
  -- 4th - Nicholas Miller - Mattoon Youth WC
  -- 5th - Jonathan Wyatt - Westville Youth
  -- 6th - Ryan Francis - Lemont Bears
  (91, 1016, NULL, 'championship_first_place', 97, 98, TRUE, '', NULL, NULL),
  (92, 1016, NULL, 'consolation_third_place',  99, 100, TRUE, '', NULL, NULL),
  (93, 1016, NULL, 'consolation_fifth_place',  101, 102, TRUE, '', NULL, NULL),
  -- bracket_id=1017 (Novice 147)
  -- 1st - Shane Butler - Midwest Central Y.
  -- 2nd - Jesus Ordaz - Crystal Lake Wiz.
  -- 3rd - Marcus McDowell - Mattoon Youth
  -- 4th - Jeffrey Janicki - Villa-Lombard
  -- 5th - Joe Youngberg - Murphysboro MS
  -- 6th - Gary Cox - Vandalia Jr. WC
  (94, 1017, NULL, 'championship_first_place', 103, 104, TRUE, '', NULL, NULL),
  (95, 1017, NULL, 'consolation_third_place',  105, 106, TRUE, '', NULL, NULL),
  (96, 1017, NULL, 'consolation_fifth_place',  107, 108, TRUE, '', NULL, NULL),
  -- bracket_id=1018 (Novice 166)
  -- 1st - Chris Espinoza - Wheaton Bulldogs
  -- 2nd - Brian Kerr - East Moline WC
  -- 3rd - Jim Huffman - Villa-Lombard
  -- 4th - Christian Bunyan - Urbana Kids WC
  -- 5th - Casey Hicks - Pontiac Pythons
  -- 6th - Mike Scheibel - Highland Bulldogs
  (97, 1018, NULL, 'championship_first_place', 109, 110, TRUE, '', NULL, NULL),
  (98, 1018, NULL, 'consolation_third_place',  111, 112, TRUE, '', NULL, NULL),
  (99, 1018, NULL, 'consolation_fifth_place',  113, 114, TRUE, '', NULL, NULL),
  -- bracket_id=1019 (Novice 215)
  -- 1st - Rusty Wheat - Roxana Kids WC
  -- 2nd - Ray Stuthers - Murphysboro MS
  -- 3rd - Brandon Sutton - Pinckneyville WC
  -- 4th - Ben Lawrence - Crossface WC
  -- 5th - Vinnie Salmieri - A-O Kids WC
  -- 6th - Ryan Weaver - Little Redbirds WC
  (100, 1019, NULL, 'championship_first_place', 115, 116, TRUE, '', NULL, NULL),
  (101, 1019, NULL, 'consolation_third_place',  117, 118, TRUE, '', NULL, NULL),
  (102, 1019, NULL, 'consolation_fifth_place',  119, 120, TRUE, '', NULL, NULL),
  -- bracket_id=1020 (Senior 70)
  -- 1st - David Murphy - Little Celtics
  -- 2nd - Cody Dietze - Tinley Park
  -- 3rd - Brandon Zerfowski - Mt. Zion WC
  -- 4th - Scott Eichberger - Orland Park
  -- 5th - John Wienert - Vittum Cats
  -- 6th - Jerry Fischer - Morton Youth
  (103, 1020, NULL, 'championship_first_place', 121, 122, TRUE, '', NULL, NULL),
  (104, 1020, NULL, 'consolation_third_place',  123, 124, TRUE, '', NULL, NULL),
  (105, 1020, NULL, 'consolation_fifth_place',  125, 126, TRUE, '', NULL, NULL),
  -- bracket_id=1021 (Senior 74)
  -- 1st - Jordan Kolinski - Rockford WC
  -- 2nd - Eric Bauer - Fox Valley WC
  -- 3rd - Daniel Leonard - Villa-Lombard
  -- 4th - Josiah Wooten - Urbana Kids Club
  -- 5th - Tony Martinez - Little Celtics
  -- 6th - Chris Maynor - Southern IL Eagles
  (106, 1021, NULL, 'championship_first_place', 127, 128, TRUE, '', NULL, NULL),
  (107, 1021, NULL, 'consolation_third_place',  129, 130, TRUE, '', NULL, NULL),
  (108, 1021, NULL, 'consolation_fifth_place',  131, 132, TRUE, '', NULL, NULL),
  -- bracket_id=1022 (Senior 79)
  -- 1st - Josh Taylor - Tigertown Tanglers
  -- 2nd - Brad Medchill - Villa-Lombard
  -- 3rd - Dan Manzella - Vittum Cats
  -- 4th - Justin Grey - Tinley Park
  -- 5th - Steve Scrementi - Little Celtics
  -- 6th - Shane Saylor - Bethalto Jr. High
  (109, 1022, NULL, 'championship_first_place', 133, 134, TRUE, '', NULL, NULL),
  (110, 1022, NULL, 'consolation_third_place',  135, 136, TRUE, '', NULL, NULL),
  (111, 1022, NULL, 'consolation_fifth_place',  137, 138, TRUE, '', NULL, NULL),
  -- bracket_id=1023 (Senior 84)
  -- 1st - Brian Dyer - Fox Valley WC
  -- 2nd - Justin Haskett - Tinley Park
  -- 3rd - Brad Dargan - Crystal Lake
  -- 4th - Tony Emma - Wheaton Monroe Eagles
  -- 5th - Thomas Tapia - East Moline WC
  -- 6th - Branden Mackey - Urbana Kids Club
  (112, 1023, NULL, 'championship_first_place', 139, 140, TRUE, '', NULL, NULL),
  (113, 1023, NULL, 'consolation_third_place',  141, 142, TRUE, '', NULL, NULL),
  (114, 1023, NULL, 'consolation_fifth_place',  143, 144, TRUE, '', NULL, NULL),
  -- bracket_id=1024 (Senior 89)
  -- 1st - Pat Barth - Morton Youth WC
  -- 2nd - Zac Berman - Little Celtics
  -- 3rd - Ryan Kimberlin - Bradley-Bour.
  -- 4th - Kevin McNicholas - Vittum Cats
  -- 5th - Michael Reese - LaSalle-Peru
  -- 6th - Chad Vandiver - Harlem Cougars
  (115, 1024, NULL, 'championship_first_place', 145, 146, TRUE, '', NULL, NULL),
  (116, 1024, NULL, 'consolation_third_place',  147, 148, TRUE, '', NULL, NULL),
  (117, 1024, NULL, 'consolation_fifth_place',  149, 150, TRUE, '', NULL, NULL),
  -- bracket_id=1025 (Senior 95)
  -- 1st - Chase Beebe - Fox Valley WC
  -- 2nd - Robert Loftus - Yorkville WC
  -- 3rd - Kevin Sheber - Lemont Bears
  -- 4th - Andrew Lukanich - Vittum Cats
  -- 5th - Adam Beeler - Edwardsville WC
  -- 6th - Mike Whalen - Edwardsville WC
  (118, 1025, NULL, 'championship_first_place', 151, 152, TRUE, '', NULL, NULL),
  (119, 1025, NULL, 'consolation_third_place',  153, 154, TRUE, '', NULL, NULL),
  (120, 1025, NULL, 'consolation_fifth_place',  155, 156, TRUE, '', NULL, NULL),
  -- bracket_id=1026 (Senior 101)
  -- 1st - Eric Tannenbaum - Fox Valley WC
  -- 2nd - Ryan Klinger - Oak Lawn Wildcats
  -- 3rd - Bob McClellan - Tinley Park
  -- 4th - Jacob Jones - Mt. Zion WC
  -- 5th - Ryan Giulano - Wolfpak WC
  -- 6th - Ryne Bird - Tigertown Tanglers
  (121, 1026, NULL, 'championship_first_place', 157, 158, TRUE, '', NULL, NULL),
  (122, 1026, NULL, 'consolation_third_place',  159, 160, TRUE, '', NULL, NULL),
  (123, 1026, NULL, 'consolation_fifth_place',  161, 162, TRUE, '', NULL, NULL),
  -- bracket_id=1027 (Senior 108)
  -- 1st - Collin McKillip - Tinley Park
  -- 2nd - Joe Gomez - Villa-Lombard
  -- 3rd - Matt Wellner - Fox Valley WC
  -- 4th - Matt Collum - Fox Valley WC
  -- 5th - Mitch Fonner - Mattoon Youth WC
  -- 6th - Matt Anderson - Harlem Cougars
  (124, 1027, NULL, 'championship_first_place', 163, 164, TRUE, '', NULL, NULL),
  (125, 1027, NULL, 'consolation_third_place',  165, 166, TRUE, '', NULL, NULL),
  (126, 1027, NULL, 'consolation_fifth_place',  167, 168, TRUE, '', NULL, NULL),
  -- bracket_id=1028 (Senior 115)
  -- 1st - Jakob Bottoms - Murphysboro MS
  -- 2nd - Ryan DeVriendt - Sherrard Jr. WC
  -- 3rd - Tyler Williams - Villa-Lombard
  -- 4th - Roberto Torres - Fox Valley WC
  -- 5th - Drew McMahon - Champaign Chargers
  -- 6th - Matthew Wahl - Jr. Golden Eagles
  (127, 1028, NULL, 'championship_first_place', 169, 170, TRUE, '', NULL, NULL),
  (128, 1028, NULL, 'consolation_third_place',  171, 172, TRUE, '', NULL, NULL),
  (129, 1028, NULL, 'consolation_fifth_place',  173, 174, TRUE, '', NULL, NULL),
  -- bracket_id=1029 (Senior 122)
  -- 1st - Ruben Villareal - Fox Valley WC
  -- 2nd - Michael Pila - Orland Park
  -- 3rd - Bryan Casey - Lemont Bears
  -- 4th - David Kuntz - Vittum Cats
  -- 5th - Jake Mekeel - Sterling-Newman
  -- 6th - Jeremy Doss - Bear Country WC
  (130, 1029, NULL, 'championship_first_place', 175, 176, TRUE, '', NULL, NULL),
  (131, 1029, NULL, 'consolation_third_place',  177, 178, TRUE, '', NULL, NULL),
  (132, 1029, NULL, 'consolation_fifth_place',  179, 180, TRUE, '', NULL, NULL),
  -- bracket_id=1030 (Senior 130)
  -- 1st - Bryan Harney - Vittum Cats
  -- 2nd - Josh Bednarek - Crystal Lake Wizards
  -- 3rd - Ben Murray - Bradley Bour.
  -- 4th - Josh Hartman - Jr. Rocket WC
  -- 5th - Tyler Worthington - Chenoa WC
  -- 6th - Mike Kerr - East Moline WC
  (133, 1030, NULL, 'championship_first_place', 181, 182, TRUE, '', NULL, NULL),
  (134, 1030, NULL, 'consolation_third_place',  183, 184, TRUE, '', NULL, NULL),
  (135, 1030, NULL, 'consolation_fifth_place',  185, 186, TRUE, '', NULL, NULL),
  -- bracket_id=1031 (Senior 138)
  -- 1st - Mark Mendoza - Fox Valley WC
  -- 2nd - Marty Cox - Yorkville WC
  -- 3rd - Justin Ochoa - Batavia Pinners
  -- 4th - Rick Hoke - Sherrard Jr. WC
  -- 5th - Bill Smith - Mustangs WC
  -- 6th - Kevin Tobola - Tinley Park
  (136, 1031, NULL, 'championship_first_place', 187, 188, TRUE, '', NULL, NULL),
  (137, 1031, NULL, 'consolation_third_place',  189, 190, TRUE, '', NULL, NULL),
  (138, 1031, NULL, 'consolation_fifth_place',  191, 192, TRUE, '', NULL, NULL),
  -- bracket_id=1032 (Senior 147)
  -- 1st - Danney Finney - Little Celtic WC
  -- 2nd - Kris Roberts - Marion WC
  -- 3rd - Adam Clay - Fox Valley WC
  -- 4th - Byran Golden - Vittum Cats
  -- 5th - Nick Derry - Harlem Cougars
  -- 6th - Adam Hock - Geneseo WC
  (139, 1032, NULL, 'championship_first_place', 193, 194, TRUE, '', NULL, NULL),
  (140, 1032, NULL, 'consolation_third_place',  195, 196, TRUE, '', NULL, NULL),
  (141, 1032, NULL, 'consolation_fifth_place',  197, 198, TRUE, '', NULL, NULL),
  -- bracket_id=1033 (Senior 156)
  -- 1st - Evan McCallister - Riverbend/Fulton WC
  -- 2nd - Kevin Brush - Tinley Park
  -- 3rd - Patrick Brownson - Brownson WC
  -- 4th - Derek Hunsinger - El Paso WC
  -- 5th - Sonny Lambert - Unity WC
  -- 6th - ERic Vari - Fox Valley WC
  (142, 1033, NULL, 'championship_first_place', 199, 200, TRUE, '', NULL, NULL),
  (143, 1033, NULL, 'consolation_third_place',  201, 202, TRUE, '', NULL, NULL),
  (144, 1033, NULL, 'consolation_fifth_place',  203, 204, TRUE, '', NULL, NULL),
  -- bracket_id=1034 (Senior 166)
  -- 1st - Terry Burner - Centralia WC
  -- 2nd - Chris Norberg - Sterling-Newman
  -- 3rd - Roberto Chavira - Belvidere Bandits
  -- 4th - Jason DePolo - Little Celtics
  -- 5th - Dustin Jackson - Vandalia Jr. WC
  -- 6th - Oscar Herrara - Rock Island Edison
  (145, 1034, NULL, 'championship_first_place', 205, 206, TRUE, '', NULL, NULL),
  (146, 1034, NULL, 'consolation_third_place',  207, 208, TRUE, '', NULL, NULL),
  (147, 1034, NULL, 'consolation_fifth_place',  209, 210, TRUE, '', NULL, NULL),
  -- bracket_id=1035 (Senior 177)
  -- 1st - Jason Ortiz - Fox Valley WC
  -- 2nd - Mario Caraveo - Rock Island Edison
  -- 3rd - Freddie Deramus - Vittum Cats
  -- 4th - Matthew Barron - PLT Prophets
  -- 5th - Rashad Stewart - Champaign Chargers
  -- 6th - Chris Johnston - Aces WC
  (148, 1035, NULL, 'championship_first_place', 211, 212, TRUE, '', NULL, NULL),
  (149, 1035, NULL, 'consolation_third_place',  213, 214, TRUE, '', NULL, NULL),
  (150, 1035, NULL, 'consolation_fifth_place',  215, 216, TRUE, '', NULL, NULL),
  -- bracket_id=1036 (Senior 189)
  -- 1st - Murphy Mahalik - Little Celtics
  -- 2nd - Zach Schroeder - Chilli Dawgs WC
  -- 3rd - Grant Miller - Harlem Cougars
  -- 4th - Matthew Stern - Villa-Lombard
  -- 5th - Michael Minton - Little Redbrids
  -- 6th - Caleb Bridges - Springfield Capitals
  (151, 1036, NULL, 'championship_first_place', 217, 218, TRUE, '', NULL, NULL),
  (152, 1036, NULL, 'consolation_third_place',  219, 220, TRUE, '', NULL, NULL),
  (153, 1036, NULL, 'consolation_fifth_place',  221, 222, TRUE, '', NULL, NULL),
  -- bracket_id=1037 (Senior 275)
  -- 1st - Kyle Crotty - Roxana Kids WC
  -- 2nd - Robert Taylor - Springfield Capitals
  -- 3rd - Ron Pena - Fox Valley WC
  -- 4th - Ben Bradfield - Bismark-Henning WC
  -- 5th - Matt Richards - Edison Panthers WC
  -- 6th - Charles Doerge - Edwardsville WC
  (154, 1037, NULL, 'championship_first_place', 223, 224, TRUE, '', NULL, NULL),
  (155, 1037, NULL, 'consolation_third_place',  225, 226, TRUE, '', NULL, NULL),
  (156, 1037, NULL, 'consolation_fifth_place',  227, 228, TRUE, '', NULL, NULL);
