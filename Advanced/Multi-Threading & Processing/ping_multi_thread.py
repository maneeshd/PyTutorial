import os
import re

received_packets = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")


for suffix in range(0, 255):
    ip = "106.51.142." + str(suffix)
    out = os.popen("ping -q -c2" + ip, "r")
    print("...Pinging", ip)
    while True:
        line = out.readline()

        n_received = received_packets.findall(line)
        if n_received:
            print(ip, ": " + status[int(n_received[0])])

