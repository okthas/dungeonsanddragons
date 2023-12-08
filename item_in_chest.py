from Item import *

def item_in_chest(player):
    item = Item(player)
    print("""
                A chest!

    """)
    if item.Attribute == "Health potion":
        None
    elif item.Attribute == "Artifact":
        player.Artifact_pouch.append(item)
        print(f"You found an {item.name}!")
        return None
    else:
        player.inventory.append(item)
    if item.Attribute == "Strength bonus":
        print(f"You found a new weapon: {item.name} in the chest!")
    elif item.Attribute == "Health potion":
        print(f"You found a health potion in the chest that gave {round(3.4 + player.level*2,2)} HP! You HP is now {round(player.hp)}/{round()}")
    else:
        print(f"You found a defensive item: {item.name} in the chest!")