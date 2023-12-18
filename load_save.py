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

def load_save(player):
    try:
        file = open("save.txt", "r")
        save = file.readline().split("-")          
        stats = save[0].split(",")
        inventory = save[1]
        try:
            Artifact_pouch = save[2]
            Artifact_pouch = Artifact_pouch.split(";")
            item = Item(player)
            item.name = Artifact_pouch[0]
            item.Artifact_ability = Artifact_pouch[1]
            item.Artifact_ = float(Artifact_pouch[2])
            item.Artifact = Artifact_pouch[3]
            player.Artifact_pouch.append(item)
        except:
            None
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
                        item.preset = inventory2[3]
                        player.strength -= item.strength_bonus
                    player.inventory.append(item)
                item_variable += 1
        player.name = stats[0]
        player.strength = float(stats[1])
        player.hp = float(stats[2])
        player.hp_max = float(stats[3])
        player.experience = float(stats[4])
        player.level = int(stats[5])
        dmg_multiplier = float(stats[6])
    except FileNotFoundError:
        print("Save file not found.")
        file_open = "2"