# search for a number x in this tuple using loop

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter the element you want to find:"))

count = 0
while count <= len(num):
    if (num[count] == x):
        print("found the index", count)
    else:
        print("not found")
    count += 1
