<?php
/**
 * Secure SQL Example - Uses Prepared Statements
 * Shows how to prevent SQL injection properly.
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
    $id = (int)$_GET['id'];
    
    $stmt = $conn->prepare("SELECT id, name, price, description FROM products WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $results = '<table border="1" cellpadding="8" cellspacing="0" style="border-color:#00ff41;width:100%">';
        $results .= '<tr style="background:#1a1a2e"><th>ID</th><th>Name</th><th>Price</th><th>Description</th></tr>';
        while ($row = $result->fetch_assoc()) {
            $results .= "<tr><td>" . htmlspecialchars($row['id']) . "</td>";
            $results .= "<td>" . htmlspecialchars($row['name']) . "</td>";
            $results .= "<td>$" . htmlspecialchars($row['price']) . "</td>";
            $results .= "<td>" . htmlspecialchars($row['description']) . "</td></tr>";
        }
        $results .= '</table>';
    } else {
        $error = "No product found with that ID.";
    }
    $stmt->close();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure SQL Example</title>
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

<h1>SECURE SQL EXAMPLE</h1>

<div class="secure">
    SECURITY: This page uses prepared statements and parameterized queries.
    Try the same SQL injection payloads - they won't work here!
</div>

<h2>Product Lookup (Secure)</h2>
<form method="GET">
    Product ID: <input type="text" name="id" value="1" style="width:300px">
    <button type="submit">Search</button>
</form>

<div class="result">
    <?php echo $results; ?>
    <?php if ($error) echo "<p style='color:#ffff00'>$error</p>"; ?>
</div>

<h2>Why This Is Secure</h2>
<pre>
// PREPARED STATEMENT (secure)
$stmt = $conn->prepare("SELECT * FROM products WHERE id = ?");
$stmt->bind_param("i", $id);  // 'i' = integer type
$stmt->execute();
$result = $stmt->get_result();

// INPUT VALIDATION
$id = (int)$_GET['id'];  // Cast to integer

// OUTPUT ENCODING
echo htmlspecialchars($row['name'], ENT_QUOTES, 'UTF-8');
</pre>

<h2>Protection Layers</h2>
<pre>
✅ Prepared statements (parameterized queries)
✅ Input validation (integer casting)
✅ Output encoding (htmlspecialchars)
✅ Least privilege database user
✅ Generic error messages
</pre>

<p><a href="index.php">Back to Lab Menu</a></p>

</body>
</html>
