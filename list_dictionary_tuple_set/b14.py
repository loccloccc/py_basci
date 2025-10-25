t = []
for x in range(5):
    x = int(input("nhap"))
    t.append(x)

t.sort()
a = tuple(t)
print(a[-2])