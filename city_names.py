#!/usr/bin/env python3
# RyanWaltersDev Jun 25 2021 -- TIY 8-6

# Initial function
def get_city_country(city, country):
    '''Return neatly formatted city and country'''
    city_country = f"{city}, {country}"
    return city_country.title()

# Function calls
name = get_city_country('santiago', 'chile')
print(name)
name = get_city_country('cairo', 'egypt')
print(name)
name = get_city_country('cozumel', 'mexico')
print(name)

# END OF PROGRAM
