#!/bin/bash

set -e -x

rm -f ./ikwf.sqlite
sqlite3 ./ikwf.sqlite < ./migrations/0001-initialize-schema.sql
sqlite3 ./ikwf.sqlite < ./migrations/0002-populate-enums.sql
sqlite3 ./ikwf.sqlite < ./migrations/0003-tournaments.sql
sqlite3 ./ikwf.sqlite < ./migrations/0004-brackets.sql
sqlite3 ./ikwf.sqlite < ./migrations/0005-teams.sql
sqlite3 ./ikwf.sqlite < ./migrations/0006-tournament-teams.sql
sqlite3 ./ikwf.sqlite < ./migrations/0007-team-point-deductions.sql
sqlite3 ./ikwf.sqlite < ./migrations/0008-competitors.sql
