import pygame, sys
from pygame.locals import *
import time

class Tester:
    def __init__(self,img,param):
        self.param=param
        self.x = -160
        self.y = 50
        self.img=pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (150, 50))
        self.soundObj = pygame.mixer.Sound('beep.mp3')
        #self.rec = rect(250,250,(20,50),(0,0,255))
    def background(self,screen):
        bg=pygame.image.load("jll.png").convert_alpha()
        bg = pygame.transform.scale(bg, (self.param.width, self.param.hight))
        screen.blit(bg,(0,0))
    def animate(self,screen):
        if (self.x >= self.param.width and self.y ==50):
            self.x = -160
            self.y = 420
        elif (self.x >= self.param.width and self.y ==420):
            self.x = -160
            self.y = 50
        self.x+=self.param.vitesse
        screen.blit(self.img,(self.x,self.y))
        #self.rec.drawRect(screen)
    def getEvent(self,event):
        if event.type == KEYDOWN:

            self.soundObj.play()
            #time.sleep(1) # wait and let the sound play for 1 second
            #soundObj.stop()

            if event.key == K_UP:
                self.y  -= 50;
                return True
        if event.type == KEYUP:
            if event.key == K_UP:
                self.y  += 50;

    def backgroundsound(self):
        pygame.mixer.music.load('MyImmortal.mp3')
        pygame.mixer.music.play(-1, 0.0)
    def beepsound(self):
        soundObj = pygame.mixer.Sound('beep.mp3')
        soundObj.play()

        time.sleep(1) # wait and let the sound play for 1 second
        soundObj.stop()
