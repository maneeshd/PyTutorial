"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 15-Feb-17
"""
import logging
from threading import Thread, current_thread
from time import sleep, ctime, time

logger = logging.getLogger("threadLogger")
logger.setLevel(logging.DEBUG)

# File Handler
fh = logging.FileHandler('threads_log.log', mode="w", encoding="utf-8")
fh.setLevel(logging.DEBUG)

# Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)


def timer(name, delay, repeat):
    logger.log(level=logging.INFO, msg=current_thread().name + " started")
    while repeat > 0:
        sleep(delay)
        logger.log(level=logging.INFO, msg=name + ": " + str(ctime(time())))
        repeat -= 1
    try:
        y = 5 / 0
    except ZeroDivisionError as ze:
        logger.log(level=logging.ERROR, msg="Divide by Zero Error caught")
    logger.log(level=logging.WARN, msg=current_thread().name + " exited")


def main():
    my_thread_1 = Thread(target=timer, args=("Timer1", 1, 5), name="Thread01")
    my_thread_2 = Thread(target=timer, args=("Timer2", 2, 5), name="Thread02")
    my_thread_1.start()
    my_thread_2.start()
    timer("MainTimer", 1, 5)
    my_thread_2.join()
    my_thread_1.join()

if __name__ == '__main__':
    main()
