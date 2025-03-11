# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

output "dns_authorizations" {
  value = google_certificate_manager_dns_authorization.ikwf_history.dns_resource_record
}

output "dns_authorization_id" {
  value = google_certificate_manager_dns_authorization.ikwf_history.id
}

output "ikwf_history_a_record" {
  value = google_compute_global_address.ikwf_history_frontend_static.address
}
