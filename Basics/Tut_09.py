"""""""""""""""""""""""""""""
"  Created On: 26-Aug-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

string = "maneesh D"
for char in string:
    if char is " ":
        string += "+"
print(string)

for char in string:
    if char is "+":
        string += "f"
print(string)

sr = 'abgsfdraa'
alpha = list(sr)
print(alpha)
print(alpha[0].isupper())

a = 9
b = 6
print(str(a) + str(b))
(a, b) = (b, a)
print(str(a) + str(b))
