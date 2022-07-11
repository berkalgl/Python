my_file = open('.\\Documents\\test.txt')

#print(my_file.read())
#You cannot read file more than once
# because of the function of open has this idea of a cursor
# once you open, it returns a file object
# and the contents of the file you can read with a cursor
# But by the end of this first reading, the cursor is going to be at
# the end of the file
# so we have to
# my_file.seek(0)
#print(my_file.read())

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines())

my_file.close()

# to avoid cursor use with statement

# mode_types
# r -> read (Default)
# w -> write # clear the file and writes it
# r+ -> read, write # overwrites the file
# a -> append
with open('.\\Documents\\test.txt', mode='w') as my_file2:
    text = my_file2.write(':)') 
    print(text) #prints the length of the characters

#non existing file
# in r+ mode FileNotFoundError exception has thrown
# in w mode creates the file
with open('.\\Documents\\sad.txt', mode='w') as my_file2:
    text = my_file2.write(':(') 
    print(text) #prints the length of the characters

# if you are on a Unix based system 
# you need to use / for the path

# pathlib allows us to work with all systems
#https://docs.python.org/3/library/pathlib.html


#File IO Errors

try:
    with open('.\\Documents\\sad2.txt', mode='r') as my_file3:
        print(my_file3.read())
except FileNotFoundError as err:
    print('File not found')
    raise err
except IOError as err:
    print('IO Error')
    raise err