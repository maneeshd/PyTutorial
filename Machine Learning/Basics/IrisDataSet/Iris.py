"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 02-Mar-17
"""
import numpy as np


arr = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], np.int32)
print(arr.shape)
print(arr)
print(arr.transpose())
print(arr.sum(axis=0))
print(arr.reshape((5, 2)))
print(arr.transpose())
print(arr.sum(axis=1))
