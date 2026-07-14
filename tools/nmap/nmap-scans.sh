#!/bin/bash
# ============================================
# Nmap Scanning Scripts
# ============================================
# Educational reference for network scanning.
# Use only on authorized targets!
# ============================================

echo "============================================"
echo "  Nmap Scanning Reference"
echo "  Author: Sifuna Codex"
echo "============================================"

# -------------------------------------------
# BASIC SCANS
# -------------------------------------------

# Quick scan - top 1000 ports
# nmap -sT target.com

# Scan all ports
# nmap -sT -p- target.com

# SYN scan (stealthy, requires root)
# sudo nmap -sS target.com

# UDP scan
# sudo nmap -sU target.com

# -------------------------------------------
# SERVICE DETECTION
# -------------------------------------------

# Detect service versions
# nmap -sV target.com

# Detect service versions with default scripts
# nmap -sV -sC target.com

# Aggressive scan (OS detection, version, scripts, traceroute)
# nmap -A target.com

# -------------------------------------------
# VULNERABILITY SCANNING
# -------------------------------------------

# Run all vulnerability scripts
# nmap --script vuln target.com

# Run specific script categories
# nmap --script "http-*" target.com
# nmap --script "auth" target.com
# nmap --script "discovery" target.com

# -------------------------------------------
# WEB APPLICATION SCANNING
# -------------------------------------------

# HTTP title discovery
# nmap --script http-title target.com

# Detect web technologies
# nmap --script http-enum target.com

# SQL injection detection
# nmap --script http-sql-injection target.com

# XSS detection
# nmap --script http-xssed target.com

# Directory brute force
# nmap --script http-brute target.com

# WordPress enumeration
# nmap --script http-wordpress-enum target.com

# -------------------------------------------
# OUTPUT FORMATS
# -------------------------------------------

# Normal output
# nmap -oN scan-results.txt target.com

# XML output (for tools like Metasploit)
# nmap -oX scan-results.xml target.com

# All formats
# nmap -oA scan-results target.com

# -------------------------------------------
# COMMON SCAN COMBINATIONS
# -------------------------------------------

# Quick web server scan
# nmap -sV -p 80,443,8080 target.com

# Full web scan
# nmap -sV -sC --script http-* -p 80,443 target.com

# Database server scan
# nmap -sV -p 3306,5432,1433,27017 target.com

# Mail server scan
# nmap -sV -p 25,110,143,993,995 target.com

echo ""
echo "[*] Uncomment commands above to use."
echo "[*] Always get authorization before scanning!"
