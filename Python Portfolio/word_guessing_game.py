import random

word_list = ['apple', 'banana', 'cherry', 'pear', 'kiwi', 'avocado']
secret_word = random.choice(word_list)

def replay():
    while True:
        answer = input('Would you like to play again? Y/N: ')
        if answer == 'Y':
            game_start()
        elif answer == 'N':
            print('Thanks for playing the word guessing game!')
            break
        else:
            print('Invalid entry')

def display_word(secret_word, guessed_letters, attempt):
    print(f'Attempt: {attempt}')
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter + ' ', end='')
        else:
            print('_ ', end='')
    print()

def game_start():
    attempt = 1
    max_attempts = 10
    guessed_letters = []

    print('Welcome to the word guessing game!')
    print(f'You have {max_attempts} attempts to guess the word')

    while attempt <= max_attempts:
        display_word(secret_word, guessed_letters, attempt)

        guess = input('Guess a letter in the word: ')
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Enter a single letter character.')
            continue
        
        if guess in guessed_letters:
            print('You have already guessed that letter.')
            continue 

        if guess in secret_word:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(secret_word):
                print(f'Well done, you have successfully guessed the word {secret_word}!')
                replay()
                break
            print('Well done, you have successfully guessed a letter in the word.')
        else:
            guessed_letters.append(guess)
            print('Unfortunately the guessed letter isn\'t part of the word.')

        if set(guessed_letters) == set(secret_word):
            print(f'Well done, you have successfully guessed the word {secret_word}!')
            break

        attempt += 1
    
    if attempt > max_attempts:
        print('Unfortunately, you have run out of attempts!')
        print(f'The secret word was {secret_word}.')
        replay()

game_start()
