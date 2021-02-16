# Implement a class to hold room information. This should have name and
# description attributes.

# Room Attributes: name, description 
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def full_room(self, item):
        self.items.append(item)
    
    def empty_room(self, item):
        self.items.remove(item)
        

