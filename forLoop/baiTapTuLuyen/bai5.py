import math
n = int(input("nhap n :"))
sum = 0
for i in range (2,n+1):
    sum += 1/math.sqrt(i)

print(sum)