"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17
"""
from multiprocessing.dummy import Pool
from pprint import pprint


def square_number(n):
    return n ** 2


def main():
    pool = Pool(4)
    numbers = [number for number in range(1, 50)]
    results = pool.map(square_number, numbers)
    pool.close()
    pool.join()
    pprint(results)


if __name__ == '__main__':
    main()
