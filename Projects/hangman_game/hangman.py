"""
File: hangman.py
Name: Hui-Chieh Chen
-----------------------------
This program plays hangman game. First, users will see a number of dashes
equivalent to the number of letters in the secret word. Users input one
letter each round, if the suggested letter occurs in the secret word,
this program fills in the letter in the right places and shows the updated
word on console. Users have N_TURNS chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Implement hangman game that lets users try to figure out the secret word
    Users have N_TURNS chances for error
    """
    secret_word = random_word()
    life = N_TURNS
    temp_ans = ''
    for i in range(len(secret_word)):  # Produce the same number of dashes as the number of letters in secret word
        temp_ans += "-"
    print("The word looks like: "+temp_ans)
    print("You have "+str(life)+" guesses left.")
    while True:
        input_ch = input("Your guess: ")
        guess = ''
        if input_ch.isalpha() and len(input_ch) == 1:  # Ensure input is not digits, symbols and more than one letter
            input_ch = input_ch.upper()  # Case-insensitive
            if input_ch not in secret_word:  # Wrong guess
                life = wrong_guess(input_ch, life)
                if life == 0:  # Failed
                    print("You are completely hung : (")
                    print("The word was: " + secret_word)
                    break
                else:
                    print("The word looks like: " + temp_ans)
                    print("You have " + str(life) + " guesses left.")
            else:
                guess = correct_guess(input_ch, secret_word, guess)
                temp_ans = update(temp_ans, guess)
                print("You are correct!")
                if temp_ans.isalpha():  # Win
                    print("You win!!")
                    print("The word was: "+temp_ans)
                    break
                else:
                    print("The word looks like: "+temp_ans)
                    print("You have "+str(life)+" guesses left.")
        else:
            print("illegal format.")


def wrong_guess(input_ch, life):
    """
    Less one chance to make wrong guess
    """
    life -= 1
    print("There is no " + input_ch + "'s in the word.")
    return life


def correct_guess(input_ch, secret_word, guess):
    """
    Fill in the correct letter in the right places of the secret word
    """
    for ch in secret_word:
        if input_ch == ch:
            guess += input_ch
        else:
            guess += "-"
    return guess


def update(temp_ans, guess):
    """
    Update the newly guessed letter to the word displayed on console
    """
    ans = ''
    for i in range(len(temp_ans)):
        ch = temp_ans[i]
        if ch.isalpha():
            ans += ch
        else:
            ans += guess[i]
    return ans


def random_word():
    """
    Randomly provide a word
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
