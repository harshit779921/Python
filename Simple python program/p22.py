#write a recursive function to print all elements in a list

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mangos",'banana',"apple"]  

print_list(fruits)