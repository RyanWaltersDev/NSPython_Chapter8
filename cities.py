#!usr/bin/env python3
# RyanWaltersDev Jun 17 2021

# Initial function
def describe_city(city, country='australia'):
    '''Name city and corresponding country'''
    print(f"{city.title()} is in {country.title()}.")

describe_city('melbourne')
describe_city('sydney')
describe_city('del rio', 'brazil')

# END OF PROGRAM
