
def findMax(arr):
    if (len(arr) == 0):
        return 0
    # Use Python built in max function or check it.
    sub_max = findMax(arr[1:])
    el = arr[0]
    return el if el > sub_max else sub_max
    # return max(arr[len(arr)-1], findMax(arr[1:]))


print(findMax([5, 2, 6, 10, 3]))
