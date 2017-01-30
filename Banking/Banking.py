"""
Author: Maneesh Divana
Python: 3.5.2
Python-201 VILT Course Assignment: Bank Transactions using text files.
Date: 8 Dec, 2016
"""
from math import fabs, pow, e
from re import compile
from sys import exit
from threading import Thread


def get_number(line):
    return line.split(" ")[0]


def get_balance(line):
    return line.split(" ")[1]


def get_name(line):
    return line.split(" ", maxsplit=2)[2].rstrip()


def equal_floats(float1, float2):
    k = 1.0 * pow(e, -8)
    if fabs(float1 - float2) < k:
        return True
    else:
        return False


def withdraw(balance):
    while True:
        try:
            debit = float(input("Enter the amount to be withdrawn: "))
            if debit < 0:
                print("Invalid Amount Entered...Amount cannot be less than 0.00")
                continue
            else:
                break
        except ValueError:
            print("Invalid entry...Should be a number not a string..")
            continue
        except (KeyboardInterrupt, EOFError):
            return None
    new_balance = balance - debit
    return new_balance


def deposit(balance):
    while True:
        try:
            credit = float(input("Enter the amount to be deposited: "))
            if credit < 0:
                print("Invalid Amount Entered...Amount cannot be less than 0.00")
                continue
            else:
                break
        except ValueError:
            print("Invalid entry...Should be a number not a string..")
            continue
        except (KeyboardInterrupt, EOFError):
            return None
    new_balance = balance + credit
    return new_balance


def main():
    f = None
    fw = None
    pattern = compile(".*(999999).*")
    try:
        f = open("customers_old.txt", "r", encoding="UTF-8")
        fw = open("customer_new.txt", "w", encoding="UTF-8")
        for customer in f.readlines():
            if pattern.search(customer):
                print("End of file reached...Saving and Exiting")
                break
            account_no = get_number(customer)
            balance = float(get_balance(customer))
            name = get_name(customer)
            while True:
                print(
                    "\nName: %s\tAccount Number: %s\tBalance: %s" %
                    (name, account_no, str(balance)))
                print("w : Withdrawal\n"
                      "d : Deposit\n"
                      "c : Close Account\n"
                      "a : Next Customer")
                try:
                    choice = input("Please select the transaction: ")
                except (KeyboardInterrupt, EOFError):
                    print("Ctrl+C has been disabled...press a to the end of file to exit..."
                          "\nSorry for the inconvenience")
                    continue

                if choice.casefold().startswith("w"):
                    new_balance = withdraw(balance)
                    if new_balance is None:
                        print("Transaction Cancelled...")
                    elif new_balance < 0 or equal_floats(new_balance, 0.00):
                        print(
                            "Withdrawal amount exceeds the current balance\nTransaction Cancelled.")
                    else:
                        balance = new_balance
                        print("Transaction Successful...")

                elif choice.casefold().startswith("d"):
                    new_balance = deposit(balance)
                    if new_balance is None:
                        print("Transaction Cancelled...")
                    elif new_balance > 9999999.99:
                        print(
                            "Deposit amount exceeds the account balance limit(9999999.99)\nTransaction Cancelled.")
                    else:
                        balance = new_balance
                        print("Transaction Successful...")

                elif choice.casefold().startswith("c"):
                    try:
                        close = str(
                            input("Are you sure you want to close the account? (Y/N): "))
                        if close.casefold().startswith("y"):
                            print("Account Closed")
                            break
                        elif close.casefold().startswith("n"):
                            print("Transaction Cancelled...")
                            continue
                        else:
                            print("Invalid Entry....")
                            continue
                    except (KeyboardInterrupt, EOFError):
                        print("Transaction Cancelled...")
                        continue

                elif choice.casefold().startswith("a"):
                    line = account_no + " " + str(balance) + " " + name
                    fw.write(line + "\n")
                    print("Next Customer...")
                    break

                else:
                    print("Please select a valid option...")

    except IOError as e1:
        print("Master File could not be opened...\n{0}".format(e1))
        exit(1)
    except KeyboardInterrupt:
        print("Ctrl+C has been disabled...Please press a to the end of file to exit...Sorry for the inconvenience")
        pass
    finally:
        f.close()
        fw.write("999999")
        fw.close()


try:
    t = Thread(target=main)
    t.start()
    t.join()
except KeyboardInterrupt:
    pass
