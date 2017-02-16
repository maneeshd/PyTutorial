"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 17-Feb-17
"""
from multiprocessing import Process
from time import sleep


class AsyncWrite(Process):
    def __init__(self, text, out):
        Process.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, "a") as fh:
            fh.write(self.text + "\n")
        sleep(2)
        print("Finished background file write to " + self.out)


def main():
    message = input("Enter your message to store: ")
    background_process = AsyncWrite(message, "out.txt")
    background_process.start()   # This process will write the mesasge to file
    print("The program can continue while it writes it in another process")
    print("100 + 400 = ", 100+400)  # Main process will compute this

    try:
        print(1 / 0)
    except ZeroDivisionError as e:
        print("Also caught an exception in main process while the background process is writing...")
        print(e)

    background_process.join()
    print("Waited until background thread completed...")
    print("Exiting program...")

if __name__ == '__main__':
    main()
