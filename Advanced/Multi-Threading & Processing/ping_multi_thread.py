"""
@author: Maneesh D
@email: maneeshd77@gmail.com

A multi-threaded ping implementation.(Pings all IP addresses in the range)
"""
from platform import system
from re import search, compile, IGNORECASE
from subprocess import getstatusoutput
from threading import Thread


def ping(ip, n=2):
    """
    Will ping the IP address.(Not websites..To ping websites remove the first if condition)
    :param ip: IP address to be pinged as a String
    :param n: Number of packets to send while pinging. Default is 2
    :return: boolean True if the IP pings or boolean False is it doesn't.
    """
    if search("\d+\.\d+\.\d+\.\d+", ip) is None:
        return False
    failure_pattern = compile(".*Destination host unreachable.*|.*General Failure.*|.*Request timed out.*",
                              IGNORECASE)
    if system() == "Windows":
        status, result = getstatusoutput("ping -n %s %s" % (n, ip))
    else:
        status, result = getstatusoutput("ping -c %s %s" % (n, ip))

    if status == 1:
        print(ip, "is not pinging")

    if failure_pattern.search(result):
        print(ip, "is not pinging")
    else:
        print(ip, "is pinging")


def main():

    threads = list()
    for suffix in range(0, 256):
        ip = "10.242.128." + str(suffix)
        thread = Thread(target=ping, args=(ip, 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    from timeit import Timer
    t = Timer(stmt='main()', setup="from ping_multi_thread import main")
    print("\nExecution Time= %.3f" % t.timeit(number=1))
