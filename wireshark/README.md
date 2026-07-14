<div align="center">

# Wireshark - Network Protocol Analyzer

<img src="https://img.shields.io/badge/Tool-Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" />
<img src="https://img.shields.io/badge/Category-Network%20Analysis-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Learning%20Complete-00D26A?style=for-the-badge" />

</div>

---

## What is Wireshark?

Wireshark is the world's foremost and widely-used network protocol analyzer. It lets you see what's happening on your network at a microscopic level and is the de facto standard across the industry.

### Key Capabilities

| Feature | Description |
|:--------|:------------|
| **Live Capture** | Capture network packets in real-time |
| **Offline Analysis** | Analyze previously captured data |
| **Deep Inspection** | Examine hundreds of protocols |
| **Multi-Platform** | Windows, macOS, Linux, FreeBSD |
| **Rich VoIP Analysis** | Analyze VoIP calls |
| **Decryption** | Support for many encryption protocols |

---

## Installation

```bash
# Debian / Ubuntu
sudo apt-get update
sudo apt-get install wireshark -y

# Allow non-root capture (recommended)
sudo dpkg-reconfigure wireshark-common
# Select "Yes" when asked about non-superuser packet capture
sudo usermod -aG wireshark $USER
# Log out and back in for group changes to take effect

# Fedora / RHEL
sudo dnf install wireshark-qt

# macOS (Homebrew)
brew install --cask wireshark

# Arch Linux
sudo pacman -S wireshark
```

### Verify Installation

```bash
wireshark --version
tshark --version
```

---

## Capture Filters (BPF Syntax)

Capture filters are applied BEFORE packet capture using Berkeley Packet Filter syntax.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HOST FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Capture traffic to/from a specific host
wireshark -i eth0 -f "host 192.168.1.1"

# Capture traffic from a specific source
wireshark -i eth0 -f "src host 192.168.1.100"

# Capture traffic to a specific destination
wireshark -i eth0 -f "dst host 192.168.1.200"

# Capture traffic on a subnet
wireshark -i eth0 -f "net 192.168.1.0/24"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PORT FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Capture HTTP traffic (port 80)
wireshark -i eth0 -f "port 80"

# Capture HTTPS traffic (port 443)
wireshark -i eth0 -f "port 443"

# Capture on a range of ports
wireshark -i eth0 -f "portrange 8000-9000"

# Capture DNS traffic (port 53)
wireshark -i eth0 -f "port 53"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROTOCOL FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Capture only TCP packets
wireshark -i eth0 -f "tcp"

# Capture only UDP packets
wireshark -i eth0 -f "udp"

# Capture only ICMP (ping)
wireshark -i eth0 -f "icmp"

# Capture only ARP traffic
wireshark -i eth0 -f "arp"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMBINED FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# HTTP traffic from a specific host
wireshark -i eth0 -f "host 192.168.1.1 and port 80"

# TCP traffic excluding ARP
wireshark -i eth0 -f "tcp and not arp"

# Traffic between two hosts
wireshark -i eth0 -f "host 192.168.1.1 and host 192.168.1.2"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SIZE FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Capture packets greater than 100 bytes
wireshark -i eth0 -f "greater 100"

# Capture packets less than 50 bytes
wireshark -i eth0 -f "less 50"
```

---

## Display Filters (Wireshark Syntax)

Display filters are applied AFTER packet capture. They use a different syntax than capture filters.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROTOCOL FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show only HTTP packets
http

# Show only DNS packets
dns

# Show only TCP packets
tcp

# Show only UDP packets
udp

# Show only ICMP packets
icmp

# Show only TLS/SSL packets
tls


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HTTP FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show only HTTP requests
http.request

# Show only HTTP responses
http.response

# Show only GET requests
http.request.method == "GET"

# Show only POST requests
http.request.method == "POST"

# Show requests to a specific host
http.host == "www.example.com"

# Show requests containing a specific URI
http.request.uri contains "login"

# Show HTTP responses with specific status code
http.response.code == 200
http.response.code == 404
http.response.code == 500


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IP ADDRESS FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show packets from specific source IP
ip.src == 192.168.1.100

# Show packets to specific destination IP
ip.dst == 192.168.1.200

# Show packets from or to a specific IP
ip.addr == 192.168.1.100

# Show only IPv6 traffic
ipv6


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TCP FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show TCP traffic on specific port
tcp.port == 80

# Show TCP traffic on source port
tcp.srcport == 443

# Show TCP traffic on destination port
tcp.dstport == 8080

# Show TCP SYN packets (new connections)
tcp.flags.syn == 1

# Show TCP FIN packets (closing connections)
tcp.flags.fin == 1

# Show TCP RST packets (reset connections)
tcp.flags.reset == 1

# Follow a specific TCP stream
tcp.stream eq 0


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMBINED FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# HTTP GET from specific IP
http.request.method == "GET" and ip.src == 192.168.1.100

# HTTPS traffic to a specific host
tcp.port == 443 and ip.dst == 10.0.0.1

# HTTP POST with specific content type
http.request.method == "POST" and http.content_type contains "application/json"

# Exclude ARP and DNS (reduce noise)
!arp and !dns


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DATA / CONTENT FILTERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show packets containing specific text
frame contains "password"

# Show packets with specific data
data contains "admin"

# Show packets larger than 1000 bytes
frame.len > 1000

# Show packets with specific HTTP content type
http.content_type contains "text/html"
```

---

## TShark - Command Line Wireshark

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BASIC CAPTURE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Capture HTTP requests on interface
tshark -i eth0 -f "tcp port 80" -Y "http.request"

# Capture with specific duration
tshark -i eth0 -w capture.pcapng -a duration:60

# Capture with packet count limit
tshark -i eth0 -w capture.pcapng -c 1000


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# READ AND FILTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Read capture file and filter
tshark -r capture.pcapng -Y "http.request.method == GET"

# Show specific fields
tshark -r capture.pcapng -Y "http" -T fields -e http.host -e http.request.uri

# Show only HTTP headers
tshark -r capture.pcapng -Y "http.request" -T fields -e http.request.method -e http.request.uri -e http.host


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXPORT AND ANALYSIS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Export HTTP objects (files, images, etc.)
tshark -r capture.pcapng -q --export-objects http,exported_files/

# Follow TCP stream
tshark -r capture.pcapng -qz follow,tcp,stream,0

# Show conversation statistics
tshark -r capture.pcapng -qz conv,tcp

# Show protocol hierarchy
tshark -r capture.pcapng -qz io,phs

# Show HTTP request/response pairs
tshark -r capture.pcapng -qz http,tree
```

---

## Wireshark GUI Tips

### Useful Menu Options

```
┌─────────────────────────────────────────────────────┐
│  Analyze → Follow → TCP Stream                      │
│  (View full conversation between two hosts)          │
│                                                      │
│  File → Export Objects → HTTP                        │
│  (Extract files transferred over HTTP)               │
│                                                      │
│  Statistics → Conversations                          │
│  (See who talked to whom)                            │
│                                                      │
│  Statistics → Protocol Hierarchy                     │
│  (See what protocols are in use)                     │
│                                                      │
│  Statistics → HTTP → Requests                        │
│  (Summary of HTTP requests)                          │
│                                                      │
│  Telephony → VoIP Calls                              │
│  (Analyze VoIP communications)                       │
└─────────────────────────────────────────────────────┘
```

### Color Rules Meaning

| Color | Meaning |
|:------|:--------|
| Black/Red | Errors, TCP retransmissions |
| Blue | DNS traffic |
| Green | HTTP traffic |
| Purple | TLS/SSL traffic |
| Gray | TCP window updates |
| Light Blue | TCP SYN/FIN |

---

## Practical Exercises

### Exercise 1: Capture and Analyze HTTP Traffic

```bash
# Step 1: Start capture
tshark -i eth0 -f "tcp port 80" -w http-exercise.pcapng

# Step 2: Generate traffic (in another terminal)
curl http://example.com

# Step 3: Stop capture (Ctrl+C)

# Step 4: Analyze
tshark -r http-exercise.pcapng -Y "http"

# Step 5: Follow TCP stream
tshark -r http-exercise.pcapng -qz follow,tcp,stream,0

# Step 6: Export objects
tshark -r http-exercise.pcapng -q --export-objects http,exported/
```

### Exercise 2: Find Suspicious Traffic

```bash
# Look for data exfiltration patterns
tshark -r suspicious.pcapng -Y "frame.len > 1000 && tcp.flags.syn == 1"

# Find DNS tunneling
tshark -r suspicious.pcapng -Y "dns && frame.len > 512"

# Look for password in HTTP traffic
tshark -r suspicious.pcapng -Y "http.request.method == POST" -T fields -e http.request.uri -e http.file_data
```

---

## Files in This Directory

| File | Description |
|:-----|:------------|
| [capture-filters.md](capture-filters.md) | Complete capture filter reference |
| [display-filters.md](display-filters.md) | Complete display filter reference |
| [http-analysis.md](http-analysis.md) | HTTP traffic analysis guide |
| [sample-captures/](sample-captures/) | Directory for .pcap files |

---

<div align="center">

**[⬆ Back to Main README](../README.md)**

</div>
