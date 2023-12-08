import random as rand
class Monster:
    def __init__(self, player):
        self.Attribute = 0
        a = rand.randint(0,round(300/player.level,0))
        b = rand.randint(0,30)
        if a == 2:
            if player.level < 10:
                self.type = "Nothing?"
                self.monster_strength = 0
                self.monster_hp = 0
            else: 
                self.Attribute = "Last boss"
                self.type = "Wait... Is that?"
                self.monster_strength = 100
                self.monster_hp = 100
        elif b == 21:
            self.type = "Mimic"
            self.monster_strength = 30 + player.level*2.3
            self.monster_hp = 25 + player.level*1.7
            self.resist = "Ice"
        else:
            self.type = rand.choice(["Golem", "Goblin", "Dragon", "Rat", "Slime"])
            if self.type == "Golem":
                self.monster_strength = 9 + player.level*1.5
                self.monster_hp = 20 + player.level*2.9
                self.resist = "Ice"
            elif self.type == "Goblin":
                self.monster_strength = 4 + player.level*1.6
                self.monster_hp = 5 + player.level*1.7
                self.resist = None
            elif self.type == "Rat":
                self.monster_strength = 3 + player.level*1.5
                self.monster_hp = 2 + player.level*1
                self.resist = None
            elif self.type == "Slime":
                self.monster_strength = 1 + player.level*0.5
                self.monster_hp = 7 + player.level*2.7
                c = rand.randint(0,0)
                if c == 0:
                    self.resist = "Ice"
                else:
                    self.resist = "Fire"
            elif self.type == "Dragon":
                self.monster_strength = 33 + player.level*2.7
                self.monster_hp = 35 + player.level*3.2
                self.resist = "Fire"
        self.experience_x = self.monster_strength + self.monster_hp
        self.experience_value = self.experience_x*0.5
