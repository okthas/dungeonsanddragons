def show_inventory(player,Artifact):
    if Artifact:
        for item in player.Artifact_pouch:
            print(item.name)
        Artifact = False
        return None
    if player.inventory == []:
       print("Nothing...")
       return None
    for item in player.inventory:
        if item.Attribute == "Strength bonus":
            print(f"{item.name} with strength bonus {round(item.strength_bonus,2)}!")
        else:
            print(f"{item.name} with health bonus {round(item.health_bonus,2)}!") 