'''Rock, Paper and Scissors game'''

# Iterate through 5 games and print out winner at the end.
game_num = 1
computer_wins = 0
user_wins = 0

# Introduce the user to the game.
print('Welcome to Rock, Paper and Scissors!')

while game_num <= 5:

    # Make the computer randomly choose an option from a list.
    import random
    choice_list = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choice_list)

    # Get the user to input their choice.
    while True:
        user_choice = input(f'Game#{game_num} - Enter Rock, Paper or Scissors: ')
        if user_choice not in choice_list:
            print('Enter Rock, Paper or Scissors!')
            user_choice = input('Enter Rock, Paper or Scissors: ')
        else:
            break

    # Computer vs User, evaluate the winner and display outcome. 
    def declare_winner(computer_choice, user_choice):
        if computer_choice == user_choice:
            return 'Tie'
        elif (computer_choice == 'Rock' and user_choice == 'Scissors') or \
            (computer_choice == 'Paper' and user_choice == 'Rock') or \
            (computer_choice == 'Scissors' and user_choice == 'Paper'):
            return 'Computer Won'
        else:
            return 'User Won'

    print(declare_winner(computer_choice, user_choice))

    # Update running counter with number of wins for each side.
    if declare_winner(computer_choice, user_choice) == 'User Won':
        user_wins += 1
        game_num += 1
    elif declare_winner(computer_choice, user_choice) == 'Computer Won':
        computer_wins += 1
        game_num += 1
    else:
        pass



if computer_wins > user_wins:
    result = 'Computer'
else:
    result = 'User'


print(f'After playing 5 games in total, the winner is {result}.')