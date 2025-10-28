"""
cắt mảng 1 chiều
"""
import numpy as np
A = np.array([1,2,3,4,5,6,7,8,9,10])
"""
1 ,cắt bỏ [start = index :end = index - 1]
2 ,cắt bỏ index phần tử cuối dãy [:-index]
3 ,cắt bỏ từ index [index:] 
4 ,đảo ngược dãy [::-1]
5 , lấy toàn bộ dãy [:]
"""
print(A[0:5])
print(A[:-5])
print(A[5:])
print(A[::-1])
print(A[:])

