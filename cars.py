#!/usr/bin/env python3
# RyanWaltersDev Jun 29 2021 -- TIY 8-14

def make_car(manufacturer, model, **car_info):
    '''Make a dictionary about a car'''
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('toyota', 'camry', color='blue', year=2007)
print(car)

# END OF PROGRAM