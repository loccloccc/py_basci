    t = []
    for i in range (5):
        x = int(input("nhap x :"))
        t.append(x)

    a = tuple(t)
    value = int(input("nhap search :"))
    for i in a:
        if i == value :
            print("YES")
            break;
        else : print("NO")