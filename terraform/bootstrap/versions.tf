# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

terraform {
  required_version = "= 1.9.8"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.24.0"
    }
  }

  backend "gcs" {
    bucket = "ikwf-history-terraform-states"
    prefix = "terraform/bootstrap"
  }
}
