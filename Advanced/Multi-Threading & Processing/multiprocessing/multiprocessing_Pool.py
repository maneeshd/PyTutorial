"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 15-Feb-17
"""
from multiprocessing import Pool


def square_primes(n):
    return n ** 2


def main():
    pool = Pool(4)
    primes = [number for number in range(2, 100) if all(number % x != 0 for x in range(2, int(number ** 0.5) + 1))]
    print("Primes:", primes)
    results = pool.map(square_primes, primes)
    pool.close()
    pool.join()
    print("Squared Primes:", results)


if __name__ == '__main__':
    main()



