n = int(input("nhập độ dài list :"))
ds = []
for i in range(n):
    x = int(input("nhập vaue :"))
    ds.append(x)

print("list khi đảo ngược là : " ,ds[::-1])