import random as rand

class Player:
    def __init__(self):
        self.level = 1
        self.hp = 100
        self.strength = 10
        self.inventory = []
        self.experience = 0

class Item:
    def __init__(self, player):
        self.name = rand.choice(["Sword", "Shield", "Bow", "Armor", "Health potion"])
        # if self.name == "Armor":
        #     self.health_bonus = rand.randint(1, 5)
        #     player.hp = player.hp + self.health_bonuss
        # else:
        #     self.strength_bonus = rand.randint(1, 5)
        #     player.strength += self.strength_bonus

class Monster:
    def __init__(self, player):
        self.monster_hp = rand.randint(2, 5) * player.strength
        self.monster_strength = 10 * player.level
        self.type = rand.choice(["Golem", "Goblin", "Dragon", "Wyvern"])

def monster_battle(player):
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
            monster.monster_hp -= player.strength
            print(f"Monster hp: {monster.monster_hp}")
            if monster.monster_hp <= 0:
                xp = monster.monster_strength/2
                print(f"You have slain the {monster.type} and received {xp} experience!")
                if xp >= 10:
                    print("Your level has risen!")
                    player.experience += xp
                    if player.experience >= 10:
                        player.level += 1
                        print("Your level has increased!")
        else:
            print("You fled!")
            break
        if player.hp <= 0:
                    print("You died")

    return player

def trap(player):
    trap_damage = rand.randint(5, 10)
    player.hp = player.hp - trap_damage
    print(f"You have been caught in a trap and lost {trap_damage} HP!")
    if player.hp <= 0:
        print("You died")

def display_stats(player):
    print(f"HP: {player.hp}")
    print(f"Level: {player.level}")
    print(f"Strength: {player.strength}")
    print(f"Experience: {player.experience}")

def item_in_chest(player):
    item = Item(player)
    player.inventory.append(item)
    if item.name == "Armor":
            item.health_bonus = rand.randint(1, 5)
            player.hp = player.hp + item.health_bonus
    else:
        item.strength_bonus = rand.randint(1, 5)
        player.strength += item.strength_bonus
    
    print(f"You have received a new weapon: {item.name}!")

def show_inventory(player):
    for item in player.inventory:
        try:
            print(f"{item.name} with strength bonus {item.strength_bonus}")
        except:
            print(f"{item.name} with health bonus {item.health_bonus}")


def main():
    player = Player()

    while player.hp >= 0:        
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
                player = monster_battle(player)
                # xp = monster.monster_strength/2
                # print(f"You have slain the {monster.type} and received {xp} experience!")
                # if xp >= 10:
                #     print("Your level has risen!")
                #     player.level += 1
                #     print(f"Your level is now {player.level}")
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

