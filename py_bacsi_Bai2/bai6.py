"""
bai 6 + 7:
ax^ + bx + c = 0 (a,b != 0)
"""

import math

a = int(input("nhap a : "))
b = int(input("nhap b : "))
c = int(input("nhap c : "))

denta = pow(b,2) - 4 * a * c
if(denta >  0):
    print(f"phuong trinh co 2 nghiem : x1 = {(-b + math.sqrt(denta)) / (2 * a)} , x2 = {(-b - math.sqrt(denta)) / (2 * a)}")
elif denta == 0:
    print(f"phuong trinh co nghiem kep : x = {(-b)/(2*a)}")
else:
    print("phuong trinh vo nghiem")