#Hangman Game
#Let player choose a word of length 1 - 15, or random length
#Build Hangman

import random
import helper_functions

with open("words.txt") as f:
    #Readlines returns lists of all words
    lines = f.readlines()

playing = True
#Game keeps running while playing == True
while playing:
    word_length = input(r'Choice a word length(or input "R" for random length): ')
    if word_length == "R" or  word_length == "r":
        word_length = random.randint(1, 15)
    elif word_length.isdigit() and int(word_length) in range(1, 15):
        pass
    else:
        print("Invalid Input!")
        continue
    
    #cast word_lenth into an int
    word_length = int(word_length) + 1
    #Assign word of length word_length to the secret word
    secret_word = helper_functions.get_word(word_length, lines)
    #Keep track of # of guesses(game over at 6)
    num_guess = 0
    #List of wrong guess letters
    wrong_letters = list()
    #List of correct guess letters
    guessed_letters = list()
    while num_guess <= 6:
        guess = input("Guess a letter: ")
        if guess.isalpha() is not True or len(guess) != 1:
            print("Invalid Guess")
            continue
        if guess in wrong_letters or guess in guessed_letters:
            print("Already guessed that letter.")
            continue
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            wrong_letters.append(guess)
            num_guess += 1
        progress = helper_functions.draw(guess, num_guess, guessed_letters, wrong_letters, secret_word)
        if progress == -1:
            playing = False
            break
        if progress == 2:
            break
        prog_len = [l for l in progress if l != "_"]
        #Check to see if user has guessed every letter
        if len(prog_len) == len(secret_word) - 1:
            again = input("You win! Press Q to quit or any key to play again: ")
            if again == "Q" or again == "q":
                playing = False
            break
        

    

    



