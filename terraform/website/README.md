# Workspace: Google Cloud resources for `ikwf-history.org` website

DNS records are managed in Cloudflare, so we use the
`google_certificate_manager_dns_authorization.ikwf_history` resource to
determine which records to create there:

```
dns_authorizations = tolist([
  {
    "data" = "0797b220-f5e9-4cca-b3a7-d67ab17dd167.4.authorize.certificatemanager.goog."
    "name" = "_acme-challenge.ikwf-history.org."
    "type" = "CNAME"
  },
])
```
