#this program is about passowrd complexity. its for mr barrow
#importing
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase, punctuation
import getpass


# Define a function to check password complexity
def checks(password, password2):
    hasupper = False
    haslower = False
    hasspecial = False
    hasnumber = False
    confirmed = False

    # Check if the password has any special characters
    if set(password).difference(ascii_letters + digits) & set(punctuation):
        hasspecial = True

    # Check if the password has any lowercase letters
    if set(password).intersection(ascii_lowercase):
        haslower = True

    # Check if the password has any uppercase letters
    if set(password).intersection(ascii_uppercase):
        hasupper = True

    # Check if the password has any digits
    if set(password).intersection(digits):
        hasnumber = True

    if password == password2:
        confirmed = True
    else:
        print("passwords are not the same")
    return hasupper, haslower, hasspecial, hasnumber, confirmed

# Prompt user to input their password
password = getpass.getpass("Please enter a password")
password2 = getpass.getpass("Please confirm the password")
# Continue prompting the user until the password meets the complexity requirements
while len(password) < 15:
    hasupper, haslower, hasspecial, hasnumber, confirmed = checks(password, password2)
    if not (hasupper and haslower and hasspecial and hasnumber):
        print("Password is not complex enough. Please make sure it contains: \n at least one upper case character, \n at least one lower case character, \n at least one number, \n at least one special character, \n and is at least fifteen characters in length.")
        password = getpass.getpass("Please enter an amended password")
        password2 = getpass.getpass("Please confirm the password")

    else:
        break

print("Password set successfully")
