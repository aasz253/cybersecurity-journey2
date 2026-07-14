"""
Secure Authentication Implementation (Flask)
----------------------------------------------
Demonstrates secure login, session management, CSRF protection,
and password hashing using bcrypt.
"""

import bcrypt
import secrets
from functools import wraps
from flask import Flask, request, session, redirect, url_for, jsonify


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Simulated user database
# In production: use PostgreSQL/MySQL with proper ORM
USERS_DB = {}


def hash_password(password):
    """Hash password with bcrypt and random salt."""
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def check_password(password, password_hash):
    """Verify password against bcrypt hash."""
    return bcrypt.checkpw(password.encode("utf-8"), password_hash)


def login_required(f):
    """Decorator to require authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.route("/register", methods=["POST"])
def register():
    """
    Secure user registration.
    - Hashes password with bcrypt
    - Validates input
    - Prevents duplicate users
    """
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Input validation
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if len(username) < 3:
        return jsonify({"error": "Username must be 3+ characters"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be 8+ characters"}), 400

    if username in USERS_DB:
        return jsonify({"error": "Username already exists"}), 409

    # Hash and store
    password_hash = hash_password(password)
    USERS_DB[username] = {
        "password_hash": password_hash,
        "role": "user",
    }

    return jsonify({"message": "Registration successful"}), 201


@app.route("/login", methods=["POST"])
def login():
    """
    Secure login with:
    - Password verification
    - Session regeneration (prevent fixation)
    - CSRF token generation
    - Rate limiting (conceptual)
    """
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = USERS_DB.get(username)

    if not user or not check_password(password, user["password_hash"]):
        # Generic message to prevent user enumeration
        return jsonify({"error": "Invalid credentials"}), 401

    # Regenerate session to prevent fixation
    session.clear()
    session["user_id"] = username
    session["role"] = user["role"]
    session["csrf_token"] = secrets.token_hex(32)

    return jsonify({
        "message": "Login successful",
        "csrf_token": session["csrf_token"],
    })


@app.route("/logout", methods=["POST"])
def logout():
    """Secure logout - clear session."""
    session.clear()
    return jsonify({"message": "Logged out successfully"})


@app.route("/profile", methods=["GET"])
@login_required
def profile():
    """Protected route - requires authentication."""
    user = USERS_DB.get(session["user_id"])
    return jsonify({
        "user": session["user_id"],
        "role": session["role"],
    })


@app.route("/change-password", methods=["POST"])
@login_required
def change_password():
    """
    Secure password change.
    - Requires current password
    - Validates new password strength
    - Rehashes with new salt
    """
    current_password = request.form.get("current_password", "")
    new_password = request.form.get("new_password", "")

    user = USERS_DB.get(session["user_id"])

    if not check_password(current_password, user["password_hash"]):
        return jsonify({"error": "Current password incorrect"}), 401

    if len(new_password) < 8:
        return jsonify({"error": "New password must be 8+ characters"}), 400

    # Rehash with new salt
    user["password_hash"] = hash_password(new_password)

    return jsonify({"message": "Password changed successfully"})


@app.route("/transfer", methods=["POST"])
@login_required
def transfer():
    """
    Protected action with CSRF token verification.
    """
    csrf_token = request.form.get("csrf_token", "")

    # Verify CSRF token
    if not secrets.compare_digest(csrf_token, session.get("csrf_token", "")):
        return jsonify({"error": "CSRF token invalid"}), 403

    amount = request.form.get("amount", "0")
    to_account = request.form.get("to_account", "")

    # Process transfer (demo only)
    return jsonify({
        "message": f"Transfer of ${amount} to {to_account} initiated",
    })


if __name__ == "__main__":
    print("[*] Flask Secure Auth Server")
    print("[*] Register:  POST /register (username, password)")
    print("[*] Login:     POST /login (username, password)")
    print("[*] Profile:   GET  /profile (Authorization: Bearer <session>)")
    print("[*] Transfer:  POST /transfer (amount, to_account, csrf_token)")
    app.run(debug=False, port=5000)
