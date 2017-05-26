"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""
from functools import reduce
from math import pow, pi

f = lambda x: pow(x, pi)

print(f(2))

squared = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(squared)

sum_of_squares = reduce(lambda x, y: x + y,  squared)
print(sum_of_squares)
print(pi)
