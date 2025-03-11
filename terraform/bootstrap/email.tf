# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

# TODO: Token permissions do not allow importing `cloudflare_email_routing_dns`

# $ terraform import cloudflare_email_routing_dns.ikwf_history 6c7b6781a0b1f44ea4a9db73216ca467
# resource "cloudflare_email_routing_dns" "ikwf_history" {
#   zone_id = data.cloudflare_zone.ikwf_history_org.zone_id
#   name    = "ikwf-history.org"
# }

resource "cloudflare_email_routing_rule" "ikwf_history_admin" {
  zone_id  = data.cloudflare_zone.ikwf_history_org.zone_id
  enabled  = true
  name     = "Rule created at 2025-03-11T03:35:14.224Z"
  priority = 0

  matchers = [{
    field = "to"
    type  = "literal"
    value = "admin@ikwf-history.org"
  }]

  actions = [{
    type  = "forward"
    value = ["daniel.j.hermes@gmail.com"]
  }]
}
