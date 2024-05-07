# Maths Calculator.

def add(num1, num2):
    result = num1 + num2
    print(result)

def subtract(num1, num2):
    result = num1 - num2
    print(result)

def multiply(num1, num2):
    result = num1 * num2
    print(result)

def divide(num1, num2):
    result = num1 // num2
    print(result)

while True:
    print('Welcome to the maths calculator.')
    print('Please choose an option from the list below.')
    print('1. Add Numbers.')
    print('2. Subtract Numbers.')
    print('3. Multiply Numbers.')
    print('4. Divide Numbers.')
    print('5. Exit')
    choice = input('Enter choice: ')

    if choice == '1':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        add(num1, num2)

    elif choice == '2':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        subtract(num1, num2)

    elif choice == '3':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        multiply(num1, num2)

    elif choice == '4':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        divide(num1, num2)

    elif choice == '5':
        print('Thanks for using the maths calculator, goodbye!')
        break

    else:
        print('Invalid entry, please enter a choice 1-5.')