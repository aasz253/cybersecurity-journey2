"""
Session Management Example
---------------------------
Demonstrates secure session lifecycle:
creation, validation, expiration, and destruction.
"""

import secrets
import time
import hashlib
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


# In-memory session store (in production, use Redis/DB)
sessions = {}

# Session configuration
SESSION_TIMEOUT = 1800  # 30 minutes
MAX_SESSIONS_PER_USER = 3


def generate_session_id():
    """Generate cryptographically random session ID."""
    return secrets.token_urlsafe(32)


def create_session(username):
    """
    Create a new session with security best practices:
    - Random session ID
    - Expiration timestamp
    - Track creation time
    - Limit concurrent sessions
    """
    # Enforce max sessions per user
    user_sessions = [
        sid for sid, data in sessions.items()
        if data.get("username") == username
    ]
    if len(user_sessions) >= MAX_SESSIONS_PER_USER:
        # Remove oldest session
        oldest = min(user_sessions, key=lambda s: sessions[s]["created"])
        del sessions[oldest]

    session_id = generate_session_id()
    sessions[session_id] = {
        "username": username,
        "created": time.time(),
        "expires": time.time() + SESSION_TIMEOUT,
        "ip_address": "127.0.0.1",  # In production: get from request
        "user_agent": "Demo",       # In production: get from request
    }
    return session_id


def validate_session(session_id):
    """
    Validate session ID:
    - Check if session exists
    - Check if session has expired
    - Refresh expiration on activity
    """
    if not session_id or session_id not in sessions:
        return None

    session = sessions[session_id]

    # Check expiration
    if time.time() > session["expires"]:
        del sessions[session_id]
        return None

    # Refresh expiration (sliding window)
    session["expires"] = time.time() + SESSION_TIMEOUT

    return session


def destroy_session(session_id):
    """Destroy session (logout)."""
    if session_id in sessions:
        del sessions[session_id]


class SessionDemoHandler(BaseHTTPRequestHandler):
    """Handler demonstrating session management."""

    def do_GET(self):
        if self.path == "/login":
            self._handle_login()
        elif self.path == "/dashboard":
            self._handle_dashboard()
        elif self.path == "/logout":
            self._handle_logout()
        elif self.path == "/sessions":
            self._list_sessions()
        else:
            self._show_menu()

    def do_POST(self):
        if self.path == "/login":
            self._handle_login()

    def _get_cookie(self, name):
        """Extract specific cookie from request."""
        cookies = self.headers.get("Cookie", "")
        for cookie in cookies.split(";"):
            cookie = cookie.strip()
            if cookie.startswith(f"{name}="):
                return cookie.split("=", 1)[1]
        return None

    def _show_menu(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        html = """
        <html><body>
        <h1>Session Management Demo</h1>
        <ul>
            <li><a href="/login">/login</a> - Create new session</li>
            <li><a href="/dashboard">/dashboard</a> - Access protected page</li>
            <li><a href="/logout">/logout</a> - Destroy session</li>
            <li><a href="/sessions">/sessions</a> - View active sessions (admin)</li>
        </ul>
        <h2>Session Security Features</h2>
        <ul>
            <li>Cryptographically random session IDs</li>
            <li>Automatic expiration (30 min timeout)</li>
            <li>Sliding window expiration</li>
            <li>Max 3 concurrent sessions per user</li>
            <li>Session regeneration after login</li>
        </ul>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _handle_login(self):
        """Create session after authentication."""
        username = "sifuna"  # Demo: hardcoded user
        session_id = create_session(username)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        # Set session cookie with security flags
        self.send_header(
            "Set-Cookie",
            f"session_id={session_id}; Path=/; "
            f"HttpOnly; SameSite=Strict; "
            f"Max-Age={SESSION_TIMEOUT}"
        )
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Session Created!</h1>
        <p>Session ID: <code>{session_id}</code></p>
        <p>Expires in: {SESSION_TIMEOUT // 60} minutes</p>
        <p><a href="/dashboard">Go to Dashboard</a></p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _handle_dashboard(self):
        """Access protected resource with valid session."""
        session_id = self._get_cookie("session_id")
        session = validate_session(session_id)

        if not session:
            self.send_response(401)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            html = """
            <html><body>
            <h1>401 - Session Invalid or Expired</h1>
            <p><a href="/login">Login again</a></p>
            </body></html>
            """
            self.wfile.write(html.encode())
            return

        remaining = int(session["expires"] - time.time())
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = f"""
        <html><body>
        <h1>Dashboard - Access Granted</h1>
        <p>User: {session['username']}</p>
        <p>Session expires in: {remaining} seconds</p>
        <p><a href="/logout">Logout</a></p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _handle_logout(self):
        """Destroy session (logout)."""
        session_id = self._get_cookie("session_id")
        destroy_session(session_id)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        # Clear the cookie
        self.send_header(
            "Set-Cookie",
            "session_id=; Path=/; Max-Age=0"
        )
        self.end_headers()
        html = """
        <html><body>
        <h1>Logged Out</h1>
        <p>Session destroyed.</p>
        <p><a href="/login">Login again</a></p>
        </body></html>
        """
        self.wfile.write(html.encode())

    def _list_sessions(self):
        """List all active sessions (admin view)."""
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = "<html><body><h1>Active Sessions</h1><table border='1'>"
        html += "<tr><th>Session ID</th><th>User</th><th>Created</th><th>Expires</th></tr>"

        for sid, data in sessions.items():
            remaining = int(data["expires"] - time.time())
            if remaining > 0:
                html += f"<tr><td>{sid[:16]}...</td><td>{data['username']}</td>"
                html += f"<td>{time.ctime(data['created'])}</td>"
                html += f"<td>{remaining}s</td></tr>"

        html += "</table></body></html>"
        self.wfile.write(html.encode())


def run_server(port=8083):
    server = HTTPServer(("localhost", port), SessionDemoHandler)
    print(f"[*] Session Demo server running on http://localhost:{port}")
    print("[*] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
