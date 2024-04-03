# wap to print the elements of a list in a single line. (list is the parameter)

cities = ["Delhi", "Mumbai", "Bangalore"]
heroes = ["Superman", "Spiderman", "Iron Man", "Arpitman"]


def print_len(list):
    print(len(list))


def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)