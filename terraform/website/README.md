# Workspace: Google Cloud resources for `ikwf-history.org` website

DNS records are managed in Cloudflare, so we use the
`google_certificate_manager_dns_authorization.ikwf_history` and
`google_compute_global_address.ikwf_history_frontend_static` resources to
determine which records to create there:

```
dns_authorizations = tolist([
  {
    "data" = "083b13ce-cfdb-45d8-92b7-0b3a886c5d04.8.authorize.certificatemanager.goog."
    "name" = "_acme-challenge.ikwf-history.org."
    "type" = "CNAME"
  },
])
ikwf_history_a_record = "34.117.199.213"
```
