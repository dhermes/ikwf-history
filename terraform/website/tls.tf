# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_compute_ssl_policy" "tls_min_12" {
  name            = "tls-min-12"
  profile         = "MODERN"
  min_tls_version = "TLS_1_2"
}
