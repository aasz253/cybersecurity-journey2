<?php
/**
 * XSS Lab - INTENTIONALLY VULNERABLE
 * Do NOT use in production.
 */
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>XSS Lab</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #0a0a1a; color: #00ff41; padding: 30px; }
        h1 { color: #ff4444; text-shadow: 0 0 10px #ff0000; }
        h2 { color: #0affed; }
        input, button { font-family: 'Courier New', monospace; padding: 8px; margin: 5px; background: #0d1117; color: #00ff41; border: 1px solid #00ff41; }
        button { background: #00ff41; color: #000; cursor: pointer; font-weight: bold; }
        .result { background: #0d1117; padding: 15px; margin: 15px 0; border: 1px solid #00ff41; }
        .hint { color: #ffff00; background: #1a1a2e; padding: 10px; border: 1px solid #ffff00; margin: 10px 0; }
        pre { color: #0affed; background: #0d1117; padding: 10px; }
        a { color: #0affed; }
    </style>
</head>
<body>

<h1>XSS LAB</h1>
<p style="color:#ff4444">WARNING: This application is intentionally vulnerable!</p>

<h2>Reflected XSS - Search</h2>
<div class="hint">
    TRY: <code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code> or <code>&lt;img src=x onerror=alert(1)&gt;</code>
</div>
<form method="GET">
    <input type="text" name="q" placeholder="Search..." style="width:400px">
    <button type="submit">Search</button>
</form>

<div class="result">
    <strong>Results for: </strong>
    <?php
    if (isset($_GET['q'])) {
        // VULNERABLE: Direct output without encoding
        echo $_GET['q'];
    } else {
        echo "<em>Enter a search term above</em>";
    }
    ?>
</div>

<h2>Stored XSS - Guestbook</h2>
<div class="hint">
    TRY: <code>&lt;script&gt;document.getElementById('flag').innerText='FLAG{xss_st0r3d}'&lt;/script&gt;</code>
</div>
<form method="POST" action="xss.php">
    Name: <input type="text" name="name" style="width:300px"><br>
    Message: <input type="text" name="message" style="width:400px">
    <button type="submit">Post</button>
</form>

<div class="result" id="guestbook">
    <strong>Guestbook:</strong><br>
    <?php
    if (isset($_POST['name']) && isset($_POST['message'])) {
        // VULNERABLE: Stored XSS
        echo "<div><strong>" . $_POST['name'] . "</strong>: " . $_POST['message'] . "</div>";
    }
    ?>
    <div id="flag" style="color:#ffff00;margin-top:10px">FLAG{...hidden...}</div>
</div>

<h2>Cheatsheet</h2>
<pre>
&lt;script&gt;alert('XSS')&lt;/script&gt;                    Basic
&lt;img src=x onerror=alert('XSS')&gt;                 Image error
&lt;svg onload=alert('XSS')&gt;                        SVG
&lt;body onload=alert('XSS')&gt;                       Body
&lt;input onfocus=alert('XSS') autofocus&gt;           Input
&lt;a href=javascript:alert('XSS')&gt;click&lt;/a&gt;        Link
&lt;script&gt;document.cookie&lt;/script&gt;                 Cookie theft
</pre>

<p><a href="index.php">Back to Lab Menu</a></p>

</body>
</html>
