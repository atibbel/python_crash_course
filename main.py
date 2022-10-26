# Author: Amber Wonnenberg
# Project: Module 5
# Date compiled: September 9th, 2022

'''
This program will allow the user to create a grocery list, view the grocery list and
add and remove items from the list.
'''

continue_program = True

# Program will run until continue_program is False.
while continue_program:
    print("\n========================================================="
          "\n\t\t\t\tGrocery List"
          "\n=========================================================")

    print('\n1) Create a new Grocery List '
          '\n2) View List'
          '\n3) Add Item to List '
          '\n4) Remove Item From List '
          '\n\n=========================================================')

    menu_option = input("\nEnter an option or 'q' to quit. ")

    # A grocery_list list will be created.
    if menu_option == '1':
        grocery_list = []
        add_items = input("\nGrocery list created!"
                          "\nWould you like to add items now? Y or N ")
        # the user will be prompted to add item to their list until they type 'N'
        if add_items.upper() == 'Y':
            print("\nEnter grocery items. Type 'N' when done:")
            while add_items.upper() != 'N':
                grocery = input()
                if grocery.upper() == 'N':
                    break
                else:
                    grocery_list.append(grocery)

    # Display items in the list
    if menu_option == '2':
        for item in grocery_list:
            print(f'\n{item.title()}')

        view_list = input()

    # Add items to the list until user types 'N'
    if menu_option == '3':
        print("\nEnter grocery items. Type 'N' when done:")
        while True:
            grocery = input()
            if grocery.upper() == 'N':
                break
            else:
                grocery_list.append(grocery)

    # Remove item from list until user types 'N'. List will be displayed when the user is done removing items.
    if menu_option == '4':
        print("\nPlease enter the grocery item you would like to remove or 'N' when done: ")
        while True:
            remove_item = input()
            if remove_item.upper() == 'N':
                break
            else:
                grocery_list.remove(remove_item.lower())
                print(f'{remove_item.title()} has been removed from the list. \n')

        for item in grocery_list:
            print(f'{item.title()}')

        view_list = input()

    # Exit the program when menu_option is 'q'
    if menu_option.lower() == 'q':
        continue_program = False


