# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_certificate_manager_dns_authorization" "ikwf_history" {
  name     = "ikwf-history-dns-authz"
  domain   = "ikwf-history.org"
  type     = "FIXED_RECORD"
  location = "global"
}

################################################################################

data "cloudflare_zone" "ikwf_history_org" {
  zone_id = "6c7b6781a0b1f44ea4a9db73216ca467"
}

resource "cloudflare_dns_record" "acme_challenge_cname" {
  for_each = { for index, resource_record in google_certificate_manager_dns_authorization.ikwf_history.dns_resource_record : resource_record.name => resource_record }

  zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
  content = trimsuffix(each.value.data, ".")
  name    = trimsuffix(each.value.name, ".")
  proxied = false
  ttl     = 1
  type    = each.value.type
}

################################################################################

resource "cloudflare_dns_record" "ikwf_history_a" {
  zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
  content = google_compute_global_address.ikwf_history_frontend_static.address
  name    = "ikwf-history.org"
  proxied = false
  ttl     = 1
  type    = "A"
}

resource "cloudflare_dns_record" "www_ikwf_history_a" {
  zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
  content = google_compute_global_address.ikwf_history_frontend_static.address
  name    = "www.ikwf-history.org"
  proxied = false
  ttl     = 1
  type    = "A"
}

# TODO: Enable Cloudflare proxy for assets
