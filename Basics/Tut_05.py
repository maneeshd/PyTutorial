"""""""""""""""""""""""""""""
"  Created On: 12-Aug-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

groceries = {'lotion', 'beer', 'museli', 'milk', 'eggs', 'cunt', 'cunt'}  # set

print(type(groceries))

dict = {'tony': 'stark', 'emma': 'watson', 'gaandu': 'raja'}
print(dict['tony'])

dict['koja'] = str(1)
for k, v in dict.items():
    print(k + ":" + v)

data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lft = data[:4]

rgt = []
rgt.extend(data[5:])
print(lft)
print(rgt)

data_squared = [num ** 2 for num in data]  # List Comprehension
print(data_squared)

var = (1, 2, 3, 4, 5)
print(type(var))

print(dict)
del dict['koja']
print(dict)
