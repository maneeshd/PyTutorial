"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


def qsort(data_, first, last):
    """
        Iterative version of quick sort
    """
    temp_stack = list()
    temp_stack.append((first, last))

    # Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(data_, left, right)
        # If items in the left of the pivot push them to the stack
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        # If items in the right of the pivot push them to the stack
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))
    return data_


def partition(data, left, right):
    i = left + 1
    pivot = data[left]
    for j in range(left + 1, right + 1):
        if data[j] < pivot:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
            i += 1
    temp = data[i - 1]
    data[i - 1] = data[left]
    data[left] = temp
    return i - 1

print(qsort([9, 8, 7, 6, 5, 4, 3], 0, 6))
