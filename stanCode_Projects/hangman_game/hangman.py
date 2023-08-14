"""
File: hangman.py
Name: You Nong HUANG
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
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
    The player has the only 7 chances to guess the hidden word.
    """
    true_ans = random_word()
    long = len(true_ans)
    # print(true_ans)
    # open it for test, or close to play.
    print('The word looks like: '+ '-'*long)
    print('You have 7 guesses left.')

    life = 7

    ans = '-'*long
    while True:
        guess = input('Your guess: ')
        guess = guess.upper()

        a = ''
        if len(guess) == 1 and guess.isalpha():
            if true_ans.find(guess) is not -1:
                print('You are correct!')
                for i in range(len(true_ans)):
                    if guess != true_ans[i]:
                        a = a + ans[i]
                    else:
                        a = a + guess
                ans = a
                if ans == true_ans:
                    print('You win!!')
                    print('The word was: '+true_ans)
                    break
                print(ans)
                print('You have '+str(life)+' guesses left')
            else:
                life = life -1
                if life == 0:
                    print('There is no ' + guess + '\'s in the word.')
                    print('You are completely hung : (')
                    print('The word was: '+true_ans)
                    break
                print(ans)
                print('There is no '+ guess+'\'s in the word.')
                print('You have '+str(life)+' guesses left.')
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


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
