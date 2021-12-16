string = "Hi My name is Berk"
print(len(string))

reversedByPython = string[::-1]
print(reversedByPython)

reversedString = ""
for i in range(len(string),0,-1):
    reversedString = reversedString + string[i-1]

print(reversedString)
