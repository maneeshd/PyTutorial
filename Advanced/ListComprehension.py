import math
import random
import time

# Ages divisible by 5
ages = [random.randint(1, 100) for i in range(100)]
print([age for age in ages if (age % 5 == 0)])

# Prime numbers less than 200
start = time.time()
primes = [num for num in range(2, 200) if all(num % i != 0 for i in range(2, int(math.sqrt(num) + 1)))]
print(primes)
print("%.3f" % (time.time() - start))

# Pythagorean Triplets
triplets = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if (x ** 2 + y ** 2 == z ** 2)]
print(triplets)
