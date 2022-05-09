def StringChallenge(sentence):
    n = len(sentence)
    result = ""
    i = 0
    while i<n:
        count = 1
        while i < n-1 and sentence[i] == sentence[i+1]:
            count += 1
            i += 1
        result = result + str(count) + sentence[i]
        i+=1


    return result

print(StringChallenge("aaaabbbccd"))