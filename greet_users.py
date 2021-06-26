#!/usr/bin/env python3
# RyanWaltersDev Jun 25 2021 -- Passing a list through a function

# Initial function
def greet_users(names):
    '''Print a simple greeting to each user in the list'''
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# Define list and pass through function
usernames = ['brooke', 'ryan', 'dixon', 'jules']
greet_users(usernames)

# END OF PROGRAM
