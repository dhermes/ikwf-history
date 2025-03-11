# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

# NOTE: Inspect this via `gcloud organizations get-iam-policy ikwf-history.org`

# TODO: Terraform the `iam.allowedPolicyMemberDomains` org policy

data "google_iam_policy" "organization_global" {
  binding {
    role    = "roles/billing.creator" # Billing Account Creator
    members = ["domain:ikwf-history.org"]
  }

  binding {
    role    = "roles/orgpolicy.policyAdmin" # Organization Policy Administrator
    members = ["user:dhermes@ikwf-history.org"]
  }

  binding {
    role    = "roles/resourcemanager.organizationAdmin" # Organization Administrator
    members = ["user:dhermes@ikwf-history.org"]
  }

  binding {
    role    = "roles/resourcemanager.projectCreator" # Project Creator
    members = ["domain:ikwf-history.org"]
  }
}

resource "google_organization_iam_policy" "organization_global" {
  org_id      = data.google_organization.ikwf_history_org.org_id
  policy_data = data.google_iam_policy.organization_global.policy_data
}
