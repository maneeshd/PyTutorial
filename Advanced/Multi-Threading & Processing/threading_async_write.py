"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 09-Feb-17
"""
from threading import Thread
from time import sleep


class AsyncWrite(Thread):
    def __init__(self, text, out):
        Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        fh = open(self.out, "a")
        fh.write(self.text + "\n")
        fh.close()
        sleep(2)
        print("Finished Background File Write to " + self.out)


def main():
    message = input("Enter ur message to store: ")
    background_thread = AsyncWrite(message, "out.txt")
    background_thread.start()   # This thread will write the mesasge to file
    print("The program can continue while it writes it in another thread")
    print("100 + 400 = ", 100+400)  # Main thread will compute this

    background_thread.join()
    print("Waited until thread was completed...")

if __name__ == '__main__':
    main()
