# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/
import re

string = 'search inside of this text please!'

print('search' in string)

a = re.search('this', string)

print(a.span()) # start and stop index 
print(a.start()) # start index
print(a.end()) # stop index
print(a.group()) # gives that piece of part

pattern = re.compile('this')
b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)

pattern2 = re.compile(r"([a-zA-Z]).([a])") # r stands for raw string / pure string
string = 'search this inside of this text please ! Berk'