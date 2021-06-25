#!/usr/bin/env python3
# RyanWaltersDev Jun 17 2021

# Initial Function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# Function call
greet_user('brooke')

# Function with while loop
def get_formatted_name(first_name, last_name):
    '''Display a full name, neatly formatted.'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# While loop
while True:
    print("\nPlease tell us your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")


#END OF PROGRAM
