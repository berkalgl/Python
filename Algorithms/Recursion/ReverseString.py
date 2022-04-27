def reverseString(str):
    if str == '':
        return ''
    reversed = reverseString(str[1:]) + str[0]
    return reversed

print(reverseString('Hello Darling!'))