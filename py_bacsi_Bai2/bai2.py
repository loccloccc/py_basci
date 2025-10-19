totalPrice = int(input("nhap so tien khach phai tra :"))
if(totalPrice >=  20000000):
    pricePromotion = totalPrice * 0.04
    print(f"so tien khach phai tra la {totalPrice - pricePromotion} , khuyen mai la : {pricePromotion}");
elif totalPrice >= 50000000 :
    pricePromotion = totalPrice * 0.055
    print(f"so tien khach phai tra la {totalPrice - pricePromotion} , khuyen mai la : {pricePromotion}");
elif totalPrice >= 100000000 :
    pricePromotion = totalPrice * 0.065
    print(f"so tien khach phai tra la {totalPrice - pricePromotion} , khuyen mai la : {pricePromotion}");
else :
    print(f"so tien khach phai tra la : {totalPrice}")