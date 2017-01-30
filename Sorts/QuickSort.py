def qsort(data, first, last):
    if first < last:
        pindex = partition(data, first, last)
        qsort(data, first, pindex - 1)
        qsort(data, pindex + 1, last)
    return data


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
