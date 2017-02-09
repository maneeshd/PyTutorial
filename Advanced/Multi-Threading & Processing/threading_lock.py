"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17

A very simple example to understand Lock in threads. Locks are useful when a resource should be accessed by
only on ethread at a time to prevent deadlock and race conditions.
"""
from threading import Thread, Lock
from time import sleep, ctime, time

t_lock = Lock()


def timer(name, delay, repeat):
    print("[INFO] " + name + " started")
    t_lock.acquire()            # 'with t_lock:' can be used.
    print("[INFO] " + name + " has acquired the Lock...")
    while repeat > 0:
        sleep(delay)
        print("[INFO] " + name + ": " + str(ctime(time())))
        repeat -= 1
    print("[INFO] " + name + " is releasing the Lock...")
    t_lock.release()
    print("[INFO] " + name + " completed")


def main():
    my_thread_1 = Thread(target=timer, args=("Timer-1", 1, 5))
    my_thread_2 = Thread(target=timer, args=("Timer-2", 2, 5))
    my_thread_1.start()
    my_thread_2.start()
    timer("MainTimer", 0.5, 5)
    print("[INFO] MainThread Exited")

if __name__ == '__main__':
    main()
