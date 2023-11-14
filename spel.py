import random as rand

class spelare:
    def __init__(self):
        self.nivå = 1
        self.hp = 10
        self.styrka = 10
        self.inventarie = []

class Item:
    def __init__(self):
        self.name = rand.choice(["Svärd", "Sköld", "Pilbåge"])
        self.styrka_bonus = rand.randint(1, 5)

def visa_stats(spelare):
    print(f"HP: {spelare.hp}")
    print(f"Nivå: {spelare.nivå}")
    print(f"Styrka: {spelare.styrka}")

def föremål_i_kista(spelare):
    föremål = Item()
    spelare.inventarie.append(föremål)
    spelare.styrka += föremål.styrka_bonus
    
    print(f"Du har fått ett nytt vapen: {föremål.name}!")
    print(f"Din styrka har ökat med {föremål.styrka_bonus}")

def monster_strid():
    monster_styrka = rand.randint(1, 10) + spelare.nivå
    monster = rand.choice(["Golem", "Goblin"])
    print(f"""

        Du har mött en {monster}!  
        Monsterstyrka: {monster_styrka}

            """)
    spelare.hp = spelare.hp - int(monster_styrka/spelare.styrka)
    xp = monster_styrka/spelare.nivå
    print(f"Du har fått {xp} xp")
    summa_xp = 0
    summa_xp += xp
    if summa_xp >= 10:
        spelare.nivå += 1
        print(f"Du har gått upp i nivå till {spelare.nivå}!")

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
            monster_strid()
            if spelare.hp <= 0:
                print("Du död")
        elif händelse == 2:
            föremål_i_kista(spelare)
            if len(spelare.inventarie) > 4:
                try:
                    print("Ditt inventarie är fullt! Välj något att byta ut!")
                    for föremål in spelare.inventarie:
                        print(f"{föremål.name} med styrka bonus {föremål.styrka_bonus}")
                    ta_bort_index = int(input("Ta bort index: "))
                    index = spelare.inventarie[ta_bort_index]
                    spelare.inventarie.remove(index)
                except:
                    print("Välj ett index som finns i listan!")
        elif händelse == 3:
            fälla_skada = rand.randint(1, 4)
            spelare.hp = spelare.hp - fälla_skada
            print(f"Du har hamnat i en fälla och har förlorat {fälla_skada} HP!")
            if spelare.hp <= 0:
                print("Du är död!!!")
    elif val == "2":
        for föremål in spelare.inventarie:
            print(f"{föremål.name} med styrka bonus {föremål.styrka_bonus}")
    elif val == "3":
        visa_stats(spelare)
    else:
        print("Välj 1, 2 eller 3!")

