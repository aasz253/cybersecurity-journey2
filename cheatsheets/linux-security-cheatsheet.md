<div align="center">

# Linux Security Cheatsheet

</div>

---

## Network Commands

```bash
# Network interfaces
ip addr show
ifconfig

# Listening ports
ss -tlnp
netstat -tlnp

# Active connections
ss -tnp
netstat -tnp

# DNS lookup
dig example.com
nslookup example.com
host example.com

# Packet capture
sudo tcpdump -i eth0 -w capture.pcap
sudo tcpdump -i eth0 port 80
sudo tcpdump -i eth0 host 192.168.1.1
```

## Firewall (iptables)

```bash
# List rules
sudo iptables -L -n

# Allow HTTP
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Allow HTTPS
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Block IP
sudo iptables -A INPUT -s 10.0.0.5 -j DROP

# Allow SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Delete rule
sudo iptables -D INPUT 1
```

## User Management

```bash
# Add user
sudo useradd -m username
sudo passwd username

# Delete user
sudo userdel -r username

# List users
cat /etc/passwd

# List groups
cat /etc/group

# Add to group
sudo usermod -aG sudo username

# Check sudo permissions
sudo -l
```

## File Permissions

```bash
# Change permissions
chmod 755 file.sh
chmod 600 secrets.txt
chmod 644 config.php

# Change ownership
chown user:group file.txt

# Find SUID files
find / -perm -4000 2>/dev/null

# Find world-writable files
find / -perm -0002 2>/dev/null
```

## Process Management

```bash
# List processes
ps aux
top
htop

# Kill process
kill PID
kill -9 PID

# Find process by name
pgrep process_name
ps aux | grep process_name
```

## Log Files

```bash
# System logs
tail -f /var/log/syslog
tail -f /var/log/auth.log

# Web server logs
tail -f /var/log/apache2/access.log
tail -f /var/log/nginx/access.log

# Search logs
grep "Failed password" /var/log/auth.log
grep "404" /var/log/apache2/access.log
```

## Security Scanning

```bash
# Check open ports
nmap -sT localhost
nmap -sV localhost

# Check for rootkits
sudo chkrootkit
sudo rkhunter --check

# Audit users
sudo auditctl -l
sudo lastlog
sudo last
```
