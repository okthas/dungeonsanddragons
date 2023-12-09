import random as rand

class Item:
    def __init__(self, player):
        self.preset = rand.randint(1,10)
        if self.preset == 1:
            self.preset = "Strong"
        elif self.preset == 2:
            self.preset = "Scaling"
        elif self.preset == 3:
            self.preset = "Frosty"
        elif self.preset == 4:
            self.preset = "Spicy"
        else:
            self.preset = "Plain"
        
        if player.level >= 7:
            x = 2    
            z = rand.randint(0,33)
            if z == 3:
                self.Attribute = "Strength bonus"
                self.name = f"Excalibur ({player.level})"
                self.strength_bonus = 15 + player.level**1.6
                player.strength += self.strength_bonus   # when youre level 7 or higher theres a 1% chance to get excalibur
                if self.preset == "Strong":
                    self.strength_bonus += 5
                    player.strength += 5
                elif self.preset == "Scaling":
                    self.strength_bonus += player.level
                    player.strength += player.level
                return None   
        elif player.level >= 4:
            x = 1
        else: 
            x = 0
        self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "J", "J", "J", "Artifact"]) 
        if player.hp == player.hp_max:
            self.name = rand.choice(["Sword", "Shield", "Bow", "Armor"])
        if player.hp < player.hp_max*0.35:
            self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "J", "J", "J", "J", "J", "J", "J", "Artifact"])
        if self.name == "Armor":
            self.Attribute = "Health bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Leather armor ({player.level})"
                self.health_bonus = 3.3 + 1.6*player.level 
                player.hp_max += self.health_bonus
            elif level == 1:
                self.name = f"Iron armor ({player.level})"
                self.health_bonus = 7.5 + 2*player.level
                player.hp_max += self.health_bonus
            elif level == 2:
                self.name = f"Diamond armor ({player.level})"
                self.health_bonus = 19 + 2.7*player.level
                player.hp_max += self.health_bonus
        elif self.name == "Shield":
            self.Attribute = "Health bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Wooden shield ({player.level})"
                self.health_bonus = 2.5 + 2.1*player.level
                player.hp_max += self.health_bonus
            elif level == 1:
                self.name = f"Iron shield ({player.level})"
                self.health_bonus = 6 + 3*player.level
                player.hp_max += self.health_bonus
            elif level == 2:
                self.name = f"Diamond shield ({player.level})"
                self.health_bonus = 11 + 4*player.level
                player.hp_max += self.health_bonus
        elif self.name == "J":
            self.name = "Health potion"
            self.Attribute = "Health potion"
            self.health_bonus = 3.4 + player.level*2
            player.hp += self.health_bonus
            if player.hp > player.hp_max:
                player.hp = player.hp_max
        elif self.name == "Sword":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"{self.preset} Wooden sword ({player.level})"
                self.strength_bonus = 3 + 0.2*player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = f"{self.preset} Iron sword ({player.level})"
                self.strength_bonus = 5 + 1.1*player.level
                player.strength += self.strength_bonus
            elif level == 2:
                self.name = f"{self.preset} Diamond sword ({player.level})"
                self.strength_bonus = 11 + 1.4*player.level
                player.strength += self.strength_bonus
            if self.preset == "Strong":
                self.strength_bonus += 5
                player.strength += 5
            elif self.preset == "Scaling":
                self.strength_bonus += player.level
                player.strength += player.level
        elif self.name == "Bow":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"{self.preset} Wooden bow ({player.level})"
                self.strength_bonus = 1.5*player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = f"{self.preset} Compound bow ({player.level})"
                self.strength_bonus = 2.2*player.level
                player.strength += self.strength_bonus
            elif level == 2:
                self.name = f"{self.preset} Enchanted bow ({player.level})"
                self.strength_bonus = 2.9*player.level
                player.strength += self.strength_bonus 
            if self.preset == "Strong":
                self.strength_bonus += 5
                player.strength += 5
            elif self.preset == "Scaling":
                self.strength_bonus += player.level
                player.strength += player.level
        elif self.name == "Artifact":
            self.Attribute = "Artifact"
            level = rand.randint(0,3)
            if level == 0:
                self.name = f"Ominous artifact ({player.level})"
                self.Artifact = "O"
                self.Artifact_ = 10 + 2.5*player.level
                self.Artifact_ability = f"Enemies deal {self.Artifact_}% less damage"
            elif level == 1:
                self.name = f"Blessed artifact ({player.level})"
                self.Artifact = "F"
                self.Artifact_ = 40 + 10*player.level
                self.Artifact_ability = f"You gain {self.Artifact_}% more fire elemental damage"
            else:
                self.name = f"Cold artifact ({player.level})"
                self.Artifact = "I"
                self.Artifact_ = 40 + 10*player.level
                self.Artifact_ability = f"You gain {self.Artifact_}% more ice elemental damage"
