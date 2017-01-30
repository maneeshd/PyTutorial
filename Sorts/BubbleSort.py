def bubble_sort(data=list()):
    n = len(data)
    if n < 2:
        print("Sorted:  " + str(data))
        return

    print("Un-Sorted Data:  " + str(data))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
        print("Iteration[%d]:  %s" % (i + 1, str(data)))
    print("Sorted Data:  " + str(data))
    return


bubble_sort([5, 6, 2, 4, 1, 3])
