#!/usr/bin/env python3
# RyanWaltersDev Jun 25 2021 -- Return dictionary in function

# Initial function
def build_person(first_name, last_name, age=None):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name, 'last': last_name}
    '''Return age is specified'''
    if age:
        person['age'] = age
    return person

# Function call
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# END OF PROGRAM
