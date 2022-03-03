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
