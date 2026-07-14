<div align="center">

# Web Vulnerabilities Reference

<img src="https://img.shields.io/badge/OWASP-Top%2010-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/Category-Vulnerabilities-orange?style=for-the-badge" />

</div>

---

## Files in This Directory

| File | Vulnerability | Type |
|:-----|:-------------|:-----|
| [sqli-vulnerable.php](sqli-vulnerable.php) | SQL Injection | Insecure Code |
| [sqli-secure.php](sqli-secure.php) | SQL Injection | Secure Code |
| [xss-vulnerable.html](xss-vulnerable.html) | Cross-Site Scripting | Insecure Code |
| [xss-secure.php](xss-secure.php) | Cross-Site Scripting | Secure Code |
| [csrf-protection.py](csrf-protection.py) | CSRF | Secure Code |

---

## OWASP Top 10 (2021)

| # | Vulnerability | Description |
|:--|:-------------|:------------|
| A01 | Broken Access Control | Unauthorized access to resources |
| A02 | Cryptographic Failures | Weak encryption, exposed secrets |
| A03 | Injection | SQL, NoSQL, OS, LDAP injection |
| A04 | Insecure Design | Missing security architecture |
| A05 | Security Misconfiguration | Default configs, unnecessary features |
| A06 | Vulnerable Components | Outdated libraries, known CVEs |
| A07 | Auth Failures | Weak passwords, session issues |
| A08 | Data Integrity Failures | Insecure deserialization, CI/CD |
| A09 | Logging Failures | Insufficient monitoring |
| A10 | SSRF | Server-Side Request Forgery |

---

## SQL Injection Quick Reference

```
Attack:  ?id=1 OR 1=1 --
Attack:  ?id=1' UNION SELECT username,password FROM users --
Attack:  ?id=1'; DROP TABLE users; --
Defense: Use parameterized queries (prepared statements)
Defense: Input validation
Defense: Least privilege database access
```

## XSS Quick Reference

```
Attack:  <script>alert('XSS')</script>
Attack:  <img src=x onerror=alert(1)>
Attack:  <svg onload=alert('XSS')>
Defense: htmlspecialchars() for HTML output
Defense: Content Security Policy (CSP) headers
Defense: Use textContent, not innerHTML
```

## CSRF Quick Reference

```
Attack:  Hidden form on attacker's site targeting bank.com/transfer
Defense: Anti-CSRF tokens in forms
Defense: SameSite cookie attribute
Defense: Re-authentication for sensitive actions
Defense: Validate Origin/Referer headers
```

---

<div align="center">

**[⬆ Back to Web Security README](README.md)** | **[⬆ Back to Main README](../README.md)**

</div>
