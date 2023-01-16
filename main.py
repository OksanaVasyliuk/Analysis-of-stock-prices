import math

data = input("numbers: ")
list_of_numbers = data.split(" ")
list = [int(number) for number in list_of_numbers]

p = list[0]
a = list[1]
b = list[2]
c = list[3]
d = list[4]
n = list[5]

prices = []
for i in range(1,n+1):
    price=p*(math.sin(a*i+b)+math.cos(c*i+d)+2)
    prices.append(price)

list_result = []
for price in prices:
    for i in range(0,n):
        if prices.index(price)<=prices.index(prices[i]):
            difference = price - prices[i]
            list_result.append(difference)

result = round(max(list_result),6)
print (result)