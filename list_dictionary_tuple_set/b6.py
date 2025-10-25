ds = []
n = int(input("nhập độ dài list :"))
for i in range(n):
    x = int(input("nhập value :"))
    ds.append(x)

chan = []
le = []
for d in ds :
    if d % 2 == 0 : 
       chan.append(d)
    else :
        le.append(d)

print(chan)
print(le)