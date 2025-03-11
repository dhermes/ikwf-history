# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

provider "google" {
  project = "ikwf-history-website"
  region  = "us-central1"

  add_terraform_attribution_label = true
  default_labels = {
    creator = "terraform"
  }
}
