# Hangman Game 
import random 
from collections import Counter 
  
gamewords = '''dictionary love beer friends food shoes prince stellar greater
adrenaline infinite program treason lawyer prayer forever ideas mongoose playboy'''
  
def select_word(gamewords):
    return random.choice(gamewords)

print(select_word(gamewords))