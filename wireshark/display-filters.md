<div align="center">

# Wireshark Display Filters

<img src="https://img.shields.io/badge/Type-Display%20Filters-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Applied-After%20Capture-orange?style=for-the-badge" />

</div>

---

## HTTP Filters

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HTTP REQUESTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show all HTTP packets
http

# Show only HTTP requests
http.request

# Show only HTTP responses
http.response

# Show GET requests
http.request.method == "GET"

# Show POST requests
http.request.method == "POST"

# Show PUT requests
http.request.method == "PUT"

# Show DELETE requests
http.request.method == "DELETE"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HTTP HOST & URI
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show requests to specific host
http.host == "www.example.com"

# Show requests to host containing text
http.host contains "example"

# Show requests to specific URI
http.request.uri == "/login"

# Show requests containing URI path
http.request.uri contains "admin"

# Show requests with specific query parameter
http.request.uri contains "id="


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HTTP RESPONSES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show 200 OK responses
http.response.code == 200

# Show 301 redirects
http.response.code == 301

# Show 404 Not Found
http.response.code == 404

# Show 500 Server Errors
http.response.code == 500

# Show 401 Unauthorized
http.response.code == 401

# Show 403 Forbidden
http.response.code == 403

# Show any 4xx error
http.response.code >= 400 && http.response.code < 500

# Show any 5xx error
http.response.code >= 500 && http.response.code < 600


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HTTP CONTENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show HTML content
http.content_type contains "text/html"

# Show JSON content
http.content_type contains "application/json"

# Show image content
http.content_type contains "image"

# Show requests with cookies
http.cookie

# Show requests setting cookies
http.set_cookie

# Show requests with authorization header
http.authorization
```

---

## TCP Filters

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TCP BASICS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show all TCP packets
tcp

# Show TCP on specific port
tcp.port == 80

# Show TCP source port
tcp.srcport == 12345

# Show TCP destination port
tcp.dstport == 80


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TCP FLAGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show SYN packets (new connections)
tcp.flags.syn == 1

# Show SYN-ACK packets
tcp.flags.syn == 1 && tcp.flags.ack == 1

# Show FIN packets (connection close)
tcp.flags.fin == 1

# Show RST packets (connection reset)
tcp.flags.reset == 1

# Show PSH packets (push data)
tcp.flags.push == 1

# Show ACK packets
tcp.flags.ack == 1


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TCP STREAMS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Follow specific TCP stream
tcp.stream eq 0

# TCP retransmissions
tcp.analysis.retransmission

# TCP duplicate ACKs
tcp.analysis.duplicate_ack

# TCP zero window
tcp.analysis.zero_window

# TCP keep-alive
tcp.analysis.keep_alive
```

---

## IP Filters

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IP ADDRESS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show all IP traffic
ip

# Show from source IP
ip.src == 192.168.1.100

# Show to destination IP
ip.dst == 192.168.1.200

# Show from or to IP
ip.addr == 192.168.1.100

# Show from subnet
ip.src == 192.168.1.0/24

# Show IPv6 traffic
ipv6

# Show specific IPv6 address
ipv6.addr == 2001:db8::1


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IP PROTOCOLS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show TCP protocol
ip.proto == 6

# Show UDP protocol
ip.proto == 17

# Show ICMP protocol
ip.proto == 1

# Show OSPF routing protocol
ip.proto == 89
```

---

## DNS Filters

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DNS QUERIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show all DNS traffic
dns

# Show DNS queries
dns.flags.response == 0

# Show DNS responses
dns.flags.response == 1

# Show queries for specific domain
dns.qry.name == "example.com"

# Show queries containing text
dns.qry.name contains "google"

# Show A record queries
dns.qry.type == 1

# Show AAAA record queries (IPv6)
dns.qry.type == 28

# Show MX record queries
dns.qry.type == 15

# Show DNS responses with specific IP
dns.a == 93.184.216.34
```

---

## TLS/SSL Filters

```bash
# Show all TLS traffic
tls

# Show TLS handshake
tls.handshake

# Show Client Hello
tls.handshake.type == 1

# Show Server Hello
tls.handshake.type == 2

# Show certificates
tls.handshake.type == 11

# Show TLS to specific server
tls.handshake.extensions_server_name == "example.com"
```

---

## Compound Filters

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# AND / OR / NOT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# HTTP GET from specific IP
http.request.method == "GET" && ip.src == 192.168.1.100

# HTTP or DNS
http || dns

# Exclude ARP
!arp

# HTTPS traffic from specific host
tcp.port == 443 && ip.addr == 10.0.0.5

# HTTP POST with JSON content
http.request.method == "POST" && http.content_type contains "application/json"

# All traffic except ARP and DNS
!arp && !dns

# Large HTTP responses
http.response && frame.len > 10000
```

---

<div align="center">

**[⬆ Back to Wireshark README](README.md)** | **[⬆ Back to Main README](../README.md)**

</div>
