# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

# $ gcloud billing accounts list
# ACCOUNT_ID            NAME                OPEN  MASTER_ACCOUNT_ID
# 01549F-BBD27B-4FA2A5  My Billing Account  True

data "google_billing_account" "default" {
  # https://console.cloud.google.com/billing/01549F-BBD27B-4FA2A5/manage?organizationId=425318408595
  display_name = "My Billing Account"
}
