"""
tính tổng : 1/2 + 2/3 + .... + n / n+1
"""
n = int(input("nhập n :"))
sum = 0.00
for i in range (1,n+1):
    sum = float(float(i)/(i+1));
print(f"sum = {sum}")