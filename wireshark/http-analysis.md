<div align="center">

# HTTP Traffic Analysis with Wireshark

<img src="https://img.shields.io/badge/Topic-HTTP%20Analysis-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Tool-Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" />

</div>

---

## HTTP Request Structure

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64)
Accept: text/html,application/xhtml+xml
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: sessionId=abc123; theme=dark
```

### HTTP Methods

| Method | Purpose | Has Body? |
|:-------|:--------|:---------:|
| GET | Retrieve data | No |
| POST | Submit data | Yes |
| PUT | Update resource | Yes |
| DELETE | Remove resource | No |
| HEAD | Get headers only | No |
| OPTIONS | Get supported methods | No |
| PATCH | Partial update | Yes |

---

## HTTP Response Structure

```http
HTTP/1.1 200 OK
Date: Mon, 01 Jan 2026 00:00:00 GMT
Server: Apache/2.4.41
Content-Type: text/html; charset=UTF-8
Content-Length: 1234
Set-Cookie: sessionId=xyz789; HttpOnly; Secure; SameSite=Strict
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'

<!DOCTYPE html>
<html>
<head><title>Example</title></head>
<body><h1>Hello World</h1></body>
</html>
```

### Status Codes

| Code | Meaning | Category |
|:----:|:--------|:---------|
| 200 | OK | Success |
| 201 | Created | Success |
| 301 | Moved Permanently | Redirection |
| 302 | Found (Temporary Redirect) | Redirection |
| 400 | Bad Request | Client Error |
| 401 | Unauthorized | Client Error |
| 403 | Forbidden | Client Error |
| 404 | Not Found | Client Error |
| 500 | Internal Server Error | Server Error |
| 502 | Bad Gateway | Server Error |
| 503 | Service Unavailable | Server Error |

---

## Wireshark HTTP Analysis Steps

### Step 1: Capture HTTP Traffic

```bash
# Using TShark
tshark -i eth0 -f "tcp port 80" -w http-capture.pcapng

# Using tcpdump
sudo tcpdump -i eth0 port 80 -w http-capture.pcap
```

### Step 2: Filter HTTP Packets

```bash
# In Wireshark Display Filter
http

# Show only GET requests
http.request.method == "GET"

# Show only POST requests
http.request.method == "POST"

# Show specific host
http.host == "www.example.com"
```

### Step 3: Follow TCP Stream

```
Right-click a packet → Follow → TCP Stream

This shows the complete conversation between client and server.
```

### Step 4: Export HTTP Objects

```
File → Export Objects → HTTP

This extracts files transferred over HTTP:
- Images (PNG, JPG, GIF)
- HTML files
- JavaScript files
- CSS files
- Any other file type
```

---

## Common HTTP Patterns in Wireshark

### Detecting Login Attempts

```bash
# Find POST requests (potential logins)
http.request.method == "POST"

# Find requests to login endpoints
http.request.uri contains "login"
http.request.uri contains "auth"
http.request.uri contains "signin"
```

### Detecting File Downloads

```bash
# Find large HTTP responses
http.response && frame.len > 50000

# Find specific file types
http.content_type contains "application/pdf"
http.content_type contains "application/zip"
http.content_type contains "application/octet-stream"
```

### Detecting API Calls

```bash
# Find JSON API calls
http.content_type contains "application/json"

# Find API endpoints
http.request.uri contains "/api/"
http.request.uri contains "/v1/"
http.request.uri contains "/v2/"
```

---

## TShark Commands for HTTP Analysis

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXTRACT HTTP DATA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Show HTTP host and URI
tshark -r capture.pcapng -Y "http.request" -T fields -e http.host -e http.request.uri

# Show HTTP methods and status codes
tshark -r capture.pcapng -Y "http" -T fields -e http.request.method -e http.response.code

# Show HTTP cookies
tshark -r capture.pcapng -Y "http.cookie" -T fields -e http.cookie

# Show HTTP user agents
tshark -r capture.pcapng -Y "http.request" -T fields -e http.user_agent

# Export all HTTP objects
tshark -r capture.pcapng -q --export-objects http,exported_files/

# Show HTTP content type
tshark -r capture.pcapng -Y "http" -T fields -e http.content_type


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HTTP STATISTICS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# HTTP request/response pairs
tshark -r capture.pcapng -qz http,tree

# HTTP statistics
tshark -r capture.pcapng -qz http,stat

# Show HTTP requests by host
tshark -r capture.pcapng -Y "http.request" -T fields -e http.host | sort | uniq -c | sort -rn
```

---

## Practical Exercise: Analyze a Web Request

```bash
# 1. Start capture
tshark -i eth0 -f "tcp port 80" -w exercise-http.pcapng

# 2. Visit a website (in browser or curl)
curl http://httpbin.org/get
curl -X POST -d "username=admin&password=test" http://httpbin.org/post

# 3. Stop capture (Ctrl+C)

# 4. Analyze the capture
tshark -r exercise-http.pcapng -Y "http"

# 5. Follow the TCP stream
tshark -r exercise-http.pcapng -qz follow,tcp,stream,0

# 6. Extract any objects
tshark -r exercise-http.pcapng -q --export-objects http,exported/

# 7. Check for credentials in POST data
tshark -r exercise-http.pcapng -Y "http.request.method == POST" -T fields -e http.file_data
```

---

<div align="center">

**[⬆ Back to Wireshark README](README.md)** | **[⬆ Back to Main README](../README.md)**

</div>
