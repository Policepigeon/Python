from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase, punctuation
import getpass

# Define a function to check password complexity
def check_complexity(password):
    hasupper = any(char in ascii_uppercase for char in password)
    haslower = any(char in ascii_lowercase for char in password)
    hasspecial = any(char in punctuation for char in password)
    hasnumber = any(char in digits for char in password)
    return hasupper, haslower, hasspecial, hasnumber

# Prompt user to input their password
password = getpass.getpass("Please enter a password (minimum 15 characters, including at least one upper case letter, one lower case letter, one number, and one special character): ")
password2 = getpass.getpass("Please confirm the password")

# Continue prompting the user until the password meets the complexity requirements
while len(password) < 15 or password != password2:
    if password != password2:
        print("Passwords do not match. Please try again.")
    else:
        hasupper, haslower, hasspecial, hasnumber = check_complexity(password)
        if not (hasupper and haslower and hasspecial and hasnumber):
            print("Password is not complex enough. Please make sure it contains: \n - at least one upper case character, \n - at least one lower case character, \n - at least one number, \n - at least one special character, \n - and is at least fifteen characters in length.")
        else:
            break

    # Prompt user to input their password again
    password = getpass.getpass("Please enter a password (minimum 15 characters, including at least one upper case letter, one lower case letter, one number, and one special character): ")
    password2 = getpass.getpass("Please confirm the password")

print("Password set successfully")
