ds = []
n = int(input("nhap do dai list :"))
for i in range(n):
    x = int(input("nhập value :"))
    ds.append(x)

value = int(input("nhập value cần đếm :"))
print(ds.count(value))