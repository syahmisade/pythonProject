import random
import string
from words import words 

#Need to read back everything because I still dont understand perfectly ;(

def get_word(words):
    word = random.choice(word) #will be choosing random word
    while '-' in word and ' ' in word:
        word = random.choice(word)
    return word.upper()

def hangman():
    word = get_word(words)
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting user input
    while len(letters) > 0:
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)

        elif letters in used_letters:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again.')
