def main()
    getSentence = input("Enter the sentence without space : ")

    uppLists = []
    stringList = []
    print("sentence before separate: ", getSentence)
    for i in range(len(getSentence)):
        if getSentence[i].isupper():
            uppLists.append(i)
    uppLists.append(len(getSentence))

    i = 0
    while i < len(uppLists) - 1:
        startLimit = int(uppLists[i])
        endLimit = int(uppLists[i + 1])
        stringList.append(getSentence[startLimit: endLimit])
        i += 1
    print("sentence after separated: ", end="")
    for i in range(len(stringList)):
        if i == 0:
            print(stringList[i] + ' ', end="")
        else:
            print(stringList[i].lower() + " ", end="")

main()