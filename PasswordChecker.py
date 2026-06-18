import hmac
from argon2 import PasswordHasher
import secrets

print("WELCOME TO PASSWORD INTEGRITY CHECKER")
print("Do you want to check your password's integrity")
decision = int(input("Type 1 to Continue and 0 to Close the program: "))

if decision == 1:
    password_input = input("Enter Your Password: ")
    password = bytearray(password_input.encode())  #Convert to bytearray
else:
    exit()

# Phase 1: Gatekeeper

# 1.Length Check
if len(password_input) < 8:
    print("Error: The password must be at least 8 characters long.")
    exit()

# 2.Common Password Check
common_passwords = [
    "password", "password123", "12345678", "123456789", "1234567890",
    "qwerty123", "welcome1", "welcome123", "letmein1", "admin123",
    "administrator", "passw0rd", "iloveyou", "football", "baseball",
    "sunshine", "princess", "trustno1", "12341234", "9876543210",
    "abcd1234", "qwertyui", "asdfghjk", "zxcvbnm1", "password1"
]
# Need to encode for comparison with bytearray
if password_input.lower() in common_passwords:
    print("Error: This password is too common! Rejected by the Gatekeeper.")
    exit()

# 3.Password Scoring
score = 0
has_lower = False
has_upper = False   
has_digit = False
has_symbol = False

for byte in password:
    char = chr(byte)  # Convert byte back to character
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    else:
        has_symbol = True

if has_digit:  
    score += 1
if has_lower:  
    score += 1
if has_upper:  
    score += 1
if has_symbol: 
    score += 1
if len(password_input) >= 8: 
    score += 1

print(f"\nYour password score is : {score} / 5")

# Password Recommendation
if not has_lower:  print(" Use at least one lowercase letter")
if not has_digit:  print(" Use at least one number")
if not has_symbol: print(" Use at least one special character")
if not has_upper:  print(" Use at least one uppercase letter")

# 4.Weak Password Block
if score <= 2:
    print("Weak password Found,Rejected by the Gatekeeper before hashing")
    exit()
elif score <= 4:
    print("Medium password strength")
else:
    print("Strong password strength")

# PHASE 2 : Hashing (Argon2id)
ph = PasswordHasher()
hashed_password = ph.hash(password_input)  

print("\nPassword is hashed using Argon2id")
print(hashed_password)

# PHASE 3: Timing attack solution
session_token = secrets.token_hex(16)
print(f"Your session token is : {session_token}")
user_token = input("Enter your session token: ")

if hmac.compare_digest(session_token, user_token):
    print("Token verified successfully")
else:
    print("Invalid token try again")


# SECURE CLEANUP: Overwrite password in RAM with zeros
password[:] = b'\x00' * len(password)  
del password
del password_input

print("\n Password securely wiped from memory")
