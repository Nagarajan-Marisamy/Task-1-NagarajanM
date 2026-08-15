
# 🔐 Password Integrity Checker

A Python-based **Password Integrity Checker** that evaluates password strength, blocks weak/common passwords, securely hashes passwords using **Argon2id**, protects token verification against timing attacks, and securely wipes sensitive password data from memory after use.

---

## 📌 Features

### Phase 1 – Password Validation (Gatekeeper)

The program performs the following security checks before accepting a password:

- Minimum password length validation (at least 8 characters)
- Detection of commonly used passwords
- Password complexity analysis
- Password strength scoring

The score is calculated based on:

- Presence of lowercase letters
- Presence of uppercase letters
- Presence of digits
- Presence of special characters
- Meeting the minimum length requirement

Password strength levels:

| Score | Strength |
|---------|----------|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

Weak passwords are rejected before proceeding to the hashing stage.

---

### Phase 2 – Secure Password Hashing

The program uses **Argon2id** to hash passwords.

Argon2id is considered one of the most secure password hashing algorithms because it:

- Resists brute-force attacks
- Uses memory-hard computations
- Automatically generates a unique salt
- Is recommended by modern security standards

The original password is never stored after hashing.

---

### Phase 3 – Timing Attack Protection

The program generates a cryptographically secure session token using Python's `secrets` module.

Token verification is performed using:

```python
hmac.compare_digest()
```

This method helps prevent timing attacks by ensuring comparisons take a constant amount of time regardless of how much of the token matches.

---

### Secure Memory Cleanup

After all operations are completed, the password stored in memory is overwritten with zeros and deleted.

This helps reduce the possibility of sensitive data remaining in RAM after program execution.

---

## 🛠 Technologies Used

- Python 3
- Argon2id (`argon2-cffi`)
- HMAC (`hmac`)
- Secrets (`secrets`)

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/Nagarajan-Marisamy/Password-Integrity-Checker.git
```

### Navigate to the Project Folder

```bash
cd password-integrity-checker
```

### Install Required Dependency

```bash
pip install argon2-cffi
```

---

## ▶️ Running the Program

```bash
python password_checker.py
```

---

## Example Execution

```text
WELCOME TO PASSWORD INTEGRITY CHECKER
Do you want to check your password's integrity
Type 1 to Continue and 0 to Close the program: 1

Enter Your Password: MySecure@123

Your password score is : 5 / 5
Strong password strength

Password is hashed using Argon2id
$argon2id$v=19$m=65536,t=3,p=4$...

Your session token is : 5e6a9b7c2d8f4e1a9c3d7f0b1e2a4c6d

Enter your session token:
Token verified successfully

Password securely wiped from memory
```

---

## 🔒 Security Concepts Demonstrated

This project demonstrates several important cybersecurity concepts:

- Password strength validation
- Common password blacklisting
- Secure password hashing
- Cryptographic token generation
- Timing attack mitigation
- Secure memory handling

---

## 📚 Learning Objectives

The goal of this project is to understand and practice:

- Secure password management
- Cryptographic hashing techniques
- Authentication security
- Python security programming
- Defensive coding practices

---

## ⚠️ Disclaimer

This project was created for educational and learning purposes. It demonstrates fundamental security concepts but should not be considered a complete authentication system for production environments without additional security controls.

---

