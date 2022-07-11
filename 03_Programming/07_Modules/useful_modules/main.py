# Collection Module

from collections import Counter,defaultdict,OrderedDict

li = [1,2,3,4,5,6,7]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

#default dict helps us to give default value for non-existing key
dictionary = defaultdict(lambda: 'does not exist',{ 'a':1 , 'b':2})
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

#returns false because of order
# with regular dict it would return true
print(d2 == d)

# Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!
#https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/

import datetime 

print(datetime.time()) # 00:00:00
print(datetime.time(5,45,2)) # 05:45:02
print(datetime.date.today()) #2022-05-23

#https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
from array import array

#typecode is what type of data we are holding
#to help memory optimization
#https://docs.python.org/3/library/array.html#module-array
arr = array('i', [1,2,3])
print(arr[0])