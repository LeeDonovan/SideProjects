#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
textX = 5
textY = 5
#Setting up Fonts
font = pygame.font.SysFont("Broadway", 60)
font_small = pygame.font.SysFont("Algerian", 20)
game_over = font.render("Game Over", True, BLACK)

#Create a white screen 
Game = pygame.display.set_mode((400,600))
Game.fill(WHITE)
pygame.display.set_caption("Pac-Man In Space")

#Updates score while in game
def show_score(x,y):
    score = font_small.render("Score: " + str(SCORE), True, WHITE)
    Game.blit(score,(x,y))

#Create an Ally that Player can score on
class Ally(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Ally.png")
        self.image = pygame.transform.scale(self.image, (40,50))
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):#when ally hits bottom of screen it resets back to the top
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Enemy ends game if Player touches
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (70,68))
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):#when Enemy hits bottom of screen it resets back to top
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (50,60))
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
                   
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load("Space.png")
            self.rectBGimg = self.bgimage.get_rect()#sets size of background
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         Game.blit(self.bgimage, (self.bgX1, self.bgY1))
         Game.blit(self.bgimage, (self.bgX2, self.bgY2))
         
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
A1 = Ally()
 
back_ground = Background()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
allies = pygame.sprite.Group()
allies.add(A1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(A1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
    
    #Cycles through all occurring events   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 1     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    back_ground.update()
    back_ground.render()
 
    #Game.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    Game.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        Game.blit(entity.image, entity.rect)
        entity.move()
    #When Ally collides with Player, Player gets a point
    if pygame.sprite.spritecollideany(P1,allies):
        pygame.mixer.Sound('coin.wav').play(loops=1)
        SCORE+=2
        A1.rect.top = 0
        

    #If Player touches Enemy game ends
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.8)
          #Shows Game Over Screen    
          Game.fill(RED)
          Game.blit(game_over, (30,250))
          Game.blit(font_small.render("Score: " + str(SCORE),True,BLACK),(30,500))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(3)
          pygame.quit()
          sys.exit()        
    show_score(textX,textY)
    pygame.display.update()
    FramePerSec.tick(FPS)