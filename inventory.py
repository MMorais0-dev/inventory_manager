inventory = []

def show_inventory():
    if len(inventory) == 0:
        print('no products in inventory')
    else:
        print('\n---Current Inventory ---')
        for product in inventory:
            print(f"- {product['name']} | QTY: {product['quantity']} | Price: ${product['price']}")
        print('------------------------ \n')

def add_product():
    name = input('Product name:')
    quantity = int(input('Quantity:'))
    price = float(input('Price: $'))
    product = {'name': name, 'quantity': quantity, 'price': price}
    inventory.append(product)
    print(f"{name} added!")


def remove_product():
    name = input('Enter product name to remove:')
    for product in inventory:
        if product['name'] == name:
            inventory.remove(product)
            print(f'{name} removed!')
            return
    print('product not found.')

def main_menu():
    while True:
        print('\n--- Inventory Menu ---')
        print('1. Show inventory')
        print('2. Add product')
        print('3. Remove product')
        print('4. Quit')
        choice = input('Choose an option (1-4): ')
        if choice == '1':
            show_inventory()
        elif choice == '2':
            add_product()
        elif choice =='3':
            remove_product()
        elif choice == '4':
            print('Goodbye!')
            break
            
main_menu()