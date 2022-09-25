def largest_value(inputDict):
    '''largest_value(inputDict) -> (key, value)
    returns key/value pair with largest value
    assume values are all positive integers'''
    # initialize variables
    largestValue = 0
    largestKey = ''
    for key in inputDict:
        if inputDict[key] > largestValue:  # found a bigger value
            (largestKey, largestValue) = (key, inputDict[key])
    return (largestKey, largestValue)

wordCount = {}  # empty dictionary to store the word counts
inFile = open('aesop.txt', 'r')

for line in inFile:
    line = line.lower()  # make everything lowercase
    # replace punctuation with spaces
    for char in '.,!?':
        line = line.replace(char, '')
    wordList = line.split()
    # count words
    for word in wordList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

inFile.close()

for i in range(10): # print out top 10 words
    (word, value) = largest_value(wordCount)
    print('\"' + word + '\"' + " appears " + str(value) + " times")
    wordCount.pop(word)