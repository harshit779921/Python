#  Generators in Python | Yield Function with Execution

# import sys
# def creater():
#     list = []
#     i = 1
#     while i<=200:
#         list.append(i)
#         i += 1
#     return list

# print(creater())
# z = sys.getsizeof(list)
# print(z)
# print([num+10 for num in creater()])

def creater1 ():
    i =1
    while i <= 200:
        yield i
        i += 1
print(creater1())
x = creater1()
print(next(x))  # prints 1 as we can print the number 1 by 1 so the memory storage is efficient

print(list(x)) # print full number
    