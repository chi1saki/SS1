#Python program to convert an input string to Morse code
def convert(string):
    #Morse dictionary presenting
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.'}
    stringoutput = "";
    #step through characters in string
    for i in string:
        #add more code in string
        if (i==' '):
            stringoutput += 1;
        else:
            stringoutput += MORSE_CODE_DICT[i]+' '
    return stringoutput
def main():
    #main method
    string = str(input("Enter a string: "))
    print("Morse Translation: "+ convert(string))

main()

