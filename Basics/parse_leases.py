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
print(ip_dict)
print(len(ip_dict))
