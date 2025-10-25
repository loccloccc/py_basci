tp_1 = (1,2,3,4,5,6,7,8,9,10)
ds = list()
for i in tp_1:
    if (i % 2 != 0 ):
        ds.append(i)

tp_2 = tuple(ds)
print(f"{tp_2}")