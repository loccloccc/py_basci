Li = []
items = [x for x in input("nhap so nhi phan : ").split(',')]
for i in items:
    i2 = int(i)
    if not i2%5 :
        Li.append(i);
print(Li);