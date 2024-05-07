# Initialise an empty dictionary.
staff_register = {}

# Define required functions for program.

def add_staff(level, name, id, loyalty):
    if level not in staff_register:
        staff_register[level] = {}
    if name not in staff_register:
        staff_register[level][name] = {}
    staff_register[level][name]['ID Number'] = id
    staff_register[level][name]['Years of Loyalty'] = loyalty
    print(f'Staff member {name} added to register with level {level} ID Number {id} and a loyalty of {loyalty} years.')

def remove_staff(name):
    for level in staff_register:
        if name in staff_register[level]:
            del staff_register[level][name]
            print(f'Staff member {name} removed from Staff Register.')
        else:
            print(f'Staff member {name} not in Staff Register!')

def check_details(name):
    for level in staff_register:
        if name in staff_register[level]:
            print(f'Staff member {name} found!')
            print('Staff information...')
            print(f'Level: {level}')
            print(f'Name: {name}')
            print(f'ID Number: {staff_register[level][name]['ID Number']}')
            print(f'Loyalty Years: {staff_register[level][name]['Years of Loyalty']}')
        else:
            print(f'Staff member {name} not in Staff Register.')


# Present user with options, and prompt to enter choice. 
print('Welcome to the staff register, helping you manage your employees.')

while True:
    print('Please choose an option from the list below.')
    print('1. Add staff member.')
    print('2. Remove staff member.')
    print('3. Check staff details.')
    print('4. Exit')
    choice = input('Please Enter Choice: ')

    if choice == '1':
        level = input('Enter staff level (Board, Manager or employee): ')
        name = input('Enter staff members name: ')
        id = input('Enter staff ID Number (#6-Digits): ')
        loyalty = input('Enter years of loyalty to company: ')
        add_staff(level, name, id, loyalty)

    elif choice == '2':
        name = input('Enter staff members name: ')
        remove_staff(name)

    elif choice == '3':
        name = input('Enter staff members name: ')
        check_details(name)

    elif choice == '4':
        print('Thanks for using the staff register!')
        break

    else:
        print('Invalid entry, enter a choice (1-4)')
