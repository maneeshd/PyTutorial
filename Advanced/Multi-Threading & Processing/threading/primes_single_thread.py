"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


def is_prime(num):
    limit = int(num ** 0.5) + 1
    for i in range(2, limit):
        if num % i == 0:
            return False
    return True


def sum_primes(upto_num):
    total = 2
    for num in range(3, upto_num+1, 2):
        if is_prime(num):
            total += num
    return total


def main():
    print("The Sum of prime numbers till 2 million is %d" % sum_primes(2000000))


if __name__ == '__main__':
    from timeit import Timer
    t = Timer(stmt="main()", setup="from primes_single_thread import main")
    print("Execution Time= %.3f Seconds" % t.timeit(number=1))
