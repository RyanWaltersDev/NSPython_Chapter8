# RyanWaltersDev Jun 29 2021 -- TIY 8-12

def build_sandwich(*toppings):
    '''Print a list of sandwich toppings'''
    print(f"\nYou have ordered the following items on your sandwich:")
    for topping in toppings:
        print(f"\t\t\t~ {topping.title()} ~")

# END OF PROGRAM
