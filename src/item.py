# Create item class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"Name: {self.name} \n Description: {self.description}"

    def pickup_item(self):
        print(f"******Well DONE! You picked up the {self.name}!!!******")

    def drop_item(self):
        print(f"******Looks like you dropped the {self.name}!******")
