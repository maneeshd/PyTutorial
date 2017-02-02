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


def main(unsorted_data):
    print("\nSorting in progress...Please Wait...")
    qsort(unsorted_data, 0, len(unsorted_data) - 1)
    print("\nSorting Complete...\n")
    print("***************************************")


if __name__ == '__main__':
    print("-" * len("QuickSort of 1 million random integers:"))
    print("QuickSort of 1 million random integers:")
    print("-" * len("QuickSort of 1 million random integers:"))
    from timeit import Timer
    print("Populating unsorted datalist with 1 million random integers...Please Wait...")
    t = Timer(stmt="main([n-randint(-77, 78) for n in range(1000000)])", setup="from QuickSort import main\n"
                                                                               "from random import randint")
    print("\nUnsorted datalist Polulated....")
    print("* Execution Time = %.3f Seconds      *" % t.timeit(number=1))
    print("***************************************")
