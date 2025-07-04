import pygame
from MobClasses.Rectangle import Rectangle
from MobClasses.Mob import Mob
from MobClasses.Player import Player
from MobClasses.Enemy import Enemy
import random
#===========================================================

# [Initialize Pygame]
pygame.init() 
screen_x=1535
screen_y=780
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Deadly Sky")
clock = pygame.time.Clock()
running = True
global game_time
game_time=0
global enemies
enemies=0
sky=(0,0,0)
global score
score=0
times=10

playerPos = {"x":50,"y":50}
enemyPos = {"x":250,"y":50}

#future TODO: Have Rectangle objects initialized outside of the loop
        #Have a "Mob" class which inherits Rectangle, but adds more methods such as Mob.Move()

#===========================================================

# # [collission callback]
# lastHit = pygame.time.get_ticks()
# def collisionDetect(object): #object should be a Rectangle object
#     global lastHit
#     currentHit = pygame.time.get_ticks()
#     if currentHit - lastHit < 250:
#         return
#     if player1.obj.colliderect(object):
#         print("the player has been damaged!")
#         lastHit=currentHit
#         player1.Take_Damage(10)

def reward():
    player1.health=100
    player1.Take_Damage(0)
    player1.pos=[0,player1.pos[1]]
    player1.speed=player1.speed*0.5+0.5

    enemylist.clear()
    for i in range(round(game_time/1000)):
        if len(enemylist)>10:
            enemies-=1

def player_update():
    global score

    key=pygame.key.get_pressed()
    player1.Move(0,0)
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player1.Move(-2,0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player1.Move(2,0)
    if key[pygame.K_UP] or key[pygame.K_w]:
        player1.Move(0,-2)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        player1.Move(0,2)
    
    if player1.pos[0]<0:
        player1.pos=[0,player1.pos[1]]
    if player1.pos[1]<0:
        player1.pos=[player1.pos[0],0]
    if player1.pos[1]>screen_y-player1.size[1]:
        player1.pos=[player1.pos[0],screen_y-player1.size[1]]
    if player1.pos[0]>screen_x:
        reward()
        score+=1

def enemy_update():
    for enemy in enemylist:
        enemy.Move(random.randint(-round(game_time/1200),round(game_time/1200)),random.randint(-round(game_time/1200),round(game_time/1200)))
        # if player.collisionDetect(enemy.obj):
        #     //player.takeDamagE(stuff)
        #wanted: if player1.collissionDetect(enemy.obj):
        #TODO: refactor collisionDetect to be a method of the Mob class


#===========================================================

    # [Initialize players/enemies]

characteristics ={
    "pos": [0,screen_y/2],
    "size":[5,5],
    "screen": screen,
}
player1 = Player(characteristics)
enemylist=[]
for i in range(5):
    enemies+=1

# Game loop
while running:
    sky=(0,0,score*(255/times))
    game_time+=1
    if game_time % 10==0:
        try:
            screen.fill(sky)
        except:
            pass

    if len(enemylist)<enemies:
        characteristics ={
        "pos": [random.randint(0,screen_x),random.randint(0,screen_y)],
        "size":[random.randint(round(10/round((game_time+20000)/20000)),round(50/round((game_time+20000)/20000))),random.randint(round(10/round((game_time+20000)/20000)),round(50/round((game_time+20000)/20000)))],
        "speed": random.randint(0,1)-0.5,
        "health": 1,
        "screen": screen,
        }

        enemylist.append( Enemy(characteristics))
    
    if len(enemylist)>enemies:
        enemylist.pop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # - - - - - - - -  -

    player_update()
    enemy_update()

       #detect collissions / damaging TODO: Debounce
    #- - - - - - - - - -
    pygame.display.flip()   #render
    clock.tick(60)          # Limit to 60 FPS
    
    if game_time%30==0:
        player1.health+=0.5
        enemies+=1


    if score==times:
        pygame.display.quit()
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((200, 100))
        screen.fill((0,0,255))
    

        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = my_font.render('You Win!', False, (0, 255, 0))
        screen.blit(text_surface, (0,0))
        pygame.display.flip()
        
        pygame.display.set_caption("Win!")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

    if player1.health>100:
        player1.health=100
    if player1.health<=0:
        pygame.display.quit()
        pygame.quit()
        pygame.init()
        screen = pygame.display.set_mode((200, 100))
        screen.fill(sky)
    

        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = my_font.render('You lose', False, (255, 0, 0))
        screen.blit(text_surface, (0,0))
        pygame.display.flip()
        
        pygame.display.set_caption("Lose")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
        print("You lose")
        break

# Quit Pygame 
pygame.quit()
