"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 13-03-2017
"""
import numpy as np

a = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], dtype=np.int64)
b = np.arange(11, 21).reshape(2, 5)
print(a)
print(a.shape)
print(a.dtype)
print()
print(b)
print(b.shape)
print(b.dtype)
print()
print(a + b)
print()
print(a - b)
print()
print(a * b)
print()
print(a / b)
print()
print(a < 8)
print()
print(a * np.cos(0))
print()
print(b + np.sin(45))
print()
c = np.array([[21, 22, 23, 24], [25, 26, 27, 28]], dtype=np.complex)
print(c)
