"""
CSRF Protection Implementation
--------------------------------
Demonstrates how to protect against Cross-Site Request Forgery
using tokens, SameSite cookies, and re-authentication.
"""

import secrets
import hashlib
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


# Session and CSRF token storage
sessions = {}
csrf_tokens = {}


class CSRFProtectionDemo(BaseHTTPRequestHandler):
    """Handler demonstrating CSRF protection mechanisms."""

    def do_GET(self):
        if self.path == "/login":
            self._handle_login()
        elif self.path == "/transfer-form":
            self._transfer_form()
        elif self.path == "/vulnerable-transfer":
            self._vulnerable_transfer()
        elif self.path == "/protected-transfer":
            self._protected_transfer()
        else:
            self._show_menu()

    def do_POST(self):
        if self.path == "/login":
            self._handle_login()
        elif self.path == "/transfer":
            self._handle_transfer()

    def _show_menu(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html = """
        <html><body>
        <h1>CSRF Protection Demo</h1>
        
        <h2>VULNERABLE: No CSRF Protection</h2>
        <pre>
// Attacker's malicious page:
&lt;form action="http://bank.com/transfer" method="POST"&gt;
    &lt;input type="hidden" name="to" value="attacker"&gt;
    &lt;input type="hidden" name="amount" value="10000"&gt;
    &lt;input type="submit" value="Click to win prize!"&gt;
&lt;/form&gt;
&lt;script&gt;document.forms[0].submit();&lt;/script&gt;
        </pre>

        <h2>SECURE: CSRF Token Protection</h2>
        <pre>
// Defense mechanisms:
1. Anti-CSRF token in forms
2. SameSite cookie attribute
3. Origin/Referer header validation
4. Re-authentication for sensitive actions
        </pre>

        <ul>
            <li><a href="/login">/login</a> - Get session and CSRF token</li>
            <li><a href="/transfer-form">/transfer-form</a> - Secure transfer form</li>
        </ul>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _handle_login(self):
        """Login and generate CSRF token."""
        session_id = secrets.token_urlsafe(32)
        csrf_token = secrets.token_hex(32)

        sessions[session_id] = {
            "user": "sifuna",
            "created": time.time(),
        }
        csrf_tokens[session_id] = csrf_token

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header(
            "Set-Cookie",
            f"session_id={session_id}; Path=/; HttpOnly; SameSite=Strict"
        )
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Logged In!</h1>
        <p>Session: {session_id[:16]}...</p>
        <p>CSRF Token: <code>{csrf_token}</code></p>
        <p><a href="/transfer-form">Go to Transfer Form</a></p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _transfer_form(self):
        """Secure transfer form with CSRF token."""
        session_id = self._get_cookie("session_id")
        session = sessions.get(session_id)
        csrf_token = csrf_tokens.get(session_id, "")

        if not session:
            self.send_response(401)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"401 - Login required. <a href='/login'>Login</a>")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Transfer Money (CSRF Protected)</h1>
        <form method="POST" action="/transfer">
            <!-- CSRF token hidden in form -->
            <input type="hidden" name="csrf_token" value="{csrf_token}">
            
            <label>To Account:</label><br>
            <input type="text" name="to_account" required><br><br>
            
            <label>Amount ($):</label><br>
            <input type="number" name="amount" required><br><br>
            
            <button type="submit">Transfer</button>
        </form>
        
        <h2>Protection Mechanisms:</h2>
        <ul>
            <li>CSRF token in hidden form field</li>
            <li>Server validates token matches session</li>
            <li>SameSite cookie prevents cross-origin requests</li>
            <li>Attacker cannot guess the CSRF token</li>
        </ul>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _handle_transfer(self):
        """Process transfer with CSRF validation."""
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        params = parse_qs(body)

        session_id = self._get_cookie("session_id")
        session = sessions.get(session_id)

        # Check authentication
        if not session:
            self._respond(401, "Not authenticated")
            return

        # Check CSRF token
        form_token = params.get("csrf_token", [""])[0]
        stored_token = csrf_tokens.get(session_id, "")

        if not secrets.compare_digest(form_token, stored_token):
            self._respond(403, "CSRF token invalid! Attack detected.")
            return

        # Process transfer
        to_account = params.get("to_account", [""])[0]
        amount = params.get("amount", ["0"])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Transfer Successful!</h1>
        <p>To: {to_account}</p>
        <p>Amount: ${amount}</p>
        <p>From: {session['user']}</p>
        <p><a href="/transfer-form">Make Another Transfer</a></p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _get_cookie(self, name):
        cookies = self.headers.get("Cookie", "")
        for cookie in cookies.split(";"):
            cookie = cookie.strip()
            if cookie.startswith(f"{name}="):
                return cookie.split("=", 1)[1]
        return None

    def _respond(self, code, message):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())


def run_server(port=8085):
    server = HTTPServer(("localhost", port), CSRFProtectionDemo)
    print(f"[*] CSRF Protection Demo on http://localhost:{port}")
    print("[*] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
