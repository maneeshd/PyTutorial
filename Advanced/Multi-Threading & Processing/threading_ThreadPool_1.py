"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17
"""
from logging import basicConfig, getLogger, DEBUG
from threading import Thread, Lock, currentThread, Semaphore
from time import sleep

basicConfig(level=DEBUG, format='(%(threadName)-9s) %(message)s',)
logger = getLogger("ThreadPool_Logger")


class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = Lock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logger.debug('Running: %s', self.active)

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logger.debug('Running: %s', self.active)


def f(sema, thread_pool):
    logger.debug('Waiting to join the pool')
    with sema:
        name = currentThread().getName()
        thread_pool.make_active(name)
        sleep(0.5)
        thread_pool.make_inactive(name)

if __name__ == '__main__':
    pool = ThreadPool()
    s = Semaphore(3)
    for i in range(10):
        t = Thread(target=f, name='thread_'+str(i), args=(s, pool))
        t.start()
