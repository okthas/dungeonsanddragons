def display_stats(player, dmg_multiplier):
    print()
    if dmg_multiplier == 1:
        print("Difficulty: Hard")
    elif dmg_multiplier == 1.5:
        print("Difficulty: Medium")
    elif dmg_multiplier == 3:
        print("Difficulty: Easy")
    else:
        print(f"Difficulty: Custom({dmg_multiplier})")
    print(f"Name: {player.name}")
    print(f"Experience: {round(player.experience,2)}/{round(24 + player.level**1.9,2)}")
    print(f"Level: {player.level}")
    print(f"Strength: {round(player.strength,2)}")
    print(f"HP: {round(player.hp,2)}/{round(player.hp_max,2)}")