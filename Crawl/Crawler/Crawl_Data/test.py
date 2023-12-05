import math
from _csv import writer

import pandas as pd

'''

d = ['Hồ Chí Minh', 'Hà NỘi', 'đà nẵng 123', '12']
col = ['1', '2', '4', '3']
df = pd.DataFrame(columns=col)

df1 = pd.DataFrame(columns=col)
df1.loc[1] = col
df1.loc[2] = d

#df.to_csv("test.csv", index=True, encoding='utf-8-sig')
#df1.to_csv('test.csv', mode='a', header=False, encoding='utf-8-sig')
with open('test.csv', 'a', encoding='utf-8-sig') as f:
    w = writer(f)
    w.writerow(d)

print(df)
'''
'''
#61
n = -1
i = 0
sum = 0
while n != 0:
    n = float(input("Enter: "))
    i = i + 1
    while n == 0 and i == 1:
        n = float(input("ERROR! Enter: "))
    sum = sum + n
print("Average: " + str(sum/(i-1)))


#75
m,n = -1, -1
while n <= 0:
    n = int(input("Enter n: "))
while m <= 0:
    m = int(input("Enter m: "))
d = m
if m > n:
    d = n
while n % d !=0 or m % d != 0:
    d = d - 1
print("The greatest common divisor of "+ str(m) + " and " +str(n) + " is "+ str(d))

'''
#64
price = "0"
sum = 0
while price.isspace()!= True and price   :
    price = input("Enter: ")
    if price.isspace()!= True and price :
        sum += int(price)
print("Total: "+ str(sum))
print(str(int(sum/5)) +" nikel and " +str(sum%5)+ " pennies")




























