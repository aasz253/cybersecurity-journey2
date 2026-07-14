<?php
/**
 * Cookie Security Lab
 * Compare secure vs insecure cookie configurations.
 */
$action = $_GET['action'] ?? 'menu';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cookie Security Lab</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #0a0a1a; color: #00ff41; padding: 30px; }
        h1 { color: #00ff41; text-shadow: 0 0 10px #00ff41; }
        h2 { color: #0affed; }
        .result { background: #0d1117; padding: 15px; margin: 15px 0; border: 1px solid #00ff41; }
        .insecure { border-color: #ff4444; }
        .secure { border-color: #00ff41; }
        pre { color: #0affed; background: #0d1117; padding: 10px; overflow-x: auto; }
        a { color: #0affed; display: inline-block; margin: 5px 0; }
        button { font-family: 'Courier New', monospace; padding: 8px 16px; background: #00ff41; color: #000; border: none; cursor: pointer; font-weight: bold; margin: 5px; }
    </style>
</head>
<body>

<h1>COOKIE SECURITY LAB</h1>

<?php if ($action === 'menu'): ?>

<h2>Choose a Demo</h2>
<p><a href="?action=insecure">Set INSECURE cookies (no flags)</a></p>
<p><a href="?action=secure">Set SECURE cookies (all flags)</a></p>
<p><a href="?action=read">Read current cookies</a></p>
<p><a href="?action=compare">Compare both configurations</a></p>

<?php elseif ($action === 'insecure'): ?>

<h2 style="color:#ff4444">Setting INSECURE Cookies</h2>
<div class="result insecure">
    <?php
    // INSECURE: No security flags
    setcookie("session_id", "abc123insecure", time() + 3600, "/");
    setcookie("user_prefs", "theme:dark", time() + 3600, "/");
    setcookie("auth_token", "secrettoken", time() + 86400, "/");
    echo "<p style='color:#ff4444'>Cookies set WITHOUT security flags:</p>";
    echo "<pre>";
    echo "Set-Cookie: session_id=abc123insecure; Path=/\n";
    echo "Set-Cookie: user_prefs=theme:dark; Path=/\n";
    echo "Set-Cookie: auth_token=secrettoken; Path=/\n";
    echo "</pre>";
    ?>
</div>
<div class="result insecure">
    <p style="color:#ff4444">RISKS:</p>
    <ul>
        <li>No HttpOnly - JavaScript can steal cookies (XSS)</li>
        <li>No Secure - Sent over HTTP (interception)</li>
        <li>No SameSite - Vulnerable to CSRF</li>
        <li>No Domain restriction - Available to all paths</li>
    </ul>
</div>
<p><a href="?action=read">View cookies</a> | <a href="?action=menu">Back</a></p>

<?php elseif ($action === 'secure'): ?>

<h2 style="color:#00ff41">Setting SECURE Cookies</h2>
<div class="result secure">
    <?php
    // SECURE: All security flags
    setcookie("session_id", "xyz789secure", [
        'expires' => time() + 1800,
        'path' => '/',
        'httponly' => true,
        'secure' => false, // Set true in production with HTTPS
        'samesite' => 'Strict',
    ]);
    setcookie("user_prefs", "theme:dark", [
        'expires' => time() + 1800,
        'path' => '/',
        'httponly' => true,
        'secure' => false,
        'samesite' => 'Lax',
    ]);
    echo "<p style='color:#00ff41'>Cookies set WITH all security flags:</p>";
    echo "<pre>";
    echo "Set-Cookie: session_id=xyz789secure; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=1800\n";
    echo "Set-Cookie: user_prefs=theme:dark; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=1800\n";
    echo "</pre>";
    ?>
</div>
<div class="result secure">
    <p style="color:#00ff41">PROTECTIONS:</p>
    <ul>
        <li>HttpOnly - JavaScript cannot access (XSS protection)</li>
        <li>Secure - Only sent over HTTPS (interception protection)</li>
        <li>SameSite=Strict - No cross-origin requests (CSRF protection)</li>
        <li>Short Max-Age - Automatic expiration</li>
    </ul>
</div>
<p><a href="?action=read">View cookies</a> | <a href="?action=menu">Back</a></p>

<?php elseif ($action === 'read'): ?>

<h2>Current Cookies</h2>
<div class="result">
    <pre><?php echo htmlspecialchars(print_r($_COOKIE, true)); ?></pre>
    <p style="color:#ffff00">Open DevTools (F12) → Application → Cookies to see flags</p>
</div>
<p><a href="?action=menu">Back to menu</a></p>

<?php elseif ($action === 'compare'): ?>

<h2>Side-by-Side Comparison</h2>
<div class="result insecure">
    <h3 style="color:#ff4444">INSECURE</h3>
    <pre>Set-Cookie: session=abc123; Path=/
Set-Cookie: token=secret; Path=/

VULNERABILITIES:
- JavaScript can read (XSS)
- Sent over HTTP (MITM)
- No CSRF protection
- No expiration</pre>
</div>
<div class="result secure">
    <h3 style="color:#00ff41">SECURE</h3>
    <pre>Set-Cookie: session=xyz789; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=1800

PROTECTIONS:
- HttpOnly: JS cannot access
- Secure: HTTPS only
- SameSite: CSRF protection
- Max-Age: Auto expiration</pre>
</div>
<p><a href="?action=menu">Back to menu</a></p>

<?php endif; ?>

<p><a href="index.php">Back to Lab Menu</a></p>

</body>
</html>
