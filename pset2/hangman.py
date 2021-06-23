import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    correct = 0
    letters = set(letters_guessed)
    for letter in letters:
        if letter in secret_word:
            correct += 1
    if correct == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct_letters = []
    word = ""
    for letter in letters_guessed:
        if letter in secret_word:
            correct_letters.append(letter)
    for letter in secret_word:
        if letter in correct_letters:
            word += letter + " "
        else:
            word += "_ "
    return word
            


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    not_used = ""
    for char in alphabet:
        if char not in letters_guessed:
            not_used += char
    return not_used
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")

    unique = ''.join(set(secret_word))
    nunique_letters = len(unique)
    nguesses_left = 12

    letters_guessed = []
    warnings = 3

    while(not is_word_guessed(secret_word, letters_guessed) and nguesses_left != 0):

        available_letters = get_available_letters(letters_guessed)

        print(f"You have {nguesses_left} number of guesses left.")
        print(f"Available letters: {available_letters}")
        print(f"You have {warnings} warnings left")

        #require user to input letter and give them three false inputs before
        #docking a guess

        guess = input("Please Guess a Letter: ")

        if warnings != 1:
            if not guess.isalpha():
                word = get_guessed_word(secret_word, letters_guessed)
                print("Oops! That is not a valid letter. You have {warnigs} left: {word} ")
                warnings -= 1
                continue
            elif guess.lower() in letters_guessed:
                word = get_guessed_word(secret_word, letters_guessed)
                print("You've already guessed this letter. You have {warnings} left: {word} ")
                warnings -= 1
                continue
        else:
            if not guess.isalpha():
                word = get_guessed_word(secret_word, letters_guessed)
                print("Oops! That is not a valid letter. You have {warnigs} left: {word} ")
                warnings = 3
                nguesses_left -= 1
                continue
            elif guess.lower() in letters_guessed:
                word = get_guessed_word(secret_word, letters_guessed)
                print("You've already guessed this letter. You have {warnings} left: {word} ")
                warnings = 3
                nguesses_left -= 1
                continue

        letters_guessed.append(guess)
        #if correct letter gets inputted

        if guess in secret_word:
            word = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {word}")
        #if incorrect letter gets inputted

        else:
            word = get_guessed_word(secret_word, letters_guessed)
            print(f"Oops! That letter is not in my word: {word}")
            nguesses_left -= 1

    #When Loop termiantes because you guessed the word or you have no guesses left

    #Losing case
    if (not is_word_guessed(secret_word, letters_guessed) and nguesses_left == 0):
        print(f"Sorry you ran out of guesses. The word was {secret_word}")

    #Winning Case
    if (is_word_guessed(secret_word, letters_guessed)):
        print(f"Congradulations, you won!\nYour total score for this game is {nguesses_left * nunique_letters}")


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    """
    Check if my_word which also has spaces, matches in form with other_word
    """
    #delete spaces in myword. Length is the number of actual characters in my_word.
    my_word = my_word.replace(" ", "")
    length = 0
    match = 0
    #if the lengths are different immediatley return false
    if len(my_word) != len(other_word):
        return False

    #for character in incomplete word, find how many actual characters there are
    for char in my_word:
        if char == "_":
            pass
        else:
            length += 1

    #If the character at the same indexes for my_word and other_word match, increment match by one
    for key, value in enumerate(my_word):
        if value != "_":
            if value == other_word[key]:
                match += 1

    #only when all the characters not _ in my_word match with other_word return true
    if match == length:
        return True
    return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = ""
    for word in word_list:
        if match_with_gaps(my_word, word) == True:
            matches += word + " "
    return matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")

    unique = ''.join(set(secret_word))
    nunique_letters = len(unique)
    nguesses_left = 12

    letters_guessed = []
    warnings = 3

    while(not is_word_guessed(secret_word, letters_guessed) and nguesses_left != 0):

        available_letters = get_available_letters(letters_guessed)

        print(f"You have {nguesses_left} number of guesses left.")
        print(f"Available letters: {available_letters}")
        print(f"You have {warnings} warnings left")

        #require user to input letter and give them three false inputs before
        #docking a guess

        guess = input("Please Guess a Letter: ")

        if guess != "*":
            if warnings != 1:
                if not guess.isalpha():
                    word = get_guessed_word(secret_word, letters_guessed)
                    print(f"Oops! That is not a valid letter. You have {warnigs} left: {word} ")
                    warnings -= 1
                    continue
                elif guess.lower() in letters_guessed:
                    word = get_guessed_word(secret_word, letters_guessed)
                    print(f"You've already guessed this letter. You have {warnings} left: {word} ")
                    warnings -= 1
                    continue
            else:
                if not guess.isalpha():
                    word = get_guessed_word(secret_word, letters_guessed)
                    print(f"Oops! That is not a valid letter. You have {warnings} left: {word} ")
                    warnings = 3
                    nguesses_left -= 1
                    continue
                elif guess.lower() in letters_guessed:
                    word = get_guessed_word(secret_word, letters_guessed)
                    print(f"You've already guessed this letter. You have {warnings} left: {word} ")
                    warnings = 3
                    nguesses_left -= 1
                    continue
        elif guess == "*":
            word = get_guessed_word(secret_word, letters_guessed)
            print(show_possible_matches(word))
            continue

        letters_guessed.append(guess)
        #if correct letter gets inputted

        if guess in secret_word:
            word = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {word}")
        #if incorrect letter gets inputted

        else:
            word = get_guessed_word(secret_word, letters_guessed)
            print(f"Oops! That letter is not in my word: {word}")
            nguesses_left -= 1

    #When Loop termiantes because you guessed the word or you have no guesses left

    #Losing case
    if (not is_word_guessed(secret_word, letters_guessed) and nguesses_left == 0):
        print(f"Sorry you ran out of guesses. The word was {secret_word}")

    #Winning Case
    if (is_word_guessed(secret_word, letters_guessed)):
        print(f"Congradulations, you won!\nYour total score for this game is {nguesses_left * nunique_letters}")


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
