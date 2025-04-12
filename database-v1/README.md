# Database (SQLite)

The final normalized place for data to end up is in the
`database-v1/ikwf.sqlite` database. This has a schema (in
`database-v1/migrations/`) and all data will be inserted via SQL scripts. (We
may generate some of these scripts via e.g. Python scripts that parse data.)

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
cd database-v1/
./_refresh.sh
```

## Common helper commands

```
$ cd database-v1/
$ sqlite3 ./ikwf.sqlite
SQLite version 3.47.0 2024-10-21 16:30:22
Enter ".help" for usage hints.
sqlite>
sqlite>
sqlite> .tables
award                  match                  team_score
award_winner           match_slot             tournament
bracket                result_type            tournament_competitor
competitor             team                   tournament_team
division               team_point_deduction   wrestleback_type
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
1|bantam
2|intermediate
3|novice
4|senior
5|bantam_girls
6|intermediate_girls
7|novice_girls
8|senior_girls
```
