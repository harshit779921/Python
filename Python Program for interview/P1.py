# Sum of odd number using while loop that add all numbers from 1 to 50

a = 1
total = 0
while a <= 50:
    if a % 2 != 0:
        total += a
    a += 1

print(total)

#  second way do not use if

a = 1
total = 0
while a <= 50:
    total += a
    a += 2

print(total)
