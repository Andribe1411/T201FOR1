# Author: <Andri Benedikt>
# Date: <19.04.24>
# Project: <Lokapróf D2>

LIVES = 3
REMOVE_LIVES = 1 #lives that are removed when guessed wrong


def check_guess(guess,word):
    if guess in word:
        return True
    else:
        return False

def reveal_letters(word,guesses):
    correct_letters = ""
    for letter in word:
        correct = False
        for x in guesses:
            if x == letter:
                correct_letters += x+" "
                correct = True
        if correct == False:
            correct_letters += "_ "

    return correct_letters

correct_word = input("The secret word: ").upper()
print()
correct_guessed_letters = len(correct_word)*"_ "
guessed_letters = []
lives_remaining = LIVES

on = True
while on:
    print(f"Lives: {lives_remaining}/{LIVES}")
    print("Word:", correct_guessed_letters)
    if guessed_letters == []:
        print("Guesses: ")
    else:
        print("Guesses: ",end="")
    guessed_letters = sorted(guessed_letters)
    for x in guessed_letters:
        if x == guessed_letters[-1]:
            print(x)
        else:
            print(x,end=",")
    
    word_correct = True
    for test_letter in correct_word:
        if test_letter not in correct_guessed_letters:
            word_correct = False
        

    if word_correct:
        print("Congratulations, you won!")
        break
    elif lives_remaining == 0:
        print("Sorry, you lost")
        break


    guess = input("Guess a letter: ").upper()
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    if check_guess(guess,correct_word):
        print("Correct guess!")
        correct_guessed_letters = reveal_letters(correct_word,guessed_letters)
    else:
        print("Sorry, wrong guess")
        lives_remaining -= REMOVE_LIVES 
    print()
    