#this program is about passowrd complexity. its for mr barrow


#defining variables
hasupper = False
haslower = False
hasspecial = False
lengthcheck = False
hasnumber = False

#this bit gets the password and checks that it is longer than fifteen characters long
password = input("what is your desired password?")
# i have to make a list for this password to get the upper/lower
uppers = [l for l in password if ord(l) >= 65 and ord(l) <= 90] 
lowers = [l for l in password if ord(l) >= 97 and ord(l) <= 122]
while int(len(password)) < 15:
    passoword = input("Password too short, please input a new password")
    uppers = [l for l in password if l.isupper()]
    lowers = [l for l in password if l.islower()]
    print(uppers)
    print(lowers)



