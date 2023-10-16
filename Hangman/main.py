import random
import string
from words import words 

def get_valid_word(words):
    word = random.choice(words) #randomly choose the words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #the letters that the users have guessed (huruf yang sudah diteka)

    while len(word_letters) > 0:
        
        #bangun dari tido, start dari sini

        user_letter = input('Guess the letter: ').upper() #the letter that the user give + quesstion for user (teka huruf)
        if user_letter in alphabet - used_letters: #if there is letter that the user havent guessed
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You already used the letter. Please try again.')
        
        else:
            print('Invalid character. Please try again.')
    
    #it will get here when the len(word_letters) == 0

