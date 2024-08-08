# Find Min and Max from Array


def find(arr):
    minn, maxx = arr[0], arr[0]
    for num in arr[1:]:
        if num < minn:
            minn = num
        elif num > maxx:
            maxx = num

    return minn, maxx


array = [4, 10, 40, 1, 5, 9, 3, 5]
minn, maxx = find(array)
print(minn, maxx)
