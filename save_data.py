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

def save_data(player, dmg_multiplier):
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
                save_string += ";" + str(item.strength_bonus) + ";" + item.preset + ","
    if player.Artifact_pouch == []:
        None
    else:
        save_string += "-"
        for item in player.Artifact_pouch:
            save_string += item.name + ";" + item.Artifact_ability + ";" + str(item.Artifact_) + ";" + item.Artifact
    file.write(save_string)
    print()
    print("Saved!")
    print()