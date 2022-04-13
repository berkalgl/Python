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

print(obj1)
print(obj2)