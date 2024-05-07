# Household Chores Delegator.

# Psedocode.
# Ask how many people live in the house
# For the relevant number of people, get their names along with ages and hours available per week.
# Store names, ages and available times into person specific data storage.
# Ask user to input jobs to delegate, along with this their difficulty on a 1-4 scale and time required.
# Once all information is received delegate and display the jobs back to the user.

# Welcome user to the program and explain it's function.
print('Welcome to the Household Chores Delegator, the fair way to split the housework!')
# Prompt user to enter number of people living in the house.
num_people = int(input('Please enter number of people living in the house 1-4: '))
# Iterate through number of occupants asking for their names, assign back to variables in person_list.
person_list = []
for person in range(1, num_people + 1):
    name = input(f'Enter name of Person {person}: ')
    person_list.append(name)
# Prompt user to enter information for each person, including time available per week and age.
time_list = []
age_list = []
for person in person_list:
    time = input(f'Enter weekly time available for {person} 0-40hrs: ')
    age = input(f'Enter age for {person} 15-40: ')
    time_list.append(time)
    age_list.append(age)
# Zip lists together into name, time available and age for each person.  
people_zipped_list = zip(person_list, time_list, age_list)


# Prompt user to enter number of chores that need doing.
num_chores = input('Enter number of chores that need doing {num_people} max: ')
# Iterate through chores to obtain difficulty and time required data.

