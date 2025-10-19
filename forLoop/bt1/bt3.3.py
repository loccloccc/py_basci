"""
tính tổng số tự nhiên của n , nhập từ bàn phím
"""

n = int(input("nhập n :"))
sum = 0
for i in range (n):
    sum += i * i
print(sum);