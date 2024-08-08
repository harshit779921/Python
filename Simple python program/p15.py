# wap to find the factorial of first n numbers

n = int(input("Enter a number: "))
fact = 1
i = 1
for i in range(1, n + 1):
    fact = fact * i

    i += 1
print("factorial =", fact)
