<?php
/**
 * SQL Injection Secure Example
 * 
 * SECURE: Uses prepared statements with parameterized queries.
 * This prevents SQL injection by separating SQL logic from data.
 * 
 * Key security measures:
 * 1. Prepared statements (parameterized queries)
 * 2. Input validation
 * 3. Output encoding
 * 4. Generic error messages
 * 5. Least privilege database access
 */

$conn = new mysqli("localhost", "app_user", "strong_password", "testdb");

if ($conn->connect_error) {
    // SECURE: Generic error message (no details exposed)
    die("Database connection error. Please try again later.");
}

$conn->set_charset("utf8mb4");


// SECURE: Prepared statement for product lookup
function getProductById($conn, $id) {
    // Validate input
    if (!is_numeric($id) || $id < 1) {
        return null;
    }

    // Prepare statement
    $stmt = $conn->prepare("SELECT id, name, price FROM products WHERE id = ?");
    
    // Bind parameter (i = integer)
    $stmt->bind_param("i", $id);
    
    // Execute
    $stmt->execute();
    
    // Get results
    $result = $stmt->get_result();
    $product = $result->fetch_assoc();
    
    $stmt->close();
    return $product;
}

// SECURE: Prepared statement for search
function searchProducts($conn, $search) {
    // Validate input
    $search = trim($search);
    if (empty($search) || strlen($search) > 100) {
        return [];
    }

    // Prepare statement with LIKE
    $stmt = $conn->prepare("SELECT id, name, price FROM products WHERE name LIKE ?");
    
    // Add wildcards for LIKE search
    $search_param = "%{$search}%";
    $stmt->bind_param("s", $search_param);
    
    $stmt->execute();
    $result = $stmt->get_result();
    
    $products = [];
    while ($row = $result->fetch_assoc()) {
        $products[] = $row;
    }
    
    $stmt->close();
    return $products;
}

// SECURE: Login with prepared statement
function login($conn, $username, $password) {
    // Validate input
    if (empty($username) || empty($password)) {
        return null;
    }

    // Prepare statement
    $stmt = $conn->prepare("SELECT id, username, password_hash FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    $user = $result->fetch_assoc();
    $stmt->close();

    // Verify password
    if ($user && password_verify($password, $user['password_hash'])) {
        return $user;
    }

    return null;
}


// === Usage Examples ===

// Product lookup
$id = $_GET['id'] ?? null;
if ($id) {
    $product = getProductById($conn, $id);
    if ($product) {
        // SECURE: Output is escaped
        echo "<div>" . htmlspecialchars($product['name'], ENT_QUOTES, 'UTF-8') . "</div>";
        echo "<div>$" . (float)$product['price'] . "</div>";
    } else {
        echo "Product not found.";
    }
}

// Search
$search = $_GET['search'] ?? null;
if ($search) {
    $products = searchProducts($conn, $search);
    foreach ($products as $product) {
        // SECURE: Output is escaped
        echo "<div>" . htmlspecialchars($product['name'], ENT_QUOTES, 'UTF-8') . "</div>";
    }
}

// Login
$username = $_POST['username'] ?? null;
$password = $_POST['password'] ?? null;
if ($username && $password) {
    $user = login($conn, $username, $password);
    if ($user) {
        echo "Login successful! Welcome, " . htmlspecialchars($user['username']);
    } else {
        // SECURE: Generic error message
        echo "Invalid username or password.";
    }
}

$conn->close();
?>
