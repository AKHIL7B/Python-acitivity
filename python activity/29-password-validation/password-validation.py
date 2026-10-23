#this program is for password validation
password = input("Enter your password(1-8 characters): ")
k = len(password)
lower = 0
upper = 0
digit = 0
special = 0
for i in password:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1
    
failed = 0

# Rule 1: minimum length
if k < 8:
    print("Rule failed: password must be at least 8 characters long")
    failed += 1

# Rules 2-5: character categories (using your counters)
if lower == 0:
    print("Rule failed: needs at least one lowercase letter")
    failed += 1
if upper == 0:
    print("Rule failed: needs at least one uppercase letter")
    failed += 1
if digit == 0:
    print("Rule failed: needs at least one digit")
    failed += 1
if special == 0:
    print("Rule failed: needs at least one special character")
    failed += 1

# Rule 6: no 3 identical characters in a row
for i in range(k - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        print("Rule failed: the same character appears 3 times in a row")
        failed += 1
        break

# Rule 7: banned words (checked in lowercase)
banned = ["password", "1234", "qwerty"]
for word in banned:
    if word in password.lower():
        print("Rule failed: contains the banned word '" + word + "'")
        failed += 1

# Final result
if failed == 0:
    print("Valid password")
else:
    print("Invalid password,", failed, "rule(s) failed")
print(f"Password length: {k}, Lowercase: {lower}, Uppercase: {upper}, Digits: {digit}, Special characters: {special}")