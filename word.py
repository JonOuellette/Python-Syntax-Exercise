def print_upper_words(words):
    """ Prints out each word uppercased and on a separate line
        For example: 
            print_upper_words(["Hello", "Hi"])
        
        should print:
        HELLO
        HI
    
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """ Prints only words that start with an e on a separate line and is uppercased
        For example: 
            print_upper_words(["eye", "Eddie", Hi])
        
        should print:
        EYE
        EDDIE
    """

    for word in words:
        if(word.startswith("e")) or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, starting_letter):
    for word in words:
        for letter in starting_letter:
            if (word.startswith(letter)):
                print (word.upper())

