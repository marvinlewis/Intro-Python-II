# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
        self.items = []
        

    def __str__(self):
        return f"{self.name} is {self.description}"
    
    def get_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            else:
                return None
    
    def remove_item(self, item):
        return self.items.remove(item)