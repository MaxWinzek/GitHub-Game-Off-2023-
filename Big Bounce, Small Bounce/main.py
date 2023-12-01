import pygame
import sys
import random
import pygame_widgets
from pygame_widgets.slider import Slider
import time
#Test

class Teleporter(pygame.sprite.Sprite):
    def __init__(self,posx,posy,group,size,RiftMaker_instance,rotation,is_firstPart):
        super().__init__(group)
        self.rift_maker_instance = RiftMaker_instance
        self.rift_maker_instance.TPs.append(self)
        self.posx = posx
        self.posy = posy
        self.size = size
        self.image = pygame.image.load("Teleporter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size,15))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(center = (self.posx,self.posy)) #680
        self.hitbox = pygame.Rect(self.rect)
        self.is_Spike = False
        self.is_TP = True
        self.first_part = is_firstPart
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5

    def update(self):
        self.rect.center += self.direction * self.speed
        self.hitbox = pygame.Rect(self.rect)
        screen.blit(self.image, self.rect.topleft)
        
        
class Floor(pygame.sprite.Sprite):
    def __init__(self,posx,group,RiftMaker_instance):
        super().__init__(group)
        self.rift_maker_instance = RiftMaker_instance
        self.rift_maker_instance.grounds.append(self)
        self.posx = posx
        self.image = pygame.image.load("Boden.png").convert_alpha()
        self.rect = self.image.get_rect(center = (self.posx,700))
        self.hitbox = pygame.Rect(self.rect)
        self.is_Spike = False
        self.is_TP = False
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        
    def update(self):
        self.rect.center += self.direction * self.speed
        screen.blit(self.image, self.rect.topleft)
                
class Laser(pygame.sprite.Sprite):
    def __init__(self,posx,posy,group,rotation):
        super().__init__(group)
        
        self.image = pygame.image.load("Laser.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(center = (posx,posy))
        self.hitbox = pygame.Rect(self.rect)
        self.is_Spike = True
        self.is_TP = False
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        
    def update(self):
        self.rect.center += self.direction * self.speed
        self.hitbox = pygame.Rect(self.rect)
        screen.blit(self.image, self.rect.topleft)
                
    
class RiftMaker():
    def __init__(self):
        #self.posx = 0
        self.objects = []
        self.grounds = []
        self.TPs = []
       
        self.objects.append(Floor(0,all_sprites,self))
        self.objects.append(Floor(self.grounds[-1].posx+500,all_sprites,self))
        self.objects.append(Floor(self.grounds[-1].posx+500,all_sprites,self))
            
            
    def hindernis1(self,x):
        self.objects.append(Floor(x,all_sprites,self))
        self.objects.append(Laser(x+300,150,all_sprites,0))
        self.objects.append(Laser(x+300,600,all_sprites,0))
        self.objects.append(Floor(x+500,all_sprites,self))
        self.objects.append(Floor(x+1000,all_sprites,self))
        
    def hindernis2(self,x):
        self.objects.append(Floor(x,all_sprites,self))
        self.objects.append(Teleporter(x,680,all_sprites,80,self,0,True))
        self.objects.append(Teleporter(x+200,680,all_sprites,80,self,0,False))
        self.objects.append(Laser(x+200,640,all_sprites,90))
        self.objects.append(Floor(x+500,all_sprites,self))
        self.objects.append(Floor(x+1000,all_sprites,self))
        
    def hindernis3(self,x):
        self.objects.append(Floor(x,all_sprites,self))
        self.objects.append(Floor(x+500,all_sprites,self))
        self.objects.append(Laser(x+250,650,all_sprites,0))
        self.objects.append(Laser(x+750,650,all_sprites,0))
        self.objects.append(Floor(x+1000,all_sprites,self))
        self.objects.append(Floor(x+1500,all_sprites,self))

        
    def hindernis4(self,x):
        self.objects.append(Floor(x,all_sprites,self))
        self.objects.append(Floor(x+500,all_sprites,self))
        self.objects.append(Laser(x+750,100,all_sprites,0))
        self.objects.append(Laser(x+750,200,all_sprites,0))
        self.objects.append(Laser(x+750,300,all_sprites,0))
        self.objects.append(Laser(x+750,400,all_sprites,0))
        self.objects.append(Laser(x+750,500,all_sprites,0))
        self.objects.append(Laser(x+750,600,all_sprites,0))
        self.objects.append(Teleporter(x+730,300,all_sprites,300,self,90,True))
        self.objects.append(Teleporter(x+900,680,all_sprites,80,self,0,False))
        self.objects.append(Floor(x+1000,all_sprites,self))
        self.objects.append(Floor(x+1500,all_sprites,self))
        
    def hindernis5(self,x):
        self.objects.append(Floor(x,all_sprites,self))
        self.objects.append(Laser(x,600,all_sprites,0))
        self.objects.append(Laser(x+500,600,all_sprites,0))
        self.objects.append(Laser(x+500,500,all_sprites,0))
        self.objects.append(Floor(x+500,all_sprites,self))
        self.objects.append(Floor(x+1000,all_sprites,self))

        
    def hindernis6(self,x):
        self.objects.append(Floor(x,all_sprites,self))
        self.objects.append(Laser(x,600,all_sprites,90))
        self.objects.append(Laser(x+100,600,all_sprites,90))
        self.objects.append(Laser(x+200,600,all_sprites,90))
        self.objects.append(Laser(x+300,600,all_sprites,90))
        self.objects.append(Floor(x+500,all_sprites,self))
        self.objects.append(Floor(x+1000,all_sprites,self))
                    
    def appendList(self):
        if self.grounds[-1].rect.center[0]<width:

            
            self.Zufall = random.randint(1,6)

            if self.Zufall == 1:
                self.hindernis1(self.grounds[-1].rect.center[0])
            if self.Zufall == 2:
                self.hindernis2(self.grounds[-1].rect.center[0])
            if self.Zufall == 3:
                self.hindernis3(self.grounds[-1].rect.center[0])
            if self.Zufall ==4:
                self.hindernis4(self.grounds[-1].rect.center[0])
            if self.Zufall == 5:
                self.hindernis5(self.grounds[-1].rect.center[0])
            if self.Zufall == 6:
                self.hindernis6(self.grounds[-1].rect.center[0])
                
            self.objects.pop(0)

    def update(self):
        self.appendList()
        all_sprites.update()
                

class Player():
    def __init__(self, pos):

        self.Radius = 30
        self.rect = pygame.draw.circle(screen, (128, 255, 0), (10, 10), self.Radius)
        self.pos = pygame.Vector2(pos)
        self.speed = 10
        self.direction = pygame.Vector2(0, 0)
        self.is_jumping = False
        self.start_jump = True
        self.kineticEnergy = 100
        self.hitbox = pygame.Rect(self.pos[0] - self.Radius // 2, self.pos[1] -  self.Radius // 2, self.Radius, self.Radius)
        
        self.TP_direction = pygame.math.Vector2(-1,0)
        self.TP_speed = 0
        
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.Radius += 10
            
            
            
        elif keys[pygame.K_d]:
            self.Radius -= 10

    def movement(self):
        if not self.is_jumping:
            self.direction.y = 1

        if self.is_jumping:
            if self.kineticEnergy > 0:
                self.direction.y = -1
                self.kineticEnergy -= 2
            else:
                self.is_jumping = False
                self.direction.y = 1
                

    def floor_collision(self):
        for Boden in RiftMaker.grounds:
            if self.hitbox.colliderect(Boden.rect):
                if self.start_jump == True:
                    for item in RiftMaker.objects:
                        item.direction.x = -1
                self.pos.y = 690 - self.Radius
                self.direction.y *= -1
                self.is_jumping = True
                self.kineticEnergy =  0.5*self.Radius
                if self.kineticEnergy >=100:
                    self.kineticEnergy = 100

    def Spike_collision(self):
        for item in RiftMaker.objects:
            if item.is_Spike == True:
                if self.hitbox.colliderect(item.hitbox):
                    pygame.mixer.Sound.play(LaserSound)
                    RiftMaker.objects.clear()
                    RiftMaker.grounds.clear()
                    RiftMaker.TPs.clear()

                    all_sprites.empty()
                    
                    RiftMaker.objects.append(Floor(0,all_sprites,RiftMaker))
                    RiftMaker.objects.append(Floor(RiftMaker.grounds[-1].posx+500,all_sprites,RiftMaker))
                    RiftMaker.objects.append(Floor(RiftMaker.grounds[-1].posx+500,all_sprites,RiftMaker))
                    global game_over
                    game_over = True

                    global hint1
                    if hint1 == True:
                        hint1 = False
                    else:
                        hint1 = True
                    
    def Teleporter_collision(self):
        for item in RiftMaker.objects:
            if item.is_TP == True and item.first_part == True:
                if item.size>= self.Radius*2:
                    if self.hitbox.colliderect(item.hitbox):
                        pygame.mixer.Sound.play(TP)
                        self.pos.y = 670-self.Radius
                        self.item_pos = RiftMaker.TPs.index(item)
                        increment = RiftMaker.TPs[self.item_pos+1].posx-RiftMaker.TPs[self.item_pos].posx                                                                                                                                            
                        for item in RiftMaker.objects:
                            item.rect.center =  (item.rect.center[0] - increment-self.Radius, item.rect.center[1])

    def update(self):

        self.input()
        self.Radius = max(10, min(self.Radius, 1280 // 2, 720 // 2))
        self.floor_collision()
        self.Spike_collision()
        self.Teleporter_collision()
        self.movement()
        self.pos += self.direction * self.speed
        pygame.draw.circle(screen, (57,166,163), self.pos, self.Radius)
        self.hitbox = pygame.Rect(self.pos[0] - self.Radius // 2, self.pos[1] -  self.Radius // 2, self.Radius, self.Radius)


        
        
global width
global height
width, height = 1280,720


pygame.init()
infoObject = pygame.display.Info()
myfont = pygame.font.SysFont("IMPACT", 60)

# render text

#Gruppen
all_sprites = pygame.sprite.Group()

#Canvas
screen = pygame.display.set_mode((width, height))

#constanten
Sky = pygame.image.load("Background.png")
Mountains = pygame.image.load("Mountain.png")
Sonne = pygame.image.load("Sonne.png")
StartScreen = pygame.image.load("TitleScreen.png")
Hint1 = pygame.image.load("Hint1.png")
Hint2 = pygame.image.load("Hint2.png")

Music = pygame.mixer.Sound("Noice.mp3")
TP = pygame.mixer.Sound("TP.mp3")
LaserSound = pygame.mixer.Sound("Laser.mp3")
pygame.mixer.Sound.play(Music)

#globale Variabeln
global scrollx
scrollx = 0
global game_over
game_over = True
score = 2000

global hint1
hint1 = True

#Objekte initialisieren
clock = pygame.time.Clock()
RiftMaker = RiftMaker()
player = Player((width//2, 60))
#all_sprites.add(player)
while True:
    while game_over == True:
        
        screen.blit(StartScreen,(0,0))
        label = myfont.render("SCORE: "+str(score-2000), 1, (217,0,41))
        screen.blit(label, (950, 100))
        if hint1 == True:
            screen.blit(Hint1,(830,160))
        else:
            screen.blit(Hint2,(830,160))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            score = 0
            game_over = False
            
        pygame.display.update()
        clock.tick(60)
    
    
    while game_over == False:

         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            
        screen.blit(Sky, (0, 0))
        screen.blit(Sonne,(250,-250))
        screen.blit(Mountains,(250,-180))
        score = RiftMaker.grounds[-1].posx
        label = myfont.render("SCORE: "+str(score-2000), 1, (217,0,41))
        screen.blit(label, (width//2-100, 10))

        player.update()
        RiftMaker.update()
    

        pygame.display.update()
        clock.tick(60)

