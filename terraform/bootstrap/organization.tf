# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

# $ gcloud organizations describe ikwf-history.org --format 'value(name)'
# organizations/425318408595

data "google_organization" "ikwf_history_org" {
  domain = "ikwf-history.org"
}

# TODO: Make API / session tokens expire (https://admin.google.com)
