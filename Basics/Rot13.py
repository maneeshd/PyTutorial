"""""""""""""""""""""""""""""
"  Created On: 30-Aug-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""


def rot13(mess):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lows = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in mess:
        if char.isupper():
            char_val = int(caps.index(char))
            shift_val = (char_val + 13) % 26
            replace_char = str(caps[shift_val])
            encrypted += replace_char
        elif char.islower():
            char_val = int(lows.index(char))
            shift_val = (char_val + 13) % 26
            replace_char = str(lows[shift_val])
            encrypted += replace_char
        else:
            encrypted += char
    return encrypted


print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('Since rot13 is symmetric you should see this message')))
