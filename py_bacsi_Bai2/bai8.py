"""
bai 8 : giai phuong trinh bac nhat 2 an
ax + by = m va dx + cy = n
"""
"""
Bài 8: Giải hệ phương trình bậc nhất 2 ẩn
ax + by = m
dx + cy = n
"""

a = int(input("nhập a: "))
b = int(input("nhập b: "))
m = int(input("nhập m: "))
d = int(input("nhập d: "))
c = int(input("nhập c: "))
n = int(input("nhập n: "))

# Tính các định thức
cramer = a * c - b * d       # Δ
cramerX = m * c - b * n      # Δx
cramerY = a * n - d * m      # Δy

if cramer != 0:
    x = cramerX / cramer
    y = cramerY / cramer
    print(f"Nghiệm duy nhất: (x, y) = ({x}, {y})")
else:
    if cramerX == 0 and cramerY == 0:
        print("Hệ có vô số nghiệm")
    else:
        print("Hệ vô nghiệm")
