def show_inventory(player):
    if player.inventory == []:
        print("Nothing...")
        return None
    for item in player.inventory:
        try:
            print(f"{item.name} with strength bonus {round(item.strength_bonus,2)}!")
        except:
            print(f"{item.name} with health bonus {round(item.health_bonus,2)}!") 