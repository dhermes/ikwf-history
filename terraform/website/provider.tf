# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

provider "cloudflare" {
  api_token = data.google_secret_manager_secret_version.cloudflare_api_token.secret_data
}

provider "google" {
  project = "ikwf-history-website"
  region  = "us-central1"

  add_terraform_attribution_label = true
  default_labels = {
    creator = "terraform"
  }
}
