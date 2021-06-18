#/usr/bin/env python3
# RyanWaltersDev Jun 17 2021 - TIY 8-3 and TIY 8-4

# Initial function
def make_shirt(size, text):
    '''Print summary of shirt.'''
    print(f"The shirt will be a size {size.title()} and say {text.title()}.")

make_shirt('large', "wu tang clan ain't nuttin ta fuck wit")
make_shirt(text="wu tang clan ain't nuttin ta fuck wit", size='large')

# Default value
def make_shirt(size='large', text='I love Python'):
    '''Print summary of shirt.'''
    print(f"The shirt will be a size {size.title()} and say {text}.")

make_shirt()
make_shirt('medium')
make_shirt(size='small', text='I love Javascript')

# END OF PROGRAM
