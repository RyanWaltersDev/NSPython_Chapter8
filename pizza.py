#!/usr/bin/env python3
# RyanWaltersDev Jun 26 2021

def make_pizza(size, *toppings):
    '''Print the list of customer's requested toppings'''
    print(f"\nCustomer has ordered a {size}-inch pizza with " 
        "the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperonni')
make_pizza(22, 'sausage', 'peppers', 'extra cheese')

# END OF PROGRAM
