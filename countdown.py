"""Countdown Game Simulator"""
import random  #imports random to use choice to choose the random letters
from itertools import combinations  #used to find possible letter combinations
import time  #used for the countdown timer
CHARACTERS = []  #list of the characters currently chosen
def select_characters():
    """Allows to user to choose what type of letters they want"""
    consonants = ['b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'f',
                  'f', 'g', 'g', 'g', 'h', 'h', 'j', 'k', 'l', 'l', 'l', 'l',
                  'l', 'm', 'm', 'm', 'm', 'n', 'n', 'n', 'n', 'n', 'n', 'n',
                  'n', 'p', 'p', 'p', 'p', 'q', 'r', 'r', 'r', 'r', 'r', 'r',
                  'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's',
                  't', 't', 't', 't', 't', 't', 't', 't', 't', 'v', 'w', 'x',
                  'y', 'z']  #list of all consonants with the distribution
    #weighted
    vowels = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
              "a", "a", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e",
              "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "i", "i", "i",
              "i", "i", "i", "i", "i", "i", "i", "i", "i", "i", "o", "o", "o",
              "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "u", "u", "u",
              "u", "u"]  #list of all vowels with the distribution weighted
    del CHARACTERS[:]  #clears the list of characters to start over
    i = 1
    while i < 10:  #loop to stop asking for inputs after 9
        corv = input("Please enter c for a consonant or v for a vowel, this is"
                     " letter number " + str(i) + ": ")
        #asks the user for an input of c or v
        if corv == "c": #if statement for an input of c
            CHARACTERS.append(random.choice(consonants))  #uses random.choice
            #and appends the character list with a random consonant
            i += 1  #adds 1 each time to count to 9
        elif corv == "C":  #if statement for an input of C
            CHARACTERS.append(random.choice(consonants))  #uses random.choice
            #and appends the character list with a new random consonant
            i += 1  #adds 1 each time to count to 9
        elif corv == "v":  #elif statement for an input of v
            CHARACTERS.append(random.choice(vowels))  #uses random.choice to
            #append the character list with a random vowel
            i += 1 #adds 1 to i each time
        elif corv == "V":  #elif statement for an input of V
            CHARACTERS.append(random.choice(vowels))  #uses random.choice to
            #append the character list with a random vowel
            i += 1  #adds 1 to i each time
        else:
            print("Please enter c or v only")  #if c or v not input asks the
            #user to retry
    print(",".join(CHARACTERS))  #prints the characters as a string
    #seperated by commas for the user to see
    return CHARACTERS

WORD_LIST = []
def dictionary_reader(filename):
    """Reads the text file into word_list and remove the newlines"""
    with open(filename) as text:  #opens the file in the argument
        WORD_LIST[:] = text.read().splitlines()  #reads the file into word_list
        #and removes the new lines between each word
        return WORD_LIST

HITS = []
def word_lookup():
    """Sorts the characters chosen and compares them to the sorted characters
    of the words in the text file and adds ones that appear in both to the hits
    list"""
    test_letters = "".join(CHARACTERS)  #sorts the letters
    sorted_word = "".join(sorted(test_letters))  #starting with the longest
    #letter string count down to zero
    sorted_word_list = list()  #creates an empty list
    for word in WORD_LIST:  #iterates through each entry in word_list
        sorted_word_list.append("".join(sorted(word)))  #appends the sorted
        #words to this list
    for i in range(len(sorted_word), 0, -1):  #for each length of letter
        #strings generate all possible combinations
        for substring_letters_list in combinations(sorted_word, i):  #for each
            #combination of letters convert list to string
            substring_letters = "".join(substring_letters_list)  #joins the
            #strings into a list
            if substring_letters in sorted_word_list:  #compares the sorted
                #characters to the sorted words
                index = sorted_word_list.index(substring_letters)  #records
                #the index number of the matching words
                HITS.append(WORD_LIST[index])  #appends the list "hits" with
                #the words of the corresponding index numbers
    return HITS

if __name__ == "__main__":
    print("""
 #####  ####### #     # #     # ####### ######  ####### #     # #     # 
#     # #     # #     # ##    #    #    #     # #     # #  #  # ##    # 
#       #     # #     # # #   #    #    #     # #     # #  #  # # #   # 
#       #     # #     # #  #  #    #    #     # #     # #  #  # #  #  # 
#       #     # #     # #   # #    #    #     # #     # #  #  # #   # # 
#     # #     # #     # #    ##    #    #     # #     # #  #  # #    ## 
 #####  #######  #####  #     #    #    ######  #######  ## ##  #     # """)
     #prints an ascii introduction
    print("""
           Welcome to Countdown, lets begin!""")  #prints an intro message
    select_characters()  #runs the fucntion to choose letters
    dictionary_reader("words.txt")  #reads the file into word_list
    CLOCK = 30  #sets a variable clock at 29
    print("You have 30 seconds to think of an answer starting now!")
    while CLOCK > 1:
        time.sleep(5)  #waits 5 seconds
        CLOCK -= 5  #removes 5 from clock
        print("Time remaining: " + str(CLOCK) + " seconds")  #prints the
       #remaining time
    word_lookup()  #compares the words to find the matches
    USER_WORD = input("Please enter your answer: ")  #asks the user for an
    #answer as an input
    if USER_WORD in HITS:  #checks if the users answer is correct
        print("That is a correct answer! You scored ", str(len(USER_WORD)),
              " points!")  #prints the users sore if correct
    else:
        print("Sorry, that is not a valid word! You scored 0 points")  #prints
        #if the user did not have a correct answer
    if HITS:  #if there were any correct answers
        BEST_SCORE = max(len(x) for x in HITS)  #finds the longest word length
        BEST_WORDS = [x for x in HITS if len(x) == BEST_SCORE]  #find the words
        #that have the same length as the longest length
        BEST_WORDS = list(set(BEST_WORDS))  #converts best_words to a set to
        #remove duplicates before converting it back to a list
        if len(BEST_WORDS) > 1:  #if there are more than one best word
            print("The best words available were:", str(BEST_WORDS), " for ",
                  str(BEST_SCORE), " points")  #prints if >1 best word
        else:
            print("The best word available was:", str(BEST_WORDS), " for ",
                  str(BEST_SCORE), " points")  #prints if only 1 best word
