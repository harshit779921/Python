# wap for fibbonacci sequence


def fibb(n):
    a = 0
    b = 1

    print("Fibonacci Series:")
    print(a, b, end=" ")
    while n > 0:
        c = a + b
        print(c, end=" ")
        a = b
        b = c

        # c = a + b
        n -= 1


n = int(input("Enter the number of terms you want in Fibonacci series:"))

fibb(n)
