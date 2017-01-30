"""""""""""""""""""""""""""""
"  Created On: 26-Jul-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

import random
import time

from Sorts import QuickSort

start = time.clock()
data = list()
for i in range(0, 200):
    data.append(random.randint(1, 778))

print('Before Sorting: ', str(data))

data = QuickSort.qsort(data, 0, len(data) - 1)
# data = MergeSort.msort(data, 0, len(data) - 1)

print('After Sorting: ', str(data))
print('\nExecution Time = ', (time.clock() - start), ' Seconds')
