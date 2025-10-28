ds = []
n = int(input("nhập độ dài : "))
for i in range(n):
    a = []
    for j in range(n):
        x = int(input(f"{j+1} : nhập value : "))
        a.append(x)
    ds.append(a)

for i in ds:
    print(i,"\n")