# 0,1,1,2,3,5,8,13,21,34,55,89,144...

calc = 0
def fibonacci(n): #where n is index and time complexity O(2^n)
    global calc
    calc += 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(20))
print(calc)
calc = 0
print('--------')

#### Pay Attention to time complexity 2^n to n, however space complexity increases

def fibonacciDP(): #where n is index and time complexity O(n)
    cache={}
    def fibonacciInner(n):
        global calc
        calc += 1
        if n < 2:
            return n

        if n not in cache:
            cache[n] = fibonacciInner(n-1) + fibonacciInner(n-2)
        
        return cache[n]
    
    return fibonacciInner

fib = fibonacciDP()
print(fib(20))
print(calc)

# Bottom up approach
def fibonacci2(n):
    answer = [0,1]
    for i in range(2, n+1):
        answer.append(answer[i-2] + answer[i-1])
    return answer.pop()

print(fibonacci2(20))