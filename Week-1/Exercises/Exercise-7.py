"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint

def computer():
    while True :
        guess = randint(1, 100)
        print('Is it ' + str(guess) + '?')
        answer = input('press "y" or "n": ')
        if answer == 'n':
            print('Hmmm lemme try again...')
        else :
            print('Found it!')
            break
    


print('Think of a number between 1 and 100, press enter when you are ready !')
input()
print('I will now try to guess what number it is')
computer()