"""
tính tổng chuỗi hình học
"""
sum = 0
a = 1
r = 1/2
giaTri = a
n = int(input("nhap n"))
for i in range (n):
    sum += giaTri
    giaTri*= r
print(sum)