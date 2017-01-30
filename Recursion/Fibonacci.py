"""""""""""""""""""""""""""""
"  Created On: 05-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 2) + fibo(n - 1)


print("Fibonacci Series till 20:")
total = 0
for i in range(20):
    n = fibo(i)
    print(n)
    total = total + n
print("Series Sum=", total)
