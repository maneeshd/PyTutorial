"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17
"""
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def f(sema, thread_pool):
    logging.debug('Waiting to join the pool')
    with sema:
        name = threading.currentThread().getName()
        thread_pool.make_active(name)
        time.sleep(0.5)
        thread_pool.make_inactive(name)

if __name__ == '__main__':
    pool = ThreadPool()
    s = threading.Semaphore(3)
    for i in range(10):
        t = threading.Thread(target=f, name='thread_'+str(i), args=(s, pool))
        t.start()
