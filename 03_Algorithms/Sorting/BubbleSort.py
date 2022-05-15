# bubble sort comes from the idea of bubbling up the largest value using multiple passthrough
# simplest, but the least efficient
# compares the number with the next number until its sorted

# best case O(n), average O(n^2), worst O(n^2)
#https://www.youtube.com/user/AlgoRythmics/videos

numbers = [99,44,6,2,1,5,63,87,283,4,0]

def bubbleSort(arr):
    length = len(arr)

    for i in range(length-1):
        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                # swap numbers
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

bubbleSort(numbers)

print(numbers)