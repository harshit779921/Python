# Find the remainder without using "%" operator

def fun(x, y):
    if x < y:
        return x
    return (x - y, y )

print(fun(50,20))
