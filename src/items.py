class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name} and {self.description}"
    
    def on_take(self):
        print(f"you have picked up {self.name}")