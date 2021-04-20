# This is a sample number guessing game
# import random number
import random




# Ask user their name with greeting message
name = input('What is your name? ')
print('Hi ' + name)

# Generate a random number with a range from 0 - 10
x = random.randint(0, 10)

play_game = input('Would you like to play a guessing game? Yes/No ')

# This will then not start the game
#if play_game == 'no':
    #print(' You are scared and the game did not start yet haha')


# This will start the game
while play_game == 'yes' or 'Yes':

    # Prompt user to import their guess
    user = int(input("Enter your guess between 1 to 10: "))

#  conditional statement to print results

    # This will propmt user to enter a valid number within the given range
    if int(user) < 1 or int(user) > 10:
        print('Please enter a number within the given range')
    elif user == x:
        print('You got lucky and guessed right')
    else:
        print('Ha! Wrong guess!')


    playAgain = input('Would you like to play again? (Enter Yes/No) ')
    if playAgain == 'no':
        print('Okay, You are scared')
        break
    if playAgain == 'yes' or 'Yes':
        user = int(input("Enter your guess between 1 to 10: "))
        if user > x:
            print('The number is smaller')
        elif user < x:
            print('The number is bigger')
        elif user == x:
            print('You got it right!')
        else:
            print('You guessed wrong!')




'''
def start_game():
    randomNumber = int(random.randint(1, 10))
    print('Hi there! Welcome to my game of guesses')
    user = input('What is your name? ')
    wannaPlay = input('Hi, would you like to play my guessing game? (Enter yes/no) ' )
    while wannaPlay == 'yes':
            guess = str(input('Pick a number between 1 and 10 '))
            if int(guess) < 1 or int(guess) > 10:
                print('Please enter a number within the given range')
            else:
                if int(guess) == randomNumber:
                    print('Wow! How did you know')
                playAgain = input('Would you like to play again? (Enter Yes/No) ')
                randomNumber = int(random.randint(1, 10))
                if playAgain == 'no':
                    print('Okay, You''re scared')
                    break
                elif int(guess) > randomNumber:
                    print('The number is lower')
                elif int(guess) < randomNumber:
                    print('The number is higher')

    else:
        print('Wow ' + user + ',' + ' You are scared, smh')
if __name__ == '__main__':
    start_game()
'''



