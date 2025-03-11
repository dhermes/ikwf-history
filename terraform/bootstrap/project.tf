# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

locals {
  project_id     = google_project.ikwf_history_website.project_id
  project_number = google_project.ikwf_history_website.number
}

resource "google_project" "ikwf_history_website" {
  name            = "ikwf-history-website"
  project_id      = "ikwf-history-website"
  org_id          = data.google_organization.ikwf_history_org.org_id
  billing_account = data.google_billing_account.default.id
}
