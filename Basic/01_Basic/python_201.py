#DATA STRUCTURES
#--------------------------------------
# =============================================================================
#                         LIST | TUPLE | DICTIONARY | SET
# Changable                Y   |   N   |     Y      |  Y
# Orderable(indexable)     Y   |   Y   |     N      |  N + Unique
# Containable              Y   |   Y   |     Y      |  Y
# =============================================================================
#LISTS

notes = [90,80,70,50, "a", [1,2,3,4]]

type(notes[5])

notes[0:4]
notes[:4]
notes[4:]

#Change Value
notes[1] = 60
#Add value
notes = notes + [100]
#Delete Value
#del notes[0]

#LIST METHODS
dir(list)
#append
notes.append(200)
#remove
notes.remove(200)
#insert
notes.insert(2, 20)
#pop
notes.pop(len(notes)-1)
#count
notes.count(200)
#copy
notes2 = notes.copy()
#extend
notes.extend(notes2)
#index
notes.index(90)
#reverse
notes.reverse()
#sort
notes.sort()
#clear
notes.clear()
#--------------------------------------
#--------------------------------------
#TUPLES - cannot be changed -can contain multiple types - ordered
#define
t = ("berk", "allül", 1,2,3.4,[0,2,4,6])
t = "berk", "allül", 1,2,3.4,[0,2,4,6]
#tuple() cannot be initialized with one element, put ','
t = ("element",)

t[1]
t[0:3]

t[2] = 99 #cannot be changed

#--------------------------------------
#--------------------------------------
#DICTIONARY - can be changed -can contain multiple types - not ordered, indexed
#define
dictionary = {1:"berk", 2:"allül"}
#get
dictionary[1]
#set
dictionary[2] = "berkalgl"
dictionary[3] = "berkalgl"
#--------------------------------------
# #--------------------------------------
#SETS - can be changed -can contain multiple types - not ordered and indexed 
#- UNIQUE VALUES
#define

l = [1,"a", "b", 123]
s = set(l)

t = (1,3,4,5)
s = set(t)

sampleStr = "Hello World, how are you ?"
s = set(sampleStr)

len(s)
s[0] #cannot be indexed

dir(s)
#add
s.add("a")
#remove
s.remove("a")
#discard , do not throw error
s.discard("a")

#cluster operations
# =============================================================================
# difference() diff between two cluster can be used with (-)
# intersection() intersection of two cluster
# union() union of two cluster
# symmetric_difference not included both
# =============================================================================

#difference
s1 = set([1,3,5])
s2 = set([2,3,6])

s1.difference(s2) #s1 has, s2 doesnt have
s2.difference(s1)

s1-s2

#symmetric_difference
s1.symmetric_difference(s2) # compared to each other and includes both

#intersection && union
intersection = s1.intersection(s2)
s1 & s2
union = s1.union(s2)

s1.intersection_update(s2) #updates with union value

#Queries in sets
s1 = set([7,8,9])
s2 = set([5,6,7,8,9,10])
#intersection is empty or not, true -> empty, false -> not empty
s1.isdisjoint(s2)
#a cluster's elements are included in the other cluster --subset
s1.issubset(s2)

#a cluster contains all the elements of other cluster --subset
s2.issuperset(s1)

#--------------------------------------

