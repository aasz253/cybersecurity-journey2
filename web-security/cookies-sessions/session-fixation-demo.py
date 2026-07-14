"""
Session Fixation Attack Demo
------------------------------
Demonstrates how session fixation vulnerabilities work
and how to prevent them.
"""

import secrets
import time
from http.server import HTTPServer, BaseHTTPRequestHandler


# INSECURE session store (no regeneration)
insecure_sessions = {}

# SECURE session store (with regeneration)
secure_sessions = {}


def generate_session_id():
    return secrets.token_urlsafe(32)


class SessionFixationDemo(BaseHTTPRequestHandler):
    """Demo showing session fixation vulnerability."""

    def do_GET(self):
        if self.path == "/insecure-login":
            self._insecure_login()
        elif self.path == "/secure-login":
            self._secure_login()
        elif self.path == "/check":
            self._check_session()
        else:
            self._show_menu()

    def _show_menu(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html = """
        <html><body>
        <h1>Session Fixation Demo</h1>

        <h2>VULNERABLE (/insecure-login)</h2>
        <p>Session ID is NOT regenerated after login.
           An attacker who sets a session ID before login
           will share the authenticated session.</p>
        <pre>
# Attack flow:
1. Attacker visits site, gets session_id=KNOWN_VALUE
2. Attacker tricks victim into using session_id=KNOWN_VALUE
3. Victim logs in with the known session_id
4. Attacker uses session_id=KNOWN_VALUE to access victim's account
        </pre>

        <h2>SECURE (/secure-login)</h2>
        <p>Session ID IS regenerated after login.
           Previous session ID is invalidated.</p>
        <pre>
# Defense:
1. Session.regenerate() after successful authentication
2. Old session ID is destroyed
3. New cryptographically random ID is issued
        </pre>

        <ul>
            <li><a href="/insecure-login">/insecure-login</a> - Vulnerable login</li>
            <li><a href="/secure-login">/secure-login</a> - Secure login</li>
            <li><a href="/check">/check</a> - Check current session</li>
        </ul>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _insecure_login(self):
        """
        INSECURE: Does NOT regenerate session ID after login.
        Vulnerable to session fixation attacks.
        """
        # Get or create session (does NOT change after login)
        session_id = self._get_cookie("session_id")
        if not session_id:
            session_id = generate_session_id()

        # Store session (attacker-controlled ID persists)
        insecure_sessions[session_id] = {
            "user": "sifuna",
            "authenticated": True,
            "created": time.time(),
        }

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header(
            "Set-Cookie",
            f"session_id={session_id}; Path=/; HttpOnly"
        )
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Insecure Login (VULNERABLE!)</h1>
        <p>Session ID: <code>{session_id}</code></p>
        <p>WARNING: This session ID was NOT regenerated after login.</p>
        <p>If an attacker set this session ID before you logged in,
           they now have access to your account!</p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _secure_login(self):
        """
        SECURE: Regenerates session ID after login.
        Prevents session fixation attacks.
        """
        # Invalidate old session
        old_session_id = self._get_cookie("session_id")
        if old_session_id in secure_sessions:
            del secure_sessions[old_session_id]

        # Generate NEW session ID (regeneration)
        new_session_id = generate_session_id()
        secure_sessions[new_session_id] = {
            "user": "sifuna",
            "authenticated": True,
            "created": time.time(),
        }

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header(
            "Set-Cookie",
            f"session_id={new_session_id}; Path=/; HttpOnly; SameSite=Strict"
        )
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Secure Login (Session Regenerated!)</h1>
        <p>New Session ID: <code>{new_session_id}</code></p>
        <p>This session ID was regenerated after login.</p>
        <p>Any previously known session ID has been invalidated.</p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _check_session(self):
        """Display current session details."""
        session_id = self._get_cookie("session_id")
        insecure = insecure_sessions.get(session_id)
        secure = secure_sessions.get(session_id)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Session Check</h1>
        <p>Cookie Value: <code>{session_id or 'None'}</code></p>
        <p>Insecure Store: {'AUTHENTICATED' if insecure else 'Not found'}</p>
        <p>Secure Store: {'AUTHENTICATED' if secure else 'Not found'}</p>
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


def run_server(port=8084):
    server = HTTPServer(("localhost", port), SessionFixationDemo)
    print(f"[*] Session Fixation Demo on http://localhost:{port}")
    print("[*] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
