#this program is about passowrd complexity. its for mr barrow
#import
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase


#defining variables
hasupper = False
haslower = False
hasspecial = False
lengthcheck = False
hasnumber = False

#making the password
password = input("please input your password")

#these check the string library for whether it has an intersection of the desired character set and the character set in the password
if set(password).difference(ascii_letters + digits):
    hasspecial = True
else:
    hasspecial = False

if set(password).intersection(ascii_lowercase):
    haslower = True
else:
    haslower = False

if set(password).intersection(ascii_uppercase):
    hasupper = True
else:
    hasupper = False

if set(password),intersection(digits):
    hasnumber = True
else:
    hasnumber = False

while len(password) < 15 or hasupper = False or haslower = False or hasspecial = false or hasnumber = false:
    password = input("please input your password")

    #these check the string library for whether it has an intersection of the desired character set and the character set in the password
    if set(password).difference(ascii_letters + digits):
        hasspecial = True
    else:
        hasspecial = False

    if set(password).intersection(ascii_lowercase):
        haslower = True
    else:
        haslower = False

    if set(password).intersection(ascii_uppercase):
        hasupper = True
    else:
        hasupper = False

    if set(password),intersection(digits):
        hasnumber = True
    else:
        hasnumber = False