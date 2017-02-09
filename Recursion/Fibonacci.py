"""
@author: Maneesh D
@email: maneeshd77@gmail.com
"""


def fibo(num):
    if num < 2:
        return num
    else:
        return fibo(num - 2) + fibo(num - 1)


def main():
    print("Fibonacci Series till 20:")
    total = 0
    for i in range(20):
        n = fibo(i)
        print(n)
        total = total + n
    print("Series Sum=", total)

if __name__ == '__main__':
    main()
