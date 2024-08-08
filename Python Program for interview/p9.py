#  Iterative() vs Recursive()

# Iterative()
def iterative(n):
    total = 0
    for i in range(n):
        total += 2 ** i
    return total

n = int(input("Enter the number: "))
print(f"iterative answer:",iterative(n))    

# Recursive()
def recursive(n):
    if n == 1:
        return 1
    return 2 ** (n-1) + recursive(n-1)

n = int(input("Enter the number: "))
print(f"recursive answer:",recursive(n))