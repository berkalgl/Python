# Write two functions that finds the factorial of any number. One should 
# use recursive, the other should just use a for loop

def findFactorialRecursive(number): #O(n)
    if number <= 1:
        return 1
    
    return number * findFactorialRecursive(number - 1)

def findFactorialIterative(number): #O(n)
    currentNumber = 1
    answer = 1
    while currentNumber <= number:
        answer = answer * currentNumber
        currentNumber += 1

    return answer

print(findFactorialRecursive(2))
print(findFactorialIterative(2))