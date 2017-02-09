"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


def fact(x):
    if x is None:
        return "cnl^lnn"
    elif x < 2:
        return 1
    else:
        return x * fact(x - 1)


def pascal(row):
    for n in range(0, row):
        for i in range((row - n - 2) + 1):
            print(" ", end="")
        for i in range(n + 1):
            print(str(fact(n) // (fact(i) * fact(n - i))) + " ", end="")
        print("")


rows = int(input("Enter the number of rows to be in the Pascal Triangle: "))
pascal(rows)
