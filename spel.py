import random as rand

class Player:
    def __init__(self):
        self.level = 1
        self.hp = 100
        self.strength = 10
        self.inventory = []

class Item:
    def __init__(self):
        self.name = rand.choice(["Sword", "Shield", "Bow", "Armor"])
        self.strength_bonus = rand.randint(1, 5)

player = Player()

class Monster:
    def __init__(self):
        self.monster_hp = rand.randint(5, 10) * player.strength
        self.monster_strength = rand.randint(2, 5) * player.level
        self.monster = rand.choice(["Golem", "Goblin", "Dragon", "Wyvern"])

def monster_battle():
    print(f"""
            You have encountered a {monster.monster}!
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
                player.hp -= monster.monster_strength
                print(f"Monster hp: {monster.monster_hp}")
                if monster.monster_hp <= 0:
                    print(f"You have slain the {monster.monster}!")
                    xp = monster.monster_strength
                    print(f"You have recieved {xp} experience!")
            else:
                print("You fled!")
                break
    sum_xp = 0
    sum_xp += xp
    if sum_xp > 10:
        print("Your level has increased!")
        player.level += sum_xp
        player.strength += 2

monster = Monster()

def display_stats(player):
    print(f"HP: {player.hp}")
    print(f"Level: {player.level}")
    print(f"Strength: {player.strength}")

def item_in_chest(player):
    item = Item()
    player.inventory.append(item)
    player.strength += item.strength_bonus
    
    print(f"You have received a new weapon: {item.name}!")
    print(f"Your strength has increased by {item.strength_bonus}")


def main():
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
                monster_battle()
                if player.hp <= 0:
                    print("You died")
            elif scenario == 2:
                item_in_chest(player)
                if len(player.inventory) > 4:
                    try:
                        print("Your inventory is full! Pick something to exchange!")
                        for item in player.inventory:
                            print(f"{item.name} with strength bonus {item.strength_bonus}")
                        remove_index = int(input("Remove index: "))
                        index = player.inventory[remove_index]
                        player.inventory.remove(index)
                    except:
                        print("Choose an index within list range!")
            elif scenario == 3:
                trap_damage = rand.randint(1, 4)
                player.hp = player.hp - trap_damage
                print(f"You have been caught in a trap and lost {trap_damage} HP!")
                if player.hp <= 0:
                    print("You died")
        elif choice == "2":
            for item in player.inventory:
                print(f"{item.name} with strength bonus {item.strength_bonus}")
        elif choice == "3":
            display_stats(player)
        else:
            print("Choose 1, 2 or 3!")

main()

