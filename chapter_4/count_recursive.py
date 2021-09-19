
def count(arr):
    if(len(arr) == 0):
        return 0
    return 1 + count(arr[1:])


print(count([5, 2, 6, 2, 10]))
