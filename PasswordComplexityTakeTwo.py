#this is a nightmare. it is for mr barrow
#importing
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase, punctuation
import random 
# This bit tries to use python's getch library to make the asterisks show when you are typing, however if you are on an unsupported platform, then it should import getpass() instead for support, you just don't get the asterisks
try:
    from getch import getch
    def getpass(prompt):
        """Replacement for getpass.getpass() which prints asterisks for each character typed"""
        print(prompt, end='', flush=True)
        buf = b''
        while True:
            ch = getch().encode()
            if ch in {b'\n', b'\r', b'\r\n'}:
                print('')
                break
            elif ch == b'\x03': # Ctrl+C
                # raise KeyboardInterrupt
                return ''
            elif ch in {b'\x08', b'\x7f'}: # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{"*" * len(buf)}', end='', flush=True)
            else:
                buf += ch
                print('*', end='', flush=True)

        return buf.decode(encoding='utf-8')
except ImportError:
    from getpass import getpass


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
    password = getpass("Please enter a password (minimum 15 characters): ")
    password2 = getpass("Please confirm the password")

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

## lets see if i can hash the password and store it to a text file

key = random.randint(1115792089237316195423570985008687907853269984665640564039457584007913129639936)