"""""""""""""""""""""""""""""
"  Created On: 05-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""


def fact(n):
    if n is None:
        return "cnl^lnn"
    elif n < 2:
        return 1
    else:
        return n * fact(n - 1)


print(fact(None))
print(fact(-9))
print(fact(0))
print(fact(1))
print(fact(2))
print(fact(5))
print(fact(44))
