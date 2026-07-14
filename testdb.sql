-- ============================================
-- Web Security Lab Database Setup
-- testdb.sql
-- ============================================

CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    role ENUM('admin', 'user') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
);

-- Products table
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sessions table
CREATE TABLE IF NOT EXISTS sessions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    session_id VARCHAR(128) NOT NULL UNIQUE,
    user_id INT,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Activity log
CREATE TABLE IF NOT EXISTS activity_log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    details TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- ============================================
-- Sample Data
-- ============================================

-- Users (passwords are bcrypt hashes)
-- admin password: admin123
-- user1 password: pass123
INSERT INTO users (username, password_hash, email, role) VALUES
('admin', '$2b$12$LJ3m4ys1Lz0YBNOURq0Y3OjCfKJmKPOJZqYHrPn8Cj2V5X9aKmGQ6', 'admin@test.com', 'admin'),
('sifuna', '$2b$12$XKx4VZq0YBNOURq0Y3OjCfKJmKPOJZqYHrPn8Cj2V5X9aKmGQ6', 'sifuna@test.com', 'user'),
('user1', '$2b$12$ABc1DeF2GhI3JkL4MnO5PqR6StU7VwX8YzA9BcD0EfG1HiJ2KlM3', 'user1@test.com', 'user'),
('user2', '$2b$12$NOpQ3RsT4UvW5XyZ6AbC7DefG8HiJ9KlM0NoP1QrS2TuV3WxY4Za', 'user2@test.com', 'user');

-- Products
INSERT INTO products (name, price, description, category) VALUES
('Laptop Pro 15', 1299.99, 'High-performance laptop with 16GB RAM', 'Electronics'),
('Wireless Mouse', 29.99, 'Ergonomic wireless optical mouse', 'Accessories'),
('Mechanical Keyboard', 89.99, 'RGB mechanical keyboard with Cherry MX switches', 'Accessories'),
('4K Monitor', 449.99, '27-inch 4K IPS display', 'Electronics'),
('USB-C Hub', 49.99, '7-in-1 USB-C hub with HDMI', 'Accessories'),
('Webcam HD', 79.99, '1080p HD webcam with microphone', 'Electronics'),
('Headset Pro', 149.99, 'Noise-cancelling gaming headset', 'Audio'),
('Desk Lamp', 34.99, 'LED desk lamp with adjustable brightness', 'Lighting'),
('Monitor Stand', 59.99, 'Adjustable aluminum monitor stand', 'Accessories'),
('Cable Management Kit', 19.99, 'Premium cable management solutions', 'Accessories');

-- Activity log entries
INSERT INTO activity_log (user_id, action, details, ip_address) VALUES
(1, 'login', 'Successful login', '192.168.1.100'),
(2, 'login', 'Successful login', '192.168.1.101'),
(1, 'product_view', 'Viewed Laptop Pro 15', '192.168.1.100'),
(2, 'product_view', 'Viewed Wireless Mouse', '192.168.1.101'),
(3, 'login_failed', 'Invalid password attempt', '192.168.1.102');
