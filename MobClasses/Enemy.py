from MobClasses.Mob import Mob

class Enemy(Mob):
    def __init__(self,charecteristics):
        MobChar={            
            "pos":charecteristics["pos"],
            "size":charecteristics["size"],
            "color":[255,0,0],
            "speed":charecteristics["speed"],
            "health":charecteristics["health"],
            "screen":charecteristics["screen"]
        }
        super().__init__(MobChar)

        # def __init__(self,pos,size,color,speed,health,screen):
