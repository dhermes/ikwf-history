## Migrations

```
/opt/homebrew/Cellar/sqlite/3.47.0/bin/sqlite3 ikwf.sqlite < ./migrations/0001-initialize-schema.sql
/opt/homebrew/Cellar/sqlite/3.47.0/bin/sqlite3 ikwf.sqlite < ./migrations/0002-populate-teams.sql
```

## Common helper commands

```
$ /opt/homebrew/Cellar/sqlite/3.47.0/bin/sqlite3 ikwf.sqlite
SQLite version 3.47.0 2024-10-21 16:30:22
Enter ".help" for usage hints.
sqlite>
sqlite>
sqlite> .tables
division    match_slot
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
