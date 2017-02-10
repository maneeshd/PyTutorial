"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 10-Feb-17
"""
from multiprocessing import Process
from time import time, ctime, sleep


def timer(name, delay, repeat):
    print("[INFO] " + name + " started")
    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print("[INFO] " + name + " completed")


def main():
    process1 = Process(target=timer, args=("Process-1", 1, 5))
    process2 = Process(target=timer, args=("Process-2", 2, 5))
    process1.start()
    process2.start()
    print("[INFO] MainProcess Started")
    timer("MainTimer", 1, 5)
    print("[INFO] MainProcess Exited")

if __name__ == '__main__':
    main()
