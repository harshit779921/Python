# Sum of Sums of Natural numbers

n = int(input())
k = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        k = k + j
print(k)
