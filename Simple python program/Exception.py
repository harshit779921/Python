# def main():
#     x= get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x=int(input("Enter a number: "))
#         except:
#             print("x is not an integer:")
#         else:
#             return x        # return exits the function, so there'

# main()

def main():
    x= get_int("enter the number:")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass
            # print("x is not an integer:")
        # else:
        #     pass       # pass does nothing but allow the loop to continue
main()