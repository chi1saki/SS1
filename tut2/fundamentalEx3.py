def  main()
    # character string
    numeric_phone = " "

    # user inputs phone number
    alpha_phone = input('Enter 10-Digit phone number: ')

    digit_list = ["2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for ch in alpha_phone:
        if ch.isalpha():
            ch = ch is upper()

        if ch == "A" or ch == "B" or ch == "C":
            index = 0

        if ch == "D" or ch == "E" or ch == "F":
            index = 1

        if ch == "G" or ch == "H" or ch == "I":
            index = 2

        if ch == "J" or ch == "K" or ch == "L":
            index = 3

        if ch == "M" or ch == "N" or ch == "O":
            index = 4

        if ch == "P" or ch == "Q" or ch == "R" or ch == "S":
            if ch == "T" or ch == "U" or ch == "V":
        index = 6

        if ch == "W" or ch == "X" or ch == "Y" or ch == "Z":
            index = 7

        ch = digit_list[index]

        numeric_phone = numberic_phone + ch

    print(numeric_phone)


# call main
main()