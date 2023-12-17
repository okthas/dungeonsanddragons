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
        if self.name == "Sword" or self.name == "Bow":
            self.strength_bonus = rand.randint(1, 5)
        else:
            self.hp_bonus = rand.randint(3, 10)

class Monster:
    def __init__(self, player):
        self.monster_hp = rand.randint(2, 4) * player.strength
        self.monster_strength = rand.randint(2, 5) * player.level
        self.monster = rand.choice(["Golem", "Goblin", "Dragon"])

def monster_battle(player):
    monster = Monster(player)
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
                    sum_xp = 0
                    sum_xp += xp
                    if sum_xp > 10:
                        print("Your level has increased!")
                        player.level += sum_xp
                        player.strength += 2
                elif player.hp <= 0:
                    print("You died")
            else:
                print("You fled!")
                break



def display_stats(player):
    print(f"HP: {player.hp}")
    print(f"Level: {player.level}")
    print(f"Strength: {player.strength}")

def item_in_chest(player):
    item = Item()
    player.inventory.append(item)
    if item.name == "Sword" or item.name == "Bow":
         player.strength += item.strength_bonus
    else:
         player.hp += item.hp_bonus
    print(f"You have received a new weapon: {item.name}!")
    try:
        print(f"Your strength has increased by {item.strength_bonus}")
    except:
        print(f"Your health has increased by {item.hp_bonus}")

def trap(player):
    trap_damage = rand.randint(1, 4)
    player.hp = player.hp - trap_damage
    print(f"You have been caught in a trap and lost {trap_damage} HP!")
    if player.hp <= 0:
        print("You died")

def main():
    player = Player()
    while player.hp > 0:        
        print(
                """

                What do you want to do?
                1. Choose a door
                2. Check inventory
                3. Display stats
                
                """)
            
        choice = input()

        if choice == "1":
            scenario = rand.randint(1, 3)
            if scenario == 1:
                monster_battle(player)
            elif scenario == 2:
                item_in_chest(player)
            elif scenario == 3:
                trap(player)
        elif choice == "2":
            if player.inventory == []:
                print("Your inventory is empty")
            else:
                for item in player.inventory:
                    try: 
                        print(f"{item.name} with strength bonus {item.strength_bonus}")
                    except:
                        print(f"{item.name} with health bonus {item.health_bonus_bonus}")
        elif choice == "3":
            display_stats(player)
        else:
            print("Choose 1, 2 or 3!")

main()