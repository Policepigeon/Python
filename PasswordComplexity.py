#this program is about passowrd complexity. its for mr barrow

#defining variables
hasupper = False
haslower = False
hasspecial = False
lengthcheck = False
hasnumber = False

#this bit gets the password and checks that it is longer than fifteen characters long

password = "short"
uppers = []
lowers = []

# i have to make a list for this password to get the upper/lower

password = input("Please enter your desired password:")

#this here checks the ascii code of the letter and adds it lowers = [l for l in password if l.islower()]sto a list if the number is between the ascii code ranges for a upper/lower case letter

uppers = [l for l in password if ord(l) >= 65 and ord(l) <= 90] 
lowers = [l for l in password if ord(l) >= 97 and ord(l) <= 122]
specials = [l for l in password if ord(l) >= 33 and ord(l) <= 47 or ord(l) >= 58 and ord(l) <= 64]
numbers = [l for l in password if ord(l) >= 48 and ord(l) <= 57]
while int(len(password)) < 15 or len(uppers) >= 1 or len(lowers) >= 1 or len(specials) >= 1 or len(numbers) >= 1:
    password = input("Password invalid, please remember that your password must have: \n at least one uppercase, \n at least one lowercase, \n at least one special character, \n at least one number, \n and be at least fifteen characters in length. \n Enter an amended password:")
    uppers = [l for l in password if l.isupper()]
    lowers = [l for l in password if l.islower()]
    #I cannot check for special characters efficiently using this method without using either a egregiously long function or importing string
    print(uppers)
    print(lowers)

#setting the variables to true
hasupper = True
haslower = True

    



