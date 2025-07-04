from MobClasses.Mob import Mob

class Player(Mob):
    def __init__(self,charecteristics):
        MobChar={
            "pos":charecteristics["pos"],
            "size":charecteristics["size"],
            "color":[0,255,0],
            "speed":0.75,
            "health":100,
            "screen":charecteristics["screen"]
        }
        super().__init__(MobChar)
    
    #consider arrow key / WASD methods?
    #def __init__(self,pos,size,color,speed,health,screen):
