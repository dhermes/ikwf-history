# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

data "google_iam_policy" "project_global" {
  binding {
    role    = "roles/compute.serviceAgent" # Compute Engine Service Agent
    members = ["serviceAccount:service-${local.project_number}@compute-system.iam.gserviceaccount.com"]
  }

  binding {
    role    = "roles/editor" # Editor
    members = ["serviceAccount:${local.project_number}@cloudservices.gserviceaccount.com"]
  }

  binding {
    role    = "roles/owner" # Owner
    members = ["user:dhermes@ikwf-history.org"]
  }
}

resource "google_project_iam_policy" "project_global" {
  project     = local.project_id
  policy_data = data.google_iam_policy.project_global.policy_data
}
