# Hangman Game 
import random 
# imports counter to couunt number of occurrence of each letter in word
from collections import Counter 

# defines a list of words to be used in the game  
gamewords = ['dictionary', 'love', 'beer', 'friends', 'food', 'shoes', 'prince', 'stellar', 'greater',
'adrenaline', 'infinite', 'program', 'treason', 'lawyer', 'prayer', 'forever', 'ideas', 'mongoose', 'playboy']

# function that randomly selects a word from the list and
def select_word(gamewords):
    return random.choice(gamewords)

# prints randomly chosen word from the list
print(select_word(gamewords))

# an integer that represents number of remaining attempts
# 6 representing (head + body +arms + legs)
remaining_attempts = 6

# displays all letters guessed by the user thar are in 'secret' word 
guessed_letters = ""

