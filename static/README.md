# Static (Hugo) website for `ikwf-history.org`

To sync with the `gs://ikwf-history-website/` bucket, do the following:

```
hugo  # Re-build
cd ./public/

gcloud storage rsync \
  --cache-control 'public, max-age=300' \
  --recursive \
  --delete-unmatched-destination-objects \
  ./ \
  gs://ikwf-history-website/
```
