import random
import string

def password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    password_length = int(input("Enter password length: "))
except ValueError:
    print("input not validated. Please enter a valid number.")
    exit()

print("Generated Password:",password(password_length))
