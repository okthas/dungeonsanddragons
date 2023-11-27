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

def main():
    trap_multiplier = 0
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
                while len(player.inventory) > 3:
                    print("""
                            My backpack is getting heavy, I need to get rid of something...
                            """)
                    show_inventory(player)
                    remove_index = input("Remove index: ")
                    if remove_index == "1" or remove_index == "2" or remove_index == "3" or remove_index == "4":
                        remove_index = int(remove_index)
                    else:
                        print(""""
                            I can't find it...
                            
                            """)
                        continue
                    index = player.inventory[remove_index-1]
                    for item in player.inventory:
                        if item == player.inventory[remove_index-1]:
                            if item.Attribute == "Strength bonus":
                                player.strength -= item.strength_bonus
                            else:
                                player.hp_max -= item.health_bonus
                        else: None
                    player.inventory.remove(index)
                    if player.hp > player.hp_max:
                        player.hp = player.hp_max
            elif scenario == 2:
                item_in_chest(player)
                if len(player.inventory) > 3:
                    while len(player.inventory) > 3:
                        print("""
                                My backpack is getting heavy, I need to get rid of something...
                                """)
                        show_inventory(player)
                        remove_index = input("Remove index: ")
                        if remove_index == "1" or remove_index == "2" or remove_index == "3" or remove_index == "4":
                            remove_index = int(remove_index)
                        else:
                            print(""""
                                I can't find it...
                                
                                """)
                            continue
                        index = player.inventory[remove_index-1]
                        for item in player.inventory:
                            if item == player.inventory[remove_index-1]:
                                if item.Attribute == "Strength bonus":
                                    player.strength -= item.strength_bonus
                                else:
                                    player.hp_max -= item.health_bonus
                            else: None
                        player.inventory.remove(index)
                        if player.hp > player.hp_max:
                            player.hp = player.hp_max
            elif scenario == 3:
                trap(player, dmg_multiplier, trap_multiplier)
        elif choice == "2":
            show_inventory(player)
        elif choice == "3":
            display_stats(player, dmg_multiplier)
        elif choice == "4":
            print("""
                            Restarting...
""")
            exit()
        else:
            print("?")
main()
#x, y, z, a, b, etc are just throwaway variables used for randomizing choices, aka: chance