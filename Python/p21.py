#write a recursive function to calculate the sum of first n natural number

def  sum_natural(n):
    if(n==0):
        return 0
    # print(n)
    return sum_natural (n-1)+n

sum=sum_natural(int(input("enter the number: ")))    
print(sum)