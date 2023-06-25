"""
File: hangman.py
Name: Sean Chen
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Play the hangman game.
    """
    ans = random_word()
    guess = '_' * len(ans)
    n = N_TURNS
    print('The word looks like ' + guess)
    print('You have ' + str(n) + ' wrong guesses left.')
    while True:
        ch = input('Your guess: ').upper()
        if ch.isalpha() and len(ch) == 1:  # checking of whether inputted guess is correct format
            if ans.find(ch) == -1:  # checking if inputted guess is included in the answer
                print('There is no ' + ch + '\'s in the word.')
                n -= 1
            else:
                i = ans.find(ch)
                while i != -1:  # find all inputted guesses in the answer
                    guess = guess[:i] + ch + guess[i+1:]
                    i = ans.find(ch, i+1)
                print('You are correct!')
            if n == 0:  # checking if N_TURNS are exhausted
                print('You are completely hung : (')
                print('The word was: ' + ans)
                break
            if guess == ans:  # checking if user win the game
                print('You win!!')
                print('The word was: ' + ans)
                break
            print('The word looks like ' + guess)
            print('You have ' + str(n) + ' wrong guesses left.')
        else:
            print('Illegal format.')


def random_word():
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


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
