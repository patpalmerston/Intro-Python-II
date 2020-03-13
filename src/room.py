# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, n_to=None, e_to=None, w_to=None, s_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.w_to = w_to
        self.s_to = s_to
        self.items = []

    def __str__(self):
        return f"name: {self.name}"

    def get_items(self):
        return self.items

    def add_item(self, item):
        return self.items.append(item)

    def delete_item(self, item):
        return self.items.remove(item)
