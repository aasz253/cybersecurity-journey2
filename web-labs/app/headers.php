<?php
/**
 * HTTP Headers Inspector
 * Shows all request and response headers.
 */
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTTP Headers Inspector</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #0a0a1a; color: #00ff41; padding: 30px; }
        h1 { color: #00ff41; text-shadow: 0 0 10px #00ff41; }
        h2 { color: #0affed; }
        table { border-collapse: collapse; width: 100%; margin: 15px 0; }
        th, td { border: 1px solid #00ff41; padding: 8px; text-align: left; }
        th { background: #1a1a2e; }
        .result { background: #0d1117; padding: 15px; margin: 15px 0; border: 1px solid #00ff41; }
        a { color: #0affed; }
    </style>
</head>
<body>

<h1>HTTP HEADERS INSPECTOR</h1>

<h2>Request Headers</h2>
<div class="result">
    <table>
        <tr><th>Header</th><th>Value</th></tr>
        <?php
        foreach ($_SERVER as $key => $value) {
            if (strpos($key, 'HTTP_') === 0 || in_array($key, ['CONTENT_TYPE', 'CONTENT_LENGTH'])) {
                $header = str_replace('_', '-', substr($key, 5));
                echo "<tr><td>" . htmlspecialchars($header) . "</td><td>" . htmlspecialchars($value) . "</td></tr>";
            }
        }
        ?>
    </table>
</div>

<h2>Server Info</h2>
<div class="result">
    <table>
        <tr><th>Item</th><th>Value</th></tr>
        <tr><td>Server Software</td><td><?php echo htmlspecialchars($_SERVER['SERVER_SOFTWARE'] ?? 'Unknown'); ?></td></tr>
        <tr><td>Request Method</td><td><?php echo htmlspecialchars($_SERVER['REQUEST_METHOD'] ?? 'Unknown'); ?></td></tr>
        <tr><td>Request URI</td><td><?php echo htmlspecialchars($_SERVER['REQUEST_URI'] ?? '/'); ?></td></tr>
        <tr><td>Query String</td><td><?php echo htmlspecialchars($_SERVER['QUERY_STRING'] ?? 'None'); ?></td></tr>
        <tr><td>Remote Address</td><td><?php echo htmlspecialchars($_SERVER['REMOTE_ADDR'] ?? 'Unknown'); ?></td></tr>
        <tr><td>Server Port</td><td><?php echo htmlspecialchars($_SERVER['SERVER_PORT'] ?? 'Unknown'); ?></td></tr>
        <tr><td>Document Root</td><td><?php echo htmlspecialchars($_SERVER['DOCUMENT_ROOT'] ?? 'Unknown'); ?></td></tr>
    </table>
</div>

<h2>PHP Headers Sent</h2>
<div class="result">
    <p style="color:#8b949e">Note: PHP processes the request before rendering this page.
    Use browser DevTools (F12) → Network tab to see full request/response headers.</p>
    <p style="color:#ffff00">Try: curl -I http://localhost/?q=test</p>
</div>

<p><a href="index.php">Back to Lab Menu</a></p>

</body>
</html>
