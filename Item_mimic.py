import random as rand

class Item_mimic:
    def __init__(self, player):
        self.name = rand.choice(["Weapon mimic", 0])
        if self.name == "Weapon mimic":
            b = rand.randint(0,2)
            if b == 0:
                self.Attribute = "Strength bonus"
                self.name = f"Enchanted bow ({player.level})"
                self.strength_bonus = 3.1*player.level
                player.strength += self.strength_bonus
            elif b == 1:
                self.Attribute = "Strength bonus"
                self.name = f"Diamond sword ({player.level})"
                self.strength_bonus = 11 + 1.4*player.level
                player.strength += self.strength_bonus
            else:
                self.Attribute = "None"
                self.name = "None"
                print("The mimic wasn't holding onto anything...")
        else:
            b = rand.randint(0,2)
            if b == 0:  
                self.Attribute = "Health bonus"
                self.name = f"Diamond shield ({player.level})"
                self.health_bonus = 11 + 4*player.level
                player.hp_max += self.health_bonus
            elif b == 1:
                self.Attribute = "Health bonus"
                self.name = f"Diamond armor ({player.level})"
                self.health_bonus = 19 + 2.7*player.level
                player.hp_max += self.health_bonus
            else:
                self.Attribute = "None"
                self.name = "None"
                print("The mimic wasn't holding onto anything...")