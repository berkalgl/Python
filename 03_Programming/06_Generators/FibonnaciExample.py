def fib(index):
    a = 0
    b = 1
    for i in range(index):
        yield a
        temp = a
        a = b
        b = temp + b
        
for x in fib(5):
    print(x)

print([x for x in fib(5)])