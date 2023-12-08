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
                Monster resist: {monster.resist}

            """)
    while monster.monster_hp > 0:
        print(f"""
                
                1. Attack
                2. Flee

        """)
        choose = input("Attack or flee?  ")
        if choose == "1":
            f_bonus = 1
            i_bonus = 1
            if player.Artifact_pouch == []:
                None
            else:
                for item in player.Artifact_pouch:
                    if item.Artifact_ability == f"Enemies deal 30% less damage":
                        enemy_debuff = 0.65
                    if item.Artifact_ability == f"You gain 50% more fire elemental damage":
                        f_bonus = 1.5
                    if item.Artifact_ability == f"You gain 50% more ice elemental damage":
                        i_bonus = 1.5
            p_strength = player.strength
            for item in player.inventory:
                if item.Attribute == "Strength bonus":
                    if item.preset == "Frosty":
                        if monster.resist == "Ice":
                            p_strength -= item.strength_bonus
                        else:
                            p_strength += i_bonus*0.5*item.strength_bonus
                    if item.preset == "Spicy":
                        if monster.resist == "Fire":
                            p_strength -= item.strength_bonus
                        else:
                            p_strength += f_bonus*0.5*item.strength_bonus
                else:
                    None
            enemy_debuff = 1
            p_hp = player.hp
            while monster.monster_hp > 0:
                monster.monster_hp -= p_strength
                if monster.monster_hp <= 0:
                    oneshotmultiplier = 2*player.level/dmg_multiplier*monster.monster_strength/player.hp_max
                    player.hp -= enemy_debuff*oneshotmultiplier
                    break
                player.hp -= enemy_debuff*monster.monster_strength/dmg_multiplier
            p_hp2 = player.hp
            print(f"You lost {round(p_hp-p_hp2,2)} HP! You HP is now {round(player.hp,2)}")
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
Max HP: {round(player.hp_max,2)} -> {round(player.hp_max+1,2)}
STR: {round(player.strength,2)} -> {round(player.strength+1,2)}                         

___________________________________________________
""")
                    player.experience -= 24 + player.level**1.9
                    player.level += 1
                    player.hp_max += 1
                    player.strength += 1
                if monster.type == "Mimic":
                    item_in_mimic_chest(player)
                    
                

        else:
            print("You fled!")
            break

    return player
