# all cases O(n^2)
# iterate the array and select the smallest item and replace it with the first item in the array

numbers = [99,44,6,2,1,5,63,87,283,4,0]

def SelectionSort(arr):
    length = len(arr)
    for i in range(length):
        #set current index to min
        min = i
        for j in range(i+1,length):
            if arr[j] < arr[min]:
                #update the minimum if current is lower that what we had before
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

numbers = SelectionSort(numbers)
print(numbers)