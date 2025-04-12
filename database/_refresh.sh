#!/bin/bash

set -e -x

rm -f ./ikwf.sqlite
sqlite3 ./ikwf.sqlite < ./migrations/0001-initialize-schema.sql
sqlite3 ./ikwf.sqlite < ./migrations/0002-populate-teams.sql
sqlite3 ./ikwf.sqlite < ./migrations/0003-populate-tournaments.sql
sqlite3 ./ikwf.sqlite < ./migrations/0004-example-bracket.sql
sqlite3 ./ikwf.sqlite < ./migrations/0005-all-weights.sql
sqlite3 ./ikwf.sqlite < ./migrations/0006-partial-brackets-1999-placements.sql
sqlite3 ./ikwf.sqlite < ./migrations/0007-team-scores-2001-to-2006.sql
sqlite3 ./ikwf.sqlite < ./migrations/0008-competitors-2000-to-2006.sql
sqlite3 ./ikwf.sqlite < ./migrations/0009-matches-2000-to-2006.sql
sqlite3 ./ikwf.sqlite < ./migrations/0010-deductions-2000-to-2006.sql
sqlite3 ./ikwf.sqlite < ./migrations/0011-populate-teams-2007-to-2025.sql
sqlite3 ./ikwf.sqlite < ./migrations/0012-deductions-2007-to-2025.sql
sqlite3 ./ikwf.sqlite < ./migrations/0013-award-winners.sql
sqlite3 ./ikwf.sqlite < ./migrations/0014-team-scores-2007-to-2025.sql
sqlite3 ./ikwf.sqlite < ./migrations/0015-competitors-2007-to-2025.sql
sqlite3 ./ikwf.sqlite < ./migrations/0016-matches-2007-to-2025.sql
sqlite3 ./ikwf.sqlite < ./migrations/0017-remove-example-duplicates.sql
sqlite3 ./ikwf.sqlite < ./migrations/0018-compute-match-scores.sql
sqlite3 ./ikwf.sqlite < ./migrations/0019-remove-placeholder-bout-number.sql
sqlite3 ./ikwf.sqlite < ./migrations/0020-per-year-competitor-names.sql
sqlite3 ./ikwf.sqlite < ./migrations/0021-per-year-team-names.sql
sqlite3 ./ikwf.sqlite < ./migrations/0022-relabel-tournaments.sql
sqlite3 ./ikwf.sqlite < ./migrations/9999-name-normalize.sql
