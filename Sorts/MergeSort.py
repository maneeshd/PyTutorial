"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


def msort(data, first, last):
    if first == last:
        return data
    if first < last:
        mid = (first + last) // 2
        msort(data, first, mid)
        msort(data, mid + 1, last)
        return merge(data, first, mid, last)


def merge(data, low, mid, high):
    left_len = mid - low + 1
    right_len = high - mid
    lft = []
    rgt = []
    for i in range(0, left_len):
        lft.append(data[i + low])

    for i in range(0, right_len):
        rgt.append(data[mid + i + 1])

    i = 0
    j = 0
    k = low

    while i < len(lft) and j < len(rgt):
        if lft[i] < rgt[j]:
            data[k] = lft[i]
            i += 1
            k += 1
        else:
            data[k] = rgt[j]
            j += 1
            k += 1
    while i < len(lft):
        data[k] = lft[i]
        i += 1
        k += 1

    while j < len(rgt):
        data[k] = rgt[j]
        j += 1
        k += 1
    return data
