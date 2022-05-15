 # DP is just an optimization technique using something called caching
 # if you have smth that you can cash, you can use dp
 # Memoization 1,2
 # is a way to solve problems by breaking it down into a collection of sub problems
 # solving each of those problems just once and storing their solutions in case next time the same problem occurs

 # Caching is a way to store values so you can use them later on
 # Memoization is a specific form of caching 

 # DP is combined Divide and Conquer + Memoization

 # 1 - Can be divided into subproblem ?
 # 2 - Recursive Solution
 # 3 - Are there repetitive subproblems ? 
 # 4 - Memoize subproblems

# Memoization 1
def AddTo80(n):
    print('long time')
    return n + 80

cache = {}

def MemoizedAddTo80(n):
    if n not in cache:
        cache[n] = AddTo80(n)
    
    return cache[n]

MemoizedAddTo80(5)
MemoizedAddTo80(5)


# Memoization 2 -- to avoid global scope
# the pattern is called closure

def Memoized2AddTo80():
    cache2 = {}
    def InnerFunction(n):
        if n not in cache2:
            cache2[n] = AddTo80(n)
        
        return cache2[n]

    return InnerFunction

memoized = Memoized2AddTo80()

print(memoized(5))
print(memoized(5))