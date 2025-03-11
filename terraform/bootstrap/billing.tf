# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

# $ gcloud billing accounts list
# ACCOUNT_ID            NAME                OPEN  MASTER_ACCOUNT_ID
# 01549F-BBD27B-4FA2A5  My Billing Account  True

data "google_billing_account" "default" {
  # https://console.cloud.google.com/billing/01549F-BBD27B-4FA2A5/manage?organizationId=425318408595
  display_name = "My Billing Account"
}

data "google_iam_policy" "default_billing_account" {
  binding {
    role    = "roles/billing.admin" # Billing Account Administrator
    members = ["user:dhermes@ikwf-history.org"]
  }
}

resource "google_billing_account_iam_policy" "default" {
  billing_account_id = data.google_billing_account.default.id
  policy_data        = data.google_iam_policy.default_billing_account.policy_data
}

# To check if budgets are enabled (to use `google_billing_budget`):
# `gcloud billing budgets list --billing-account 01549F-BBD27B-4FA2A5 --billing-project ikwf-history-website`
