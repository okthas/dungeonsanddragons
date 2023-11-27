import random as rand
from delay_print import *

def trap(player, dmg_multiplier, trap_multiplier):
    print("""
                A trap!
          """)
    y = rand.randint(0,trap_multiplier+1)
    if y == 0:
        trap_damage = 0.5/dmg_multiplier*rand.randint(0, 2) + 0.6*player.level
        player.hp -= trap_damage
        print(f"""
You have been caught in the trap and lost {round(trap_damage,2)} HP!""")
    else:
        print("""
You managed to dodge the trap!""")
        trap_multiplier -= 1
    if player.hp <= 0:
        delay_print("""
                            
                You died
              
              """)

