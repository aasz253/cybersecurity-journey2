"""
CSRF Practice Lab
------------------
A safe environment to practice CSRF attacks and defenses.

SETUP:
  1. pip install flask
  2. python csrf-lab.py
  3. Visit http://localhost:9000

EXERCISES:
  1. View the vulnerable transfer form
  2. Create a malicious page that auto-submits
  3. Test CSRF token protection
  4. Compare SameSite cookie behavior
"""

import secrets
import time
from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Simple user store
USERS = {"sifuna": {"password": "codex2026", "balance": 10000}}
sessions = {}
csrf_tokens = {}


# ---- TEMPLATES ----

VULNERABLE_FORM = """
<!DOCTYPE html>
<html>
<head><title>VULNERABLE - No CSRF Protection</title></head>
<body style="font-family:monospace; background:#1a1a2e; color:#0f0; padding:20px">
<h1 style="color:#ff0000">VULNERABLE Transfer Form</h1>
<p>This form has NO CSRF protection.</p>

<h2>Your Account</h2>
<p>Balance: ${{ balance }}</p>

<h2>Transfer Money</h2>
<form method="POST" action="/transfer-vulnerable">
    To Account: <input type="text" name="to_account" style="background:#0d0d0d;color:#0f0;border:1px solid #0f0"><br><br>
    Amount: $ <input type="number" name="amount" style="background:#0d0d0d;color:#0f0;border:1px solid #0f0"><br><br>
    <button type="submit" style="background:#0f0;color:#000;border:none;padding:5px 15px">Transfer</button>
</form>

<h3 style="color:#ffff00">Attack Scenario:</h3>
<pre style="color:#0affed">
Create a page with this form and trick the victim into visiting it:

&lt;form action="http://localhost:9000/transfer-vulnerable" method="POST"&gt;
    &lt;input type="hidden" name="to_account" value="attacker"&gt;
    &lt;input type="hidden" name="amount" value="10000"&gt;
&lt;/form&gt;
&lt;script&gt;document.forms[0].submit();&lt;/script&gt;
</pre>
</body>
</html>
"""

SECURE_FORM = """
<!DOCTYPE html>
<html>
<head><title>SECURE - CSRF Token Protected</title></head>
<body style="font-family:monospace; background:#1a1a2e; color:#0f0; padding:20px">
<h1 style="color:#00ff41">SECURE Transfer Form</h1>
<p>This form has CSRF token protection.</p>

<h2>Your Account</h2>
<p>Balance: ${{ balance }}</p>

<h2>Transfer Money</h2>
<form method="POST" action="/transfer-secure">
    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
    To Account: <input type="text" name="to_account" style="background:#0d0d0d;color:#0f0;border:1px solid #0f0"><br><br>
    Amount: $ <input type="number" name="amount" style="background:#0d0d0d;color:#0f0;border:1px solid #0f0"><br><br>
    <button type="submit" style="background:#0f0;color:#000;border:none;padding:5px 15px">Transfer</button>
</form>

<h3 style="color:#ffff00">Why this is secure:</h3>
<pre style="color:#0affed">
1. CSRF token is unique per session
2. Token is validated server-side
3. Attacker cannot guess the token
4. Even if victim visits malicious page,
   the form won't have the valid CSRF token
</pre>
</body>
</html>
"""


@app.route("/")
def index():
    return """
    <html>
    <body style="font-family:monospace; background:#1a1a2e; color:#0f0; padding:20px">
    <h1>CSRF Practice Lab</h1>
    <h2>Vulnerable Version</h2>
    <ul>
        <li><a href="/login-vulnerable" style="color:#ff0000">Login (Vulnerable)</a></li>
        <li><a href="/vulnerable" style="color:#ff0000">Transfer Form (No CSRF Protection)</a></li>
    </ul>
    <h2>Secure Version</h2>
    <ul>
        <li><a href="/login-secure" style="color:#00ff41">Login (Secure)</a></li>
        <li><a href="/secure" style="color:#00ff41">Transfer Form (CSRF Token Protected)</a></li>
    </ul>
    <h2>Results</h2>
    <ul>
        <li><a href="/results" style="color:#0affed">View Transfer History</a></li>
    </ul>
    </body>
    </html>
    """


# ---- VULNERABLE (No CSRF Protection) ----

@app.route("/login-vulnerable")
def login_vulnerable():
    session_id = secrets.token_urlsafe(32)
    sessions[session_id] = {"user": "sifuna", "auth": True}
    resp = redirect("/vulnerable")
    resp.set_cookie("session_id", session_id)
    return resp


@app.route("/vulnerable")
def vulnerable():
    session_id = request.cookies.get("session_id")
    user_session = sessions.get(session_id)
    if not user_session:
        return redirect("/login-vulnerable")
    return render_template_string(VULNERABLE_FORM, balance=USERS["sifuna"]["balance"])


@app.route("/transfer-vulnerable", methods=["POST"])
def transfer_vulnerable():
    """No CSRF validation - vulnerable to attack!"""
    session_id = request.cookies.get("session_id")
    user_session = sessions.get(session_id)
    if not user_session:
        return "Unauthorized", 401

    to_account = request.form.get("to_account", "")
    amount = request.form.get("amount", "0")
    transfer_history.append(f"[VULNERABLE] {user_session['user']} -> {to_account}: ${amount}")
    return f"Transfer of ${amount} to {to_account} completed!"


# ---- SECURE (CSRF Token Protected) ----

@app.route("/login-secure")
def login_secure():
    session_id = secrets.token_urlsafe(32)
    csrf_token = secrets.token_hex(32)
    sessions[session_id] = {"user": "sifuna", "auth": True}
    csrf_tokens[session_id] = csrf_token
    resp = redirect("/secure")
    resp.set_cookie("session_id", session_id, samesite="Strict")
    return resp


@app.route("/secure")
def secure():
    session_id = request.cookies.get("session_id")
    user_session = sessions.get(session_id)
    if not user_session:
        return redirect("/login-secure")
    token = csrf_tokens.get(session_id, "")
    return render_template_string(SECURE_FORM, balance=USERS["sifuna"]["balance"], csrf_token=token)


@app.route("/transfer-secure", methods=["POST"])
def transfer_secure():
    """CSRF token validated - secure against attack!"""
    session_id = request.cookies.get("session_id")
    user_session = sessions.get(session_id)
    if not user_session:
        return "Unauthorized", 401

    form_token = request.form.get("csrf_token", "")
    stored_token = csrf_tokens.get(session_id, "")

    if not secrets.compare_digest(form_token, stored_token):
        return "CSRF TOKEN INVALID! Attack detected.", 403

    to_account = request.form.get("to_account", "")
    amount = request.form.get("amount", "0")
    transfer_history.append(f"[SECURE] {user_session['user']} -> {to_account}: ${amount}")
    return f"Transfer of ${amount} to {to_account} completed!"


# ---- RESULTS ----

transfer_history = []

@app.route("/results")
def results():
    html = "<html><body style='font-family:monospace; background:#1a1a2e; color:#0f0; padding:20px'>"
    html += "<h1>Transfer History</h1><ul>"
    for entry in transfer_history:
        html += f"<li>{entry}</li>"
    html += "</ul><a href='/'>Back</a></body></html>"
    return html


if __name__ == "__main__":
    print("[*] CSRF Practice Lab")
    print("[*] Visit http://localhost:9000")
    print("[*] Press Ctrl+C to stop")
    app.run(port=9000, debug=False)
