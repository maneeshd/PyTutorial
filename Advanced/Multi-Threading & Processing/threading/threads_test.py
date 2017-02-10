# thread_test.py

import random
import threading


def list_append(count, out_list):
    """
    Creates an empty list and then appends a
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in range(count):
        out_list.append(random.random())


def main():
    size = 10000000  # Number of random numbers to add
    threads = 2   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=list_append(size, out_list))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

    print("List processing complete.")
    return

if __name__ == '__main__':
    from timeit import Timer
    t = Timer("main()", "from __main__ import main")
    print("Execution Time= %.4f Seconds" % t.timeit(number=1))
