import pygame
from MobClasses.Rectangle import Rectangle

def lerp(a,b,t):
    return a + (b-a) * t

def colorLerp(b,t):
    currentColor = [0,255,0]
    wantedColor = b
    newColor = [
      lerp(currentColor[0],wantedColor[0],t),
      lerp(currentColor[1],wantedColor[1],t),
      lerp(currentColor[2],wantedColor[2],t)
    ]
    return newColor

lastHit = pygame.time.get_ticks()

class Mob(Rectangle):
    def __init__(self,mobChar):
        self.speed=mobChar["speed"]
        super().__init__(
            mobChar["size"],
            mobChar["pos"],
            mobChar["color"],
            0,
            mobChar["screen"]
        )


    def Move(self,dx,dy,):
        before = self.pos[0]
        self.pos[0]+=dx*self.speed
        self.pos[1]+=dy*self.speed
        # print("bx: "+str(before)+" | ax: "+str(self.pos[0]))
        self.obj = pygame.draw.rect(self.window, self.color, [self.pos[0], self.pos[1], self.size[0], self.size[1]])
        # consider collisionDetect()

    def Take_Damage(self,damage):
        self.health-=damage
        self.color=colorLerp([255,0,0],1-self.health/100)

    def collisionDetect(object): #object should be a Rectangle object
        global lastHit
        currentHit = pygame.time.get_ticks()
        if currentHit - lastHit < 250:
            return
        if self.obj.colliderect(object):
            # print("the player has been damaged!")
            # lastHit=currentHit
            # player1.Take_Damage(10)
            print(str(self.obj)+" has collided with "+str(object))
            return True
        else:
            return False