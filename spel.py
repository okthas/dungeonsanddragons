import random as rand

class Player:
    def __init__(self):
        self.level = 1
        self.hp = 9 + self.level
        self.hp_max = 9 + self.level
        self.strength = 4 + self.level
        self.inventory = []
        self.experience = 0

class Item:
    def __init__(self, player):
        self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "Health potion"])
        if self.name == "Armor":
            level = rand.randint(1,player.level+1)
            if level >= 8:
                self.name == "Rusty old armor"
                player.hp_max += 3 + player.level
            elif level >= 10:
                self.name == "Diamond armor"
                player.hp_max += 15 + player.level
        elif self.name == "Health potion":
            self.health_bonus = 4 + player.level
            if player.hp > player.hp_max:
                player.hp = player.hp_max
        elif self.name =="Sword":
            level = rand.randint(1,player.level+1)
            if level >= 8:
                self.name == "Wooden sword"
                player.strength += 3 + player.level
            elif level >= 10:
                self.name == "Diamond sword"
                player.strength += 15 + player.level
        elif self.name =="Shield":
            level = rand.randint(1,player.level+1)
            if level >= 8:
                self.name == "Wooden shield"
                player.hp_max += 3 + player.level
            elif level >= 10:
                   self.name == "Diamond shield"
                   player.hp_max += 15 + player.level

class Monster:
    def __init__(self, player):
        self.monster_hp = rand.randint(2, 5) * player.strength
        self.type = rand.choice(["Golem", "Goblin", "Dragon"])
        if self.type == "Golem":
            self.monster_strength = 15 + player.level*1.7
        elif self.type == "Goblin":
            self.monster_strength = 5 + player.level*1.5
        elif self.type == "Dragon":
            self.monster_strength = 30 + player.level*2
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
                    player.level += 1
                    print(f"Your level has increased! You're now level {player.level}!")
        else:
            print("You fled!")
            break
        if player.hp <= 0:
                    print("You died")

    return player

def trap(player):
    trap_damage = rand.randint(1, 5) + player.level
    player.hp = player.hp - trap_damage
    print(f"You have been caught in a trap and lost {trap_damage} HP!")
    if player.hp <= 0:
        print("You died")

def display_stats(player):
    xp_rounded = round(player.experience, 2)
    hp_rounded = round(player.hp, 2)
    print(f"HP: {hp_rounded}")
    print(f"Level: {player.level}")
    print(f"Strength: {player.strength}")
    print(f"Experience: {xp_rounded}")

def item_in_chest(player):
    item = Item(player)
    player.inventory.append(item)
    
    print(f"You have received a new weapon: {item.name}!")

def show_inventory(player):
    for item in player.inventory:
        try:
            print(f"{item.name} with strength bonus {item.strength_bonus}")
        except:
            print(f"{item.name} with health bonus {item.health_bonus}")


def main():
    player = Player()
    dmg_multiplier = input("""
                       Choose difficulty:
                       1. Easy
                       2. Medium
                       3. Hard
                       """)
    if dmg_multiplier == "1":
        dmg_multiplier = 7
    elif dmg_multiplier == "2":
        dmg_multiplier = 13
    elif dmg_multiplier == "3":
        dmg_multiplier = 20
    else:
        dmg_multiplier = dmg_multiplier

    while player.hp > 0:        
        print(
                """

                What do you want to do?
                1. Choose a door
                2. Check inventory
                3. Display stats
                
                """)
            
        choice = input("What do you want to do? (1, 2 or 3) ")

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
        else:
            print("Choose 1, 2 or 3!")

main()

