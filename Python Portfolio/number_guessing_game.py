import random

def replay():
    
    while True:
        play_again = input('Would you like to play again? Y/N: ')

        if play_again == 'Y':
            main_game()
        elif play_again == 'N':
            print('Thanks for playing the number guessing game, goodbye!')
            break
        else:
            print('Invalid entry, enter either Y or N.')

def main_game():

    print('Welcome to the number guessing game.')
    print('You have 10 chances to guess the secret number between 1-100.')

    attempt = 1
    max_attempts = 10
    secret_number = random.randrange(1, 101)

    while attempt <= max_attempts:
        try:
            guess = int(input(f'Attempt: {attempt}, Enter Guess: '))
            if guess < 1 or guess > 100:
                print('Please enter a value between 1-100.')
                continue

        except ValueError:
            print('Please enter an integer value.')
            continue


        if 1 <= guess < secret_number:
            print('Too low, try a higher number!')
        elif secret_number < guess <= 100:
            print('Too high, try a lower number!') 
        elif guess == secret_number:
            print(f'Congratulations, you guessed the number to be {secret_number} in {attempt} attempts!')
            replay()
            break
        else:
            print('Invalid entry, guess a number between 1-100.')
            continue

        attempt += 1 

    if attempt > max_attempts:
        print(f'Unfortunately you ran out of attempts, the secret number was {secret_number}.')
        replay()

main_game()
