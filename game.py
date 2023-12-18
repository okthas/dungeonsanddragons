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
from load_save import *
from save_data import *

def main():
    Artifact = False
    player = Player()
    file_open = False 
    file = open("save.txt", "r")
    save = file.readline().split("-")
    if save != ['']:
        file_open = input ("""
                    Open save file?
                    1. Yes
                    2. No

                    --> """)
    if file_open == "1":
        load_save(player)
    else:
        player.name = input("""
                
                What's your name? 
""")
        if player.name == "Marie":
            delay_print("""
                            That sounds... Familiar
""")
    trap_multiplier = 0    
    while True:

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
            try: 
                dmg_multiplier = float(dmg_multiplier)
            except:
                print("Choose 1, 2 or 3!")
                continue
        break        
    while player.hp > 0:        
        print(
                """

                1. Choose a door
                2. Check inventory
                3. Display stats
                4. Save
                5. Quit
                
                """)
            
        choice = input("What should I do? ")

        if choice == "1":
            while True:
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
                    choice2 = float(input("Which door should I choose... "))
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
                    break
                except:
                    delay_print("""
That's not even a number... Let's go through this one...
""")
                    break
            scenario = rand.randint(1, 3)
            if scenario == 1:
                player = monster_battle(player, dmg_multiplier, trap_multiplier)
                remove_item(player,Artifact)
            elif scenario == 2:
                Artifact = False
                item_in_chest(player)
                if len(player.inventory) > 3:
                    remove_item(player,Artifact)
                if len(player.Artifact_pouch) > 1:
                    Artifact = True
                    remove_item(player,Artifact)
            elif scenario == 3:
                trap(player, dmg_multiplier, trap_multiplier)
        elif choice == "2":
            show_inventory(player,Artifact)
        elif choice == "3":
            display_stats(player, dmg_multiplier)
        elif choice == "4":
            save_data(player, dmg_multiplier)
        elif choice == "5":
            print("""
                        Restarting...
""")
            exit()
        else:
            print("?")
main()
#x, y, z, a, b, etc are just throwaway variables used for randomizing choices, aka: chance