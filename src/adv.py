from room import Room
from player import Player
import textwrap

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
to north."""),

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

# Intro Message
def intro_message():
    print("Find Charles!")

intro_message()

# Make a new player object that is currently in the 'outside' room.
character = input("Hello human. What is your name? ")
location = room['outside']
player1 = Player(character, location)

# Write a loop that:
#-
while True:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    current_room = player1.current_room
    print(f"{player1.current_room.description}. You're currently in {player1.current_room.name}. \n")

# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
    choice = input("You can move [n, e, s, w] or press [q] to quit. Which way would you like to go? \n")

# If the user enters "q", quit the game.
    if choice == 'q':
        print("Bye, for now " + character)
        break
# Player is outside
    if choice == 'n':
        if hasattr(current_room, 'n_to'):
            player1.current_room = current_room.n_to
            print("You are now heading north... \n")
 
# Print an error message if the movement isn't allowed.           
        else: 
            print(f"{character}, you can't be here. Go Back! \n")
    
    elif choice == 'e':
        if hasattr(current_room, 'e_to'):
            player1.current_room = current_room.e_to
            print("You are now heading east... \n")
        else: 
            print(f"{character}, you can't be here. Go Back! \n")
    elif choice == 's':
        if hasattr(current_room, 's_to'):
            player1.current_room = current_room.s_to
            print("You are now heading south... \n")
        else: 
            print(f"{character}, you can't be here. Go Back! \n")
    elif choice == 'w':
        if hasattr(current_room, 'w_to'):
            player1.current_room = current_room.w_to
            print("You are now heading west... \n")
        else: 
            print(f"{character}, you can't be here. Go Back! \n")

# hasattr(): (object, name) <-- looks thru object to find specified name. RETURNS True or false