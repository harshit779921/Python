# Without Lambda function

numbers = [11, 20, 31, 40, 51, 60, 71, 80 ,91, 100]

def even(x):
    return x % 2 == 0

even_num = list(filter(even, numbers))

print("Even Numbers: ", even_num)

# Lambda Function 

numbers = [11, 20, 31, 40, 51, 60, 71, 80 ,91, 100]

even_num = list(filter(lambda x : x % 2 == 0 and x > 30, numbers))

print ("Even numbers greater than 30: ", even_num)