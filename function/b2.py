ds = []
for i in range (270,650):
    if i % 7 == 0 and i % 5 != 0 :
        ds.append(i)

print(ds)