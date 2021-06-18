#!/usr/bin/env python3
# RyanWaltersDev Jun 17 2021 -- Return simple value

# Initial function
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# END OF PROGRAM
