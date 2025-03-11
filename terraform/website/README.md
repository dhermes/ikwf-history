# Workspace: Google Cloud resources for `ikwf-history.org` website

## Redirects

Both `ikwf-history.org` and `www.ikwf-history.org` point to the same static
IP:

```
$ dig +noall +answer ikwf-history.org. A
ikwf-history.org.       300     IN      A       34.117.199.213
$ dig +noall +answer www.ikwf-history.org. A
www.ikwf-history.org.   300     IN      A       34.117.199.213
```

Each of these domains should redirect on HTTP, and `ikwf-history.org` should
also redirect on HTTPS:

```
$ curl --include http://ikwf-history.org/
HTTP/1.1 301 Moved Permanently
Cache-Control: private
Location: https://www.ikwf-history.org:443/
Content-Length: 0
Date: Tue, 11 Mar 2025 06:02:24 GMT
Content-Type: text/html; charset=UTF-8

$ curl --include http://www.ikwf-history.org/
HTTP/1.1 301 Moved Permanently
Cache-Control: private
Location: https://www.ikwf-history.org:443/
Content-Length: 0
Date: Tue, 11 Mar 2025 06:02:37 GMT
Content-Type: text/html; charset=UTF-8

$ curl --include https://ikwf-history.org/
HTTP/2 301
cache-control: private
location: https://www.ikwf-history.org:443/
content-length: 0
date: Tue, 11 Mar 2025 06:02:09 GMT
content-type: text/html; charset=UTF-8
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

$
```
