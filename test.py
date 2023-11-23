import random as rand
class Item:
    def __init__(self):
        x = rand.randint(1,3)
        if x == 1:
            self.Attribute = "1"
            self.Name = "One"
        elif x == 2:
            self.Attribute = "2"
            self.Name = "Two"
w = Item()
print(w.Attribute)
print(w.Name)