#main method definition
if __name__ == '__main__':
    #insert the name
    name = input("Enter your full name: ")
    #split the name
    n=name.split()
    print("The initials is: ")
    for str in n:
        #print output
        print(str[0], ". ", sep='', end='')
    print()
main()