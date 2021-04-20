"""
Hi guys, For this video today, we are implement a guessing game where the computer has a secret number and
we are trying to guess that secret number.
First
We need to have the computer generate a random number for us to guess.
"""
# import random number - a package that comes with python and makes it avalible in our script
import random


# creating a function
def guess():
    # asking the user their name + greeting them
    name = input('What is your name? ')
    print('Hi, ' + name)
    # first step
    # generate a random number within the range of 1 - 10
    random_number = random.randint(1, 10)
    # telling python this variable exist. Zero because we don't want our guess to accidently equals the random number.
    # Also means the random number will never be zero.
    guess = 0
    # second step - to guess our number once the computer has a random number and input what our guess of the number is
    # and the computer will tell us whether its too high, low or if we guessed the number correctly.
    # We need to keep looping until we get the right answer - use while loop(needs an expression)
    # We want to stop this loop when our guess equals the random number.
    # Define guess on line 21.
    # if user guess is not correct move to the conditional statements
    while guess != random_number:
        # ask user to guess a number. Int, want our guesses to be integer
        guess = int(input('Guess a number between 1 and 10: '))
        # print if conditions are right / gives feedback that tells us if we are high or low or guessed it right
        if guess < random_number:
            print('Sorry, try again. Too low')
        elif guess > random_number:
            print('Sorry, try again. Too high')
        else:
            print(f'Wow, you have guessed the number {random_number} correctly')

"""
The __name__ is a special built-in variable which evaluates to the name of the current module.
However, if a module is being run directly (from command line), then __name__ instead is set to the string “__main__”.
python module is a file that has a .py extension
"""
# call function - The variable __name__ for this module is set to __main__
if __name__ == '__main__':
    guess()
