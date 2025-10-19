ds = []
for i in range (1000,3001):
    iStr = str(i)
    # for j in range (len(iStr)):
    #     if int(iStr[j]) %2 ==0 :
    #         ds.append(iStr[j])
    if (int(iStr[0]) % 2 == 0) and (int(iStr[1]) % 2 == 0) and (int(iStr[2]) % 2 == 0) and (int(iStr[3]) % 2 == 0):
        ds.append(iStr)
print("cac so chan : \n",','.join(ds));