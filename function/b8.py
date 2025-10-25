ds = (1,2,3,4,5,6,7,8,9,10)

binh_phuong = list(map(lambda x : x ** 2,ds))
ds_2 = tuple(binh_phuong)
print(f"{ds_2}")