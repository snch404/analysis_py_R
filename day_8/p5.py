import re

pwd = input("Enter a new password: ")

errors = []

if len(pwd) < 8:
    errors.append("Password must be at least 8 characters long.")

if re.search(r"\s", pwd):
    errors.append("Password must not contain spaces.")

if not re.search(r"[a-z]", pwd):
    errors.append("Password must contain at least one lowercase letter.")

if not re.search(r"[A-Z]", pwd):
    errors.append("Password must contain at least one uppercase letter.")

if not re.search(r"[0-9]", pwd):
    errors.append("Password must contain at least one numeral (0–9).")

if not re.search(r"[^A-Za-z0-9]", pwd):
    errors.append("Password must contain at least one special character (e.g. @, #, $, %).")

if not errors:
    print("Password is valid.")
else:
    print("Password is invalid due to the following reason(s):")
    for e in errors:
        print("-", e)
