# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_storage_bucket" "ikwf_history_website" {
  name                        = "ikwf-history-website"
  location                    = "US"
  storage_class               = "STANDARD"
  enable_object_retention     = false
  requester_pays              = false
  rpo                         = "DEFAULT"
  uniform_bucket_level_access = true
  public_access_prevention    = "inherited"

  website {
    main_page_suffix = "index.html"
    not_found_page   = "index.html"
  }

  # TODO: Enable access logging
  # logging {
  #   log_bucket        = data.google_storage_bucket.access_logs.name
  #   log_object_prefix = "ikwf-history.org/"
  # }
}

data "google_iam_policy" "ikwf_history_website_bucket" {
  binding {
    role    = "roles/storage.objectViewer" # Storage Object Viewer
    members = ["allUsers"]
  }

  binding {
    role = "roles/storage.legacyBucketOwner" # Storage Legacy Bucket Owner
    members = [
      "projectEditor:${local.project_id}",
      "projectOwner:${local.project_id}",
    ]
  }

  binding {
    role = "roles/storage.legacyBucketReader" # Storage Legacy Bucket Reader
    members = [
      "projectViewer:${local.project_id}",
    ]
  }

  binding {
    role = "roles/storage.legacyObjectOwner" # Storage Legacy Object Owner
    members = [
      "projectEditor:${local.project_id}",
      "projectOwner:${local.project_id}",
    ]
  }

  binding {
    role = "roles/storage.legacyObjectReader" # Storage Legacy Object Reader
    members = [
      "projectViewer:${local.project_id}",
    ]
  }
}

resource "google_storage_bucket_iam_policy" "ikwf_history_website" {
  bucket      = google_storage_bucket.ikwf_history_website.name
  policy_data = data.google_iam_policy.ikwf_history_website_bucket.policy_data
}
