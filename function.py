def countWordsFromFile():  
    fileName = input("New Text Document")
    numberOfWords=0

    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)             

    print("number of  words")
    print(numberOfWords)

countWordsFromFile()