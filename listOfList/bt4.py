ds = []
n = int(input("nhập độ dài : "))
for i in range(n):
    a = []
    for j in range(n):
        x = int(input(f"{j+1} : nhập value : "))
        a.append(x)
    ds.append(a)


for i in range(n):
    total = 0
    for j in range(n):
        total += ds[j][i]
    print(total)