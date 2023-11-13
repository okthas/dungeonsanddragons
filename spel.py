import random as rand

class spelare:
    def __init__(self):
        self.nivå = 1
        self.hp = 10
        self.styrka = rand.randint(0, 10)
        self.inventarie = []

def visa_stats(spelare):
    print(f"HP: {spelare.hp}")
    print(f"Nivå: {spelare.nivå}")
    print(f"Styrka: {spelare.styrka}")

def föremål_i_kista(spelare):
    vapen_nivå = rand.randint(0, spelare.styrka)
    styrke_bonus = rand.randint(1, 5)
    vapen = f"Vapen nivå {vapen_nivå} med styrkebonus {styrke_bonus}"
    
    spelare.inventarie.append(vapen)
    spelare.styrka += styrke_bonus
    
    print(f"Du har fått ett nytt vapen: {vapen}!")

spelare = spelare()

while spelare.hp >= 0:        
    print(
            """

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            
            """)
        
    val = input("Vad vill du göra? (1, 2 eller 3) ")

    if val == "1":
        händelse = rand.randint(1, 3)
        if händelse == 1:
            monster_styrka = rand.randint(1, 10) + 2 * spelare.nivå
            print(f"""

                  Du har mått ett monster!  
                  Monsterstyrka: {monster_styrka}

                    """)
            spelare.hp = spelare.hp - monster_styrka/spelare.styrka
            xp = monster_styrka/spelare.nivå
            print(f"Du har fått {xp} xp")
        elif händelse == 2:
            föremål_i_kista(spelare)
        elif händelse == 3:
            fälla_skada = rand.randint(1, 4)
            spelare.hp = spelare.hp - fälla_skada
            print(f"Du har hamnat i en fälla och har förlorat {fälla_skada} HP!")
    elif val == "2":
        print(spelare.inventarie)
    elif val == "3":
        visa_stats(spelare)
    else:
        print("Välj 1, 2 eller 3!")

