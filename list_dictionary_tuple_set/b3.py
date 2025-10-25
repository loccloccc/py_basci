ds = []
n = int(input("nhap do dai list :"))
for i in range(n):
    x = int(input("nhập value :"))
    ds.append(x)

print(min(ds))
print(max(ds))