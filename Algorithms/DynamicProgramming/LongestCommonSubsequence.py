def LCSRecursive(A,B, i, j):
    if i >= len(A) or j >= len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + LCSRecursive(A,B,i+1,j+1)
    else:
        return max(LCSRecursive(A,B,i+1,j), LCSRecursive(A,B,i,j+1))

def LCSDP(A, B, lenA, lenB, twodim):
    if lenA == 0 or lenB == 0:
        return 0

    if A[lenA - 1] == B[lenB - 1]:
        twodim[lenA][lenB] = 1 + LCSDP(A, B, lenA - 1, lenB - 1, twodim)
        return twodim[lenA][lenB]
    
    if twodim[lenA][lenB] != -1:
        return twodim[lenA][lenB]

    twodim[lenA][lenB] = max(LCSDP(A, B, lenA, lenB - 1, twodim), LCSDP(A, B, lenA - 1, lenB, twodim))

arr1="ABCDGHLQR"
arr2="AEDPHR"
two= [[]]
print(LCSRecursive(arr1,arr2,0,0))
print(LCSDP(arr1,arr2,len(arr1),len(arr2),two))