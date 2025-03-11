# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

data "google_project" "current" {}

locals {
  project_id = data.google_project.current.project_id
}
