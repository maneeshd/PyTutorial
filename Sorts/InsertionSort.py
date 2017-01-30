def insertion_sort(data=list()):
    n = len(data)
    if n < 2:
        print("Sorted:  " + str(data))
        return

    print("Un-Sorted Data:  " + str(data))
    for i in range(1, n):
        val = data[i]
        j = i - 1
        while j >= 0 and val < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = val
        print("Iteration[%d]:  %s" % (i, str(data)))
    print("Sorted Data:  " + str(data))
    return


insertion_sort([5, 1, 6, 2, 4, 3])
