#this is a nightmare. it is for mr barrow
#importing
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase, punctuation
import getpass

# Define a function to check password complexity
def checks(password, password2):
    hasupper = any(char in ascii_uppercase for char in password)
    haslower = any(char in ascii_lowercase for char in password)
    hasspecial = any(char in punctuation for char in password)
    hasnumber = any(char in digits for char in password)
    confirmed = (password == password2)
    
    # Print status of each check
    if hasspecial:
        print("Special characters: OK")
    if haslower:
        print("Lowercase letters: OK")
    if hasupper:
        print("Uppercase letters: OK")
    if hasnumber:
        print("Numbers: OK")
    if confirmed:
        print("Passwords: OK")
    else:
        print("Passwords do not match")
    
    return hasupper, haslower, hasspecial, hasnumber, confirmed

# Prompt user to input their password
while True:
    password = getpass.getpass("Please enter a password (minimum 15 characters): ")
    password2 = getpass.getpass("Please confirm the password")

    # Check password criteria
    hasupper, haslower, hasspecial, hasnumber, confirmed = checks(password, password2)

    # Length check and complexity check
    if len(password) < 15:
        print("Password is too short. It must be at least 15 characters long.")
    elif not (hasupper and haslower and hasspecial and hasnumber and confirmed):
        print("Password does not meet all the complexity requirements.")
        print("Please make sure it contains: \n - at least one upper case character, \n - at least one lower case character, \n - at least one number, \n - at least one special character.")
    else:
        break

print("Password set successfully")
