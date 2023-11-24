import random as rand

class Player:
    def __init__(self):
        self.level = 1
        self.hp = 10
        self.hp_max = 10
        self.strength = 5
        self.inventory = []
        self.experience = 0
# class Item:
#     def __init__(self, player):
#         if player.level >= 7:
#             x = 2    
#             z = rand.randint(0,100)
#             if z == 3:
#                 self.Attribute = "Strength bonus"
#                 self.name = f"Excalibur ({player.level})"
#                 self.strength_bonus = 15 + player.level**1.6
#                 player.strength += self.strength_bonus   
#                 return None   
#         elif player.level >= 5:
#             x = 1
#         else: 
#             x = 0
#         self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "J", "J", "J"])
#         if self.name == "Armor":
#             self.Attribute = "Health bonus"
#             level = rand.randint(0,x)
#             if level == 0:
#                 self.name = f"Leather armor ({player.level})"
#                 self.health_bonus = 3 + player.level 
#                 player.hp_max += self.health_bonus
#             elif level == 1:
#                 self.name = f"Iron armor ({player.level})"
#                 self.health_bonus = 7 + 1.4*player.level
#                 player.hp_max += self.health_bonus
#             elif level == 2:
#                 self.name = f"Diamond armor ({player.level})"
#                 self.health_bonus = 15 + 2*player.level
#                 player.hp_max += self.health_bonus
#         elif self.name == "Shield":
#             self.Attribute = "Health bonus"
#             level = rand.randint(0,x)
#             if level == 0:
#                 self.name = f"Wooden shield ({player.level})"
#                 self.health_bonus = 3 + player.level
#                 player.hp_max += self.health_bonus
#             elif level == 1:
#                 self.name = f"Iron shield ({player.level})"
#                 self.health_bonus = 7 + 1.4*player.level
#                 player.hp_max += self.health_bonus
#             elif level == 2:
#                 self.name = f"Diamond shield ({player.level})"
#                 self.health_bonus = 15 + 2*player.level
#                 player.hp_max += self.health_bonus
#         elif self.name == "J":
#             self.name = "Health potion"
#             self.Attribute = "Health potion"
#             self.health_bonus = 3.7 + player.level*2.5
#             player.hp += self.health_bonus
#             if player.hp > player.hp_max:
#                 player.hp = player.hp_max
#         elif self.name == "Sword":
#             self.Attribute = "Strength bonus"
#             level = rand.randint(0,x)
#             if level == 0:
#                 self.name = f"Wooden sword ({player.level})"
#                 self.strength_bonus = 3 + player.level
#                 player.strength += self.strength_bonus
#             elif level == 1:
#                 self.name = f"Iron sword ({player.level})"
#                 self.strength_bonus = 7 + 1.4*player.level
#                 player.strength += self.strength_bonus
#             elif level == 2:
#                 self.name = f"Diamond sword ({player.level})"
#                 self.strength_bonus = 15 + 2*player.level
#                 player.strength += self.strength_bonus
#         elif self.name == "Bow":
#             self.Attribute = "Strength bonus"
#             level = rand.randint(0,x)
#             if level == 0:
#                 self.name = f"Wooden bow ({player.level})"
#                 self.strength_bonus = 3 + player.level
#                 player.strength += self.strength_bonus
#             elif level == 1:
#                 self.name = f"Compound bow ({player.level})"
#                 self.strength_bonus = 7 + 1.4*player.level
#                 player.strength += self.strength_bonus
#             elif level == 2:
#                 self.name = f"Enchanted bow ({player.level})"
#                 self.strength_bonus = 15 + 2*player.level
#                 player.strength += self.strength_bonus
# 
# only if [item] is in player.inventory
# if self.Attribute == "Health bonus":
    # for item in player.inventory
    #     if item == "Leather armor":
    #         self.health_bonus += 3 + player.level
    #       /.../ rest of the items, will have to make it in test.py later
    #     else:
    #         self.health_bonus = self.health_bonus //////////
    # strength bonus, and health bonus total gets added to your stats aka: the bonus is stored in a different variable that only increases stats based on the total boost in your inventory
class Item:
    def __init__(self, player):
        if player.level >= 7:
            x = 2    
            z = rand.randint(0,33)
            if z == 3:
                self.Attribute = "Strength bonus"
                self.name = f"Excalibur ({player.level})"
                self.strength_bonus = 15 + player.level**1.6
                player.strength += self.strength_bonus   # when youre level 7 or higher theres a 1% chance to get excalibur
                return None   
        elif player.level >= 5:
            x = 1
        else: 
            x = 0
        self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "J", "J", "J"])
        if self.name == "Armor":
            self.Attribute = "Health bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Leather armor ({player.level})"
                self.health_bonus = 3 + player.level 
                player.hp_max += self.health_bonus
            elif level == 1:
                self.name = f"Iron armor ({player.level})"
                self.health_bonus = 7 + 1.4*player.level
                player.hp_max += self.health_bonus
            elif level == 2:
                self.name = f"Diamond armor ({player.level})"
                self.health_bonus = 15 + 2*player.level
                player.hp_max += self.health_bonus
        elif self.name == "Shield":
            self.Attribute = "Health bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Wooden shield ({player.level})"
                self.health_bonus = 3 + player.level
                player.hp_max += self.health_bonus
            elif level == 1:
                self.name = f"Iron shield ({player.level})"
                self.health_bonus = 7 + 1.4*player.level
                player.hp_max += self.health_bonus
            elif level == 2:
                self.name = f"Diamond shield ({player.level})"
                self.health_bonus = 15 + 2*player.level
                player.hp_max += self.health_bonus
        elif self.name == "J":
            self.name = "Health potion"
            self.Attribute = "Health potion"
            self.health_bonus = 3.7 + player.level*2.5
            player.hp += self.health_bonus
            if player.hp > player.hp_max:
                player.hp = player.hp_max
        elif self.name == "Sword":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Wooden sword ({player.level})"
                self.strength_bonus = 3 + player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = f"Iron sword ({player.level})"
                self.strength_bonus = 7 + 1.4*player.level
                player.strength += self.strength_bonus
            elif level == 2:
                self.name = f"Diamond sword ({player.level})"
                self.strength_bonus = 15 + 2*player.level
                player.strength += self.strength_bonus
        elif self.name == "Bow":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Wooden bow ({player.level})"
                self.strength_bonus = 3 + player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = f"Compound bow ({player.level})"
                self.strength_bonus = 7 + 1.4*player.level
                player.strength += self.strength_bonus
            elif level == 2:
                self.name = f"Enchanted bow ({player.level})"
                self.strength_bonus = 15 + 2*player.level
                player.strength += self.strength_bonus

class Monster:
    def __init__(self, player):
        a = rand.randint(0,50)
        if a == 4:
            self.type = "Charizard"
            self.monster_strength = 45 + player.level*5
            self.monster_hp = 60 + player.level*6
        else:
            self.type = rand.choice(["Golem", "Goblin", "Dragon"])
            if self.type == "Golem":
                self.monster_strength = 12 + player.level*2.9
                self.monster_hp = 14 + player.level*3.7
            elif self.type == "Goblin":
                self.monster_strength = 4 + player.level*1.9
                self.monster_hp = 5 + player.level*2.9
            elif self.type == "Dragon":
                self.monster_strength = 33 + player.level*4.1
                self.monster_hp = 35 + player.level*4.4
        self.experience_x = self.monster_strength + self.monster_hp
        self.experience_value = self.experience_x*0.5

def monster_battle(player, dmg_multiplier):
    monster = Monster(player)
    print(f"""
            You have encountered a {monster.type}!
            Monster hp: {round(monster.monster_hp,2)}   
            Monster strength: {round(monster.monster_strength,2)}

            """)
    while monster.monster_hp > 0:
        print(f"""
            1. Attack
            2. Flee

        """)
        choose = input("Attack or flee?  ")
        if choose == "1":
            while monster.monster_hp > 0:
                dmg = player.strength * dmg_multiplier
                player.hp -= monster.monster_strength/dmg
                monster.monster_hp -= player.strength
            if player.hp <= 0:
                    print("""
                          You died
                          """)
                    exit()
            if monster.monster_hp <= 0:
                xp = monster.experience_value
                player.experience += xp
                print(f"You have slain the {monster.type} and received {round(xp,2)} experience!")
                while player.experience >= 24 + player.level**1.6:
                    player.experience -= 24 + player.level**1.6
                    player.level += 1
                    player.hp += 1 + player.level**1.4
                    player.hp_max += 1 + player.level**1.4
                    player.strength += 1 + player.level**1.2
                    print(f"Your level has increased! You're now level {player.level}!")
        else:
            print("You fled!")
            break

    return player

def trap(player):
    y = rand.randint(0,1)
    if y == 0:
        trap_damage = 0.5*rand.randint(0, 2) + 0.9*player.level
        player.hp -= trap_damage
        print(f"You have been caught in a trap and lost {round(trap_damage,2)} HP!")
    else:
        print("You managed to dodge the trap!")
    if player.hp <= 0:
        print("""
              You died
              """)

def display_stats(player):
    print(f"Experience: {round(player.experience,2)}/{round(24 + player.level**1.6,2)}")
    print(f"Level: {player.level}")
    print(f"Strength: {round(player.strength,2)}")
    print(f"HP: {round(player.hp,2)}/{round(player.hp_max,2)}")

def item_in_chest(player):
    item = Item(player)
    if item.Attribute == "Health potion":
        None
    else:
        player.inventory.append(item)
    if item.Attribute == "Strength bonus":
        print(f"You have received a new weapon: {item.name}!")
    else:
        print(f"You have received a new defensive item: {item.name}!")

def show_inventory(player):
    for item in player.inventory:
        # if item.Attribute == "Strength bonus":
        # else:
        try:
            print(f"{item.name} with strength bonus {round(item.strength_bonus,2)}")
        except:
            print(f"{item.name} with health bonus {round(item.health_bonus,2)}") # it seems to show at random, which is annoying if u wanna know what item ur deleting
    #print(player.inventory) # just for analytical reasons


def main():
    player = Player()
    dmg_multiplier = input("""
                       Choose difficulty:
                       1. Easy
                       2. Medium
                       3. Hard


--> """)
    if dmg_multiplier == "1":
        dmg_multiplier = 4
    elif dmg_multiplier == "2":
        dmg_multiplier = 2
    elif dmg_multiplier == "3":
        dmg_multiplier = 1
    else:
        dmg_multiplier = float(dmg_multiplier) # lower the multiplier, higher the damage you take!
    
    while player.hp > 0:        
        print(
                """

                1. Choose a door
                2. Check inventory
                3. Display stats
                4. Quit
                
                """)
            
        choice = input("What do you want to do? ")

        if choice == "1":
            scenario = rand.randint(1, 3)
            if scenario == 1:
                player = monster_battle(player, dmg_multiplier)
            elif scenario == 2:
                item_in_chest(player)
                if len(player.inventory) > 2:
                    try:
                        print("""
                              Your inventory is full! Pick something to exchange!
                              """)
                        show_inventory(player)
                        remove_index = int(input("Remove index: "))
                        index = player.inventory[remove_index+1]
                        player.inventory.remove(index)
                    except:
                        print(""""
                              Choose an index within list range!
                              
                              """)
                        print("Your inventory is full! Pick something to exchange!")
                        show_inventory(player)
                        remove_index = int(input("Remove index: "))
                        index = player.inventory[remove_index-1]
                        player.inventory.remove(index)
            elif scenario == 3:
                trap(player)
        elif choice == "2":
            show_inventory(player)
        elif choice == "3":
            display_stats(player)
        elif choice == "4":
            exit()
        else:
            print("Could not execute command") # makes the code look badass B)
main()
