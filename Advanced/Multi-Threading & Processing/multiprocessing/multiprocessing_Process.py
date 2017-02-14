"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 10-Feb-17
"""
from multiprocessing import Process, current_process
from time import time, ctime, sleep


def timer(delay, repeat):
    name = current_process().name
    print("[INFO] " + name + " started")
    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print("[INFO] " + name + " completed")


def main():
    process1 = Process(target=timer, args=(1, 5,), name="Process_01")
    process2 = Process(target=timer, args=(2, 5,), name="Process_02")
    process1.start()
    process2.start()
    timer(1, 5)

if __name__ == '__main__':
    main()
