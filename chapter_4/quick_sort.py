# QuickSort implementation
def qSort(arr):
    # Arrays that has only one item or empty (NO SORT NEEDED)
    # Base Case
    if len(arr) < 2:
        return arr

    # Sorting using partitioning select pivot  put at the middle,
    # (less elements left) + pivot + (great elements right)
    pivot = arr[0]

    # Single line two loops
    lArr = [i for i in arr[1:] if i <= pivot]
    gArr = [i for i in arr[1:] if i > pivot]

    # One loop 
    # lArr = []
    # gArr = []
    # for i in arr[1:]:
    #     if i <= pivot:
    #         lArr.append(i)
    #     else:
    #         gArr.append(i)
    return qSort(lArr) + [pivot] + qSort(gArr)


print(qSort([100, 20, 10, 200, 300, 50, 30, 40]))
