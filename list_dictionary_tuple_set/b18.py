t = []
for i in range(5):
    x = int(input("nhập x : "))
    t.append(x)

a = tuple(t)
print(f"tổng tuple : {sum(a)}")