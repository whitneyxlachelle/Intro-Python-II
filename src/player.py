# Write a class to hold player information, e.g. what room they are in
# currently.

# Use the __init__() function to assign values to object properties

# Player Attributes: name, current_room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def take_item(self, item):
        # adding item to inventory 
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    
   