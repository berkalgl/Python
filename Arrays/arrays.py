strings = ["a","b","c","d"]
#4*4 = 16 bytes of storage

#push
strings.append("e") #O(1)
print(strings)

#pop
strings.pop() #O(1)
print(strings)

#insert
strings.insert(0,"x") #O(n)
print(strings)

strings.insert(2,"alien") #O(n)
print(strings)