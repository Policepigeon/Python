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
if set(password).difference(ascii_letters + diigts):
    print("hasspecial")
else:
    print("hasntspecials")
    