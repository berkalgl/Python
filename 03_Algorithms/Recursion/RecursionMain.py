# is a concept actually.
# searching file in our desktop, we need to look at the folders recursively
# recursive functions have two paths
# 1 is the recursive case that is called a function again and run it
# 2 is the best case stop calling the function, there's nothing more to search

counter = 0
def inception():
    global counter
    print(str(counter))
    # base case
    if counter > 3:
        return 'done'
    #base case

    counter += 1
    #recursive case
    return inception()
    #recursive case

inception()
# 1 - identify the base case
# 2 - identify the recursive case
# 3 - get closer and closer and return when needed. Usually you have two returns