num = [2, 3, 2, 6, 3, 6, 1]

# 1
num = set(num)
print(num)

# 2
uniques = []
for i in num:
    if i not in uniques:
        uniques.append(i)
print(uniques)
