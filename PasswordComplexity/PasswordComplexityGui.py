#this is a nightmare. it is for mr barrow
#importing
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase, punctuation
import random 
import tkinter
#pip install pwinput MUST BE USED HERE
import pwinput


m = tkinter.Tk()
'''
widget = Entry(parent, show="*", width=15)'''
m.mainloop()



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
    password = pwinput.pwinput("Please enter a password (minimum 15 characters): ")
    password2 = pwinput.pwinput("Please confirm the password")

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

key = int(random.randint(0,1115792089237316195423570985008687907853269984665640564039457584007913129639936))
passlist = password.split()

#gets the ascii values for the characters stored in list passlist
asc = []
for j in passlist:
    asc.extend(ord(num) for num in j)
 
# printing result
print("The ascii list is : " + str(asc))

for i in range(len(asc)):
    asc[i]= int(asc[i]) * key
    print(asc[i])
    asc[i]= str(asc[i])

print(asc)
print(key)


asc_str = ', '.join(asc)


with open("passwordfile.txt", "a") as passwordfile:
    passwordfile.write(asc_str + "\n")

with open("keyfile.txt", "a") as keyfile:
    keyfile.write(str(key) + "\n")

keyfile.close
passwordfile.close