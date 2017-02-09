"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""
from pprint import pprint


lt = filter(lambda x: all(x % y != 0 for y in range(2, int(x ** 0.5) + 1)), range(2, 100))
print(list(lt))

l1 = ['Senor Pablo Escobar', 'Jon Snow', 'Maneesh', 'Jesse Pinkman', 'You']
l2 = ['Plata o Plomo', 'You know nothing', 'Fuck Off cnllnn', 'Bitch!!']

s = map(lambda x, y: x + ": " + y, l1, l2)
pprint(list(s))
