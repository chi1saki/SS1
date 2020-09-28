def main()
    getSentence = input("Enter the sentence : ")

    i = 0
    while i < len(getSentence):
        if i == 0:
            print(getSentence[i].upper(), end="")
        elif getSentence[i] == '.':
            print(". ", end="")
            print(getSentence[i + 2].upper(), end="")
            i += 2
        else:
            print(getSentence[i], end="")
            i += 1
main()