# Task-1-NagarajanM
# Password Integrity Checker & Securer

A Python-based command-line tool designed to evaluate password strength, safely hash passwords using industry-standard algorithms, and protect sensitive data in memory. It acts as a multi-phase security gatekeeper to ensure users implement strong credentials.

## 🚀 Features

The application processes security in three distinct phases:

### 1. Phase 1: The Gatekeeper (Validation & Scoring)
* **Length Check:** Rejects any password shorter than 8 characters.
* **Common Password Blacklist:** Prevents the use of notoriously weak/common passwords (e.g., `password123`, `qwerty`).
* **Complexity Scoring:** Rates the password out of 5 based on length and character diversity (uppercase, lowercase, digits, and special characters).
* **Smart Feedback:** Provides actionable recommendations if your password is lacking a specific character type.
* **Weak Password Block:** Immediately terminates execution if the password scores 2 or less.

### 2. Phase 2: Secure Hashing
* Utilizes **Argon2id** (via the `argon2-cffi` library), the winner of the Password Hashing Competition, to safely hash the validated password against brute-force and GPU-accelerated attacks.

### 3. Phase 3: Post-Hash Protections
* **Timing Attack Mitigation:** Generates a secure session token via the `secrets` module and uses `hmac.compare_digest` to prevent timing side-channel attacks during verification.
* **Memory Zeroization:** Converts the password into a mutable `bytearray` and explicitly overwrites it with null bytes (`\x00`) in RAM before garbage collection to minimize the risk of memory dumping attacks.

---

## 🛠️ Prerequisites & Installation

Before running the script, ensure you have Python 3.x installed along with the `argon2-cffi` dependency.

1. Clone this repository:
   ```bash
   git clone [https://github.com/Nagarajan-Marisamy/Task-1-NagarajanM.git](https://github.com/Nagarajan-Marisamy/Task-1-NagarajanM.git)
   cd YOUR_REPO_NAME
Install the required dependencies:

Bash
pip install argon2-cffi
💻 Usage
Run the script from your terminal:

Bash
python password_checker.py
Example Walkthrough
Plaintext
WELCOME TO PASSWORD INTEGRITY CHECKER
Do you want to check your password's integrity
Type 1 to Continue and 0 to Close the program: 1
Enter Your Password: •••••••••••••

Your password score is : 5 / 5
Strong password strength

Password is hashed using Argon2id
$argon2id$v=19$m=65536,t=3,p=4$6F...

Your session token is : 4a2b9c...
Enter your session token: 4a2b9c...
Token verified successfully

Password securely wiped from memory
🔒 Security Architecture Notes
Why Argon2id? Unlike older algorithms like MD5 or SHA-256 (which are fast and optimized for hardware, making them vulnerable to GPU cracking), Argon2id is memory-hard, making it highly resistant to specialized ASIC/GPU password-cracking rigs.

Memory Hygiene: Simply running del password in Python doesn't immediately clear data from physical RAM due to how the garbage collector works. By modifying a mutable bytearray in-place (password[:] = b'\x00' * len(password)), this script actively destroys the plaintext footprint.
