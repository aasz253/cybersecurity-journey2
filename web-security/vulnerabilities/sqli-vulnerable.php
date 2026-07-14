<?php
/**
 * SQL Injection Vulnerable Example
 * 
 * WARNING: This code is INTENTIONALLY VULNERABLE.
 * Do NOT use in production. For educational purposes only.
 * 
 * Vulnerabilities:
 * 1. Direct variable interpolation in SQL query
 * 2. No input validation
 * 3. No prepared statements
 * 4. Error messages exposed to user
 * 5. No output encoding
 */

$conn = mysqli_connect("localhost", "root", "", "testdb");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// VULNERABLE: Direct interpolation in SQL query
// Attack: ?id=1 OR 1=1 -- returns ALL users
// Attack: ?id=1; DROP TABLE users -- deletes table
// Attack: ?id=1' UNION SELECT username, password FROM users -- dumps credentials
$id = $_GET['id'];
$query = "SELECT * FROM products WHERE id = $id";
$result = mysqli_query($conn, $query);

if ($result) {
    echo "<h2>Products</h2>";
    while ($row = mysqli_fetch_assoc($result)) {
        // VULNERABLE: No output encoding (XSS)
        echo "<div>" . $row['name'] . " - $" . $row['price'] . "</div>";
    }
} else {
    // VULNERABLE: Exposing error details
    echo "Error: " . mysqli_error($conn);
}

// VULNERABLE: Search endpoint
$search = $_GET['search'];
// Attack: ?search=<script>alert('XSS')</script>
// Attack: ?search=' OR 1=1 --
$search_query = "SELECT * FROM products WHERE name LIKE '%$search%'";
$result2 = mysqli_query($conn, $search_query);

if ($result2) {
    while ($row = mysqli_fetch_assoc($result2)) {
        // VULNERABLE: XSS - direct output of user input
        echo "<div>" . $row['name'] . "</div>";
    }
}

// VULNERABLE: Login check
$username = $_GET['username'];
$password = $_GET['password'];
// Attack: ?username=admin' -- &password=anything
// Attack: ?username=' OR '1'='1&password=' OR '1'='1
$login_query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$login_result = mysqli_query($conn, $login_query);

if (mysqli_num_rows($login_result) > 0) {
    echo "Login successful!";
} else {
    echo "Login failed!";
}

mysqli_close($conn);
?>
