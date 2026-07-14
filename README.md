<div align="center">

<!-- shields.io badges -->
<a href="https://github.com/sifuna-denson/cybersecurity-journey">
  <img src="https://komarev.com/ghpvc/?username=sifuna-denson&label=Repository%20Views&color=0e75b6&style=flat" alt="Repository Views"/>
</a>

<img src="https://img.shields.io/badge/Day%205--6-Wireshark%20%26%20Web%20Security-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=github" />
<img src="https://img.shields.io/badge/Tools-Wireshark%20%7C%20Burp%20Suite%20%7C%20Nmap-blue?style=for-the-badge" />

<br/>

<!-- animated typing SVG -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=0E75B6&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=100&lines=%F0%9F%9A%AA+Sifuna+Codex;Cybersecurity+Student+%7C+Ethical+Hacker;Welcome+to+My+Learning+Journey" alt="Typing SVG" />

</div>

---

## About Me

```
╔══════════════════════════════════════════════════════════════╗
║  Name    : Sifuna Anthony                                    ║
║  Alias   : Sifuna Codex                                      ║
║  Role    : Cybersecurity Student                             ║
║  Focus   : Network Analysis & Web Security                   ║
║  Tools   : Wireshark | Burp Suite | Nmap | SQLMap            ║
║  Goal    : Master Ethical Hacking & Secure Development       ║
╚══════════════════════════════════════════════════════════════╝
```

---

## What I Learned (Days 5-6)

<div align="center">

| Day | Topic | Status |
|:---:|:------|:------:|
| 5 | Wireshark Deep Dive - Packet Capture & Analysis | ✅ |
| 5 | HTTP/HTTPS Protocol Analysis | ✅ |
| 6 | Web Security Fundamentals | ✅ |
| 6 | Cookies, Sessions & Authentication | ✅ |
| 6 | SQL Injection & XSS Vulnerabilities | ✅ |
| 6 | Secure Coding Practices | ✅ |

</div>

---

## Repository Structure

```
cybersecurity-journey/
│
├── README.md                          # 📋 This file
│
├── wireshark/                         # 🔍 Network Analysis
│   ├── README.md                      # Wireshark overview & setup
│   ├── capture-filters.md             # Capture filter commands
│   ├── display-filters.md             # Display filter commands
│   ├── http-analysis.md               # HTTP traffic analysis
│   └── sample-captures/               # Sample .pcap files
│
├── web-security/                      # 🌐 Web Security
│   ├── README.md                      # Web security overview
│   ├── http-requests/                 # HTTP request/response examples
│   │   ├── GET-request.txt
│   │   ├── POST-request.txt
│   │   └── HTTP-methods.md
│   ├── authentication/                # Auth methods & examples
│   │   ├── basic-auth.py
│   │   ├── token-auth.py
│   │   └── secure-auth-flask.py
│   ├── cookies-sessions/              # Cookie & session management
│   │   ├── cookie-examples.py
│   │   ├── session-management.py
│   │   └── session-fixation-demo.py
│   └── vulnerabilities/               # Vulnerability examples
│       ├── README.md
│       ├── sqli-vulnerable.php
│       ├── sqli-secure.php
│       ├── xss-vulnerable.html
│       ├── xss-secure.php
│       └── csrf-protection.py
│
├── tools/                             # 🛠️ Security Tools
│   ├── README.md
│   ├── burp-suite/
│   │   └── burp-extension.py
│   ├── nmap/
│   │   └── nmap-scans.sh
│   └── sqlmap/
│       └── sqlmap-commands.txt
│
├── practice-labs/                     # 🧪 Hands-On Labs
│   ├── README.md
│   ├── sqli-examples/
│   │   └── sqli-lab.php
│   ├── xss-examples/
│   │   └── xss-lab.html
│   └── csrf-examples/
│       └── csrf-lab.py
│
├── cheatsheets/                       # 📝 Quick Reference
│   ├── wireshark-cheatsheet.md
│   ├── web-security-cheatsheet.md
│   └── linux-security-cheatsheet.md
│
├── resources/                         # 📚 Learning Resources
│   └── resources.md
│
├── docker-compose.yml                 # 🐳 Lab Environment Setup
├── testdb.sql                         # 🗄️ Database Setup
└── LICENSE                            # 📜 MIT License
```

---

## Quick Start

### Clone the Repository

```bash
git clone https://github.com/sifuna-denson/cybersecurity-journey.git
cd cybersecurity-journey
```

### Setup Lab Environment

```bash
# Start the vulnerable web apps
docker-compose up -d

# Access the apps
# SQLi Lab:      http://localhost:8080
# XSS Lab:       http://localhost:8081
# Main Web App:  http://localhost:80
# phpMyAdmin:    http://localhost:8082
```

---

## Wireshark Commands

```bash
# Install Wireshark
sudo apt-get install wireshark -y

# Capture HTTP traffic on interface
sudo wireshark -i eth0 -f "tcp port 80"

# TShark command line capture
tshark -i eth0 -f "tcp port 80" -Y "http.request" -w capture.pcapng

# Read and filter capture
tshark -r capture.pcapng -Y "http.request.method == GET"

# Export HTTP objects
tshark -r capture.pcapng -q --export-objects http,exported_files/

# Follow TCP stream
tshark -r capture.pcapng -qz follow,tcp,stream,0
```

---

## Web Security Code Examples

### SQL Injection - Vulnerable vs Secure

```php
// VULNERABLE - SQL Injection
$query = "SELECT * FROM users WHERE id = $_GET[id]";

// SECURE - Parameterized Query
$stmt = $conn->prepare("SELECT * FROM users WHERE id = ?");
$stmt->bind_param("i", $_GET['id']);
$stmt->execute();
```

### XSS - Vulnerable vs Secure

```php
// VULNERABLE - Cross-Site Scripting
echo $_GET['search'];

// SECURE - Output Encoding
echo htmlspecialchars($_GET['search'], ENT_QUOTES, 'UTF-8');
```

### Secure Authentication

```python
import bcrypt, secrets
from flask import Flask, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

@app.route('/login', methods=['POST'])
def login():
    user = get_user_by_username(request.form['username'])
    if user and bcrypt.checkpw(request.form['password'].encode(), user['pw_hash']):
        session.clear()
        session['user_id'] = user['id']
        session['csrf_token'] = secrets.token_hex(16)
        return "Login successful"
    return "Invalid credentials", 401
```

---

## Tools Used

<div align="center">

| Tool | Purpose | Status |
|:----:|:--------|:------:|
| <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat&logo=wireshark&logoColor=white" /> | Packet Analysis | Active |
| <img src="https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat&logo=burpsuite&logoColor=white" /> | Web App Testing | Active |
| <img src="https://img.shields.io/badge/Nmap-4DA6FF?style=flat&logo=nmap&logoColor=white" /> | Network Scanning | Active |
| <img src="https://img.shields.io/badge/SQLMap-5C7AE6?style=flat&logo=database&logoColor=white" /> | SQL Injection | Active |
| <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" /> | Automation | Active |
| <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" /> | Lab Environment | Active |

</div>

---

## Practice Platforms

- [HackTheBox](https://www.hackthebox.com) - CTF challenges
- [TryHackMe](https://tryhackme.com) - Guided learning
- [PortSwigger Academy](https://portswigger.net/web-security) - Web security labs
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop) - Vulnerable web app

---

## Progress Tracker

```text
██████████████████░░░░░░  65% Complete

[✅] Networking Basics (Days 1-2)
[✅] Ports & Protocols   (Days 3-4)
[✅] Wireshark & Web Sec (Days 5-6)  <-- YOU ARE HERE
[🔄] SQL Injection Deep  (Days 7-8)
[⬜] XSS & CSRF          (Days 9-10)
[⬜] Auth & Sessions     (Days 11-12)
[⬜] Advanced Topics     (Days 13+)
```

---

## Disclaimer

```
This repository is for EDUCATIONAL PURPOSES ONLY.
All techniques and tools demonstrated are to be used
only in authorized environments. Practice responsibly.
```

---

<div align="center">

<!-- animated footer -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=16&duration=4000&pause=1000&color=0E75B6&center=true&vCenter=true&multiline=true&repeat=true&width=500&height=80&lines=%F0%9F%94%97+Always+Learn+New+Techniques;%F0%9F%9A%AA+Practice+Ethical+Hacking;%F0%9F%9A%AA+Document+Everything" alt="Footer Typing SVG" />

<br/>

**Sifuna Codex** | Cybersecurity Student

![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

*"The only way to do great work is to love what you do."*

</div>
