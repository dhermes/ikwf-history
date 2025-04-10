# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_secret_manager_secret" "cloudflare_api_token" {
  secret_id = "CLOUDFLARE_API_TOKEN"

  replication {
    auto {}
  }
}

data "google_iam_policy" "cloudflare_api_token_secret" {
}

resource "google_secret_manager_secret_iam_policy" "cloudflare_api_token" {
  secret_id   = google_secret_manager_secret.cloudflare_api_token.secret_id
  policy_data = data.google_iam_policy.cloudflare_api_token_secret.policy_data
}

# IKWF History (2025-03-11) API token (https://dash.cloudflare.com/profile/api-tokens)
# * ZONE: ikwf-history.org
#   * DNS:Edit
#   * Email Routing Rules:Edit
# * Client IP Address Filtering
#   * Is in - 67.184.37.102, 2601:249:100:a570:5cad:6dc6:34e8:34b1
# * TTL
#   * not_before: 2025-03-10T00:00:00Z
#   * expires_on: 2026-03-31T23:59:59Z
data "google_secret_manager_secret_version" "cloudflare_api_token" {
  secret = google_secret_manager_secret.cloudflare_api_token.secret_id
}
