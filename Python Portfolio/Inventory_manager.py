# Inventory Management System.

# Initialise inventory dictionary to store relevant information.
inventory = {}
# Create definitions for main three required functions.
def add_product(product, price, quantity):
    inventory[product] = {'Quantity': quantity, 'Price': price}
    print(f'Product {product} added to Inventory, with a price of £{price} at a quantity of {quantity}.')

def remove_product(product):
    if product not in inventory:
        print(f'Product {product} not in Inventory.')
    else:
        del inventory[product]
        print(f'Product {product} removed from Inventory.')

def adjust_product(product, price, quantity):
    if product not in inventory:
        print(f'Product {product} not in Inventory.')
    else:
        inventory[product] = {'Price': price, 'Quantity': quantity}
        print(f'Product {product} updated with a quantity of {quantity} and a price of £{price}')

def view_products():
    if not inventory:
        print('Inventory System Empty!')
    else:
        print('Current Inventory:')
        for product, details in inventory.items():
            print(f"Product: {product}, Price: {details['Price']}, Quantity: {details['Quantity']}")

# Present options to the user to interact with the inventory tool.
while True:
    print('Welcome to the Inventory Management system.')
    print('Please choose an option from the list below.')
    print('1. Add a Product.')
    print('2. Remove a Product.')
    print('3. Adjust a Product.')
    print('4. View Products.')
    print('5. Exit.')
    choice = input('Enter Choice: ')

    if choice == '1':
        product = input('Enter Product Name: ')
        price = input('Enter Product Price: ')
        quantity = input('Enter Product Quantity: ')
        add_product(product, price, quantity)

    elif choice == '2':
        product = input('Enter Product Name: ')
        remove_product(product)

    elif choice == '3':
        product = input('Enter Product Name: ')
        price = input('Enter Product Price: ')
        quantity = input('Enter Product Quantity: ')
        adjust_product(product, price, quantity)

    elif choice == '4':
        view_products()

    elif choice == '5':
        print('Thanks for using the Inventory Management System.')
        break

    else:
        print('Invalid entry, please make a choice 1-5.')

