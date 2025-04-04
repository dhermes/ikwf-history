#!/bin/bash

set -e -x

rm -f ./ikwf.sqlite
sqlite3 ./ikwf.sqlite < ./migrations/0001-initialize-schema.sql
sqlite3 ./ikwf.sqlite < ./migrations/0002-populate-teams.sql
sqlite3 ./ikwf.sqlite < ./migrations/0003-populate-tournaments.sql
sqlite3 ./ikwf.sqlite < ./migrations/0004-example-bracket.sql
sqlite3 ./ikwf.sqlite < ./migrations/0005-all-weights.sql
sqlite3 ./ikwf.sqlite < ./migrations/0006-partial-brackets-1999-placements.sql
sqlite3 ./ikwf.sqlite < ./migrations/0007-team-scores.sql
sqlite3 ./ikwf.sqlite < ./migrations/0008-competitors.sql
sqlite3 ./ikwf.sqlite < ./migrations/0009-matches-2000-to-2006.sql
sqlite3 ./ikwf.sqlite < ./migrations/0010-deductions-2000-to-2006.sql
