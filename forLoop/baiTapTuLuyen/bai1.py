"""
tính tổng chuỗi điều hòa :  1 + 1/2 .... + 1/n
"""
sum = 0
n = int(input("nhap n"))
for i in range (1,n+1):
    sum += 1/i
print(sum);