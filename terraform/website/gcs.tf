# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_storage_bucket" "ikwf_history_website" {
  name                        = "ikwf-history-website"
  location                    = "US"
  storage_class               = "STANDARD"
  enable_object_retention     = false
  requester_pays              = false
  rpo                         = "DEFAULT"
  uniform_bucket_level_access = true
  public_access_prevention    = "inherited"

  website {
    main_page_suffix = "index.html"
    not_found_page   = "index.html"
  }

  # TODO: Enable access logging
  # logging {
  #   log_bucket        = data.google_storage_bucket.access_logs.name
  #   log_object_prefix = "ikwf-history.org/"
  # }
}
