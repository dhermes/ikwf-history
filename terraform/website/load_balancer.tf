# Copyright (c) 2025 - Present. IKWF History. All rights reserved.

resource "google_compute_backend_bucket" "ikwf_history_website" {
  name             = "ikwf-history-website"
  bucket_name      = google_storage_bucket.ikwf_history_website.name
  enable_cdn       = true
  compression_mode = "AUTOMATIC"
}

resource "google_compute_url_map" "ikwf_history_website_redirect" {
  name = "ikwf-history-website-redirect"

  default_url_redirect {
    https_redirect = true
    strip_query    = false
  }
}

resource "google_compute_target_http_proxy" "ikwf_history_website" {
  name    = "ikwf-history-website-http-proxy"
  url_map = google_compute_url_map.ikwf_history_website_redirect.id
}

resource "google_compute_global_forwarding_rule" "ikwf_history_website_http" {
  name                  = "ikwf-history-website-http"
  target                = google_compute_target_http_proxy.ikwf_history_website.id
  ip_address            = google_compute_global_address.ikwf_history_frontend_static.address
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL_MANAGED"
  port_range            = "80"
}

resource "google_compute_url_map" "ikwf_history_website" {
  name = "ikwf-history-website"

  default_url_redirect {
    host_redirect  = "ikwf.org"
    https_redirect = true
    path_redirect  = "/"
    strip_query    = true
  }

  host_rule {
    hosts        = ["ikwf-history.org"]
    path_matcher = "match-frontend"
  }

  path_matcher {
    name            = "match-frontend"
    default_service = google_compute_backend_bucket.ikwf_history_website.id

    # Enable HTTP Strict Transport Security (HSTS)
    header_action {
      # NOTE: 60 * 60 * 24 * 365 = 31536000 (i.e. 365 days, in seconds)
      response_headers_to_add {
        header_name  = "Strict-Transport-Security"
        header_value = "max-age=31536000; includeSubDomains"
        replace      = false
      }
    }
  }
}

resource "google_compute_target_https_proxy" "ikwf_history_website" {
  name            = "ikwf-history-website-https-proxy"
  url_map         = google_compute_url_map.ikwf_history_website.id
  certificate_map = "//certificatemanager.googleapis.com/${google_certificate_manager_certificate_map.ikwf_history_wildcard.id}"
  ssl_policy      = google_compute_ssl_policy.tls_min_12.id
}

resource "google_compute_global_forwarding_rule" "ikwf_history_website_https" {
  name                  = "ikwf-history-website-https"
  target                = google_compute_target_https_proxy.ikwf_history_website.self_link
  ip_address            = google_compute_global_address.ikwf_history_frontend_static.address
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL_MANAGED"
  port_range            = "443"
}
