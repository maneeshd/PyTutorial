"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 16-Feb-17
"""
from multiprocessing import Process, Lock, current_process
from time import time, ctime, sleep


p_lock = Lock()


def timer(name, delay, repeat):
    print("[!] " + current_process().name + " started")
    p_lock.acquire()            # 'with p_lock:' can be used.
    print("[!] " + current_process().name + " has acquired the Lock...")
    while repeat > 0:
        # sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print("[!] " + current_process().name + " is releasing the Lock...")
    p_lock.release()
    print("[!] " + current_process().name + " exited")


def main():
    process1 = Process(target=timer, args=("Timer1", 1, 5), name="Process1")
    process2 = Process(target=timer, args=("Timer2", 2, 5), name="Process2")
    process1.start()
    process2.start()
    # timer("MainTimer", 1, 5)
    process1.join()
    process2.join()


if __name__ == '__main__':
    main()
