'''
Q.1) Write a program to implement Hangman game using python. Description: Hangman is a classic word-guessing game. The user should guess the word correctly by entering alphabets of the user choice. The Program will get input as single alphabet from the user and it will matchmaking with the alphabets in the original
[10 Marks]
'''

import random

def hangman():
    words = ['python', 'programming', 'algorithm', 'computer', 'science']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    print("Word:", ' '.join(guessed))
    
    while attempts > 0 and '_' in guessed:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts remaining.")
        
        print("Word:", ' '.join(guessed))
    
    if '_' not in guessed:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was: {word}")

hangman()
