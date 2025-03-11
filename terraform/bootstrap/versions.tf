# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

terraform {
  required_version = "= 1.11.1"

  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "5.1.0"
    }

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
