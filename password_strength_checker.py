# ask user to enter a password
password = input("Enter a password: ")

# this will track how strong the password is
strength = 0

# check if password length is at least 8 characters
if len(password) >= 8:
    strength += 1

# check if password has at least one uppercase letter
if any(char.isupper() for char in password):
    strength += 1

# check if password has at least one number
if any(char.isdigit() for char in password):
    strength += 1

# check if password has at least one special character
if any(char in "!@#$%^&*()" for char in password):
    strength += 1

# determine overall strength based on score
if strength == 4:
    print("Strong password")
elif strength == 3:
    print("Medium password")
else:
    print("Weak password")

print("Password strength score:", strength, "/4")