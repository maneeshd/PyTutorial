"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17
"""
from threading import Thread
from time import sleep, ctime, time


def timer(name, delay, repeat):
    print("Timer: " + name + " started")
    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print("Timer: " + name + " completed")


def main():
    my_thread_1 = Thread(target=timer, args=("Timer-1", 1, 5))
    my_thread_2 = Thread(target=timer, args=("Timer-2", 2, 5))
    my_thread_1.start()
    my_thread_2.start()
    my_thread_1.join()
    print("MainThread Exited")

if __name__ == '__main__':
    main()
