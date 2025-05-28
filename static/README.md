# Static (Hugo) website for `ikwf-history.org`

## Publishing (to Google Cloud Storage)

To sync with the `gs://ikwf-history-website/` bucket, do the following:

```
hugo  # Re-build
cd ./public/

gcloud storage rsync \
  --cache-control 'public, max-age=21600' \
  --recursive \
  --delete-unmatched-destination-objects \
  ./ \
  gs://ikwf-history-website/
```

## Bracket JS / CSS / HTML

The bracket template is intended to be fully static, but benefits greatly
by borrowing from:

- [`brackets-manager.js`][1]
- [`brackets-viewer.js`][2]

The goal of that project is to "hydrate" and allow editing of a bracket in
JavaScript. The goal of this project is to pre-compute all brackets when
generating the pages and then just render static content. In addition, there
are a few other assumptions that the `brackets-*` make that we need to relax:

- a winner will be determined by score (in wrestling we also have pins and
  there are rare UTB, forfeits, disqualifications, etc.)
- bracket entries have seeds
- bracket slots are teams (instead we have an athlete name **AND** a
  team name)
- there are no bout numbers

[1]: https://github.com/Drarig29/brackets-manager.js
[2]: https://github.com/Drarig29/brackets-viewer.js
