"""""""""""""""""""""""""""""
"  Created On: 20-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

flag = 1

for i in range(0, 5):
    if flag == 0:
        print("~~~~~~~~~~")
    elif flag == 1:
        pass
    print("I am bored...")
    if i == 3:
        flag = 0

s = "\n";
seq = ("a", "b", "c")  # This is sequence of strings.
print(s.join(seq))
