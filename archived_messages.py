#!/usr/bin/env python3
# RyanWaltersDev Jun 26 2021 -- TIY 8-9

def send_messages(unsent_messages, sent_messages):
    '''
    Prints each text message in the list.
    Moves sent messages to new list.
    '''
    print("Here's a list of sample text messages:")
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"\n{message}")
        sent_messages.append(message)

# Message list define and function call
message_list = ["Hello!", "How's it going?", "Hope you're doing well!"]
sent_list = []
send_messages(message_list[:], sent_list)

# Test to be sure lists are moved
print(message_list)
print(sent_list)

# END OF PROGRAM
