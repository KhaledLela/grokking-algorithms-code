
def findMax(arr):
    if (len(arr) == 0):
        return arr[0]
    return max(arr[len(arr) - 1], findMax(arr[1:]))


print(max([5, 2, 6, 10, 3]))
