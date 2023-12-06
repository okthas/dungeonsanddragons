import random as rand
from Player import *
from display_stats import *
from delay_print import *
from show_inventory import *
from Item_mimic import *
from Item import *
from Monster import *
from monster_battle import *
from trap import *
from item_in_mimic_chest import *
from item_in_chest import *
from remove_item import *

def main():
    i = 0
    player = Player()
    file = open("save.txt", "r")
    file_open = input ("""
                Open save file?
                1. Yes
                2. No
-> """)
    if file_open == "1":
        try:
            save = file.readline().split("-")
            stats = save[0].split(",")
            inventory = save[1]
            player.name = stats[0]
            player.strength = float(stats[1])
            player.hp = float(stats[2])
            player.hp_max = float(stats[3])
            player.experience = float(stats[4])
            player.level = int(stats[5])
            dmg_multiplier = float(stats[6])
            item_variable = 0
            if inventory == [''] or inventory == []:
                inventory == []
            else:
                inventory = inventory.split(",")
                for item2 in inventory:
                    if  item2 == '':
                        inventory.remove(item2)
                    else:
                        item = Item(player)
                        inventory2 = inventory[item_variable]
                        inventory2 = inventory2.split(";")
                        item.name = inventory2[0]
                        item.Attribute = inventory2[1]
                        if item.Attribute == "Health bonus":
                            item.health_bonus = float(inventory2[2])
                            player.hp_max -= item.health_bonus
                        else:
                            item.strength_bonus = float(inventory2[2])
                            player.strength -= item.strength_bonus
                        player.inventory.append(item)
                    item_variable += 1
        except:
            print("""
                There is no save file...""")
            file_open = "2"

    else:
        None
    trap_multiplier = 0
    if file_open != "1":
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
    if file_open != "1":
        player.name = input("""
                
                What's your name? 
""")
        if player.name == "Marie":
            delay_print("""
                            That sounds... Familiar
""")
    while player.hp > 0:        
        print(
                """

                1. Choose a door
                2. Check inventory
                3. Display stats
                4. Quit
                
                """)
            
        choice = input("What should I do? ")

        if choice == "1":
            x = 1
            while x == 1:
                try:
                    print("""
                                    


        1:              2:              3:
     _________       _________       _________      
    I         I     I         I     I         I     I
    I         I     I         I     I         I     I
    I         I     I         I     I         I     I
    I O       I     I O       I     I O       I     I
    I         I     I         I     I         I     I
    I         I     I         I     I         I     I
____________________________________________________I """)
                    choice2 = int(input("Which door should I choose... "))
                    if choice2 != 1 and choice2 != 2 and choice2 != 3:
                        if choice2%2 == 0:
                            delay_print("""
That door isn't here... is it?
""")
                        else:
                            delay_print("""
...
""")
                        continue
                    x = 0
                except:
                    delay_print("""
That's not even a number... Let's go through this one...
""")
                    x = 0
            scenario = rand.randint(1, 3)
            if scenario == 1:
                player = monster_battle(player, dmg_multiplier, trap_multiplier)
                remove_item(player)
            elif scenario == 2:
                item_in_chest(player)
                if len(player.inventory) > 3:
                    remove_item(player)
            elif scenario == 3:
                trap(player, dmg_multiplier, trap_multiplier)
        elif choice == "2":
            show_inventory(player)
        elif choice == "3":
            display_stats(player, dmg_multiplier)
        elif choice == "4":
            save_ = input("""
                Save?
                1. yes
                2. no
-> """)
            if save_ == "1":
                file = open("save.txt", "w")
                save_string = str(player.name) + "," + str(player.strength) + "," + str(player.hp) + "," + str(player.hp_max) + "," + str(player.experience) + "," + str(player.level) + "," + str(dmg_multiplier) + "-"
                if player.inventory == []:
                    None
                else:
                    for item in player.inventory:
                        save_string += item.name + ";" + item.Attribute
                        if item.Attribute == "Health bonus":
                            save_string += ";" + str(item.health_bonus) + ","
                        else:
                            save_string += ";" + str(item.strength_bonus) + ","
                file.write(save_string)
                print()
                delay_print("Saving...")
                print()
            else:
                print("""
                            Restarting...
""")
            exit()
        else:
            print("?")
main()
#x, y, z, a, b, etc are just throwaway variables used for randomizing choices, aka: chance