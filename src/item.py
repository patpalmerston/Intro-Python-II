# Create item class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name} \n Description: {self.description}"

    def pickup_item(self):
        return f"you picked up {self.name}"

    def drop_item(self):
        return f"you dropped the {self.name}"
