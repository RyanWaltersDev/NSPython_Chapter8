#!/usr/bin/env python3
# RyanWaltersDev Jun 25 2021 -- Modifying a list in a function
from printing_functions import print_models
from printing_functions import show_completed_models

# Start with designs that need to be printed
unprinted_designs = ['phone case', 'rubix cube', 'dodecahedron']
completed_models = []

# Simulate printing each design until none are left
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Function call from import

unprinted_designs = ['phone case', 'rubix cube', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)

# END OF PROGRAM
