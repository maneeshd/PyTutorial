"""""""""""""""""""""""""""""
"  Created On: 07-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

lst = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5 + 1)))]
print(lst)

lst2 = [x for x in range(0, 101) if x % 2 == 0]
print(lst2)
