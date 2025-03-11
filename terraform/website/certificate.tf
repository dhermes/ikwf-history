# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_certificate_manager_certificate" "ikwf_history_wildcard" {
  name     = "ikwf-history-wildcard"
  location = "global"
  managed {
    domains = [
      "ikwf-history.org",
      "*.ikwf-history.org",
    ]
    dns_authorizations = [
      google_certificate_manager_dns_authorization.ikwf_history.id,
    ]
  }
}

resource "google_certificate_manager_certificate_map" "ikwf_history_wildcard" {
  name = "ikwf-history-wildcard"
}

resource "google_certificate_manager_certificate_map_entry" "ikwf_history_wildcard" {
  name         = "ikwf-history-wildcard"
  map          = google_certificate_manager_certificate_map.ikwf_history_wildcard.name
  certificates = [google_certificate_manager_certificate.ikwf_history_wildcard.id]
  matcher      = "PRIMARY"
}
