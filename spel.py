import random as rand

class Player:
    def __init__(self):
        self.name = 0
        self.level = 1
        self.hp = 10
        self.hp_max = 10
        self.strength = 5
        self.inventory = []
        self.experience = 0

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
            self.health_bonus = 3.7 + player.level*2.5
            player.hp += self.health_bonus
            if player.hp > player.hp_max:
                player.hp = player.hp_max
        elif self.name == "Sword":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Wooden sword ({player.level})"
                self.strength_bonus = 3 + 0.2*player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = f"Iron sword ({player.level})"
                self.strength_bonus = 5 + 1.1*player.level
                player.strength += self.strength_bonus
            elif level == 2:
                self.name = f"Diamond sword ({player.level})"
                self.strength_bonus = 11 + 1.4*player.level
                player.strength += self.strength_bonus
        elif self.name == "Bow":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = f"Wooden bow ({player.level})"
                self.strength_bonus = 1.9*player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = f"Compound bow ({player.level})"
                self.strength_bonus = 2.4*player.level
                player.strength += self.strength_bonus
            elif level == 2:
                self.name = f"Enchanted bow ({player.level})"
                self.strength_bonus = 3.1*player.level
                player.strength += self.strength_bonus

class Monster:
    def __init__(self, player):
        self.Attribute = 0
        a = rand.randint(0,50)
        if a == 4:
            self.type = "Charizard"
            self.monster_strength = 45 + player.level*3
            self.monster_hp = 60 + player.level*4
        elif a == 2:
            if player.level < 10:
                self.type = "Nothing?"
                self.monster_strength = 0
                self.monster_hp = 0
            else: 
                self.Attribute = "Last boss"
                self.type = "Wait... Is that?"
                self.monster_strength = 99 + player.level*5
                self.monster_hp = 99 + player.level*5
        else:
            self.type = rand.choice(["Golem", "Goblin", "Dragon", "Rat", "Slime"])
            if self.type == "Golem":
                self.monster_strength = 9 + player.level*1.5
                self.monster_hp = 20 + player.level*2.9
            elif self.type == "Goblin":
                self.monster_strength = 4 + player.level*1.6
                self.monster_hp = 5 + player.level*1.7
            elif self.type == "Rat":
                self.monster_strength = 3 + player.level*1.5
                self.monster_hp = 2 + player.level*1
            elif self.type == "Slime":
                self.monster_strength = 1 + player.level*0.5
                self.monster_hp = 7 + player.level*2.7
            elif self.type == "Dragon":
                self.monster_strength = 33 + player.level*2.7
                self.monster_hp = 35 + player.level*3.2
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
                monster.monster_hp -= player.strength
                if monster.monster_hp <= 0:
                    player.hp -= 5*monster.monster_strength/player.hp_max
                    break
                player.hp -= monster.monster_strength/dmg_multiplier
            if player.hp <= 0:
                    print("""
                          You died
                          """)
                    exit()
            if monster.monster_hp <= 0:
                if monster.Attribute == "Last boss":
                    choice = input(f"""
                        Congratulations! you beat the game!
                        {player.name}, Thank you for playing!

                        Do you wish to keep playing?

                            1. Yes
                    """)
                    if choice != "1":
                        exit()
                xp = monster.experience_value
                player.experience += xp
                print(f"You have slain the {monster.type} and received {round(xp,2)} experience!")
                while player.experience >= 24 + player.level**1.9:
                    print(f"""
          Your level has increased!
Level: {player.level} -> {player.level+1}
Max HP: {round(player.hp_max,2)} -> {round(player.hp_max+1+player.level+1,2)}
STR: {round(player.strength,2)} -> {round(player.strength+1+player.level*0.7+0.7,2)}
                          """)
                    player.experience -= 24 + player.level**1.9
                    player.level += 1
                    player.hp_max += 1 + player.level
                    player.strength += 1 + player.level*0.7
        else:
            print("You fled!")
            break

    return player

def trap(player):
    y = rand.randint(0,1)
    if y == 0:
        trap_damage = 0.5*rand.randint(0, 2) + 0.6*player.level
        player.hp -= trap_damage
        print(f"You have been caught in a trap and lost {round(trap_damage,2)} HP!")
    else:
        print("You managed to dodge the trap!")
    if player.hp <= 0:
        print("""
              You died
              """)

def display_stats(player):
    print(f"Name: {player.name}")
    print(f"Experience: {round(player.experience,2)}/{round(24 + player.level**1.9,2)}")
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
            print(f"{item.name} with health bonus {round(item.health_bonus,2)}") 


def main():
    player = Player()
    dmg_multiplier = input("""
                Choose difficulty:
                1. Easy
                2. Medium
                3. Hard


--> """)
    if dmg_multiplier == "1":
        dmg_multiplier = 3
    elif dmg_multiplier == "2":
        dmg_multiplier = 1.5
    elif dmg_multiplier == "3":
        dmg_multiplier = 1
    else:
        dmg_multiplier = float(dmg_multiplier) # lower the multiplier, higher the damage you take!
    player.name = input("What's your name? ")
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
                if len(player.inventory) > 3:
                    try:
                        print("""
                              Your inventory is full! Pick something to exchange!
                              """)
                        show_inventory(player)
                        remove_index = int(input("Remove index: "))
                        index = player.inventory[remove_index-1]
                        # print(index) # index == <__main__.Item object at (code)> which means you cant use it with Item()
                        for item in player.inventory:
                            if item == player.inventory[remove_index-1]:
                                if item.Attribute == "Strength bonus":
                                    player.strength -= item.strength_bonus
                                    #player.inventory.remove(index)
                                else:
                                    player.hp_max -= item.health_bonus
                                    #player.inventory.remove(index)
                            else: None
                        player.inventory.remove(index)
                        if player.hp > player.hp_max:
                            player.hp = player.hp_max
                    except:
                        print(""""
                              Choose an index within list range!
                              
                              """)
                        print("Your inventory is full! Pick something to exchange!")
                        show_inventory(player)
                        remove_index = int(input("Remove index: ")) # or: stat... -= stat of weapon, item.health_bonus/item.strength_bonus
                        index = player.inventory[remove_index-1]
                        for item in player.inventory:
                            if item == player.inventory[remove_index-1]:
                                if item.Attribute == "Strength bonus":
                                    player.strength -= item.strength_bonus
                                    #player.inventory.remove(index)
                                else:
                                    player.hp_max -= item.health_bonus
                                    #player.inventory.remove(index)
                            else: None
                        # print(index)
                        # item = Item(index)
                        # if item.Attribute == "Strength bonus":
                        #     player.strength -= item.strength_bonus
                        # else:
                        #     player.hp -= item.health_bonus
                        player.inventory.remove(index)
                        if player.hp > player.hp_max:
                            player.hp = player.hp_max
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
#1.8 (hp)
#1.2 (strength)