a = [2,19,30,45,100,101,104,103,200,301,257]
b = []

for pt in a:
    s = 0
    for i in range (1,pt):
        if pt%i==0:
            s+=1
    if s==1:
        b=b+[pt]

print(b)