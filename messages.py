#!/usr/bin/env python3
# RyanWaltersDev Jun 26 2021 -- TIY 8-9

def show_messages(messages):
    '''Prints each message in the list'''
    print("Here's a list of sample text messages:")
    for message in messages:
        print(f"\n{message}")

message_list = ["Hello!", "How's it going?", "Hope you're doing well!"]
show_messages(message_list)

# END OF PROGRAM
