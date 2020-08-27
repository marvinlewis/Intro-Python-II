from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

"""
player is outside and wants to move in a direction


"""


player1 = Player("marvin", room['outside'])

    

# Write a loop that:

while True: 
#
# * Prints the current room name

    print(player1.current_room)
# * Prints the current description (the textwrap module might be useful here).
    print(player1.current_room.description)
# * Waits for user input and decides what to do.
    user_input = input("Choose a direction: (n, s, e, w) ")
# If the user enters a cardinal direction, attempt to move to the room there.
    if user_input == "n":
        if player1.current_room.n_to is not None:
            player1.current_room = player1.current_room.n_to
        else:
            pass
    if user_input == "s":
        if player1.current_room.s_to is not None:
            player1.current_room = player1.current_room.s_to
        else:
            pass
    if user_input == "w":
        if player1.current_room.w_to is not None:
            player1.current_room = player1.current_room.w_to
        else:
            pass
    if user_input == "e":
        if player1.current_room.e_to is not None:
            player1.current_room = player1.current_room.e_to
        else:
            pass
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if user_input == "q":
        break


#create room class with name and description
#north of player1 is the foyer.. player one is currenlty in the outside room
#if he moves "n" or north he enters the "foyer"