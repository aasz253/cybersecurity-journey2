<div align="center">

# Security Tools

<img src="https://img.shields.io/badge/Burp%20Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white" />
<img src="https://img.shields.io/badge/Nmap-4DA6FF?style=for-the-badge&logo=nmap&logoColor=white" />
<img src="https://img.shields.io/badge/SQLMap-5C7AE6?style=for-the-badge&logo=database&logoColor=white" />

</div>

---

## Files

| Directory | Tool | Description |
|:----------|:-----|:------------|
| [burp-suite/](burp-suite/) | Burp Suite | Web application testing proxy |
| [nmap/](nmap/) | Nmap | Network discovery and scanning |
| [sqlmap/](sqlmap/) | SQLMap | Automated SQL injection testing |

---

## Installation

```bash
# Nmap
sudo apt-get install nmap -y

# SQLMap
sudo apt-get install sqlmap -y
# Or from source
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git

# Nikto
sudo apt-get install nikto -y

# Dirb
sudo apt-get install dirb -y

# WFuzz
pip install wfuzz

# Burp Suite
# Download from https://portswigger.net/burp
```

---

## Quick Usage

```bash
# Nmap - Basic scan
nmap -sV -sC target.com

# Nmap - Vulnerability scan
nmap --script vuln target.com

# SQLMap - Test for injection
sqlmap -u "http://target.com/product?id=1" --dbs

# Nikto - Web server scan
nikto -h http://target.com

# Dirb - Directory enumeration
dirb http://target.com

# WFuzz - Fuzzing
wfuzz -z file,wordlist.txt http://target.com/FUZZ
```

---

<div align="center">

**[⬆ Back to Main README](../README.md)**

</div>
