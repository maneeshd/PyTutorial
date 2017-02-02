"""""""""""""""""""""""""""""
"  Created On: 19-Sep-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

string = "ThiS is String with Upper and lower case Letters."
dicto = {}

for char in string.lower():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char in alphabet:
        if char not in dicto:
            dicto[char] = 1
        else:
            count = dicto.get(char)
            count += 1
            dicto[char] = count
keys = list(dicto.keys())
keys.sort()

for char in keys:
    print(char, dicto[char])

word = "--------------------------------------------------maneesh-----------------------------------------"
word = word.replace("-", "")
print(word)
