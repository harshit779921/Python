# Scope & Lifetime of a Variable

glob = "Hi , I am Globally Vaiable"

def f1():
    """
    Testing scope and lifetime of a variable
    """
    local = "Hi , I am Locally Variable"
    print(local)
    print(glob)
    
f1()
print(glob)
# print(local) does not print outside the function