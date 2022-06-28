import random

#Choices a random word for us of length word_length from lines
def get_word(word_length, lines):
    words = [word for word in lines if len(word) == word_length]
    word = random.choice(words)
    return word

def draw(guess, num_guess, guessed_letters, wrong_letters, secret_word):
    progress = list()
    if num_guess == 0:
        print(r"""
            |-------|
            |       
            |       
            |      
            |
        ---------
        """)
    
    elif num_guess == 1:
        print(r"""
            |-------|
            |       O
            |       
            |      
            |
        ---------
        """)
    elif num_guess == 2:
        print(r"""
            |-------|
            |       O
            |       |
            |      
            |
        ---------
        """)
    elif num_guess == 3:
        print(r"""
            |-------|
            |       O
            |      -|
            |      
            |
        ---------
        """)
    elif num_guess == 4:
        print(r"""
            |-------|
            |       O
            |      -|-
            |      
            |
        ---------
        """)
    elif num_guess == 5:
        print(r"""
            |-------|
            |       O
            |      -|-
            |      / 
            |
        ---------
        """)
    
    elif num_guess == 6:
        print(r"""
            |-------|
            |       O
            |      -|-
            |      / \
            |
        ---------
        """)
        again = input(f"You lost! The word was: {secret_word}. Press Q to quit or any key to play again: ")
        if again == "Q" or again == "q":
            return -1
        else:
            return 2
    for letter in secret_word:
        if letter in guessed_letters:
            progress.append(letter)
        else:
            progress.append("_")
    progress.pop()

    print(f"  {progress}")
    print(f"  GUESSED LETTERS: {wrong_letters}")
    print('\n')
    
    return progress
    

    