"""""""""""""""""""""""""""""
"  Created On: 25-Aug-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""

import time

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lows = "abcdefghijklmnopqrstuvwxyz"


def encrypt(message, shift_key):
    encrypted = ""
    for char in message:
        if char in caps:
            char_val = int(caps.index(char))
            shift_val = (char_val + shift_key) % 26
            replace_char = str(caps[shift_val])
            encrypted += replace_char
        elif char in lows:
            char_val = int(lows.index(char))
            shift_val = (char_val + shift_key) % 26
            replace_char = str(lows[shift_val])
            encrypted += replace_char
        else:
            encrypted += char
    return encrypted


def decrypt(encrypted, key):
    message = ""
    for char in encrypted:
        if char in caps:
            char_val = int(caps.index(char))
            shift_val = (char_val - key) % 26
            if shift_val < 0:
                shift_val = (len(caps) + shift_val)
            replace_char = str(caps[shift_val])
            message += replace_char
        elif char in lows:
            char_val = int(lows.index(char))
            shift_val = (char_val - key) % 26
            if shift_val < 0:
                shift_val = (len(lows) + shift_val)
            replace_char = str(lows[shift_val])
            message += replace_char
        else:
            message += char
    return message


def main():
    while True:
        print("1.Encrypt\n2.Decrypt\n3.Exit")
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3"]:
            print()
            print("Please enter a valid choice...")
            print()
        elif choice is "1":
            print()
            msg = input("Please enter the message to be encrypted: ")
            shift = input("Please enter the key to shift: ")
            print("The encrypted message = " + str(encrypt(msg, int(shift))))
            print()
        elif choice is "2":
            print()
            enc = input("Enter the encrypted message: ")
            key = int(input("Enter the key: "))
            print("The decrypted message = " + decrypt(enc, key))
            print()
        elif choice is "3":
            print("\nTHANK YOU :-)")
            time.sleep(1)
            exit(0)


if __name__ == '__main__':
    main()
