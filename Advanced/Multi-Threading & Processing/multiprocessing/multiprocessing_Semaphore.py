"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 17-Feb-17
"""
from multiprocessing import Process, current_process, BoundedSemaphore
from time import ctime, time, sleep


sema = BoundedSemaphore(2)


def timer(name, delay, repeat):
    print("[!] " + current_process().name + " started")
    sema.acquire()
    print("[!] " + current_process().name + " has acquired the Sema...")
    while repeat > 0:
        sleep(delay)
        print(name + ": " + str(ctime(time())))
        repeat -= 1
    print("[!] " + current_process().name + " is releasing the Sema...")
    sema.release()
    print("[!] " + current_process().name + " exited")


def main():
    process1 = Process(target=timer, args=("Timer1", 1, 5), name="Process1")
    process2 = Process(target=timer, args=("Timer2", 1, 5), name="Process2")
    process3 = Process(target=timer, args=("Timer3", 1, 5), name="Process3")

    process1.start()
    process2.start()
    process3.start()
    timer("MainTimer", 1, 5)

if __name__ == '__main__':
    main()