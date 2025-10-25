ds = (1,2,3,4,5,6,7,8,9,10)
so_chan = list(filter(lambda x : x % 2 == 0, ds))
ds_2 = tuple(so_chan)
print(f"{ds_2}")