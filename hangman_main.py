# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:21:10 2022

@author: Sumit
"""

import random
import hangman_pics
import words


choosen_word = random.choice(words.list_of_words)
hidden_word = []

for _ in choosen_word:
    hidden_word += "_"

print(hidden_word)

print("\nYou have 6 life.")

life = 6

while life > 0 and "_" in hidden_word:
    guess = input("__________________________________\nGuess a letter: ")
    for n in range(len(choosen_word)):
        if guess in choosen_word[n]:
            hidden_word[n] = guess

    print(hidden_word)

    if not guess in hidden_word:
        life -= 1
        print("\nOh no, you lose a life.")
        print(f"\nYou have {life} life remaining.")
    print(f"{hangman_pics.h_pics[life]}")
    if life == 0:
        print(f"Game Over, the word is {choosen_word}")
    if not "_" in hidden_word:
        print("\nYou Win")
