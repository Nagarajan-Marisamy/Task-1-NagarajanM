# Task-1-NagarajanM
Password Integrity Checker

A Python-based Password Integrity Checker that evaluates password strength, blocks weak and common passwords, securely hashes passwords using Argon2id, protects token verification against timing attacks, and performs basic memory cleanup after processing.

Features
Phase 1: Gatekeeper (Password Validation)
1. Minimum Length Check
Ensures the password is at least 8 characters long.
Rejects shorter passwords immediately.
2. Common Password Detection
Compares the entered password against a list of frequently used passwords.
Prevents the use of easily guessable passwords such as:
password
password123
12345678
qwerty123
admin123
etc.
3. Password Strength Scoring

The password is evaluated based on:

Requirement	Score
Contains lowercase letters	+1
Contains uppercase letters	+1
Contains digits	+1
Contains special characters	+1
Length ≥ 8 characters	+1

Maximum Score: 5/5

4. Password Strength Classification
Score	Classification
0 – 2	Weak (Rejected)
3 – 4	Medium
5	Strong

The program also provides recommendations for missing password components.

Phase 2: Secure Password Hashing (Argon2id)

Passwords are hashed using Argon2id, which is recommended by modern security standards and the OWASP Password Storage Cheat Sheet.

Benefits:

Resistant to brute-force attacks
Memory-hard algorithm
Industry-standard password hashing method
Generates a unique salt automatically

Example hash:

$argon2id$v=19$m=65536,t=3,p=4$...
Phase 3: Timing Attack Mitigation

The program generates a secure session token using Python's secrets module:

session_token = secrets.token_hex(16)

Token verification is performed using:

hmac.compare_digest()

This prevents timing-based side-channel attacks by ensuring comparisons take constant time.

Secure Memory Cleanup

After processing:

The password is stored in a mutable bytearray
The contents are overwritten with zeros
Variables containing the password are deleted

Example:

password[:] = b'\x00' * len(password)
del password
del password_input

This reduces the chance of sensitive data remaining in memory longer than necessary.

Installation
1. Clone the Repository
git clone https://github.com/yourusername/password-integrity-checker.git
cd password-integrity-checker
2. Install Dependencies
pip install argon2-cffi
Usage

Run the program:

python password_checker.py

Example:

WELCOME TO PASSWORD INTEGRITY CHECKER
Do you want to check your password's integrity
Type 1 to Continue and 0 to Close the program: 1

Enter Your Password: MySecure@123

Your password score is : 5 / 5
Strong password strength

Password is hashed using Argon2id
$argon2id$v=19$m=65536,t=3,p=4$...

Your session token is : 4f7a2c5f1e8b...
Enter your session token:
Token verified successfully

Password securely wiped from memory
Technologies Used
Python 3
Argon2id (argon2-cffi)
HMAC (hmac.compare_digest)
Cryptographically secure token generation (secrets)
Security Concepts Demonstrated
Password validation
Password strength assessment
Common password filtering
Secure password hashing (Argon2id)
Timing attack mitigation
Secure random token generation
Basic memory sanitization
Project Purpose

This project was developed as a cybersecurity learning exercise to demonstrate practical implementation of:

Authentication security principles
Secure password handling
Password hashing techniques
Defensive coding practices
Basic cryptographic protections

It is intended for educational purposes and can serve as a foundation for more advanced authentication systems.
