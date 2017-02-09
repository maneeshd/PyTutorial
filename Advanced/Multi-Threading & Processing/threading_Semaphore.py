"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17

Simple example for a Semaphore. The use of a bounded semaphore reduces the chance that a programming error
(which causes the semaphore to be released more than it's acquired) will go undetected.
Semaphores are also often used to guard resources with limited capacity, for example, a database server.
"""
from threading import Thread, BoundedSemaphore
from time import sleep, time, ctime

sema = BoundedSemaphore(value=2)    # Creates a Semaphore which gives max 2 threads the access at time.


def timer(name, delay, repeat):
    print("[INFO] " + name + " started")
    with sema:
        """
        with sema: is equivalent to:

        sema.acquire()
        try:
            # do stuff...
        finally:
            sema.release()
        """
        print("[INFO] " + name + " has acquired the Semaphore...")
        while repeat > 0:
            sleep(delay)
            print("[INFO] " + name + ": " + str(ctime(time())))
            repeat -= 1
        print("[INFO] " + name + " is releasing the Semaphore...")
    print("[INFO] " + name + " completed")


def main():
    my_thread_1 = Thread(target=timer, args=("Timer-1", 1, 5))
    my_thread_2 = Thread(target=timer, args=("Timer-2", 2, 5))
    my_thread_1.start()
    my_thread_2.start()
    timer("MainTimer", 1, 5)
    print("[INFO] MainThread Exited")

if __name__ == '__main__':
    main()

