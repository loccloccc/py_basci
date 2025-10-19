
def sumNumber():
    sum = 0
    count = 0
    while True:
            n = float(input(" nhap so :"))
            if n > 3 or n < -3:
                print(f"so {n} khong hop le , moi ban nhap lai :")
                break;
            else:
                sum += n
                count += 1
                if count == 4: return sum
print(sumNumber())