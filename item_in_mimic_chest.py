from delay_print import *
import random as rand
from Item_mimic import *
def item_in_mimic_chest(player):
    item_mimic = Item_mimic(player)
    if item_mimic.name == "None":
        x = rand.randint(0,10)
        if x == 1:
            delay_print("""
                            Wait a second...
                            What is that light?
                          """)
            delay_print("""
                            Oh... It's nothing
""")
        return None
    player.inventory.append(item_mimic)
    if item_mimic.Attribute == "Strength bonus":
        print()
        print(f"You found a new weapon in the mimic: {item_mimic.name}!")
    else:
        print()
        print(f"You found a new defensive item in the mimic: {item_mimic.name}!")