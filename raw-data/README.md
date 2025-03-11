# Raw bracket data

## Storing

```sql
CREATE TABLE bracket_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL
  -- TODO: UNIQUE(key)
)

INSERT INTO
  bracket_type (id, key)
VALUES
  (1, 'championship'),
  (2, 'consolation'),
  (3, 'fifth_place'),
  (4, 'seventh_place');

CREATE TABLE division (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL
  -- TODO: UNIQUE(key)
)

INSERT INTO
  division (id, key)
VALUES
  (1, 'bantam_boys'),
  (2, 'intermediate_boys'),
  (3, 'novice_boys'),
  (4, 'senior_boys'),
  (5, 'bantam_girls'),
  (6, 'intermediate_girls'),
  (7, 'novice_girls'),
  (8, 'senior_girls');

--------------------------------------------------------------------------------

CREATE TABLE team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE team_competitor (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  team_id INTEGER NOT NULL REFERENCES team(id),
  competitor_id INTEGER NOT NULL REFERENCES competitor(id)
);

CREATE TABLE bracket (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  weight INTEGER NOT NULL,
  division TEXT NOT NULL REFERENCES division(key),
  year INTEGER NOT NULL
);

CREATE TABLE match (
  match_id SERIAL PRIMARY KEY,
  bracket_id INTEGER REFERENCES bracket(id),
  round_number INTEGER NOT NULL,
  match_number INTEGER NOT NULL, -- TODO: hardcoded schema
  bracket_type TEXT NOT NULL REFERENCES bracket_type(key),
  top_competitor_id INTEGER REFERENCES team_competitor(id),
  bottom_competitor_id INTEGER REFERENCES team_competitor(id),
  top_win BOOLEAN NOT NULL
  -- TODO: CHECK constraint that at most one of competitors is NULL
  -- TODO: CHECK constraint that `top_win` cannot be set to favor NULL
);
```

I think it makes sense to just hardcode a 24-man bracket based on the
following match counts (62 total matches, 16 of which are byes):

- Championship: 16 first round (R32); 8 byes
- Championship: 8 second round (R16)
- Championship: 4 quarterfinal
- Championship: 2 semifinal
- Championship: 1 final
- Consolation: 8 first round; 8 byes
- Consolation: 8 second round
- Consolation: 4 third round
- Consolation: 4 fourth round
- Consolation: 2 fifth round
- Consolation: 2 semifinals
- Consolation: 1 3rd place
- Consolation: 1 5th place
- Consolation: 1 7th place
