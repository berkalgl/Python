#basket = ['apples', 'grapes', 'pears']

#linkedList
# apples --> grapes --> pears
#
# apples 
# 8947 --> grapes
#          8742 --> pears
#                   372 --> null   #numbers are location of the memory
# prepend O(1), append O(1), lookup O(n), insert O(n), delete O(n)
#
# a pointer is a simply reference of another location in the memory

# both obj1 and obj2 reference to {'a': True} in the memory
obj1 = { 'a' : True}
obj2 = obj1
obj1['a'] = 'hi there'

#computer are gonna delete the memory that is unused and because it sees that object is still referencing the location of 
# {'a' : True} and this will not be deleted
# CARBAGE COLLECTION
# If obj2 is changed by another value like a string, {'a': True} will not be used anymore and it is going to be garbage collected and deleted
del obj1

print(obj1) #obj1 is undefined
print(obj2) # but this works !!!