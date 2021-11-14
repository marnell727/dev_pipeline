choice = ''

with open('shopping_list.txt','wt') as shop_file:
    shop_file.write('''      Shopping List
-------------------------''')

print('''
Welcome to your shopping list program!
------------------------------------
''')

while choice != 'Q':
    choice = input('''
What would you like to do?
(P)rint the shopping list
(A)dd an item to the shopping list
(C)lear the shopping list
(Q)uit
''').upper()
    if choice == 'P':
        with open('shopping_list.txt') as shop_list:
            print('')
            print(shop_list.read())
    elif choice == 'A':
        new_item = input("What would you like to add? ('Return' to return to main menu) ").capitalize()
        if new_item != '':
            with open('shopping_list.txt','at') as shop_list:
                shop_list.write(f'\n- {new_item}')
                print('')
                print(f"'{new_item}' has been added to your shopping list.")
    elif choice == 'C':
        with open('shopping_list.txt','wt') as shop_list:
            shop_list.write('''      Shopping List
-------------------------''')
            print('Your shopping list has been cleared. ')
print('')
print('Goodbye!')