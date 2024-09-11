#this program is about passowrd complexity. its for mr barrow
#importing
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase, punctuation
import getpass


# testing what getpass does
shrersh = getpass.getpass()
print(shrersh)
# Define a function to check password complexity
def checks(password):
    hasupper = False
    haslower = False
    hasspecial = False
    hasnumber = False

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

    return hasupper, haslower, hasspecial, hasnumber

# Prompt user to input their password
password = input("Please input your password: ")

# Continue prompting the user until the password meets the complexity requirements
while len(password) < 15:
    hasupper, haslower, hasspecial, hasnumber = checks(password)
    if not (hasupper and haslower and hasspecial and hasnumber):
        print("Password is not complex enough. Please make sure it contains: \n at least one upper case character, \n at least one lower case character, \n at least one number, \n at least one special character, \n and is at least fifteen characters in length.")
        password = input("Please input your password: ")
    else:
        break

print("Password set successfully")
