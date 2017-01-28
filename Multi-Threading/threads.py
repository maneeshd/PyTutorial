"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""

import threading


print("Creating Thread1...")
thread1 = threading.Thread(name='MyThread-1')
thread1.start()
print("Thread1 = ", thread1.getName())
print("Thread1 is daemon = ", thread1.isDaemon())

print("Creating Thread2...")
thread2 = threading.Thread(name="MyThread-2", daemon=True)
thread1.join()
print("Killing Thread1...")
thread2.start()
print("Thread2 = ", thread2.getName())
print("Thread2 is daemon = ", thread2.isDaemon())
thread2.join()
print("Killing Thread2...")
