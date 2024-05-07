# House Chores Delegator.

# Initialise empty dictionaries to store collected data.
occupants = {}
chores = {}

# Define function to add occupants and their information.
def add_occupant(name, age, time):
    occupants[name] = {'Age': age, 'Time': time}
    print(f'Occupant {name} added to house.')

# Define function to add chores and their information.
def add_chore(chore, time, difficulty):
    chores[chore] = {'Time': time, 'Difficulty': difficulty}
    print(f'Chore {chore} added to list.')

# Define function to view all occupants of the house.
def view_occupants():
    print('Current Occupants: ')
    for name in occupants.keys():
        print(name)

# Define function to view all Chores on the list.
def view_chores():
    print('Current Chores: ')
    for chore in chores.keys():
        print(chore)

# Define function to delegate the chores based on age, with the youngest taking on the easiest chores.
def sort_age():
    age_sorted = sorted(occupants.items(), key=lambda x: x[1]['Age'])
    difficulty_sorted = sorted(chores.items(), key=lambda x: x[1]['Difficulty'])
    
    for (occupant, occupant_data), (chore, chore_data) in zip(age_sorted, difficulty_sorted):
        print(f'Occupant {occupant} will complete job {chore}.')


# Define function to delegate the chores based on time, with those which have the most time free taking on the longest tasks.
def sort_time():
    time_sorted =  sorted(occupants.items(), key=lambda x: x[1]['Time'])
    print(time_sorted)

print('Welcome to the Chores Delegator, the fair way to split the work!')

while True:
    print('Please choose an option from the list below.')
    print('1. Add Household Occupant.')
    print('2. Add Household Chore')
    print('3. View all Occupants.')
    print('4. View all Chores.')
    print('5. Sort via Age.')
    print('6. Sort via Time.')
    print('7. Exit')
    choice = input('Enter Choice: ')

    if choice == '1':
        name = input('Enter Housemate Name: ')
        age = int(input('Enter Housemate age (15-50yrs old): '))
        time = int(input('Enter Housemate free time (5-40hrs Weekly): '))
        add_occupant(name, age, time)

    elif choice == '2':
        chore = input('Enter Chore Title: ')
        time = int(input('Enter Chore time to complete (20-60mins): '))
        difficulty = int(input('Enter chore difficulty level 1-3 (low-high): '))
        add_chore(chore, time, difficulty)

    elif choice == '3':
        view_occupants()

    elif choice == '4':
        view_chores()

    elif choice == '5':
        sort_age()

    elif choice == '6':
        sort_time()

    elif choice == '7':
        print('Thanks for using the chores delegator, goodbye.')
        break

    else:
        print('Invalid entry, enter a choice 1-7.')

