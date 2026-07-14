<?php
/**
 * XSS Secure Example
 * 
 * Demonstrates proper output encoding and CSP headers
 * to prevent Cross-Site Scripting (XSS) attacks.
 * 
 * Key defenses:
 * 1. htmlspecialchars() for HTML context
 * 2. Content Security Policy (CSP) headers
 * 3. Input validation
 * 4. HttpOnly cookies
 * 5. X-Content-Type-Options header
 */

// Set security headers to prevent XSS
header("Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'");
header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: DENY");
header("X-XSS-Protection: 1; mode=block");

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Search Results</title>
</head>
<body>
    <h1>Search Results</h1>

    <?php
    // Get search query
    $query = $_GET['q'] ?? '';

    // VALIDATE: Check input length and content
    if (strlen($query) > 100) {
        echo "<p>Error: Search query too long.</p>";
    } elseif (empty($query)) {
        echo "<p>Please enter a search term.</p>";
    } else {
        // ENCODE: htmlspecialchars prevents XSS in HTML context
        // ENT_QUOTES: encodes both single and double quotes
        // UTF-8: ensures proper character encoding
        $safe_query = htmlspecialchars($query, ENT_QUOTES, 'UTF-8');

        echo "<p>Search results for: <strong>{$safe_query}</strong></p>";

        // Simulated search results
        $results = ["Network Security", "Web Security", "Penetration Testing", "Wireshark Guide"];
        $found = false;

        foreach ($results as $result) {
            if (stripos($result, $query) !== false) {
                // ENCODE: All output is escaped
                echo "<div>" . htmlspecialchars($result, ENT_QUOTES, 'UTF-8') . "</div>";
                $found = true;
            }
        }

        if (!$found) {
            echo "<p>No results found for: {$safe_query}</p>";
        }
    }
    ?>

    <script>
        // SECURE: Use textContent instead of innerHTML
        // textContent does NOT parse HTML/JS
        var userInput = new URLSearchParams(window.location.search).get('q');
        var safeDiv = document.createElement('div');
        safeDiv.textContent = 'You searched for: ' + userInput;
        document.getElementById('results').appendChild(safeDiv);
        
        // NEVER use innerHTML with user input
        // NEVER use eval() with user input
        // NEVER use document.write() with user input
    </script>

    <h2>Security Features Active</h2>
    <ul>
        <li>Content Security Policy (CSP) enabled</li>
        <li>Output encoding with htmlspecialchars()</li>
        <li>Input validation (length check)</li>
        <li>X-Content-Type-Options: nosniff</li>
        <li>X-Frame-Options: DENY</li>
    </ul>

    <h2>Safe Links (No XSS)</h2>
    <ul>
        <li><a href="?q=network">Search: network</a></li>
        <li><a href="?q=security">Search: security</a></li>
        <li><a href="?q=wireshark">Search: wireshark</a></li>
    </ul>
</body>
</html>
