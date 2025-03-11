# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

data "cloudflare_zone" "ikwf_history_org" {
  zone_id = "6c7b6781a0b1f44ea4a9db73216ca467"
}

################################################################################

resource "cloudflare_dns_record" "ikwf_history_mx1" {
  zone_id  = data.cloudflare_zone.ikwf_history_org.zone_id
  content  = "route1.mx.cloudflare.net"
  name     = "ikwf-history.org"
  proxied  = false
  priority = 24
  ttl      = 1
  type     = "MX"
}

resource "cloudflare_dns_record" "ikwf_history_mx2" {
  zone_id  = data.cloudflare_zone.ikwf_history_org.zone_id
  content  = "route2.mx.cloudflare.net"
  name     = "ikwf-history.org"
  proxied  = false
  priority = 16
  ttl      = 1
  type     = "MX"
}

resource "cloudflare_dns_record" "ikwf_history_mx3" {
  zone_id  = data.cloudflare_zone.ikwf_history_org.zone_id
  content  = "route3.mx.cloudflare.net"
  name     = "ikwf-history.org"
  proxied  = false
  priority = 40
  ttl      = 1
  type     = "MX"
}

################################################################################

resource "cloudflare_dns_record" "ikwf_history_cloudflare_domainkey_txt" {
  zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
  content = "\"v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiweykoi+o48IOGuP7GR3X0MOExCUDY/BCRHoWBnh3rChl7WhdyCxW3jgq1daEjPPqoi7sJvdg5hEQVsgVRQP4DcnQDVjGMbASQtrY4WmB1VebF+RPJB2ECPsEDTpeiI5ZyUAwJaVX7r6bznU67g7LvFq35yIo4sdlmtZGV+i0H4cpYH9+3JJ78k\" \"m4KXwaf9xUJCWF6nxeD+qG6Fyruw1Qlbds2r85U9dkNDVAS3gioCvELryh1TxKGiVTkg4wqHTyHfWsp7KD3WQHYJn0RyfJJu6YEmL77zonn7p2SRMvTMP3ZEXibnC9gz3nnhR6wcYL8Q7zXypKTMD58bTixDSJwIDAQAB\""
  name    = "cf2024-1._domainkey.ikwf-history.org"
  proxied = false
  ttl     = 1
  type    = "TXT"
}

resource "cloudflare_dns_record" "ikwf_history_cloudflare_spf_txt" {
  zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
  content = "\"v=spf1 include:_spf.mx.cloudflare.net ~all\""
  name    = "ikwf-history.org"
  proxied = false
  ttl     = 1
  type    = "TXT"
}

resource "cloudflare_dns_record" "ikwf_history_google_verify_txt" {
  zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
  content = "\"google-site-verification=ueMqN3FJ2wQLklPdEBarrym-CrFSva96c4jv9qN3Lh0\""
  name    = "ikwf-history.org"
  proxied = false
  ttl     = 1
  type    = "TXT"
}

# TODO: Terraform Cloudflare email forwarding in here
