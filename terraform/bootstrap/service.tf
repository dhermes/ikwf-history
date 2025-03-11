# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

locals {
  # NOTE: Inspect this via `gcloud services list --enabled --project ikwf-history-website`
  enabled_services = [
    "analyticshub.googleapis.com",        # Analytics Hub API
    "bigquery.googleapis.com",            # BigQuery API
    "bigqueryconnection.googleapis.com",  # BigQuery Connection API
    "bigquerydatapolicy.googleapis.com",  # BigQuery Data Policy API
    "bigquerymigration.googleapis.com",   # BigQuery Migration API
    "bigqueryreservation.googleapis.com", # BigQuery Reservation API
    "bigquerystorage.googleapis.com",     # BigQuery Storage API
    "certificatemanager.googleapis.com",  # Certificate Manager API
    "cloudapis.googleapis.com",           # Google Cloud APIs
    "cloudtrace.googleapis.com",          # Cloud Trace API
    "compute.googleapis.com",             # Compute Engine API
    "dataform.googleapis.com",            # Dataform API
    "dataplex.googleapis.com",            # Cloud Dataplex API
    "datastore.googleapis.com",           # Cloud Datastore API
    "logging.googleapis.com",             # Cloud Logging API
    "monitoring.googleapis.com",          # Cloud Monitoring API
    "orgpolicy.googleapis.com",           # Organization Policy API
    "oslogin.googleapis.com",             # Cloud OS Login API
    "secretmanager.googleapis.com",       # Secret Manager API
    "servicemanagement.googleapis.com",   # Service Management API
    "serviceusage.googleapis.com",        # Service Usage API
    "sql-component.googleapis.com",       # Cloud SQL
    "storage-api.googleapis.com",         # Google Cloud Storage JSON API
    "storage-component.googleapis.com",   # Cloud Storage
    "storage.googleapis.com",             # Cloud Storage API
  ]
}

resource "google_project_service" "enabled" {
  for_each = toset(local.enabled_services)

  service            = each.key
  disable_on_destroy = true
}
