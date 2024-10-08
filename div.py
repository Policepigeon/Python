balance = 1000
interest = 2
years = 2
interest = float(interest)
interest = interest / 100
for i in range(1,years):
    balance = int(balance)
    interest = float(interest)
    balance = balance*(1+interest)
print(balance)