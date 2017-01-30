from functools import reduce

# Map
data = [11, 22, 33, 44, 55, 66, 77, 88, 99]
data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
data3 = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

result = map(lambda x: x + 1, data)
print(list(result))

result = list(map(lambda x, y, z: x + y + z, data, data2, data3))
print(result)

# Reduce
reduced = reduce(lambda x, y: x if (x < y) else y, result)
print(reduced)

print(reduce(lambda x, y: x + y, range(1, 1000001)))
