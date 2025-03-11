# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_compute_global_address" "ikwf_history_frontend_static" {
  name         = "ikwf-history-frontend-static"
  ip_version   = "IPV4"
  address_type = "EXTERNAL"
}
