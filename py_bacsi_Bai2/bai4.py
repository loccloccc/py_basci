year = int(input("nhap nam :"))
if(year%400==0) or ((year%4==0) and (year%100!=0)):
    print(f"nam {year} la nam nhuan")
else :
    print(f"nam {year} khong la nam nhuan")