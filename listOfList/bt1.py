
ds = []
n = int(input("nhập kích thước :"))
for i in range(n):
    a = []
    for j in range(2):
        x = int(input(f"{j+1} nhập : "))
        a.append(x)
    ds.append(a)
print(ds)