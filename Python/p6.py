# wap to find greatest of 4 number

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter forth number:"))

if (a > b) and (a > c) and (a > d):
    print("The Greatest Number is", a)
elif (b > c) and (b > d):
    print("The Greatest Number is", b)
elif c > d:
    print("The Greatest Number is", c)
else:
    print("The Greatest Number is", d)
