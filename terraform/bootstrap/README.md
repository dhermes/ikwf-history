# Meta Workspace: Bootstrap (`ikwf-history-website` project)

This is the bottom of the stack of turtles. All other Terraform workspaces
assume there is a GCP resource available:

- The `ikwf-history-terraform-states` GCS bucket for storing Terraform state
  and locks

This workspace brings these up as the bare minimum to create all other
resources.

## Import

```
terraform import google_organization_iam_policy.organization_global 425318408595
terraform import google_billing_account_iam_policy.default 01549F-BBD27B-4FA2A5

terraform import google_project.ikwf_history_website ikwf-history-website
terraform import google_project_iam_policy.project_global ikwf-history-website

terraform import google_secret_manager_secret.cloudflare_api_token projects/ikwf-history-website/secrets/CLOUDFLARE_API_TOKEN
terraform import google_secret_manager_secret_iam_policy.cloudflare_api_token projects/ikwf-history-website/secrets/CLOUDFLARE_API_TOKEN

terraform import google_storage_bucket.terraform_state ikwf-history-terraform-states
terraform import google_storage_bucket_iam_policy.terraform_state b/ikwf-history-terraform-states

terraform import cloudflare_email_routing_rule.ikwf_history_admin 6c7b6781a0b1f44ea4a9db73216ca467/acdd2ad1791943bda7137ea5ae0794ca

terraform import cloudflare_dns_record.ikwf_history_cloudflare_domainkey_txt 6c7b6781a0b1f44ea4a9db73216ca467/4f176bda3f7b5dbcb39c6d0bc554f5f6
terraform import cloudflare_dns_record.ikwf_history_cloudflare_spf_txt 6c7b6781a0b1f44ea4a9db73216ca467/2231f875427c9f756e9588f7c57dcb51
terraform import cloudflare_dns_record.ikwf_history_google_verify_txt 6c7b6781a0b1f44ea4a9db73216ca467/fe56c2ebb2a7638aa9415b1e112c5987
terraform import cloudflare_dns_record.ikwf_history_mx1 6c7b6781a0b1f44ea4a9db73216ca467/397f81a0eeff8272ace1dc5a8f05eab5
terraform import cloudflare_dns_record.ikwf_history_mx2 6c7b6781a0b1f44ea4a9db73216ca467/92866ded27f33bb4964298056edba226
terraform import cloudflare_dns_record.ikwf_history_mx3 6c7b6781a0b1f44ea4a9db73216ca467/a81072f061dae647e621b2e2cf3e83b4

terraform import 'google_project_service.enabled["analyticshub.googleapis.com"']        ikwf-history-website/analyticshub.googleapis.com
terraform import 'google_project_service.enabled["bigquery.googleapis.com"']            ikwf-history-website/bigquery.googleapis.com
terraform import 'google_project_service.enabled["bigqueryconnection.googleapis.com"']  ikwf-history-website/bigqueryconnection.googleapis.com
terraform import 'google_project_service.enabled["bigquerydatapolicy.googleapis.com"']  ikwf-history-website/bigquerydatapolicy.googleapis.com
terraform import 'google_project_service.enabled["bigquerymigration.googleapis.com"']   ikwf-history-website/bigquerymigration.googleapis.com
terraform import 'google_project_service.enabled["bigqueryreservation.googleapis.com"'] ikwf-history-website/bigqueryreservation.googleapis.com
terraform import 'google_project_service.enabled["bigquerystorage.googleapis.com"']     ikwf-history-website/bigquerystorage.googleapis.com
terraform import 'google_project_service.enabled["billingbudgets.googleapis.com"']      ikwf-history-website/billingbudgets.googleapis.com
terraform import 'google_project_service.enabled["certificatemanager.googleapis.com"']  ikwf-history-website/certificatemanager.googleapis.com
terraform import 'google_project_service.enabled["cloudapis.googleapis.com"']           ikwf-history-website/cloudapis.googleapis.com
terraform import 'google_project_service.enabled["cloudtrace.googleapis.com"']          ikwf-history-website/cloudtrace.googleapis.com
terraform import 'google_project_service.enabled["compute.googleapis.com"']             ikwf-history-website/compute.googleapis.com
terraform import 'google_project_service.enabled["dataform.googleapis.com"']            ikwf-history-website/dataform.googleapis.com
terraform import 'google_project_service.enabled["dataplex.googleapis.com"']            ikwf-history-website/dataplex.googleapis.com
terraform import 'google_project_service.enabled["datastore.googleapis.com"']           ikwf-history-website/datastore.googleapis.com
terraform import 'google_project_service.enabled["logging.googleapis.com"']             ikwf-history-website/logging.googleapis.com
terraform import 'google_project_service.enabled["monitoring.googleapis.com"']          ikwf-history-website/monitoring.googleapis.com
terraform import 'google_project_service.enabled["orgpolicy.googleapis.com"']           ikwf-history-website/orgpolicy.googleapis.com
terraform import 'google_project_service.enabled["oslogin.googleapis.com"']             ikwf-history-website/oslogin.googleapis.com
terraform import 'google_project_service.enabled["secretmanager.googleapis.com"']       ikwf-history-website/secretmanager.googleapis.com
terraform import 'google_project_service.enabled["servicemanagement.googleapis.com"']   ikwf-history-website/servicemanagement.googleapis.com
terraform import 'google_project_service.enabled["serviceusage.googleapis.com"']        ikwf-history-website/serviceusage.googleapis.com
terraform import 'google_project_service.enabled["sql-component.googleapis.com"']       ikwf-history-website/sql-component.googleapis.com
terraform import 'google_project_service.enabled["storage-api.googleapis.com"']         ikwf-history-website/storage-api.googleapis.com
terraform import 'google_project_service.enabled["storage-component.googleapis.com"']   ikwf-history-website/storage-component.googleapis.com
terraform import 'google_project_service.enabled["storage.googleapis.com"']             ikwf-history-website/storage.googleapis.com
```
