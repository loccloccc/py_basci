"""
    các phép toán cơ bản : yêu cầu phải cùng độ dài
    phép cộng thì + như bth
    phép nhân dùng .dot()
"""
import numpy as np
A = np.array([[2,4],[5,6]])
B = np.array([[1,4],[4,6]])
C = A + B
D = A.dot(B)
print(C)
print(D)