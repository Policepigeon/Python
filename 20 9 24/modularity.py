#this is  aprogram that should use procedures

#function to get the value of pi r
def pir(radius):
    pir = 3.14159 * radius
    return pir

#now calculate radius

radius = float(input("please input radius"))
pir(radius)
area = pir * radius
circumference = pir * 2
print("area:", area)
print("curcumference", circumference)