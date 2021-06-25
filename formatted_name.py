#!/usr/bin/env python3
# RyanWaltersDev Jun 17 2021 -- Return simple value

# Initial function
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Expand function to include middle name
def get_formatted_name(first_name, middle_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# Function with middle name not required
def get_formatted_name(first_name, last_name, middle_name=''):
    '''Return a full name, neatly formatted'''
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Middle_name argument must go last
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# END OF PROGRAM
