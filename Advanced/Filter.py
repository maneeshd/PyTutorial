import math

for num in filter(lambda x: all(x % y != 0 for y in range(2, int(math.sqrt(x)) + 1)), range(2, 500)):
    print(num)
