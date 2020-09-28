def main():
    string = input("Enter the string : ")
    charList = []
    occurList = []
    for ch in string:
        count = 0
        for i in range(len(string)):
            if ch == string[i]:
                count += 1
        if ch in charList:
            charList
            occurList
        else:
            charList.append(ch)
            occurList.append(count)
    print("character list : ", charList)
    print("corresponding occurance list :", occurList)
    print()
    mostfreChar = maxOccur(occurList, charList)
    if mostfreChar == " ":
        print(" most frequent character : space ")
    else:
        print(" most frequent character :", mostfreChar)


def maxOccur(list1, list2):
    largest = 0
    for i in range(len(list1)):
        find_lar = int(list1[i])
        if (largest <= find_lar):
            largest = find_lar

    for i in range(len(list1)):
        find_position = int(list1[i])
        if (find_position == largest):
            return list2[i]


main()