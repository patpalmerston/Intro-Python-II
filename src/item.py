# Create item class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup_item(self, item):
        return f"you picked up {self.item}"

    def drop_item(self, item):
        return f"you dropped the {self.item}"
