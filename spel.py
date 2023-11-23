import random as rand
Attribute = 0
class Player:
    def __init__(self):
        self.level = 1
        self.hp = 10
        self.hp_max = 10
        self.strength = 4 + self.level
        self.inventory = []
        self.experience = 0

class Item:
    def __init__(self, player):
        if player.level >= 8:
            x = 1
        else: 
            x = 0
        self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "Health potion"])
        if self.name == "Armor":
            self.Attribute = "Health bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = "Leather armor"
                self.health_bonus = 3 + player.level
                player.hp_max += self.health_bonus
            elif level == 1:
                self.name = "Diamond armor"
                self.health_bonus = 15 + player.level
                player.hp_max += self.health_bonus
        elif self.name == "Shield":
            self.Attribute = "Health bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = "Wooden shield"
                self.health_bonus = 3 + player.level
                player.hp_max += self.health_bonus
            elif level == 1:
                self.name = "Diamond shield"
                self.health_bonus = 15 + player.level
                player.hp_max += self.health_bonus
        elif self.name == "Health potion":
            self.Attribute = "Health bonus"
            self.health_bonus = 4 + player.level
            player.hp += self.health_bonus
            if player.hp > player.hp_max:
                player.hp = player.hp_max
        elif self.name == "Sword":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = "Wooden sword"
                self.strength_bonus = 3 + player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = "Diamond sword"
                self.strength_bonus = 15 + player.level
                player.strength += self.strength_bonus
        elif self.name == "Bow":
            self.Attribute = "Strength bonus"
            level = rand.randint(0,x)
            if level == 0:
                self.name = "Bow"
                self.strength_bonus = 3 + player.level
                player.strength += self.strength_bonus
            elif level == 1:
                self.name = "Enchanted bow"
                self.strength_bonus = 15 + player.level
                player.strength += self.strength_bonus

class Monster:
    def __init__(self, player):
        self.monster_hp = rand.randint(2, 5) * player.strength
        self.type = rand.choice(["Golem", "Goblin", "Dragon"])
        if self.type == "Golem":
            self.monster_strength = 20 + player.level*3
        elif self.type == "Goblin":
            self.monster_strength = 10 + player.level*2
        elif self.type == "Dragon":
            self.monster_strength = 40 + player.level*4
        self.experience_value = self.monster_strength

def monster_battle(player, dmg_multiplier):
    monster = Monster(player)
    print(f"""
            You have encountered a {monster.type}!
            Monster hp: {monster.monster_hp}   
            Monster strength: {monster.monster_strength}

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
                monster.monster_hp -= player.strength
                player.hp -= monster.monster_strength/dmg
            if monster.monster_hp <= 0:
                xp = monster.experience_value
                player.experience += xp
                print(f"You have slain the {monster.type} and received {xp} experience!")
                if player.experience >= 45 + 5*player.level:
                    player.experience -= 45 + 5*player.level
                    player.level += 1
                    player.hp += 1
                    player.hp_max += 1
                    print(f"Your level has increased! You're now level {player.level}!")
        else:
            print("You fled!")
            break
        if player.hp <= 0:
                    print("You died")

    return player

def trap(player):
    y = rand.randint(0,1)
    if y == 0:
        trap_damage = rand.randint(1, 2) + 0.5*player.level
        player.hp -= trap_damage
        print(f"You have been caught in a trap and lost {round(trap_damage,2)} HP!")
    else:
        print("You managed to dodge the trap!")
    if player.hp <= 0:
        print("You died")

def display_stats(player):
    print(f"HP: {round(player.hp,2)}/{round(player.hp_max,2)}")
    print(f"Level: {player.level}")
    print(f"Strength: {round(player.strength,2)}")
    print(f"Experience: {round(player.experience,2)}")

def item_in_chest(player):
    item = Item(player)
    if item == "Health potion":
        None
    else:
        player.inventory.append(item)
    if item.Attribute == "Strength bonus":
        print(f"You have received a new weapon: {item.name}!")
    else:
        print(f"You have received a new defensive item: {item.name}!")

def show_inventory(player):
    for item in player.inventory:
        if item.Attribute == "Strength bonus":
            print(f"{item.name} with strength bonus ") #{item.strength_bonus}
        else:
            print(f"{item.name} with health bonus ") #{item.health_bonus}


def main():
    player = Player()
    dmg_multiplier = input("""
                       Choose difficulty:
                       1. Easy
                       2. Medium
                       3. Hard


--> """)
    if dmg_multiplier == "1":
        dmg_multiplier = 25
    elif dmg_multiplier == "2":
        dmg_multiplier = 17
    elif dmg_multiplier == "3":
        dmg_multiplier = 10
    else:
        dmg_multiplier = int(dmg_multiplier)

    while player.hp > 0:        
        print(
                """

                What do you want to do?
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
                if len(player.inventory) > 4:
                    try:
                        print("Your inventory is full! Pick something to exchange!")
                        show_inventory(player)
                        remove_index = int(input("Remove index: "))
                        index = player.inventory[remove_index]
                        player.inventory.remove(index)
                    except:
                        print("Choose an index within list range!")
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
