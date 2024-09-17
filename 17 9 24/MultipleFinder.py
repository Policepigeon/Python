#this is a program to find the tihngs in a list diivsible by 7

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % 7 == 0:
           print(i)

num = 320

print_factors(num)
