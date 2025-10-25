t = []
for i in range(5):
    x = int(input("nhập x : "))
    t.append(x)
a = tuple(t)
count = 0
for i in a:
    if i%2==0: count+=1;

print(f"số chẵn : {count} , số lẻ {len(a) - count}")