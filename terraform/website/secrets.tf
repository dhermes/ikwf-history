# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

data "google_secret_manager_secret_version" "cloudflare_api_token" {
  secret = "CLOUDFLARE_API_TOKEN"
}
