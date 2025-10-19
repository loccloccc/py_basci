"""
viết hàm tính và trả vể khoảng cách giữa 2 điểm :
- A(xA,yA,zA)
- B(xB,yB,zB)
trong không gian 3 chiều
"""
import math


def calculate_distance(a,b):
    return math.sqrt(pow(a[0]-b[0] , 2) + pow(a[1]-b[1] , 2) + pow(a[2]-b[2] , 2))



a = (1,3,6)
b = (2 , -1 , -3);

reslut =  calculate_distance(a,b)
print(reslut)