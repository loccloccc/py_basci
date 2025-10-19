choice =  int(input("hay chon 3 cach cua sau (1 , 2 , 3 ) de co the tim kho bau :"))
match choice:
    case 1: print("thang")
    case 2: print("thua")
    case 3: print("chet")
    case _: print(f"khong co lua chon {choice}")