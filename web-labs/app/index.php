<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Security Lab</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Courier New', monospace; background: #0a0a1a; color: #00ff41; padding: 40px; }
        h1 { color: #00ff41; text-align: center; font-size: 2.5em; margin-bottom: 10px; text-shadow: 0 0 10px #00ff41; }
        .subtitle { text-align: center; color: #0affed; margin-bottom: 40px; font-size: 1.2em; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }
        .card { background: #0d1117; border: 1px solid #00ff41; border-radius: 8px; padding: 25px; transition: 0.3s; }
        .card:hover { border-color: #0affed; box-shadow: 0 0 15px rgba(10,255,237,0.3); transform: translateY(-3px); }
        .card h2 { color: #0affed; margin-bottom: 15px; font-size: 1.3em; }
        .card .tag { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.75em; margin-bottom: 10px; }
        .tag-vuln { background: #ff000033; color: #ff4444; border: 1px solid #ff4444; }
        .tag-secure { background: #00ff4133; color: #00ff41; border: 1px solid #00ff41; }
        .card p { color: #8b949e; line-height: 1.6; margin-bottom: 15px; }
        .card a { display: inline-block; padding: 8px 20px; background: #00ff41; color: #000; text-decoration: none; border-radius: 4px; font-weight: bold; transition: 0.3s; }
        .card a:hover { background: #0affed; }
        .flag { background: #1a1a2e; border: 1px solid #ffff00; padding: 20px; border-radius: 8px; margin-top: 30px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto; }
        .flag h3 { color: #ffff00; }
        .disclaimer { text-align: center; color: #ff4444; margin-top: 30px; font-size: 0.9em; border-top: 1px solid #ff444433; padding-top: 20px; }
    </style>
</head>
<body>

<h1>WEB SECURITY LAB</h1>
<p class="subtitle">Hands-on vulnerable applications for security learning</p>

<div class="grid">

    <!-- SQL Injection Lab -->
    <div class="card">
        <span class="tag tag-vuln">VULNERABLE</span>
        <h2>SQL Injection Lab</h2>
        <p>Practice SQL injection attacks on a real database. Extract data, bypass authentication, and learn parameterized queries.</p>
        <a href="sqli.php">Launch Lab</a>
    </div>

    <!-- XSS Lab -->
    <div class="card">
        <span class="tag tag-vuln">VULNERABLE</span>
        <h2>XSS Lab</h2>
        <p>Test Reflected, Stored, and DOM-based Cross-Site Scripting attacks. See why output encoding matters.</p>
        <a href="xss.php">Launch Lab</a>
    </div>

    <!-- Secure SQLi Version -->
    <div class="card">
        <span class="tag tag-secure">SECURE</span>
        <h2>Secure SQL Example</h2>
        <p>See how parameterized queries and prepared statements prevent SQL injection.</p>
        <a href="secure-sqli.php">Launch Lab</a>
    </div>

    <!-- Secure XSS Version -->
    <div class="card">
        <span class="tag tag-secure">SECURE</span>
        <h2>Secure XSS Example</h2>
        <p>See how output encoding and CSP headers prevent Cross-Site Scripting.</p>
        <a href="secure-xss.php">Launch Lab</a>
    </div>

    <!-- HTTP Headers -->
    <div class="card">
        <span class="tag tag-secure">LEARNING</span>
        <h2>HTTP Headers Inspector</h2>
        <p>View request and response headers. Understand how HTTP works under the hood.</p>
        <a href="headers.php">Launch Lab</a>
    </div>

    <!-- Cookie Lab -->
    <div class="card">
        <span class="tag tag-vuln">VULNERABLE</span>
        <h2>Cookie Security Lab</h2>
        <p>Compare secure vs insecure cookie configurations. See how HttpOnly, Secure, and SameSite flags work.</p>
        <a href="cookies.php">Launch Lab</a>
    </div>

</div>

<div class="flag">
    <h3>CHALLENGE: Find all the hidden flags!</h3>
    <p style="color: #8b949e;">Each lab contains a hidden FLAG{...} string. Can you find them all?</p>
</div>

<div class="disclaimer">
    <p>FOR EDUCATIONAL PURPOSES ONLY. Use these labs only in authorized environments.</p>
</div>

</body>
</html>
