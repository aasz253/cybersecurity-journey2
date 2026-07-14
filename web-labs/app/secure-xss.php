<?php
/**
 * Secure XSS Example - Uses Output Encoding
 * Shows how to prevent XSS properly.
 */
header("Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'");
header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: DENY");
header("X-XSS-Protection: 1; mode=block");

$search = isset($_GET['q']) ? $_GET['q'] : '';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure XSS Example</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #0a0a1a; color: #00ff41; padding: 30px; }
        h1 { color: #00ff41; text-shadow: 0 0 10px #00ff41; }
        h2 { color: #0affed; }
        input, button { font-family: 'Courier New', monospace; padding: 8px; margin: 5px; background: #0d1117; color: #00ff41; border: 1px solid #00ff41; }
        button { background: #00ff41; color: #000; cursor: pointer; font-weight: bold; }
        .result { background: #0d1117; padding: 15px; margin: 15px 0; border: 1px solid #00ff41; }
        .secure { color: #00ff41; background: #0d1117; padding: 10px; border: 1px solid #00ff41; margin: 10px 0; }
        pre { color: #0affed; background: #0d1117; padding: 10px; }
        a { color: #0affed; }
    </style>
</head>
<body>

<h1>SECURE XSS EXAMPLE</h1>

<div class="secure">
    SECURITY: This page uses output encoding and CSP headers.
    Try the same XSS payloads - they won't execute!
</div>

<h2>Search (Secure)</h2>
<form method="GET">
    <input type="text" name="q" placeholder="Search..." value="<?php echo htmlspecialchars($search, ENT_QUOTES, 'UTF-8'); ?>" style="width:400px">
    <button type="submit">Search</button>
</form>

<div class="result">
    <strong>Results for: </strong>
    <?php
    if ($search) {
        // SECURE: Output is encoded
        echo htmlspecialchars($search, ENT_QUOTES, 'UTF-8');
    } else {
        echo "<em>Enter a search term above</em>";
    }
    ?>
</div>

<h2>Why This Is Secure</h2>
<pre>
// SERVER-SIDE OUTPUT ENCODING
echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');

// SECURITY HEADERS
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block

// CLIENT-SIDE (use textContent, not innerHTML)
element.textContent = userInput;
</pre>

<h2>Protection Layers</h2>
<pre>
✅ Output encoding (htmlspecialchars)
✅ Content Security Policy (CSP) headers
✅ Input validation (length limits)
✅ X-Content-Type-Options: nosniff
✅ X-Frame-Options: DENY
✅ textContent instead of innerHTML
</pre>

<p><a href="index.php">Back to Lab Menu</a></p>

</body>
</html>
