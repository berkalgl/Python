def SearchChallenge(sentence):
    wordArray = [word for word in sentence.split()]
    count = 0
    word = "-1"

    for i in range(0, len(wordArray) - 1):
        for a in range(0, len(wordArray[i]) - 1):
            newCount = 0

            for b in range(a + 1, len(wordArray[i]) - 1):
                if wordArray[i][a] == wordArray[i][b]:
                    newCount += 1
            
            if newCount > count:
                count = newCount
                word = wordArray[i]

    return word


print(SearchChallenge("Merhabaa benim adım namee"))