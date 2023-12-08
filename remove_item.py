import random as rand
from Player import *
from display_stats import *
from show_inventory import *
from Item import *


def remove_item(player,Artifact):
    if Artifact:
        while len(player.Artifact_pouch) > 1:
            print("""
                            I can't have more than one artifact... for some reason?
""")
            show_inventory(player,Artifact)
            remove_index = input("Remove index: ")
            if remove_index == "1" or remove_index == "2":
                remove_index = int(remove_index)
            else:
                print(""""
                                I can't find it...
                    
                    """)
                continue
            index = player.Artifact_pouch[remove_index-1]
            for item in player.Artifact_pouch:
                if item == player.Artifact_pouch[remove_index-1]:
                    player.Artifact_pouch.remove(index)
                    ""
                else: None
            player.inventory.remove(index)
            if player.hp > player.hp_max:
                player.hp = player.hp_max
            return None
    while len(player.inventory) > 3:
        print("""
                            My backpack is getting heavy, I need to get rid of something...
                                """)
        show_inventory(player,Artifact)
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