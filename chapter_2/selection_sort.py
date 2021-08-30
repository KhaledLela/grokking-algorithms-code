# Selection sort algorithm O(n²)
# You check n elements then n-1 , n-2, ....,2,1
# on avarage you can check a list that has 1/2 x n
# The runtime is O(n x 1/2 n)
# But constants like 1/2 are ignored in Big O notation
# You just write O(n x n) Or O(n²)

def findSmallest(arr):
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1,len(arr)):
        item = arr[i]
        if item < smallest:
            smallest = item
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))
