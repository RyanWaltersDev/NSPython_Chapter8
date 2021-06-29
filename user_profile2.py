#!/usr/bin/env python3
# RyanWaltersDev Jun 29 2021 -- TIY 8-13

def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user'''
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('ryan', 'walters',
                            location='georgia',
                            field='philosophy',
                            favorite_food='sushi',
                            hobby='music',
                            favorite_color='black')
print(user_profile)

# END OF PROGRAM
