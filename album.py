#!/usr/bin/env python3
# RyanWaltersDev Jun 25 2021 -- TIY 8-7

# Initial Function
def make_album(artist, album_title, year=None, number_of_songs=None):
    '''Return album dictionary'''
    album = {'artist': artist, 'album title': album_title}
    if year:
        album['year'] = year
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album

# Function Calls
album = make_album('nujabes', 'modal soul')
print(album)
album = make_album('gorillaz', 'demon days', year=2005)
print(album)
album = make_album('flying lotus', 'flamagra', year=2019, number_of_songs=27)
print(album)

# While loop for user input
while True:
    print("\nPlease enter the artist and album title for your favorite album.")
    print(f"(Enter 'quit' at any time to exit the program.)")
    artist = input("Artist: ")
    if artist == 'quit' or artist == 'Quit':
        break
    album_title = input("Album Title: ")
    if album_title == 'quit' or album_title == 'Quit':
        break

    album = make_album(artist, album_title)
    print(album)
    print(f"Your favorite album is {album_title} by {artist}? Cool!")

# END OF PROGRAM
