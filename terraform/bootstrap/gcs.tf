# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_storage_bucket" "terraform_state" {
  name                        = "ikwf-history-terraform-states"
  location                    = "US"
  storage_class               = "STANDARD"
  enable_object_retention     = false
  requester_pays              = false
  rpo                         = "DEFAULT"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"

  versioning {
    enabled = true
  }

  soft_delete_policy {
    retention_duration_seconds = 604800
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      num_newer_versions = 5
      with_state         = "ARCHIVED"
    }
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      days_since_noncurrent_time = 7
      with_state                 = "ANY"
    }
  }
}

data "google_iam_policy" "terraform_state" {
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

resource "google_storage_bucket_iam_policy" "terraform_state" {
  bucket      = google_storage_bucket.terraform_state.name
  policy_data = data.google_iam_policy.terraform_state.policy_data
}
