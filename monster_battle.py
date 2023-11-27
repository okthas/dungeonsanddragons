import random as rand
from Monster import *
from delay_print import *
from item_in_mimic_chest import *
def monster_battle(player, dmg_multiplier, trap_multiplier):
    monster = Monster(player)
    if monster.type == "Nothing?" or monster.type == "Wait... Is that?":
        print(f"""
                You have encountered... {monster.type}?
                Monster hp: {round(monster.monster_hp,2)}   
                Monster strength: {round(monster.monster_strength,2)}

            """)
    else:
        print(f"""
                You have encountered a {monster.type}!
                Monster hp: {round(monster.monster_hp,2)}   
                Monster strength: {round(monster.monster_strength,2)}

            """)
    while monster.monster_hp > 0:
        print(f"""
                
                1. Attack
                2. Flee

        """)
        choose = input("Attack or flee?  ")
        if choose == "1":
            while monster.monster_hp > 0:
                monster.monster_hp -= player.strength
                if monster.monster_hp <= 0:
                    player.hp -= 2*player.level/dmg_multiplier*monster.monster_strength/player.hp_max
                    break
                player.hp -= monster.monster_strength/dmg_multiplier
            if player.hp <= 0:
                    print("""
                          
                You died
                          
                          """)
                    exit()
            if monster.monster_hp <= 0:
                if monster.Attribute == "Last boss":
                    print("""





                                                    I
                                                    I
                                                    I    
                                                    I
                                                    I
                                                    I
____________________________________________________I """)
                    input("Which door should I choose... ")
                    if player.name == "Marie":
                        delay_print("""
                                
                            Marie... 
                          
                            Wake up.

                          """)
                    else:
                        delay_print("""
                                
                            I hear someone... 
                          
                            What are they saying?

                          """)
                    exit()
                xp = monster.experience_value
                player.experience += xp
                trap_multiplier += 1
                print(f"You have slain the {monster.type} and received {round(xp,2)} experience!")
                while player.experience >= 24 + player.level**1.9:
                    print(f"""
___________________________________________________

        Your level has increased!
Level: {player.level} -> {player.level+1}
Max HP: {round(player.hp_max,2)} -> {round(player.hp_max+1+0.7*player.level+0.7,2)}
STR: {round(player.strength,2)} -> {round(player.strength+1+0.4*player.level+0.4,2)}                         

___________________________________________________
""")
                    player.experience -= 24 + player.level**1.9
                    player.level += 1
                    player.hp_max += 1 + 0.7*player.level
                    player.strength += 1  + 0.4*player.level
                if monster.type == "Mimic":
                    item_in_mimic_chest(player)
                    
                

        else:
            print("You fled!")
            break

    return player
