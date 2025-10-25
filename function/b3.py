ds = []
for i in range(1000,3000):
    iStr = str(i)
    if ((int(iStr[0])%2==0) and (int(iStr[1])%2==0)  and (int(iStr[2])%2==0) and (int(iStr[3])%2==0)):
        ds.append(iStr)

print(','.join(ds))