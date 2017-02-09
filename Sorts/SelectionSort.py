"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


def selection_sort(data=list()):
    n = len(data)
    if n < 2:
        print("Sorted:  " + str(data))
        return

    print("Un-Sorted Data:  " + str(data))
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[min_index] > data[j]:
                min_index = j
        if min_index != i:
            temp = data[min_index]
            data[min_index] = data[i]
            data[i] = temp
        print("Iteration[%d]:  %s" % (i + 1, str(data)))
    print("Sorted Data:  " + str(data))
    return


selection_sort([5, 1, 6, 2, 4, 3])
