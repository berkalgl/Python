#DATA STRUCTURES
#--------------------------------------
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

