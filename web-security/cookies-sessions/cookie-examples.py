"""
Cookie Examples
----------------
Demonstrates cookie attributes and security implications.
Shows secure vs insecure cookie configurations.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler


class CookieDemoHandler(BaseHTTPRequestHandler):
    """Handler demonstrating cookie attributes and security."""

    def do_GET(self):
        if self.path == "/insecure":
            self._set_insecure_cookies()
        elif self.path == "/secure":
            self._set_secure_cookies()
        elif self.path == "/read":
            self._read_cookies()
        else:
            self._show_menu()

    def _show_menu(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html = """
        <html>
        <head><title>Cookie Security Demo</title></head>
        <body>
            <h1>Cookie Security Demo</h1>
            <h2>Vulnerable Cookie Attributes</h2>
            <ul>
                <li><a href="/insecure">/insecure</a> - Sets cookies WITHOUT security flags</li>
            </ul>
            <h2>Secure Cookie Attributes</h2>
            <ul>
                <li><a href="/secure">/secure</a> - Sets cookies WITH all security flags</li>
            </ul>
            <h2>Read Cookies</h2>
            <ul>
                <li><a href="/read">/read</a> - Display current cookies</li>
            </ul>
            <h2>Browser DevTools</h2>
            <p>Open Developer Tools (F12) and check the Application tab to see cookies.</p>
            <h2>Wireshark Analysis</h2>
            <p>Capture HTTP traffic to see Set-Cookie headers in plaintext.</p>
            <pre>
tshark -i eth0 -f "tcp port 80" -Y "http.set_cookie" -T fields -e http.set_cookie
            </pre>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def _set_insecure_cookies(self):
        """
        INSECURE cookies - missing security flags.
        Vulnerable to XSS, CSRF, and session hijacking.
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")

        # INSECURE - Missing HttpOnly, Secure, SameSite
        self.send_header(
            "Set-Cookie",
            "session_id=abc123insecure; Path=/; Max-Age=3600"
        )
        # INSECURE - No domain restriction
        self.send_header(
            "Set-Cookie",
            "user_prefs=theme:dark,lang:en; Path=/"
        )
        # INSECURE - Overly broad path
        self.send_header(
            "Set-Cookie",
            "auth_token=secrettoken123; Path=/; Max-Age=86400"
        )
        self.end_headers()

        html = """
        <html><body>
        <h1>Insecure Cookies Set!</h1>
        <p>These cookies have NO security flags:</p>
        <ul>
            <li>No HttpOnly - JavaScript can access (XSS risk)</li>
            <li>No Secure - Sent over HTTP (interception risk)</li>
            <li>No SameSite - Vulnerable to CSRF</li>
        </ul>
        <p>Check browser DevTools > Application > Cookies</p>
        <p>Check Wireshark for plaintext cookie values!</p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _set_secure_cookies(self):
        """
        SECURE cookies - all security flags set.
        Protected against XSS, CSRF, and session hijacking.
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")

        # SECURE - All flags set
        self.send_header(
            "Set-Cookie",
            "session_id=xyz789secure; Path=/; Max-Age=3600; "
            "HttpOnly; Secure; SameSite=Strict"
        )
        # SECURE - Domain restricted
        self.send_header(
            "Set-Cookie",
            "user_prefs=theme:dark,lang:en; Path=/; "
            "HttpOnly; Secure; SameSite=Lax; Domain=localhost"
        )
        # SECURE - Short-lived auth token
        self.send_header(
            "Set-Cookie",
            "auth_token=securetoken456; Path=/; Max-Age=900; "
            "HttpOnly; Secure; SameSite=Strict"
        )
        self.end_headers()

        html = """
        <html><body>
        <h1>Secure Cookies Set!</h1>
        <p>These cookies have ALL security flags:</p>
        <ul>
            <li>HttpOnly - JavaScript cannot access (XSS protection)</li>
            <li>Secure - Only sent over HTTPS (interception protection)</li>
            <li>SameSite=Strict - CSRF protection</li>
            <li>Domain restriction - Scoped to specific domain</li>
            <li>Short Max-Age - Automatic expiration</li>
        </ul>
        <p>Check browser DevTools > Application > Cookies</p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _read_cookies(self):
        """Display cookies sent by the client."""
        cookies = self.headers.get("Cookie", "No cookies set")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Current Cookies</h1>
        <pre>{cookies}</pre>
        <p><a href="/">Back to menu</a></p>
        </body></html>
        """
        self.wfile.write(html.encode())


def run_server(port=8082):
    server = HTTPServer(("localhost", port), CookieDemoHandler)
    print(f"[*] Cookie Demo server running on http://localhost:{port}")
    print("[*] Visit /insecure for vulnerable cookies")
    print("[*] Visit /secure for secure cookies")
    print("[*] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
