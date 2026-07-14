<div align="center">

# Practice Labs

<img src="https://img.shields.io/badge/Type-Hands%20On-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Level-Beginner-blue?style=for-the-badge" />

</div>

---

## Labs Overview

| Lab | File | Vulnerability | Skill Level |
|:----|:-----|:-------------|:------------|
| SQL Injection | [sqli-lab.php](sqli-examples/sqli-lab.php) | SQLi | Beginner |
| XSS | [xss-lab.html](xss-examples/xss-lab.html) | XSS | Beginner |
| CSRF | [csrf-lab.py](csrf-examples/csrf-lab.py) | CSRF | Intermediate |

---

## Running the Labs

### SQL Injection Lab

```bash
# Requires PHP with SQLite extension
cd practice-labs/sqli-examples
php -S localhost:9000

# Visit http://localhost:9000/sqli-lab.php
```

### XSS Lab

```bash
# Requires PHP
cd practice-labs/xss-examples
php -S localhost:9001

# Visit http://localhost:9001/xss-lab.html
```

### CSRF Lab

```bash
# Requires Python + Flask
pip install flask
cd practice-labs/csrf-examples
python csrf-lab.py

# Visit http://localhost:9000
```

---

## Practice Goals

### SQL Injection

- [ ] Extract all usernames from products table
- [ ] Find the admin password using UNION injection
- [ ] Use blind SQLi to extract data character by character
- [ ] Bypass login authentication
- [ ] Dump entire database

### XSS

- [ ] Achieve reflected XSS via search box
- [ ] Create stored XSS in guestbook
- [ ] Craft payload to steal cookies
- [ ] Achieve DOM-based XSS via URL fragment
- [ ] Build keylogger using XSS

### CSRF

- [ ] Create malicious page that auto-submits transfer
- [ ] Test without CSRF token (should succeed)
- [ ] Test with invalid CSRF token (should fail)
- [ ] Understand SameSite cookie behavior

---

## Docker Lab Environment

```bash
# Start all vulnerable apps
docker-compose up -d

# Access:
# SQLi Lab:    http://localhost:8080
# XSS Lab:     http://localhost:8081
# Main App:    http://localhost:80
# phpMyAdmin:  http://localhost:8082
```

---

<div align="center">

**[⬆ Back to Main README](../README.md)**

</div>
