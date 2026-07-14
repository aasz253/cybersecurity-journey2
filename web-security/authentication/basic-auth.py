"""
Basic Authentication Example
------------------------------
Demonstrates HTTP Basic Authentication mechanism.
WARNING: Basic auth sends credentials Base64 encoded (NOT encrypted).
Always use HTTPS with Basic Authentication.
"""

import base64
import hashlib
import os
from http.server import HTTPServer, BaseHTTPRequestHandler


# Simulated user database (in production, use a real database with hashed passwords)
USERS = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "sifuna": hashlib.sha256("codex2026".encode()).hexdigest(),
}


class BasicAuthHandler(BaseHTTPRequestHandler):
    """Handler demonstrating Basic Authentication."""

    def _check_auth(self):
        """Check for valid Basic Authentication header."""
        auth_header = self.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Basic "):
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="Secure Area"')
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"401 - Authentication Required")
            return False

        # Decode credentials
        encoded_credentials = auth_header.split(" ", 1)[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        username, password = decoded_credentials.split(":", 1)

        # Verify credentials
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if username in USERS and USERS[username] == password_hash:
            return True

        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Secure Area"')
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"401 - Invalid Credentials")
        return False

    def do_GET(self):
        """Handle GET requests with Basic Auth."""
        if self._check_auth():
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"200 - Access Granted! Welcome, authenticated user.")


def run_server(port=8080):
    """Start the Basic Auth demo server."""
    server = HTTPServer(("localhost", port), BasicAuthHandler)
    print(f"[*] Basic Auth server running on http://localhost:{port}")
    print("[*] Try: curl -u admin:admin123 http://localhost:8080")
    print("[*] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
