# Database (SQLite)

The final normalized place for data to end up is in the `database/ikwf.sqlite`
database. This has a schema (in `database/migrations/`) and all data will
be inserted via SQL scripts. (We may generate some of these scripts via
e.g. Python scripts that parse data.)

## Tooling

I use the latest `sqlite` binary on macOS installed from Homebrew. I ensure
that it is ahead of `/usr/bin/sqlite3` on my `${PATH}` by using `direnv` in
this repository:

```
$ cat .envrc
export PATH="/opt/homebrew/Cellar/sqlite/3.47.0/bin:${PATH}"
```

## Migrations

```
cd database/
sqlite3 ./ikwf.sqlite < ./migrations/0001-initialize-schema.sql
sqlite3 ./ikwf.sqlite < ./migrations/0002-populate-teams.sql
sqlite3 ./ikwf.sqlite < ./migrations/0003-populate-tournaments.sql
sqlite3 ./ikwf.sqlite < ./migrations/0004-example-bracket.sql
sqlite3 ./ikwf.sqlite < ./migrations/0005-all-weights.sql
sqlite3 ./ikwf.sqlite < ./migrations/0006-partial-brackets-1999-placements.sql
sqlite3 ./ikwf.sqlite < ./migrations/0007-example-brackets-from-html.sql
```

## Common helper commands

```
$ cd database/
$ sqlite3 ./ikwf.sqlite
SQLite version 3.47.0 2024-10-21 16:30:22
Enter ".help" for usage hints.
sqlite>
sqlite>
sqlite> .tables
bracket          division         match_slot       team_competitor
competitor       match            team             tournament
sqlite>
sqlite>
sqlite> .schema division
CREATE TABLE division (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL UNIQUE
);
sqlite>
sqlite>
sqlite> SELECT * FROM division;
1|bantam_boys
2|intermediate_boys
3|novice_boys
4|senior_boys
5|bantam_girls
6|intermediate_girls
7|novice_girls
8|senior_girls
```
