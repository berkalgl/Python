#divide and conquer
# we are building a reverse tree
# O(nlogn) n comes from we still compare everything.
# get length of the list and find the middle
# O(logn) is kind of like the height of the tree
#https://stackoverflow.com/questions/1517793/what-is-stability-in-sorting-algorithms-and-why-is-it-important

numbers = [99,44,6,2,1,5,63,87,283,4,0]

def MergeSort(arr):
    if len(arr) == 1:
        return arr
    #split the array in into right and left
    left,right = SplitArr(arr)

    return Merge(MergeSort(left), MergeSort(right)) 

def SplitArr(arr):
    half = len(arr)//2
    return arr[:half],arr[half:]

def Merge(left,right):
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex +=1
    mergedArr = result + left[leftIndex:] + right[rightIndex:]    
    return mergedArr

SortedArr = MergeSort(numbers)
print(SortedArr)
