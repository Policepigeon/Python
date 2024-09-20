#another procedural program
num = 0
def numgetter():
    num = int(input("what is your number"))
    return num


num1 = numgetter()
num2 = numgetter()
num3 = numgetter()

if (num1>=num2) and (num1 >= num3):
    largest = num1
elif (num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest = num3

print("largest is:", largest)