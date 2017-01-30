def selection_sort(data=list()):
    n = len(data)
    if n < 2:
        return data

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            temp = data[min_index]
            data[min_index] = data[i]
            data[i] = temp
    return data


def insertion_sort(data=list()):
    n = len(data)
    if n < 2:
        return data

    for i in range(1, n):
        val = data[i]
        j = i - 1
        while j >= 0 and val < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = val
    return data


def bubble_sort(data=list()):
    n = len(data)
    if n < 2:
        return data

    for i in range(n - 1):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data
