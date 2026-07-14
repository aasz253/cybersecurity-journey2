<?php
/**
 * SQL Injection Practice Lab
 * 
 * A safe environment to practice SQL injection attacks.
 * Uses SQLite (no real credentials at risk).
 * 
 * SETUP:
 *   1. php -S localhost:9000 (in this directory)
 *   2. Visit http://localhost:9000/sqli-lab.php
 * 
 * EXERCISES:
 *   1. Extract all usernames
 *   2. Find the admin password
 *   3. Dump the entire users table
 *   4. Use UNION-based injection
 *   5. Use blind SQL injection
 */

// Create SQLite database for practice
$db = new SQLite8(__DIR__ . '/practice.db');

// Create tables
$db->exec("CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    role TEXT DEFAULT 'user'
)");

$db->exec("CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    secret_code TEXT
)");

// Insert sample data (if empty)
$count = $db->querySingle("SELECT COUNT(*) FROM users");
if ($count == 0) {
    $db->exec("INSERT INTO users VALUES (1, 'admin', 's3cur3_p@ss!', 'admin@test.com', 'admin')");
    $db->exec("INSERT INTO users VALUES (2, 'user1', 'pass123', 'user1@test.com', 'user')");
    $db->exec("INSERT INTO users VALUES (3, 'user2', 'qwerty', 'user2@test.com', 'user')");
    
    $db->exec("INSERT INTO products VALUES (1, 'Laptop', 999.99, 'FLAG{sqli_l4b_1s_d0n3}')");
    $db->exec("INSERT INTO products VALUES (2, 'Mouse', 29.99, 'FLAG{un10n_b4s3d}')");
    $db->exec("INSERT INTO products VALUES (3, 'Keyboard', 49.99, 'FLAG{bl1nd_sqli}')");
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SQL Injection Practice Lab</title>
    <style>
        body { font-family: monospace; background: #1a1a2e; color: #0f0; padding: 20px; }
        h1 { color: #00ff41; }
        h2 { color: #0affed; }
        input, button { font-family: monospace; padding: 5px; margin: 5px; }
        input { background: #0d0d0d; color: #0f0; border: 1px solid #0f0; }
        button { background: #0f0; color: #000; cursor: pointer; border: none; }
        .result { background: #0d0d0d; padding: 10px; margin: 10px 0; border: 1px solid #0f0; }
        .hint { color: #ffff00; }
        pre { color: #0affed; }
    </style>
</head>
<body>

<h1>SQL Injection Practice Lab</h1>
<p>This is a SAFE environment to practice SQL injection techniques.</p>

<h2>Exercise 1: Basic Injection</h2>
<pre>Try: 1 OR 1=1</pre>
<form method="GET">
    Product ID: <input type="text" name="id" value="1">
    <button type="submit">Search</button>
</form>

<?php
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    
    // INTENTIONALLY VULNERABLE
    $query = "SELECT * FROM products WHERE id = $id";
    
    echo "<div class='result'>";
    echo "<strong>Query:</strong> " . htmlspecialchars($query) . "<br><br>";
    
    try {
        $result = $db->query($query);
        if ($result) {
            echo "<table border='1' cellpadding='5'>";
            echo "<tr><th>ID</th><th>Name</th><th>Price</th></tr>";
            while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
                echo "<tr><td>{$row['id']}</td><td>{$row['name']}</td><td>{$row['price']}</td></tr>";
            }
            echo "</table>";
        }
    } catch (Exception $e) {
        echo "<span class='hint'>Error: " . $e->getMessage() . "</span>";
    }
    echo "</div>";
}
?>

<h2>Exercise 2: UNION Injection</h2>
<pre>Try: 1 UNION SELECT 1,2,3,4,5</pre>
<p class="hint">Find the number of columns, then extract data from other tables.</p>

<h2>Exercise 3: Blind SQL Injection</h2>
<pre>Try: 1 AND SUBSTR((SELECT password FROM users LIMIT 1),1,1)='s'</pre>
<p class="hint">Use boolean conditions to extract data character by character.</p>

<h2>Exercise 4: Login Bypass</h2>
<pre>Username: admin' --
Password: anything</pre>

<h2>Cheatsheet</h2>
<pre>
' OR 1=1 --                    Basic bypass
' UNION SELECT NULL,NULL,NULL  Column count
' ORDER BY 10--                Find columns
' UNION SELECT username,password FROM users--  Dump data
' AND 1=1--                    True condition
' AND 1=2--                    False condition
' AND SUBSTR(sql,1,1)='s'--    Blind extraction
</pre>

</body>
</html>
