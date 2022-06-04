def LCSRecursive(A,B, i, j):
    if i >= len(A) or j >= len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + LCSRecursive(A,B,i+1,j+1)
    else:
        return max(LCSRecursive(A,B,i+1,j), LCSRecursive(A,B,i,j+1))

def LCSDP(A, B, lenA, lenB, lookup):
    if lenA == 0 or lenB == 0:
        return 0
    
    key = (lenA, lenB)

    if key not in lookup:
        if A[lenA-1] == B[lenB-1]:
            lookup[key] = LCSDP(A, B, lenA - 1, lenB - 1, lookup) + 1
        else:
            lookup[key] = max(LCSDP(A, B, lenA - 1, lenB, lookup), LCSDP(A,B, lenA, lenB - 1, lookup))

    return lookup[key]
    

arr1="ABCDGHLQR"
arr2="AEDPHR"
lookup = {}
print(LCSRecursive(arr1,arr2,0,0))
print(LCSDP(arr1,arr2,len(arr1),len(arr2),lookup))