<div align="center">

# Wireshark Cheatsheet

</div>

---

## Installation

```bash
sudo apt-get install wireshark -y
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark $USER
```

## Capture Filters

```bash
host 192.168.1.1              # Specific host
src host 192.168.1.100        # Source only
dst host 192.168.1.200        # Destination only
net 192.168.1.0/24            # Subnet
port 80                       # Specific port
portrange 8000-9000           # Port range
tcp                           # TCP only
udp                           # UDP only
icmp                          # ICMP only
!arp                          # Exclude ARP
greater 100                   # Packet > 100 bytes
less 50                       # Packet < 50 bytes
```

## Display Filters

```bash
# HTTP
http                              # All HTTP
http.request.method == "GET"      # GET requests
http.request.method == "POST"     # POST requests
http.host == "example.com"        # Specific host
http.request.uri contains "login" # URI contains text
http.response.code == 404         # 404 errors
http.response.code >= 400         # All errors

# TCP
tcp.port == 443                   # Port 443
tcp.flags.syn == 1                # SYN packets
tcp.flags.fin == 1                # FIN packets
tcp.flags.reset == 1              # RST packets
tcp.stream eq 0                   # Stream 0
tcp.analysis.retransmission       # Retransmissions

# IP
ip.src == 192.168.1.100           # Source IP
ip.dst == 192.168.1.200           # Dest IP
ip.addr == 192.168.1.100          # Either direction

# DNS
dns                               # All DNS
dns.qry.name == "example.com"     # Specific domain
dns.flags.response == 1           # Responses only

# TLS
tls.handshake                     # Handshake
tls.handshake.extensions_server_name == "example.com"

# Combined
http.request.method == "POST" && ip.src == 192.168.1.100
tcp.port == 443 && ip.dst == 10.0.0.1
!arp && !dns
frame contains "password"
```

## TShark Commands

```bash
# Capture
tshark -i eth0 -f "tcp port 80" -w capture.pcapng
tshark -i eth0 -a duration:60 -w capture.pcapng

# Read
tshark -r capture.pcapng -Y "http.request"
tshark -r capture.pcapng -Y "http.request.method == GET"

# Extract fields
tshark -r capture.pcapng -Y "http.request" -T fields -e http.host -e http.request.uri
tshark -r capture.pcapng -Y "http.cookie" -T fields -e http.cookie

# Export objects
tshark -r capture.pcapng -q --export-objects http,exported/

# Statistics
tshark -r capture.pcapng -qz follow,tcp,stream,0
tshark -r capture.pcapng -qz conv,tcp
tshark -r capture.pcapng -qz io,phs
```
