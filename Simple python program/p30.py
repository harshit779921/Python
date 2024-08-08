#   Write a program that calculates the factorial of a number.

def fact(n) : 
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("enter the number: "))  
print("The factorial of",n,"is",fact(n))