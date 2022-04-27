#in some cases, it is very efficient to use
# if list is almost sorted
# best case O(n), average O(n^2), worst O(n^2)


numbers = [99,44,6,2,1,5,63,87,283,4,0]

def InsertionSort(arr):
    length = len(arr)
    for i in range(1,length):
        key = arr[i]
        j = i -1
        #compare key with each element on the left of it until an element smaller than it is found
        #for descending order, change key<array[j] to key>array[j]
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        
        #place key at after the element just smaller than it
        arr[j+1] = key

    return arr

sortedArray = InsertionSort(numbers)
print(sortedArray)