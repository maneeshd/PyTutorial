""" 
@author: Maneesh D 
@email: maneeshd77@gmail.com 
""" 


from multiprocessing import Process, Queue


def is_prime(num):
    limit = int(num ** 0.5) + 1
    for i in range(2, limit):
        if num % i == 0:
            return False
    return True


def sum_primes(start, end, q):
    total = 0
    for num in range(start, end+1):
        if is_prime(num):
            total += num
    q.put(total)


def main():
    q = Queue()

    p1 = Process(target=sum_primes, args=[2, 500000, q],)
    p2 = Process(target=sum_primes, args=[500001, 1000000, q],)
    p3 = Process(target=sum_primes, args=[1000001, 1500000, q], )
    p4 = Process(target=sum_primes, args=[1500001, 2000000, q], )

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    total = q.get() + q.get() + q.get() + q.get()
    print("The Sum of prime numbers till 2 million is %d" % total)


if __name__ == '__main__':
    from timeit import Timer
    t = Timer(stmt="main()", setup="from primes_multi_processing import main")
    print("Execution Time= %.3f Seconds" % t.timeit(number=1))
