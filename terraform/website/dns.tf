# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_certificate_manager_dns_authorization" "ikwf_history" {
  name     = "ikwf-history-dns-authz"
  domain   = "ikwf-history.org"
  type     = "FIXED_RECORD"
  location = "global"
}

# TODO: Terraform Cloudflare DNS records and email forwarding in here
