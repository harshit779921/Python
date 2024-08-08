# wap to check id a list contains a plindrome of elemnets
# l1 = []
# l2 = []

# list1 = input("Enter the list1:\n")
# l1.append(list1)

list1 = ['R','A','C', 'E', 'C', 'A', 'R']


# list2 = input("Enter the list2:\n")
# l2.append(l2)

list1_copy = list1.copy()
list1_copy.reverse()

# list2_copy = l2.copy()
# list2_copy.reverse()

if list1_copy == list1:  # (list2_copy == l2):

    print(" it is palindrome")

else:
    print("not palindrome")
