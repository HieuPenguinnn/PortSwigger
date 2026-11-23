import os

path = os.path.join(os.path.dirname(__file__), "passwords.txt")

with open(path, "r", encoding="utf-8") as f:
    passwords = [line.strip() for line in f if line.strip()]

print("[")
for password in passwords:
    print(f'    "{password}",')
print("]")