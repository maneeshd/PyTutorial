#!/usr/local/bin/python3.6
"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


import threading
import time


class MyThread (threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


def main():
    print(threading.current_thread().getName())

    # Create new threads
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

#    Start new Threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
