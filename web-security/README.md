<div align="center">

# Web Security Fundamentals

<img src="https://img.shields.io/badge/Topic-Web%20Security-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Days-5%20%26%206-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Learning%20Complete-00D26A?style=for-the-badge" />

</div>

---

## Contents

| Directory | Description |
|:----------|:------------|
| [http-requests/](http-requests/) | HTTP request/response examples and methods |
| [authentication/](authentication/) | Authentication methods and secure implementations |
| [cookies-sessions/](cookies-sessions/) | Cookie attributes and session management |
| [vulnerabilities/](vulnerabilities/) | Common web vulnerabilities (SQLi, XSS, CSRF) |

---

## HTTP Overview

### Request Structure

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: sessionId=abc123
```

### Response Structure

```http
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: sessionId=xyz789; HttpOnly; Secure
Content-Length: 1234
```

---

## Status Codes

| Code | Meaning |
|:----:|:--------|
| 200 | OK (Success) |
| 201 | Created |
| 301 | Moved Permanently |
| 302 | Found (Redirect) |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## Security Best Practices

```
1. Always use HTTPS
2. Validate all user input
3. Encode all output
4. Use parameterized queries
5. Implement CSRF protection
6. Set secure cookie flags
7. Use strong password hashing
8. Enable MFA where possible
9. Apply rate limiting
10. Log and monitor all access
```

---

<div align="center">

**[⬆ Back to Main README](../README.md)**

</div>
