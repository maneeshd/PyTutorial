"""""""""""""""""""""""""""""
"  Created On: 20-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""
import re

fh1 = open("details.txt", 'r')
fh2 = open("adapters.txt", 'r')

det = fh1.read()
ad = fh2.read()

p1 = re.compile("Power:(\s*)(on|off)*")
p2 = re.compile("Product Name:(\s*)(\w*)(\s*)(\w*)(\s*)(\w*)")
p3 = re.compile("Serial Number:(\s*)(\w*)")
p4 = re.compile("Slot (\w*)")
p5 = re.compile("Product Name : .*[^\n]")

p_state = p1.search(det).group()
if p_state == "Power: on":
    print("On")
print(p2.search(det).group())
print(p3.search(det).group())
slist = p4.findall(ad)
print(slist)
plist = p5.findall(ad)

for i in range(0, len(plist)):
    plist[i] = plist[i].strip("Product Name : ")

print(plist)

dic = dict(zip(slist, plist))
print("-" * 15)
for key in dic.keys():
    print(key + "=> " + dic.get(key))
