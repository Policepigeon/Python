#this program is about passowrd complexity. its for mr barrow

#this bit gets the password and checks that it is longer than fifteen characters long
password = input("what is your desired password?")
while int(len(password)) < 15:
    input("Password too short, please input a new password")

