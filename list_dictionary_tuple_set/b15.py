t1  = []
t2 = []
for i in range(5):
    x = int(input("nhap t1 :"))
    y = int(input("nhap t2 :"))
    t1.append(x)
    t2.append(y)

t3 = t1 + t2
a = tuple(t3)
print(a)