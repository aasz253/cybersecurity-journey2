<div align="center">

# Wireshark Capture Filters

<img src="https://img.shields.io/badge/Type-Capture%20Filters-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Applied-Before%20Capture-orange?style=for-the-badge" />

</div>

---

## Syntax Reference

```
capture_filter_syntax:
  filter_expression := expression [AND|OR expression] ...
  expression       := qualifier [qualifier] ...
  qualifier        := protocol_direction [value]
  protocol         := tcp | udp | icmp | arp | ip | ipv6 | ...
  direction        := src | dst | src or dst | src and dst
  value            := host | net | port | portrange | ...
```

---

## Host Filters

```bash
# Traffic to/from a specific host
host 192.168.1.1

# Traffic from a specific source
src host 192.168.1.100

# Traffic to a specific destination
dst host 192.168.1.200

# Traffic between two hosts
host 192.168.1.1 and host 192.168.1.2

# Traffic on a subnet
net 192.168.1.0/24

# Traffic to/from IPv6 host
host 2001:db8::1
```

---

## Port Filters

```bash
# Traffic on a specific port
port 80

# Traffic on multiple ports
port 80 or port 443

# Traffic on a port range
portrange 8000-9000

# Source port only
src port 12345

# Destination port only
dst port 80

# Traffic not on port 80
not port 80
```

---

## Protocol Filters

```bash
# TCP only
tcp

# UDP only
udp

# ICMP only
icmp

# ARP only
arp

# DNS (UDP port 53)
udp port 53

# HTTP (TCP port 80)
tcp port 80

# HTTPS (TCP port 443)
tcp port 443

# SSH (TCP port 22)
tcp port 22

# FTP (TCP port 21)
tcp port 21

# SMTP (TCP port 25)
tcp port 25
```

---

## Size Filters

```bash
# Packets greater than 100 bytes
greater 100

# Packets less than 50 bytes
less 50

# Packets exactly 64 bytes
len == 64

# Packets between 100 and 500 bytes
greater 100 and less 500
```

---

## Combined Filters (Examples)

```bash
# HTTP traffic from a specific host
host 192.168.1.100 and tcp port 80

# All traffic except ARP
not arp

# All traffic except DNS
not port 53

# SSH traffic to a server
tcp port 22 and dst host 10.0.0.5

# Large HTTP packets
tcp port 80 and greater 1000

# All traffic from a host except HTTP
src host 192.168.1.100 and not tcp port 80

# ICMP and DNS only
icmp or udp port 53

# Web traffic (HTTP + HTTPS)
tcp port 80 or tcp port 443
```

---

## Usage with Wireshark GUI

```bash
# Apply capture filter before starting capture
# In the Wireshark filter bar (top), enter the filter
# Or use the "Capture Options" dialog

# Example: Capture filter in Wireshark GUI
# Filter: host 192.168.1.100 and port 80
```

---

## Usage with TShark

```bash
# Basic syntax: tshark -i <interface> -f "<filter>"

# Capture HTTP traffic
tshark -i eth0 -f "tcp port 80"

# Capture to file with filter
tshark -i eth0 -f "host 192.168.1.1" -w capture.pcapng

# Capture for specific duration
tshark -i eth0 -f "tcp port 443" -a duration:300

# Capture limited number of packets
tshark -i eth0 -f "icmp" -c 100
```

---

## Usage with tcpdump

```bash
# Basic syntax: tcpdump -i <interface> -w <file> <filter>

# Capture HTTP traffic
sudo tcpdump -i eth0 port 80 -w http-capture.pcap

# Capture from specific host
sudo tcpdump -i eth0 host 192.168.1.1 -w host-capture.pcap

# Capture with verbose output
sudo tcpdump -i eth0 -v port 80

# Capture with hex and ASCII output
sudo tcpdump -i eth0 -X port 80

# Read capture file
tcpdump -r capture.pcap -nn

# Display filter while reading
tcpdump -r capture.pcap "tcp[tcpflags] & tcp-syn != 0"
```

---

<div align="center">

**[⬆ Back to Wireshark README](README.md)** | **[⬆ Back to Main README](../README.md)**

</div>
