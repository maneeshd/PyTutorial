"""""""""""""""""""""""""""""
"  Created On: 24-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

import re

ip_dict = {}
count = 0
pattern = re.compile('lease\s(10\.126\.141\.\d+)\s*\{.*?binding\sstate\s(active);.*?hardware\sethernet\s([:a-f0-9]+);'
                     '.*?uid "(Cisco Systems Inc.*?)";.*?\}', re.MULTILINE | re.DOTALL | re.M)

with open("dhcpd.leases", 'r') as f:
    for match in pattern.finditer(f.read()):
        ip_dict[match.group(1)] = match.group(3)

print("Total Leased Server IPs: " + str(len(ip_dict)))
print("IP ADDRESS \t\t:\t\t MAC ADDRESS")
print("-" * len("IP ADDRESS        :        MAC ADDRESS"))

for key in ip_dict.keys():
    print("%s \t:\t %s" % (key, ip_dict.get(key),))
