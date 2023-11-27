from Item import *

def item_in_chest(player):
    item = Item(player)
    print("""
                A chest!

    """)
    if item.Attribute == "Health potion":
        None
    else:
        player.inventory.append(item)
    if item.Attribute == "Strength bonus":
        print(f"You found a new weapon: {item.name} in the chest!")
    elif item.Attribute == "Health potion":
        print(f"You found a health potion in the chest!")
    else:
        print(f"You found a defensive item: {item.name} in the chest!")