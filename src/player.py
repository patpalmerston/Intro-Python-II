# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"name: {self.name} \n Room: {self.current_room}"

    def get_inventory(self):
        return self.inventory

    def get_item(self, item):
        return self.inventory.append(item)

    def throw_item(self, item):
        return self.inventory.remove(item)
