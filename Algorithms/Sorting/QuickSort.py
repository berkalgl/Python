# it is also divide and conquer
# O(nlogn)
# if the choosen pivot is bad, it can be O(n^2)

numbers = [99,44,6,2,1,5,63,87,283,4,0]

def QuickSort(arr, left, right):
    pivot = 0
    partitionIndex = 0

    if left < right:
        pivot = right
        partitionIndex = Partition(arr, pivot, left, right)

        #sort left and right
        QuickSort(arr, left, partitionIndex -1)
        QuickSort(arr, partitionIndex + 1, right)

    return arr


def Partition(arr, pivot, left, right):
    pivotValue = arr[pivot]
    partitionIndex = left

    for i in range(left,right):
        if arr[i] < pivotValue:
            Swap(arr, i, partitionIndex)
            partitionIndex += 1
    
    Swap(arr,right,partitionIndex)
    return partitionIndex

def Swap(arr, firstIndex, secondIndex):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp

#Select first and last index as 2nd and 3rd parameters
sorted = QuickSort(numbers, 0, len(numbers) - 1)
print(sorted)