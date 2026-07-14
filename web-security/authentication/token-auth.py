"""
Token-Based Authentication Example (JWT)
-----------------------------------------
Demonstrates JSON Web Token authentication flow.
JWT is stateless - the token itself contains user claims.
"""

import hashlib
import hmac
import json
import base64
import time
import secrets
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


# Secret key for JWT signing (in production, use env variable)
SECRET_KEY = secrets.token_hex(32)

# Simulated user database
USERS = {
    "sifuna": hashlib.sha256("codex2026".encode()).hexdigest(),
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
}


def base64url_encode(data):
    """Base64url encode without padding."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def base64url_decode(data):
    """Base64url decode with padding restoration."""
    padding = 4 - len(data) % 4
    if padding != 4:
        data += "=" * padding
    return base64.urlsafe_b64decode(data)


def create_jwt(payload, secret, expires_in=3600):
    """
    Create a JWT token.

    Header:  {"alg": "HS256", "typ": "JWT"}
    Payload: {"user": "...", "exp": ..., "iat": ...}
    Signature: HMAC-SHA256(header + "." + payload, secret)
    """
    # Header
    header = {"alg": "HS256", "typ": "JWT"}
    header_encoded = base64url_encode(json.dumps(header))

    # Payload with expiration
    payload["iat"] = int(time.time())
    payload["exp"] = int(time.time()) + expires_in
    payload_encoded = base64url_encode(json.dumps(payload))

    # Signature
    signing_input = f"{header_encoded}.{payload_encoded}"
    signature = hmac.new(
        secret.encode("utf-8"),
        signing_input.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    signature_encoded = base64url_encode(signature)

    return f"{header_encoded}.{payload_encoded}.{signature_encoded}"


def verify_jwt(token, secret):
    """
    Verify a JWT token.
    Returns payload if valid, None if invalid or expired.
    """
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None

        header_encoded, payload_encoded, signature_encoded = parts

        # Recalculate signature
        signing_input = f"{header_encoded}.{payload_encoded}"
        expected_sig = hmac.new(
            secret.encode("utf-8"),
            signing_input.encode("utf-8"),
            hashlib.sha256,
        ).digest()
        expected_encoded = base64url_encode(expected_sig)

        # Verify signature
        if not hmac.compare_digest(signature_encoded, expected_encoded):
            return None

        # Decode payload
        payload = json.loads(base64url_decode(payload_encoded))

        # Check expiration
        if payload.get("exp", 0) < time.time():
            return None

        return payload

    except Exception:
        return None


class TokenAuthHandler(BaseHTTPRequestHandler):
    """Handler demonstrating Token-based Authentication."""

    def do_GET(self):
        if self.path == "/login":
            self._handle_login()
        elif self.path == "/protected":
            self._handle_protected()
        else:
            self._send_response(404, "Not Found")

    def _handle_login(self):
        """Authenticate and issue JWT token."""
        # In production, parse POST body for credentials
        username = "sifuna"
        password = "codex2026"

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if username in USERS and USERS[username] == password_hash:
            token = create_jwt(
                {"user": username, "role": "student"},
                SECRET_KEY,
                expires_in=3600,
            )
            response = json.dumps({
                "message": "Login successful",
                "token": token,
                "expires_in": 3600,
            })
            self._send_response(200, response, content_type="application/json")
        else:
            self._send_response(401, '{"error": "Invalid credentials"}')

    def _handle_protected(self):
        """Access protected resource with JWT."""
        auth_header = self.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            self._send_response(401, '{"error": "Missing or invalid token"}')
            return

        token = auth_header.split(" ", 1)[1]
        payload = verify_jwt(token, SECRET_KEY)

        if payload:
            response = json.dumps({
                "message": f"Welcome, {payload['user']}!",
                "role": payload["role"],
                "expires_at": payload["exp"],
            })
            self._send_response(200, response, content_type="application/json")
        else:
            self._send_response(401, '{"error": "Invalid or expired token"}')

    def _send_response(self, code, body, content_type="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


def run_server(port=8081):
    server = HTTPServer(("localhost", port), TokenAuthHandler)
    print(f"[*] JWT Auth server running on http://localhost:{port}")
    print("[*] Login:   curl http://localhost:8081/login")
    print("[*] Protected: curl -H 'Authorization: Bearer <token>' http://localhost:8081/protected")
    print("[*] Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()
