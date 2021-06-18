#!/usr/bin/env python3
# RyanWaltersDev Jun 17 2021 -- Positional Arguments

# Initial function
def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Positional Arguments
describe_pet('cat', 'bonzo')
describe_pet('cat', 'chihiro')

# Keyword arguments
describe_pet(animal_type='cat', pet_name='bonzo')
describe_pet(pet_name='chihiro', animal_type='cat')

# Default Value
def describe_pet(pet_name, animal_type='cat'):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='bonzo')

# Call without default value
describe_pet(pet_name='allister', animal_type='snail')

# A cat named Chihiro
describe_pet('chihiro')
describe_pet(pet_name='chihiro')

# A frog named Phillip
describe_pet('phillip', 'frog')
describe_pet(pet_name='phillip', animal_type='frog')
describe_pet(animal_type='frog', pet_name='phillip')

# END OF PROGRAM
