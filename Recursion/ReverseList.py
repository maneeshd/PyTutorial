import time


def reverse_list(q):
    if len(q) == 0:
        return []
    elif len(q) == 1:
        return q
    else:
        return reverse_list(q[1:]) + [q[0]]


lst1 = []
lst2 = [1]
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using user defined function is slower
start = time.clock()
print(reverse_list(lst1), end=", ")
print(reverse_list(lst2), end=", ")
print(reverse_list(lst3))
print("Time Taken= ", (time.clock() - start) * 100000)

# Always use built-in methods...fast af
start = time.clock()
print(list(reversed(lst1)), end=", ")
print(list(reversed(lst2)), end=", ")
print(list(reversed(lst3)))
print("Time Taken= ", (time.clock() - start) * 100000)

# Very Fast...fastest of the three
start = time.clock()
print(lst1[::-1], end=", ")
print(lst2[::-1], end=", ")
print(lst3[::-1])
print("Time Taken= ", (time.clock() - start) * 100000)
