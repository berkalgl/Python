def mergeSortedArrays(arr1, arr2, m, n):
    print(type(arr1))
    print(type(arr2))
    #check input
    if isinstance(arr1,list) == False:
        return "arr1 is not valid"
        
    if isinstance(arr2,list) == False:
        return "arr2 is not valid"

    if len(arr1) == 0:
        return arr2
    
    if len(arr2) == 0:
        return arr1

    last = m + n - 1

    while m > 0 and n > 0:
        if arr1[m - 1] > arr2[n - 1]:
            arr1[last] = arr1[m - 1]
            m -= 1
        else:
            arr1[last] = arr2[n - 1]
            n -= 1
        last -= 1
    
    while n > 0:
        arr1[last] = arr2[n - 1]
        n, last = n - 1, last - 1
    
    return arr1
    #easier way
    # arr1.extend(arr2)
    # arr1.sort()
    # return arr1

mergedArray = mergeSortedArrays([11,13,16,19,24,0,0,0,0,0,0,0,0],[7,10,12,18,33,53,66,71], 5, 8)

for i in mergedArray:
    print(i)